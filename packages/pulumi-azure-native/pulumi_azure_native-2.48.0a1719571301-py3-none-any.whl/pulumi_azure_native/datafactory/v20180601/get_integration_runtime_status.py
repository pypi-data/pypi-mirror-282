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
    'GetIntegrationRuntimeStatusResult',
    'AwaitableGetIntegrationRuntimeStatusResult',
    'get_integration_runtime_status',
    'get_integration_runtime_status_output',
]

@pulumi.output_type
class GetIntegrationRuntimeStatusResult:
    """
    Integration runtime status response.
    """
    def __init__(__self__, name=None, properties=None):
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The integration runtime name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Any:
        """
        Integration runtime properties.
        """
        return pulumi.get(self, "properties")


class AwaitableGetIntegrationRuntimeStatusResult(GetIntegrationRuntimeStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationRuntimeStatusResult(
            name=self.name,
            properties=self.properties)


def get_integration_runtime_status(factory_name: Optional[str] = None,
                                   integration_runtime_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationRuntimeStatusResult:
    """
    Gets detailed status information for an integration runtime.


    :param str factory_name: The factory name.
    :param str integration_runtime_name: The integration runtime name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['integrationRuntimeName'] = integration_runtime_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory/v20180601:getIntegrationRuntimeStatus', __args__, opts=opts, typ=GetIntegrationRuntimeStatusResult).value

    return AwaitableGetIntegrationRuntimeStatusResult(
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'))


@_utilities.lift_output_func(get_integration_runtime_status)
def get_integration_runtime_status_output(factory_name: Optional[pulumi.Input[str]] = None,
                                          integration_runtime_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIntegrationRuntimeStatusResult]:
    """
    Gets detailed status information for an integration runtime.


    :param str factory_name: The factory name.
    :param str integration_runtime_name: The integration runtime name.
    :param str resource_group_name: The resource group name.
    """
    ...
