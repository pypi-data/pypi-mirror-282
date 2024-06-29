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

__all__ = [
    'GetLocalRuleCountersResult',
    'AwaitableGetLocalRuleCountersResult',
    'get_local_rule_counters',
    'get_local_rule_counters_output',
]

@pulumi.output_type
class GetLocalRuleCountersResult:
    """
    Rule counter
    """
    def __init__(__self__, app_seen=None, firewall_name=None, hit_count=None, last_updated_timestamp=None, priority=None, request_timestamp=None, rule_list_name=None, rule_name=None, rule_stack_name=None, timestamp=None):
        if app_seen and not isinstance(app_seen, dict):
            raise TypeError("Expected argument 'app_seen' to be a dict")
        pulumi.set(__self__, "app_seen", app_seen)
        if firewall_name and not isinstance(firewall_name, str):
            raise TypeError("Expected argument 'firewall_name' to be a str")
        pulumi.set(__self__, "firewall_name", firewall_name)
        if hit_count and not isinstance(hit_count, int):
            raise TypeError("Expected argument 'hit_count' to be a int")
        pulumi.set(__self__, "hit_count", hit_count)
        if last_updated_timestamp and not isinstance(last_updated_timestamp, str):
            raise TypeError("Expected argument 'last_updated_timestamp' to be a str")
        pulumi.set(__self__, "last_updated_timestamp", last_updated_timestamp)
        if priority and not isinstance(priority, str):
            raise TypeError("Expected argument 'priority' to be a str")
        pulumi.set(__self__, "priority", priority)
        if request_timestamp and not isinstance(request_timestamp, str):
            raise TypeError("Expected argument 'request_timestamp' to be a str")
        pulumi.set(__self__, "request_timestamp", request_timestamp)
        if rule_list_name and not isinstance(rule_list_name, str):
            raise TypeError("Expected argument 'rule_list_name' to be a str")
        pulumi.set(__self__, "rule_list_name", rule_list_name)
        if rule_name and not isinstance(rule_name, str):
            raise TypeError("Expected argument 'rule_name' to be a str")
        pulumi.set(__self__, "rule_name", rule_name)
        if rule_stack_name and not isinstance(rule_stack_name, str):
            raise TypeError("Expected argument 'rule_stack_name' to be a str")
        pulumi.set(__self__, "rule_stack_name", rule_stack_name)
        if timestamp and not isinstance(timestamp, str):
            raise TypeError("Expected argument 'timestamp' to be a str")
        pulumi.set(__self__, "timestamp", timestamp)

    @property
    @pulumi.getter(name="appSeen")
    def app_seen(self) -> Optional['outputs.AppSeenDataResponse']:
        """
        apps seen
        """
        return pulumi.get(self, "app_seen")

    @property
    @pulumi.getter(name="firewallName")
    def firewall_name(self) -> Optional[str]:
        """
        firewall name
        """
        return pulumi.get(self, "firewall_name")

    @property
    @pulumi.getter(name="hitCount")
    def hit_count(self) -> Optional[int]:
        """
        hit count
        """
        return pulumi.get(self, "hit_count")

    @property
    @pulumi.getter(name="lastUpdatedTimestamp")
    def last_updated_timestamp(self) -> Optional[str]:
        """
        last updated timestamp
        """
        return pulumi.get(self, "last_updated_timestamp")

    @property
    @pulumi.getter
    def priority(self) -> str:
        """
        priority number
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="requestTimestamp")
    def request_timestamp(self) -> Optional[str]:
        """
        timestamp of request
        """
        return pulumi.get(self, "request_timestamp")

    @property
    @pulumi.getter(name="ruleListName")
    def rule_list_name(self) -> Optional[str]:
        """
        rule list name
        """
        return pulumi.get(self, "rule_list_name")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> str:
        """
        rule name
        """
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="ruleStackName")
    def rule_stack_name(self) -> Optional[str]:
        """
        rule Stack Name
        """
        return pulumi.get(self, "rule_stack_name")

    @property
    @pulumi.getter
    def timestamp(self) -> Optional[str]:
        """
        timestamp of response
        """
        return pulumi.get(self, "timestamp")


class AwaitableGetLocalRuleCountersResult(GetLocalRuleCountersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalRuleCountersResult(
            app_seen=self.app_seen,
            firewall_name=self.firewall_name,
            hit_count=self.hit_count,
            last_updated_timestamp=self.last_updated_timestamp,
            priority=self.priority,
            request_timestamp=self.request_timestamp,
            rule_list_name=self.rule_list_name,
            rule_name=self.rule_name,
            rule_stack_name=self.rule_stack_name,
            timestamp=self.timestamp)


def get_local_rule_counters(firewall_name: Optional[str] = None,
                            local_rulestack_name: Optional[str] = None,
                            priority: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalRuleCountersResult:
    """
    Get counters


    :param str local_rulestack_name: LocalRulestack resource name
    :param str priority: Local Rule priority
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['firewallName'] = firewall_name
    __args__['localRulestackName'] = local_rulestack_name
    __args__['priority'] = priority
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20231010preview:getLocalRuleCounters', __args__, opts=opts, typ=GetLocalRuleCountersResult).value

    return AwaitableGetLocalRuleCountersResult(
        app_seen=pulumi.get(__ret__, 'app_seen'),
        firewall_name=pulumi.get(__ret__, 'firewall_name'),
        hit_count=pulumi.get(__ret__, 'hit_count'),
        last_updated_timestamp=pulumi.get(__ret__, 'last_updated_timestamp'),
        priority=pulumi.get(__ret__, 'priority'),
        request_timestamp=pulumi.get(__ret__, 'request_timestamp'),
        rule_list_name=pulumi.get(__ret__, 'rule_list_name'),
        rule_name=pulumi.get(__ret__, 'rule_name'),
        rule_stack_name=pulumi.get(__ret__, 'rule_stack_name'),
        timestamp=pulumi.get(__ret__, 'timestamp'))


@_utilities.lift_output_func(get_local_rule_counters)
def get_local_rule_counters_output(firewall_name: Optional[pulumi.Input[Optional[str]]] = None,
                                   local_rulestack_name: Optional[pulumi.Input[str]] = None,
                                   priority: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocalRuleCountersResult]:
    """
    Get counters


    :param str local_rulestack_name: LocalRulestack resource name
    :param str priority: Local Rule priority
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
