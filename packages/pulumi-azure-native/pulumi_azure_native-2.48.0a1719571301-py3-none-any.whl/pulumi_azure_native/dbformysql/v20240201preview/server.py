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
from ._inputs import *

__all__ = ['ServerArgs', 'Server']

@pulumi.input_type
class ServerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup: Optional[pulumi.Input['BackupArgs']] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 data_encryption: Optional[pulumi.Input['DataEncryptionArgs']] = None,
                 high_availability: Optional[pulumi.Input['HighAvailabilityArgs']] = None,
                 identity: Optional[pulumi.Input['MySQLServerIdentityArgs']] = None,
                 import_source_properties: Optional[pulumi.Input['ImportSourcePropertiesArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input['MaintenanceWindowArgs']] = None,
                 network: Optional[pulumi.Input['NetworkArgs']] = None,
                 replication_role: Optional[pulumi.Input[Union[str, 'ReplicationRole']]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['MySQLServerSkuArgs']] = None,
                 source_server_resource_id: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input['StorageArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None):
        """
        The set of arguments for constructing a Server resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] administrator_login: The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        :param pulumi.Input[str] administrator_login_password: The password of the administrator login (required for server creation).
        :param pulumi.Input[str] availability_zone: availability Zone information of the server.
        :param pulumi.Input['BackupArgs'] backup: Backup related properties of a server.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: The mode to create a new MySQL server.
        :param pulumi.Input['DataEncryptionArgs'] data_encryption: The Data Encryption for CMK.
        :param pulumi.Input['HighAvailabilityArgs'] high_availability: High availability related properties of a server.
        :param pulumi.Input['MySQLServerIdentityArgs'] identity: The cmk identity for the server.
        :param pulumi.Input['ImportSourcePropertiesArgs'] import_source_properties: Source properties for import from storage.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['MaintenanceWindowArgs'] maintenance_window: Maintenance window of a server.
        :param pulumi.Input['NetworkArgs'] network: Network related properties of a server.
        :param pulumi.Input[Union[str, 'ReplicationRole']] replication_role: The replication role.
        :param pulumi.Input[str] restore_point_in_time: Restore point creation time (ISO8601 format), specifying the time to restore from.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input['MySQLServerSkuArgs'] sku: The SKU (pricing tier) of the server.
        :param pulumi.Input[str] source_server_resource_id: The source MySQL server id.
        :param pulumi.Input['StorageArgs'] storage: Storage related properties of a server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'ServerVersion']] version: Server version.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if administrator_login is not None:
            pulumi.set(__self__, "administrator_login", administrator_login)
        if administrator_login_password is not None:
            pulumi.set(__self__, "administrator_login_password", administrator_login_password)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if backup is not None:
            pulumi.set(__self__, "backup", backup)
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if data_encryption is not None:
            pulumi.set(__self__, "data_encryption", data_encryption)
        if high_availability is not None:
            pulumi.set(__self__, "high_availability", high_availability)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if import_source_properties is not None:
            pulumi.set(__self__, "import_source_properties", import_source_properties)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if maintenance_window is not None:
            pulumi.set(__self__, "maintenance_window", maintenance_window)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if replication_role is not None:
            pulumi.set(__self__, "replication_role", replication_role)
        if restore_point_in_time is not None:
            pulumi.set(__self__, "restore_point_in_time", restore_point_in_time)
        if server_name is not None:
            pulumi.set(__self__, "server_name", server_name)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if source_server_resource_id is not None:
            pulumi.set(__self__, "source_server_resource_id", source_server_resource_id)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[pulumi.Input[str]]:
        """
        The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @administrator_login.setter
    def administrator_login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login", value)

    @property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the administrator login (required for server creation).
        """
        return pulumi.get(self, "administrator_login_password")

    @administrator_login_password.setter
    def administrator_login_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_login_password", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        availability Zone information of the server.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter
    def backup(self) -> Optional[pulumi.Input['BackupArgs']]:
        """
        Backup related properties of a server.
        """
        return pulumi.get(self, "backup")

    @backup.setter
    def backup(self, value: Optional[pulumi.Input['BackupArgs']]):
        pulumi.set(self, "backup", value)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[str, 'CreateMode']]]:
        """
        The mode to create a new MySQL server.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[str, 'CreateMode']]]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="dataEncryption")
    def data_encryption(self) -> Optional[pulumi.Input['DataEncryptionArgs']]:
        """
        The Data Encryption for CMK.
        """
        return pulumi.get(self, "data_encryption")

    @data_encryption.setter
    def data_encryption(self, value: Optional[pulumi.Input['DataEncryptionArgs']]):
        pulumi.set(self, "data_encryption", value)

    @property
    @pulumi.getter(name="highAvailability")
    def high_availability(self) -> Optional[pulumi.Input['HighAvailabilityArgs']]:
        """
        High availability related properties of a server.
        """
        return pulumi.get(self, "high_availability")

    @high_availability.setter
    def high_availability(self, value: Optional[pulumi.Input['HighAvailabilityArgs']]):
        pulumi.set(self, "high_availability", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['MySQLServerIdentityArgs']]:
        """
        The cmk identity for the server.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['MySQLServerIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="importSourceProperties")
    def import_source_properties(self) -> Optional[pulumi.Input['ImportSourcePropertiesArgs']]:
        """
        Source properties for import from storage.
        """
        return pulumi.get(self, "import_source_properties")

    @import_source_properties.setter
    def import_source_properties(self, value: Optional[pulumi.Input['ImportSourcePropertiesArgs']]):
        pulumi.set(self, "import_source_properties", value)

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
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[pulumi.Input['MaintenanceWindowArgs']]:
        """
        Maintenance window of a server.
        """
        return pulumi.get(self, "maintenance_window")

    @maintenance_window.setter
    def maintenance_window(self, value: Optional[pulumi.Input['MaintenanceWindowArgs']]):
        pulumi.set(self, "maintenance_window", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input['NetworkArgs']]:
        """
        Network related properties of a server.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input['NetworkArgs']]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> Optional[pulumi.Input[Union[str, 'ReplicationRole']]]:
        """
        The replication role.
        """
        return pulumi.get(self, "replication_role")

    @replication_role.setter
    def replication_role(self, value: Optional[pulumi.Input[Union[str, 'ReplicationRole']]]):
        pulumi.set(self, "replication_role", value)

    @property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> Optional[pulumi.Input[str]]:
        """
        Restore point creation time (ISO8601 format), specifying the time to restore from.
        """
        return pulumi.get(self, "restore_point_in_time")

    @restore_point_in_time.setter
    def restore_point_in_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_point_in_time", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['MySQLServerSkuArgs']]:
        """
        The SKU (pricing tier) of the server.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['MySQLServerSkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="sourceServerResourceId")
    def source_server_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The source MySQL server id.
        """
        return pulumi.get(self, "source_server_resource_id")

    @source_server_resource_id.setter
    def source_server_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_server_resource_id", value)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input['StorageArgs']]:
        """
        Storage related properties of a server.
        """
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input['StorageArgs']]):
        pulumi.set(self, "storage", value)

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
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[str, 'ServerVersion']]]:
        """
        Server version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[str, 'ServerVersion']]]):
        pulumi.set(self, "version", value)


class Server(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup: Optional[pulumi.Input[pulumi.InputType['BackupArgs']]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 data_encryption: Optional[pulumi.Input[pulumi.InputType['DataEncryptionArgs']]] = None,
                 high_availability: Optional[pulumi.Input[pulumi.InputType['HighAvailabilityArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['MySQLServerIdentityArgs']]] = None,
                 import_source_properties: Optional[pulumi.Input[pulumi.InputType['ImportSourcePropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']]] = None,
                 network: Optional[pulumi.Input[pulumi.InputType['NetworkArgs']]] = None,
                 replication_role: Optional[pulumi.Input[Union[str, 'ReplicationRole']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['MySQLServerSkuArgs']]] = None,
                 source_server_resource_id: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input[pulumi.InputType['StorageArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None,
                 __props__=None):
        """
        Represents a server.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administrator_login: The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        :param pulumi.Input[str] administrator_login_password: The password of the administrator login (required for server creation).
        :param pulumi.Input[str] availability_zone: availability Zone information of the server.
        :param pulumi.Input[pulumi.InputType['BackupArgs']] backup: Backup related properties of a server.
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: The mode to create a new MySQL server.
        :param pulumi.Input[pulumi.InputType['DataEncryptionArgs']] data_encryption: The Data Encryption for CMK.
        :param pulumi.Input[pulumi.InputType['HighAvailabilityArgs']] high_availability: High availability related properties of a server.
        :param pulumi.Input[pulumi.InputType['MySQLServerIdentityArgs']] identity: The cmk identity for the server.
        :param pulumi.Input[pulumi.InputType['ImportSourcePropertiesArgs']] import_source_properties: Source properties for import from storage.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']] maintenance_window: Maintenance window of a server.
        :param pulumi.Input[pulumi.InputType['NetworkArgs']] network: Network related properties of a server.
        :param pulumi.Input[Union[str, 'ReplicationRole']] replication_role: The replication role.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] restore_point_in_time: Restore point creation time (ISO8601 format), specifying the time to restore from.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[pulumi.InputType['MySQLServerSkuArgs']] sku: The SKU (pricing tier) of the server.
        :param pulumi.Input[str] source_server_resource_id: The source MySQL server id.
        :param pulumi.Input[pulumi.InputType['StorageArgs']] storage: Storage related properties of a server.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'ServerVersion']] version: Server version.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a server.

        :param str resource_name: The name of the resource.
        :param ServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_login: Optional[pulumi.Input[str]] = None,
                 administrator_login_password: Optional[pulumi.Input[str]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 backup: Optional[pulumi.Input[pulumi.InputType['BackupArgs']]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 data_encryption: Optional[pulumi.Input[pulumi.InputType['DataEncryptionArgs']]] = None,
                 high_availability: Optional[pulumi.Input[pulumi.InputType['HighAvailabilityArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['MySQLServerIdentityArgs']]] = None,
                 import_source_properties: Optional[pulumi.Input[pulumi.InputType['ImportSourcePropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maintenance_window: Optional[pulumi.Input[pulumi.InputType['MaintenanceWindowArgs']]] = None,
                 network: Optional[pulumi.Input[pulumi.InputType['NetworkArgs']]] = None,
                 replication_role: Optional[pulumi.Input[Union[str, 'ReplicationRole']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['MySQLServerSkuArgs']]] = None,
                 source_server_resource_id: Optional[pulumi.Input[str]] = None,
                 storage: Optional[pulumi.Input[pulumi.InputType['StorageArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerArgs.__new__(ServerArgs)

            __props__.__dict__["administrator_login"] = administrator_login
            __props__.__dict__["administrator_login_password"] = administrator_login_password
            __props__.__dict__["availability_zone"] = availability_zone
            __props__.__dict__["backup"] = backup
            __props__.__dict__["create_mode"] = create_mode
            __props__.__dict__["data_encryption"] = data_encryption
            __props__.__dict__["high_availability"] = high_availability
            __props__.__dict__["identity"] = identity
            __props__.__dict__["import_source_properties"] = import_source_properties
            __props__.__dict__["location"] = location
            __props__.__dict__["maintenance_window"] = maintenance_window
            __props__.__dict__["network"] = network
            __props__.__dict__["replication_role"] = replication_role
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["restore_point_in_time"] = restore_point_in_time
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["source_server_resource_id"] = source_server_resource_id
            __props__.__dict__["storage"] = storage
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version"] = version
            __props__.__dict__["fully_qualified_domain_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["replica_capacity"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dbformysql:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20200701preview:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20200701privatepreview:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20210501:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20210501preview:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20211201preview:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20220101:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20220930preview:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20230601preview:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20230630:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20231001preview:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20231201preview:Server"), pulumi.Alias(type_="azure-native:dbformysql/v20231230:Server")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Server, __self__).__init__(
            'azure-native:dbformysql/v20240201preview:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerArgs.__new__(ServerArgs)

        __props__.__dict__["administrator_login"] = None
        __props__.__dict__["availability_zone"] = None
        __props__.__dict__["backup"] = None
        __props__.__dict__["data_encryption"] = None
        __props__.__dict__["fully_qualified_domain_name"] = None
        __props__.__dict__["high_availability"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["import_source_properties"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["maintenance_window"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["replica_capacity"] = None
        __props__.__dict__["replication_role"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["source_server_resource_id"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["storage"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Output[Optional[str]]:
        """
        The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[Optional[str]]:
        """
        availability Zone information of the server.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def backup(self) -> pulumi.Output[Optional['outputs.BackupResponse']]:
        """
        Backup related properties of a server.
        """
        return pulumi.get(self, "backup")

    @property
    @pulumi.getter(name="dataEncryption")
    def data_encryption(self) -> pulumi.Output[Optional['outputs.DataEncryptionResponse']]:
        """
        The Data Encryption for CMK.
        """
        return pulumi.get(self, "data_encryption")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> pulumi.Output[str]:
        """
        The fully qualified domain name of a server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter(name="highAvailability")
    def high_availability(self) -> pulumi.Output[Optional['outputs.HighAvailabilityResponse']]:
        """
        High availability related properties of a server.
        """
        return pulumi.get(self, "high_availability")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.MySQLServerIdentityResponse']]:
        """
        The cmk identity for the server.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="importSourceProperties")
    def import_source_properties(self) -> pulumi.Output[Optional['outputs.ImportSourcePropertiesResponse']]:
        """
        Source properties for import from storage.
        """
        return pulumi.get(self, "import_source_properties")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> pulumi.Output[Optional['outputs.MaintenanceWindowResponse']]:
        """
        Maintenance window of a server.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[Optional['outputs.NetworkResponse']]:
        """
        Network related properties of a server.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        PrivateEndpointConnections related properties of a server.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="replicaCapacity")
    def replica_capacity(self) -> pulumi.Output[int]:
        """
        The maximum number of replicas that a primary server can have.
        """
        return pulumi.get(self, "replica_capacity")

    @property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> pulumi.Output[Optional[str]]:
        """
        The replication role.
        """
        return pulumi.get(self, "replication_role")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.MySQLServerSkuResponse']]:
        """
        The SKU (pricing tier) of the server.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sourceServerResourceId")
    def source_server_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The source MySQL server id.
        """
        return pulumi.get(self, "source_server_resource_id")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of a server.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def storage(self) -> pulumi.Output[Optional['outputs.StorageResponse']]:
        """
        Storage related properties of a server.
        """
        return pulumi.get(self, "storage")

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
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Server version.
        """
        return pulumi.get(self, "version")

