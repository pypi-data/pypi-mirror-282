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

__all__ = ['SignalRPrivateEndpointConnectionArgs', 'SignalRPrivateEndpointConnection']

@pulumi.input_type
class SignalRPrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 private_endpoint: Optional[pulumi.Input['PrivateEndpointArgs']] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']] = None):
        """
        The set of arguments for constructing a SignalRPrivateEndpointConnection resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name: The name of the resource.
        :param pulumi.Input['PrivateEndpointArgs'] private_endpoint: Private endpoint
        :param pulumi.Input[str] private_endpoint_connection_name: The name of the private endpoint connection associated with the Azure resource.
        :param pulumi.Input['PrivateLinkServiceConnectionStateArgs'] private_link_service_connection_state: Connection state of the private endpoint connection
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_endpoint_connection_name is not None:
            pulumi.set(__self__, "private_endpoint_connection_name", private_endpoint_connection_name)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input['PrivateEndpointArgs']]:
        """
        Private endpoint
        """
        return pulumi.get(self, "private_endpoint")

    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input['PrivateEndpointArgs']]):
        pulumi.set(self, "private_endpoint", value)

    @property
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the private endpoint connection associated with the Azure resource.
        """
        return pulumi.get(self, "private_endpoint_connection_name")

    @private_endpoint_connection_name.setter
    def private_endpoint_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_connection_name", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']]:
        """
        Connection state of the private endpoint connection
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']]):
        pulumi.set(self, "private_link_service_connection_state", value)


class SignalRPrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 private_endpoint: Optional[pulumi.Input[pulumi.InputType['PrivateEndpointArgs']]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A private endpoint connection to an azure resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PrivateEndpointArgs']] private_endpoint: Private endpoint
        :param pulumi.Input[str] private_endpoint_connection_name: The name of the private endpoint connection associated with the Azure resource.
        :param pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']] private_link_service_connection_state: Connection state of the private endpoint connection
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SignalRPrivateEndpointConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A private endpoint connection to an azure resource

        :param str resource_name: The name of the resource.
        :param SignalRPrivateEndpointConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SignalRPrivateEndpointConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 private_endpoint: Optional[pulumi.Input[pulumi.InputType['PrivateEndpointArgs']]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SignalRPrivateEndpointConnectionArgs.__new__(SignalRPrivateEndpointConnectionArgs)

            __props__.__dict__["private_endpoint"] = private_endpoint
            __props__.__dict__["private_endpoint_connection_name"] = private_endpoint_connection_name
            __props__.__dict__["private_link_service_connection_state"] = private_link_service_connection_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["group_ids"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:signalrservice:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20200501:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20200701preview:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20210401preview:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20210601preview:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20210901preview:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20211001:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20220201:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20220801preview:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20230201:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20230301preview:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20230801preview:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20240101preview:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20240301:SignalRPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:signalrservice/v20240401preview:SignalRPrivateEndpointConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SignalRPrivateEndpointConnection, __self__).__init__(
            'azure-native:signalrservice/v20230601preview:SignalRPrivateEndpointConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SignalRPrivateEndpointConnection':
        """
        Get an existing SignalRPrivateEndpointConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SignalRPrivateEndpointConnectionArgs.__new__(SignalRPrivateEndpointConnectionArgs)

        __props__.__dict__["group_ids"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint"] = None
        __props__.__dict__["private_link_service_connection_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SignalRPrivateEndpointConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Group IDs
        """
        return pulumi.get(self, "group_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> pulumi.Output[Optional['outputs.PrivateEndpointResponse']]:
        """
        Private endpoint
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Output[Optional['outputs.PrivateLinkServiceConnectionStateResponse']]:
        """
        Connection state of the private endpoint connection
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

