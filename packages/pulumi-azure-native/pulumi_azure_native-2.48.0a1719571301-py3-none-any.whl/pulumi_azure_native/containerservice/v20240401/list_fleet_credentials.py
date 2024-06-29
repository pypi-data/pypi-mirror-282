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
    'ListFleetCredentialsResult',
    'AwaitableListFleetCredentialsResult',
    'list_fleet_credentials',
    'list_fleet_credentials_output',
]

@pulumi.output_type
class ListFleetCredentialsResult:
    """
    The Credential results response.
    """
    def __init__(__self__, kubeconfigs=None):
        if kubeconfigs and not isinstance(kubeconfigs, list):
            raise TypeError("Expected argument 'kubeconfigs' to be a list")
        pulumi.set(__self__, "kubeconfigs", kubeconfigs)

    @property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence['outputs.FleetCredentialResultResponse']:
        """
        Array of base64-encoded Kubernetes configuration files.
        """
        return pulumi.get(self, "kubeconfigs")


class AwaitableListFleetCredentialsResult(ListFleetCredentialsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListFleetCredentialsResult(
            kubeconfigs=self.kubeconfigs)


def list_fleet_credentials(fleet_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListFleetCredentialsResult:
    """
    Lists the user credentials of a Fleet.


    :param str fleet_name: The name of the Fleet resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['fleetName'] = fleet_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20240401:listFleetCredentials', __args__, opts=opts, typ=ListFleetCredentialsResult).value

    return AwaitableListFleetCredentialsResult(
        kubeconfigs=pulumi.get(__ret__, 'kubeconfigs'))


@_utilities.lift_output_func(list_fleet_credentials)
def list_fleet_credentials_output(fleet_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListFleetCredentialsResult]:
    """
    Lists the user credentials of a Fleet.


    :param str fleet_name: The name of the Fleet resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
