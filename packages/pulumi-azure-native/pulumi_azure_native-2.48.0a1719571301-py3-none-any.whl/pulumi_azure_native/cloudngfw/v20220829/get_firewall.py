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
    'GetFirewallResult',
    'AwaitableGetFirewallResult',
    'get_firewall',
    'get_firewall_output',
]

@pulumi.output_type
class GetFirewallResult:
    """
    PaloAltoNetworks Firewall
    """
    def __init__(__self__, associated_rulestack=None, dns_settings=None, front_end_settings=None, id=None, identity=None, is_panorama_managed=None, location=None, marketplace_details=None, name=None, network_profile=None, pan_etag=None, panorama_config=None, plan_data=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if associated_rulestack and not isinstance(associated_rulestack, dict):
            raise TypeError("Expected argument 'associated_rulestack' to be a dict")
        pulumi.set(__self__, "associated_rulestack", associated_rulestack)
        if dns_settings and not isinstance(dns_settings, dict):
            raise TypeError("Expected argument 'dns_settings' to be a dict")
        pulumi.set(__self__, "dns_settings", dns_settings)
        if front_end_settings and not isinstance(front_end_settings, list):
            raise TypeError("Expected argument 'front_end_settings' to be a list")
        pulumi.set(__self__, "front_end_settings", front_end_settings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if is_panorama_managed and not isinstance(is_panorama_managed, str):
            raise TypeError("Expected argument 'is_panorama_managed' to be a str")
        pulumi.set(__self__, "is_panorama_managed", is_panorama_managed)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if marketplace_details and not isinstance(marketplace_details, dict):
            raise TypeError("Expected argument 'marketplace_details' to be a dict")
        pulumi.set(__self__, "marketplace_details", marketplace_details)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if pan_etag and not isinstance(pan_etag, str):
            raise TypeError("Expected argument 'pan_etag' to be a str")
        pulumi.set(__self__, "pan_etag", pan_etag)
        if panorama_config and not isinstance(panorama_config, dict):
            raise TypeError("Expected argument 'panorama_config' to be a dict")
        pulumi.set(__self__, "panorama_config", panorama_config)
        if plan_data and not isinstance(plan_data, dict):
            raise TypeError("Expected argument 'plan_data' to be a dict")
        pulumi.set(__self__, "plan_data", plan_data)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="associatedRulestack")
    def associated_rulestack(self) -> Optional['outputs.RulestackDetailsResponse']:
        """
        Associated Rulestack
        """
        return pulumi.get(self, "associated_rulestack")

    @property
    @pulumi.getter(name="dnsSettings")
    def dns_settings(self) -> 'outputs.DNSSettingsResponse':
        """
        DNS settings for Firewall
        """
        return pulumi.get(self, "dns_settings")

    @property
    @pulumi.getter(name="frontEndSettings")
    def front_end_settings(self) -> Optional[Sequence['outputs.FrontendSettingResponse']]:
        """
        Frontend settings for Firewall
        """
        return pulumi.get(self, "front_end_settings")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.AzureResourceManagerManagedIdentityPropertiesResponse']:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="isPanoramaManaged")
    def is_panorama_managed(self) -> Optional[str]:
        """
        Panorama Managed: Default is False. Default will be CloudSec managed
        """
        return pulumi.get(self, "is_panorama_managed")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="marketplaceDetails")
    def marketplace_details(self) -> 'outputs.MarketplaceDetailsResponse':
        """
        Marketplace details
        """
        return pulumi.get(self, "marketplace_details")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> 'outputs.NetworkProfileResponse':
        """
        Network settings
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[str]:
        """
        panEtag info
        """
        return pulumi.get(self, "pan_etag")

    @property
    @pulumi.getter(name="panoramaConfig")
    def panorama_config(self) -> Optional['outputs.PanoramaConfigResponse']:
        """
        Panorama Configuration
        """
        return pulumi.get(self, "panorama_config")

    @property
    @pulumi.getter(name="planData")
    def plan_data(self) -> 'outputs.PlanDataResponse':
        """
        Billing plan information.
        """
        return pulumi.get(self, "plan_data")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetFirewallResult(GetFirewallResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallResult(
            associated_rulestack=self.associated_rulestack,
            dns_settings=self.dns_settings,
            front_end_settings=self.front_end_settings,
            id=self.id,
            identity=self.identity,
            is_panorama_managed=self.is_panorama_managed,
            location=self.location,
            marketplace_details=self.marketplace_details,
            name=self.name,
            network_profile=self.network_profile,
            pan_etag=self.pan_etag,
            panorama_config=self.panorama_config,
            plan_data=self.plan_data,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_firewall(firewall_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallResult:
    """
    Get a FirewallResource


    :param str firewall_name: Firewall resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['firewallName'] = firewall_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20220829:getFirewall', __args__, opts=opts, typ=GetFirewallResult).value

    return AwaitableGetFirewallResult(
        associated_rulestack=pulumi.get(__ret__, 'associated_rulestack'),
        dns_settings=pulumi.get(__ret__, 'dns_settings'),
        front_end_settings=pulumi.get(__ret__, 'front_end_settings'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        is_panorama_managed=pulumi.get(__ret__, 'is_panorama_managed'),
        location=pulumi.get(__ret__, 'location'),
        marketplace_details=pulumi.get(__ret__, 'marketplace_details'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        pan_etag=pulumi.get(__ret__, 'pan_etag'),
        panorama_config=pulumi.get(__ret__, 'panorama_config'),
        plan_data=pulumi.get(__ret__, 'plan_data'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_firewall)
def get_firewall_output(firewall_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallResult]:
    """
    Get a FirewallResource


    :param str firewall_name: Firewall resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
