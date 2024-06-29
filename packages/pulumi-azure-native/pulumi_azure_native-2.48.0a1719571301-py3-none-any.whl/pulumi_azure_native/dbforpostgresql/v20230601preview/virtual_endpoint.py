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

__all__ = ['VirtualEndpointArgs', 'VirtualEndpoint']

@pulumi.input_type
class VirtualEndpointArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 endpoint_type: Optional[pulumi.Input[Union[str, 'VirtualEndpointType']]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 virtual_endpoint_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualEndpoint resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[Union[str, 'VirtualEndpointType']] endpoint_type: The endpoint type for the virtual endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: List of members for a virtual endpoint
        :param pulumi.Input[str] virtual_endpoint_name: The name of the virtual endpoint.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if endpoint_type is not None:
            pulumi.set(__self__, "endpoint_type", endpoint_type)
        if members is not None:
            pulumi.set(__self__, "members", members)
        if virtual_endpoint_name is not None:
            pulumi.set(__self__, "virtual_endpoint_name", virtual_endpoint_name)

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
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[Union[str, 'VirtualEndpointType']]]:
        """
        The endpoint type for the virtual endpoint.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[Union[str, 'VirtualEndpointType']]]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of members for a virtual endpoint
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter(name="virtualEndpointName")
    def virtual_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the virtual endpoint.
        """
        return pulumi.get(self, "virtual_endpoint_name")

    @virtual_endpoint_name.setter
    def virtual_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_endpoint_name", value)


class VirtualEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_type: Optional[pulumi.Input[Union[str, 'VirtualEndpointType']]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 virtual_endpoint_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a virtual endpoint for a server.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'VirtualEndpointType']] endpoint_type: The endpoint type for the virtual endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: List of members for a virtual endpoint
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] virtual_endpoint_name: The name of the virtual endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a virtual endpoint for a server.

        :param str resource_name: The name of the resource.
        :param VirtualEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_type: Optional[pulumi.Input[Union[str, 'VirtualEndpointType']]] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 virtual_endpoint_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualEndpointArgs.__new__(VirtualEndpointArgs)

            __props__.__dict__["endpoint_type"] = endpoint_type
            __props__.__dict__["members"] = members
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["virtual_endpoint_name"] = virtual_endpoint_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["virtual_endpoints"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dbforpostgresql:VirtualEndpoint"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20231201preview:VirtualEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualEndpoint, __self__).__init__(
            'azure-native:dbforpostgresql/v20230601preview:VirtualEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualEndpoint':
        """
        Get an existing VirtualEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualEndpointArgs.__new__(VirtualEndpointArgs)

        __props__.__dict__["endpoint_type"] = None
        __props__.__dict__["members"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_endpoints"] = None
        return VirtualEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[Optional[str]]:
        """
        The endpoint type for the virtual endpoint.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of members for a virtual endpoint
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

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

    @property
    @pulumi.getter(name="virtualEndpoints")
    def virtual_endpoints(self) -> pulumi.Output[Sequence[str]]:
        """
        List of virtual endpoints for a server
        """
        return pulumi.get(self, "virtual_endpoints")

