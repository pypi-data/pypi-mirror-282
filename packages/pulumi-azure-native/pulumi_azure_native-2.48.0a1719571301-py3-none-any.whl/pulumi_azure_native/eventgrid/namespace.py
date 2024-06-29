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

__all__ = ['NamespaceArgs', 'Namespace']

@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['IdentityInfoArgs']] = None,
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]] = None,
                 is_zone_redundant: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version_allowed: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 sku: Optional[pulumi.Input['NamespaceSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_spaces_configuration: Optional[pulumi.Input['TopicSpacesConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Namespace resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input['IdentityInfoArgs'] identity: Identity information for the Namespace resource.
        :param pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]] inbound_ip_rules: This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        :param pulumi.Input[bool] is_zone_redundant: Allows the user to specify if the service is zone-redundant. This is a required property and user needs to specify this value explicitly.
               Once specified, this property cannot be updated.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[Union[str, 'TlsVersion']] minimum_tls_version_allowed: Minimum TLS version of the publisher allowed to publish to this namespace. Only TLS version 1.2 is supported.
        :param pulumi.Input[str] namespace_name: Name of the namespace.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled.
               You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PubSub.NamespaceProperties.InboundIpRules" />
        :param pulumi.Input['NamespaceSkuArgs'] sku: Represents available Sku pricing tiers.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        :param pulumi.Input['TopicSpacesConfigurationArgs'] topic_spaces_configuration: Topic spaces configuration information for the namespace resource
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if inbound_ip_rules is not None:
            pulumi.set(__self__, "inbound_ip_rules", inbound_ip_rules)
        if is_zone_redundant is not None:
            pulumi.set(__self__, "is_zone_redundant", is_zone_redundant)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if minimum_tls_version_allowed is not None:
            pulumi.set(__self__, "minimum_tls_version_allowed", minimum_tls_version_allowed)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if private_endpoint_connections is not None:
            pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if topic_spaces_configuration is not None:
            pulumi.set(__self__, "topic_spaces_configuration", topic_spaces_configuration)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityInfoArgs']]:
        """
        Identity information for the Namespace resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityInfoArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]]:
        """
        This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        """
        return pulumi.get(self, "inbound_ip_rules")

    @inbound_ip_rules.setter
    def inbound_ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]]):
        pulumi.set(self, "inbound_ip_rules", value)

    @property
    @pulumi.getter(name="isZoneRedundant")
    def is_zone_redundant(self) -> Optional[pulumi.Input[bool]]:
        """
        Allows the user to specify if the service is zone-redundant. This is a required property and user needs to specify this value explicitly.
        Once specified, this property cannot be updated.
        """
        return pulumi.get(self, "is_zone_redundant")

    @is_zone_redundant.setter
    def is_zone_redundant(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_zone_redundant", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> Optional[pulumi.Input[Union[str, 'TlsVersion']]]:
        """
        Minimum TLS version of the publisher allowed to publish to this namespace. Only TLS version 1.2 is supported.
        """
        return pulumi.get(self, "minimum_tls_version_allowed")

    @minimum_tls_version_allowed.setter
    def minimum_tls_version_allowed(self, value: Optional[pulumi.Input[Union[str, 'TlsVersion']]]):
        pulumi.set(self, "minimum_tls_version_allowed", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the namespace.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]:
        return pulumi.get(self, "private_endpoint_connections")

    @private_endpoint_connections.setter
    def private_endpoint_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]):
        pulumi.set(self, "private_endpoint_connections", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PubSub.NamespaceProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['NamespaceSkuArgs']]:
        """
        Represents available Sku pricing tiers.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['NamespaceSkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="topicSpacesConfiguration")
    def topic_spaces_configuration(self) -> Optional[pulumi.Input['TopicSpacesConfigurationArgs']]:
        """
        Topic spaces configuration information for the namespace resource
        """
        return pulumi.get(self, "topic_spaces_configuration")

    @topic_spaces_configuration.setter
    def topic_spaces_configuration(self, value: Optional[pulumi.Input['TopicSpacesConfigurationArgs']]):
        pulumi.set(self, "topic_spaces_configuration", value)


class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityInfoArgs']]] = None,
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InboundIpRuleArgs']]]]] = None,
                 is_zone_redundant: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version_allowed: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['NamespaceSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_spaces_configuration: Optional[pulumi.Input[pulumi.InputType['TopicSpacesConfigurationArgs']]] = None,
                 __props__=None):
        """
        Namespace resource.
        Azure REST API version: 2023-06-01-preview.

        Other available API versions: 2023-12-15-preview, 2024-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['IdentityInfoArgs']] identity: Identity information for the Namespace resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InboundIpRuleArgs']]]] inbound_ip_rules: This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        :param pulumi.Input[bool] is_zone_redundant: Allows the user to specify if the service is zone-redundant. This is a required property and user needs to specify this value explicitly.
               Once specified, this property cannot be updated.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[Union[str, 'TlsVersion']] minimum_tls_version_allowed: Minimum TLS version of the publisher allowed to publish to this namespace. Only TLS version 1.2 is supported.
        :param pulumi.Input[str] namespace_name: Name of the namespace.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled.
               You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PubSub.NamespaceProperties.InboundIpRules" />
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[pulumi.InputType['NamespaceSkuArgs']] sku: Represents available Sku pricing tiers.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        :param pulumi.Input[pulumi.InputType['TopicSpacesConfigurationArgs']] topic_spaces_configuration: Topic spaces configuration information for the namespace resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Namespace resource.
        Azure REST API version: 2023-06-01-preview.

        Other available API versions: 2023-12-15-preview, 2024-06-01-preview.

        :param str resource_name: The name of the resource.
        :param NamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityInfoArgs']]] = None,
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InboundIpRuleArgs']]]]] = None,
                 is_zone_redundant: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version_allowed: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['NamespaceSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_spaces_configuration: Optional[pulumi.Input[pulumi.InputType['TopicSpacesConfigurationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceArgs.__new__(NamespaceArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["inbound_ip_rules"] = inbound_ip_rules
            __props__.__dict__["is_zone_redundant"] = is_zone_redundant
            __props__.__dict__["location"] = location
            __props__.__dict__["minimum_tls_version_allowed"] = minimum_tls_version_allowed
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["private_endpoint_connections"] = private_endpoint_connections
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["topic_spaces_configuration"] = topic_spaces_configuration
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["topics_configuration"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid/v20230601preview:Namespace"), pulumi.Alias(type_="azure-native:eventgrid/v20231215preview:Namespace"), pulumi.Alias(type_="azure-native:eventgrid/v20240601preview:Namespace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Namespace, __self__).__init__(
            'azure-native:eventgrid:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceArgs.__new__(NamespaceArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["inbound_ip_rules"] = None
        __props__.__dict__["is_zone_redundant"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["minimum_tls_version_allowed"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["topic_spaces_configuration"] = None
        __props__.__dict__["topics_configuration"] = None
        __props__.__dict__["type"] = None
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityInfoResponse']]:
        """
        Identity information for the Namespace resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> pulumi.Output[Optional[Sequence['outputs.InboundIpRuleResponse']]]:
        """
        This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        """
        return pulumi.get(self, "inbound_ip_rules")

    @property
    @pulumi.getter(name="isZoneRedundant")
    def is_zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Allows the user to specify if the service is zone-redundant. This is a required property and user needs to specify this value explicitly.
        Once specified, this property cannot be updated.
        """
        return pulumi.get(self, "is_zone_redundant")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumTlsVersionAllowed")
    def minimum_tls_version_allowed(self) -> pulumi.Output[Optional[str]]:
        """
        Minimum TLS version of the publisher allowed to publish to this namespace. Only TLS version 1.2 is supported.
        """
        return pulumi.get(self, "minimum_tls_version_allowed")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]]:
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the namespace resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PubSub.NamespaceProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.NamespaceSkuResponse']]:
        """
        Represents available Sku pricing tiers.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to the namespace resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="topicSpacesConfiguration")
    def topic_spaces_configuration(self) -> pulumi.Output[Optional['outputs.TopicSpacesConfigurationResponse']]:
        """
        Topic spaces configuration information for the namespace resource
        """
        return pulumi.get(self, "topic_spaces_configuration")

    @property
    @pulumi.getter(name="topicsConfiguration")
    def topics_configuration(self) -> pulumi.Output[Optional['outputs.TopicsConfigurationResponse']]:
        """
        Topics configuration information for the namespace resource
        """
        return pulumi.get(self, "topics_configuration")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

