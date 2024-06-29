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

__all__ = ['ExtensionArgs', 'Extension']

@pulumi.input_type
class ExtensionArgs:
    def __init__(__self__, *,
                 farm_beats_resource_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 additional_api_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['ApiPropertiesArgs']]]] = None,
                 extension_id: Optional[pulumi.Input[str]] = None,
                 extension_version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Extension resource.
        :param pulumi.Input[str] farm_beats_resource_name: FarmBeats resource name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input['ApiPropertiesArgs']]] additional_api_properties: Additional Api Properties.
        :param pulumi.Input[str] extension_id: Id of extension resource.
        :param pulumi.Input[str] extension_version: Extension Version.
        """
        pulumi.set(__self__, "farm_beats_resource_name", farm_beats_resource_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if additional_api_properties is not None:
            pulumi.set(__self__, "additional_api_properties", additional_api_properties)
        if extension_id is not None:
            pulumi.set(__self__, "extension_id", extension_id)
        if extension_version is not None:
            pulumi.set(__self__, "extension_version", extension_version)

    @property
    @pulumi.getter(name="farmBeatsResourceName")
    def farm_beats_resource_name(self) -> pulumi.Input[str]:
        """
        FarmBeats resource name.
        """
        return pulumi.get(self, "farm_beats_resource_name")

    @farm_beats_resource_name.setter
    def farm_beats_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "farm_beats_resource_name", value)

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
    @pulumi.getter(name="additionalApiProperties")
    def additional_api_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ApiPropertiesArgs']]]]:
        """
        Additional Api Properties.
        """
        return pulumi.get(self, "additional_api_properties")

    @additional_api_properties.setter
    def additional_api_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ApiPropertiesArgs']]]]):
        pulumi.set(self, "additional_api_properties", value)

    @property
    @pulumi.getter(name="extensionId")
    def extension_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of extension resource.
        """
        return pulumi.get(self, "extension_id")

    @extension_id.setter
    def extension_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extension_id", value)

    @property
    @pulumi.getter(name="extensionVersion")
    def extension_version(self) -> Optional[pulumi.Input[str]]:
        """
        Extension Version.
        """
        return pulumi.get(self, "extension_version")

    @extension_version.setter
    def extension_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extension_version", value)


class Extension(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_api_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ApiPropertiesArgs']]]]] = None,
                 extension_id: Optional[pulumi.Input[str]] = None,
                 extension_version: Optional[pulumi.Input[str]] = None,
                 farm_beats_resource_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Extension resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ApiPropertiesArgs']]]] additional_api_properties: Additional Api Properties.
        :param pulumi.Input[str] extension_id: Id of extension resource.
        :param pulumi.Input[str] extension_version: Extension Version.
        :param pulumi.Input[str] farm_beats_resource_name: FarmBeats resource name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExtensionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Extension resource.

        :param str resource_name: The name of the resource.
        :param ExtensionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExtensionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_api_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ApiPropertiesArgs']]]]] = None,
                 extension_id: Optional[pulumi.Input[str]] = None,
                 extension_version: Optional[pulumi.Input[str]] = None,
                 farm_beats_resource_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExtensionArgs.__new__(ExtensionArgs)

            __props__.__dict__["additional_api_properties"] = additional_api_properties
            __props__.__dict__["extension_id"] = extension_id
            __props__.__dict__["extension_version"] = extension_version
            if farm_beats_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'farm_beats_resource_name'")
            __props__.__dict__["farm_beats_resource_name"] = farm_beats_resource_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["extension_api_docs_link"] = None
            __props__.__dict__["extension_auth_link"] = None
            __props__.__dict__["extension_category"] = None
            __props__.__dict__["installed_extension_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:agfoodplatform:Extension"), pulumi.Alias(type_="azure-native:agfoodplatform/v20200512preview:Extension"), pulumi.Alias(type_="azure-native:agfoodplatform/v20230601preview:Extension")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Extension, __self__).__init__(
            'azure-native:agfoodplatform/v20210901preview:Extension',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Extension':
        """
        Get an existing Extension resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExtensionArgs.__new__(ExtensionArgs)

        __props__.__dict__["additional_api_properties"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["extension_api_docs_link"] = None
        __props__.__dict__["extension_auth_link"] = None
        __props__.__dict__["extension_category"] = None
        __props__.__dict__["extension_id"] = None
        __props__.__dict__["installed_extension_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Extension(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalApiProperties")
    def additional_api_properties(self) -> pulumi.Output[Mapping[str, 'outputs.ApiPropertiesResponse']]:
        """
        Additional api properties.
        """
        return pulumi.get(self, "additional_api_properties")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        The ETag value to implement optimistic concurrency.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="extensionApiDocsLink")
    def extension_api_docs_link(self) -> pulumi.Output[str]:
        """
        Extension api docs link.
        """
        return pulumi.get(self, "extension_api_docs_link")

    @property
    @pulumi.getter(name="extensionAuthLink")
    def extension_auth_link(self) -> pulumi.Output[str]:
        """
        Extension auth link.
        """
        return pulumi.get(self, "extension_auth_link")

    @property
    @pulumi.getter(name="extensionCategory")
    def extension_category(self) -> pulumi.Output[str]:
        """
        Extension category. e.g. weather/sensor/satellite.
        """
        return pulumi.get(self, "extension_category")

    @property
    @pulumi.getter(name="extensionId")
    def extension_id(self) -> pulumi.Output[str]:
        """
        Extension Id.
        """
        return pulumi.get(self, "extension_id")

    @property
    @pulumi.getter(name="installedExtensionVersion")
    def installed_extension_version(self) -> pulumi.Output[str]:
        """
        Installed extension version.
        """
        return pulumi.get(self, "installed_extension_version")

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

