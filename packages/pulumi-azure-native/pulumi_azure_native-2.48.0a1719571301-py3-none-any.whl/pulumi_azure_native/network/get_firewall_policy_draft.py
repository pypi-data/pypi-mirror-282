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

__all__ = [
    'GetFirewallPolicyDraftResult',
    'AwaitableGetFirewallPolicyDraftResult',
    'get_firewall_policy_draft',
    'get_firewall_policy_draft_output',
]

@pulumi.output_type
class GetFirewallPolicyDraftResult:
    """
    FirewallPolicy Resource.
    """
    def __init__(__self__, base_policy=None, dns_settings=None, explicit_proxy=None, id=None, insights=None, intrusion_detection=None, location=None, name=None, snat=None, sql=None, tags=None, threat_intel_mode=None, threat_intel_whitelist=None, type=None):
        if base_policy and not isinstance(base_policy, dict):
            raise TypeError("Expected argument 'base_policy' to be a dict")
        pulumi.set(__self__, "base_policy", base_policy)
        if dns_settings and not isinstance(dns_settings, dict):
            raise TypeError("Expected argument 'dns_settings' to be a dict")
        pulumi.set(__self__, "dns_settings", dns_settings)
        if explicit_proxy and not isinstance(explicit_proxy, dict):
            raise TypeError("Expected argument 'explicit_proxy' to be a dict")
        pulumi.set(__self__, "explicit_proxy", explicit_proxy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if insights and not isinstance(insights, dict):
            raise TypeError("Expected argument 'insights' to be a dict")
        pulumi.set(__self__, "insights", insights)
        if intrusion_detection and not isinstance(intrusion_detection, dict):
            raise TypeError("Expected argument 'intrusion_detection' to be a dict")
        pulumi.set(__self__, "intrusion_detection", intrusion_detection)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if snat and not isinstance(snat, dict):
            raise TypeError("Expected argument 'snat' to be a dict")
        pulumi.set(__self__, "snat", snat)
        if sql and not isinstance(sql, dict):
            raise TypeError("Expected argument 'sql' to be a dict")
        pulumi.set(__self__, "sql", sql)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if threat_intel_mode and not isinstance(threat_intel_mode, str):
            raise TypeError("Expected argument 'threat_intel_mode' to be a str")
        pulumi.set(__self__, "threat_intel_mode", threat_intel_mode)
        if threat_intel_whitelist and not isinstance(threat_intel_whitelist, dict):
            raise TypeError("Expected argument 'threat_intel_whitelist' to be a dict")
        pulumi.set(__self__, "threat_intel_whitelist", threat_intel_whitelist)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="basePolicy")
    def base_policy(self) -> Optional['outputs.SubResourceResponse']:
        """
        The parent firewall policy from which rules are inherited.
        """
        return pulumi.get(self, "base_policy")

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> Optional['outputs.DnsSettingsResponse']:
        """
        DNS Proxy Settings definition.
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter(name="explicitProxy")
    def explicit_proxy(self) -> Optional['outputs.ExplicitProxyResponse']:
        """
        Explicit Proxy Settings definition.
        """
        return pulumi.get(self, "explicit_proxy")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def insights(self) -> Optional['outputs.FirewallPolicyInsightsResponse']:
        """
        Insights on Firewall Policy.
        """
        return pulumi.get(self, "insights")

    @property
    @pulumi.getter(name="intrusionDetection")
    def intrusion_detection(self) -> Optional['outputs.FirewallPolicyIntrusionDetectionResponse']:
        """
        The configuration for Intrusion detection.
        """
        return pulumi.get(self, "intrusion_detection")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def snat(self) -> Optional['outputs.FirewallPolicySNATResponse']:
        """
        The private IP addresses/IP ranges to which traffic will not be SNAT.
        """
        return pulumi.get(self, "snat")

    @property
    @pulumi.getter
    def sql(self) -> Optional['outputs.FirewallPolicySQLResponse']:
        """
        SQL Settings definition.
        """
        return pulumi.get(self, "sql")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="threatIntelMode")
    def threat_intel_mode(self) -> Optional[str]:
        """
        The operation mode for Threat Intelligence.
        """
        return pulumi.get(self, "threat_intel_mode")

    @property
    @pulumi.getter(name="threatIntelWhitelist")
    def threat_intel_whitelist(self) -> Optional['outputs.FirewallPolicyThreatIntelWhitelistResponse']:
        """
        ThreatIntel Whitelist for Firewall Policy.
        """
        return pulumi.get(self, "threat_intel_whitelist")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetFirewallPolicyDraftResult(GetFirewallPolicyDraftResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallPolicyDraftResult(
            base_policy=self.base_policy,
            dns_settings=self.dns_settings,
            explicit_proxy=self.explicit_proxy,
            id=self.id,
            insights=self.insights,
            intrusion_detection=self.intrusion_detection,
            location=self.location,
            name=self.name,
            snat=self.snat,
            sql=self.sql,
            tags=self.tags,
            threat_intel_mode=self.threat_intel_mode,
            threat_intel_whitelist=self.threat_intel_whitelist,
            type=self.type)


def get_firewall_policy_draft(firewall_policy_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallPolicyDraftResult:
    """
    Get a draft Firewall Policy.
    Azure REST API version: 2023-11-01.

    Other available API versions: 2024-01-01.


    :param str firewall_policy_name: The name of the Firewall Policy.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['firewallPolicyName'] = firewall_policy_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getFirewallPolicyDraft', __args__, opts=opts, typ=GetFirewallPolicyDraftResult).value

    return AwaitableGetFirewallPolicyDraftResult(
        base_policy=pulumi.get(__ret__, 'base_policy'),
        dns_settings=pulumi.get(__ret__, 'dns_settings'),
        explicit_proxy=pulumi.get(__ret__, 'explicit_proxy'),
        id=pulumi.get(__ret__, 'id'),
        insights=pulumi.get(__ret__, 'insights'),
        intrusion_detection=pulumi.get(__ret__, 'intrusion_detection'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        snat=pulumi.get(__ret__, 'snat'),
        sql=pulumi.get(__ret__, 'sql'),
        tags=pulumi.get(__ret__, 'tags'),
        threat_intel_mode=pulumi.get(__ret__, 'threat_intel_mode'),
        threat_intel_whitelist=pulumi.get(__ret__, 'threat_intel_whitelist'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_firewall_policy_draft)
def get_firewall_policy_draft_output(firewall_policy_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallPolicyDraftResult]:
    """
    Get a draft Firewall Policy.
    Azure REST API version: 2023-11-01.

    Other available API versions: 2024-01-01.


    :param str firewall_policy_name: The name of the Firewall Policy.
    :param str resource_group_name: The name of the resource group.
    """
    ...
