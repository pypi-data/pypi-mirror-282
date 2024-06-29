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

__all__ = ['VMSkusArgs', 'VMSkus']

@pulumi.input_type
class VMSkusArgs:
    def __init__(__self__, *,
                 custom_location_resource_uri: pulumi.Input[str],
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None):
        """
        The set of arguments for constructing a VMSkus resource.
        :param pulumi.Input[str] custom_location_resource_uri: The fully qualified Azure Resource Manager identifier of the custom location resource.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: Extended location pointing to the underlying infrastructure
        """
        pulumi.set(__self__, "custom_location_resource_uri", custom_location_resource_uri)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)

    @property
    @pulumi.getter(name="customLocationResourceUri")
    def custom_location_resource_uri(self) -> pulumi.Input[str]:
        """
        The fully qualified Azure Resource Manager identifier of the custom location resource.
        """
        return pulumi.get(self, "custom_location_resource_uri")

    @custom_location_resource_uri.setter
    def custom_location_resource_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "custom_location_resource_uri", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        Extended location pointing to the underlying infrastructure
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)


class VMSkus(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_location_resource_uri: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 __props__=None):
        """
        The list of supported VM SKUs.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] custom_location_resource_uri: The fully qualified Azure Resource Manager identifier of the custom location resource.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: Extended location pointing to the underlying infrastructure
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VMSkusArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The list of supported VM SKUs.

        :param str resource_name: The name of the resource.
        :param VMSkusArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VMSkusArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_location_resource_uri: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VMSkusArgs.__new__(VMSkusArgs)

            if custom_location_resource_uri is None and not opts.urn:
                raise TypeError("Missing required property 'custom_location_resource_uri'")
            __props__.__dict__["custom_location_resource_uri"] = custom_location_resource_uri
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["name"] = None
            __props__.__dict__["properties"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybridcontainerservice/v20231115preview:VMSkus")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VMSkus, __self__).__init__(
            'azure-native:hybridcontainerservice/v20240101:VMSkus',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VMSkus':
        """
        Get an existing VMSkus resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VMSkusArgs.__new__(VMSkusArgs)

        __props__.__dict__["extended_location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return VMSkus(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        Extended location pointing to the underlying infrastructure
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.VmSkuProfileResponseProperties']:
        return pulumi.get(self, "properties")

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

