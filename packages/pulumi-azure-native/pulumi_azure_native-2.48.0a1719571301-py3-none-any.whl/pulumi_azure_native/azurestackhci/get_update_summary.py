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

__all__ = [
    'GetUpdateSummaryResult',
    'AwaitableGetUpdateSummaryResult',
    'get_update_summary',
    'get_update_summary_output',
]

@pulumi.output_type
class GetUpdateSummaryResult:
    """
    Get the update summaries for the cluster
    """
    def __init__(__self__, current_version=None, hardware_model=None, health_check_date=None, id=None, last_checked=None, last_updated=None, location=None, name=None, oem_family=None, provisioning_state=None, state=None, system_data=None, type=None):
        if current_version and not isinstance(current_version, str):
            raise TypeError("Expected argument 'current_version' to be a str")
        pulumi.set(__self__, "current_version", current_version)
        if hardware_model and not isinstance(hardware_model, str):
            raise TypeError("Expected argument 'hardware_model' to be a str")
        pulumi.set(__self__, "hardware_model", hardware_model)
        if health_check_date and not isinstance(health_check_date, str):
            raise TypeError("Expected argument 'health_check_date' to be a str")
        pulumi.set(__self__, "health_check_date", health_check_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_checked and not isinstance(last_checked, str):
            raise TypeError("Expected argument 'last_checked' to be a str")
        pulumi.set(__self__, "last_checked", last_checked)
        if last_updated and not isinstance(last_updated, str):
            raise TypeError("Expected argument 'last_updated' to be a str")
        pulumi.set(__self__, "last_updated", last_updated)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if oem_family and not isinstance(oem_family, str):
            raise TypeError("Expected argument 'oem_family' to be a str")
        pulumi.set(__self__, "oem_family", oem_family)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional[str]:
        """
        Current Solution Bundle version of the stamp.
        """
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter(name="hardwareModel")
    def hardware_model(self) -> Optional[str]:
        """
        Name of the hardware model.
        """
        return pulumi.get(self, "hardware_model")

    @property
    @pulumi.getter(name="healthCheckDate")
    def health_check_date(self) -> Optional[str]:
        """
        Last time the package-specific checks were run.
        """
        return pulumi.get(self, "health_check_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> Optional[str]:
        """
        Last time the update service successfully checked for updates
        """
        return pulumi.get(self, "last_checked")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[str]:
        """
        Last time an update installation completed successfully.
        """
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oemFamily")
    def oem_family(self) -> Optional[str]:
        """
        OEM family name.
        """
        return pulumi.get(self, "oem_family")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the UpdateSummaries proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        Overall update state of the stamp.
        """
        return pulumi.get(self, "state")

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


class AwaitableGetUpdateSummaryResult(GetUpdateSummaryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUpdateSummaryResult(
            current_version=self.current_version,
            hardware_model=self.hardware_model,
            health_check_date=self.health_check_date,
            id=self.id,
            last_checked=self.last_checked,
            last_updated=self.last_updated,
            location=self.location,
            name=self.name,
            oem_family=self.oem_family,
            provisioning_state=self.provisioning_state,
            state=self.state,
            system_data=self.system_data,
            type=self.type)


def get_update_summary(cluster_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUpdateSummaryResult:
    """
    Get all Update summaries under the HCI cluster
    Azure REST API version: 2023-03-01.

    Other available API versions: 2022-12-15-preview, 2023-06-01, 2023-08-01, 2023-08-01-preview, 2023-11-01-preview, 2024-01-01, 2024-02-15-preview, 2024-04-01.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci:getUpdateSummary', __args__, opts=opts, typ=GetUpdateSummaryResult).value

    return AwaitableGetUpdateSummaryResult(
        current_version=pulumi.get(__ret__, 'current_version'),
        hardware_model=pulumi.get(__ret__, 'hardware_model'),
        health_check_date=pulumi.get(__ret__, 'health_check_date'),
        id=pulumi.get(__ret__, 'id'),
        last_checked=pulumi.get(__ret__, 'last_checked'),
        last_updated=pulumi.get(__ret__, 'last_updated'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        oem_family=pulumi.get(__ret__, 'oem_family'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        state=pulumi.get(__ret__, 'state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_update_summary)
def get_update_summary_output(cluster_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUpdateSummaryResult]:
    """
    Get all Update summaries under the HCI cluster
    Azure REST API version: 2023-03-01.

    Other available API versions: 2022-12-15-preview, 2023-06-01, 2023-08-01, 2023-08-01-preview, 2023-11-01-preview, 2024-01-01, 2024-02-15-preview, 2024-04-01.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
