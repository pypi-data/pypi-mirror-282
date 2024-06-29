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
    'GetConsoleResult',
    'AwaitableGetConsoleResult',
    'get_console',
    'get_console_output',
]

@pulumi.output_type
class GetConsoleResult:
    """
    Cloud shell console
    """
    def __init__(__self__, properties=None):
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ConsolePropertiesResponse':
        """
        Cloud shell console properties.
        """
        return pulumi.get(self, "properties")


class AwaitableGetConsoleResult(GetConsoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConsoleResult(
            properties=self.properties)


def get_console(console_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConsoleResult:
    """
    Gets the console for the user.
    Azure REST API version: 2018-10-01.


    :param str console_name: The name of the console
    """
    __args__ = dict()
    __args__['consoleName'] = console_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:portal:getConsole', __args__, opts=opts, typ=GetConsoleResult).value

    return AwaitableGetConsoleResult(
        properties=pulumi.get(__ret__, 'properties'))


@_utilities.lift_output_func(get_console)
def get_console_output(console_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConsoleResult]:
    """
    Gets the console for the user.
    Azure REST API version: 2018-10-01.


    :param str console_name: The name of the console
    """
    ...
