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

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regional_affinity: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 reporting: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 scalable_execution: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] name: Name of account
        :param pulumi.Input[Union[str, 'EnablementStatus']] regional_affinity: This property sets the connection region for Playwright client workers to cloud-hosted browsers. If enabled, workers connect to browsers in the closest Azure region, ensuring lower latency. If disabled, workers connect to browsers in the Azure region in which the workspace was initially created.
        :param pulumi.Input[Union[str, 'EnablementStatus']] reporting: When enabled, this feature allows the workspace to upload and display test results, including artifacts like traces and screenshots, in the Playwright portal. This enables faster and more efficient troubleshooting.
        :param pulumi.Input[Union[str, 'EnablementStatus']] scalable_execution: When enabled, Playwright client workers can connect to cloud-hosted browsers. This can increase the number of parallel workers for a test run, significantly minimizing test completion durations.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if regional_affinity is None:
            regional_affinity = 'Enabled'
        if regional_affinity is not None:
            pulumi.set(__self__, "regional_affinity", regional_affinity)
        if reporting is None:
            reporting = 'Disabled'
        if reporting is not None:
            pulumi.set(__self__, "reporting", reporting)
        if scalable_execution is None:
            scalable_execution = 'Enabled'
        if scalable_execution is not None:
            pulumi.set(__self__, "scalable_execution", scalable_execution)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of account
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="regionalAffinity")
    def regional_affinity(self) -> Optional[pulumi.Input[Union[str, 'EnablementStatus']]]:
        """
        This property sets the connection region for Playwright client workers to cloud-hosted browsers. If enabled, workers connect to browsers in the closest Azure region, ensuring lower latency. If disabled, workers connect to browsers in the Azure region in which the workspace was initially created.
        """
        return pulumi.get(self, "regional_affinity")

    @regional_affinity.setter
    def regional_affinity(self, value: Optional[pulumi.Input[Union[str, 'EnablementStatus']]]):
        pulumi.set(self, "regional_affinity", value)

    @property
    @pulumi.getter
    def reporting(self) -> Optional[pulumi.Input[Union[str, 'EnablementStatus']]]:
        """
        When enabled, this feature allows the workspace to upload and display test results, including artifacts like traces and screenshots, in the Playwright portal. This enables faster and more efficient troubleshooting.
        """
        return pulumi.get(self, "reporting")

    @reporting.setter
    def reporting(self, value: Optional[pulumi.Input[Union[str, 'EnablementStatus']]]):
        pulumi.set(self, "reporting", value)

    @property
    @pulumi.getter(name="scalableExecution")
    def scalable_execution(self) -> Optional[pulumi.Input[Union[str, 'EnablementStatus']]]:
        """
        When enabled, Playwright client workers can connect to cloud-hosted browsers. This can increase the number of parallel workers for a test run, significantly minimizing test completion durations.
        """
        return pulumi.get(self, "scalable_execution")

    @scalable_execution.setter
    def scalable_execution(self, value: Optional[pulumi.Input[Union[str, 'EnablementStatus']]]):
        pulumi.set(self, "scalable_execution", value)

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


class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regional_affinity: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 reporting: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scalable_execution: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        An account resource
        Azure REST API version: 2023-10-01-preview.

        Other available API versions: 2024-02-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] name: Name of account
        :param pulumi.Input[Union[str, 'EnablementStatus']] regional_affinity: This property sets the connection region for Playwright client workers to cloud-hosted browsers. If enabled, workers connect to browsers in the closest Azure region, ensuring lower latency. If disabled, workers connect to browsers in the Azure region in which the workspace was initially created.
        :param pulumi.Input[Union[str, 'EnablementStatus']] reporting: When enabled, this feature allows the workspace to upload and display test results, including artifacts like traces and screenshots, in the Playwright portal. This enables faster and more efficient troubleshooting.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'EnablementStatus']] scalable_execution: When enabled, Playwright client workers can connect to cloud-hosted browsers. This can increase the number of parallel workers for a test run, significantly minimizing test completion durations.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An account resource
        Azure REST API version: 2023-10-01-preview.

        Other available API versions: 2024-02-01-preview.

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regional_affinity: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 reporting: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scalable_execution: Optional[pulumi.Input[Union[str, 'EnablementStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if regional_affinity is None:
                regional_affinity = 'Enabled'
            __props__.__dict__["regional_affinity"] = regional_affinity
            if reporting is None:
                reporting = 'Disabled'
            __props__.__dict__["reporting"] = reporting
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if scalable_execution is None:
                scalable_execution = 'Enabled'
            __props__.__dict__["scalable_execution"] = scalable_execution
            __props__.__dict__["tags"] = tags
            __props__.__dict__["dashboard_uri"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azureplaywrightservice/v20231001preview:Account"), pulumi.Alias(type_="azure-native:azureplaywrightservice/v20240201preview:Account")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Account, __self__).__init__(
            'azure-native:azureplaywrightservice:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccountArgs.__new__(AccountArgs)

        __props__.__dict__["dashboard_uri"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["regional_affinity"] = None
        __props__.__dict__["reporting"] = None
        __props__.__dict__["scalable_execution"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardUri")
    def dashboard_uri(self) -> pulumi.Output[str]:
        """
        The Playwright testing dashboard URI for the account resource.
        """
        return pulumi.get(self, "dashboard_uri")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="regionalAffinity")
    def regional_affinity(self) -> pulumi.Output[Optional[str]]:
        """
        This property sets the connection region for Playwright client workers to cloud-hosted browsers. If enabled, workers connect to browsers in the closest Azure region, ensuring lower latency. If disabled, workers connect to browsers in the Azure region in which the workspace was initially created.
        """
        return pulumi.get(self, "regional_affinity")

    @property
    @pulumi.getter
    def reporting(self) -> pulumi.Output[Optional[str]]:
        """
        When enabled, this feature allows the workspace to upload and display test results, including artifacts like traces and screenshots, in the Playwright portal. This enables faster and more efficient troubleshooting.
        """
        return pulumi.get(self, "reporting")

    @property
    @pulumi.getter(name="scalableExecution")
    def scalable_execution(self) -> pulumi.Output[Optional[str]]:
        """
        When enabled, Playwright client workers can connect to cloud-hosted browsers. This can increase the number of parallel workers for a test run, significantly minimizing test completion durations.
        """
        return pulumi.get(self, "scalable_execution")

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

