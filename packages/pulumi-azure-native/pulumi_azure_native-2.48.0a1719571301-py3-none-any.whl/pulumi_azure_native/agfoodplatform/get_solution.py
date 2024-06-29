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
    'GetSolutionResult',
    'AwaitableGetSolutionResult',
    'get_solution',
    'get_solution_output',
]

@pulumi.output_type
class GetSolutionResult:
    """
    Solution resource.
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
        The ETag value to implement optimistic concurrency.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
    def properties(self) -> 'outputs.SolutionPropertiesResponse':
        """
        Solution resource properties.
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


class AwaitableGetSolutionResult(GetSolutionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSolutionResult(
            e_tag=self.e_tag,
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_solution(data_manager_for_agriculture_resource_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 solution_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSolutionResult:
    """
    Get installed Solution details by Solution id.
    Azure REST API version: 2023-06-01-preview.

    Other available API versions: 2021-09-01-preview.


    :param str data_manager_for_agriculture_resource_name: DataManagerForAgriculture resource name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str solution_id: SolutionId for Data Manager For Agriculture Resource.
    """
    __args__ = dict()
    __args__['dataManagerForAgricultureResourceName'] = data_manager_for_agriculture_resource_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['solutionId'] = solution_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:agfoodplatform:getSolution', __args__, opts=opts, typ=GetSolutionResult).value

    return AwaitableGetSolutionResult(
        e_tag=pulumi.get(__ret__, 'e_tag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_solution)
def get_solution_output(data_manager_for_agriculture_resource_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        solution_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSolutionResult]:
    """
    Get installed Solution details by Solution id.
    Azure REST API version: 2023-06-01-preview.

    Other available API versions: 2021-09-01-preview.


    :param str data_manager_for_agriculture_resource_name: DataManagerForAgriculture resource name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str solution_id: SolutionId for Data Manager For Agriculture Resource.
    """
    ...
