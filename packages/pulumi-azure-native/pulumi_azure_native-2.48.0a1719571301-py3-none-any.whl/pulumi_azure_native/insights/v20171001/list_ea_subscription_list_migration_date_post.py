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
    'ListEASubscriptionListMigrationDatePostResult',
    'AwaitableListEASubscriptionListMigrationDatePostResult',
    'list_ea_subscription_list_migration_date_post',
    'list_ea_subscription_list_migration_date_post_output',
]

@pulumi.output_type
class ListEASubscriptionListMigrationDatePostResult:
    """
    Subscription migrate date information properties
    """
    def __init__(__self__, is_grand_fatherable_subscription=None, opted_in_date=None):
        if is_grand_fatherable_subscription and not isinstance(is_grand_fatherable_subscription, bool):
            raise TypeError("Expected argument 'is_grand_fatherable_subscription' to be a bool")
        pulumi.set(__self__, "is_grand_fatherable_subscription", is_grand_fatherable_subscription)
        if opted_in_date and not isinstance(opted_in_date, str):
            raise TypeError("Expected argument 'opted_in_date' to be a str")
        pulumi.set(__self__, "opted_in_date", opted_in_date)

    @property
    @pulumi.getter(name="isGrandFatherableSubscription")
    def is_grand_fatherable_subscription(self) -> Optional[bool]:
        """
        Is subscription in the grand fatherable subscription list.
        """
        return pulumi.get(self, "is_grand_fatherable_subscription")

    @property
    @pulumi.getter(name="optedInDate")
    def opted_in_date(self) -> Optional[str]:
        """
        Time to start using new pricing model.
        """
        return pulumi.get(self, "opted_in_date")


class AwaitableListEASubscriptionListMigrationDatePostResult(ListEASubscriptionListMigrationDatePostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListEASubscriptionListMigrationDatePostResult(
            is_grand_fatherable_subscription=self.is_grand_fatherable_subscription,
            opted_in_date=self.opted_in_date)


def list_ea_subscription_list_migration_date_post(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListEASubscriptionListMigrationDatePostResult:
    """
    list date to migrate to new pricing model.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20171001:listEASubscriptionListMigrationDatePost', __args__, opts=opts, typ=ListEASubscriptionListMigrationDatePostResult).value

    return AwaitableListEASubscriptionListMigrationDatePostResult(
        is_grand_fatherable_subscription=pulumi.get(__ret__, 'is_grand_fatherable_subscription'),
        opted_in_date=pulumi.get(__ret__, 'opted_in_date'))


@_utilities.lift_output_func(list_ea_subscription_list_migration_date_post)
def list_ea_subscription_list_migration_date_post_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListEASubscriptionListMigrationDatePostResult]:
    """
    list date to migrate to new pricing model.
    """
    ...
