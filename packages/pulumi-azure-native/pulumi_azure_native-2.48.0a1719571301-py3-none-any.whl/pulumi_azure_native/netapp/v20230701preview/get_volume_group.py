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
    'GetVolumeGroupResult',
    'AwaitableGetVolumeGroupResult',
    'get_volume_group',
    'get_volume_group_output',
]

@pulumi.output_type
class GetVolumeGroupResult:
    """
    Volume group resource for create
    """
    def __init__(__self__, group_meta_data=None, id=None, location=None, name=None, provisioning_state=None, type=None, volumes=None):
        if group_meta_data and not isinstance(group_meta_data, dict):
            raise TypeError("Expected argument 'group_meta_data' to be a dict")
        pulumi.set(__self__, "group_meta_data", group_meta_data)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volumes and not isinstance(volumes, list):
            raise TypeError("Expected argument 'volumes' to be a list")
        pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter(name="groupMetaData")
    def group_meta_data(self) -> Optional['outputs.VolumeGroupMetaDataResponse']:
        """
        Volume group details
        """
        return pulumi.get(self, "group_meta_data")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence['outputs.VolumeGroupVolumePropertiesResponse']]:
        """
        List of volumes from group
        """
        return pulumi.get(self, "volumes")


class AwaitableGetVolumeGroupResult(GetVolumeGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeGroupResult(
            group_meta_data=self.group_meta_data,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            type=self.type,
            volumes=self.volumes)


def get_volume_group(account_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     volume_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeGroupResult:
    """
    Get details of the specified volume group


    :param str account_name: The name of the NetApp account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str volume_group_name: The name of the volumeGroup
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['volumeGroupName'] = volume_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20230701preview:getVolumeGroup', __args__, opts=opts, typ=GetVolumeGroupResult).value

    return AwaitableGetVolumeGroupResult(
        group_meta_data=pulumi.get(__ret__, 'group_meta_data'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'),
        volumes=pulumi.get(__ret__, 'volumes'))


@_utilities.lift_output_func(get_volume_group)
def get_volume_group_output(account_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            volume_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeGroupResult]:
    """
    Get details of the specified volume group


    :param str account_name: The name of the NetApp account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str volume_group_name: The name of the volumeGroup
    """
    ...
