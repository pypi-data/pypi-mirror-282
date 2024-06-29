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
    'GetNetworkConnectionResult',
    'AwaitableGetNetworkConnectionResult',
    'get_network_connection',
    'get_network_connection_output',
]

@pulumi.output_type
class GetNetworkConnectionResult:
    """
    Network related settings
    """
    def __init__(__self__, domain_join_type=None, domain_name=None, domain_password=None, domain_username=None, health_check_status=None, id=None, location=None, name=None, networking_resource_group_name=None, organization_unit=None, provisioning_state=None, subnet_id=None, system_data=None, tags=None, type=None):
        if domain_join_type and not isinstance(domain_join_type, str):
            raise TypeError("Expected argument 'domain_join_type' to be a str")
        pulumi.set(__self__, "domain_join_type", domain_join_type)
        if domain_name and not isinstance(domain_name, str):
            raise TypeError("Expected argument 'domain_name' to be a str")
        pulumi.set(__self__, "domain_name", domain_name)
        if domain_password and not isinstance(domain_password, str):
            raise TypeError("Expected argument 'domain_password' to be a str")
        pulumi.set(__self__, "domain_password", domain_password)
        if domain_username and not isinstance(domain_username, str):
            raise TypeError("Expected argument 'domain_username' to be a str")
        pulumi.set(__self__, "domain_username", domain_username)
        if health_check_status and not isinstance(health_check_status, str):
            raise TypeError("Expected argument 'health_check_status' to be a str")
        pulumi.set(__self__, "health_check_status", health_check_status)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if networking_resource_group_name and not isinstance(networking_resource_group_name, str):
            raise TypeError("Expected argument 'networking_resource_group_name' to be a str")
        pulumi.set(__self__, "networking_resource_group_name", networking_resource_group_name)
        if organization_unit and not isinstance(organization_unit, str):
            raise TypeError("Expected argument 'organization_unit' to be a str")
        pulumi.set(__self__, "organization_unit", organization_unit)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="domainJoinType")
    def domain_join_type(self) -> str:
        """
        AAD Join type.
        """
        return pulumi.get(self, "domain_join_type")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[str]:
        """
        Active Directory domain name
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="domainPassword")
    def domain_password(self) -> Optional[str]:
        """
        The password for the account used to join domain
        """
        return pulumi.get(self, "domain_password")

    @property
    @pulumi.getter(name="domainUsername")
    def domain_username(self) -> Optional[str]:
        """
        The username of an Active Directory account (user or service account) that has permissions to create computer objects in Active Directory. Required format: admin@contoso.com.
        """
        return pulumi.get(self, "domain_username")

    @property
    @pulumi.getter(name="healthCheckStatus")
    def health_check_status(self) -> str:
        """
        Overall health status of the network connection. Health checks are run on creation, update, and periodically to validate the network connection.
        """
        return pulumi.get(self, "health_check_status")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkingResourceGroupName")
    def networking_resource_group_name(self) -> Optional[str]:
        """
        The name for resource group where NICs will be placed.
        """
        return pulumi.get(self, "networking_resource_group_name")

    @property
    @pulumi.getter(name="organizationUnit")
    def organization_unit(self) -> Optional[str]:
        """
        Active Directory domain Organization Unit (OU)
        """
        return pulumi.get(self, "organization_unit")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The subnet to attach Virtual Machines to
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetNetworkConnectionResult(GetNetworkConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkConnectionResult(
            domain_join_type=self.domain_join_type,
            domain_name=self.domain_name,
            domain_password=self.domain_password,
            domain_username=self.domain_username,
            health_check_status=self.health_check_status,
            id=self.id,
            location=self.location,
            name=self.name,
            networking_resource_group_name=self.networking_resource_group_name,
            organization_unit=self.organization_unit,
            provisioning_state=self.provisioning_state,
            subnet_id=self.subnet_id,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_network_connection(network_connection_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkConnectionResult:
    """
    Gets a network connection resource


    :param str network_connection_name: Name of the Network Connection that can be applied to a Pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['networkConnectionName'] = network_connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20240501preview:getNetworkConnection', __args__, opts=opts, typ=GetNetworkConnectionResult).value

    return AwaitableGetNetworkConnectionResult(
        domain_join_type=pulumi.get(__ret__, 'domain_join_type'),
        domain_name=pulumi.get(__ret__, 'domain_name'),
        domain_password=pulumi.get(__ret__, 'domain_password'),
        domain_username=pulumi.get(__ret__, 'domain_username'),
        health_check_status=pulumi.get(__ret__, 'health_check_status'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        networking_resource_group_name=pulumi.get(__ret__, 'networking_resource_group_name'),
        organization_unit=pulumi.get(__ret__, 'organization_unit'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        subnet_id=pulumi.get(__ret__, 'subnet_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_network_connection)
def get_network_connection_output(network_connection_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkConnectionResult]:
    """
    Gets a network connection resource


    :param str network_connection_name: Name of the Network Connection that can be applied to a Pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
