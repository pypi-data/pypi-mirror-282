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
    'GetRouteResult',
    'AwaitableGetRouteResult',
    'get_route',
    'get_route_output',
]

@pulumi.output_type
class GetRouteResult:
    """
    Friendly Routes name mapping to the any Routes or secret related information.
    """
    def __init__(__self__, cache_configuration=None, custom_domains=None, deployment_status=None, enabled_state=None, endpoint_name=None, forwarding_protocol=None, https_redirect=None, id=None, link_to_default_domain=None, name=None, origin_group=None, origin_path=None, patterns_to_match=None, provisioning_state=None, rule_sets=None, supported_protocols=None, system_data=None, type=None):
        if cache_configuration and not isinstance(cache_configuration, dict):
            raise TypeError("Expected argument 'cache_configuration' to be a dict")
        pulumi.set(__self__, "cache_configuration", cache_configuration)
        if custom_domains and not isinstance(custom_domains, list):
            raise TypeError("Expected argument 'custom_domains' to be a list")
        pulumi.set(__self__, "custom_domains", custom_domains)
        if deployment_status and not isinstance(deployment_status, str):
            raise TypeError("Expected argument 'deployment_status' to be a str")
        pulumi.set(__self__, "deployment_status", deployment_status)
        if enabled_state and not isinstance(enabled_state, str):
            raise TypeError("Expected argument 'enabled_state' to be a str")
        pulumi.set(__self__, "enabled_state", enabled_state)
        if endpoint_name and not isinstance(endpoint_name, str):
            raise TypeError("Expected argument 'endpoint_name' to be a str")
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        if forwarding_protocol and not isinstance(forwarding_protocol, str):
            raise TypeError("Expected argument 'forwarding_protocol' to be a str")
        pulumi.set(__self__, "forwarding_protocol", forwarding_protocol)
        if https_redirect and not isinstance(https_redirect, str):
            raise TypeError("Expected argument 'https_redirect' to be a str")
        pulumi.set(__self__, "https_redirect", https_redirect)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if link_to_default_domain and not isinstance(link_to_default_domain, str):
            raise TypeError("Expected argument 'link_to_default_domain' to be a str")
        pulumi.set(__self__, "link_to_default_domain", link_to_default_domain)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if origin_group and not isinstance(origin_group, dict):
            raise TypeError("Expected argument 'origin_group' to be a dict")
        pulumi.set(__self__, "origin_group", origin_group)
        if origin_path and not isinstance(origin_path, str):
            raise TypeError("Expected argument 'origin_path' to be a str")
        pulumi.set(__self__, "origin_path", origin_path)
        if patterns_to_match and not isinstance(patterns_to_match, list):
            raise TypeError("Expected argument 'patterns_to_match' to be a list")
        pulumi.set(__self__, "patterns_to_match", patterns_to_match)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rule_sets and not isinstance(rule_sets, list):
            raise TypeError("Expected argument 'rule_sets' to be a list")
        pulumi.set(__self__, "rule_sets", rule_sets)
        if supported_protocols and not isinstance(supported_protocols, list):
            raise TypeError("Expected argument 'supported_protocols' to be a list")
        pulumi.set(__self__, "supported_protocols", supported_protocols)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> Optional['outputs.AfdRouteCacheConfigurationResponse']:
        """
        The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object.
        """
        return pulumi.get(self, "cache_configuration")

    @property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[Sequence['outputs.ActivatedResourceReferenceResponse']]:
        """
        Domains referenced by this endpoint.
        """
        return pulumi.get(self, "custom_domains")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> str:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[str]:
        """
        Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> str:
        """
        The name of the endpoint which holds the route.
        """
        return pulumi.get(self, "endpoint_name")

    @property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(self) -> Optional[str]:
        """
        Protocol this rule will use when forwarding traffic to backends.
        """
        return pulumi.get(self, "forwarding_protocol")

    @property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> Optional[str]:
        """
        Whether to automatically redirect HTTP traffic to HTTPS traffic. Note that this is a easy way to set up this rule and it will be the first rule that gets executed.
        """
        return pulumi.get(self, "https_redirect")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="linkToDefaultDomain")
    def link_to_default_domain(self) -> Optional[str]:
        """
        whether this route will be linked to the default endpoint domain.
        """
        return pulumi.get(self, "link_to_default_domain")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> 'outputs.ResourceReferenceResponse':
        """
        A reference to the origin group.
        """
        return pulumi.get(self, "origin_group")

    @property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[str]:
        """
        A directory path on the origin that AzureFrontDoor can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.
        """
        return pulumi.get(self, "origin_path")

    @property
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(self) -> Optional[Sequence[str]]:
        """
        The route patterns of the rule.
        """
        return pulumi.get(self, "patterns_to_match")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> Optional[Sequence['outputs.ResourceReferenceResponse']]:
        """
        rule sets referenced by this endpoint.
        """
        return pulumi.get(self, "rule_sets")

    @property
    @pulumi.getter(name="supportedProtocols")
    def supported_protocols(self) -> Optional[Sequence[str]]:
        """
        List of supported protocols for this route.
        """
        return pulumi.get(self, "supported_protocols")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetRouteResult(GetRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteResult(
            cache_configuration=self.cache_configuration,
            custom_domains=self.custom_domains,
            deployment_status=self.deployment_status,
            enabled_state=self.enabled_state,
            endpoint_name=self.endpoint_name,
            forwarding_protocol=self.forwarding_protocol,
            https_redirect=self.https_redirect,
            id=self.id,
            link_to_default_domain=self.link_to_default_domain,
            name=self.name,
            origin_group=self.origin_group,
            origin_path=self.origin_path,
            patterns_to_match=self.patterns_to_match,
            provisioning_state=self.provisioning_state,
            rule_sets=self.rule_sets,
            supported_protocols=self.supported_protocols,
            system_data=self.system_data,
            type=self.type)


def get_route(endpoint_name: Optional[str] = None,
              profile_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              route_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteResult:
    """
    Gets an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.
    Azure REST API version: 2023-05-01.

    Other available API versions: 2020-09-01, 2023-07-01-preview, 2024-02-01, 2024-05-01-preview.


    :param str endpoint_name: Name of the endpoint under the profile which is unique globally.
    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str route_name: Name of the routing rule.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['routeName'] = route_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cdn:getRoute', __args__, opts=opts, typ=GetRouteResult).value

    return AwaitableGetRouteResult(
        cache_configuration=pulumi.get(__ret__, 'cache_configuration'),
        custom_domains=pulumi.get(__ret__, 'custom_domains'),
        deployment_status=pulumi.get(__ret__, 'deployment_status'),
        enabled_state=pulumi.get(__ret__, 'enabled_state'),
        endpoint_name=pulumi.get(__ret__, 'endpoint_name'),
        forwarding_protocol=pulumi.get(__ret__, 'forwarding_protocol'),
        https_redirect=pulumi.get(__ret__, 'https_redirect'),
        id=pulumi.get(__ret__, 'id'),
        link_to_default_domain=pulumi.get(__ret__, 'link_to_default_domain'),
        name=pulumi.get(__ret__, 'name'),
        origin_group=pulumi.get(__ret__, 'origin_group'),
        origin_path=pulumi.get(__ret__, 'origin_path'),
        patterns_to_match=pulumi.get(__ret__, 'patterns_to_match'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rule_sets=pulumi.get(__ret__, 'rule_sets'),
        supported_protocols=pulumi.get(__ret__, 'supported_protocols'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_route)
def get_route_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                     profile_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     route_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteResult]:
    """
    Gets an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint.
    Azure REST API version: 2023-05-01.

    Other available API versions: 2020-09-01, 2023-07-01-preview, 2024-02-01, 2024-05-01-preview.


    :param str endpoint_name: Name of the endpoint under the profile which is unique globally.
    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str route_name: Name of the routing rule.
    """
    ...
