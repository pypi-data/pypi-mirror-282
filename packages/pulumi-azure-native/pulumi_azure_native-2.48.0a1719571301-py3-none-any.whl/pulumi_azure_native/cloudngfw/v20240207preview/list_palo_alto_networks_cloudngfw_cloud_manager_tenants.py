# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListPaloAltoNetworksCloudngfwCloudManagerTenantsResult',
    'AwaitableListPaloAltoNetworksCloudngfwCloudManagerTenantsResult',
    'list_palo_alto_networks_cloudngfw_cloud_manager_tenants',
    'list_palo_alto_networks_cloudngfw_cloud_manager_tenants_output',
]

@pulumi.output_type
class ListPaloAltoNetworksCloudngfwCloudManagerTenantsResult:
    """
    Cloud Manager Tenant
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Sequence[str]:
        """
        List of Cloud Manager Tenants
        """
        return pulumi.get(self, "value")


class AwaitableListPaloAltoNetworksCloudngfwCloudManagerTenantsResult(ListPaloAltoNetworksCloudngfwCloudManagerTenantsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListPaloAltoNetworksCloudngfwCloudManagerTenantsResult(
            value=self.value)


def list_palo_alto_networks_cloudngfw_cloud_manager_tenants(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListPaloAltoNetworksCloudngfwCloudManagerTenantsResult:
    """
    Cloud Manager Tenant
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20240207preview:listPaloAltoNetworksCloudngfwCloudManagerTenants', __args__, opts=opts, typ=ListPaloAltoNetworksCloudngfwCloudManagerTenantsResult).value

    return AwaitableListPaloAltoNetworksCloudngfwCloudManagerTenantsResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_palo_alto_networks_cloudngfw_cloud_manager_tenants)
def list_palo_alto_networks_cloudngfw_cloud_manager_tenants_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListPaloAltoNetworksCloudngfwCloudManagerTenantsResult]:
    """
    Cloud Manager Tenant
    """
    ...
