# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetIscsiTargetResult',
    'AwaitableGetIscsiTargetResult',
    'get_iscsi_target',
    'get_iscsi_target_output',
]

@pulumi.output_type
class GetIscsiTargetResult:
    """
    Response for iSCSI Target requests.
    """
    def __init__(__self__, acl_mode=None, endpoints=None, id=None, luns=None, managed_by=None, managed_by_extended=None, name=None, port=None, provisioning_state=None, sessions=None, static_acls=None, status=None, system_data=None, target_iqn=None, type=None):
        if acl_mode and not isinstance(acl_mode, str):
            raise TypeError("Expected argument 'acl_mode' to be a str")
        pulumi.set(__self__, "acl_mode", acl_mode)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if luns and not isinstance(luns, list):
            raise TypeError("Expected argument 'luns' to be a list")
        pulumi.set(__self__, "luns", luns)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if managed_by_extended and not isinstance(managed_by_extended, list):
            raise TypeError("Expected argument 'managed_by_extended' to be a list")
        pulumi.set(__self__, "managed_by_extended", managed_by_extended)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sessions and not isinstance(sessions, list):
            raise TypeError("Expected argument 'sessions' to be a list")
        pulumi.set(__self__, "sessions", sessions)
        if static_acls and not isinstance(static_acls, list):
            raise TypeError("Expected argument 'static_acls' to be a list")
        pulumi.set(__self__, "static_acls", static_acls)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if target_iqn and not isinstance(target_iqn, str):
            raise TypeError("Expected argument 'target_iqn' to be a str")
        pulumi.set(__self__, "target_iqn", target_iqn)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="aclMode")
    def acl_mode(self) -> str:
        """
        Mode for Target connectivity.
        """
        return pulumi.get(self, "acl_mode")

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence[str]]:
        """
        List of private IPv4 addresses to connect to the iSCSI Target.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def luns(self) -> Optional[Sequence['outputs.IscsiLunResponse']]:
        """
        List of LUNs to be exposed through iSCSI Target.
        """
        return pulumi.get(self, "luns")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> str:
        """
        Azure resource id. Indicates if this resource is managed by another Azure resource.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> Sequence[str]:
        """
        List of Azure resource ids that manage this resource.
        """
        return pulumi.get(self, "managed_by_extended")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The port used by iSCSI Target portal group.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sessions(self) -> Sequence[str]:
        """
        List of identifiers for active sessions on the iSCSI target
        """
        return pulumi.get(self, "sessions")

    @property
    @pulumi.getter(name="staticAcls")
    def static_acls(self) -> Optional[Sequence['outputs.AclResponse']]:
        """
        Access Control List (ACL) for an iSCSI Target; defines LUN masking policy
        """
        return pulumi.get(self, "static_acls")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Operational status of the iSCSI Target.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemMetadataResponse':
        """
        Resource metadata required by ARM RPC
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetIqn")
    def target_iqn(self) -> str:
        """
        iSCSI Target IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:server".
        """
        return pulumi.get(self, "target_iqn")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")


class AwaitableGetIscsiTargetResult(GetIscsiTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIscsiTargetResult(
            acl_mode=self.acl_mode,
            endpoints=self.endpoints,
            id=self.id,
            luns=self.luns,
            managed_by=self.managed_by,
            managed_by_extended=self.managed_by_extended,
            name=self.name,
            port=self.port,
            provisioning_state=self.provisioning_state,
            sessions=self.sessions,
            static_acls=self.static_acls,
            status=self.status,
            system_data=self.system_data,
            target_iqn=self.target_iqn,
            type=self.type)


def get_iscsi_target(disk_pool_name: Optional[str] = None,
                     iscsi_target_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIscsiTargetResult:
    """
    Get an iSCSI Target.
    Azure REST API version: 2021-08-01.

    Other available API versions: 2020-03-15-preview.


    :param str disk_pool_name: The name of the Disk Pool.
    :param str iscsi_target_name: The name of the iSCSI Target.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['diskPoolName'] = disk_pool_name
    __args__['iscsiTargetName'] = iscsi_target_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storagepool:getIscsiTarget', __args__, opts=opts, typ=GetIscsiTargetResult).value

    return AwaitableGetIscsiTargetResult(
        acl_mode=pulumi.get(__ret__, 'acl_mode'),
        endpoints=pulumi.get(__ret__, 'endpoints'),
        id=pulumi.get(__ret__, 'id'),
        luns=pulumi.get(__ret__, 'luns'),
        managed_by=pulumi.get(__ret__, 'managed_by'),
        managed_by_extended=pulumi.get(__ret__, 'managed_by_extended'),
        name=pulumi.get(__ret__, 'name'),
        port=pulumi.get(__ret__, 'port'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sessions=pulumi.get(__ret__, 'sessions'),
        static_acls=pulumi.get(__ret__, 'static_acls'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        target_iqn=pulumi.get(__ret__, 'target_iqn'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_iscsi_target)
def get_iscsi_target_output(disk_pool_name: Optional[pulumi.Input[str]] = None,
                            iscsi_target_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIscsiTargetResult]:
    """
    Get an iSCSI Target.
    Azure REST API version: 2021-08-01.

    Other available API versions: 2020-03-15-preview.


    :param str disk_pool_name: The name of the Disk Pool.
    :param str iscsi_target_name: The name of the iSCSI Target.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
