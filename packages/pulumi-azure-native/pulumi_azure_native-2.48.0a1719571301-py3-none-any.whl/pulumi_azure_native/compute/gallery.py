# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['GalleryArgs', 'Gallery']

@pulumi.input_type
class GalleryArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sharing_profile: Optional[pulumi.Input['SharingProfileArgs']] = None,
                 soft_delete_policy: Optional[pulumi.Input['SoftDeletePolicyArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Gallery resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] description: The description of this Shared Image Gallery resource. This property is updatable.
        :param pulumi.Input[str] gallery_name: The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['SharingProfileArgs'] sharing_profile: Profile for gallery sharing to subscription or tenant
        :param pulumi.Input['SoftDeletePolicyArgs'] soft_delete_policy: Contains information about the soft deletion policy of the gallery.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gallery_name is not None:
            pulumi.set(__self__, "gallery_name", gallery_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sharing_profile is not None:
            pulumi.set(__self__, "sharing_profile", sharing_profile)
        if soft_delete_policy is not None:
            pulumi.set(__self__, "soft_delete_policy", soft_delete_policy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of this Shared Image Gallery resource. This property is updatable.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="galleryName")
    def gallery_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.
        """
        return pulumi.get(self, "gallery_name")

    @gallery_name.setter
    def gallery_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gallery_name", value)

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
    @pulumi.getter(name="sharingProfile")
    def sharing_profile(self) -> Optional[pulumi.Input['SharingProfileArgs']]:
        """
        Profile for gallery sharing to subscription or tenant
        """
        return pulumi.get(self, "sharing_profile")

    @sharing_profile.setter
    def sharing_profile(self, value: Optional[pulumi.Input['SharingProfileArgs']]):
        pulumi.set(self, "sharing_profile", value)

    @property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> Optional[pulumi.Input['SoftDeletePolicyArgs']]:
        """
        Contains information about the soft deletion policy of the gallery.
        """
        return pulumi.get(self, "soft_delete_policy")

    @soft_delete_policy.setter
    def soft_delete_policy(self, value: Optional[pulumi.Input['SoftDeletePolicyArgs']]):
        pulumi.set(self, "soft_delete_policy", value)

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


class Gallery(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sharing_profile: Optional[pulumi.Input[pulumi.InputType['SharingProfileArgs']]] = None,
                 soft_delete_policy: Optional[pulumi.Input[pulumi.InputType['SoftDeletePolicyArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Specifies information about the Shared Image Gallery that you want to create or update.
        Azure REST API version: 2022-03-03. Prior API version in Azure Native 1.x: 2020-09-30.

        Other available API versions: 2022-08-03, 2023-07-03.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of this Shared Image Gallery resource. This property is updatable.
        :param pulumi.Input[str] gallery_name: The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['SharingProfileArgs']] sharing_profile: Profile for gallery sharing to subscription or tenant
        :param pulumi.Input[pulumi.InputType['SoftDeletePolicyArgs']] soft_delete_policy: Contains information about the soft deletion policy of the gallery.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GalleryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Specifies information about the Shared Image Gallery that you want to create or update.
        Azure REST API version: 2022-03-03. Prior API version in Azure Native 1.x: 2020-09-30.

        Other available API versions: 2022-08-03, 2023-07-03.

        :param str resource_name: The name of the resource.
        :param GalleryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GalleryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 gallery_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sharing_profile: Optional[pulumi.Input[pulumi.InputType['SharingProfileArgs']]] = None,
                 soft_delete_policy: Optional[pulumi.Input[pulumi.InputType['SoftDeletePolicyArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GalleryArgs.__new__(GalleryArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["gallery_name"] = gallery_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sharing_profile"] = sharing_profile
            __props__.__dict__["soft_delete_policy"] = soft_delete_policy
            __props__.__dict__["tags"] = tags
            __props__.__dict__["identifier"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["sharing_status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:compute/v20180601:Gallery"), pulumi.Alias(type_="azure-native:compute/v20190301:Gallery"), pulumi.Alias(type_="azure-native:compute/v20190701:Gallery"), pulumi.Alias(type_="azure-native:compute/v20191201:Gallery"), pulumi.Alias(type_="azure-native:compute/v20200930:Gallery"), pulumi.Alias(type_="azure-native:compute/v20210701:Gallery"), pulumi.Alias(type_="azure-native:compute/v20211001:Gallery"), pulumi.Alias(type_="azure-native:compute/v20220103:Gallery"), pulumi.Alias(type_="azure-native:compute/v20220303:Gallery"), pulumi.Alias(type_="azure-native:compute/v20220803:Gallery"), pulumi.Alias(type_="azure-native:compute/v20230703:Gallery")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Gallery, __self__).__init__(
            'azure-native:compute:Gallery',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Gallery':
        """
        Get an existing Gallery resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GalleryArgs.__new__(GalleryArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["identifier"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sharing_profile"] = None
        __props__.__dict__["sharing_status"] = None
        __props__.__dict__["soft_delete_policy"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Gallery(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of this Shared Image Gallery resource. This property is updatable.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def identifier(self) -> pulumi.Output[Optional['outputs.GalleryIdentifierResponse']]:
        """
        Describes the gallery unique name.
        """
        return pulumi.get(self, "identifier")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sharingProfile")
    def sharing_profile(self) -> pulumi.Output[Optional['outputs.SharingProfileResponse']]:
        """
        Profile for gallery sharing to subscription or tenant
        """
        return pulumi.get(self, "sharing_profile")

    @property
    @pulumi.getter(name="sharingStatus")
    def sharing_status(self) -> pulumi.Output['outputs.SharingStatusResponse']:
        """
        Sharing status of current gallery.
        """
        return pulumi.get(self, "sharing_status")

    @property
    @pulumi.getter(name="softDeletePolicy")
    def soft_delete_policy(self) -> pulumi.Output[Optional['outputs.SoftDeletePolicyResponse']]:
        """
        Contains information about the soft deletion policy of the gallery.
        """
        return pulumi.get(self, "soft_delete_policy")

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

