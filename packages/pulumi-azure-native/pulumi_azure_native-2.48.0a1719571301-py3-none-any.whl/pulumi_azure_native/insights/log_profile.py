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
from ._inputs import *

__all__ = ['LogProfileArgs', 'LogProfile']

@pulumi.input_type
class LogProfileArgs:
    def __init__(__self__, *,
                 categories: pulumi.Input[Sequence[pulumi.Input[str]]],
                 locations: pulumi.Input[Sequence[pulumi.Input[str]]],
                 retention_policy: pulumi.Input['RetentionPolicyArgs'],
                 location: Optional[pulumi.Input[str]] = None,
                 log_profile_name: Optional[pulumi.Input[str]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LogProfile resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] categories: the categories of the logs. These categories are created as is convenient to the user. Some values are: 'Write', 'Delete', and/or 'Action.'
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locations: List of regions for which Activity Log events should be stored or streamed. It is a comma separated list of valid ARM locations including the 'global' location.
        :param pulumi.Input['RetentionPolicyArgs'] retention_policy: the retention policy for the events in the log.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] log_profile_name: The name of the log profile.
        :param pulumi.Input[str] service_bus_rule_id: The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format: '{service bus resource ID}/authorizationrules/{key name}'.
        :param pulumi.Input[str] storage_account_id: the resource id of the storage account to which you would like to send the Activity Log.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "categories", categories)
        pulumi.set(__self__, "locations", locations)
        pulumi.set(__self__, "retention_policy", retention_policy)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if log_profile_name is not None:
            pulumi.set(__self__, "log_profile_name", log_profile_name)
        if service_bus_rule_id is not None:
            pulumi.set(__self__, "service_bus_rule_id", service_bus_rule_id)
        if storage_account_id is not None:
            pulumi.set(__self__, "storage_account_id", storage_account_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def categories(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        the categories of the logs. These categories are created as is convenient to the user. Some values are: 'Write', 'Delete', and/or 'Action.'
        """
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter
    def locations(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of regions for which Activity Log events should be stored or streamed. It is a comma separated list of valid ARM locations including the 'global' location.
        """
        return pulumi.get(self, "locations")

    @locations.setter
    def locations(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "locations", value)

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> pulumi.Input['RetentionPolicyArgs']:
        """
        the retention policy for the events in the log.
        """
        return pulumi.get(self, "retention_policy")

    @retention_policy.setter
    def retention_policy(self, value: pulumi.Input['RetentionPolicyArgs']):
        pulumi.set(self, "retention_policy", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="logProfileName")
    def log_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the log profile.
        """
        return pulumi.get(self, "log_profile_name")

    @log_profile_name.setter
    def log_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_profile_name", value)

    @property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format: '{service bus resource ID}/authorizationrules/{key name}'.
        """
        return pulumi.get(self, "service_bus_rule_id")

    @service_bus_rule_id.setter
    def service_bus_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_bus_rule_id", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        the resource id of the storage account to which you would like to send the Activity Log.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class LogProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 log_profile_name: Optional[pulumi.Input[str]] = None,
                 retention_policy: Optional[pulumi.Input[pulumi.InputType['RetentionPolicyArgs']]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The log profile resource.
        Azure REST API version: 2016-03-01. Prior API version in Azure Native 1.x: 2016-03-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] categories: the categories of the logs. These categories are created as is convenient to the user. Some values are: 'Write', 'Delete', and/or 'Action.'
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locations: List of regions for which Activity Log events should be stored or streamed. It is a comma separated list of valid ARM locations including the 'global' location.
        :param pulumi.Input[str] log_profile_name: The name of the log profile.
        :param pulumi.Input[pulumi.InputType['RetentionPolicyArgs']] retention_policy: the retention policy for the events in the log.
        :param pulumi.Input[str] service_bus_rule_id: The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format: '{service bus resource ID}/authorizationrules/{key name}'.
        :param pulumi.Input[str] storage_account_id: the resource id of the storage account to which you would like to send the Activity Log.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The log profile resource.
        Azure REST API version: 2016-03-01. Prior API version in Azure Native 1.x: 2016-03-01.

        :param str resource_name: The name of the resource.
        :param LogProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 log_profile_name: Optional[pulumi.Input[str]] = None,
                 retention_policy: Optional[pulumi.Input[pulumi.InputType['RetentionPolicyArgs']]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogProfileArgs.__new__(LogProfileArgs)

            if categories is None and not opts.urn:
                raise TypeError("Missing required property 'categories'")
            __props__.__dict__["categories"] = categories
            __props__.__dict__["location"] = location
            if locations is None and not opts.urn:
                raise TypeError("Missing required property 'locations'")
            __props__.__dict__["locations"] = locations
            __props__.__dict__["log_profile_name"] = log_profile_name
            if retention_policy is None and not opts.urn:
                raise TypeError("Missing required property 'retention_policy'")
            __props__.__dict__["retention_policy"] = retention_policy
            __props__.__dict__["service_bus_rule_id"] = service_bus_rule_id
            __props__.__dict__["storage_account_id"] = storage_account_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights/v20160301:LogProfile")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LogProfile, __self__).__init__(
            'azure-native:insights:LogProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LogProfile':
        """
        Get an existing LogProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LogProfileArgs.__new__(LogProfileArgs)

        __props__.__dict__["categories"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["locations"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["retention_policy"] = None
        __props__.__dict__["service_bus_rule_id"] = None
        __props__.__dict__["storage_account_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return LogProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Sequence[str]]:
        """
        the categories of the logs. These categories are created as is convenient to the user. Some values are: 'Write', 'Delete', and/or 'Action.'
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def locations(self) -> pulumi.Output[Sequence[str]]:
        """
        List of regions for which Activity Log events should be stored or streamed. It is a comma separated list of valid ARM locations including the 'global' location.
        """
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> pulumi.Output['outputs.RetentionPolicyResponse']:
        """
        the retention policy for the events in the log.
        """
        return pulumi.get(self, "retention_policy")

    @property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> pulumi.Output[Optional[str]]:
        """
        The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format: '{service bus resource ID}/authorizationrules/{key name}'.
        """
        return pulumi.get(self, "service_bus_rule_id")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        the resource id of the storage account to which you would like to send the Activity Log.
        """
        return pulumi.get(self, "storage_account_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

