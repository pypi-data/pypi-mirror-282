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
from ._enums import *

__all__ = ['TestLineArgs', 'TestLine']

@pulumi.input_type
class TestLineArgs:
    def __init__(__self__, *,
                 communications_gateway_name: pulumi.Input[str],
                 phone_number: pulumi.Input[str],
                 purpose: pulumi.Input['TestLinePurpose'],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 test_line_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TestLine resource.
        :param pulumi.Input[str] communications_gateway_name: Unique identifier for this deployment
        :param pulumi.Input[str] phone_number: The phone number
        :param pulumi.Input['TestLinePurpose'] purpose: Purpose of this test line, e.g. automated or manual testing
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] test_line_name: Unique identifier for this test line
        """
        pulumi.set(__self__, "communications_gateway_name", communications_gateway_name)
        pulumi.set(__self__, "phone_number", phone_number)
        pulumi.set(__self__, "purpose", purpose)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if test_line_name is not None:
            pulumi.set(__self__, "test_line_name", test_line_name)

    @property
    @pulumi.getter(name="communicationsGatewayName")
    def communications_gateway_name(self) -> pulumi.Input[str]:
        """
        Unique identifier for this deployment
        """
        return pulumi.get(self, "communications_gateway_name")

    @communications_gateway_name.setter
    def communications_gateway_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "communications_gateway_name", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[str]:
        """
        The phone number
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "phone_number", value)

    @property
    @pulumi.getter
    def purpose(self) -> pulumi.Input['TestLinePurpose']:
        """
        Purpose of this test line, e.g. automated or manual testing
        """
        return pulumi.get(self, "purpose")

    @purpose.setter
    def purpose(self, value: pulumi.Input['TestLinePurpose']):
        pulumi.set(self, "purpose", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="testLineName")
    def test_line_name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier for this test line
        """
        return pulumi.get(self, "test_line_name")

    @test_line_name.setter
    def test_line_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "test_line_name", value)


class TestLine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 communications_gateway_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input['TestLinePurpose']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 test_line_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A TestLine resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] communications_gateway_name: Unique identifier for this deployment
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] phone_number: The phone number
        :param pulumi.Input['TestLinePurpose'] purpose: Purpose of this test line, e.g. automated or manual testing
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] test_line_name: Unique identifier for this test line
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TestLineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A TestLine resource

        :param str resource_name: The name of the resource.
        :param TestLineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TestLineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 communications_gateway_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input['TestLinePurpose']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 test_line_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TestLineArgs.__new__(TestLineArgs)

            if communications_gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'communications_gateway_name'")
            __props__.__dict__["communications_gateway_name"] = communications_gateway_name
            __props__.__dict__["location"] = location
            if phone_number is None and not opts.urn:
                raise TypeError("Missing required property 'phone_number'")
            __props__.__dict__["phone_number"] = phone_number
            if purpose is None and not opts.urn:
                raise TypeError("Missing required property 'purpose'")
            __props__.__dict__["purpose"] = purpose
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["test_line_name"] = test_line_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:voiceservices:TestLine"), pulumi.Alias(type_="azure-native:voiceservices/v20230131:TestLine"), pulumi.Alias(type_="azure-native:voiceservices/v20230403:TestLine"), pulumi.Alias(type_="azure-native:voiceservices/v20230901:TestLine")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TestLine, __self__).__init__(
            'azure-native:voiceservices/v20221201preview:TestLine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TestLine':
        """
        Get an existing TestLine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TestLineArgs.__new__(TestLineArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["phone_number"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["purpose"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return TestLine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Output[str]:
        """
        The phone number
        """
        return pulumi.get(self, "phone_number")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[str]:
        """
        Purpose of this test line, e.g. automated or manual testing
        """
        return pulumi.get(self, "purpose")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

