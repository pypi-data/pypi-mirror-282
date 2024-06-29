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
    'AddressArgs',
    'ContactDetailsArgs',
    'DataResidencyArgs',
    'SkuArgs',
]

@pulumi.input_type
class AddressArgs:
    def __init__(__self__, *,
                 country: pulumi.Input[str],
                 address_line1: Optional[pulumi.Input[str]] = None,
                 address_line2: Optional[pulumi.Input[str]] = None,
                 address_line3: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        The shipping address of the customer.
        :param pulumi.Input[str] country: The country name.
        :param pulumi.Input[str] address_line1: The address line1.
        :param pulumi.Input[str] address_line2: The address line2.
        :param pulumi.Input[str] address_line3: The address line3.
        :param pulumi.Input[str] city: The city name.
        :param pulumi.Input[str] postal_code: The postal code.
        :param pulumi.Input[str] state: The state name.
        """
        pulumi.set(__self__, "country", country)
        if address_line1 is not None:
            pulumi.set(__self__, "address_line1", address_line1)
        if address_line2 is not None:
            pulumi.set(__self__, "address_line2", address_line2)
        if address_line3 is not None:
            pulumi.set(__self__, "address_line3", address_line3)
        if city is not None:
            pulumi.set(__self__, "city", city)
        if postal_code is not None:
            pulumi.set(__self__, "postal_code", postal_code)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def country(self) -> pulumi.Input[str]:
        """
        The country name.
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: pulumi.Input[str]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[str]]:
        """
        The address line1.
        """
        return pulumi.get(self, "address_line1")

    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line1", value)

    @property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[str]]:
        """
        The address line2.
        """
        return pulumi.get(self, "address_line2")

    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line2", value)

    @property
    @pulumi.getter(name="addressLine3")
    def address_line3(self) -> Optional[pulumi.Input[str]]:
        """
        The address line3.
        """
        return pulumi.get(self, "address_line3")

    @address_line3.setter
    def address_line3(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line3", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        The city name.
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[str]]:
        """
        The postal code.
        """
        return pulumi.get(self, "postal_code")

    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "postal_code", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state name.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class ContactDetailsArgs:
    def __init__(__self__, *,
                 company_name: pulumi.Input[str],
                 contact_person: pulumi.Input[str],
                 email_list: pulumi.Input[Sequence[pulumi.Input[str]]],
                 phone: pulumi.Input[str]):
        """
        Contains all the contact details of the customer.
        :param pulumi.Input[str] company_name: The name of the company.
        :param pulumi.Input[str] contact_person: The contact person name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_list: The email list.
        :param pulumi.Input[str] phone: The phone number.
        """
        pulumi.set(__self__, "company_name", company_name)
        pulumi.set(__self__, "contact_person", contact_person)
        pulumi.set(__self__, "email_list", email_list)
        pulumi.set(__self__, "phone", phone)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> pulumi.Input[str]:
        """
        The name of the company.
        """
        return pulumi.get(self, "company_name")

    @company_name.setter
    def company_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "company_name", value)

    @property
    @pulumi.getter(name="contactPerson")
    def contact_person(self) -> pulumi.Input[str]:
        """
        The contact person name.
        """
        return pulumi.get(self, "contact_person")

    @contact_person.setter
    def contact_person(self, value: pulumi.Input[str]):
        pulumi.set(self, "contact_person", value)

    @property
    @pulumi.getter(name="emailList")
    def email_list(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The email list.
        """
        return pulumi.get(self, "email_list")

    @email_list.setter
    def email_list(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "email_list", value)

    @property
    @pulumi.getter
    def phone(self) -> pulumi.Input[str]:
        """
        The phone number.
        """
        return pulumi.get(self, "phone")

    @phone.setter
    def phone(self, value: pulumi.Input[str]):
        pulumi.set(self, "phone", value)


@pulumi.input_type
class DataResidencyArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input[Union[str, 'DataResidencyType']]] = None):
        """
        Wraps data-residency related information for edge-resource and this should be used with ARM layer.
        :param pulumi.Input[Union[str, 'DataResidencyType']] type: DataResidencyType enum
        """
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'DataResidencyType']]]:
        """
        DataResidencyType enum
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'DataResidencyType']]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[Union[str, 'SkuName']]] = None,
                 tier: Optional[pulumi.Input[Union[str, 'SkuTier']]] = None):
        """
        The SKU type.
        :param pulumi.Input[Union[str, 'SkuName']] name: SKU name.
        :param pulumi.Input[Union[str, 'SkuTier']] tier: The SKU tier. This is based on the SKU name.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[str, 'SkuName']]]:
        """
        SKU name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[str, 'SkuName']]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[str, 'SkuTier']]]:
        """
        The SKU tier. This is based on the SKU name.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[str, 'SkuTier']]]):
        pulumi.set(self, "tier", value)


