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
from ._inputs import *

__all__ = ['NamespaceAuthorizationRuleArgs', 'NamespaceAuthorizationRule']

@pulumi.input_type
class NamespaceAuthorizationRuleArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 properties: pulumi.Input['SharedAccessAuthorizationRulePropertiesArgs'],
                 resource_group_name: pulumi.Input[str],
                 authorization_rule_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NamespaceAuthorizationRule resource.
        :param pulumi.Input[str] namespace_name: The namespace name.
        :param pulumi.Input['SharedAccessAuthorizationRulePropertiesArgs'] properties: Properties of the Namespace AuthorizationRules.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] authorization_rule_name: Authorization Rule Name.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authorization_rule_name is not None:
            pulumi.set(__self__, "authorization_rule_name", authorization_rule_name)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The namespace name.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['SharedAccessAuthorizationRulePropertiesArgs']:
        """
        Properties of the Namespace AuthorizationRules.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['SharedAccessAuthorizationRulePropertiesArgs']):
        pulumi.set(self, "properties", value)

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
    @pulumi.getter(name="authorizationRuleName")
    def authorization_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Authorization Rule Name.
        """
        return pulumi.get(self, "authorization_rule_name")

    @authorization_rule_name.setter
    def authorization_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_rule_name", value)


class NamespaceAuthorizationRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_rule_name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['SharedAccessAuthorizationRulePropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Description of a Namespace AuthorizationRules.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_rule_name: Authorization Rule Name.
        :param pulumi.Input[str] namespace_name: The namespace name.
        :param pulumi.Input[pulumi.InputType['SharedAccessAuthorizationRulePropertiesArgs']] properties: Properties of the Namespace AuthorizationRules.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceAuthorizationRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of a Namespace AuthorizationRules.

        :param str resource_name: The name of the resource.
        :param NamespaceAuthorizationRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceAuthorizationRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_rule_name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['SharedAccessAuthorizationRulePropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceAuthorizationRuleArgs.__new__(NamespaceAuthorizationRuleArgs)

            __props__.__dict__["authorization_rule_name"] = authorization_rule_name
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["claim_type"] = None
            __props__.__dict__["claim_value"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["key_name"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["modified_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["primary_key"] = None
            __props__.__dict__["revision"] = None
            __props__.__dict__["rights"] = None
            __props__.__dict__["secondary_key"] = None
            __props__.__dict__["sku"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:notificationhubs:NamespaceAuthorizationRule"), pulumi.Alias(type_="azure-native:notificationhubs/v20160301:NamespaceAuthorizationRule"), pulumi.Alias(type_="azure-native:notificationhubs/v20230101preview:NamespaceAuthorizationRule"), pulumi.Alias(type_="azure-native:notificationhubs/v20230901:NamespaceAuthorizationRule"), pulumi.Alias(type_="azure-native:notificationhubs/v20231001preview:NamespaceAuthorizationRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NamespaceAuthorizationRule, __self__).__init__(
            'azure-native:notificationhubs/v20170401:NamespaceAuthorizationRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NamespaceAuthorizationRule':
        """
        Get an existing NamespaceAuthorizationRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceAuthorizationRuleArgs.__new__(NamespaceAuthorizationRuleArgs)

        __props__.__dict__["claim_type"] = None
        __props__.__dict__["claim_value"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["key_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["primary_key"] = None
        __props__.__dict__["revision"] = None
        __props__.__dict__["rights"] = None
        __props__.__dict__["secondary_key"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return NamespaceAuthorizationRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="claimType")
    def claim_type(self) -> pulumi.Output[str]:
        """
        A string that describes the claim type
        """
        return pulumi.get(self, "claim_type")

    @property
    @pulumi.getter(name="claimValue")
    def claim_value(self) -> pulumi.Output[str]:
        """
        A string that describes the claim value
        """
        return pulumi.get(self, "claim_value")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        The created time for this rule
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[str]:
        """
        A string that describes the authorization rule.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="modifiedTime")
    def modified_time(self) -> pulumi.Output[str]:
        """
        The last modified time for this rule
        """
        return pulumi.get(self, "modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> pulumi.Output[str]:
        """
        A base64-encoded 256-bit primary key for signing and validating the SAS token.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Output[int]:
        """
        The revision number for the rule
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter
    def rights(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The rights associated with the rule.
        """
        return pulumi.get(self, "rights")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> pulumi.Output[str]:
        """
        A base64-encoded 256-bit primary key for signing and validating the SAS token.
        """
        return pulumi.get(self, "secondary_key")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the created namespace
        """
        return pulumi.get(self, "sku")

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
        Resource type
        """
        return pulumi.get(self, "type")

