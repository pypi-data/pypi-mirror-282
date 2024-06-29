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
    'GetBillingInfoResult',
    'AwaitableGetBillingInfoResult',
    'get_billing_info',
    'get_billing_info_output',
]

@pulumi.output_type
class GetBillingInfoResult:
    """
    Marketplace Subscription and Organization details to which resource gets billed into.
    """
    def __init__(__self__, marketplace_saas_info=None, partner_billing_entity=None):
        if marketplace_saas_info and not isinstance(marketplace_saas_info, dict):
            raise TypeError("Expected argument 'marketplace_saas_info' to be a dict")
        pulumi.set(__self__, "marketplace_saas_info", marketplace_saas_info)
        if partner_billing_entity and not isinstance(partner_billing_entity, dict):
            raise TypeError("Expected argument 'partner_billing_entity' to be a dict")
        pulumi.set(__self__, "partner_billing_entity", partner_billing_entity)

    @property
    @pulumi.getter(name="marketplaceSaasInfo")
    def marketplace_saas_info(self) -> Optional['outputs.MarketplaceSaaSInfoResponse']:
        """
        Marketplace Subscription details
        """
        return pulumi.get(self, "marketplace_saas_info")

    @property
    @pulumi.getter(name="partnerBillingEntity")
    def partner_billing_entity(self) -> Optional['outputs.PartnerBillingEntityResponse']:
        """
        Partner Billing Entity details: Organization Info
        """
        return pulumi.get(self, "partner_billing_entity")


class AwaitableGetBillingInfoResult(GetBillingInfoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBillingInfoResult(
            marketplace_saas_info=self.marketplace_saas_info,
            partner_billing_entity=self.partner_billing_entity)


def get_billing_info(monitor_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBillingInfoResult:
    """
    Marketplace Subscription and Organization details to which resource gets billed into.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic/v20231101preview:getBillingInfo', __args__, opts=opts, typ=GetBillingInfoResult).value

    return AwaitableGetBillingInfoResult(
        marketplace_saas_info=pulumi.get(__ret__, 'marketplace_saas_info'),
        partner_billing_entity=pulumi.get(__ret__, 'partner_billing_entity'))


@_utilities.lift_output_func(get_billing_info)
def get_billing_info_output(monitor_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBillingInfoResult]:
    """
    Marketplace Subscription and Organization details to which resource gets billed into.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
