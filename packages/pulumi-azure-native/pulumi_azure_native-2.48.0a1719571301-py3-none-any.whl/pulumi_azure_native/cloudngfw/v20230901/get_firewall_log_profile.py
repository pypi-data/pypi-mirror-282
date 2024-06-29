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
    'GetFirewallLogProfileResult',
    'AwaitableGetFirewallLogProfileResult',
    'get_firewall_log_profile',
    'get_firewall_log_profile_output',
]

@pulumi.output_type
class GetFirewallLogProfileResult:
    """
    Log Settings for Firewall
    """
    def __init__(__self__, application_insights=None, common_destination=None, decrypt_log_destination=None, log_option=None, log_type=None, threat_log_destination=None, traffic_log_destination=None):
        if application_insights and not isinstance(application_insights, dict):
            raise TypeError("Expected argument 'application_insights' to be a dict")
        pulumi.set(__self__, "application_insights", application_insights)
        if common_destination and not isinstance(common_destination, dict):
            raise TypeError("Expected argument 'common_destination' to be a dict")
        pulumi.set(__self__, "common_destination", common_destination)
        if decrypt_log_destination and not isinstance(decrypt_log_destination, dict):
            raise TypeError("Expected argument 'decrypt_log_destination' to be a dict")
        pulumi.set(__self__, "decrypt_log_destination", decrypt_log_destination)
        if log_option and not isinstance(log_option, str):
            raise TypeError("Expected argument 'log_option' to be a str")
        pulumi.set(__self__, "log_option", log_option)
        if log_type and not isinstance(log_type, str):
            raise TypeError("Expected argument 'log_type' to be a str")
        pulumi.set(__self__, "log_type", log_type)
        if threat_log_destination and not isinstance(threat_log_destination, dict):
            raise TypeError("Expected argument 'threat_log_destination' to be a dict")
        pulumi.set(__self__, "threat_log_destination", threat_log_destination)
        if traffic_log_destination and not isinstance(traffic_log_destination, dict):
            raise TypeError("Expected argument 'traffic_log_destination' to be a dict")
        pulumi.set(__self__, "traffic_log_destination", traffic_log_destination)

    @property
    @pulumi.getter(name="applicationInsights")
    def application_insights(self) -> Optional['outputs.ApplicationInsightsResponse']:
        """
        Application Insight details
        """
        return pulumi.get(self, "application_insights")

    @property
    @pulumi.getter(name="commonDestination")
    def common_destination(self) -> Optional['outputs.LogDestinationResponse']:
        """
        Common destination configurations
        """
        return pulumi.get(self, "common_destination")

    @property
    @pulumi.getter(name="decryptLogDestination")
    def decrypt_log_destination(self) -> Optional['outputs.LogDestinationResponse']:
        """
        Decrypt destination configurations
        """
        return pulumi.get(self, "decrypt_log_destination")

    @property
    @pulumi.getter(name="logOption")
    def log_option(self) -> Optional[str]:
        """
        Log option SAME/INDIVIDUAL
        """
        return pulumi.get(self, "log_option")

    @property
    @pulumi.getter(name="logType")
    def log_type(self) -> Optional[str]:
        """
        One of possible log type
        """
        return pulumi.get(self, "log_type")

    @property
    @pulumi.getter(name="threatLogDestination")
    def threat_log_destination(self) -> Optional['outputs.LogDestinationResponse']:
        """
        Threat destination configurations
        """
        return pulumi.get(self, "threat_log_destination")

    @property
    @pulumi.getter(name="trafficLogDestination")
    def traffic_log_destination(self) -> Optional['outputs.LogDestinationResponse']:
        """
        Traffic destination configurations
        """
        return pulumi.get(self, "traffic_log_destination")


class AwaitableGetFirewallLogProfileResult(GetFirewallLogProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallLogProfileResult(
            application_insights=self.application_insights,
            common_destination=self.common_destination,
            decrypt_log_destination=self.decrypt_log_destination,
            log_option=self.log_option,
            log_type=self.log_type,
            threat_log_destination=self.threat_log_destination,
            traffic_log_destination=self.traffic_log_destination)


def get_firewall_log_profile(firewall_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallLogProfileResult:
    """
    Log Profile for Firewall


    :param str firewall_name: Firewall resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['firewallName'] = firewall_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20230901:getFirewallLogProfile', __args__, opts=opts, typ=GetFirewallLogProfileResult).value

    return AwaitableGetFirewallLogProfileResult(
        application_insights=pulumi.get(__ret__, 'application_insights'),
        common_destination=pulumi.get(__ret__, 'common_destination'),
        decrypt_log_destination=pulumi.get(__ret__, 'decrypt_log_destination'),
        log_option=pulumi.get(__ret__, 'log_option'),
        log_type=pulumi.get(__ret__, 'log_type'),
        threat_log_destination=pulumi.get(__ret__, 'threat_log_destination'),
        traffic_log_destination=pulumi.get(__ret__, 'traffic_log_destination'))


@_utilities.lift_output_func(get_firewall_log_profile)
def get_firewall_log_profile_output(firewall_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallLogProfileResult]:
    """
    Log Profile for Firewall


    :param str firewall_name: Firewall resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
