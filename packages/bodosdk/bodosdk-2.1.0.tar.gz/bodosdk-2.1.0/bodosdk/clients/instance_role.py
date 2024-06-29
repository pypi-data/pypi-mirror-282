from __future__ import annotations

from typing import Optional, Union, Dict

from bodosdk.interfaces import IBodoWorkspaceClient, IInstanceRoleClient
from bodosdk.models.instance_role import (
    InstanceRole,
    InstanceRoleList,
    InstanceRoleFilter,
)


class InstanceRoleClient(IInstanceRoleClient):
    _deprecated_methods: dict

    def __init__(self, workspace_client: IBodoWorkspaceClient):
        """
        Initializes the ClusterClient with a given workspace client.

        Args:
            workspace_client (IBodoWorkspaceClient): The workspace client to interact with the API.
        """
        self._workspace_client = workspace_client

    @property
    def InstanceRole(self) -> InstanceRole:
        return InstanceRole(self._workspace_client)

    @property
    def InstanceRoleList(self) -> InstanceRoleList:
        return InstanceRoleList(self._workspace_client)

    def list(
        self,
        filters: Optional[Union[Dict, InstanceRoleFilter]] = None,
        order: Optional[Dict] = None,
    ) -> InstanceRoleList:
        return self.InstanceRoleList(filters=filters, order=order)

    def get(
        self,
        id: str,
    ) -> InstanceRole:
        return self.InstanceRole(uuid=id)._load()

    def create(self, role_arn: str, description: str, name: str = None):
        return self.InstanceRole(
            role_arn=role_arn, name=name, description=description
        )._save()

    def delete(self, id: str):
        self.InstanceRole(uuid=id).delete()
