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

__all__ = ['NamespaceArgs', 'Namespace']

@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input['EncryptionArgs']] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 premium_messaging_partitions: Optional[pulumi.Input[int]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 sku: Optional[pulumi.Input['SBSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Namespace resource.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] alternate_name: Alternate name for namespace
        :param pulumi.Input[bool] disable_local_auth: This property disables SAS authentication for the Service Bus namespace.
        :param pulumi.Input['EncryptionArgs'] encryption: Properties of BYOK Encryption description
        :param pulumi.Input['IdentityArgs'] identity: Properties of BYOK Identity description
        :param pulumi.Input[str] location: The Geo-location where the resource lives
        :param pulumi.Input[Union[str, 'TlsVersion']] minimum_tls_version: The minimum TLS version for the cluster to support, e.g. '1.2'
        :param pulumi.Input[str] namespace_name: The namespace name.
        :param pulumi.Input[int] premium_messaging_partitions: The number of partitions of a Service Bus namespace. This property is only applicable to Premium SKU namespaces. The default value is 1 and possible values are 1, 2 and 4
        :param pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]] private_endpoint_connections: List of private endpoint connections.
               These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled.
        :param pulumi.Input['SBSkuArgs'] sku: Properties of SKU
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[bool] zone_redundant: Enabling this property creates a Premium Service Bus Namespace in regions supported availability zones.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if alternate_name is not None:
            pulumi.set(__self__, "alternate_name", alternate_name)
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if minimum_tls_version is not None:
            pulumi.set(__self__, "minimum_tls_version", minimum_tls_version)
        if namespace_name is not None:
            pulumi.set(__self__, "namespace_name", namespace_name)
        if premium_messaging_partitions is not None:
            pulumi.set(__self__, "premium_messaging_partitions", premium_messaging_partitions)
        if private_endpoint_connections is not None:
            pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access is None:
            public_network_access = 'Enabled'
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zone_redundant is not None:
            pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> Optional[pulumi.Input[str]]:
        """
        Alternate name for namespace
        """
        return pulumi.get(self, "alternate_name")

    @alternate_name.setter
    def alternate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alternate_name", value)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        This property disables SAS authentication for the Service Bus namespace.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['EncryptionArgs']]:
        """
        Properties of BYOK Encryption description
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['EncryptionArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        Properties of BYOK Identity description
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The Geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[pulumi.Input[Union[str, 'TlsVersion']]]:
        """
        The minimum TLS version for the cluster to support, e.g. '1.2'
        """
        return pulumi.get(self, "minimum_tls_version")

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: Optional[pulumi.Input[Union[str, 'TlsVersion']]]):
        pulumi.set(self, "minimum_tls_version", value)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace name.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="premiumMessagingPartitions")
    def premium_messaging_partitions(self) -> Optional[pulumi.Input[int]]:
        """
        The number of partitions of a Service Bus namespace. This property is only applicable to Premium SKU namespaces. The default value is 1 and possible values are 1, 2 and 4
        """
        return pulumi.get(self, "premium_messaging_partitions")

    @premium_messaging_partitions.setter
    def premium_messaging_partitions(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "premium_messaging_partitions", value)

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]:
        """
        List of private endpoint connections.
        These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @private_endpoint_connections.setter
    def private_endpoint_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]):
        pulumi.set(self, "private_endpoint_connections", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SBSkuArgs']]:
        """
        Properties of SKU
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SBSkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[pulumi.Input[bool]]:
        """
        Enabling this property creates a Premium Service Bus Namespace in regions supported availability zones.
        """
        return pulumi.get(self, "zone_redundant")

    @zone_redundant.setter
    def zone_redundant(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "zone_redundant", value)


class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['EncryptionArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 premium_messaging_partitions: Optional[pulumi.Input[int]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SBSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Description of a namespace resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alternate_name: Alternate name for namespace
        :param pulumi.Input[bool] disable_local_auth: This property disables SAS authentication for the Service Bus namespace.
        :param pulumi.Input[pulumi.InputType['EncryptionArgs']] encryption: Properties of BYOK Encryption description
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: Properties of BYOK Identity description
        :param pulumi.Input[str] location: The Geo-location where the resource lives
        :param pulumi.Input[Union[str, 'TlsVersion']] minimum_tls_version: The minimum TLS version for the cluster to support, e.g. '1.2'
        :param pulumi.Input[str] namespace_name: The namespace name.
        :param pulumi.Input[int] premium_messaging_partitions: The number of partitions of a Service Bus namespace. This property is only applicable to Premium SKU namespaces. The default value is 1 and possible values are 1, 2 and 4
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]] private_endpoint_connections: List of private endpoint connections.
               These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[pulumi.InputType['SBSkuArgs']] sku: Properties of SKU
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[bool] zone_redundant: Enabling this property creates a Premium Service Bus Namespace in regions supported availability zones.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of a namespace resource.

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
                 alternate_name: Optional[pulumi.Input[str]] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['EncryptionArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 minimum_tls_version: Optional[pulumi.Input[Union[str, 'TlsVersion']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 premium_messaging_partitions: Optional[pulumi.Input[int]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SBSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zone_redundant: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceArgs.__new__(NamespaceArgs)

            __props__.__dict__["alternate_name"] = alternate_name
            __props__.__dict__["disable_local_auth"] = disable_local_auth
            __props__.__dict__["encryption"] = encryption
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["minimum_tls_version"] = minimum_tls_version
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["premium_messaging_partitions"] = premium_messaging_partitions
            __props__.__dict__["private_endpoint_connections"] = private_endpoint_connections
            if public_network_access is None:
                public_network_access = 'Enabled'
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zone_redundant"] = zone_redundant
            __props__.__dict__["created_at"] = None
            __props__.__dict__["metric_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["service_bus_endpoint"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_at"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicebus:Namespace"), pulumi.Alias(type_="azure-native:servicebus/v20140901:Namespace"), pulumi.Alias(type_="azure-native:servicebus/v20150801:Namespace"), pulumi.Alias(type_="azure-native:servicebus/v20170401:Namespace"), pulumi.Alias(type_="azure-native:servicebus/v20180101preview:Namespace"), pulumi.Alias(type_="azure-native:servicebus/v20210101preview:Namespace"), pulumi.Alias(type_="azure-native:servicebus/v20210601preview:Namespace"), pulumi.Alias(type_="azure-native:servicebus/v20211101:Namespace"), pulumi.Alias(type_="azure-native:servicebus/v20220101preview:Namespace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Namespace, __self__).__init__(
            'azure-native:servicebus/v20221001preview:Namespace',
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

        __props__.__dict__["alternate_name"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["disable_local_auth"] = None
        __props__.__dict__["encryption"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metric_id"] = None
        __props__.__dict__["minimum_tls_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["premium_messaging_partitions"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["service_bus_endpoint"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_at"] = None
        __props__.__dict__["zone_redundant"] = None
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alternateName")
    def alternate_name(self) -> pulumi.Output[Optional[str]]:
        """
        Alternate name for namespace
        """
        return pulumi.get(self, "alternate_name")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time the namespace was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> pulumi.Output[Optional[bool]]:
        """
        This property disables SAS authentication for the Service Bus namespace.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional['outputs.EncryptionResponse']]:
        """
        Properties of BYOK Encryption description
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        Properties of BYOK Identity description
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The Geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> pulumi.Output[str]:
        """
        Identifier for Azure Insights metrics
        """
        return pulumi.get(self, "metric_id")

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> pulumi.Output[Optional[str]]:
        """
        The minimum TLS version for the cluster to support, e.g. '1.2'
        """
        return pulumi.get(self, "minimum_tls_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="premiumMessagingPartitions")
    def premium_messaging_partitions(self) -> pulumi.Output[Optional[int]]:
        """
        The number of partitions of a Service Bus namespace. This property is only applicable to Premium SKU namespaces. The default value is 1 and possible values are 1, 2 and 4
        """
        return pulumi.get(self, "premium_messaging_partitions")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]]:
        """
        List of private endpoint connections.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> pulumi.Output[str]:
        """
        Endpoint you can use to perform Service Bus operations.
        """
        return pulumi.get(self, "service_bus_endpoint")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SBSkuResponse']]:
        """
        Properties of SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the namespace.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

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

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The time the namespace was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> pulumi.Output[Optional[bool]]:
        """
        Enabling this property creates a Premium Service Bus Namespace in regions supported availability zones.
        """
        return pulumi.get(self, "zone_redundant")

