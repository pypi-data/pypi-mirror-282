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
    'GetPartnerNamespaceResult',
    'AwaitableGetPartnerNamespaceResult',
    'get_partner_namespace',
    'get_partner_namespace_output',
]

@pulumi.output_type
class GetPartnerNamespaceResult:
    """
    EventGrid Partner Namespace.
    """
    def __init__(__self__, disable_local_auth=None, endpoint=None, id=None, inbound_ip_rules=None, location=None, minimum_tls_version_allowed=None, name=None, partner_registration_fully_qualified_id=None, partner_topic_routing_mode=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, system_data=None, tags=None, type=None):
        if disable_local_auth and not isinstance(disable_local_auth, bool):
            raise TypeError("Expected argument 'disable_local_auth' to be a bool")
        pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inbound_ip_rules and not isinstance(inbound_ip_rules, list):
            raise TypeError("Expected argument 'inbound_ip_rules' to be a list")
        pulumi.set(__self__, "inbound_ip_rules", inbound_ip_rules)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if minimum_tls_version_allowed and not isinstance(minimum_tls_version_allowed, str):
            raise TypeError("Expected argument 'minimum_tls_version_allowed' to be a str")
        pulumi.set(__self__, "minimum_tls_version_allowed", minimum_tls_version_allowed)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_registration_fully_qualified_id and not isinstance(partner_registration_fully_qualified_id, str):
            raise TypeError("Expected argument 'partner_registration_fully_qualified_id' to be a str")
        pulumi.set(__self__, "partner_registration_fully_qualified_id", partner_registration_fully_qualified_id)
        if partner_topic_routing_mode and not isinstance(partner_topic_routing_mode, str):
            raise TypeError("Expected argument 'partner_topic_routing_mode' to be a str")
        pulumi.set(__self__, "partner_topic_routing_mode", partner_topic_routing_mode)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
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
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[bool]:
        """
        This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the partner namespace.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        Endpoint for the partner namespace.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> Optional[Sequence['outputs.InboundIpRuleResponse']]:
        """
        This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        """
        return pulumi.get(self, "inbound_ip_rules")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> Optional[str]:
        """
        Minimum TLS version of the publisher allowed to publish to this partner namespace
        """
        return pulumi.get(self, "minimum_tls_version_allowed")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerRegistrationFullyQualifiedId")
    def partner_registration_fully_qualified_id(self) -> Optional[str]:
        """
        The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format:
        /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventGrid/partnerRegistrations/{partnerRegistrationName}.
        """
        return pulumi.get(self, "partner_registration_fully_qualified_id")

    @property
    @pulumi.getter(name="partnerTopicRoutingMode")
    def partner_topic_routing_mode(self) -> Optional[str]:
        """
        This determines if events published to this partner namespace should use the source attribute in the event payload
        or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic.
        """
        return pulumi.get(self, "partner_topic_routing_mode")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the partner namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PartnerNamespaceProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to Partner Namespace resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPartnerNamespaceResult(GetPartnerNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPartnerNamespaceResult(
            disable_local_auth=self.disable_local_auth,
            endpoint=self.endpoint,
            id=self.id,
            inbound_ip_rules=self.inbound_ip_rules,
            location=self.location,
            minimum_tls_version_allowed=self.minimum_tls_version_allowed,
            name=self.name,
            partner_registration_fully_qualified_id=self.partner_registration_fully_qualified_id,
            partner_topic_routing_mode=self.partner_topic_routing_mode,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_partner_namespace(partner_namespace_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPartnerNamespaceResult:
    """
    Get properties of a partner namespace.


    :param str partner_namespace_name: Name of the partner namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['partnerNamespaceName'] = partner_namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20231215preview:getPartnerNamespace', __args__, opts=opts, typ=GetPartnerNamespaceResult).value

    return AwaitableGetPartnerNamespaceResult(
        disable_local_auth=pulumi.get(__ret__, 'disable_local_auth'),
        endpoint=pulumi.get(__ret__, 'endpoint'),
        id=pulumi.get(__ret__, 'id'),
        inbound_ip_rules=pulumi.get(__ret__, 'inbound_ip_rules'),
        location=pulumi.get(__ret__, 'location'),
        minimum_tls_version_allowed=pulumi.get(__ret__, 'minimum_tls_version_allowed'),
        name=pulumi.get(__ret__, 'name'),
        partner_registration_fully_qualified_id=pulumi.get(__ret__, 'partner_registration_fully_qualified_id'),
        partner_topic_routing_mode=pulumi.get(__ret__, 'partner_topic_routing_mode'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_partner_namespace)
def get_partner_namespace_output(partner_namespace_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPartnerNamespaceResult]:
    """
    Get properties of a partner namespace.


    :param str partner_namespace_name: Name of the partner namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
