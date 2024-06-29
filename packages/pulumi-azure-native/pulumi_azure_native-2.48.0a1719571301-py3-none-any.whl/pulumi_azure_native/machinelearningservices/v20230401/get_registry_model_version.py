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
    'GetRegistryModelVersionResult',
    'AwaitableGetRegistryModelVersionResult',
    'get_registry_model_version',
    'get_registry_model_version_output',
]

@pulumi.output_type
class GetRegistryModelVersionResult:
    """
    Azure Resource Manager resource envelope.
    """
    def __init__(__self__, id=None, model_version_properties=None, name=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if model_version_properties and not isinstance(model_version_properties, dict):
            raise TypeError("Expected argument 'model_version_properties' to be a dict")
        pulumi.set(__self__, "model_version_properties", model_version_properties)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    @pulumi.getter(name="modelVersionProperties")
    def model_version_properties(self) -> 'outputs.ModelVersionResponse':
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "model_version_properties")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

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


class AwaitableGetRegistryModelVersionResult(GetRegistryModelVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryModelVersionResult(
            id=self.id,
            model_version_properties=self.model_version_properties,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_registry_model_version(model_name: Optional[str] = None,
                               registry_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               version: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistryModelVersionResult:
    """
    Azure Resource Manager resource envelope.


    :param str model_name: Container name. This is case-sensitive.
    :param str registry_name: Name of Azure Machine Learning registry. This is case-insensitive
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str version: Version identifier. This is case-sensitive.
    """
    __args__ = dict()
    __args__['modelName'] = model_name
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20230401:getRegistryModelVersion', __args__, opts=opts, typ=GetRegistryModelVersionResult).value

    return AwaitableGetRegistryModelVersionResult(
        id=pulumi.get(__ret__, 'id'),
        model_version_properties=pulumi.get(__ret__, 'model_version_properties'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_registry_model_version)
def get_registry_model_version_output(model_name: Optional[pulumi.Input[str]] = None,
                                      registry_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      version: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegistryModelVersionResult]:
    """
    Azure Resource Manager resource envelope.


    :param str model_name: Container name. This is case-sensitive.
    :param str registry_name: Name of Azure Machine Learning registry. This is case-insensitive
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str version: Version identifier. This is case-sensitive.
    """
    ...
