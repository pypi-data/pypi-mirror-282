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
    'GetSkusNestedResourceTypeThirdResult',
    'AwaitableGetSkusNestedResourceTypeThirdResult',
    'get_skus_nested_resource_type_third',
    'get_skus_nested_resource_type_third_output',
]

@pulumi.output_type
class GetSkusNestedResourceTypeThirdResult:
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, type=None):
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
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.SkuResourceResponseProperties':
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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSkusNestedResourceTypeThirdResult(GetSkusNestedResourceTypeThirdResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSkusNestedResourceTypeThirdResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_skus_nested_resource_type_third(nested_resource_type_first: Optional[str] = None,
                                        nested_resource_type_second: Optional[str] = None,
                                        nested_resource_type_third: Optional[str] = None,
                                        provider_namespace: Optional[str] = None,
                                        resource_type: Optional[str] = None,
                                        sku: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSkusNestedResourceTypeThirdResult:
    """
    Gets the sku details for the given resource type and sku name.
    Azure REST API version: 2021-09-01-preview.


    :param str nested_resource_type_first: The first child resource type.
    :param str nested_resource_type_second: The second child resource type.
    :param str nested_resource_type_third: The third child resource type.
    :param str provider_namespace: The name of the resource provider hosted within ProviderHub.
    :param str resource_type: The resource type.
    :param str sku: The SKU.
    """
    __args__ = dict()
    __args__['nestedResourceTypeFirst'] = nested_resource_type_first
    __args__['nestedResourceTypeSecond'] = nested_resource_type_second
    __args__['nestedResourceTypeThird'] = nested_resource_type_third
    __args__['providerNamespace'] = provider_namespace
    __args__['resourceType'] = resource_type
    __args__['sku'] = sku
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:providerhub:getSkusNestedResourceTypeThird', __args__, opts=opts, typ=GetSkusNestedResourceTypeThirdResult).value

    return AwaitableGetSkusNestedResourceTypeThirdResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_skus_nested_resource_type_third)
def get_skus_nested_resource_type_third_output(nested_resource_type_first: Optional[pulumi.Input[str]] = None,
                                               nested_resource_type_second: Optional[pulumi.Input[str]] = None,
                                               nested_resource_type_third: Optional[pulumi.Input[str]] = None,
                                               provider_namespace: Optional[pulumi.Input[str]] = None,
                                               resource_type: Optional[pulumi.Input[str]] = None,
                                               sku: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSkusNestedResourceTypeThirdResult]:
    """
    Gets the sku details for the given resource type and sku name.
    Azure REST API version: 2021-09-01-preview.


    :param str nested_resource_type_first: The first child resource type.
    :param str nested_resource_type_second: The second child resource type.
    :param str nested_resource_type_third: The third child resource type.
    :param str provider_namespace: The name of the resource provider hosted within ProviderHub.
    :param str resource_type: The resource type.
    :param str sku: The SKU.
    """
    ...
