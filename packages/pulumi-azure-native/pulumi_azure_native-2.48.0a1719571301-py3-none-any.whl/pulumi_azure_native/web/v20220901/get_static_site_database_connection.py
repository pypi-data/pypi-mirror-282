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
    'GetStaticSiteDatabaseConnectionResult',
    'AwaitableGetStaticSiteDatabaseConnectionResult',
    'get_static_site_database_connection',
    'get_static_site_database_connection_output',
]

@pulumi.output_type
class GetStaticSiteDatabaseConnectionResult:
    """
    Static Site Database Connection resource.
    """
    def __init__(__self__, configuration_files=None, connection_identity=None, connection_string=None, id=None, kind=None, name=None, region=None, resource_id=None, type=None):
        if configuration_files and not isinstance(configuration_files, list):
            raise TypeError("Expected argument 'configuration_files' to be a list")
        pulumi.set(__self__, "configuration_files", configuration_files)
        if connection_identity and not isinstance(connection_identity, str):
            raise TypeError("Expected argument 'connection_identity' to be a str")
        pulumi.set(__self__, "connection_identity", connection_identity)
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="configurationFiles")
    def configuration_files(self) -> Sequence['outputs.StaticSiteDatabaseConnectionConfigurationFileOverviewResponse']:
        """
        A list of configuration files associated with this database connection.
        """
        return pulumi.get(self, "configuration_files")

    @property
    @pulumi.getter(name="connectionIdentity")
    def connection_identity(self) -> Optional[str]:
        """
        If present, the identity is used in conjunction with connection string to connect to the database. Use of the system-assigned managed identity is indicated with the string 'SystemAssigned', while use of a user-assigned managed identity is indicated with the resource id of the managed identity resource.
        """
        return pulumi.get(self, "connection_identity")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[str]:
        """
        The connection string to use to connect to the database.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region of the database resource.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> str:
        """
        The resource id of the database.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetStaticSiteDatabaseConnectionResult(GetStaticSiteDatabaseConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStaticSiteDatabaseConnectionResult(
            configuration_files=self.configuration_files,
            connection_identity=self.connection_identity,
            connection_string=self.connection_string,
            id=self.id,
            kind=self.kind,
            name=self.name,
            region=self.region,
            resource_id=self.resource_id,
            type=self.type)


def get_static_site_database_connection(database_connection_name: Optional[str] = None,
                                        name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStaticSiteDatabaseConnectionResult:
    """
    Static Site Database Connection resource.


    :param str database_connection_name: Name of the database connection.
    :param str name: Name of the static site
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['databaseConnectionName'] = database_connection_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20220901:getStaticSiteDatabaseConnection', __args__, opts=opts, typ=GetStaticSiteDatabaseConnectionResult).value

    return AwaitableGetStaticSiteDatabaseConnectionResult(
        configuration_files=pulumi.get(__ret__, 'configuration_files'),
        connection_identity=pulumi.get(__ret__, 'connection_identity'),
        connection_string=pulumi.get(__ret__, 'connection_string'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        region=pulumi.get(__ret__, 'region'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_static_site_database_connection)
def get_static_site_database_connection_output(database_connection_name: Optional[pulumi.Input[str]] = None,
                                               name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStaticSiteDatabaseConnectionResult]:
    """
    Static Site Database Connection resource.


    :param str database_connection_name: Name of the database connection.
    :param str name: Name of the static site
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
