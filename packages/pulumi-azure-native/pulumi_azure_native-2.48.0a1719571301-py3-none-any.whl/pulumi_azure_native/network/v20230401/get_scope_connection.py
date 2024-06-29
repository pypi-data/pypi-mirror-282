# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetScopeConnectionResult',
    'AwaitableGetScopeConnectionResult',
    'get_scope_connection',
    'get_scope_connection_output',
]

@pulumi.output_type
class GetScopeConnectionResult:
    """
    The Scope Connections resource
    """
    def __init__(__self__, description=None, etag=None, id=None, name=None, resource_id=None, system_data=None, tenant_id=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the scope connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        Tenant ID.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetScopeConnectionResult(GetScopeConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScopeConnectionResult(
            description=self.description,
            etag=self.etag,
            id=self.id,
            name=self.name,
            resource_id=self.resource_id,
            system_data=self.system_data,
            tenant_id=self.tenant_id,
            type=self.type)


def get_scope_connection(network_manager_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         scope_connection_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScopeConnectionResult:
    """
    Get specified scope connection created by this Network Manager.


    :param str network_manager_name: The name of the network manager.
    :param str resource_group_name: The name of the resource group.
    :param str scope_connection_name: Name for the cross-tenant connection.
    """
    __args__ = dict()
    __args__['networkManagerName'] = network_manager_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['scopeConnectionName'] = scope_connection_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230401:getScopeConnection', __args__, opts=opts, typ=GetScopeConnectionResult).value

    return AwaitableGetScopeConnectionResult(
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_scope_connection)
def get_scope_connection_output(network_manager_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                scope_connection_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScopeConnectionResult]:
    """
    Get specified scope connection created by this Network Manager.


    :param str network_manager_name: The name of the network manager.
    :param str resource_group_name: The name of the resource group.
    :param str scope_connection_name: Name for the cross-tenant connection.
    """
    ...
