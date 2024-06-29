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
    'ListJobSecretsResult',
    'AwaitableListJobSecretsResult',
    'list_job_secrets',
    'list_job_secrets_output',
]

@pulumi.output_type
class ListJobSecretsResult:
    """
    Container Apps Job Secrets Collection ARM resource.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.SecretResponse']:
        """
        Collection of resources.
        """
        return pulumi.get(self, "value")


class AwaitableListJobSecretsResult(ListJobSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListJobSecretsResult(
            value=self.value)


def list_job_secrets(job_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListJobSecretsResult:
    """
    Container Apps Job Secrets Collection ARM resource.


    :param str job_name: Job Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['jobName'] = job_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20230401preview:listJobSecrets', __args__, opts=opts, typ=ListJobSecretsResult).value

    return AwaitableListJobSecretsResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_job_secrets)
def list_job_secrets_output(job_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListJobSecretsResult]:
    """
    Container Apps Job Secrets Collection ARM resource.


    :param str job_name: Job Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
