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
    'ListDaprComponentSecretsResult',
    'AwaitableListDaprComponentSecretsResult',
    'list_dapr_component_secrets',
    'list_dapr_component_secrets_output',
]

@pulumi.output_type
class ListDaprComponentSecretsResult:
    """
    Dapr component Secrets Collection for ListSecrets Action.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.DaprSecretResponse']:
        """
        Collection of secrets used by a Dapr component
        """
        return pulumi.get(self, "value")


class AwaitableListDaprComponentSecretsResult(ListDaprComponentSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDaprComponentSecretsResult(
            value=self.value)


def list_dapr_component_secrets(component_name: Optional[str] = None,
                                environment_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDaprComponentSecretsResult:
    """
    Dapr component Secrets Collection for ListSecrets Action.


    :param str component_name: Name of the Dapr Component.
    :param str environment_name: Name of the Managed Environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['componentName'] = component_name
    __args__['environmentName'] = environment_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20221001:listDaprComponentSecrets', __args__, opts=opts, typ=ListDaprComponentSecretsResult).value

    return AwaitableListDaprComponentSecretsResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_dapr_component_secrets)
def list_dapr_component_secrets_output(component_name: Optional[pulumi.Input[str]] = None,
                                       environment_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDaprComponentSecretsResult]:
    """
    Dapr component Secrets Collection for ListSecrets Action.


    :param str component_name: Name of the Dapr Component.
    :param str environment_name: Name of the Managed Environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
