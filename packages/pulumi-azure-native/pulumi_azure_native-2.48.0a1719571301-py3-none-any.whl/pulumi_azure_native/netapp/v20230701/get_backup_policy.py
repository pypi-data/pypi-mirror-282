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
    'GetBackupPolicyResult',
    'AwaitableGetBackupPolicyResult',
    'get_backup_policy',
    'get_backup_policy_output',
]

@pulumi.output_type
class GetBackupPolicyResult:
    """
    Backup policy information
    """
    def __init__(__self__, backup_policy_id=None, daily_backups_to_keep=None, enabled=None, etag=None, id=None, location=None, monthly_backups_to_keep=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None, volume_backups=None, volumes_assigned=None, weekly_backups_to_keep=None):
        if backup_policy_id and not isinstance(backup_policy_id, str):
            raise TypeError("Expected argument 'backup_policy_id' to be a str")
        pulumi.set(__self__, "backup_policy_id", backup_policy_id)
        if daily_backups_to_keep and not isinstance(daily_backups_to_keep, int):
            raise TypeError("Expected argument 'daily_backups_to_keep' to be a int")
        pulumi.set(__self__, "daily_backups_to_keep", daily_backups_to_keep)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if monthly_backups_to_keep and not isinstance(monthly_backups_to_keep, int):
            raise TypeError("Expected argument 'monthly_backups_to_keep' to be a int")
        pulumi.set(__self__, "monthly_backups_to_keep", monthly_backups_to_keep)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volume_backups and not isinstance(volume_backups, list):
            raise TypeError("Expected argument 'volume_backups' to be a list")
        pulumi.set(__self__, "volume_backups", volume_backups)
        if volumes_assigned and not isinstance(volumes_assigned, int):
            raise TypeError("Expected argument 'volumes_assigned' to be a int")
        pulumi.set(__self__, "volumes_assigned", volumes_assigned)
        if weekly_backups_to_keep and not isinstance(weekly_backups_to_keep, int):
            raise TypeError("Expected argument 'weekly_backups_to_keep' to be a int")
        pulumi.set(__self__, "weekly_backups_to_keep", weekly_backups_to_keep)

    @property
    @pulumi.getter(name="backupPolicyId")
    def backup_policy_id(self) -> str:
        """
        Backup Policy Resource ID
        """
        return pulumi.get(self, "backup_policy_id")

    @property
    @pulumi.getter(name="dailyBackupsToKeep")
    def daily_backups_to_keep(self) -> Optional[int]:
        """
        Daily backups count to keep
        """
        return pulumi.get(self, "daily_backups_to_keep")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        The property to decide policy is enabled or not
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="monthlyBackupsToKeep")
    def monthly_backups_to_keep(self) -> Optional[int]:
        """
        Monthly backups count to keep
        """
        return pulumi.get(self, "monthly_backups_to_keep")

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
        Azure lifecycle management
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
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeBackups")
    def volume_backups(self) -> Sequence['outputs.VolumeBackupsResponse']:
        """
        A list of volumes assigned to this policy
        """
        return pulumi.get(self, "volume_backups")

    @property
    @pulumi.getter(name="volumesAssigned")
    def volumes_assigned(self) -> int:
        """
        Volumes using current backup policy
        """
        return pulumi.get(self, "volumes_assigned")

    @property
    @pulumi.getter(name="weeklyBackupsToKeep")
    def weekly_backups_to_keep(self) -> Optional[int]:
        """
        Weekly backups count to keep
        """
        return pulumi.get(self, "weekly_backups_to_keep")


class AwaitableGetBackupPolicyResult(GetBackupPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackupPolicyResult(
            backup_policy_id=self.backup_policy_id,
            daily_backups_to_keep=self.daily_backups_to_keep,
            enabled=self.enabled,
            etag=self.etag,
            id=self.id,
            location=self.location,
            monthly_backups_to_keep=self.monthly_backups_to_keep,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            volume_backups=self.volume_backups,
            volumes_assigned=self.volumes_assigned,
            weekly_backups_to_keep=self.weekly_backups_to_keep)


def get_backup_policy(account_name: Optional[str] = None,
                      backup_policy_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackupPolicyResult:
    """
    Get a particular backup Policy


    :param str account_name: The name of the NetApp account
    :param str backup_policy_name: Backup policy Name which uniquely identify backup policy.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['backupPolicyName'] = backup_policy_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20230701:getBackupPolicy', __args__, opts=opts, typ=GetBackupPolicyResult).value

    return AwaitableGetBackupPolicyResult(
        backup_policy_id=pulumi.get(__ret__, 'backup_policy_id'),
        daily_backups_to_keep=pulumi.get(__ret__, 'daily_backups_to_keep'),
        enabled=pulumi.get(__ret__, 'enabled'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        monthly_backups_to_keep=pulumi.get(__ret__, 'monthly_backups_to_keep'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        volume_backups=pulumi.get(__ret__, 'volume_backups'),
        volumes_assigned=pulumi.get(__ret__, 'volumes_assigned'),
        weekly_backups_to_keep=pulumi.get(__ret__, 'weekly_backups_to_keep'))


@_utilities.lift_output_func(get_backup_policy)
def get_backup_policy_output(account_name: Optional[pulumi.Input[str]] = None,
                             backup_policy_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackupPolicyResult]:
    """
    Get a particular backup Policy


    :param str account_name: The name of the NetApp account
    :param str backup_policy_name: Backup policy Name which uniquely identify backup policy.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
