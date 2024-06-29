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
from ._inputs import *

__all__ = ['MarkupRuleArgs', 'MarkupRule']

@pulumi.input_type
class MarkupRuleArgs:
    def __init__(__self__, *,
                 billing_account_id: pulumi.Input[str],
                 billing_profile_id: pulumi.Input[str],
                 customer_details: pulumi.Input['CustomerMetadataArgs'],
                 percentage: pulumi.Input[float],
                 start_date: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MarkupRule resource.
        :param pulumi.Input[str] billing_account_id: BillingAccount ID
        :param pulumi.Input[str] billing_profile_id: BillingProfile ID
        :param pulumi.Input['CustomerMetadataArgs'] customer_details: Customer information for the markup rule.
        :param pulumi.Input[float] percentage: The markup percentage of the rule.
        :param pulumi.Input[str] start_date: Starting date of the markup rule.
        :param pulumi.Input[str] description: The description of the markup rule.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[str] end_date: Ending date of the markup rule.
        :param pulumi.Input[str] name: Markup rule name.
        """
        pulumi.set(__self__, "billing_account_id", billing_account_id)
        pulumi.set(__self__, "billing_profile_id", billing_profile_id)
        pulumi.set(__self__, "customer_details", customer_details)
        pulumi.set(__self__, "percentage", percentage)
        pulumi.set(__self__, "start_date", start_date)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[str]:
        """
        BillingAccount ID
        """
        return pulumi.get(self, "billing_account_id")

    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_account_id", value)

    @property
    @pulumi.getter(name="billingProfileId")
    def billing_profile_id(self) -> pulumi.Input[str]:
        """
        BillingProfile ID
        """
        return pulumi.get(self, "billing_profile_id")

    @billing_profile_id.setter
    def billing_profile_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_profile_id", value)

    @property
    @pulumi.getter(name="customerDetails")
    def customer_details(self) -> pulumi.Input['CustomerMetadataArgs']:
        """
        Customer information for the markup rule.
        """
        return pulumi.get(self, "customer_details")

    @customer_details.setter
    def customer_details(self, value: pulumi.Input['CustomerMetadataArgs']):
        pulumi.set(self, "customer_details", value)

    @property
    @pulumi.getter
    def percentage(self) -> pulumi.Input[float]:
        """
        The markup percentage of the rule.
        """
        return pulumi.get(self, "percentage")

    @percentage.setter
    def percentage(self, value: pulumi.Input[float]):
        pulumi.set(self, "percentage", value)

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Input[str]:
        """
        Starting date of the markup rule.
        """
        return pulumi.get(self, "start_date")

    @start_date.setter
    def start_date(self, value: pulumi.Input[str]):
        pulumi.set(self, "start_date", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the markup rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[str]]:
        """
        Ending date of the markup rule.
        """
        return pulumi.get(self, "end_date")

    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Markup rule name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class MarkupRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 billing_profile_id: Optional[pulumi.Input[str]] = None,
                 customer_details: Optional[pulumi.Input[pulumi.InputType['CustomerMetadataArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 percentage: Optional[pulumi.Input[float]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Markup rule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] billing_account_id: BillingAccount ID
        :param pulumi.Input[str] billing_profile_id: BillingProfile ID
        :param pulumi.Input[pulumi.InputType['CustomerMetadataArgs']] customer_details: Customer information for the markup rule.
        :param pulumi.Input[str] description: The description of the markup rule.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[str] end_date: Ending date of the markup rule.
        :param pulumi.Input[str] name: Markup rule name.
        :param pulumi.Input[float] percentage: The markup percentage of the rule.
        :param pulumi.Input[str] start_date: Starting date of the markup rule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MarkupRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Markup rule

        :param str resource_name: The name of the resource.
        :param MarkupRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MarkupRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 billing_profile_id: Optional[pulumi.Input[str]] = None,
                 customer_details: Optional[pulumi.Input[pulumi.InputType['CustomerMetadataArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 percentage: Optional[pulumi.Input[float]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MarkupRuleArgs.__new__(MarkupRuleArgs)

            if billing_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'billing_account_id'")
            __props__.__dict__["billing_account_id"] = billing_account_id
            if billing_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'billing_profile_id'")
            __props__.__dict__["billing_profile_id"] = billing_profile_id
            if customer_details is None and not opts.urn:
                raise TypeError("Missing required property 'customer_details'")
            __props__.__dict__["customer_details"] = customer_details
            __props__.__dict__["description"] = description
            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["end_date"] = end_date
            __props__.__dict__["name"] = name
            if percentage is None and not opts.urn:
                raise TypeError("Missing required property 'percentage'")
            __props__.__dict__["percentage"] = percentage
            if start_date is None and not opts.urn:
                raise TypeError("Missing required property 'start_date'")
            __props__.__dict__["start_date"] = start_date
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement:MarkupRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MarkupRule, __self__).__init__(
            'azure-native:costmanagement/v20221005preview:MarkupRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MarkupRule':
        """
        Get an existing MarkupRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MarkupRuleArgs.__new__(MarkupRuleArgs)

        __props__.__dict__["customer_details"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["end_date"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["percentage"] = None
        __props__.__dict__["start_date"] = None
        __props__.__dict__["type"] = None
        return MarkupRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customerDetails")
    def customer_details(self) -> pulumi.Output['outputs.CustomerMetadataResponse']:
        """
        Customer information for the markup rule.
        """
        return pulumi.get(self, "customer_details")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the markup rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[str]]:
        """
        Ending date of the markup rule.
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def percentage(self) -> pulumi.Output[float]:
        """
        The markup percentage of the rule.
        """
        return pulumi.get(self, "percentage")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[str]:
        """
        Starting date of the markup rule.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

