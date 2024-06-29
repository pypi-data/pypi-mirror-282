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
    'GetBillingHubServiceFreeHourBalanceResult',
    'AwaitableGetBillingHubServiceFreeHourBalanceResult',
    'get_billing_hub_service_free_hour_balance',
    'get_billing_hub_service_free_hour_balance_output',
]

@pulumi.output_type
class GetBillingHubServiceFreeHourBalanceResult:
    def __init__(__self__, increment_entries=None, total_remaining_free_hours=None):
        if increment_entries and not isinstance(increment_entries, list):
            raise TypeError("Expected argument 'increment_entries' to be a list")
        pulumi.set(__self__, "increment_entries", increment_entries)
        if total_remaining_free_hours and not isinstance(total_remaining_free_hours, float):
            raise TypeError("Expected argument 'total_remaining_free_hours' to be a float")
        pulumi.set(__self__, "total_remaining_free_hours", total_remaining_free_hours)

    @property
    @pulumi.getter(name="incrementEntries")
    def increment_entries(self) -> Optional[Sequence['outputs.BillingHubFreeHourIncrementEntryResponse']]:
        return pulumi.get(self, "increment_entries")

    @property
    @pulumi.getter(name="totalRemainingFreeHours")
    def total_remaining_free_hours(self) -> Optional[float]:
        return pulumi.get(self, "total_remaining_free_hours")


class AwaitableGetBillingHubServiceFreeHourBalanceResult(GetBillingHubServiceFreeHourBalanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBillingHubServiceFreeHourBalanceResult(
            increment_entries=self.increment_entries,
            total_remaining_free_hours=self.total_remaining_free_hours)


def get_billing_hub_service_free_hour_balance(resource_group_name: Optional[str] = None,
                                              test_base_account_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBillingHubServiceFreeHourBalanceResult:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['testBaseAccountName'] = test_base_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:testbase/v20231101preview:getBillingHubServiceFreeHourBalance', __args__, opts=opts, typ=GetBillingHubServiceFreeHourBalanceResult).value

    return AwaitableGetBillingHubServiceFreeHourBalanceResult(
        increment_entries=pulumi.get(__ret__, 'increment_entries'),
        total_remaining_free_hours=pulumi.get(__ret__, 'total_remaining_free_hours'))


@_utilities.lift_output_func(get_billing_hub_service_free_hour_balance)
def get_billing_hub_service_free_hour_balance_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                     test_base_account_name: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBillingHubServiceFreeHourBalanceResult]:
    """
    Use this data source to access information about an existing resource.

    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    ...
