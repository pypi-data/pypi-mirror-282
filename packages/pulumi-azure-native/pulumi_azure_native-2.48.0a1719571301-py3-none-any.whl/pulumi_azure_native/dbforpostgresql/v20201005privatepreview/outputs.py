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
    'MaintenanceWindowResponse',
    'ServerGroupPropertiesResponseDelegatedSubnetArguments',
    'ServerGroupPropertiesResponsePrivateDnsZoneArguments',
    'ServerNameItemResponse',
    'ServerRoleGroupResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class MaintenanceWindowResponse(dict):
    """
    Maintenance window of a server group.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customWindow":
            suggest = "custom_window"
        elif key == "dayOfWeek":
            suggest = "day_of_week"
        elif key == "startHour":
            suggest = "start_hour"
        elif key == "startMinute":
            suggest = "start_minute"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MaintenanceWindowResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MaintenanceWindowResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MaintenanceWindowResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 custom_window: Optional[str] = None,
                 day_of_week: Optional[int] = None,
                 start_hour: Optional[int] = None,
                 start_minute: Optional[int] = None):
        """
        Maintenance window of a server group.
        :param str custom_window: indicates whether custom window is enabled or disabled
        :param int day_of_week: day of week for maintenance window
        :param int start_hour: start hour for maintenance window
        :param int start_minute: start minute for maintenance window
        """
        if custom_window is not None:
            pulumi.set(__self__, "custom_window", custom_window)
        if day_of_week is not None:
            pulumi.set(__self__, "day_of_week", day_of_week)
        if start_hour is not None:
            pulumi.set(__self__, "start_hour", start_hour)
        if start_minute is not None:
            pulumi.set(__self__, "start_minute", start_minute)

    @property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[str]:
        """
        indicates whether custom window is enabled or disabled
        """
        return pulumi.get(self, "custom_window")

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[int]:
        """
        day of week for maintenance window
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[int]:
        """
        start hour for maintenance window
        """
        return pulumi.get(self, "start_hour")

    @property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[int]:
        """
        start minute for maintenance window
        """
        return pulumi.get(self, "start_minute")


@pulumi.output_type
class ServerGroupPropertiesResponseDelegatedSubnetArguments(dict):
    """
    The delegated subnet arguments for a server group.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetArmResourceId":
            suggest = "subnet_arm_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServerGroupPropertiesResponseDelegatedSubnetArguments. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServerGroupPropertiesResponseDelegatedSubnetArguments.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServerGroupPropertiesResponseDelegatedSubnetArguments.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_arm_resource_id: Optional[str] = None):
        """
        The delegated subnet arguments for a server group.
        :param str subnet_arm_resource_id: delegated subnet arm resource id.
        """
        if subnet_arm_resource_id is not None:
            pulumi.set(__self__, "subnet_arm_resource_id", subnet_arm_resource_id)

    @property
    @pulumi.getter(name="subnetArmResourceId")
    def subnet_arm_resource_id(self) -> Optional[str]:
        """
        delegated subnet arm resource id.
        """
        return pulumi.get(self, "subnet_arm_resource_id")


@pulumi.output_type
class ServerGroupPropertiesResponsePrivateDnsZoneArguments(dict):
    """
    The private dns zone arguments for a server group.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateDnsZoneArmResourceId":
            suggest = "private_dns_zone_arm_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServerGroupPropertiesResponsePrivateDnsZoneArguments. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServerGroupPropertiesResponsePrivateDnsZoneArguments.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServerGroupPropertiesResponsePrivateDnsZoneArguments.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 private_dns_zone_arm_resource_id: Optional[str] = None):
        """
        The private dns zone arguments for a server group.
        :param str private_dns_zone_arm_resource_id: private dns zone arm resource id.
        """
        if private_dns_zone_arm_resource_id is not None:
            pulumi.set(__self__, "private_dns_zone_arm_resource_id", private_dns_zone_arm_resource_id)

    @property
    @pulumi.getter(name="privateDnsZoneArmResourceId")
    def private_dns_zone_arm_resource_id(self) -> Optional[str]:
        """
        private dns zone arm resource id.
        """
        return pulumi.get(self, "private_dns_zone_arm_resource_id")


@pulumi.output_type
class ServerNameItemResponse(dict):
    """
    The name object for a server.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fullyQualifiedDomainName":
            suggest = "fully_qualified_domain_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServerNameItemResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServerNameItemResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServerNameItemResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fully_qualified_domain_name: str,
                 name: Optional[str] = None):
        """
        The name object for a server.
        :param str fully_qualified_domain_name: The fully qualified domain name of a server.
        :param str name: The name of a server.
        """
        pulumi.set(__self__, "fully_qualified_domain_name", fully_qualified_domain_name)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> str:
        """
        The fully qualified domain name of a server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of a server.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class ServerRoleGroupResponse(dict):
    """
    Represents a server role group.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "enablePublicIp":
            suggest = "enable_public_ip"
        elif key == "serverNames":
            suggest = "server_names"
        elif key == "enableHa":
            suggest = "enable_ha"
        elif key == "serverCount":
            suggest = "server_count"
        elif key == "serverEdition":
            suggest = "server_edition"
        elif key == "storageQuotaInMb":
            suggest = "storage_quota_in_mb"
        elif key == "vCores":
            suggest = "v_cores"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServerRoleGroupResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServerRoleGroupResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServerRoleGroupResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enable_public_ip: bool,
                 server_names: Sequence['outputs.ServerNameItemResponse'],
                 enable_ha: Optional[bool] = None,
                 name: Optional[str] = None,
                 role: Optional[str] = None,
                 server_count: Optional[int] = None,
                 server_edition: Optional[str] = None,
                 storage_quota_in_mb: Optional[float] = None,
                 v_cores: Optional[float] = None):
        """
        Represents a server role group.
        :param bool enable_public_ip: If public IP is requested or not for a server.
        :param Sequence['ServerNameItemResponse'] server_names: The list of server names in the server role group.
        :param bool enable_ha: If high availability is enabled or not for the server.
        :param str name: The name of the server role group.
        :param str role: The role of servers in the server role group.
        :param int server_count: The number of servers in the server role group.
        :param str server_edition: The edition of a server (default: GeneralPurpose).
        :param float storage_quota_in_mb: The storage of a server in MB (max: 2097152 = 2TiB).
        :param float v_cores: The vCores count of a server (max: 64).
        """
        pulumi.set(__self__, "enable_public_ip", enable_public_ip)
        pulumi.set(__self__, "server_names", server_names)
        if enable_ha is not None:
            pulumi.set(__self__, "enable_ha", enable_ha)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if server_count is not None:
            pulumi.set(__self__, "server_count", server_count)
        if server_edition is not None:
            pulumi.set(__self__, "server_edition", server_edition)
        if storage_quota_in_mb is not None:
            pulumi.set(__self__, "storage_quota_in_mb", storage_quota_in_mb)
        if v_cores is not None:
            pulumi.set(__self__, "v_cores", v_cores)

    @property
    @pulumi.getter(name="enablePublicIp")
    def enable_public_ip(self) -> bool:
        """
        If public IP is requested or not for a server.
        """
        return pulumi.get(self, "enable_public_ip")

    @property
    @pulumi.getter(name="serverNames")
    def server_names(self) -> Sequence['outputs.ServerNameItemResponse']:
        """
        The list of server names in the server role group.
        """
        return pulumi.get(self, "server_names")

    @property
    @pulumi.getter(name="enableHa")
    def enable_ha(self) -> Optional[bool]:
        """
        If high availability is enabled or not for the server.
        """
        return pulumi.get(self, "enable_ha")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the server role group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def role(self) -> Optional[str]:
        """
        The role of servers in the server role group.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="serverCount")
    def server_count(self) -> Optional[int]:
        """
        The number of servers in the server role group.
        """
        return pulumi.get(self, "server_count")

    @property
    @pulumi.getter(name="serverEdition")
    def server_edition(self) -> Optional[str]:
        """
        The edition of a server (default: GeneralPurpose).
        """
        return pulumi.get(self, "server_edition")

    @property
    @pulumi.getter(name="storageQuotaInMb")
    def storage_quota_in_mb(self) -> Optional[float]:
        """
        The storage of a server in MB (max: 2097152 = 2TiB).
        """
        return pulumi.get(self, "storage_quota_in_mb")

    @property
    @pulumi.getter(name="vCores")
    def v_cores(self) -> Optional[float]:
        """
        The vCores count of a server (max: 64).
        """
        return pulumi.get(self, "v_cores")


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


