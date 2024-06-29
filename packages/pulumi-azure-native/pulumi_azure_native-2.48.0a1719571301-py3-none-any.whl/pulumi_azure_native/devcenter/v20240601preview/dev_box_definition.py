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

__all__ = ['DevBoxDefinitionArgs', 'DevBoxDefinition']

@pulumi.input_type
class DevBoxDefinitionArgs:
    def __init__(__self__, *,
                 dev_center_name: pulumi.Input[str],
                 image_reference: pulumi.Input['ImageReferenceArgs'],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['SkuArgs'],
                 dev_box_definition_name: Optional[pulumi.Input[str]] = None,
                 hibernate_support: Optional[pulumi.Input[Union[str, 'HibernateSupport']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_storage_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DevBoxDefinition resource.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input['ImageReferenceArgs'] image_reference: Image reference information.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['SkuArgs'] sku: The SKU for Dev Boxes created using this definition.
        :param pulumi.Input[str] dev_box_definition_name: The name of the Dev Box definition.
        :param pulumi.Input[Union[str, 'HibernateSupport']] hibernate_support: Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] os_storage_type: The storage type used for the Operating System disk of Dev Boxes created using this definition.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "dev_center_name", dev_center_name)
        pulumi.set(__self__, "image_reference", image_reference)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if dev_box_definition_name is not None:
            pulumi.set(__self__, "dev_box_definition_name", dev_box_definition_name)
        if hibernate_support is not None:
            pulumi.set(__self__, "hibernate_support", hibernate_support)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if os_storage_type is not None:
            pulumi.set(__self__, "os_storage_type", os_storage_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="devCenterName")
    def dev_center_name(self) -> pulumi.Input[str]:
        """
        The name of the devcenter.
        """
        return pulumi.get(self, "dev_center_name")

    @dev_center_name.setter
    def dev_center_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "dev_center_name", value)

    @property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> pulumi.Input['ImageReferenceArgs']:
        """
        Image reference information.
        """
        return pulumi.get(self, "image_reference")

    @image_reference.setter
    def image_reference(self, value: pulumi.Input['ImageReferenceArgs']):
        pulumi.set(self, "image_reference", value)

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
    @pulumi.getter
    def sku(self) -> pulumi.Input['SkuArgs']:
        """
        The SKU for Dev Boxes created using this definition.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['SkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="devBoxDefinitionName")
    def dev_box_definition_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Dev Box definition.
        """
        return pulumi.get(self, "dev_box_definition_name")

    @dev_box_definition_name.setter
    def dev_box_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dev_box_definition_name", value)

    @property
    @pulumi.getter(name="hibernateSupport")
    def hibernate_support(self) -> Optional[pulumi.Input[Union[str, 'HibernateSupport']]]:
        """
        Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate
        """
        return pulumi.get(self, "hibernate_support")

    @hibernate_support.setter
    def hibernate_support(self, value: Optional[pulumi.Input[Union[str, 'HibernateSupport']]]):
        pulumi.set(self, "hibernate_support", value)

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
    @pulumi.getter(name="osStorageType")
    def os_storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        The storage type used for the Operating System disk of Dev Boxes created using this definition.
        """
        return pulumi.get(self, "os_storage_type")

    @os_storage_type.setter
    def os_storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_storage_type", value)

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


class DevBoxDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dev_box_definition_name: Optional[pulumi.Input[str]] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 hibernate_support: Optional[pulumi.Input[Union[str, 'HibernateSupport']]] = None,
                 image_reference: Optional[pulumi.Input[pulumi.InputType['ImageReferenceArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_storage_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents a definition for a Developer Machine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dev_box_definition_name: The name of the Dev Box definition.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[Union[str, 'HibernateSupport']] hibernate_support: Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate
        :param pulumi.Input[pulumi.InputType['ImageReferenceArgs']] image_reference: Image reference information.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] os_storage_type: The storage type used for the Operating System disk of Dev Boxes created using this definition.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The SKU for Dev Boxes created using this definition.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DevBoxDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a definition for a Developer Machine.

        :param str resource_name: The name of the resource.
        :param DevBoxDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DevBoxDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dev_box_definition_name: Optional[pulumi.Input[str]] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 hibernate_support: Optional[pulumi.Input[Union[str, 'HibernateSupport']]] = None,
                 image_reference: Optional[pulumi.Input[pulumi.InputType['ImageReferenceArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_storage_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DevBoxDefinitionArgs.__new__(DevBoxDefinitionArgs)

            __props__.__dict__["dev_box_definition_name"] = dev_box_definition_name
            if dev_center_name is None and not opts.urn:
                raise TypeError("Missing required property 'dev_center_name'")
            __props__.__dict__["dev_center_name"] = dev_center_name
            __props__.__dict__["hibernate_support"] = hibernate_support
            if image_reference is None and not opts.urn:
                raise TypeError("Missing required property 'image_reference'")
            __props__.__dict__["image_reference"] = image_reference
            __props__.__dict__["location"] = location
            __props__.__dict__["os_storage_type"] = os_storage_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["active_image_reference"] = None
            __props__.__dict__["image_validation_error_details"] = None
            __props__.__dict__["image_validation_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["validation_status"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20220801preview:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20220901preview:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20221012preview:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20221111preview:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20230101preview:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20230401:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20230801preview:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20231001preview:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20240201:DevBoxDefinition"), pulumi.Alias(type_="azure-native:devcenter/v20240501preview:DevBoxDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DevBoxDefinition, __self__).__init__(
            'azure-native:devcenter/v20240601preview:DevBoxDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DevBoxDefinition':
        """
        Get an existing DevBoxDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DevBoxDefinitionArgs.__new__(DevBoxDefinitionArgs)

        __props__.__dict__["active_image_reference"] = None
        __props__.__dict__["hibernate_support"] = None
        __props__.__dict__["image_reference"] = None
        __props__.__dict__["image_validation_error_details"] = None
        __props__.__dict__["image_validation_status"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["os_storage_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["validation_status"] = None
        return DevBoxDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="activeImageReference")
    def active_image_reference(self) -> pulumi.Output['outputs.ImageReferenceResponse']:
        """
        Image reference information for the currently active image (only populated during updates).
        """
        return pulumi.get(self, "active_image_reference")

    @property
    @pulumi.getter(name="hibernateSupport")
    def hibernate_support(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether Dev Boxes created with this definition are capable of hibernation. Not all images are capable of supporting hibernation. To find out more see https://aka.ms/devbox/hibernate
        """
        return pulumi.get(self, "hibernate_support")

    @property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> pulumi.Output['outputs.ImageReferenceResponse']:
        """
        Image reference information.
        """
        return pulumi.get(self, "image_reference")

    @property
    @pulumi.getter(name="imageValidationErrorDetails")
    def image_validation_error_details(self) -> pulumi.Output['outputs.ImageValidationErrorDetailsResponse']:
        """
        Details for image validator error. Populated when the image validation is not successful.
        """
        return pulumi.get(self, "image_validation_error_details")

    @property
    @pulumi.getter(name="imageValidationStatus")
    def image_validation_status(self) -> pulumi.Output[str]:
        """
        Validation status of the configured image.
        """
        return pulumi.get(self, "image_validation_status")

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
    @pulumi.getter(name="osStorageType")
    def os_storage_type(self) -> pulumi.Output[Optional[str]]:
        """
        The storage type used for the Operating System disk of Dev Boxes created using this definition.
        """
        return pulumi.get(self, "os_storage_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.SkuResponse']:
        """
        The SKU for Dev Boxes created using this definition.
        """
        return pulumi.get(self, "sku")

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

    @property
    @pulumi.getter(name="validationStatus")
    def validation_status(self) -> pulumi.Output[str]:
        """
        Validation status for the Dev Box Definition.
        """
        return pulumi.get(self, "validation_status")

