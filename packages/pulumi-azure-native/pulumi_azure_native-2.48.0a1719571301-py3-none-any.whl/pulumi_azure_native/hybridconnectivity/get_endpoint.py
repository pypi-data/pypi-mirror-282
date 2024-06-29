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
    'GetEndpointResult',
    'AwaitableGetEndpointResult',
    'get_endpoint',
    'get_endpoint_output',
]

@pulumi.output_type
class GetEndpointResult:
    """
    The endpoint for the target resource.
    """
    def __init__(__self__, created_at=None, created_by=None, created_by_type=None, id=None, last_modified_at=None, last_modified_by=None, last_modified_by_type=None, name=None, properties=None, system_data=None, type=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if created_by_type and not isinstance(created_by_type, str):
            raise TypeError("Expected argument 'created_by_type' to be a str")
        pulumi.set(__self__, "created_by_type", created_by_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_at and not isinstance(last_modified_at, str):
            raise TypeError("Expected argument 'last_modified_at' to be a str")
        pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by and not isinstance(last_modified_by, str):
            raise TypeError("Expected argument 'last_modified_by' to be a str")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type and not isinstance(last_modified_by_type, str):
            raise TypeError("Expected argument 'last_modified_by_type' to be a str")
        pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
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
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.EndpointPropertiesResponse':
        """
        The endpoint properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetEndpointResult(GetEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEndpointResult(
            created_at=self.created_at,
            created_by=self.created_by,
            created_by_type=self.created_by_type,
            id=self.id,
            last_modified_at=self.last_modified_at,
            last_modified_by=self.last_modified_by,
            last_modified_by_type=self.last_modified_by_type,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_endpoint(endpoint_name: Optional[str] = None,
                 resource_uri: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEndpointResult:
    """
    Gets the endpoint to the resource.
    Azure REST API version: 2023-03-15.

    Other available API versions: 2022-05-01-preview.


    :param str endpoint_name: The endpoint name.
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['resourceUri'] = resource_uri
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridconnectivity:getEndpoint', __args__, opts=opts, typ=GetEndpointResult).value

    return AwaitableGetEndpointResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        created_by=pulumi.get(__ret__, 'created_by'),
        created_by_type=pulumi.get(__ret__, 'created_by_type'),
        id=pulumi.get(__ret__, 'id'),
        last_modified_at=pulumi.get(__ret__, 'last_modified_at'),
        last_modified_by=pulumi.get(__ret__, 'last_modified_by'),
        last_modified_by_type=pulumi.get(__ret__, 'last_modified_by_type'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_endpoint)
def get_endpoint_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                        resource_uri: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEndpointResult]:
    """
    Gets the endpoint to the resource.
    Azure REST API version: 2023-03-15.

    Other available API versions: 2022-05-01-preview.


    :param str endpoint_name: The endpoint name.
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    """
    ...
