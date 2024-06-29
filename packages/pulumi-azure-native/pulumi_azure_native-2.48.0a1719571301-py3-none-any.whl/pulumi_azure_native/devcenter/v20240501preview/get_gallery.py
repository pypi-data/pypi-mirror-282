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
    'GetGalleryResult',
    'AwaitableGetGalleryResult',
    'get_gallery',
    'get_gallery_output',
]

@pulumi.output_type
class GetGalleryResult:
    """
    Represents a gallery.
    """
    def __init__(__self__, gallery_resource_id=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if gallery_resource_id and not isinstance(gallery_resource_id, str):
            raise TypeError("Expected argument 'gallery_resource_id' to be a str")
        pulumi.set(__self__, "gallery_resource_id", gallery_resource_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="galleryResourceId")
    def gallery_resource_id(self) -> str:
        """
        The resource ID of the backing Azure Compute Gallery.
        """
        return pulumi.get(self, "gallery_resource_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetGalleryResult(GetGalleryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGalleryResult(
            gallery_resource_id=self.gallery_resource_id,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_gallery(dev_center_name: Optional[str] = None,
                gallery_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGalleryResult:
    """
    Gets a gallery


    :param str dev_center_name: The name of the devcenter.
    :param str gallery_name: The name of the gallery.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['devCenterName'] = dev_center_name
    __args__['galleryName'] = gallery_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20240501preview:getGallery', __args__, opts=opts, typ=GetGalleryResult).value

    return AwaitableGetGalleryResult(
        gallery_resource_id=pulumi.get(__ret__, 'gallery_resource_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_gallery)
def get_gallery_output(dev_center_name: Optional[pulumi.Input[str]] = None,
                       gallery_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGalleryResult]:
    """
    Gets a gallery


    :param str dev_center_name: The name of the devcenter.
    :param str gallery_name: The name of the gallery.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
