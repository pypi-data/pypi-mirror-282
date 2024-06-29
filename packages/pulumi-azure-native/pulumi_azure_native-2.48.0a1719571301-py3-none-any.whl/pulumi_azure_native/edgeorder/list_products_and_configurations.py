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
from ._enums import *
from ._inputs import *

__all__ = [
    'ListProductsAndConfigurationsResult',
    'AwaitableListProductsAndConfigurationsResult',
    'list_products_and_configurations',
    'list_products_and_configurations_output',
]

@pulumi.output_type
class ListProductsAndConfigurationsResult:
    """
    The list of configurations.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        Link for the next set of configurations.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.ConfigurationResponse']:
        """
        List of configurations.
        """
        return pulumi.get(self, "value")


class AwaitableListProductsAndConfigurationsResult(ListProductsAndConfigurationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListProductsAndConfigurationsResult(
            next_link=self.next_link,
            value=self.value)


def list_products_and_configurations(configuration_filter: Optional[pulumi.InputType['ConfigurationFilter']] = None,
                                     customer_subscription_details: Optional[pulumi.InputType['CustomerSubscriptionDetails']] = None,
                                     skip_token: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListProductsAndConfigurationsResult:
    """
    List configurations for the given product family, product line and product for the given subscription.
    Azure REST API version: 2022-05-01-preview.

    Other available API versions: 2024-02-01.


    :param pulumi.InputType['ConfigurationFilter'] configuration_filter: Holds details about product hierarchy information and filterable property.
    :param pulumi.InputType['CustomerSubscriptionDetails'] customer_subscription_details: Customer subscription properties. Clients can display available products to unregistered customers by explicitly passing subscription details.
    :param str skip_token: $skipToken is supported on list of configurations, which provides the next page in the list of configurations.
    """
    __args__ = dict()
    __args__['configurationFilter'] = configuration_filter
    __args__['customerSubscriptionDetails'] = customer_subscription_details
    __args__['skipToken'] = skip_token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:edgeorder:listProductsAndConfigurations', __args__, opts=opts, typ=ListProductsAndConfigurationsResult).value

    return AwaitableListProductsAndConfigurationsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_products_and_configurations)
def list_products_and_configurations_output(configuration_filter: Optional[pulumi.Input[Optional[pulumi.InputType['ConfigurationFilter']]]] = None,
                                            customer_subscription_details: Optional[pulumi.Input[Optional[pulumi.InputType['CustomerSubscriptionDetails']]]] = None,
                                            skip_token: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListProductsAndConfigurationsResult]:
    """
    List configurations for the given product family, product line and product for the given subscription.
    Azure REST API version: 2022-05-01-preview.

    Other available API versions: 2024-02-01.


    :param pulumi.InputType['ConfigurationFilter'] configuration_filter: Holds details about product hierarchy information and filterable property.
    :param pulumi.InputType['CustomerSubscriptionDetails'] customer_subscription_details: Customer subscription properties. Clients can display available products to unregistered customers by explicitly passing subscription details.
    :param str skip_token: $skipToken is supported on list of configurations, which provides the next page in the list of configurations.
    """
    ...
