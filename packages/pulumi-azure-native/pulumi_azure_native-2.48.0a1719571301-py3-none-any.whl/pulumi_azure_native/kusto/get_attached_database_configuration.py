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
    'GetAttachedDatabaseConfigurationResult',
    'AwaitableGetAttachedDatabaseConfigurationResult',
    'get_attached_database_configuration',
    'get_attached_database_configuration_output',
]

@pulumi.output_type
class GetAttachedDatabaseConfigurationResult:
    """
    Class representing an attached database configuration.
    """
    def __init__(__self__, attached_database_names=None, cluster_resource_id=None, database_name=None, database_name_override=None, database_name_prefix=None, default_principals_modification_kind=None, id=None, location=None, name=None, provisioning_state=None, table_level_sharing_properties=None, type=None):
        if attached_database_names and not isinstance(attached_database_names, list):
            raise TypeError("Expected argument 'attached_database_names' to be a list")
        pulumi.set(__self__, "attached_database_names", attached_database_names)
        if cluster_resource_id and not isinstance(cluster_resource_id, str):
            raise TypeError("Expected argument 'cluster_resource_id' to be a str")
        pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if database_name_override and not isinstance(database_name_override, str):
            raise TypeError("Expected argument 'database_name_override' to be a str")
        pulumi.set(__self__, "database_name_override", database_name_override)
        if database_name_prefix and not isinstance(database_name_prefix, str):
            raise TypeError("Expected argument 'database_name_prefix' to be a str")
        pulumi.set(__self__, "database_name_prefix", database_name_prefix)
        if default_principals_modification_kind and not isinstance(default_principals_modification_kind, str):
            raise TypeError("Expected argument 'default_principals_modification_kind' to be a str")
        pulumi.set(__self__, "default_principals_modification_kind", default_principals_modification_kind)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if table_level_sharing_properties and not isinstance(table_level_sharing_properties, dict):
            raise TypeError("Expected argument 'table_level_sharing_properties' to be a dict")
        pulumi.set(__self__, "table_level_sharing_properties", table_level_sharing_properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="attachedDatabaseNames")
    def attached_database_names(self) -> Sequence[str]:
        """
        The list of databases from the clusterResourceId which are currently attached to the cluster.
        """
        return pulumi.get(self, "attached_database_names")

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> str:
        """
        The resource id of the cluster where the databases you would like to attach reside.
        """
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> str:
        """
        The name of the database which you would like to attach, use * if you want to follow all current and future databases.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="databaseNameOverride")
    def database_name_override(self) -> Optional[str]:
        """
        Overrides the original database name. Relevant only when attaching to a specific database.
        """
        return pulumi.get(self, "database_name_override")

    @property
    @pulumi.getter(name="databaseNamePrefix")
    def database_name_prefix(self) -> Optional[str]:
        """
        Adds a prefix to the attached databases name. When following an entire cluster, that prefix would be added to all of the databases original names from leader cluster.
        """
        return pulumi.get(self, "database_name_prefix")

    @property
    @pulumi.getter(name="defaultPrincipalsModificationKind")
    def default_principals_modification_kind(self) -> str:
        """
        The default principals modification kind
        """
        return pulumi.get(self, "default_principals_modification_kind")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

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
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="tableLevelSharingProperties")
    def table_level_sharing_properties(self) -> Optional['outputs.TableLevelSharingPropertiesResponse']:
        """
        Table level sharing specifications
        """
        return pulumi.get(self, "table_level_sharing_properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAttachedDatabaseConfigurationResult(GetAttachedDatabaseConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAttachedDatabaseConfigurationResult(
            attached_database_names=self.attached_database_names,
            cluster_resource_id=self.cluster_resource_id,
            database_name=self.database_name,
            database_name_override=self.database_name_override,
            database_name_prefix=self.database_name_prefix,
            default_principals_modification_kind=self.default_principals_modification_kind,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            table_level_sharing_properties=self.table_level_sharing_properties,
            type=self.type)


def get_attached_database_configuration(attached_database_configuration_name: Optional[str] = None,
                                        cluster_name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAttachedDatabaseConfigurationResult:
    """
    Returns an attached database configuration.
    Azure REST API version: 2022-12-29.

    Other available API versions: 2023-05-02, 2023-08-15.


    :param str attached_database_configuration_name: The name of the attached database configuration.
    :param str cluster_name: The name of the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['attachedDatabaseConfigurationName'] = attached_database_configuration_name
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kusto:getAttachedDatabaseConfiguration', __args__, opts=opts, typ=GetAttachedDatabaseConfigurationResult).value

    return AwaitableGetAttachedDatabaseConfigurationResult(
        attached_database_names=pulumi.get(__ret__, 'attached_database_names'),
        cluster_resource_id=pulumi.get(__ret__, 'cluster_resource_id'),
        database_name=pulumi.get(__ret__, 'database_name'),
        database_name_override=pulumi.get(__ret__, 'database_name_override'),
        database_name_prefix=pulumi.get(__ret__, 'database_name_prefix'),
        default_principals_modification_kind=pulumi.get(__ret__, 'default_principals_modification_kind'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        table_level_sharing_properties=pulumi.get(__ret__, 'table_level_sharing_properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_attached_database_configuration)
def get_attached_database_configuration_output(attached_database_configuration_name: Optional[pulumi.Input[str]] = None,
                                               cluster_name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAttachedDatabaseConfigurationResult]:
    """
    Returns an attached database configuration.
    Azure REST API version: 2022-12-29.

    Other available API versions: 2023-05-02, 2023-08-15.


    :param str attached_database_configuration_name: The name of the attached database configuration.
    :param str cluster_name: The name of the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
