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
    'GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult',
    'AwaitableGetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult',
    'get_private_endpoint_connection_controller_private_endpoint_connection',
    'get_private_endpoint_connection_controller_private_endpoint_connection_output',
]

@pulumi.output_type
class GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult:
    """
    REST model used to encapsulate the user visible state of a PrivateEndpoint.
    """
    def __init__(__self__, e_tag=None, id=None, name=None, properties=None, system_data=None, type=None):
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        Gets the tag for optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Relative URL to get this Sites.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.PrivateEndpointConnectionPropertiesResponse':
        """
        Gets the properties of the object.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult(GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult(
            e_tag=self.e_tag,
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_private_endpoint_connection_controller_private_endpoint_connection(migrate_project_name: Optional[str] = None,
                                                                           pe_connection_name: Optional[str] = None,
                                                                           resource_group_name: Optional[str] = None,
                                                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult:
    """
    Get the private endpoint with the specified name.


    :param str migrate_project_name: Migrate project name.
    :param str pe_connection_name: Private endpoint connection name.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    """
    __args__ = dict()
    __args__['migrateProjectName'] = migrate_project_name
    __args__['peConnectionName'] = pe_connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate/v20200501:getPrivateEndpointConnectionControllerPrivateEndpointConnection', __args__, opts=opts, typ=GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult).value

    return AwaitableGetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult(
        e_tag=pulumi.get(__ret__, 'e_tag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_private_endpoint_connection_controller_private_endpoint_connection)
def get_private_endpoint_connection_controller_private_endpoint_connection_output(migrate_project_name: Optional[pulumi.Input[str]] = None,
                                                                                  pe_connection_name: Optional[pulumi.Input[str]] = None,
                                                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateEndpointConnectionControllerPrivateEndpointConnectionResult]:
    """
    Get the private endpoint with the specified name.


    :param str migrate_project_name: Migrate project name.
    :param str pe_connection_name: Private endpoint connection name.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    """
    ...
