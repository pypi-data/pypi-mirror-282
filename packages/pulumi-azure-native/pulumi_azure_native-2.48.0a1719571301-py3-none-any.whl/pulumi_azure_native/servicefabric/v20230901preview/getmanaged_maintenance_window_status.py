# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetmanagedMaintenanceWindowStatusResult',
    'AwaitableGetmanagedMaintenanceWindowStatusResult',
    'getmanaged_maintenance_window_status',
    'getmanaged_maintenance_window_status_output',
]

@pulumi.output_type
class GetmanagedMaintenanceWindowStatusResult:
    """
    Describes the maintenance window status of the Service Fabric Managed Cluster.
    """
    def __init__(__self__, can_apply_updates=None, is_region_ready=None, is_window_active=None, is_window_enabled=None, last_window_end_time_utc=None, last_window_start_time_utc=None, last_window_status_update_at_utc=None):
        if can_apply_updates and not isinstance(can_apply_updates, bool):
            raise TypeError("Expected argument 'can_apply_updates' to be a bool")
        pulumi.set(__self__, "can_apply_updates", can_apply_updates)
        if is_region_ready and not isinstance(is_region_ready, bool):
            raise TypeError("Expected argument 'is_region_ready' to be a bool")
        pulumi.set(__self__, "is_region_ready", is_region_ready)
        if is_window_active and not isinstance(is_window_active, bool):
            raise TypeError("Expected argument 'is_window_active' to be a bool")
        pulumi.set(__self__, "is_window_active", is_window_active)
        if is_window_enabled and not isinstance(is_window_enabled, bool):
            raise TypeError("Expected argument 'is_window_enabled' to be a bool")
        pulumi.set(__self__, "is_window_enabled", is_window_enabled)
        if last_window_end_time_utc and not isinstance(last_window_end_time_utc, str):
            raise TypeError("Expected argument 'last_window_end_time_utc' to be a str")
        pulumi.set(__self__, "last_window_end_time_utc", last_window_end_time_utc)
        if last_window_start_time_utc and not isinstance(last_window_start_time_utc, str):
            raise TypeError("Expected argument 'last_window_start_time_utc' to be a str")
        pulumi.set(__self__, "last_window_start_time_utc", last_window_start_time_utc)
        if last_window_status_update_at_utc and not isinstance(last_window_status_update_at_utc, str):
            raise TypeError("Expected argument 'last_window_status_update_at_utc' to be a str")
        pulumi.set(__self__, "last_window_status_update_at_utc", last_window_status_update_at_utc)

    @property
    @pulumi.getter(name="canApplyUpdates")
    def can_apply_updates(self) -> bool:
        """
        If updates can be applied.
        """
        return pulumi.get(self, "can_apply_updates")

    @property
    @pulumi.getter(name="isRegionReady")
    def is_region_ready(self) -> bool:
        """
        Indicates if the region is ready to configure maintenance windows.
        """
        return pulumi.get(self, "is_region_ready")

    @property
    @pulumi.getter(name="isWindowActive")
    def is_window_active(self) -> bool:
        """
        If maintenance window is active.
        """
        return pulumi.get(self, "is_window_active")

    @property
    @pulumi.getter(name="isWindowEnabled")
    def is_window_enabled(self) -> bool:
        """
        If maintenance window is enabled on this cluster.
        """
        return pulumi.get(self, "is_window_enabled")

    @property
    @pulumi.getter(name="lastWindowEndTimeUTC")
    def last_window_end_time_utc(self) -> str:
        """
        Last window end time in UTC.
        """
        return pulumi.get(self, "last_window_end_time_utc")

    @property
    @pulumi.getter(name="lastWindowStartTimeUTC")
    def last_window_start_time_utc(self) -> str:
        """
        Last window start time in UTC.
        """
        return pulumi.get(self, "last_window_start_time_utc")

    @property
    @pulumi.getter(name="lastWindowStatusUpdateAtUTC")
    def last_window_status_update_at_utc(self) -> str:
        """
        Last window update time in UTC.
        """
        return pulumi.get(self, "last_window_status_update_at_utc")


class AwaitableGetmanagedMaintenanceWindowStatusResult(GetmanagedMaintenanceWindowStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetmanagedMaintenanceWindowStatusResult(
            can_apply_updates=self.can_apply_updates,
            is_region_ready=self.is_region_ready,
            is_window_active=self.is_window_active,
            is_window_enabled=self.is_window_enabled,
            last_window_end_time_utc=self.last_window_end_time_utc,
            last_window_start_time_utc=self.last_window_start_time_utc,
            last_window_status_update_at_utc=self.last_window_status_update_at_utc)


def getmanaged_maintenance_window_status(cluster_name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetmanagedMaintenanceWindowStatusResult:
    """
    Action to get Maintenance Window Status of the Service Fabric Managed Clusters.


    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric/v20230901preview:getmanagedMaintenanceWindowStatus', __args__, opts=opts, typ=GetmanagedMaintenanceWindowStatusResult).value

    return AwaitableGetmanagedMaintenanceWindowStatusResult(
        can_apply_updates=pulumi.get(__ret__, 'can_apply_updates'),
        is_region_ready=pulumi.get(__ret__, 'is_region_ready'),
        is_window_active=pulumi.get(__ret__, 'is_window_active'),
        is_window_enabled=pulumi.get(__ret__, 'is_window_enabled'),
        last_window_end_time_utc=pulumi.get(__ret__, 'last_window_end_time_utc'),
        last_window_start_time_utc=pulumi.get(__ret__, 'last_window_start_time_utc'),
        last_window_status_update_at_utc=pulumi.get(__ret__, 'last_window_status_update_at_utc'))


@_utilities.lift_output_func(getmanaged_maintenance_window_status)
def getmanaged_maintenance_window_status_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetmanagedMaintenanceWindowStatusResult]:
    """
    Action to get Maintenance Window Status of the Service Fabric Managed Clusters.


    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    ...
