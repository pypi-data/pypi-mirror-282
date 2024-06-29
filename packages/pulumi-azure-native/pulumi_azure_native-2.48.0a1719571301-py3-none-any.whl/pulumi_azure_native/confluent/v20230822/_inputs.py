# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'LinkOrganizationArgs',
    'OfferDetailArgs',
    'UserDetailArgs',
]

@pulumi.input_type
class LinkOrganizationArgs:
    def __init__(__self__, *,
                 token: pulumi.Input[str]):
        """
        Link an existing Confluent organization
        :param pulumi.Input[str] token: User auth token
        """
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        """
        User auth token
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)


@pulumi.input_type
class OfferDetailArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 plan_id: pulumi.Input[str],
                 plan_name: pulumi.Input[str],
                 publisher_id: pulumi.Input[str],
                 term_unit: pulumi.Input[str],
                 private_offer_id: Optional[pulumi.Input[str]] = None,
                 private_offer_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[Union[str, 'SaaSOfferStatus']]] = None,
                 term_id: Optional[pulumi.Input[str]] = None):
        """
        Confluent Offer detail
        :param pulumi.Input[str] id: Offer Id
        :param pulumi.Input[str] plan_id: Offer Plan Id
        :param pulumi.Input[str] plan_name: Offer Plan Name
        :param pulumi.Input[str] publisher_id: Publisher Id
        :param pulumi.Input[str] term_unit: Offer Plan Term unit
        :param pulumi.Input[str] private_offer_id: Private Offer Id
        :param pulumi.Input[Sequence[pulumi.Input[str]]] private_offer_ids: Array of Private Offer Ids
        :param pulumi.Input[Union[str, 'SaaSOfferStatus']] status: SaaS Offer Status
        :param pulumi.Input[str] term_id: Offer Plan Term Id
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "plan_id", plan_id)
        pulumi.set(__self__, "plan_name", plan_name)
        pulumi.set(__self__, "publisher_id", publisher_id)
        pulumi.set(__self__, "term_unit", term_unit)
        if private_offer_id is not None:
            pulumi.set(__self__, "private_offer_id", private_offer_id)
        if private_offer_ids is not None:
            pulumi.set(__self__, "private_offer_ids", private_offer_ids)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if term_id is not None:
            pulumi.set(__self__, "term_id", term_id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Offer Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="planId")
    def plan_id(self) -> pulumi.Input[str]:
        """
        Offer Plan Id
        """
        return pulumi.get(self, "plan_id")

    @plan_id.setter
    def plan_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "plan_id", value)

    @property
    @pulumi.getter(name="planName")
    def plan_name(self) -> pulumi.Input[str]:
        """
        Offer Plan Name
        """
        return pulumi.get(self, "plan_name")

    @plan_name.setter
    def plan_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "plan_name", value)

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> pulumi.Input[str]:
        """
        Publisher Id
        """
        return pulumi.get(self, "publisher_id")

    @publisher_id.setter
    def publisher_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "publisher_id", value)

    @property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> pulumi.Input[str]:
        """
        Offer Plan Term unit
        """
        return pulumi.get(self, "term_unit")

    @term_unit.setter
    def term_unit(self, value: pulumi.Input[str]):
        pulumi.set(self, "term_unit", value)

    @property
    @pulumi.getter(name="privateOfferId")
    def private_offer_id(self) -> Optional[pulumi.Input[str]]:
        """
        Private Offer Id
        """
        return pulumi.get(self, "private_offer_id")

    @private_offer_id.setter
    def private_offer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_offer_id", value)

    @property
    @pulumi.getter(name="privateOfferIds")
    def private_offer_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Array of Private Offer Ids
        """
        return pulumi.get(self, "private_offer_ids")

    @private_offer_ids.setter
    def private_offer_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "private_offer_ids", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'SaaSOfferStatus']]]:
        """
        SaaS Offer Status
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'SaaSOfferStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="termId")
    def term_id(self) -> Optional[pulumi.Input[str]]:
        """
        Offer Plan Term Id
        """
        return pulumi.get(self, "term_id")

    @term_id.setter
    def term_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "term_id", value)


@pulumi.input_type
class UserDetailArgs:
    def __init__(__self__, *,
                 email_address: pulumi.Input[str],
                 aad_email: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 user_principal_name: Optional[pulumi.Input[str]] = None):
        """
        Subscriber detail
        :param pulumi.Input[str] email_address: Email address
        :param pulumi.Input[str] aad_email: AAD email address
        :param pulumi.Input[str] first_name: First name
        :param pulumi.Input[str] last_name: Last name
        :param pulumi.Input[str] user_principal_name: User principal name
        """
        pulumi.set(__self__, "email_address", email_address)
        if aad_email is not None:
            pulumi.set(__self__, "aad_email", aad_email)
        if first_name is not None:
            pulumi.set(__self__, "first_name", first_name)
        if last_name is not None:
            pulumi.set(__self__, "last_name", last_name)
        if user_principal_name is not None:
            pulumi.set(__self__, "user_principal_name", user_principal_name)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[str]:
        """
        Email address
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="aadEmail")
    def aad_email(self) -> Optional[pulumi.Input[str]]:
        """
        AAD email address
        """
        return pulumi.get(self, "aad_email")

    @aad_email.setter
    def aad_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aad_email", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter(name="userPrincipalName")
    def user_principal_name(self) -> Optional[pulumi.Input[str]]:
        """
        User principal name
        """
        return pulumi.get(self, "user_principal_name")

    @user_principal_name.setter
    def user_principal_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_principal_name", value)


