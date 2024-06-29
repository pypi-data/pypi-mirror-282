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
    'GetOpenAIStatusResult',
    'AwaitableGetOpenAIStatusResult',
    'get_open_ai_status',
    'get_open_ai_status_output',
]

@pulumi.output_type
class GetOpenAIStatusResult:
    """
    Status of the OpenAI Integration
    """
    def __init__(__self__, properties=None):
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.OpenAIIntegrationStatusResponsePropertiesResponse':
        """
        Status of the OpenAI Integration
        """
        return pulumi.get(self, "properties")


class AwaitableGetOpenAIStatusResult(GetOpenAIStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOpenAIStatusResult(
            properties=self.properties)


def get_open_ai_status(integration_name: Optional[str] = None,
                       monitor_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOpenAIStatusResult:
    """
    Status of the OpenAI Integration
    Azure REST API version: 2024-03-01.

    Other available API versions: 2024-01-01-preview, 2024-05-01-preview, 2024-06-15-preview.


    :param str integration_name: OpenAI Integration name
    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['integrationName'] = integration_name
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic:getOpenAIStatus', __args__, opts=opts, typ=GetOpenAIStatusResult).value

    return AwaitableGetOpenAIStatusResult(
        properties=pulumi.get(__ret__, 'properties'))


@_utilities.lift_output_func(get_open_ai_status)
def get_open_ai_status_output(integration_name: Optional[pulumi.Input[str]] = None,
                              monitor_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOpenAIStatusResult]:
    """
    Status of the OpenAI Integration
    Azure REST API version: 2024-03-01.

    Other available API versions: 2024-01-01-preview, 2024-05-01-preview, 2024-06-15-preview.


    :param str integration_name: OpenAI Integration name
    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
