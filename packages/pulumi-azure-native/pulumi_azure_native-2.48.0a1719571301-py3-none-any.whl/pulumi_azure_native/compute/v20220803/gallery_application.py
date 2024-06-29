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

__all__ = ['GalleryApplicationArgs', 'GalleryApplication']

@pulumi.input_type
class GalleryApplicationArgs:
    def __init__(__self__, *,
                 gallery_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 supported_os_type: pulumi.Input['OperatingSystemTypes'],
                 custom_actions: Optional[pulumi.Input[Sequence[pulumi.Input['GalleryApplicationCustomActionArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 end_of_life_date: Optional[pulumi.Input[str]] = None,
                 eula: Optional[pulumi.Input[str]] = None,
                 gallery_application_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 privacy_statement_uri: Optional[pulumi.Input[str]] = None,
                 release_note_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a GalleryApplication resource.
        :param pulumi.Input[str] gallery_name: The name of the Shared Application Gallery in which the Application Definition is to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['OperatingSystemTypes'] supported_os_type: This property allows you to specify the supported type of the OS that application is built for. Possible values are: **Windows,** **Linux.**
        :param pulumi.Input[Sequence[pulumi.Input['GalleryApplicationCustomActionArgs']]] custom_actions: A list of custom actions that can be performed with all of the Gallery Application Versions within this Gallery Application.
        :param pulumi.Input[str] description: The description of this gallery Application Definition resource. This property is updatable.
        :param pulumi.Input[str] end_of_life_date: The end of life date of the gallery Application Definition. This property can be used for decommissioning purposes. This property is updatable.
        :param pulumi.Input[str] eula: The Eula agreement for the gallery Application Definition.
        :param pulumi.Input[str] gallery_application_name: The name of the gallery Application Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] privacy_statement_uri: The privacy statement uri.
        :param pulumi.Input[str] release_note_uri: The release note uri.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "gallery_name", gallery_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "supported_os_type", supported_os_type)
        if custom_actions is not None:
            pulumi.set(__self__, "custom_actions", custom_actions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if end_of_life_date is not None:
            pulumi.set(__self__, "end_of_life_date", end_of_life_date)
        if eula is not None:
            pulumi.set(__self__, "eula", eula)
        if gallery_application_name is not None:
            pulumi.set(__self__, "gallery_application_name", gallery_application_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if privacy_statement_uri is not None:
            pulumi.set(__self__, "privacy_statement_uri", privacy_statement_uri)
        if release_note_uri is not None:
            pulumi.set(__self__, "release_note_uri", release_note_uri)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> pulumi.Input[str]:
        """
        The name of the Shared Application Gallery in which the Application Definition is to be created.
        """
        return pulumi.get(self, "gallery_name")

    @gallery_name.setter
    def gallery_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "gallery_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="supportedOSType")
    def supported_os_type(self) -> pulumi.Input['OperatingSystemTypes']:
        """
        This property allows you to specify the supported type of the OS that application is built for. Possible values are: **Windows,** **Linux.**
        """
        return pulumi.get(self, "supported_os_type")

    @supported_os_type.setter
    def supported_os_type(self, value: pulumi.Input['OperatingSystemTypes']):
        pulumi.set(self, "supported_os_type", value)

    @property
    @pulumi.getter(name="customActions")
    def custom_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GalleryApplicationCustomActionArgs']]]]:
        """
        A list of custom actions that can be performed with all of the Gallery Application Versions within this Gallery Application.
        """
        return pulumi.get(self, "custom_actions")

    @custom_actions.setter
    def custom_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GalleryApplicationCustomActionArgs']]]]):
        pulumi.set(self, "custom_actions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of this gallery Application Definition resource. This property is updatable.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[pulumi.Input[str]]:
        """
        The end of life date of the gallery Application Definition. This property can be used for decommissioning purposes. This property is updatable.
        """
        return pulumi.get(self, "end_of_life_date")

    @end_of_life_date.setter
    def end_of_life_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_of_life_date", value)

    @property
    @pulumi.getter
    def eula(self) -> Optional[pulumi.Input[str]]:
        """
        The Eula agreement for the gallery Application Definition.
        """
        return pulumi.get(self, "eula")

    @eula.setter
    def eula(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "eula", value)

    @property
    @pulumi.getter(name="galleryApplicationName")
    def gallery_application_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the gallery Application Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
        """
        return pulumi.get(self, "gallery_application_name")

    @gallery_application_name.setter
    def gallery_application_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gallery_application_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The privacy statement uri.
        """
        return pulumi.get(self, "privacy_statement_uri")

    @privacy_statement_uri.setter
    def privacy_statement_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "privacy_statement_uri", value)

    @property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The release note uri.
        """
        return pulumi.get(self, "release_note_uri")

    @release_note_uri.setter
    def release_note_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "release_note_uri", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class GalleryApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GalleryApplicationCustomActionArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 end_of_life_date: Optional[pulumi.Input[str]] = None,
                 eula: Optional[pulumi.Input[str]] = None,
                 gallery_application_name: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 privacy_statement_uri: Optional[pulumi.Input[str]] = None,
                 release_note_uri: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 supported_os_type: Optional[pulumi.Input['OperatingSystemTypes']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Specifies information about the gallery Application Definition that you want to create or update.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GalleryApplicationCustomActionArgs']]]] custom_actions: A list of custom actions that can be performed with all of the Gallery Application Versions within this Gallery Application.
        :param pulumi.Input[str] description: The description of this gallery Application Definition resource. This property is updatable.
        :param pulumi.Input[str] end_of_life_date: The end of life date of the gallery Application Definition. This property can be used for decommissioning purposes. This property is updatable.
        :param pulumi.Input[str] eula: The Eula agreement for the gallery Application Definition.
        :param pulumi.Input[str] gallery_application_name: The name of the gallery Application Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
        :param pulumi.Input[str] gallery_name: The name of the Shared Application Gallery in which the Application Definition is to be created.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] privacy_statement_uri: The privacy statement uri.
        :param pulumi.Input[str] release_note_uri: The release note uri.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['OperatingSystemTypes'] supported_os_type: This property allows you to specify the supported type of the OS that application is built for. Possible values are: **Windows,** **Linux.**
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GalleryApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specifies information about the gallery Application Definition that you want to create or update.

        :param str resource_name: The name of the resource.
        :param GalleryApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GalleryApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GalleryApplicationCustomActionArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 end_of_life_date: Optional[pulumi.Input[str]] = None,
                 eula: Optional[pulumi.Input[str]] = None,
                 gallery_application_name: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 privacy_statement_uri: Optional[pulumi.Input[str]] = None,
                 release_note_uri: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 supported_os_type: Optional[pulumi.Input['OperatingSystemTypes']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GalleryApplicationArgs.__new__(GalleryApplicationArgs)

            __props__.__dict__["custom_actions"] = custom_actions
            __props__.__dict__["description"] = description
            __props__.__dict__["end_of_life_date"] = end_of_life_date
            __props__.__dict__["eula"] = eula
            __props__.__dict__["gallery_application_name"] = gallery_application_name
            if gallery_name is None and not opts.urn:
                raise TypeError("Missing required property 'gallery_name'")
            __props__.__dict__["gallery_name"] = gallery_name
            __props__.__dict__["location"] = location
            __props__.__dict__["privacy_statement_uri"] = privacy_statement_uri
            __props__.__dict__["release_note_uri"] = release_note_uri
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if supported_os_type is None and not opts.urn:
                raise TypeError("Missing required property 'supported_os_type'")
            __props__.__dict__["supported_os_type"] = supported_os_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20190301:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20190701:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20191201:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20200930:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20210701:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20211001:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20220103:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20220303:GalleryApplication"), pulumi.Alias(type_="azure-native:compute/v20230703:GalleryApplication")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GalleryApplication, __self__).__init__(
            'azure-native:compute/v20220803:GalleryApplication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GalleryApplication':
        """
        Get an existing GalleryApplication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GalleryApplicationArgs.__new__(GalleryApplicationArgs)

        __props__.__dict__["custom_actions"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["end_of_life_date"] = None
        __props__.__dict__["eula"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["privacy_statement_uri"] = None
        __props__.__dict__["release_note_uri"] = None
        __props__.__dict__["supported_os_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return GalleryApplication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customActions")
    def custom_actions(self) -> pulumi.Output[Optional[Sequence['outputs.GalleryApplicationCustomActionResponse']]]:
        """
        A list of custom actions that can be performed with all of the Gallery Application Versions within this Gallery Application.
        """
        return pulumi.get(self, "custom_actions")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of this gallery Application Definition resource. This property is updatable.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> pulumi.Output[Optional[str]]:
        """
        The end of life date of the gallery Application Definition. This property can be used for decommissioning purposes. This property is updatable.
        """
        return pulumi.get(self, "end_of_life_date")

    @property
    @pulumi.getter
    def eula(self) -> pulumi.Output[Optional[str]]:
        """
        The Eula agreement for the gallery Application Definition.
        """
        return pulumi.get(self, "eula")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> pulumi.Output[Optional[str]]:
        """
        The privacy statement uri.
        """
        return pulumi.get(self, "privacy_statement_uri")

    @property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> pulumi.Output[Optional[str]]:
        """
        The release note uri.
        """
        return pulumi.get(self, "release_note_uri")

    @property
    @pulumi.getter(name="supportedOSType")
    def supported_os_type(self) -> pulumi.Output[str]:
        """
        This property allows you to specify the supported type of the OS that application is built for. Possible values are: **Windows,** **Linux.**
        """
        return pulumi.get(self, "supported_os_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

