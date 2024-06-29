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

__all__ = ['FrontendsInterfaceArgs', 'FrontendsInterface']

@pulumi.input_type
class FrontendsInterfaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 traffic_controller_name: pulumi.Input[str],
                 frontend_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a FrontendsInterface resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] traffic_controller_name: traffic controller name for path
        :param pulumi.Input[str] frontend_name: Frontends
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "traffic_controller_name", traffic_controller_name)
        if frontend_name is not None:
            pulumi.set(__self__, "frontend_name", frontend_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="trafficControllerName")
    def traffic_controller_name(self) -> pulumi.Input[str]:
        """
        traffic controller name for path
        """
        return pulumi.get(self, "traffic_controller_name")

    @traffic_controller_name.setter
    def traffic_controller_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "traffic_controller_name", value)

    @property
    @pulumi.getter(name="frontendName")
    def frontend_name(self) -> Optional[pulumi.Input[str]]:
        """
        Frontends
        """
        return pulumi.get(self, "frontend_name")

    @frontend_name.setter
    def frontend_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "frontend_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class FrontendsInterface(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 frontend_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_controller_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Frontend Sub Resource of Traffic Controller.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] frontend_name: Frontends
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] traffic_controller_name: traffic controller name for path
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FrontendsInterfaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Frontend Sub Resource of Traffic Controller.

        :param str resource_name: The name of the resource.
        :param FrontendsInterfaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FrontendsInterfaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 frontend_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 traffic_controller_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FrontendsInterfaceArgs.__new__(FrontendsInterfaceArgs)

            __props__.__dict__["frontend_name"] = frontend_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if traffic_controller_name is None and not opts.urn:
                raise TypeError("Missing required property 'traffic_controller_name'")
            __props__.__dict__["traffic_controller_name"] = traffic_controller_name
            __props__.__dict__["fqdn"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicenetworking:FrontendsInterface"), pulumi.Alias(type_="azure-native:servicenetworking/v20221001preview:FrontendsInterface"), pulumi.Alias(type_="azure-native:servicenetworking/v20230501preview:FrontendsInterface"), pulumi.Alias(type_="azure-native:servicenetworking/v20240501preview:FrontendsInterface")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FrontendsInterface, __self__).__init__(
            'azure-native:servicenetworking/v20231101:FrontendsInterface',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FrontendsInterface':
        """
        Get an existing FrontendsInterface resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FrontendsInterfaceArgs.__new__(FrontendsInterfaceArgs)

        __props__.__dict__["fqdn"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return FrontendsInterface(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        The Fully Qualified Domain Name of the DNS record associated to a Traffic Controller frontend.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning State of Traffic Controller Frontend Resource
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

