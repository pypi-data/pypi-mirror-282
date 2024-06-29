# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AzureKeyVaultSmbCredentialsArgs',
    'AzureStorageBlobContainerEndpointPropertiesArgs',
    'AzureStorageSmbFileShareEndpointPropertiesArgs',
    'NfsMountEndpointPropertiesArgs',
    'SmbMountEndpointPropertiesArgs',
    'TimeArgs',
    'UploadLimitScheduleArgs',
    'UploadLimitWeeklyRecurrenceArgs',
]

@pulumi.input_type
class AzureKeyVaultSmbCredentialsArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 password_uri: Optional[pulumi.Input[str]] = None,
                 username_uri: Optional[pulumi.Input[str]] = None):
        """
        The Azure Key Vault secret URIs which store the credentials.
        :param pulumi.Input[str] type: The Credentials type.
               Expected value is 'AzureKeyVaultSmb'.
        :param pulumi.Input[str] password_uri: The Azure Key Vault secret URI which stores the password. Use empty string to clean-up existing value.
        :param pulumi.Input[str] username_uri: The Azure Key Vault secret URI which stores the username. Use empty string to clean-up existing value.
        """
        pulumi.set(__self__, "type", 'AzureKeyVaultSmb')
        if password_uri is not None:
            pulumi.set(__self__, "password_uri", password_uri)
        if username_uri is not None:
            pulumi.set(__self__, "username_uri", username_uri)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The Credentials type.
        Expected value is 'AzureKeyVaultSmb'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="passwordUri")
    def password_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Key Vault secret URI which stores the password. Use empty string to clean-up existing value.
        """
        return pulumi.get(self, "password_uri")

    @password_uri.setter
    def password_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_uri", value)

    @property
    @pulumi.getter(name="usernameUri")
    def username_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure Key Vault secret URI which stores the username. Use empty string to clean-up existing value.
        """
        return pulumi.get(self, "username_uri")

    @username_uri.setter
    def username_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username_uri", value)


@pulumi.input_type
class AzureStorageBlobContainerEndpointPropertiesArgs:
    def __init__(__self__, *,
                 blob_container_name: pulumi.Input[str],
                 endpoint_type: pulumi.Input[str],
                 storage_account_resource_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The properties of Azure Storage blob container endpoint.
        :param pulumi.Input[str] blob_container_name: The name of the Storage blob container that is the target destination.
        :param pulumi.Input[str] endpoint_type: The Endpoint resource type.
               Expected value is 'AzureStorageBlobContainer'.
        :param pulumi.Input[str] storage_account_resource_id: The Azure Resource ID of the storage account that is the target destination.
        :param pulumi.Input[str] description: A description for the Endpoint.
        """
        pulumi.set(__self__, "blob_container_name", blob_container_name)
        pulumi.set(__self__, "endpoint_type", 'AzureStorageBlobContainer')
        pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> pulumi.Input[str]:
        """
        The name of the Storage blob container that is the target destination.
        """
        return pulumi.get(self, "blob_container_name")

    @blob_container_name.setter
    def blob_container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "blob_container_name", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The Endpoint resource type.
        Expected value is 'AzureStorageBlobContainer'.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> pulumi.Input[str]:
        """
        The Azure Resource ID of the storage account that is the target destination.
        """
        return pulumi.get(self, "storage_account_resource_id")

    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_resource_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class AzureStorageSmbFileShareEndpointPropertiesArgs:
    def __init__(__self__, *,
                 endpoint_type: pulumi.Input[str],
                 file_share_name: pulumi.Input[str],
                 storage_account_resource_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The properties of Azure Storage SMB file share endpoint.
        :param pulumi.Input[str] endpoint_type: The Endpoint resource type.
               Expected value is 'AzureStorageSmbFileShare'.
        :param pulumi.Input[str] file_share_name: The name of the Azure Storage file share.
        :param pulumi.Input[str] storage_account_resource_id: The Azure Resource ID of the storage account.
        :param pulumi.Input[str] description: A description for the Endpoint.
        """
        pulumi.set(__self__, "endpoint_type", 'AzureStorageSmbFileShare')
        pulumi.set(__self__, "file_share_name", file_share_name)
        pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The Endpoint resource type.
        Expected value is 'AzureStorageSmbFileShare'.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure Storage file share.
        """
        return pulumi.get(self, "file_share_name")

    @file_share_name.setter
    def file_share_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "file_share_name", value)

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> pulumi.Input[str]:
        """
        The Azure Resource ID of the storage account.
        """
        return pulumi.get(self, "storage_account_resource_id")

    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_resource_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class NfsMountEndpointPropertiesArgs:
    def __init__(__self__, *,
                 endpoint_type: pulumi.Input[str],
                 export: pulumi.Input[str],
                 host: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 nfs_version: Optional[pulumi.Input[Union[str, 'NfsVersion']]] = None):
        """
        The properties of NFS share endpoint.
        :param pulumi.Input[str] endpoint_type: The Endpoint resource type.
               Expected value is 'NfsMount'.
        :param pulumi.Input[str] export: The directory being exported from the server.
        :param pulumi.Input[str] host: The host name or IP address of the server exporting the file system.
        :param pulumi.Input[str] description: A description for the Endpoint.
        :param pulumi.Input[Union[str, 'NfsVersion']] nfs_version: The NFS protocol version.
        """
        pulumi.set(__self__, "endpoint_type", 'NfsMount')
        pulumi.set(__self__, "export", export)
        pulumi.set(__self__, "host", host)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if nfs_version is not None:
            pulumi.set(__self__, "nfs_version", nfs_version)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The Endpoint resource type.
        Expected value is 'NfsMount'.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter
    def export(self) -> pulumi.Input[str]:
        """
        The directory being exported from the server.
        """
        return pulumi.get(self, "export")

    @export.setter
    def export(self, value: pulumi.Input[str]):
        pulumi.set(self, "export", value)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        """
        The host name or IP address of the server exporting the file system.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="nfsVersion")
    def nfs_version(self) -> Optional[pulumi.Input[Union[str, 'NfsVersion']]]:
        """
        The NFS protocol version.
        """
        return pulumi.get(self, "nfs_version")

    @nfs_version.setter
    def nfs_version(self, value: Optional[pulumi.Input[Union[str, 'NfsVersion']]]):
        pulumi.set(self, "nfs_version", value)


@pulumi.input_type
class SmbMountEndpointPropertiesArgs:
    def __init__(__self__, *,
                 endpoint_type: pulumi.Input[str],
                 host: pulumi.Input[str],
                 share_name: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['AzureKeyVaultSmbCredentialsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The properties of SMB share endpoint.
        :param pulumi.Input[str] endpoint_type: The Endpoint resource type.
               Expected value is 'SmbMount'.
        :param pulumi.Input[str] host: The host name or IP address of the server exporting the file system.
        :param pulumi.Input[str] share_name: The name of the SMB share being exported from the server.
        :param pulumi.Input['AzureKeyVaultSmbCredentialsArgs'] credentials: The Azure Key Vault secret URIs which store the required credentials to access the SMB share.
        :param pulumi.Input[str] description: A description for the Endpoint.
        """
        pulumi.set(__self__, "endpoint_type", 'SmbMount')
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "share_name", share_name)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The Endpoint resource type.
        Expected value is 'SmbMount'.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        """
        The host name or IP address of the server exporting the file system.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter(name="shareName")
    def share_name(self) -> pulumi.Input[str]:
        """
        The name of the SMB share being exported from the server.
        """
        return pulumi.get(self, "share_name")

    @share_name.setter
    def share_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "share_name", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['AzureKeyVaultSmbCredentialsArgs']]:
        """
        The Azure Key Vault secret URIs which store the required credentials to access the SMB share.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['AzureKeyVaultSmbCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class TimeArgs:
    def __init__(__self__, *,
                 hour: pulumi.Input[int],
                 minute: Optional[pulumi.Input[int]] = None):
        """
        The time of day.
        :param pulumi.Input[int] hour: The hour element of the time. Allowed values range from 0 (start of the selected day) to 24 (end of the selected day). Hour value 24 cannot be combined with any other minute value but 0.
        :param pulumi.Input[int] minute: The minute element of the time. Allowed values are 0 and 30. If not specified, its value defaults to 0.
        """
        pulumi.set(__self__, "hour", hour)
        if minute is None:
            minute = 0
        if minute is not None:
            pulumi.set(__self__, "minute", minute)

    @property
    @pulumi.getter
    def hour(self) -> pulumi.Input[int]:
        """
        The hour element of the time. Allowed values range from 0 (start of the selected day) to 24 (end of the selected day). Hour value 24 cannot be combined with any other minute value but 0.
        """
        return pulumi.get(self, "hour")

    @hour.setter
    def hour(self, value: pulumi.Input[int]):
        pulumi.set(self, "hour", value)

    @property
    @pulumi.getter
    def minute(self) -> Optional[pulumi.Input[int]]:
        """
        The minute element of the time. Allowed values are 0 and 30. If not specified, its value defaults to 0.
        """
        return pulumi.get(self, "minute")

    @minute.setter
    def minute(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minute", value)


@pulumi.input_type
class UploadLimitScheduleArgs:
    def __init__(__self__, *,
                 weekly_recurrences: Optional[pulumi.Input[Sequence[pulumi.Input['UploadLimitWeeklyRecurrenceArgs']]]] = None):
        """
        The WAN-link upload limit schedule. Overlapping recurrences are not allowed.
        :param pulumi.Input[Sequence[pulumi.Input['UploadLimitWeeklyRecurrenceArgs']]] weekly_recurrences: The set of weekly repeating recurrences of the WAN-link upload limit schedule.
        """
        if weekly_recurrences is not None:
            pulumi.set(__self__, "weekly_recurrences", weekly_recurrences)

    @property
    @pulumi.getter(name="weeklyRecurrences")
    def weekly_recurrences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UploadLimitWeeklyRecurrenceArgs']]]]:
        """
        The set of weekly repeating recurrences of the WAN-link upload limit schedule.
        """
        return pulumi.get(self, "weekly_recurrences")

    @weekly_recurrences.setter
    def weekly_recurrences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UploadLimitWeeklyRecurrenceArgs']]]]):
        pulumi.set(self, "weekly_recurrences", value)


@pulumi.input_type
class UploadLimitWeeklyRecurrenceArgs:
    def __init__(__self__, *,
                 days: pulumi.Input[Sequence[pulumi.Input['DayOfWeek']]],
                 end_time: pulumi.Input['TimeArgs'],
                 limit_in_mbps: pulumi.Input[int],
                 start_time: pulumi.Input['TimeArgs']):
        """
        The weekly recurrence of the WAN-link upload limit schedule. The start time must be earlier in the day than the end time. The recurrence must not span across multiple days.
        :param pulumi.Input[Sequence[pulumi.Input['DayOfWeek']]] days: The set of days of week for the schedule recurrence. A day must not be specified more than once in a recurrence.
        :param pulumi.Input['TimeArgs'] end_time: The end time of the schedule recurrence. Full hour and 30-minute intervals are supported.
        :param pulumi.Input[int] limit_in_mbps: The WAN-link upload bandwidth (maximum data transfer rate) in megabits per second. Value of 0 indicates no throughput is allowed and any running migration job is effectively paused for the duration of this recurrence. Only data plane operations are governed by this limit. Control plane operations ensure seamless functionality. The agent may exceed this limit with control messages, if necessary.
        :param pulumi.Input['TimeArgs'] start_time: The start time of the schedule recurrence. Full hour and 30-minute intervals are supported.
        """
        pulumi.set(__self__, "days", days)
        pulumi.set(__self__, "end_time", end_time)
        pulumi.set(__self__, "limit_in_mbps", limit_in_mbps)
        pulumi.set(__self__, "start_time", start_time)

    @property
    @pulumi.getter
    def days(self) -> pulumi.Input[Sequence[pulumi.Input['DayOfWeek']]]:
        """
        The set of days of week for the schedule recurrence. A day must not be specified more than once in a recurrence.
        """
        return pulumi.get(self, "days")

    @days.setter
    def days(self, value: pulumi.Input[Sequence[pulumi.Input['DayOfWeek']]]):
        pulumi.set(self, "days", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Input['TimeArgs']:
        """
        The end time of the schedule recurrence. Full hour and 30-minute intervals are supported.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: pulumi.Input['TimeArgs']):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter(name="limitInMbps")
    def limit_in_mbps(self) -> pulumi.Input[int]:
        """
        The WAN-link upload bandwidth (maximum data transfer rate) in megabits per second. Value of 0 indicates no throughput is allowed and any running migration job is effectively paused for the duration of this recurrence. Only data plane operations are governed by this limit. Control plane operations ensure seamless functionality. The agent may exceed this limit with control messages, if necessary.
        """
        return pulumi.get(self, "limit_in_mbps")

    @limit_in_mbps.setter
    def limit_in_mbps(self, value: pulumi.Input[int]):
        pulumi.set(self, "limit_in_mbps", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Input['TimeArgs']:
        """
        The start time of the schedule recurrence. Full hour and 30-minute intervals are supported.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: pulumi.Input['TimeArgs']):
        pulumi.set(self, "start_time", value)


