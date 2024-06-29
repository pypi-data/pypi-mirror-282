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
    'GetVariableResult',
    'AwaitableGetVariableResult',
    'get_variable',
    'get_variable_output',
]

@pulumi.output_type
class GetVariableResult:
    """
    The variable.
    """
    def __init__(__self__, columns=None, id=None, name=None, system_data=None, type=None):
        if columns and not isinstance(columns, list):
            raise TypeError("Expected argument 'columns' to be a list")
        pulumi.set(__self__, "columns", columns)
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
    @pulumi.getter
    def columns(self) -> Sequence['outputs.PolicyVariableColumnResponse']:
        """
        Variable column definitions.
        """
        return pulumi.get(self, "columns")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the variable.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the variable.
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
        The type of the resource (Microsoft.Authorization/variables).
        """
        return pulumi.get(self, "type")


class AwaitableGetVariableResult(GetVariableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVariableResult(
            columns=self.columns,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_variable(variable_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVariableResult:
    """
    This operation retrieves a single variable, given its name and the subscription it was created at.


    :param str variable_name: The name of the variable to operate on.
    """
    __args__ = dict()
    __args__['variableName'] = variable_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization/v20220801preview:getVariable', __args__, opts=opts, typ=GetVariableResult).value

    return AwaitableGetVariableResult(
        columns=pulumi.get(__ret__, 'columns'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_variable)
def get_variable_output(variable_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVariableResult]:
    """
    This operation retrieves a single variable, given its name and the subscription it was created at.


    :param str variable_name: The name of the variable to operate on.
    """
    ...
