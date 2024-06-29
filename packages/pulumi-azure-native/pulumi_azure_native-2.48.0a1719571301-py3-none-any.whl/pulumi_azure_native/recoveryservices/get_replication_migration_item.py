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
    'GetReplicationMigrationItemResult',
    'AwaitableGetReplicationMigrationItemResult',
    'get_replication_migration_item',
    'get_replication_migration_item_output',
]

@pulumi.output_type
class GetReplicationMigrationItemResult:
    """
    Migration item.
    """
    def __init__(__self__, id=None, location=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.MigrationItemPropertiesResponse':
        """
        The migration item properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource Type
        """
        return pulumi.get(self, "type")


class AwaitableGetReplicationMigrationItemResult(GetReplicationMigrationItemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationMigrationItemResult(
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_replication_migration_item(fabric_name: Optional[str] = None,
                                   migration_item_name: Optional[str] = None,
                                   protection_container_name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   resource_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationMigrationItemResult:
    """
    Migration item.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-06-01, 2023-08-01, 2024-01-01, 2024-02-01, 2024-04-01.


    :param str fabric_name: Fabric unique name.
    :param str migration_item_name: Migration item name.
    :param str protection_container_name: Protection container name.
    :param str resource_group_name: The name of the resource group where the recovery services vault is present.
    :param str resource_name: The name of the recovery services vault.
    """
    __args__ = dict()
    __args__['fabricName'] = fabric_name
    __args__['migrationItemName'] = migration_item_name
    __args__['protectionContainerName'] = protection_container_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:recoveryservices:getReplicationMigrationItem', __args__, opts=opts, typ=GetReplicationMigrationItemResult).value

    return AwaitableGetReplicationMigrationItemResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_replication_migration_item)
def get_replication_migration_item_output(fabric_name: Optional[pulumi.Input[str]] = None,
                                          migration_item_name: Optional[pulumi.Input[str]] = None,
                                          protection_container_name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          resource_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationMigrationItemResult]:
    """
    Migration item.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-06-01, 2023-08-01, 2024-01-01, 2024-02-01, 2024-04-01.


    :param str fabric_name: Fabric unique name.
    :param str migration_item_name: Migration item name.
    :param str protection_container_name: Protection container name.
    :param str resource_group_name: The name of the resource group where the recovery services vault is present.
    :param str resource_name: The name of the recovery services vault.
    """
    ...
