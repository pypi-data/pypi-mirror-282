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
    'GetSolutionsControllerSolutionResult',
    'AwaitableGetSolutionsControllerSolutionResult',
    'get_solutions_controller_solution',
    'get_solutions_controller_solution_output',
]

@pulumi.output_type
class GetSolutionsControllerSolutionResult:
    """
    Solution REST Resource.
    """
    def __init__(__self__, etag=None, id=None, name=None, properties=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Gets or sets the ETAG for optimistic concurrency control.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Gets the relative URL to get to this REST resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the name of this REST resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.SolutionPropertiesResponse':
        """
        Gets or sets the properties of the solution.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the type of this REST resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetSolutionsControllerSolutionResult(GetSolutionsControllerSolutionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSolutionsControllerSolutionResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_solutions_controller_solution(migrate_project_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      solution_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSolutionsControllerSolutionResult:
    """
    Solution REST Resource.


    :param str migrate_project_name: Name of the Azure Migrate project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str solution_name: Unique name of a migration solution within a migrate project.
    """
    __args__ = dict()
    __args__['migrateProjectName'] = migrate_project_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['solutionName'] = solution_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate/v20230101:getSolutionsControllerSolution', __args__, opts=opts, typ=GetSolutionsControllerSolutionResult).value

    return AwaitableGetSolutionsControllerSolutionResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_solutions_controller_solution)
def get_solutions_controller_solution_output(migrate_project_name: Optional[pulumi.Input[str]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             solution_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSolutionsControllerSolutionResult]:
    """
    Solution REST Resource.


    :param str migrate_project_name: Name of the Azure Migrate project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str solution_name: Unique name of a migration solution within a migrate project.
    """
    ...
