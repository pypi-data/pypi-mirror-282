# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSecretValueResult',
    'AwaitableGetSecretValueResult',
    'get_secret_value',
    'get_secret_value_output',
]

@pulumi.output_type
class GetSecretValueResult:
    """
    This type describes a value of a secret resource. The name of this resource is the version identifier corresponding to this secret value.
    """
    def __init__(__self__, id=None, location=None, name=None, provisioning_state=None, tags=None, type=None, value=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the resource.
        """
        return pulumi.get(self, "provisioning_state")

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
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The actual value of the secret.
        """
        return pulumi.get(self, "value")


class AwaitableGetSecretValueResult(GetSecretValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretValueResult(
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type,
            value=self.value)


def get_secret_value(resource_group_name: Optional[str] = None,
                     secret_resource_name: Optional[str] = None,
                     secret_value_resource_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretValueResult:
    """
    Get the information about the specified named secret value resources. The information does not include the actual value of the secret.
    Azure REST API version: 2018-09-01-preview.


    :param str resource_group_name: Azure resource group name
    :param str secret_resource_name: The name of the secret resource.
    :param str secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['secretResourceName'] = secret_resource_name
    __args__['secretValueResourceName'] = secret_value_resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabricmesh:getSecretValue', __args__, opts=opts, typ=GetSecretValueResult).value

    return AwaitableGetSecretValueResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_secret_value)
def get_secret_value_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                            secret_resource_name: Optional[pulumi.Input[str]] = None,
                            secret_value_resource_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretValueResult]:
    """
    Get the information about the specified named secret value resources. The information does not include the actual value of the secret.
    Azure REST API version: 2018-09-01-preview.


    :param str resource_group_name: Azure resource group name
    :param str secret_resource_name: The name of the secret resource.
    :param str secret_value_resource_name: The name of the secret resource value which is typically the version identifier for the value.
    """
    ...
