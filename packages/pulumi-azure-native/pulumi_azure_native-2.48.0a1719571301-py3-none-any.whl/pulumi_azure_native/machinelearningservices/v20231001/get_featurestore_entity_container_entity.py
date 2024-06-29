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
    'GetFeaturestoreEntityContainerEntityResult',
    'AwaitableGetFeaturestoreEntityContainerEntityResult',
    'get_featurestore_entity_container_entity',
    'get_featurestore_entity_container_entity_output',
]

@pulumi.output_type
class GetFeaturestoreEntityContainerEntityResult:
    """
    Azure Resource Manager resource envelope.
    """
    def __init__(__self__, featurestore_entity_container_properties=None, id=None, name=None, system_data=None, type=None):
        if featurestore_entity_container_properties and not isinstance(featurestore_entity_container_properties, dict):
            raise TypeError("Expected argument 'featurestore_entity_container_properties' to be a dict")
        pulumi.set(__self__, "featurestore_entity_container_properties", featurestore_entity_container_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
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
    @pulumi.getter(name="featurestoreEntityContainerProperties")
    def featurestore_entity_container_properties(self) -> 'outputs.FeaturestoreEntityContainerResponse':
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "featurestore_entity_container_properties")

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


class AwaitableGetFeaturestoreEntityContainerEntityResult(GetFeaturestoreEntityContainerEntityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFeaturestoreEntityContainerEntityResult(
            featurestore_entity_container_properties=self.featurestore_entity_container_properties,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_featurestore_entity_container_entity(name: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             workspace_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFeaturestoreEntityContainerEntityResult:
    """
    Azure Resource Manager resource envelope.


    :param str name: Container name. This is case-sensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20231001:getFeaturestoreEntityContainerEntity', __args__, opts=opts, typ=GetFeaturestoreEntityContainerEntityResult).value

    return AwaitableGetFeaturestoreEntityContainerEntityResult(
        featurestore_entity_container_properties=pulumi.get(__ret__, 'featurestore_entity_container_properties'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_featurestore_entity_container_entity)
def get_featurestore_entity_container_entity_output(name: Optional[pulumi.Input[str]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    workspace_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFeaturestoreEntityContainerEntityResult]:
    """
    Azure Resource Manager resource envelope.


    :param str name: Container name. This is case-sensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
