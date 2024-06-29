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

__all__ = ['SubscriptionNetworkManagerConnectionArgs', 'SubscriptionNetworkManagerConnection']

@pulumi.input_type
class SubscriptionNetworkManagerConnectionArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 network_manager_connection_name: Optional[pulumi.Input[str]] = None,
                 network_manager_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SubscriptionNetworkManagerConnection resource.
        :param pulumi.Input[str] description: A description of the network manager connection.
        :param pulumi.Input[str] network_manager_connection_name: Name for the network manager connection.
        :param pulumi.Input[str] network_manager_id: Network Manager Id.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if network_manager_connection_name is not None:
            pulumi.set(__self__, "network_manager_connection_name", network_manager_connection_name)
        if network_manager_id is not None:
            pulumi.set(__self__, "network_manager_id", network_manager_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the network manager connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="networkManagerConnectionName")
    def network_manager_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the network manager connection.
        """
        return pulumi.get(self, "network_manager_connection_name")

    @network_manager_connection_name.setter
    def network_manager_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_manager_connection_name", value)

    @property
    @pulumi.getter(name="networkManagerId")
    def network_manager_id(self) -> Optional[pulumi.Input[str]]:
        """
        Network Manager Id.
        """
        return pulumi.get(self, "network_manager_id")

    @network_manager_id.setter
    def network_manager_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_manager_id", value)


class SubscriptionNetworkManagerConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_manager_connection_name: Optional[pulumi.Input[str]] = None,
                 network_manager_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Network Manager Connection resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the network manager connection.
        :param pulumi.Input[str] network_manager_connection_name: Name for the network manager connection.
        :param pulumi.Input[str] network_manager_id: Network Manager Id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SubscriptionNetworkManagerConnectionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Network Manager Connection resource

        :param str resource_name: The name of the resource.
        :param SubscriptionNetworkManagerConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriptionNetworkManagerConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 network_manager_connection_name: Optional[pulumi.Input[str]] = None,
                 network_manager_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubscriptionNetworkManagerConnectionArgs.__new__(SubscriptionNetworkManagerConnectionArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["network_manager_connection_name"] = network_manager_connection_name
            __props__.__dict__["network_manager_id"] = network_manager_id
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20210501preview:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20220101:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20220201preview:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20220401preview:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20220501:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20220701:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20220901:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20221101:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20230201:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20230401:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20230501:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20230901:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20231101:SubscriptionNetworkManagerConnection"), pulumi.Alias(type_="azure-native:network/v20240101:SubscriptionNetworkManagerConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SubscriptionNetworkManagerConnection, __self__).__init__(
            'azure-native:network/v20230601:SubscriptionNetworkManagerConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SubscriptionNetworkManagerConnection':
        """
        Get an existing SubscriptionNetworkManagerConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubscriptionNetworkManagerConnectionArgs.__new__(SubscriptionNetworkManagerConnectionArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_manager_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SubscriptionNetworkManagerConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the network manager connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkManagerId")
    def network_manager_id(self) -> pulumi.Output[Optional[str]]:
        """
        Network Manager Id.
        """
        return pulumi.get(self, "network_manager_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

