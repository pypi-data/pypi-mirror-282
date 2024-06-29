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

__all__ = ['UserRuleCollectionArgs', 'UserRuleCollection']

@pulumi.input_type
class UserRuleCollectionArgs:
    def __init__(__self__, *,
                 applies_to_groups: pulumi.Input[Sequence[pulumi.Input['NetworkManagerSecurityGroupItemArgs']]],
                 configuration_name: pulumi.Input[str],
                 network_manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 rule_collection_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserRuleCollection resource.
        :param pulumi.Input[Sequence[pulumi.Input['NetworkManagerSecurityGroupItemArgs']]] applies_to_groups: Groups for configuration
        :param pulumi.Input[str] configuration_name: The name of the network manager Security Configuration.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] description: A description of the user rule collection.
        :param pulumi.Input[str] rule_collection_name: The name of the network manager security Configuration rule collection.
        """
        pulumi.set(__self__, "applies_to_groups", applies_to_groups)
        pulumi.set(__self__, "configuration_name", configuration_name)
        pulumi.set(__self__, "network_manager_name", network_manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if rule_collection_name is not None:
            pulumi.set(__self__, "rule_collection_name", rule_collection_name)

    @property
    @pulumi.getter(name="appliesToGroups")
    def applies_to_groups(self) -> pulumi.Input[Sequence[pulumi.Input['NetworkManagerSecurityGroupItemArgs']]]:
        """
        Groups for configuration
        """
        return pulumi.get(self, "applies_to_groups")

    @applies_to_groups.setter
    def applies_to_groups(self, value: pulumi.Input[Sequence[pulumi.Input['NetworkManagerSecurityGroupItemArgs']]]):
        pulumi.set(self, "applies_to_groups", value)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager Security Configuration.
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager.
        """
        return pulumi.get(self, "network_manager_name")

    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_manager_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the user rule collection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ruleCollectionName")
    def rule_collection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network manager security Configuration rule collection.
        """
        return pulumi.get(self, "rule_collection_name")

    @rule_collection_name.setter
    def rule_collection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_collection_name", value)


class UserRuleCollection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 applies_to_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkManagerSecurityGroupItemArgs']]]]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collection_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the user rule collection.
        Azure REST API version: 2022-04-01-preview. Prior API version in Azure Native 1.x: 2021-02-01-preview.

        Other available API versions: 2021-02-01-preview, 2021-05-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkManagerSecurityGroupItemArgs']]]] applies_to_groups: Groups for configuration
        :param pulumi.Input[str] configuration_name: The name of the network manager Security Configuration.
        :param pulumi.Input[str] description: A description of the user rule collection.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] rule_collection_name: The name of the network manager security Configuration rule collection.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserRuleCollectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the user rule collection.
        Azure REST API version: 2022-04-01-preview. Prior API version in Azure Native 1.x: 2021-02-01-preview.

        Other available API versions: 2021-02-01-preview, 2021-05-01-preview.

        :param str resource_name: The name of the resource.
        :param UserRuleCollectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserRuleCollectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 applies_to_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkManagerSecurityGroupItemArgs']]]]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_collection_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserRuleCollectionArgs.__new__(UserRuleCollectionArgs)

            if applies_to_groups is None and not opts.urn:
                raise TypeError("Missing required property 'applies_to_groups'")
            __props__.__dict__["applies_to_groups"] = applies_to_groups
            if configuration_name is None and not opts.urn:
                raise TypeError("Missing required property 'configuration_name'")
            __props__.__dict__["configuration_name"] = configuration_name
            __props__.__dict__["description"] = description
            if network_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_manager_name'")
            __props__.__dict__["network_manager_name"] = network_manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rule_collection_name"] = rule_collection_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20210201preview:UserRuleCollection"), pulumi.Alias(type_="azure-native:network/v20210501preview:UserRuleCollection"), pulumi.Alias(type_="azure-native:network/v20220201preview:UserRuleCollection"), pulumi.Alias(type_="azure-native:network/v20220401preview:UserRuleCollection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(UserRuleCollection, __self__).__init__(
            'azure-native:network:UserRuleCollection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserRuleCollection':
        """
        Get an existing UserRuleCollection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserRuleCollectionArgs.__new__(UserRuleCollectionArgs)

        __props__.__dict__["applies_to_groups"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return UserRuleCollection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appliesToGroups")
    def applies_to_groups(self) -> pulumi.Output[Sequence['outputs.NetworkManagerSecurityGroupItemResponse']]:
        """
        Groups for configuration
        """
        return pulumi.get(self, "applies_to_groups")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the user rule collection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

