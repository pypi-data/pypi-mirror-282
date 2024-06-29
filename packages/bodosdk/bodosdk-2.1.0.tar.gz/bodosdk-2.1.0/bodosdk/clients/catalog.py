from typing import Optional, Union

from bodosdk.interfaces import IBodoWorkspaceClient, ICatalogClient
from bodosdk.models import Catalog
from bodosdk.models.catalog import SnowflakeDetails, CatalogList


class CatalogClient(ICatalogClient):
    _deprecated_methods: dict

    def __init__(self, workspace_client: IBodoWorkspaceClient):
        self._workspace_client = workspace_client

    @property
    def Catalog(self) -> Catalog:
        return Catalog(self._workspace_client)

    @property
    def CatalogList(self) -> CatalogList:
        return CatalogList(self._workspace_client)

    def list(self, filters: dict = None) -> CatalogList:
        return self.CatalogList(filters=filters)

    def get(
        self,
        id: str,
    ) -> Catalog:
        return self.Catalog(uuid=id)._load()

    def create(
        self,
        name: str,
        catalog_type: str,
        details: Union[SnowflakeDetails, dict],
        description: Optional[str] = None,
    ):
        if isinstance(details, dict) and catalog_type == "SNOWFLAKE":
            details = SnowflakeDetails(**details)
        catalog = self.Catalog(
            catalog_type=catalog_type,
            name=name,
            description=description,
            details=details,
        )
        return catalog._save()

    def create_snowflake_catalog(
        self,
        name: str,
        details: Union[SnowflakeDetails, dict],
        description: Optional[str] = None,
    ):
        return self.create(name, "SNOWFLAKE", details, description)

    def delete(self, id: str):
        self.Catalog(uuid=id).delete()
