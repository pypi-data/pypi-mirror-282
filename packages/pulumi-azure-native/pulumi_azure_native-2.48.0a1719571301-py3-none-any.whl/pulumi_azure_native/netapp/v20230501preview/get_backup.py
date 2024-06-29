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
    'GetBackupResult',
    'AwaitableGetBackupResult',
    'get_backup',
    'get_backup_output',
]

@pulumi.output_type
class GetBackupResult:
    """
    Backup under a Backup Vault
    """
    def __init__(__self__, backup_id=None, backup_policy_resource_id=None, backup_type=None, creation_date=None, failure_reason=None, id=None, label=None, name=None, provisioning_state=None, size=None, snapshot_name=None, system_data=None, type=None, use_existing_snapshot=None, volume_resource_id=None):
        if backup_id and not isinstance(backup_id, str):
            raise TypeError("Expected argument 'backup_id' to be a str")
        pulumi.set(__self__, "backup_id", backup_id)
        if backup_policy_resource_id and not isinstance(backup_policy_resource_id, str):
            raise TypeError("Expected argument 'backup_policy_resource_id' to be a str")
        pulumi.set(__self__, "backup_policy_resource_id", backup_policy_resource_id)
        if backup_type and not isinstance(backup_type, str):
            raise TypeError("Expected argument 'backup_type' to be a str")
        pulumi.set(__self__, "backup_type", backup_type)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if failure_reason and not isinstance(failure_reason, str):
            raise TypeError("Expected argument 'failure_reason' to be a str")
        pulumi.set(__self__, "failure_reason", failure_reason)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        pulumi.set(__self__, "size", size)
        if snapshot_name and not isinstance(snapshot_name, str):
            raise TypeError("Expected argument 'snapshot_name' to be a str")
        pulumi.set(__self__, "snapshot_name", snapshot_name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if use_existing_snapshot and not isinstance(use_existing_snapshot, bool):
            raise TypeError("Expected argument 'use_existing_snapshot' to be a bool")
        pulumi.set(__self__, "use_existing_snapshot", use_existing_snapshot)
        if volume_resource_id and not isinstance(volume_resource_id, str):
            raise TypeError("Expected argument 'volume_resource_id' to be a str")
        pulumi.set(__self__, "volume_resource_id", volume_resource_id)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> str:
        """
        UUID v4 used to identify the Backup
        """
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="backupPolicyResourceId")
    def backup_policy_resource_id(self) -> str:
        """
        ResourceId used to identify the backup policy
        """
        return pulumi.get(self, "backup_policy_resource_id")

    @property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> str:
        """
        Type of backup Manual or Scheduled
        """
        return pulumi.get(self, "backup_type")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The creation date of the backup
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> str:
        """
        Failure reason
        """
        return pulumi.get(self, "failure_reason")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def label(self) -> Optional[str]:
        """
        Label for backup
        """
        return pulumi.get(self, "label")

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
    @pulumi.getter
    def size(self) -> float:
        """
        Size of backup in bytes
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[str]:
        """
        The name of the snapshot
        """
        return pulumi.get(self, "snapshot_name")

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

    @property
    @pulumi.getter(name="useExistingSnapshot")
    def use_existing_snapshot(self) -> Optional[bool]:
        """
        Manual backup an already existing snapshot. This will always be false for scheduled backups and true/false for manual backups
        """
        return pulumi.get(self, "use_existing_snapshot")

    @property
    @pulumi.getter(name="volumeResourceId")
    def volume_resource_id(self) -> str:
        """
        ResourceId used to identify the Volume
        """
        return pulumi.get(self, "volume_resource_id")


class AwaitableGetBackupResult(GetBackupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackupResult(
            backup_id=self.backup_id,
            backup_policy_resource_id=self.backup_policy_resource_id,
            backup_type=self.backup_type,
            creation_date=self.creation_date,
            failure_reason=self.failure_reason,
            id=self.id,
            label=self.label,
            name=self.name,
            provisioning_state=self.provisioning_state,
            size=self.size,
            snapshot_name=self.snapshot_name,
            system_data=self.system_data,
            type=self.type,
            use_existing_snapshot=self.use_existing_snapshot,
            volume_resource_id=self.volume_resource_id)


def get_backup(account_name: Optional[str] = None,
               backup_name: Optional[str] = None,
               backup_vault_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackupResult:
    """
    Get the specified Backup under Backup Vault.


    :param str account_name: The name of the NetApp account
    :param str backup_name: The name of the backup
    :param str backup_vault_name: The name of the Backup Vault
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['backupName'] = backup_name
    __args__['backupVaultName'] = backup_vault_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20230501preview:getBackup', __args__, opts=opts, typ=GetBackupResult).value

    return AwaitableGetBackupResult(
        backup_id=pulumi.get(__ret__, 'backup_id'),
        backup_policy_resource_id=pulumi.get(__ret__, 'backup_policy_resource_id'),
        backup_type=pulumi.get(__ret__, 'backup_type'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        failure_reason=pulumi.get(__ret__, 'failure_reason'),
        id=pulumi.get(__ret__, 'id'),
        label=pulumi.get(__ret__, 'label'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        size=pulumi.get(__ret__, 'size'),
        snapshot_name=pulumi.get(__ret__, 'snapshot_name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        use_existing_snapshot=pulumi.get(__ret__, 'use_existing_snapshot'),
        volume_resource_id=pulumi.get(__ret__, 'volume_resource_id'))


@_utilities.lift_output_func(get_backup)
def get_backup_output(account_name: Optional[pulumi.Input[str]] = None,
                      backup_name: Optional[pulumi.Input[str]] = None,
                      backup_vault_name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackupResult]:
    """
    Get the specified Backup under Backup Vault.


    :param str account_name: The name of the NetApp account
    :param str backup_name: The name of the backup
    :param str backup_vault_name: The name of the Backup Vault
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
