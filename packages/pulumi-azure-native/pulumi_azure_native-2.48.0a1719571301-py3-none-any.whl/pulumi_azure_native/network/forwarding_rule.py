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
from ._inputs import *

__all__ = ['ForwardingRuleArgs', 'ForwardingRule']

@pulumi.input_type
class ForwardingRuleArgs:
    def __init__(__self__, *,
                 dns_forwarding_ruleset_name: pulumi.Input[str],
                 domain_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 target_dns_servers: pulumi.Input[Sequence[pulumi.Input['TargetDnsServerArgs']]],
                 forwarding_rule_name: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_state: Optional[pulumi.Input[Union[str, 'ForwardingRuleState']]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ForwardingRule resource.
        :param pulumi.Input[str] dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :param pulumi.Input[str] domain_name: The domain name for the forwarding rule.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['TargetDnsServerArgs']]] target_dns_servers: DNS servers to forward the DNS query to.
        :param pulumi.Input[str] forwarding_rule_name: The name of the forwarding rule.
        :param pulumi.Input[Union[str, 'ForwardingRuleState']] forwarding_rule_state: The state of forwarding rule.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Metadata attached to the forwarding rule.
        """
        pulumi.set(__self__, "dns_forwarding_ruleset_name", dns_forwarding_ruleset_name)
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "target_dns_servers", target_dns_servers)
        if forwarding_rule_name is not None:
            pulumi.set(__self__, "forwarding_rule_name", forwarding_rule_name)
        if forwarding_rule_state is not None:
            pulumi.set(__self__, "forwarding_rule_state", forwarding_rule_state)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)

    @property
    @pulumi.getter(name="dnsForwardingRulesetName")
    def dns_forwarding_ruleset_name(self) -> pulumi.Input[str]:
        """
        The name of the DNS forwarding ruleset.
        """
        return pulumi.get(self, "dns_forwarding_ruleset_name")

    @dns_forwarding_ruleset_name.setter
    def dns_forwarding_ruleset_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "dns_forwarding_ruleset_name", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The domain name for the forwarding rule.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

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
    @pulumi.getter(name="targetDnsServers")
    def target_dns_servers(self) -> pulumi.Input[Sequence[pulumi.Input['TargetDnsServerArgs']]]:
        """
        DNS servers to forward the DNS query to.
        """
        return pulumi.get(self, "target_dns_servers")

    @target_dns_servers.setter
    def target_dns_servers(self, value: pulumi.Input[Sequence[pulumi.Input['TargetDnsServerArgs']]]):
        pulumi.set(self, "target_dns_servers", value)

    @property
    @pulumi.getter(name="forwardingRuleName")
    def forwarding_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the forwarding rule.
        """
        return pulumi.get(self, "forwarding_rule_name")

    @forwarding_rule_name.setter
    def forwarding_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "forwarding_rule_name", value)

    @property
    @pulumi.getter(name="forwardingRuleState")
    def forwarding_rule_state(self) -> Optional[pulumi.Input[Union[str, 'ForwardingRuleState']]]:
        """
        The state of forwarding rule.
        """
        return pulumi.get(self, "forwarding_rule_state")

    @forwarding_rule_state.setter
    def forwarding_rule_state(self, value: Optional[pulumi.Input[Union[str, 'ForwardingRuleState']]]):
        pulumi.set(self, "forwarding_rule_state", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Metadata attached to the forwarding rule.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)


class ForwardingRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_forwarding_ruleset_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_name: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_state: Optional[pulumi.Input[Union[str, 'ForwardingRuleState']]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetDnsServerArgs']]]]] = None,
                 __props__=None):
        """
        Describes a forwarding rule within a DNS forwarding ruleset.
        Azure REST API version: 2022-07-01. Prior API version in Azure Native 1.x: 2020-04-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :param pulumi.Input[str] domain_name: The domain name for the forwarding rule.
        :param pulumi.Input[str] forwarding_rule_name: The name of the forwarding rule.
        :param pulumi.Input[Union[str, 'ForwardingRuleState']] forwarding_rule_state: The state of forwarding rule.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Metadata attached to the forwarding rule.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetDnsServerArgs']]]] target_dns_servers: DNS servers to forward the DNS query to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ForwardingRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a forwarding rule within a DNS forwarding ruleset.
        Azure REST API version: 2022-07-01. Prior API version in Azure Native 1.x: 2020-04-01-preview.

        :param str resource_name: The name of the resource.
        :param ForwardingRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ForwardingRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_forwarding_ruleset_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_name: Optional[pulumi.Input[str]] = None,
                 forwarding_rule_state: Optional[pulumi.Input[Union[str, 'ForwardingRuleState']]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_dns_servers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TargetDnsServerArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ForwardingRuleArgs.__new__(ForwardingRuleArgs)

            if dns_forwarding_ruleset_name is None and not opts.urn:
                raise TypeError("Missing required property 'dns_forwarding_ruleset_name'")
            __props__.__dict__["dns_forwarding_ruleset_name"] = dns_forwarding_ruleset_name
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["forwarding_rule_name"] = forwarding_rule_name
            __props__.__dict__["forwarding_rule_state"] = forwarding_rule_state
            __props__.__dict__["metadata"] = metadata
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if target_dns_servers is None and not opts.urn:
                raise TypeError("Missing required property 'target_dns_servers'")
            __props__.__dict__["target_dns_servers"] = target_dns_servers
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20200401preview:ForwardingRule"), pulumi.Alias(type_="azure-native:network/v20220701:ForwardingRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ForwardingRule, __self__).__init__(
            'azure-native:network:ForwardingRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ForwardingRule':
        """
        Get an existing ForwardingRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ForwardingRuleArgs.__new__(ForwardingRuleArgs)

        __props__.__dict__["domain_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["forwarding_rule_state"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_dns_servers"] = None
        __props__.__dict__["type"] = None
        return ForwardingRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The domain name for the forwarding rule.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        ETag of the forwarding rule.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="forwardingRuleState")
    def forwarding_rule_state(self) -> pulumi.Output[Optional[str]]:
        """
        The state of forwarding rule.
        """
        return pulumi.get(self, "forwarding_rule_state")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Metadata attached to the forwarding rule.
        """
        return pulumi.get(self, "metadata")

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
        The current provisioning state of the forwarding rule. This is a read-only property and any attempt to set this value will be ignored.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetDnsServers")
    def target_dns_servers(self) -> pulumi.Output[Sequence['outputs.TargetDnsServerResponse']]:
        """
        DNS servers to forward the DNS query to.
        """
        return pulumi.get(self, "target_dns_servers")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

