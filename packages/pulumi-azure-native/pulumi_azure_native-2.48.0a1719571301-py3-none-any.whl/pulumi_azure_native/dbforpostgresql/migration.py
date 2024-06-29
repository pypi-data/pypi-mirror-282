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
from ._inputs import *

__all__ = ['MigrationArgs', 'Migration']

@pulumi.input_type
class MigrationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 target_db_server_name: pulumi.Input[str],
                 cancel: Optional[pulumi.Input[Union[str, 'CancelEnum']]] = None,
                 dbs_to_cancel_migration_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dbs_to_migrate: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dbs_to_trigger_cutover_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migration_mode: Optional[pulumi.Input[Union[str, 'MigrationMode']]] = None,
                 migration_name: Optional[pulumi.Input[str]] = None,
                 migration_window_end_time_in_utc: Optional[pulumi.Input[str]] = None,
                 migration_window_start_time_in_utc: Optional[pulumi.Input[str]] = None,
                 overwrite_dbs_in_target: Optional[pulumi.Input[Union[str, 'OverwriteDbsInTargetEnum']]] = None,
                 secret_parameters: Optional[pulumi.Input['MigrationSecretParametersArgs']] = None,
                 setup_logical_replication_on_source_db_if_needed: Optional[pulumi.Input[Union[str, 'LogicalReplicationOnSourceDbEnum']]] = None,
                 source_db_server_fully_qualified_domain_name: Optional[pulumi.Input[str]] = None,
                 source_db_server_resource_id: Optional[pulumi.Input[str]] = None,
                 start_data_migration: Optional[pulumi.Input[Union[str, 'StartDataMigrationEnum']]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_db_server_fully_qualified_domain_name: Optional[pulumi.Input[str]] = None,
                 trigger_cutover: Optional[pulumi.Input[Union[str, 'TriggerCutoverEnum']]] = None):
        """
        The set of arguments for constructing a Migration resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the target database server.
        :param pulumi.Input[str] target_db_server_name: The name of the target database server.
        :param pulumi.Input[Union[str, 'CancelEnum']] cancel: To trigger cancel for entire migration we need to send this flag as True
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dbs_to_cancel_migration_on: When you want to trigger cancel for specific databases send cancel flag as True and database names in this array
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dbs_to_migrate: Number of databases to migrate
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dbs_to_trigger_cutover_on: When you want to trigger cutover for specific databases send triggerCutover flag as True and database names in this array
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'MigrationMode']] migration_mode: There are two types of migration modes Online and Offline
        :param pulumi.Input[str] migration_name: The name of the migration.
        :param pulumi.Input[str] migration_window_end_time_in_utc: End time in UTC for migration window
        :param pulumi.Input[str] migration_window_start_time_in_utc: Start time in UTC for migration window
        :param pulumi.Input[Union[str, 'OverwriteDbsInTargetEnum']] overwrite_dbs_in_target: Indicates whether the databases on the target server can be overwritten, if already present. If set to False, the migration workflow will wait for a confirmation, if it detects that the database already exists.
        :param pulumi.Input['MigrationSecretParametersArgs'] secret_parameters: Migration secret parameters
        :param pulumi.Input[Union[str, 'LogicalReplicationOnSourceDbEnum']] setup_logical_replication_on_source_db_if_needed: Indicates whether to setup LogicalReplicationOnSourceDb, if needed
        :param pulumi.Input[str] source_db_server_fully_qualified_domain_name: Source server fully qualified domain name or ip. It is a optional value, if customer provide it, dms will always use it for connection
        :param pulumi.Input[str] source_db_server_resource_id: ResourceId of the source database server
        :param pulumi.Input[Union[str, 'StartDataMigrationEnum']] start_data_migration: Indicates whether the data migration should start right away
        :param pulumi.Input[str] subscription_id: The subscription ID of the target database server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] target_db_server_fully_qualified_domain_name: Target server fully qualified domain name or ip. It is a optional value, if customer provide it, dms will always use it for connection
        :param pulumi.Input[Union[str, 'TriggerCutoverEnum']] trigger_cutover: To trigger cutover for entire migration we need to send this flag as True
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "target_db_server_name", target_db_server_name)
        if cancel is not None:
            pulumi.set(__self__, "cancel", cancel)
        if dbs_to_cancel_migration_on is not None:
            pulumi.set(__self__, "dbs_to_cancel_migration_on", dbs_to_cancel_migration_on)
        if dbs_to_migrate is not None:
            pulumi.set(__self__, "dbs_to_migrate", dbs_to_migrate)
        if dbs_to_trigger_cutover_on is not None:
            pulumi.set(__self__, "dbs_to_trigger_cutover_on", dbs_to_trigger_cutover_on)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if migration_mode is not None:
            pulumi.set(__self__, "migration_mode", migration_mode)
        if migration_name is not None:
            pulumi.set(__self__, "migration_name", migration_name)
        if migration_window_end_time_in_utc is not None:
            pulumi.set(__self__, "migration_window_end_time_in_utc", migration_window_end_time_in_utc)
        if migration_window_start_time_in_utc is not None:
            pulumi.set(__self__, "migration_window_start_time_in_utc", migration_window_start_time_in_utc)
        if overwrite_dbs_in_target is not None:
            pulumi.set(__self__, "overwrite_dbs_in_target", overwrite_dbs_in_target)
        if secret_parameters is not None:
            pulumi.set(__self__, "secret_parameters", secret_parameters)
        if setup_logical_replication_on_source_db_if_needed is not None:
            pulumi.set(__self__, "setup_logical_replication_on_source_db_if_needed", setup_logical_replication_on_source_db_if_needed)
        if source_db_server_fully_qualified_domain_name is not None:
            pulumi.set(__self__, "source_db_server_fully_qualified_domain_name", source_db_server_fully_qualified_domain_name)
        if source_db_server_resource_id is not None:
            pulumi.set(__self__, "source_db_server_resource_id", source_db_server_resource_id)
        if start_data_migration is not None:
            pulumi.set(__self__, "start_data_migration", start_data_migration)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_db_server_fully_qualified_domain_name is not None:
            pulumi.set(__self__, "target_db_server_fully_qualified_domain_name", target_db_server_fully_qualified_domain_name)
        if trigger_cutover is not None:
            pulumi.set(__self__, "trigger_cutover", trigger_cutover)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the target database server.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="targetDbServerName")
    def target_db_server_name(self) -> pulumi.Input[str]:
        """
        The name of the target database server.
        """
        return pulumi.get(self, "target_db_server_name")

    @target_db_server_name.setter
    def target_db_server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_db_server_name", value)

    @property
    @pulumi.getter
    def cancel(self) -> Optional[pulumi.Input[Union[str, 'CancelEnum']]]:
        """
        To trigger cancel for entire migration we need to send this flag as True
        """
        return pulumi.get(self, "cancel")

    @cancel.setter
    def cancel(self, value: Optional[pulumi.Input[Union[str, 'CancelEnum']]]):
        pulumi.set(self, "cancel", value)

    @property
    @pulumi.getter(name="dbsToCancelMigrationOn")
    def dbs_to_cancel_migration_on(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        When you want to trigger cancel for specific databases send cancel flag as True and database names in this array
        """
        return pulumi.get(self, "dbs_to_cancel_migration_on")

    @dbs_to_cancel_migration_on.setter
    def dbs_to_cancel_migration_on(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dbs_to_cancel_migration_on", value)

    @property
    @pulumi.getter(name="dbsToMigrate")
    def dbs_to_migrate(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Number of databases to migrate
        """
        return pulumi.get(self, "dbs_to_migrate")

    @dbs_to_migrate.setter
    def dbs_to_migrate(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dbs_to_migrate", value)

    @property
    @pulumi.getter(name="dbsToTriggerCutoverOn")
    def dbs_to_trigger_cutover_on(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        When you want to trigger cutover for specific databases send triggerCutover flag as True and database names in this array
        """
        return pulumi.get(self, "dbs_to_trigger_cutover_on")

    @dbs_to_trigger_cutover_on.setter
    def dbs_to_trigger_cutover_on(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dbs_to_trigger_cutover_on", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="migrationMode")
    def migration_mode(self) -> Optional[pulumi.Input[Union[str, 'MigrationMode']]]:
        """
        There are two types of migration modes Online and Offline
        """
        return pulumi.get(self, "migration_mode")

    @migration_mode.setter
    def migration_mode(self, value: Optional[pulumi.Input[Union[str, 'MigrationMode']]]):
        pulumi.set(self, "migration_mode", value)

    @property
    @pulumi.getter(name="migrationName")
    def migration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the migration.
        """
        return pulumi.get(self, "migration_name")

    @migration_name.setter
    def migration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "migration_name", value)

    @property
    @pulumi.getter(name="migrationWindowEndTimeInUtc")
    def migration_window_end_time_in_utc(self) -> Optional[pulumi.Input[str]]:
        """
        End time in UTC for migration window
        """
        return pulumi.get(self, "migration_window_end_time_in_utc")

    @migration_window_end_time_in_utc.setter
    def migration_window_end_time_in_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "migration_window_end_time_in_utc", value)

    @property
    @pulumi.getter(name="migrationWindowStartTimeInUtc")
    def migration_window_start_time_in_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Start time in UTC for migration window
        """
        return pulumi.get(self, "migration_window_start_time_in_utc")

    @migration_window_start_time_in_utc.setter
    def migration_window_start_time_in_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "migration_window_start_time_in_utc", value)

    @property
    @pulumi.getter(name="overwriteDbsInTarget")
    def overwrite_dbs_in_target(self) -> Optional[pulumi.Input[Union[str, 'OverwriteDbsInTargetEnum']]]:
        """
        Indicates whether the databases on the target server can be overwritten, if already present. If set to False, the migration workflow will wait for a confirmation, if it detects that the database already exists.
        """
        return pulumi.get(self, "overwrite_dbs_in_target")

    @overwrite_dbs_in_target.setter
    def overwrite_dbs_in_target(self, value: Optional[pulumi.Input[Union[str, 'OverwriteDbsInTargetEnum']]]):
        pulumi.set(self, "overwrite_dbs_in_target", value)

    @property
    @pulumi.getter(name="secretParameters")
    def secret_parameters(self) -> Optional[pulumi.Input['MigrationSecretParametersArgs']]:
        """
        Migration secret parameters
        """
        return pulumi.get(self, "secret_parameters")

    @secret_parameters.setter
    def secret_parameters(self, value: Optional[pulumi.Input['MigrationSecretParametersArgs']]):
        pulumi.set(self, "secret_parameters", value)

    @property
    @pulumi.getter(name="setupLogicalReplicationOnSourceDbIfNeeded")
    def setup_logical_replication_on_source_db_if_needed(self) -> Optional[pulumi.Input[Union[str, 'LogicalReplicationOnSourceDbEnum']]]:
        """
        Indicates whether to setup LogicalReplicationOnSourceDb, if needed
        """
        return pulumi.get(self, "setup_logical_replication_on_source_db_if_needed")

    @setup_logical_replication_on_source_db_if_needed.setter
    def setup_logical_replication_on_source_db_if_needed(self, value: Optional[pulumi.Input[Union[str, 'LogicalReplicationOnSourceDbEnum']]]):
        pulumi.set(self, "setup_logical_replication_on_source_db_if_needed", value)

    @property
    @pulumi.getter(name="sourceDbServerFullyQualifiedDomainName")
    def source_db_server_fully_qualified_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Source server fully qualified domain name or ip. It is a optional value, if customer provide it, dms will always use it for connection
        """
        return pulumi.get(self, "source_db_server_fully_qualified_domain_name")

    @source_db_server_fully_qualified_domain_name.setter
    def source_db_server_fully_qualified_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_db_server_fully_qualified_domain_name", value)

    @property
    @pulumi.getter(name="sourceDbServerResourceId")
    def source_db_server_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ResourceId of the source database server
        """
        return pulumi.get(self, "source_db_server_resource_id")

    @source_db_server_resource_id.setter
    def source_db_server_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_db_server_resource_id", value)

    @property
    @pulumi.getter(name="startDataMigration")
    def start_data_migration(self) -> Optional[pulumi.Input[Union[str, 'StartDataMigrationEnum']]]:
        """
        Indicates whether the data migration should start right away
        """
        return pulumi.get(self, "start_data_migration")

    @start_data_migration.setter
    def start_data_migration(self, value: Optional[pulumi.Input[Union[str, 'StartDataMigrationEnum']]]):
        pulumi.set(self, "start_data_migration", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The subscription ID of the target database server.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetDbServerFullyQualifiedDomainName")
    def target_db_server_fully_qualified_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Target server fully qualified domain name or ip. It is a optional value, if customer provide it, dms will always use it for connection
        """
        return pulumi.get(self, "target_db_server_fully_qualified_domain_name")

    @target_db_server_fully_qualified_domain_name.setter
    def target_db_server_fully_qualified_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_db_server_fully_qualified_domain_name", value)

    @property
    @pulumi.getter(name="triggerCutover")
    def trigger_cutover(self) -> Optional[pulumi.Input[Union[str, 'TriggerCutoverEnum']]]:
        """
        To trigger cutover for entire migration we need to send this flag as True
        """
        return pulumi.get(self, "trigger_cutover")

    @trigger_cutover.setter
    def trigger_cutover(self, value: Optional[pulumi.Input[Union[str, 'TriggerCutoverEnum']]]):
        pulumi.set(self, "trigger_cutover", value)


class Migration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cancel: Optional[pulumi.Input[Union[str, 'CancelEnum']]] = None,
                 dbs_to_cancel_migration_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dbs_to_migrate: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dbs_to_trigger_cutover_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migration_mode: Optional[pulumi.Input[Union[str, 'MigrationMode']]] = None,
                 migration_name: Optional[pulumi.Input[str]] = None,
                 migration_window_end_time_in_utc: Optional[pulumi.Input[str]] = None,
                 migration_window_start_time_in_utc: Optional[pulumi.Input[str]] = None,
                 overwrite_dbs_in_target: Optional[pulumi.Input[Union[str, 'OverwriteDbsInTargetEnum']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secret_parameters: Optional[pulumi.Input[pulumi.InputType['MigrationSecretParametersArgs']]] = None,
                 setup_logical_replication_on_source_db_if_needed: Optional[pulumi.Input[Union[str, 'LogicalReplicationOnSourceDbEnum']]] = None,
                 source_db_server_fully_qualified_domain_name: Optional[pulumi.Input[str]] = None,
                 source_db_server_resource_id: Optional[pulumi.Input[str]] = None,
                 start_data_migration: Optional[pulumi.Input[Union[str, 'StartDataMigrationEnum']]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_db_server_fully_qualified_domain_name: Optional[pulumi.Input[str]] = None,
                 target_db_server_name: Optional[pulumi.Input[str]] = None,
                 trigger_cutover: Optional[pulumi.Input[Union[str, 'TriggerCutoverEnum']]] = None,
                 __props__=None):
        """
        Represents a migration resource.
        Azure REST API version: 2023-03-01-preview.

        Other available API versions: 2021-06-15-privatepreview, 2022-05-01-preview, 2023-06-01-preview, 2023-12-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'CancelEnum']] cancel: To trigger cancel for entire migration we need to send this flag as True
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dbs_to_cancel_migration_on: When you want to trigger cancel for specific databases send cancel flag as True and database names in this array
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dbs_to_migrate: Number of databases to migrate
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dbs_to_trigger_cutover_on: When you want to trigger cutover for specific databases send triggerCutover flag as True and database names in this array
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union[str, 'MigrationMode']] migration_mode: There are two types of migration modes Online and Offline
        :param pulumi.Input[str] migration_name: The name of the migration.
        :param pulumi.Input[str] migration_window_end_time_in_utc: End time in UTC for migration window
        :param pulumi.Input[str] migration_window_start_time_in_utc: Start time in UTC for migration window
        :param pulumi.Input[Union[str, 'OverwriteDbsInTargetEnum']] overwrite_dbs_in_target: Indicates whether the databases on the target server can be overwritten, if already present. If set to False, the migration workflow will wait for a confirmation, if it detects that the database already exists.
        :param pulumi.Input[str] resource_group_name: The resource group name of the target database server.
        :param pulumi.Input[pulumi.InputType['MigrationSecretParametersArgs']] secret_parameters: Migration secret parameters
        :param pulumi.Input[Union[str, 'LogicalReplicationOnSourceDbEnum']] setup_logical_replication_on_source_db_if_needed: Indicates whether to setup LogicalReplicationOnSourceDb, if needed
        :param pulumi.Input[str] source_db_server_fully_qualified_domain_name: Source server fully qualified domain name or ip. It is a optional value, if customer provide it, dms will always use it for connection
        :param pulumi.Input[str] source_db_server_resource_id: ResourceId of the source database server
        :param pulumi.Input[Union[str, 'StartDataMigrationEnum']] start_data_migration: Indicates whether the data migration should start right away
        :param pulumi.Input[str] subscription_id: The subscription ID of the target database server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] target_db_server_fully_qualified_domain_name: Target server fully qualified domain name or ip. It is a optional value, if customer provide it, dms will always use it for connection
        :param pulumi.Input[str] target_db_server_name: The name of the target database server.
        :param pulumi.Input[Union[str, 'TriggerCutoverEnum']] trigger_cutover: To trigger cutover for entire migration we need to send this flag as True
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MigrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a migration resource.
        Azure REST API version: 2023-03-01-preview.

        Other available API versions: 2021-06-15-privatepreview, 2022-05-01-preview, 2023-06-01-preview, 2023-12-01-preview.

        :param str resource_name: The name of the resource.
        :param MigrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MigrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cancel: Optional[pulumi.Input[Union[str, 'CancelEnum']]] = None,
                 dbs_to_cancel_migration_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dbs_to_migrate: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dbs_to_trigger_cutover_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migration_mode: Optional[pulumi.Input[Union[str, 'MigrationMode']]] = None,
                 migration_name: Optional[pulumi.Input[str]] = None,
                 migration_window_end_time_in_utc: Optional[pulumi.Input[str]] = None,
                 migration_window_start_time_in_utc: Optional[pulumi.Input[str]] = None,
                 overwrite_dbs_in_target: Optional[pulumi.Input[Union[str, 'OverwriteDbsInTargetEnum']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secret_parameters: Optional[pulumi.Input[pulumi.InputType['MigrationSecretParametersArgs']]] = None,
                 setup_logical_replication_on_source_db_if_needed: Optional[pulumi.Input[Union[str, 'LogicalReplicationOnSourceDbEnum']]] = None,
                 source_db_server_fully_qualified_domain_name: Optional[pulumi.Input[str]] = None,
                 source_db_server_resource_id: Optional[pulumi.Input[str]] = None,
                 start_data_migration: Optional[pulumi.Input[Union[str, 'StartDataMigrationEnum']]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_db_server_fully_qualified_domain_name: Optional[pulumi.Input[str]] = None,
                 target_db_server_name: Optional[pulumi.Input[str]] = None,
                 trigger_cutover: Optional[pulumi.Input[Union[str, 'TriggerCutoverEnum']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MigrationArgs.__new__(MigrationArgs)

            __props__.__dict__["cancel"] = cancel
            __props__.__dict__["dbs_to_cancel_migration_on"] = dbs_to_cancel_migration_on
            __props__.__dict__["dbs_to_migrate"] = dbs_to_migrate
            __props__.__dict__["dbs_to_trigger_cutover_on"] = dbs_to_trigger_cutover_on
            __props__.__dict__["location"] = location
            __props__.__dict__["migration_mode"] = migration_mode
            __props__.__dict__["migration_name"] = migration_name
            __props__.__dict__["migration_window_end_time_in_utc"] = migration_window_end_time_in_utc
            __props__.__dict__["migration_window_start_time_in_utc"] = migration_window_start_time_in_utc
            __props__.__dict__["overwrite_dbs_in_target"] = overwrite_dbs_in_target
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["secret_parameters"] = secret_parameters
            __props__.__dict__["setup_logical_replication_on_source_db_if_needed"] = setup_logical_replication_on_source_db_if_needed
            __props__.__dict__["source_db_server_fully_qualified_domain_name"] = source_db_server_fully_qualified_domain_name
            __props__.__dict__["source_db_server_resource_id"] = source_db_server_resource_id
            __props__.__dict__["start_data_migration"] = start_data_migration
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_db_server_fully_qualified_domain_name"] = target_db_server_fully_qualified_domain_name
            if target_db_server_name is None and not opts.urn:
                raise TypeError("Missing required property 'target_db_server_name'")
            __props__.__dict__["target_db_server_name"] = target_db_server_name
            __props__.__dict__["trigger_cutover"] = trigger_cutover
            __props__.__dict__["current_status"] = None
            __props__.__dict__["migration_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["source_db_server_metadata"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["target_db_server_metadata"] = None
            __props__.__dict__["target_db_server_resource_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dbforpostgresql/v20210615privatepreview:Migration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20220501preview:Migration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20230301preview:Migration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20230601preview:Migration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20231201preview:Migration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Migration, __self__).__init__(
            'azure-native:dbforpostgresql:Migration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Migration':
        """
        Get an existing Migration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MigrationArgs.__new__(MigrationArgs)

        __props__.__dict__["cancel"] = None
        __props__.__dict__["current_status"] = None
        __props__.__dict__["dbs_to_cancel_migration_on"] = None
        __props__.__dict__["dbs_to_migrate"] = None
        __props__.__dict__["dbs_to_trigger_cutover_on"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["migration_id"] = None
        __props__.__dict__["migration_mode"] = None
        __props__.__dict__["migration_window_end_time_in_utc"] = None
        __props__.__dict__["migration_window_start_time_in_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["overwrite_dbs_in_target"] = None
        __props__.__dict__["setup_logical_replication_on_source_db_if_needed"] = None
        __props__.__dict__["source_db_server_fully_qualified_domain_name"] = None
        __props__.__dict__["source_db_server_metadata"] = None
        __props__.__dict__["source_db_server_resource_id"] = None
        __props__.__dict__["start_data_migration"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_db_server_fully_qualified_domain_name"] = None
        __props__.__dict__["target_db_server_metadata"] = None
        __props__.__dict__["target_db_server_resource_id"] = None
        __props__.__dict__["trigger_cutover"] = None
        __props__.__dict__["type"] = None
        return Migration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cancel(self) -> pulumi.Output[Optional[str]]:
        """
        To trigger cancel for entire migration we need to send this flag as True
        """
        return pulumi.get(self, "cancel")

    @property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> pulumi.Output['outputs.MigrationStatusResponse']:
        """
        Current status of migration
        """
        return pulumi.get(self, "current_status")

    @property
    @pulumi.getter(name="dbsToCancelMigrationOn")
    def dbs_to_cancel_migration_on(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        When you want to trigger cancel for specific databases send cancel flag as True and database names in this array
        """
        return pulumi.get(self, "dbs_to_cancel_migration_on")

    @property
    @pulumi.getter(name="dbsToMigrate")
    def dbs_to_migrate(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Number of databases to migrate
        """
        return pulumi.get(self, "dbs_to_migrate")

    @property
    @pulumi.getter(name="dbsToTriggerCutoverOn")
    def dbs_to_trigger_cutover_on(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        When you want to trigger cutover for specific databases send triggerCutover flag as True and database names in this array
        """
        return pulumi.get(self, "dbs_to_trigger_cutover_on")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> pulumi.Output[str]:
        """
        ID for migration, a GUID.
        """
        return pulumi.get(self, "migration_id")

    @property
    @pulumi.getter(name="migrationMode")
    def migration_mode(self) -> pulumi.Output[Optional[str]]:
        """
        There are two types of migration modes Online and Offline
        """
        return pulumi.get(self, "migration_mode")

    @property
    @pulumi.getter(name="migrationWindowEndTimeInUtc")
    def migration_window_end_time_in_utc(self) -> pulumi.Output[Optional[str]]:
        """
        End time in UTC for migration window
        """
        return pulumi.get(self, "migration_window_end_time_in_utc")

    @property
    @pulumi.getter(name="migrationWindowStartTimeInUtc")
    def migration_window_start_time_in_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Start time in UTC for migration window
        """
        return pulumi.get(self, "migration_window_start_time_in_utc")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="overwriteDbsInTarget")
    def overwrite_dbs_in_target(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether the databases on the target server can be overwritten, if already present. If set to False, the migration workflow will wait for a confirmation, if it detects that the database already exists.
        """
        return pulumi.get(self, "overwrite_dbs_in_target")

    @property
    @pulumi.getter(name="setupLogicalReplicationOnSourceDbIfNeeded")
    def setup_logical_replication_on_source_db_if_needed(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether to setup LogicalReplicationOnSourceDb, if needed
        """
        return pulumi.get(self, "setup_logical_replication_on_source_db_if_needed")

    @property
    @pulumi.getter(name="sourceDbServerFullyQualifiedDomainName")
    def source_db_server_fully_qualified_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        Source server fully qualified domain name or ip. It is a optional value, if customer provide it, dms will always use it for connection
        """
        return pulumi.get(self, "source_db_server_fully_qualified_domain_name")

    @property
    @pulumi.getter(name="sourceDbServerMetadata")
    def source_db_server_metadata(self) -> pulumi.Output['outputs.DbServerMetadataResponse']:
        """
        Metadata of the source database server
        """
        return pulumi.get(self, "source_db_server_metadata")

    @property
    @pulumi.getter(name="sourceDbServerResourceId")
    def source_db_server_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        ResourceId of the source database server
        """
        return pulumi.get(self, "source_db_server_resource_id")

    @property
    @pulumi.getter(name="startDataMigration")
    def start_data_migration(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether the data migration should start right away
        """
        return pulumi.get(self, "start_data_migration")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetDbServerFullyQualifiedDomainName")
    def target_db_server_fully_qualified_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        Target server fully qualified domain name or ip. It is a optional value, if customer provide it, dms will always use it for connection
        """
        return pulumi.get(self, "target_db_server_fully_qualified_domain_name")

    @property
    @pulumi.getter(name="targetDbServerMetadata")
    def target_db_server_metadata(self) -> pulumi.Output['outputs.DbServerMetadataResponse']:
        """
        Metadata of the target database server
        """
        return pulumi.get(self, "target_db_server_metadata")

    @property
    @pulumi.getter(name="targetDbServerResourceId")
    def target_db_server_resource_id(self) -> pulumi.Output[str]:
        """
        ResourceId of the source database server
        """
        return pulumi.get(self, "target_db_server_resource_id")

    @property
    @pulumi.getter(name="triggerCutover")
    def trigger_cutover(self) -> pulumi.Output[Optional[str]]:
        """
        To trigger cutover for entire migration we need to send this flag as True
        """
        return pulumi.get(self, "trigger_cutover")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

