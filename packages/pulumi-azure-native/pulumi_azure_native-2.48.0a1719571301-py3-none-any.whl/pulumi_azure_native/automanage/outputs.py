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

__all__ = [
    'AccountIdentityResponse',
    'ConfigurationProfileAssignmentPropertiesResponse',
    'ConfigurationProfilePreferenceAntiMalwareResponse',
    'ConfigurationProfilePreferencePropertiesResponse',
    'ConfigurationProfilePreferenceVmBackupResponse',
    'ConfigurationProfilePropertiesResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class AccountIdentityResponse(dict):
    """
    Identity for the Automanage account.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccountIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccountIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccountIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Identity for the Automanage account.
        :param str principal_id: The principal id of Automanage account identity.
        :param str tenant_id: The tenant id associated with the Automanage account.
        :param str type: The type of identity used for the Automanage account. Currently, the only supported type is 'SystemAssigned', which implicitly creates an identity.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal id of Automanage account identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant id associated with the Automanage account.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of identity used for the Automanage account. Currently, the only supported type is 'SystemAssigned', which implicitly creates an identity.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ConfigurationProfileAssignmentPropertiesResponse(dict):
    """
    Automanage configuration profile assignment properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "targetId":
            suggest = "target_id"
        elif key == "configurationProfile":
            suggest = "configuration_profile"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationProfileAssignmentPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationProfileAssignmentPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationProfileAssignmentPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 status: str,
                 target_id: str,
                 configuration_profile: Optional[str] = None):
        """
        Automanage configuration profile assignment properties.
        :param str status: The status of onboarding, which only appears in the response.
        :param str target_id: The target VM resource URI
        :param str configuration_profile: The Automanage configurationProfile ARM Resource URI.
        """
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "target_id", target_id)
        if configuration_profile is not None:
            pulumi.set(__self__, "configuration_profile", configuration_profile)

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of onboarding, which only appears in the response.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> str:
        """
        The target VM resource URI
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="configurationProfile")
    def configuration_profile(self) -> Optional[str]:
        """
        The Automanage configurationProfile ARM Resource URI.
        """
        return pulumi.get(self, "configuration_profile")


@pulumi.output_type
class ConfigurationProfilePreferenceAntiMalwareResponse(dict):
    """
    Automanage configuration profile Antimalware preferences.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enableRealTimeProtection":
            suggest = "enable_real_time_protection"
        elif key == "runScheduledScan":
            suggest = "run_scheduled_scan"
        elif key == "scanDay":
            suggest = "scan_day"
        elif key == "scanTimeInMinutes":
            suggest = "scan_time_in_minutes"
        elif key == "scanType":
            suggest = "scan_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationProfilePreferenceAntiMalwareResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationProfilePreferenceAntiMalwareResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationProfilePreferenceAntiMalwareResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enable_real_time_protection: Optional[str] = None,
                 exclusions: Optional[Any] = None,
                 run_scheduled_scan: Optional[str] = None,
                 scan_day: Optional[str] = None,
                 scan_time_in_minutes: Optional[str] = None,
                 scan_type: Optional[str] = None):
        """
        Automanage configuration profile Antimalware preferences.
        :param str enable_real_time_protection: Enables or disables Real Time Protection
        :param Any exclusions: Extensions, Paths and Processes that must be excluded from scan
        :param str run_scheduled_scan: Enables or disables a periodic scan for antimalware
        :param str scan_day: Schedule scan settings day
        :param str scan_time_in_minutes: Schedule scan settings time
        :param str scan_type: Type of scheduled scan
        """
        if enable_real_time_protection is not None:
            pulumi.set(__self__, "enable_real_time_protection", enable_real_time_protection)
        if exclusions is not None:
            pulumi.set(__self__, "exclusions", exclusions)
        if run_scheduled_scan is not None:
            pulumi.set(__self__, "run_scheduled_scan", run_scheduled_scan)
        if scan_day is not None:
            pulumi.set(__self__, "scan_day", scan_day)
        if scan_time_in_minutes is not None:
            pulumi.set(__self__, "scan_time_in_minutes", scan_time_in_minutes)
        if scan_type is not None:
            pulumi.set(__self__, "scan_type", scan_type)

    @property
    @pulumi.getter(name="enableRealTimeProtection")
    def enable_real_time_protection(self) -> Optional[str]:
        """
        Enables or disables Real Time Protection
        """
        return pulumi.get(self, "enable_real_time_protection")

    @property
    @pulumi.getter
    def exclusions(self) -> Optional[Any]:
        """
        Extensions, Paths and Processes that must be excluded from scan
        """
        return pulumi.get(self, "exclusions")

    @property
    @pulumi.getter(name="runScheduledScan")
    def run_scheduled_scan(self) -> Optional[str]:
        """
        Enables or disables a periodic scan for antimalware
        """
        return pulumi.get(self, "run_scheduled_scan")

    @property
    @pulumi.getter(name="scanDay")
    def scan_day(self) -> Optional[str]:
        """
        Schedule scan settings day
        """
        return pulumi.get(self, "scan_day")

    @property
    @pulumi.getter(name="scanTimeInMinutes")
    def scan_time_in_minutes(self) -> Optional[str]:
        """
        Schedule scan settings time
        """
        return pulumi.get(self, "scan_time_in_minutes")

    @property
    @pulumi.getter(name="scanType")
    def scan_type(self) -> Optional[str]:
        """
        Type of scheduled scan
        """
        return pulumi.get(self, "scan_type")


@pulumi.output_type
class ConfigurationProfilePreferencePropertiesResponse(dict):
    """
    Automanage configuration profile preference properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "antiMalware":
            suggest = "anti_malware"
        elif key == "vmBackup":
            suggest = "vm_backup"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationProfilePreferencePropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationProfilePreferencePropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationProfilePreferencePropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 anti_malware: Optional['outputs.ConfigurationProfilePreferenceAntiMalwareResponse'] = None,
                 vm_backup: Optional['outputs.ConfigurationProfilePreferenceVmBackupResponse'] = None):
        """
        Automanage configuration profile preference properties.
        :param 'ConfigurationProfilePreferenceAntiMalwareResponse' anti_malware: The custom preferences for Azure Antimalware.
        :param 'ConfigurationProfilePreferenceVmBackupResponse' vm_backup: The custom preferences for Azure VM Backup.
        """
        if anti_malware is not None:
            pulumi.set(__self__, "anti_malware", anti_malware)
        if vm_backup is not None:
            pulumi.set(__self__, "vm_backup", vm_backup)

    @property
    @pulumi.getter(name="antiMalware")
    def anti_malware(self) -> Optional['outputs.ConfigurationProfilePreferenceAntiMalwareResponse']:
        """
        The custom preferences for Azure Antimalware.
        """
        return pulumi.get(self, "anti_malware")

    @property
    @pulumi.getter(name="vmBackup")
    def vm_backup(self) -> Optional['outputs.ConfigurationProfilePreferenceVmBackupResponse']:
        """
        The custom preferences for Azure VM Backup.
        """
        return pulumi.get(self, "vm_backup")


@pulumi.output_type
class ConfigurationProfilePreferenceVmBackupResponse(dict):
    """
    Automanage configuration profile VM Backup preferences.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "instantRpRetentionRangeInDays":
            suggest = "instant_rp_retention_range_in_days"
        elif key == "retentionPolicy":
            suggest = "retention_policy"
        elif key == "schedulePolicy":
            suggest = "schedule_policy"
        elif key == "timeZone":
            suggest = "time_zone"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConfigurationProfilePreferenceVmBackupResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConfigurationProfilePreferenceVmBackupResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConfigurationProfilePreferenceVmBackupResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 instant_rp_retention_range_in_days: Optional[int] = None,
                 retention_policy: Optional[str] = None,
                 schedule_policy: Optional[str] = None,
                 time_zone: Optional[str] = None):
        """
        Automanage configuration profile VM Backup preferences.
        :param int instant_rp_retention_range_in_days: Instant RP retention policy range in days
        :param str retention_policy: Retention policy with the details on backup copy retention ranges.
        :param str schedule_policy: Backup schedule specified as part of backup policy.
        :param str time_zone: TimeZone optional input as string. For example: Pacific Standard Time
        """
        if instant_rp_retention_range_in_days is not None:
            pulumi.set(__self__, "instant_rp_retention_range_in_days", instant_rp_retention_range_in_days)
        if retention_policy is not None:
            pulumi.set(__self__, "retention_policy", retention_policy)
        if schedule_policy is not None:
            pulumi.set(__self__, "schedule_policy", schedule_policy)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="instantRpRetentionRangeInDays")
    def instant_rp_retention_range_in_days(self) -> Optional[int]:
        """
        Instant RP retention policy range in days
        """
        return pulumi.get(self, "instant_rp_retention_range_in_days")

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[str]:
        """
        Retention policy with the details on backup copy retention ranges.
        """
        return pulumi.get(self, "retention_policy")

    @property
    @pulumi.getter(name="schedulePolicy")
    def schedule_policy(self) -> Optional[str]:
        """
        Backup schedule specified as part of backup policy.
        """
        return pulumi.get(self, "schedule_policy")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        TimeZone optional input as string. For example: Pacific Standard Time
        """
        return pulumi.get(self, "time_zone")


@pulumi.output_type
class ConfigurationProfilePropertiesResponse(dict):
    """
    Automanage configuration profile properties.
    """
    def __init__(__self__, *,
                 configuration: Optional[Any] = None):
        """
        Automanage configuration profile properties.
        :param Any configuration: configuration dictionary of the configuration profile.
        """
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[Any]:
        """
        configuration dictionary of the configuration profile.
        """
        return pulumi.get(self, "configuration")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


