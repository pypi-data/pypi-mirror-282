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

__all__ = ['CustomizedAcceleratorArgs', 'CustomizedAccelerator']

@pulumi.input_type
class CustomizedAcceleratorArgs:
    def __init__(__self__, *,
                 application_accelerator_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 customized_accelerator_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['CustomizedAcceleratorPropertiesArgs']] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None):
        """
        The set of arguments for constructing a CustomizedAccelerator resource.
        :param pulumi.Input[str] application_accelerator_name: The name of the application accelerator.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] service_name: The name of the Service resource.
        :param pulumi.Input[str] customized_accelerator_name: The name of the customized accelerator.
        :param pulumi.Input['CustomizedAcceleratorPropertiesArgs'] properties: Customized accelerator properties payload
        :param pulumi.Input['SkuArgs'] sku: Sku of the customized accelerator resource
        """
        pulumi.set(__self__, "application_accelerator_name", application_accelerator_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if customized_accelerator_name is not None:
            pulumi.set(__self__, "customized_accelerator_name", customized_accelerator_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)

    @property
    @pulumi.getter(name="applicationAcceleratorName")
    def application_accelerator_name(self) -> pulumi.Input[str]:
        """
        The name of the application accelerator.
        """
        return pulumi.get(self, "application_accelerator_name")

    @application_accelerator_name.setter
    def application_accelerator_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_accelerator_name", value)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the Service resource.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="customizedAcceleratorName")
    def customized_accelerator_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the customized accelerator.
        """
        return pulumi.get(self, "customized_accelerator_name")

    @customized_accelerator_name.setter
    def customized_accelerator_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customized_accelerator_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['CustomizedAcceleratorPropertiesArgs']]:
        """
        Customized accelerator properties payload
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['CustomizedAcceleratorPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        Sku of the customized accelerator resource
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)


class CustomizedAccelerator(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_accelerator_name: Optional[pulumi.Input[str]] = None,
                 customized_accelerator_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['CustomizedAcceleratorPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 __props__=None):
        """
        Customized accelerator resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_accelerator_name: The name of the application accelerator.
        :param pulumi.Input[str] customized_accelerator_name: The name of the customized accelerator.
        :param pulumi.Input[pulumi.InputType['CustomizedAcceleratorPropertiesArgs']] properties: Customized accelerator properties payload
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] service_name: The name of the Service resource.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: Sku of the customized accelerator resource
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomizedAcceleratorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Customized accelerator resource

        :param str resource_name: The name of the resource.
        :param CustomizedAcceleratorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomizedAcceleratorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_accelerator_name: Optional[pulumi.Input[str]] = None,
                 customized_accelerator_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['CustomizedAcceleratorPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomizedAcceleratorArgs.__new__(CustomizedAcceleratorArgs)

            if application_accelerator_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_accelerator_name'")
            __props__.__dict__["application_accelerator_name"] = application_accelerator_name
            __props__.__dict__["customized_accelerator_name"] = customized_accelerator_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:appplatform:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20221101preview:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20230101preview:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20230301preview:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20230501preview:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20230701preview:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20230901preview:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20231101preview:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20231201:CustomizedAccelerator"), pulumi.Alias(type_="azure-native:appplatform/v20240101preview:CustomizedAccelerator")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomizedAccelerator, __self__).__init__(
            'azure-native:appplatform/v20240501preview:CustomizedAccelerator',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomizedAccelerator':
        """
        Get an existing CustomizedAccelerator resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomizedAcceleratorArgs.__new__(CustomizedAcceleratorArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CustomizedAccelerator(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.CustomizedAcceleratorPropertiesResponse']:
        """
        Customized accelerator properties payload
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        Sku of the customized accelerator resource
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

