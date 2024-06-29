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

__all__ = ['DelegatedSubnetServiceDetailsArgs', 'DelegatedSubnetServiceDetails']

@pulumi.input_type
class DelegatedSubnetServiceDetailsArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 controller_details: Optional[pulumi.Input['ControllerDetailsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 subnet_details: Optional[pulumi.Input['SubnetDetailsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DelegatedSubnetServiceDetails resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ControllerDetailsArgs'] controller_details: Properties of the controller.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] resource_name: The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
        :param pulumi.Input['SubnetDetailsArgs'] subnet_details: subnet details
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if controller_details is not None:
            pulumi.set(__self__, "controller_details", controller_details)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if subnet_details is not None:
            pulumi.set(__self__, "subnet_details", subnet_details)
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
    @pulumi.getter(name="controllerDetails")
    def controller_details(self) -> Optional[pulumi.Input['ControllerDetailsArgs']]:
        """
        Properties of the controller.
        """
        return pulumi.get(self, "controller_details")

    @controller_details.setter
    def controller_details(self, value: Optional[pulumi.Input['ControllerDetailsArgs']]):
        pulumi.set(self, "controller_details", value)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="subnetDetails")
    def subnet_details(self) -> Optional[pulumi.Input['SubnetDetailsArgs']]:
        """
        subnet details
        """
        return pulumi.get(self, "subnet_details")

    @subnet_details.setter
    def subnet_details(self, value: Optional[pulumi.Input['SubnetDetailsArgs']]):
        pulumi.set(self, "subnet_details", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DelegatedSubnetServiceDetails(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 controller_details: Optional[pulumi.Input[pulumi.InputType['ControllerDetailsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 subnet_details: Optional[pulumi.Input[pulumi.InputType['SubnetDetailsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents an instance of a orchestrator.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ControllerDetailsArgs']] controller_details: Properties of the controller.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the resource. It must be a minimum of 3 characters, and a maximum of 63.
        :param pulumi.Input[pulumi.InputType['SubnetDetailsArgs']] subnet_details: subnet details
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DelegatedSubnetServiceDetailsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an instance of a orchestrator.

        :param str resource_name: The name of the resource.
        :param DelegatedSubnetServiceDetailsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DelegatedSubnetServiceDetailsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 controller_details: Optional[pulumi.Input[pulumi.InputType['ControllerDetailsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 subnet_details: Optional[pulumi.Input[pulumi.InputType['SubnetDetailsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DelegatedSubnetServiceDetailsArgs.__new__(DelegatedSubnetServiceDetailsArgs)

            __props__.__dict__["controller_details"] = controller_details
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["subnet_details"] = subnet_details
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:delegatednetwork:DelegatedSubnetServiceDetails"), pulumi.Alias(type_="azure-native:delegatednetwork/v20200808preview:DelegatedSubnetServiceDetails"), pulumi.Alias(type_="azure-native:delegatednetwork/v20230518preview:DelegatedSubnetServiceDetails"), pulumi.Alias(type_="azure-native:delegatednetwork/v20230627preview:DelegatedSubnetServiceDetails")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DelegatedSubnetServiceDetails, __self__).__init__(
            'azure-native:delegatednetwork/v20210315:DelegatedSubnetServiceDetails',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DelegatedSubnetServiceDetails':
        """
        Get an existing DelegatedSubnetServiceDetails resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DelegatedSubnetServiceDetailsArgs.__new__(DelegatedSubnetServiceDetailsArgs)

        __props__.__dict__["controller_details"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["subnet_details"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DelegatedSubnetServiceDetails(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="controllerDetails")
    def controller_details(self) -> pulumi.Output[Optional['outputs.ControllerDetailsResponse']]:
        """
        Properties of the controller.
        """
        return pulumi.get(self, "controller_details")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current state of dnc delegated subnet resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        Resource guid.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="subnetDetails")
    def subnet_details(self) -> pulumi.Output[Optional['outputs.SubnetDetailsResponse']]:
        """
        subnet details
        """
        return pulumi.get(self, "subnet_details")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of resource.
        """
        return pulumi.get(self, "type")

