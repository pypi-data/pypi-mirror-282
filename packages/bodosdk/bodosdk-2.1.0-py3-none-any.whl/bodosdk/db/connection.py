import json
import os
from typing import Union, Any, Sequence, Dict
from uuid import uuid4

import requests

from bodosdk.db.downloader import DownloadManager
from bodosdk.db.exc import DatabaseError, NotSupportedError
from bodosdk.exceptions import TimeoutException
from bodosdk.interfaces import ICluster, IJobRun
import pyarrow.parquet as pq


class Cursor:
    def __init__(
        self, catalog: str, cluster: ICluster, timeout: int = 3600, query_id=None
    ):
        self._catalog = catalog
        self.cluster = cluster
        self._timeout = timeout
        self._current_row = None
        self._metadata = None
        self._results_urls = None
        self._file_index = 0
        self._results = []
        self._rows_stripped = 0
        self.uuid = uuid4()
        self._files = []
        if query_id:
            self._job = cluster._workspace_client.JobClient.JobRun(uuid=query_id)
        else:
            self._job: IJobRun = None

    def __enter__(self) -> "Cursor":
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __iter__(self):
        row = self.fetchone()
        while row:
            yield row
            row = self.fetchone()

    @property
    def rownumber(self):
        return self._current_row

    @property
    def rowcount(self):
        self._wait_for_finished_job()
        self._load_metadata()
        if self._results_urls:
            return self._metadata["num_rows"]

    def execute(self, query: str, args: Union[Sequence[Any], Dict] = None):
        self._results_urls = None
        self._file_index = 0
        self._current_row = None
        self._results = []
        self._rows_stripped = 0
        self._job = self.cluster.run_sql_query(
            catalog=self._catalog,
            sql_query=query,
            args=args,
            timeout=self._timeout,
            store_result=True,
        )
        self._wait_for_finished_job()
        self._load_metadata()
        return self

    def execute_async(self, query: str, args: Union[Sequence[Any], Dict] = None):
        self._results_urls = None
        self._file_index = None
        self._current_row = None
        self._results = []
        self._rows_stripped = 0
        self._job = self.cluster.run_sql_query(
            catalog=self._catalog, sql_query=query, args=args, store_result=True
        )
        return self

    def fetchone(self):
        self._wait_for_finished_job()
        self._load_metadata()
        if self._current_row >= self.rowcount:
            return None
        if self._current_row >= len(self._results) + self._rows_stripped:
            self._load_next_file()
        record = self._results[self._current_row - self._rows_stripped]
        self._current_row += 1
        return record

    def fetchmany(self, size):
        self._wait_for_finished_job()
        self._load_metadata()
        if self._current_row >= self.rowcount:
            return None
        results = list(self._results)
        while size > len(results):
            if self._load_next_file():
                results.extend(self._results)
            else:
                break
        data_to_return = results[max(self._current_row - self._rows_stripped, 0):size]
        self._results = list(
            results[max(self._current_row - self._rows_stripped, 0) + size:]
        )
        self._current_row += min(size, len(results))
        self._rows_stripped = self._current_row
        return list(data_to_return)

    def fetchall(self):
        self._wait_for_finished_job()
        self._load_metadata()
        results = []
        results.extend(self._results)
        while self._load_next_file():
            results.extend(self._results)
        self._current_row = self.rowcount
        return results

    def setinputsizes(self, sizes):
        pass

    def setoutputsize(self, size, column=None):
        pass

    def _load_metadata(self):
        if not self._results_urls:
            self._results_urls = self._job.get_result_urls()
            metadata_url = self._results_urls[0]
            response = requests.get(metadata_url)
            self._metadata = json.loads(response.content)
            self._file_index = 0
            self._current_row = 0
            self.download_manager = DownloadManager(
                self._job.uuid, self._results_urls[1:]
            )
            self._files.extend(
                self.download_manager.download_files(self.uuid, self._timeout)
            )

    def _load_next_file(self):
        filename = f"{self.uuid}-{self._job.uuid}-{self._file_index}.pq"
        try:
            df = pq.read_table(filename).to_pandas()
            data = list(df.to_records(index=False))
        except FileNotFoundError:
            return None
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass
        else:
            if filename in self._files:
                del self._files[self._files.index(filename)]
        self._rows_stripped += len(self._results)
        self._results = data
        self._file_index += 1
        return True

    def _wait_for_finished_job(self):
        try:
            self._job.wait_for_status(
                ["SUCCEEDED", "FAILED", "CANCELLED"], tick=10, timeout=self._timeout
            )
        except TimeoutException:
            raise DatabaseError("Query timed out")
        if self._job.status in ["FAILED", "CANCELLED"]:
            raise DatabaseError(
                f"Query failed due to {self._job.reason}. {self._job.get_stderr()}"
            )

    def close(self):
        self._results = []
        self._file_index = 0
        self._rows_stripped = 0
        self._metadata = None
        self._results_urls = None
        self._current_row = None
        for file in self._files:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass
        self._files = []

    @property
    def query_id(self):
        if self._job:
            return self._job.id


class Connection:
    def __init__(self, catalog: str, cluster: ICluster, timeout=3600):
        self._catalog = catalog
        self._cluster = cluster
        self._timeout = timeout
        self._cursors = {}

    def __enter__(self) -> "Connection":
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __del__(self):
        self.close()

    def cursor(self, query_id=None):
        c = Cursor(self._catalog, self._cluster, self._timeout, query_id)
        self._cursors[c.uuid] = c
        return c

    def commit(self):
        """
        No-op because Bodo does not support transactions: https://peps.python.org/pep-0249/#commit
        """
        pass

    def close(self):
        for c_uuid, curor in self._cursors.items():
            curor.close()
        self._cursors = {}

    def rollback(self):
        raise NotSupportedError("Transactions are not supported on Bodo")
