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
from ._enums import *

__all__ = [
    'AgentPropertiesResponseErrorDetails',
    'AzureKeyVaultSmbCredentialsResponse',
    'AzureStorageBlobContainerEndpointPropertiesResponse',
    'AzureStorageSmbFileShareEndpointPropertiesResponse',
    'NfsMountEndpointPropertiesResponse',
    'SmbMountEndpointPropertiesResponse',
    'SystemDataResponse',
    'TimeResponse',
    'UploadLimitScheduleResponse',
    'UploadLimitWeeklyRecurrenceResponse',
]

@pulumi.output_type
class AgentPropertiesResponseErrorDetails(dict):
    def __init__(__self__, *,
                 code: Optional[str] = None,
                 message: Optional[str] = None):
        """
        :param str code: Error code reported by Agent
        :param str message: Expanded description of reported error code
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        Error code reported by Agent
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        Expanded description of reported error code
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class AzureKeyVaultSmbCredentialsResponse(dict):
    """
    The Azure Key Vault secret URIs which store the credentials.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "passwordUri":
            suggest = "password_uri"
        elif key == "usernameUri":
            suggest = "username_uri"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AzureKeyVaultSmbCredentialsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AzureKeyVaultSmbCredentialsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AzureKeyVaultSmbCredentialsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 password_uri: Optional[str] = None,
                 username_uri: Optional[str] = None):
        """
        The Azure Key Vault secret URIs which store the credentials.
        :param str type: The Credentials type.
               Expected value is 'AzureKeyVaultSmb'.
        :param str password_uri: The Azure Key Vault secret URI which stores the password. Use empty string to clean-up existing value.
        :param str username_uri: The Azure Key Vault secret URI which stores the username. Use empty string to clean-up existing value.
        """
        pulumi.set(__self__, "type", 'AzureKeyVaultSmb')
        if password_uri is not None:
            pulumi.set(__self__, "password_uri", password_uri)
        if username_uri is not None:
            pulumi.set(__self__, "username_uri", username_uri)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The Credentials type.
        Expected value is 'AzureKeyVaultSmb'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="passwordUri")
    def password_uri(self) -> Optional[str]:
        """
        The Azure Key Vault secret URI which stores the password. Use empty string to clean-up existing value.
        """
        return pulumi.get(self, "password_uri")

    @property
    @pulumi.getter(name="usernameUri")
    def username_uri(self) -> Optional[str]:
        """
        The Azure Key Vault secret URI which stores the username. Use empty string to clean-up existing value.
        """
        return pulumi.get(self, "username_uri")


@pulumi.output_type
class AzureStorageBlobContainerEndpointPropertiesResponse(dict):
    """
    The properties of Azure Storage blob container endpoint.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "blobContainerName":
            suggest = "blob_container_name"
        elif key == "endpointType":
            suggest = "endpoint_type"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "storageAccountResourceId":
            suggest = "storage_account_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AzureStorageBlobContainerEndpointPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AzureStorageBlobContainerEndpointPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AzureStorageBlobContainerEndpointPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 blob_container_name: str,
                 endpoint_type: str,
                 provisioning_state: str,
                 storage_account_resource_id: str,
                 description: Optional[str] = None):
        """
        The properties of Azure Storage blob container endpoint.
        :param str blob_container_name: The name of the Storage blob container that is the target destination.
        :param str endpoint_type: The Endpoint resource type.
               Expected value is 'AzureStorageBlobContainer'.
        :param str provisioning_state: The provisioning state of this resource.
        :param str storage_account_resource_id: The Azure Resource ID of the storage account that is the target destination.
        :param str description: A description for the Endpoint.
        """
        pulumi.set(__self__, "blob_container_name", blob_container_name)
        pulumi.set(__self__, "endpoint_type", 'AzureStorageBlobContainer')
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> str:
        """
        The name of the Storage blob container that is the target destination.
        """
        return pulumi.get(self, "blob_container_name")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> str:
        """
        The Endpoint resource type.
        Expected value is 'AzureStorageBlobContainer'.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of this resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> str:
        """
        The Azure Resource ID of the storage account that is the target destination.
        """
        return pulumi.get(self, "storage_account_resource_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")


@pulumi.output_type
class AzureStorageSmbFileShareEndpointPropertiesResponse(dict):
    """
    The properties of Azure Storage SMB file share endpoint.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endpointType":
            suggest = "endpoint_type"
        elif key == "fileShareName":
            suggest = "file_share_name"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "storageAccountResourceId":
            suggest = "storage_account_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AzureStorageSmbFileShareEndpointPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AzureStorageSmbFileShareEndpointPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AzureStorageSmbFileShareEndpointPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint_type: str,
                 file_share_name: str,
                 provisioning_state: str,
                 storage_account_resource_id: str,
                 description: Optional[str] = None):
        """
        The properties of Azure Storage SMB file share endpoint.
        :param str endpoint_type: The Endpoint resource type.
               Expected value is 'AzureStorageSmbFileShare'.
        :param str file_share_name: The name of the Azure Storage file share.
        :param str provisioning_state: The provisioning state of this resource.
        :param str storage_account_resource_id: The Azure Resource ID of the storage account.
        :param str description: A description for the Endpoint.
        """
        pulumi.set(__self__, "endpoint_type", 'AzureStorageSmbFileShare')
        pulumi.set(__self__, "file_share_name", file_share_name)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> str:
        """
        The Endpoint resource type.
        Expected value is 'AzureStorageSmbFileShare'.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> str:
        """
        The name of the Azure Storage file share.
        """
        return pulumi.get(self, "file_share_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of this resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> str:
        """
        The Azure Resource ID of the storage account.
        """
        return pulumi.get(self, "storage_account_resource_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")


@pulumi.output_type
class NfsMountEndpointPropertiesResponse(dict):
    """
    The properties of NFS share endpoint.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endpointType":
            suggest = "endpoint_type"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "nfsVersion":
            suggest = "nfs_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NfsMountEndpointPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NfsMountEndpointPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NfsMountEndpointPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint_type: str,
                 export: str,
                 host: str,
                 provisioning_state: str,
                 description: Optional[str] = None,
                 nfs_version: Optional[str] = None):
        """
        The properties of NFS share endpoint.
        :param str endpoint_type: The Endpoint resource type.
               Expected value is 'NfsMount'.
        :param str export: The directory being exported from the server.
        :param str host: The host name or IP address of the server exporting the file system.
        :param str provisioning_state: The provisioning state of this resource.
        :param str description: A description for the Endpoint.
        :param str nfs_version: The NFS protocol version.
        """
        pulumi.set(__self__, "endpoint_type", 'NfsMount')
        pulumi.set(__self__, "export", export)
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if nfs_version is not None:
            pulumi.set(__self__, "nfs_version", nfs_version)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> str:
        """
        The Endpoint resource type.
        Expected value is 'NfsMount'.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter
    def export(self) -> str:
        """
        The directory being exported from the server.
        """
        return pulumi.get(self, "export")

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        The host name or IP address of the server exporting the file system.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of this resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="nfsVersion")
    def nfs_version(self) -> Optional[str]:
        """
        The NFS protocol version.
        """
        return pulumi.get(self, "nfs_version")


@pulumi.output_type
class SmbMountEndpointPropertiesResponse(dict):
    """
    The properties of SMB share endpoint.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endpointType":
            suggest = "endpoint_type"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "shareName":
            suggest = "share_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SmbMountEndpointPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SmbMountEndpointPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SmbMountEndpointPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint_type: str,
                 host: str,
                 provisioning_state: str,
                 share_name: str,
                 credentials: Optional['outputs.AzureKeyVaultSmbCredentialsResponse'] = None,
                 description: Optional[str] = None):
        """
        The properties of SMB share endpoint.
        :param str endpoint_type: The Endpoint resource type.
               Expected value is 'SmbMount'.
        :param str host: The host name or IP address of the server exporting the file system.
        :param str provisioning_state: The provisioning state of this resource.
        :param str share_name: The name of the SMB share being exported from the server.
        :param 'AzureKeyVaultSmbCredentialsResponse' credentials: The Azure Key Vault secret URIs which store the required credentials to access the SMB share.
        :param str description: A description for the Endpoint.
        """
        pulumi.set(__self__, "endpoint_type", 'SmbMount')
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "share_name", share_name)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> str:
        """
        The Endpoint resource type.
        Expected value is 'SmbMount'.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        The host name or IP address of the server exporting the file system.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of this resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="shareName")
    def share_name(self) -> str:
        """
        The name of the SMB share being exported from the server.
        """
        return pulumi.get(self, "share_name")

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.AzureKeyVaultSmbCredentialsResponse']:
        """
        The Azure Key Vault secret URIs which store the required credentials to access the SMB share.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")


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


@pulumi.output_type
class TimeResponse(dict):
    """
    The time of day.
    """
    def __init__(__self__, *,
                 hour: int,
                 minute: Optional[int] = None):
        """
        The time of day.
        :param int hour: The hour element of the time. Allowed values range from 0 (start of the selected day) to 24 (end of the selected day). Hour value 24 cannot be combined with any other minute value but 0.
        :param int minute: The minute element of the time. Allowed values are 0 and 30. If not specified, its value defaults to 0.
        """
        pulumi.set(__self__, "hour", hour)
        if minute is None:
            minute = 0
        if minute is not None:
            pulumi.set(__self__, "minute", minute)

    @property
    @pulumi.getter
    def hour(self) -> int:
        """
        The hour element of the time. Allowed values range from 0 (start of the selected day) to 24 (end of the selected day). Hour value 24 cannot be combined with any other minute value but 0.
        """
        return pulumi.get(self, "hour")

    @property
    @pulumi.getter
    def minute(self) -> Optional[int]:
        """
        The minute element of the time. Allowed values are 0 and 30. If not specified, its value defaults to 0.
        """
        return pulumi.get(self, "minute")


@pulumi.output_type
class UploadLimitScheduleResponse(dict):
    """
    The WAN-link upload limit schedule. Overlapping recurrences are not allowed.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "weeklyRecurrences":
            suggest = "weekly_recurrences"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UploadLimitScheduleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UploadLimitScheduleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UploadLimitScheduleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 weekly_recurrences: Optional[Sequence['outputs.UploadLimitWeeklyRecurrenceResponse']] = None):
        """
        The WAN-link upload limit schedule. Overlapping recurrences are not allowed.
        :param Sequence['UploadLimitWeeklyRecurrenceResponse'] weekly_recurrences: The set of weekly repeating recurrences of the WAN-link upload limit schedule.
        """
        if weekly_recurrences is not None:
            pulumi.set(__self__, "weekly_recurrences", weekly_recurrences)

    @property
    @pulumi.getter(name="weeklyRecurrences")
    def weekly_recurrences(self) -> Optional[Sequence['outputs.UploadLimitWeeklyRecurrenceResponse']]:
        """
        The set of weekly repeating recurrences of the WAN-link upload limit schedule.
        """
        return pulumi.get(self, "weekly_recurrences")


@pulumi.output_type
class UploadLimitWeeklyRecurrenceResponse(dict):
    """
    The weekly recurrence of the WAN-link upload limit schedule. The start time must be earlier in the day than the end time. The recurrence must not span across multiple days.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "endTime":
            suggest = "end_time"
        elif key == "limitInMbps":
            suggest = "limit_in_mbps"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UploadLimitWeeklyRecurrenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UploadLimitWeeklyRecurrenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UploadLimitWeeklyRecurrenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days: Sequence[str],
                 end_time: 'outputs.TimeResponse',
                 limit_in_mbps: int,
                 start_time: 'outputs.TimeResponse'):
        """
        The weekly recurrence of the WAN-link upload limit schedule. The start time must be earlier in the day than the end time. The recurrence must not span across multiple days.
        :param Sequence[str] days: The set of days of week for the schedule recurrence. A day must not be specified more than once in a recurrence.
        :param 'TimeResponse' end_time: The end time of the schedule recurrence. Full hour and 30-minute intervals are supported.
        :param int limit_in_mbps: The WAN-link upload bandwidth (maximum data transfer rate) in megabits per second. Value of 0 indicates no throughput is allowed and any running migration job is effectively paused for the duration of this recurrence. Only data plane operations are governed by this limit. Control plane operations ensure seamless functionality. The agent may exceed this limit with control messages, if necessary.
        :param 'TimeResponse' start_time: The start time of the schedule recurrence. Full hour and 30-minute intervals are supported.
        """
        pulumi.set(__self__, "days", days)
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "limit_in_mbps", limit_in_mbps)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter
    def days(self) -> Sequence[str]:
        """
        The set of days of week for the schedule recurrence. A day must not be specified more than once in a recurrence.
        """
        return pulumi.get(self, "days")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> 'outputs.TimeResponse':
        """
        The end time of the schedule recurrence. Full hour and 30-minute intervals are supported.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="limitInMbps")
    def limit_in_mbps(self) -> int:
        """
        The WAN-link upload bandwidth (maximum data transfer rate) in megabits per second. Value of 0 indicates no throughput is allowed and any running migration job is effectively paused for the duration of this recurrence. Only data plane operations are governed by this limit. Control plane operations ensure seamless functionality. The agent may exceed this limit with control messages, if necessary.
        """
        return pulumi.get(self, "limit_in_mbps")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> 'outputs.TimeResponse':
        """
        The start time of the schedule recurrence. Full hour and 30-minute intervals are supported.
        """
        return pulumi.get(self, "start_time")


