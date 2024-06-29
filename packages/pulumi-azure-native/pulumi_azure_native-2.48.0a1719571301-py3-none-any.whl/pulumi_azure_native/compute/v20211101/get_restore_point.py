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
    'GetRestorePointResult',
    'AwaitableGetRestorePointResult',
    'get_restore_point',
    'get_restore_point_output',
]

@pulumi.output_type
class GetRestorePointResult:
    """
    Restore Point details.
    """
    def __init__(__self__, consistency_mode=None, exclude_disks=None, id=None, instance_view=None, name=None, provisioning_state=None, source_metadata=None, source_restore_point=None, time_created=None, type=None):
        if consistency_mode and not isinstance(consistency_mode, str):
            raise TypeError("Expected argument 'consistency_mode' to be a str")
        pulumi.set(__self__, "consistency_mode", consistency_mode)
        if exclude_disks and not isinstance(exclude_disks, list):
            raise TypeError("Expected argument 'exclude_disks' to be a list")
        pulumi.set(__self__, "exclude_disks", exclude_disks)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_view and not isinstance(instance_view, dict):
            raise TypeError("Expected argument 'instance_view' to be a dict")
        pulumi.set(__self__, "instance_view", instance_view)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source_metadata and not isinstance(source_metadata, dict):
            raise TypeError("Expected argument 'source_metadata' to be a dict")
        pulumi.set(__self__, "source_metadata", source_metadata)
        if source_restore_point and not isinstance(source_restore_point, dict):
            raise TypeError("Expected argument 'source_restore_point' to be a dict")
        pulumi.set(__self__, "source_restore_point", source_restore_point)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="consistencyMode")
    def consistency_mode(self) -> str:
        """
        Gets the consistency mode for the restore point. Please refer to https://aka.ms/RestorePoints for more details.
        """
        return pulumi.get(self, "consistency_mode")

    @property
    @pulumi.getter(name="excludeDisks")
    def exclude_disks(self) -> Optional[Sequence['outputs.ApiEntityReferenceResponse']]:
        """
        List of disk resource ids that the customer wishes to exclude from the restore point. If no disks are specified, all disks will be included.
        """
        return pulumi.get(self, "exclude_disks")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> 'outputs.RestorePointInstanceViewResponse':
        """
        The restore point instance view.
        """
        return pulumi.get(self, "instance_view")

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
        Gets the provisioning state of the restore point.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceMetadata")
    def source_metadata(self) -> 'outputs.RestorePointSourceMetadataResponse':
        """
        Gets the details of the VM captured at the time of the restore point creation.
        """
        return pulumi.get(self, "source_metadata")

    @property
    @pulumi.getter(name="sourceRestorePoint")
    def source_restore_point(self) -> Optional['outputs.ApiEntityReferenceResponse']:
        """
        Resource Id of the source restore point from which a copy needs to be created.
        """
        return pulumi.get(self, "source_restore_point")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> Optional[str]:
        """
        Gets the creation time of the restore point.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetRestorePointResult(GetRestorePointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRestorePointResult(
            consistency_mode=self.consistency_mode,
            exclude_disks=self.exclude_disks,
            id=self.id,
            instance_view=self.instance_view,
            name=self.name,
            provisioning_state=self.provisioning_state,
            source_metadata=self.source_metadata,
            source_restore_point=self.source_restore_point,
            time_created=self.time_created,
            type=self.type)


def get_restore_point(expand: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      restore_point_collection_name: Optional[str] = None,
                      restore_point_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRestorePointResult:
    """
    The operation to get the restore point.


    :param str expand: The expand expression to apply on the operation. 'InstanceView' retrieves information about the run-time state of a restore point.
    :param str resource_group_name: The name of the resource group.
    :param str restore_point_collection_name: The name of the restore point collection.
    :param str restore_point_name: The name of the restore point.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['restorePointCollectionName'] = restore_point_collection_name
    __args__['restorePointName'] = restore_point_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20211101:getRestorePoint', __args__, opts=opts, typ=GetRestorePointResult).value

    return AwaitableGetRestorePointResult(
        consistency_mode=pulumi.get(__ret__, 'consistency_mode'),
        exclude_disks=pulumi.get(__ret__, 'exclude_disks'),
        id=pulumi.get(__ret__, 'id'),
        instance_view=pulumi.get(__ret__, 'instance_view'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        source_metadata=pulumi.get(__ret__, 'source_metadata'),
        source_restore_point=pulumi.get(__ret__, 'source_restore_point'),
        time_created=pulumi.get(__ret__, 'time_created'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_restore_point)
def get_restore_point_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             restore_point_collection_name: Optional[pulumi.Input[str]] = None,
                             restore_point_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRestorePointResult]:
    """
    The operation to get the restore point.


    :param str expand: The expand expression to apply on the operation. 'InstanceView' retrieves information about the run-time state of a restore point.
    :param str resource_group_name: The name of the resource group.
    :param str restore_point_collection_name: The name of the restore point collection.
    :param str restore_point_name: The name of the restore point.
    """
    ...
