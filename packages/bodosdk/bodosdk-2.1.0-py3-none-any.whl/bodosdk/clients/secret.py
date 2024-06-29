from typing import Union

from bodosdk.interfaces import IBodoWorkspaceClient, ISecretClient
from bodosdk.models.secret import (
    SecretGroup,
    SecretGroupList,
    Secret,
    SecretList,
    SecretGroupFilter,
    SecretFilter,
)


class SecretClient(ISecretClient):
    def __init__(self, workspace_client: IBodoWorkspaceClient):
        self._workspace_client = workspace_client

    @property
    def SecretGroup(self) -> SecretGroup:
        return SecretGroup(self._workspace_client)

    @property
    def SecretGroupList(self) -> SecretGroupList:
        return SecretGroupList(self._workspace_client)

    @property
    def Secret(self) -> Secret:
        return Secret(self._workspace_client)

    @property
    def SecretList(self) -> SecretList:
        return SecretList(self._workspace_client)

    def list_secret_groups(
        self, filters: Union[dict, SecretGroupFilter] = None
    ) -> SecretGroupList:
        return self.SecretGroupList(filters=filters)

    def list_secrets(self, filters: Union[dict, SecretFilter] = None) -> SecretList:
        return self.SecretList(filters=filters)

    def get_secret(
        self,
        id: str,
    ) -> Secret:
        return self.Secret(uuid=id)._load()

    def create_secret(
        self,
        name: str,
        secret_type: str,
        data: dict,
        secret_group: SecretGroup,
    ) -> Secret:
        secret = self.Secret(
            secret_type=secret_type,
            name=name,
            data=data,
            secret_group=secret_group,
        )
        return secret._save()

    def delete_secret(self, id: str):
        self.Secret(uuid=id).delete()

    def create_secret_group(
        self,
        name: str,
        description: str,
    ) -> SecretGroup:
        sg = self.SecretGroup(
            name=name,
            description=description,
        )
        return sg._save()

    def delete_secret_group(self, name: str):
        self.SecretGroup(name=name).delete()
