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
    'ManagedServiceIdentityArgs',
    'PrivateLinkServiceConnectionStateArgs',
    'RedisCommonPropertiesRedisConfigurationArgs',
    'ScheduleEntryArgs',
    'SkuArgs',
]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Managed service identity (system assigned and/or user assigned identities)
        :param pulumi.Input[Union[str, 'ManagedServiceIdentityType']] type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ManagedServiceIdentityType']]:
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval/rejection of the connection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class RedisCommonPropertiesRedisConfigurationArgs:
    def __init__(__self__, *,
                 aad_enabled: Optional[pulumi.Input[str]] = None,
                 aof_backup_enabled: Optional[pulumi.Input[str]] = None,
                 aof_storage_connection_string0: Optional[pulumi.Input[str]] = None,
                 aof_storage_connection_string1: Optional[pulumi.Input[str]] = None,
                 authnotrequired: Optional[pulumi.Input[str]] = None,
                 maxfragmentationmemory_reserved: Optional[pulumi.Input[str]] = None,
                 maxmemory_delta: Optional[pulumi.Input[str]] = None,
                 maxmemory_policy: Optional[pulumi.Input[str]] = None,
                 maxmemory_reserved: Optional[pulumi.Input[str]] = None,
                 notify_keyspace_events: Optional[pulumi.Input[str]] = None,
                 preferred_data_persistence_auth_method: Optional[pulumi.Input[str]] = None,
                 rdb_backup_enabled: Optional[pulumi.Input[str]] = None,
                 rdb_backup_frequency: Optional[pulumi.Input[str]] = None,
                 rdb_backup_max_snapshot_count: Optional[pulumi.Input[str]] = None,
                 rdb_storage_connection_string: Optional[pulumi.Input[str]] = None,
                 storage_subscription_id: Optional[pulumi.Input[str]] = None):
        """
        All Redis Settings. Few possible keys: rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value etc.
        :param pulumi.Input[str] aad_enabled: Specifies whether AAD based authentication has been enabled or disabled for the cache
        :param pulumi.Input[str] aof_backup_enabled: Specifies whether the aof backup is enabled
        :param pulumi.Input[str] aof_storage_connection_string0: First storage account connection string
        :param pulumi.Input[str] aof_storage_connection_string1: Second storage account connection string
        :param pulumi.Input[str] authnotrequired: Specifies whether the authentication is disabled. Setting this property is highly discouraged from security point of view.
        :param pulumi.Input[str] maxfragmentationmemory_reserved: Value in megabytes reserved for fragmentation per shard
        :param pulumi.Input[str] maxmemory_delta: Value in megabytes reserved for non-cache usage per shard e.g. failover.
        :param pulumi.Input[str] maxmemory_policy: The eviction strategy used when your data won't fit within its memory limit.
        :param pulumi.Input[str] maxmemory_reserved: Value in megabytes reserved for non-cache usage per shard e.g. failover.
        :param pulumi.Input[str] notify_keyspace_events: The keyspace events which should be monitored.
        :param pulumi.Input[str] preferred_data_persistence_auth_method: Preferred auth method to communicate to storage account used for data persistence, specify SAS or ManagedIdentity, default value is SAS
        :param pulumi.Input[str] rdb_backup_enabled: Specifies whether the rdb backup is enabled
        :param pulumi.Input[str] rdb_backup_frequency: Specifies the frequency for creating rdb backup in minutes. Valid values: (15, 30, 60, 360, 720, 1440)
        :param pulumi.Input[str] rdb_backup_max_snapshot_count: Specifies the maximum number of snapshots for rdb backup
        :param pulumi.Input[str] rdb_storage_connection_string: The storage account connection string for storing rdb file
        :param pulumi.Input[str] storage_subscription_id: SubscriptionId of the storage account for persistence (aof/rdb) using ManagedIdentity.
        """
        if aad_enabled is not None:
            pulumi.set(__self__, "aad_enabled", aad_enabled)
        if aof_backup_enabled is not None:
            pulumi.set(__self__, "aof_backup_enabled", aof_backup_enabled)
        if aof_storage_connection_string0 is not None:
            pulumi.set(__self__, "aof_storage_connection_string0", aof_storage_connection_string0)
        if aof_storage_connection_string1 is not None:
            pulumi.set(__self__, "aof_storage_connection_string1", aof_storage_connection_string1)
        if authnotrequired is not None:
            pulumi.set(__self__, "authnotrequired", authnotrequired)
        if maxfragmentationmemory_reserved is not None:
            pulumi.set(__self__, "maxfragmentationmemory_reserved", maxfragmentationmemory_reserved)
        if maxmemory_delta is not None:
            pulumi.set(__self__, "maxmemory_delta", maxmemory_delta)
        if maxmemory_policy is not None:
            pulumi.set(__self__, "maxmemory_policy", maxmemory_policy)
        if maxmemory_reserved is not None:
            pulumi.set(__self__, "maxmemory_reserved", maxmemory_reserved)
        if notify_keyspace_events is not None:
            pulumi.set(__self__, "notify_keyspace_events", notify_keyspace_events)
        if preferred_data_persistence_auth_method is not None:
            pulumi.set(__self__, "preferred_data_persistence_auth_method", preferred_data_persistence_auth_method)
        if rdb_backup_enabled is not None:
            pulumi.set(__self__, "rdb_backup_enabled", rdb_backup_enabled)
        if rdb_backup_frequency is not None:
            pulumi.set(__self__, "rdb_backup_frequency", rdb_backup_frequency)
        if rdb_backup_max_snapshot_count is not None:
            pulumi.set(__self__, "rdb_backup_max_snapshot_count", rdb_backup_max_snapshot_count)
        if rdb_storage_connection_string is not None:
            pulumi.set(__self__, "rdb_storage_connection_string", rdb_storage_connection_string)
        if storage_subscription_id is not None:
            pulumi.set(__self__, "storage_subscription_id", storage_subscription_id)

    @property
    @pulumi.getter(name="aadEnabled")
    def aad_enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether AAD based authentication has been enabled or disabled for the cache
        """
        return pulumi.get(self, "aad_enabled")

    @aad_enabled.setter
    def aad_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aad_enabled", value)

    @property
    @pulumi.getter(name="aofBackupEnabled")
    def aof_backup_enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether the aof backup is enabled
        """
        return pulumi.get(self, "aof_backup_enabled")

    @aof_backup_enabled.setter
    def aof_backup_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aof_backup_enabled", value)

    @property
    @pulumi.getter(name="aofStorageConnectionString0")
    def aof_storage_connection_string0(self) -> Optional[pulumi.Input[str]]:
        """
        First storage account connection string
        """
        return pulumi.get(self, "aof_storage_connection_string0")

    @aof_storage_connection_string0.setter
    def aof_storage_connection_string0(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aof_storage_connection_string0", value)

    @property
    @pulumi.getter(name="aofStorageConnectionString1")
    def aof_storage_connection_string1(self) -> Optional[pulumi.Input[str]]:
        """
        Second storage account connection string
        """
        return pulumi.get(self, "aof_storage_connection_string1")

    @aof_storage_connection_string1.setter
    def aof_storage_connection_string1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aof_storage_connection_string1", value)

    @property
    @pulumi.getter
    def authnotrequired(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether the authentication is disabled. Setting this property is highly discouraged from security point of view.
        """
        return pulumi.get(self, "authnotrequired")

    @authnotrequired.setter
    def authnotrequired(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authnotrequired", value)

    @property
    @pulumi.getter(name="maxfragmentationmemoryReserved")
    def maxfragmentationmemory_reserved(self) -> Optional[pulumi.Input[str]]:
        """
        Value in megabytes reserved for fragmentation per shard
        """
        return pulumi.get(self, "maxfragmentationmemory_reserved")

    @maxfragmentationmemory_reserved.setter
    def maxfragmentationmemory_reserved(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maxfragmentationmemory_reserved", value)

    @property
    @pulumi.getter(name="maxmemoryDelta")
    def maxmemory_delta(self) -> Optional[pulumi.Input[str]]:
        """
        Value in megabytes reserved for non-cache usage per shard e.g. failover.
        """
        return pulumi.get(self, "maxmemory_delta")

    @maxmemory_delta.setter
    def maxmemory_delta(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maxmemory_delta", value)

    @property
    @pulumi.getter(name="maxmemoryPolicy")
    def maxmemory_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The eviction strategy used when your data won't fit within its memory limit.
        """
        return pulumi.get(self, "maxmemory_policy")

    @maxmemory_policy.setter
    def maxmemory_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maxmemory_policy", value)

    @property
    @pulumi.getter(name="maxmemoryReserved")
    def maxmemory_reserved(self) -> Optional[pulumi.Input[str]]:
        """
        Value in megabytes reserved for non-cache usage per shard e.g. failover.
        """
        return pulumi.get(self, "maxmemory_reserved")

    @maxmemory_reserved.setter
    def maxmemory_reserved(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maxmemory_reserved", value)

    @property
    @pulumi.getter(name="notifyKeyspaceEvents")
    def notify_keyspace_events(self) -> Optional[pulumi.Input[str]]:
        """
        The keyspace events which should be monitored.
        """
        return pulumi.get(self, "notify_keyspace_events")

    @notify_keyspace_events.setter
    def notify_keyspace_events(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notify_keyspace_events", value)

    @property
    @pulumi.getter(name="preferredDataPersistenceAuthMethod")
    def preferred_data_persistence_auth_method(self) -> Optional[pulumi.Input[str]]:
        """
        Preferred auth method to communicate to storage account used for data persistence, specify SAS or ManagedIdentity, default value is SAS
        """
        return pulumi.get(self, "preferred_data_persistence_auth_method")

    @preferred_data_persistence_auth_method.setter
    def preferred_data_persistence_auth_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_data_persistence_auth_method", value)

    @property
    @pulumi.getter(name="rdbBackupEnabled")
    def rdb_backup_enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether the rdb backup is enabled
        """
        return pulumi.get(self, "rdb_backup_enabled")

    @rdb_backup_enabled.setter
    def rdb_backup_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rdb_backup_enabled", value)

    @property
    @pulumi.getter(name="rdbBackupFrequency")
    def rdb_backup_frequency(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the frequency for creating rdb backup in minutes. Valid values: (15, 30, 60, 360, 720, 1440)
        """
        return pulumi.get(self, "rdb_backup_frequency")

    @rdb_backup_frequency.setter
    def rdb_backup_frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rdb_backup_frequency", value)

    @property
    @pulumi.getter(name="rdbBackupMaxSnapshotCount")
    def rdb_backup_max_snapshot_count(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the maximum number of snapshots for rdb backup
        """
        return pulumi.get(self, "rdb_backup_max_snapshot_count")

    @rdb_backup_max_snapshot_count.setter
    def rdb_backup_max_snapshot_count(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rdb_backup_max_snapshot_count", value)

    @property
    @pulumi.getter(name="rdbStorageConnectionString")
    def rdb_storage_connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        The storage account connection string for storing rdb file
        """
        return pulumi.get(self, "rdb_storage_connection_string")

    @rdb_storage_connection_string.setter
    def rdb_storage_connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rdb_storage_connection_string", value)

    @property
    @pulumi.getter(name="storageSubscriptionId")
    def storage_subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        SubscriptionId of the storage account for persistence (aof/rdb) using ManagedIdentity.
        """
        return pulumi.get(self, "storage_subscription_id")

    @storage_subscription_id.setter
    def storage_subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_subscription_id", value)


@pulumi.input_type
class ScheduleEntryArgs:
    def __init__(__self__, *,
                 day_of_week: pulumi.Input['DayOfWeek'],
                 start_hour_utc: pulumi.Input[int],
                 maintenance_window: Optional[pulumi.Input[str]] = None):
        """
        Patch schedule entry for a Premium Redis Cache.
        :param pulumi.Input['DayOfWeek'] day_of_week: Day of the week when a cache can be patched.
        :param pulumi.Input[int] start_hour_utc: Start hour after which cache patching can start.
        :param pulumi.Input[str] maintenance_window: ISO8601 timespan specifying how much time cache patching can take. 
        """
        pulumi.set(__self__, "day_of_week", day_of_week)
        pulumi.set(__self__, "start_hour_utc", start_hour_utc)
        if maintenance_window is not None:
            pulumi.set(__self__, "maintenance_window", maintenance_window)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> pulumi.Input['DayOfWeek']:
        """
        Day of the week when a cache can be patched.
        """
        return pulumi.get(self, "day_of_week")

    @day_of_week.setter
    def day_of_week(self, value: pulumi.Input['DayOfWeek']):
        pulumi.set(self, "day_of_week", value)

    @property
    @pulumi.getter(name="startHourUtc")
    def start_hour_utc(self) -> pulumi.Input[int]:
        """
        Start hour after which cache patching can start.
        """
        return pulumi.get(self, "start_hour_utc")

    @start_hour_utc.setter
    def start_hour_utc(self, value: pulumi.Input[int]):
        pulumi.set(self, "start_hour_utc", value)

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input[str]]:
        """
        ISO8601 timespan specifying how much time cache patching can take. 
        """
        return pulumi.get(self, "maintenance_window")

    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maintenance_window", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 capacity: pulumi.Input[int],
                 family: pulumi.Input[Union[str, 'SkuFamily']],
                 name: pulumi.Input[Union[str, 'SkuName']]):
        """
        SKU parameters supplied to the create Redis operation.
        :param pulumi.Input[int] capacity: The size of the Redis cache to deploy. Valid values: for C (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium) family (1, 2, 3, 4).
        :param pulumi.Input[Union[str, 'SkuFamily']] family: The SKU family to use. Valid values: (C, P). (C = Basic/Standard, P = Premium).
        :param pulumi.Input[Union[str, 'SkuName']] name: The type of Redis cache to deploy. Valid values: (Basic, Standard, Premium)
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Input[int]:
        """
        The size of the Redis cache to deploy. Valid values: for C (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium) family (1, 2, 3, 4).
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: pulumi.Input[int]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def family(self) -> pulumi.Input[Union[str, 'SkuFamily']]:
        """
        The SKU family to use. Valid values: (C, P). (C = Basic/Standard, P = Premium).
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: pulumi.Input[Union[str, 'SkuFamily']]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'SkuName']]:
        """
        The type of Redis cache to deploy. Valid values: (Basic, Standard, Premium)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'SkuName']]):
        pulumi.set(self, "name", value)


