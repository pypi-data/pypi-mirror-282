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
from ._inputs import *

__all__ = ['ManagedInstancePrivateEndpointConnectionArgs', 'ManagedInstancePrivateEndpointConnection']

@pulumi.input_type
class ManagedInstancePrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 managed_instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 private_endpoint: Optional[pulumi.Input['ManagedInstancePrivateEndpointPropertyArgs']] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input['ManagedInstancePrivateLinkServiceConnectionStatePropertyArgs']] = None):
        """
        The set of arguments for constructing a ManagedInstancePrivateEndpointConnection resource.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input['ManagedInstancePrivateEndpointPropertyArgs'] private_endpoint: Private endpoint which the connection belongs to.
        :param pulumi.Input['ManagedInstancePrivateLinkServiceConnectionStatePropertyArgs'] private_link_service_connection_state: Connection State of the Private Endpoint Connection.
        """
        pulumi.set(__self__, "managed_instance_name", managed_instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_endpoint_connection_name is not None:
            pulumi.set(__self__, "private_endpoint_connection_name", private_endpoint_connection_name)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

    @property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the managed instance.
        """
        return pulumi.get(self, "managed_instance_name")

    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input['ManagedInstancePrivateEndpointPropertyArgs']]:
        """
        Private endpoint which the connection belongs to.
        """
        return pulumi.get(self, "private_endpoint")

    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input['ManagedInstancePrivateEndpointPropertyArgs']]):
        pulumi.set(self, "private_endpoint", value)

    @property
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_endpoint_connection_name")

    @private_endpoint_connection_name.setter
    def private_endpoint_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_connection_name", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input['ManagedInstancePrivateLinkServiceConnectionStatePropertyArgs']]:
        """
        Connection State of the Private Endpoint Connection.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input['ManagedInstancePrivateLinkServiceConnectionStatePropertyArgs']]):
        pulumi.set(self, "private_link_service_connection_state", value)


class ManagedInstancePrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint: Optional[pulumi.Input[pulumi.InputType['ManagedInstancePrivateEndpointPropertyArgs']]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['ManagedInstancePrivateLinkServiceConnectionStatePropertyArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A private endpoint connection

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[pulumi.InputType['ManagedInstancePrivateEndpointPropertyArgs']] private_endpoint: Private endpoint which the connection belongs to.
        :param pulumi.Input[pulumi.InputType['ManagedInstancePrivateLinkServiceConnectionStatePropertyArgs']] private_link_service_connection_state: Connection State of the Private Endpoint Connection.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedInstancePrivateEndpointConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A private endpoint connection

        :param str resource_name: The name of the resource.
        :param ManagedInstancePrivateEndpointConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedInstancePrivateEndpointConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint: Optional[pulumi.Input[pulumi.InputType['ManagedInstancePrivateEndpointPropertyArgs']]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['ManagedInstancePrivateLinkServiceConnectionStatePropertyArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedInstancePrivateEndpointConnectionArgs.__new__(ManagedInstancePrivateEndpointConnectionArgs)

            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__.__dict__["managed_instance_name"] = managed_instance_name
            __props__.__dict__["private_endpoint"] = private_endpoint
            __props__.__dict__["private_endpoint_connection_name"] = private_endpoint_connection_name
            __props__.__dict__["private_link_service_connection_state"] = private_link_service_connection_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20200801preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20210201preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20210801preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20211101:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20211101preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20220201preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20220501preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20220801preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20221101preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20230201preview:ManagedInstancePrivateEndpointConnection"), pulumi.Alias(type_="azure-native:sql/v20230801preview:ManagedInstancePrivateEndpointConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedInstancePrivateEndpointConnection, __self__).__init__(
            'azure-native:sql/v20230501preview:ManagedInstancePrivateEndpointConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedInstancePrivateEndpointConnection':
        """
        Get an existing ManagedInstancePrivateEndpointConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedInstancePrivateEndpointConnectionArgs.__new__(ManagedInstancePrivateEndpointConnectionArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint"] = None
        __props__.__dict__["private_link_service_connection_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return ManagedInstancePrivateEndpointConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> pulumi.Output[Optional['outputs.ManagedInstancePrivateEndpointPropertyResponse']]:
        """
        Private endpoint which the connection belongs to.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Output[Optional['outputs.ManagedInstancePrivateLinkServiceConnectionStatePropertyResponse']]:
        """
        Connection State of the Private Endpoint Connection.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the Private Endpoint Connection.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

