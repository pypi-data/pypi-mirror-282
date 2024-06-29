# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetSyncAgentResult',
    'AwaitableGetSyncAgentResult',
    'get_sync_agent',
    'get_sync_agent_output',
]

@pulumi.output_type
class GetSyncAgentResult:
    """
    An Azure SQL Database sync agent.
    """
    def __init__(__self__, expiry_time=None, id=None, is_up_to_date=None, last_alive_time=None, name=None, state=None, sync_database_id=None, type=None, version=None):
        if expiry_time and not isinstance(expiry_time, str):
            raise TypeError("Expected argument 'expiry_time' to be a str")
        pulumi.set(__self__, "expiry_time", expiry_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_up_to_date and not isinstance(is_up_to_date, bool):
            raise TypeError("Expected argument 'is_up_to_date' to be a bool")
        pulumi.set(__self__, "is_up_to_date", is_up_to_date)
        if last_alive_time and not isinstance(last_alive_time, str):
            raise TypeError("Expected argument 'last_alive_time' to be a str")
        pulumi.set(__self__, "last_alive_time", last_alive_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if sync_database_id and not isinstance(sync_database_id, str):
            raise TypeError("Expected argument 'sync_database_id' to be a str")
        pulumi.set(__self__, "sync_database_id", sync_database_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="expiryTime")
    def expiry_time(self) -> str:
        """
        Expiration time of the sync agent version.
        """
        return pulumi.get(self, "expiry_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isUpToDate")
    def is_up_to_date(self) -> bool:
        """
        If the sync agent version is up to date.
        """
        return pulumi.get(self, "is_up_to_date")

    @property
    @pulumi.getter(name="lastAliveTime")
    def last_alive_time(self) -> str:
        """
        Last alive time of the sync agent.
        """
        return pulumi.get(self, "last_alive_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the sync agent.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="syncDatabaseId")
    def sync_database_id(self) -> Optional[str]:
        """
        ARM resource id of the sync database in the sync agent.
        """
        return pulumi.get(self, "sync_database_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of the sync agent.
        """
        return pulumi.get(self, "version")


class AwaitableGetSyncAgentResult(GetSyncAgentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSyncAgentResult(
            expiry_time=self.expiry_time,
            id=self.id,
            is_up_to_date=self.is_up_to_date,
            last_alive_time=self.last_alive_time,
            name=self.name,
            state=self.state,
            sync_database_id=self.sync_database_id,
            type=self.type,
            version=self.version)


def get_sync_agent(resource_group_name: Optional[str] = None,
                   server_name: Optional[str] = None,
                   sync_agent_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSyncAgentResult:
    """
    Gets a sync agent.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server on which the sync agent is hosted.
    :param str sync_agent_name: The name of the sync agent.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    __args__['syncAgentName'] = sync_agent_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230801preview:getSyncAgent', __args__, opts=opts, typ=GetSyncAgentResult).value

    return AwaitableGetSyncAgentResult(
        expiry_time=pulumi.get(__ret__, 'expiry_time'),
        id=pulumi.get(__ret__, 'id'),
        is_up_to_date=pulumi.get(__ret__, 'is_up_to_date'),
        last_alive_time=pulumi.get(__ret__, 'last_alive_time'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        sync_database_id=pulumi.get(__ret__, 'sync_database_id'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_sync_agent)
def get_sync_agent_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                          server_name: Optional[pulumi.Input[str]] = None,
                          sync_agent_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSyncAgentResult]:
    """
    Gets a sync agent.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server on which the sync agent is hosted.
    :param str sync_agent_name: The name of the sync agent.
    """
    ...
