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

__all__ = ['PrefixListGlobalRulestackArgs', 'PrefixListGlobalRulestack']

@pulumi.input_type
class PrefixListGlobalRulestackArgs:
    def __init__(__self__, *,
                 global_rulestack_name: pulumi.Input[str],
                 prefix_list: pulumi.Input[Sequence[pulumi.Input[str]]],
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrefixListGlobalRulestack resource.
        :param pulumi.Input[str] global_rulestack_name: GlobalRulestack resource name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] prefix_list: prefix list
        :param pulumi.Input[str] audit_comment: comment for this object
        :param pulumi.Input[str] description: prefix description
        :param pulumi.Input[str] name: Local Rule priority
        """
        pulumi.set(__self__, "global_rulestack_name", global_rulestack_name)
        pulumi.set(__self__, "prefix_list", prefix_list)
        if audit_comment is not None:
            pulumi.set(__self__, "audit_comment", audit_comment)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="globalRulestackName")
    def global_rulestack_name(self) -> pulumi.Input[str]:
        """
        GlobalRulestack resource name
        """
        return pulumi.get(self, "global_rulestack_name")

    @global_rulestack_name.setter
    def global_rulestack_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "global_rulestack_name", value)

    @property
    @pulumi.getter(name="prefixList")
    def prefix_list(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        prefix list
        """
        return pulumi.get(self, "prefix_list")

    @prefix_list.setter
    def prefix_list(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "prefix_list", value)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[pulumi.Input[str]]:
        """
        comment for this object
        """
        return pulumi.get(self, "audit_comment")

    @audit_comment.setter
    def audit_comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "audit_comment", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        prefix description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Local Rule priority
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class PrefixListGlobalRulestack(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_rulestack_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prefix_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        GlobalRulestack prefixList

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] audit_comment: comment for this object
        :param pulumi.Input[str] description: prefix description
        :param pulumi.Input[str] global_rulestack_name: GlobalRulestack resource name
        :param pulumi.Input[str] name: Local Rule priority
        :param pulumi.Input[Sequence[pulumi.Input[str]]] prefix_list: prefix list
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrefixListGlobalRulestackArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        GlobalRulestack prefixList

        :param str resource_name: The name of the resource.
        :param PrefixListGlobalRulestackArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrefixListGlobalRulestackArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 audit_comment: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_rulestack_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prefix_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrefixListGlobalRulestackArgs.__new__(PrefixListGlobalRulestackArgs)

            __props__.__dict__["audit_comment"] = audit_comment
            __props__.__dict__["description"] = description
            if global_rulestack_name is None and not opts.urn:
                raise TypeError("Missing required property 'global_rulestack_name'")
            __props__.__dict__["global_rulestack_name"] = global_rulestack_name
            __props__.__dict__["name"] = name
            if prefix_list is None and not opts.urn:
                raise TypeError("Missing required property 'prefix_list'")
            __props__.__dict__["prefix_list"] = prefix_list
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cloudngfw:PrefixListGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829:PrefixListGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20220829preview:PrefixListGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20230901:PrefixListGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20231010preview:PrefixListGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20240119preview:PrefixListGlobalRulestack"), pulumi.Alias(type_="azure-native:cloudngfw/v20240207preview:PrefixListGlobalRulestack")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrefixListGlobalRulestack, __self__).__init__(
            'azure-native:cloudngfw/v20230901preview:PrefixListGlobalRulestack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrefixListGlobalRulestack':
        """
        Get an existing PrefixListGlobalRulestack resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrefixListGlobalRulestackArgs.__new__(PrefixListGlobalRulestackArgs)

        __props__.__dict__["audit_comment"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["prefix_list"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PrefixListGlobalRulestack(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> pulumi.Output[Optional[str]]:
        """
        comment for this object
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        prefix description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        etag info
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="prefixList")
    def prefix_list(self) -> pulumi.Output[Sequence[str]]:
        """
        prefix list
        """
        return pulumi.get(self, "prefix_list")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

