from typing import Dict, List, Optional, Union, Sequence, Any

import bodosdk.models.job
from bodosdk.db.args_parser import parse_args
from bodosdk.interfaces import (
    IJobClient,
    IBodoWorkspaceClient,
    IS3Source,
    IGitRepoSource,
    IWorkspaceSource,
    ITextSource,
    ICluster,
)
from bodosdk.models.job import TextSource, JobFilter


class JobClient(IJobClient):
    _deprecated_methods: Dict

    def __init__(self, workspace_client: IBodoWorkspaceClient):
        self._workspace_client = workspace_client

    @property
    def JobRun(self) -> bodosdk.models.job.JobRun:
        return bodosdk.models.job.JobRun(self._workspace_client)

    @property
    def JobRunList(self) -> bodosdk.models.job.JobRunList:
        return bodosdk.models.job.JobRunList(self._workspace_client)

    def run(
        self,
        template_id: str = None,
        cluster: Union[dict, ICluster] = None,
        code_type: str = None,
        source: Union[
            dict, IS3Source, IGitRepoSource, IWorkspaceSource, ITextSource
        ] = None,
        exec_file: str = None,
        exec_text: str = None,
        args: Union[Sequence[Any], Dict, str] = None,
        env_vars: dict = None,
        timeout: int = None,
        num_retries: int = None,
        delay_between_retries: int = None,
        retry_on_timeout: bool = None,
        name: str = None,
        catalog: str = None,
        store_result: bool = None,
    ) -> bodosdk.models.job.JobRun:
        if isinstance(cluster, dict):
            cluster = self._workspace_client.ClusterClient.Cluster(**cluster)
        if code_type == "SQL":
            new_query, args = parse_args(exec_text, args)
            exec_text = new_query or exec_text
        data = {
            "name": name,
            "job_template_id": template_id,
            "config": {
                "type": code_type,
                "source": source,
                "exec_file": exec_file,
                "exec_text": exec_text,
                "args": args if code_type != "SQL" else None,
                "sql_query_parameters": args if code_type == "SQL" else None,
                "store_result": store_result
                if store_result is not None
                else code_type == "SQL",
                "env_vars": env_vars,
                "timeout": timeout,
                "catalog": catalog,
            },
        }
        if (
            num_retries is not None
            or delay_between_retries is not None
            or retry_on_timeout is not None
        ):
            data["config"]["retry_strategy"] = {
                "num_retries": num_retries,
                "delay_between_retries": delay_between_retries,
                "retry_on_timeout": retry_on_timeout,
            }
        if cluster and cluster.id:
            data["cluster_id"] = cluster.id
        else:
            data["cluster_config"] = cluster
        job = self.JobRun(**data)
        return job._save()

    def run_sql_query(
        self,
        template_id: str = None,
        catalog: str = None,
        sql_query: str = None,
        cluster: Union[dict, ICluster] = None,
        name: str = None,
        args: Union[Sequence[Any], Dict] = None,
        timeout: int = None,
        num_retries: int = None,
        delay_between_retries: int = None,
        retry_on_timeout: bool = None,
        store_result: bool = True,
    ) -> bodosdk.models.job.JobRun:
        if isinstance(cluster, dict):
            cluster = self._workspace_client.ClusterClient.Cluster(**cluster)
        new_query, args = parse_args(sql_query, args)
        sql_query = new_query or sql_query
        data = {
            "name": name,
            "job_template_id": template_id,
            "config": {
                "type": "SQL",
                "source": TextSource(),
                "exec_text": sql_query,
                "catalog": catalog,
                "sql_query_parameters": args,
                "timeout": timeout,
                "store_result": store_result,
            },
        }
        if (
            num_retries is not None
            or delay_between_retries is not None
            or retry_on_timeout is not None
        ):
            data["retry_strategy"] = {
                "num_retries": num_retries,
                "delay_between_retries": delay_between_retries,
                "retry_on_timeout": retry_on_timeout,
            }
        if cluster and cluster.id:
            data["cluster_id"] = cluster.id
        else:
            data["cluster_config"] = cluster
        job = self.JobRun(**data)
        return job._save()

    def get(self, id: str) -> bodosdk.models.job.JobRun:
        return self.JobRun(uuid=id)._load()

    def list(
        self,
        filters: Optional[Union[Dict, JobFilter]] = None,
        order: Optional[Dict] = None,
    ) -> bodosdk.models.job.JobRunList:
        return self.JobRunList(filters=filters, order=order)

    def cancel_job(self, id: str) -> bodosdk.models.job.JobRun:
        return self.JobRun(uuid=id).cancel()

    def cancel_jobs(
        self, filters: Optional[Union[Dict, JobFilter]] = None
    ) -> bodosdk.models.job.JobRunList:
        return self.JobRunList(filters=filters).cancel()

    def wait_for_status(
        self, id: str, statuses: List[str], timeout: int = 3600, tick: int = 30
    ) -> bodosdk.models.job.JobRun:
        return self.JobRun(uuid=id).wait_for_status(
            statuses=statuses, timeout=timeout, tick=tick
        )
