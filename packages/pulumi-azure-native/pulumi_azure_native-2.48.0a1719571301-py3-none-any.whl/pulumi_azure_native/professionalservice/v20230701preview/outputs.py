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
    'ProfessionalServicePropertiesResponseTerm',
    'ProfessionalServiceResourceResponseProperties',
]

@pulumi.output_type
class ProfessionalServicePropertiesResponseTerm(dict):
    """
    The current Term object.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endDate":
            suggest = "end_date"
        elif key == "startDate":
            suggest = "start_date"
        elif key == "termUnit":
            suggest = "term_unit"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProfessionalServicePropertiesResponseTerm. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProfessionalServicePropertiesResponseTerm.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProfessionalServicePropertiesResponseTerm.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 end_date: Optional[str] = None,
                 start_date: Optional[str] = None,
                 term_unit: Optional[str] = None):
        """
        The current Term object.
        :param str end_date: The end date of the current term
        :param str start_date: The start date of the current term
        :param str term_unit: The unit term eg P1M,P1Y,P2Y,P3Y meaning month,1year,2year,3year respectively
        """
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)
        if start_date is not None:
            pulumi.set(__self__, "start_date", start_date)
        if term_unit is not None:
            pulumi.set(__self__, "term_unit", term_unit)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[str]:
        """
        The end date of the current term
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[str]:
        """
        The start date of the current term
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> Optional[str]:
        """
        The unit term eg P1M,P1Y,P2Y,P3Y meaning month,1year,2year,3year respectively
        """
        return pulumi.get(self, "term_unit")


@pulumi.output_type
class ProfessionalServiceResourceResponseProperties(dict):
    """
    professionalService properties
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "autoRenew":
            suggest = "auto_renew"
        elif key == "billingPeriod":
            suggest = "billing_period"
        elif key == "isFreeTrial":
            suggest = "is_free_trial"
        elif key == "lastModified":
            suggest = "last_modified"
        elif key == "offerId":
            suggest = "offer_id"
        elif key == "paymentChannelMetadata":
            suggest = "payment_channel_metadata"
        elif key == "paymentChannelType":
            suggest = "payment_channel_type"
        elif key == "publisherId":
            suggest = "publisher_id"
        elif key == "quoteId":
            suggest = "quote_id"
        elif key == "skuId":
            suggest = "sku_id"
        elif key == "storeFront":
            suggest = "store_front"
        elif key == "termUnit":
            suggest = "term_unit"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProfessionalServiceResourceResponseProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProfessionalServiceResourceResponseProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProfessionalServiceResourceResponseProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created: str,
                 auto_renew: Optional[bool] = None,
                 billing_period: Optional[str] = None,
                 is_free_trial: Optional[bool] = None,
                 last_modified: Optional[str] = None,
                 offer_id: Optional[str] = None,
                 payment_channel_metadata: Optional[Mapping[str, str]] = None,
                 payment_channel_type: Optional[str] = None,
                 publisher_id: Optional[str] = None,
                 quote_id: Optional[str] = None,
                 sku_id: Optional[str] = None,
                 status: Optional[str] = None,
                 store_front: Optional[str] = None,
                 term: Optional['outputs.ProfessionalServicePropertiesResponseTerm'] = None,
                 term_unit: Optional[str] = None):
        """
        professionalService properties
        :param str created: The created date of this resource.
        :param bool auto_renew: Whether the ProfessionalService subscription will auto renew upon term end.
        :param str billing_period: The billing period eg P1M,P1Y for monthly,yearly respectively
        :param bool is_free_trial: Whether the current term is a Free Trial term
        :param str last_modified: The last modifier date if this resource.
        :param str offer_id: The offer id.
        :param Mapping[str, str] payment_channel_metadata: The metadata about the ProfessionalService subscription such as the AzureSubscriptionId and ResourceUri.
        :param str payment_channel_type: The Payment channel for the ProfessionalServiceSubscription.
        :param str publisher_id: The publisher id.
        :param str quote_id: The quote id which the ProfessionalService will be purchase with.
        :param str sku_id: The plan id.
        :param str status: The ProfessionalService Subscription Status.
        :param str store_front: The store front which initiates the purchase.
        :param 'ProfessionalServicePropertiesResponseTerm' term: The current Term object.
        :param str term_unit: The unit term eg P1M,P1Y,P2Y,P3Y meaning month,1year,2year,3year respectively
        """
        pulumi.set(__self__, "created", created)
        if auto_renew is not None:
            pulumi.set(__self__, "auto_renew", auto_renew)
        if billing_period is not None:
            pulumi.set(__self__, "billing_period", billing_period)
        if is_free_trial is not None:
            pulumi.set(__self__, "is_free_trial", is_free_trial)
        if last_modified is not None:
            pulumi.set(__self__, "last_modified", last_modified)
        if offer_id is not None:
            pulumi.set(__self__, "offer_id", offer_id)
        if payment_channel_metadata is not None:
            pulumi.set(__self__, "payment_channel_metadata", payment_channel_metadata)
        if payment_channel_type is not None:
            pulumi.set(__self__, "payment_channel_type", payment_channel_type)
        if publisher_id is not None:
            pulumi.set(__self__, "publisher_id", publisher_id)
        if quote_id is not None:
            pulumi.set(__self__, "quote_id", quote_id)
        if sku_id is not None:
            pulumi.set(__self__, "sku_id", sku_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if store_front is not None:
            pulumi.set(__self__, "store_front", store_front)
        if term is not None:
            pulumi.set(__self__, "term", term)
        if term_unit is not None:
            pulumi.set(__self__, "term_unit", term_unit)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The created date of this resource.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> Optional[bool]:
        """
        Whether the ProfessionalService subscription will auto renew upon term end.
        """
        return pulumi.get(self, "auto_renew")

    @property
    @pulumi.getter(name="billingPeriod")
    def billing_period(self) -> Optional[str]:
        """
        The billing period eg P1M,P1Y for monthly,yearly respectively
        """
        return pulumi.get(self, "billing_period")

    @property
    @pulumi.getter(name="isFreeTrial")
    def is_free_trial(self) -> Optional[bool]:
        """
        Whether the current term is a Free Trial term
        """
        return pulumi.get(self, "is_free_trial")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> Optional[str]:
        """
        The last modifier date if this resource.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> Optional[str]:
        """
        The offer id.
        """
        return pulumi.get(self, "offer_id")

    @property
    @pulumi.getter(name="paymentChannelMetadata")
    def payment_channel_metadata(self) -> Optional[Mapping[str, str]]:
        """
        The metadata about the ProfessionalService subscription such as the AzureSubscriptionId and ResourceUri.
        """
        return pulumi.get(self, "payment_channel_metadata")

    @property
    @pulumi.getter(name="paymentChannelType")
    def payment_channel_type(self) -> Optional[str]:
        """
        The Payment channel for the ProfessionalServiceSubscription.
        """
        return pulumi.get(self, "payment_channel_type")

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> Optional[str]:
        """
        The publisher id.
        """
        return pulumi.get(self, "publisher_id")

    @property
    @pulumi.getter(name="quoteId")
    def quote_id(self) -> Optional[str]:
        """
        The quote id which the ProfessionalService will be purchase with.
        """
        return pulumi.get(self, "quote_id")

    @property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> Optional[str]:
        """
        The plan id.
        """
        return pulumi.get(self, "sku_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The ProfessionalService Subscription Status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storeFront")
    def store_front(self) -> Optional[str]:
        """
        The store front which initiates the purchase.
        """
        return pulumi.get(self, "store_front")

    @property
    @pulumi.getter
    def term(self) -> Optional['outputs.ProfessionalServicePropertiesResponseTerm']:
        """
        The current Term object.
        """
        return pulumi.get(self, "term")

    @property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> Optional[str]:
        """
        The unit term eg P1M,P1Y,P2Y,P3Y meaning month,1year,2year,3year respectively
        """
        return pulumi.get(self, "term_unit")


