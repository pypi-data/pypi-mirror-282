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

__all__ = [
    'GetGalleryImageResult',
    'AwaitableGetGalleryImageResult',
    'get_gallery_image',
    'get_gallery_image_output',
]

@pulumi.output_type
class GetGalleryImageResult:
    """
    Represents an image from the Azure Marketplace
    """
    def __init__(__self__, author=None, created_date=None, description=None, icon=None, id=None, image_reference=None, is_enabled=None, is_override=None, is_plan_authorized=None, latest_operation_result=None, location=None, name=None, plan_id=None, provisioning_state=None, tags=None, type=None, unique_identifier=None):
        if author and not isinstance(author, str):
            raise TypeError("Expected argument 'author' to be a str")
        pulumi.set(__self__, "author", author)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if icon and not isinstance(icon, str):
            raise TypeError("Expected argument 'icon' to be a str")
        pulumi.set(__self__, "icon", icon)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_reference and not isinstance(image_reference, dict):
            raise TypeError("Expected argument 'image_reference' to be a dict")
        pulumi.set(__self__, "image_reference", image_reference)
        if is_enabled and not isinstance(is_enabled, bool):
            raise TypeError("Expected argument 'is_enabled' to be a bool")
        pulumi.set(__self__, "is_enabled", is_enabled)
        if is_override and not isinstance(is_override, bool):
            raise TypeError("Expected argument 'is_override' to be a bool")
        pulumi.set(__self__, "is_override", is_override)
        if is_plan_authorized and not isinstance(is_plan_authorized, bool):
            raise TypeError("Expected argument 'is_plan_authorized' to be a bool")
        pulumi.set(__self__, "is_plan_authorized", is_plan_authorized)
        if latest_operation_result and not isinstance(latest_operation_result, dict):
            raise TypeError("Expected argument 'latest_operation_result' to be a dict")
        pulumi.set(__self__, "latest_operation_result", latest_operation_result)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan_id and not isinstance(plan_id, str):
            raise TypeError("Expected argument 'plan_id' to be a str")
        pulumi.set(__self__, "plan_id", plan_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_identifier and not isinstance(unique_identifier, str):
            raise TypeError("Expected argument 'unique_identifier' to be a str")
        pulumi.set(__self__, "unique_identifier", unique_identifier)

    @property
    @pulumi.getter
    def author(self) -> str:
        """
        The author of the gallery image.
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        The creation date of the gallery image.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the gallery image.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def icon(self) -> str:
        """
        The icon of the gallery image.
        """
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> 'outputs.GalleryImageReferenceResponse':
        """
        The image reference of the gallery image.
        """
        return pulumi.get(self, "image_reference")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[bool]:
        """
        Indicates whether this gallery image is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="isOverride")
    def is_override(self) -> Optional[bool]:
        """
        Indicates whether this gallery has been overridden for this lab account
        """
        return pulumi.get(self, "is_override")

    @property
    @pulumi.getter(name="isPlanAuthorized")
    def is_plan_authorized(self) -> Optional[bool]:
        """
        Indicates if the plan has been authorized for programmatic deployment.
        """
        return pulumi.get(self, "is_plan_authorized")

    @property
    @pulumi.getter(name="latestOperationResult")
    def latest_operation_result(self) -> 'outputs.LatestOperationResultResponse':
        """
        The details of the latest operation. ex: status, error
        """
        return pulumi.get(self, "latest_operation_result")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="planId")
    def plan_id(self) -> str:
        """
        The third party plan that applies to this image
        """
        return pulumi.get(self, "plan_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> Optional[str]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")


class AwaitableGetGalleryImageResult(GetGalleryImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGalleryImageResult(
            author=self.author,
            created_date=self.created_date,
            description=self.description,
            icon=self.icon,
            id=self.id,
            image_reference=self.image_reference,
            is_enabled=self.is_enabled,
            is_override=self.is_override,
            is_plan_authorized=self.is_plan_authorized,
            latest_operation_result=self.latest_operation_result,
            location=self.location,
            name=self.name,
            plan_id=self.plan_id,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type,
            unique_identifier=self.unique_identifier)


def get_gallery_image(expand: Optional[str] = None,
                      gallery_image_name: Optional[str] = None,
                      lab_account_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGalleryImageResult:
    """
    Get gallery image


    :param str expand: Specify the $expand query. Example: 'properties($select=author)'
    :param str gallery_image_name: The name of the gallery Image.
    :param str lab_account_name: The name of the lab Account.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['galleryImageName'] = gallery_image_name
    __args__['labAccountName'] = lab_account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices/v20181015:getGalleryImage', __args__, opts=opts, typ=GetGalleryImageResult).value

    return AwaitableGetGalleryImageResult(
        author=pulumi.get(__ret__, 'author'),
        created_date=pulumi.get(__ret__, 'created_date'),
        description=pulumi.get(__ret__, 'description'),
        icon=pulumi.get(__ret__, 'icon'),
        id=pulumi.get(__ret__, 'id'),
        image_reference=pulumi.get(__ret__, 'image_reference'),
        is_enabled=pulumi.get(__ret__, 'is_enabled'),
        is_override=pulumi.get(__ret__, 'is_override'),
        is_plan_authorized=pulumi.get(__ret__, 'is_plan_authorized'),
        latest_operation_result=pulumi.get(__ret__, 'latest_operation_result'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        plan_id=pulumi.get(__ret__, 'plan_id'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        unique_identifier=pulumi.get(__ret__, 'unique_identifier'))


@_utilities.lift_output_func(get_gallery_image)
def get_gallery_image_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                             gallery_image_name: Optional[pulumi.Input[str]] = None,
                             lab_account_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGalleryImageResult]:
    """
    Get gallery image


    :param str expand: Specify the $expand query. Example: 'properties($select=author)'
    :param str gallery_image_name: The name of the gallery Image.
    :param str lab_account_name: The name of the lab Account.
    :param str resource_group_name: The name of the resource group.
    """
    ...
