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
    'GetSqlResourceSqlUserDefinedFunctionResult',
    'AwaitableGetSqlResourceSqlUserDefinedFunctionResult',
    'get_sql_resource_sql_user_defined_function',
    'get_sql_resource_sql_user_defined_function_output',
]

@pulumi.output_type
class GetSqlResourceSqlUserDefinedFunctionResult:
    """
    An Azure Cosmos DB userDefinedFunction.
    """
    def __init__(__self__, id=None, identity=None, location=None, name=None, resource=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource and not isinstance(resource, dict):
            raise TypeError("Expected argument 'resource' to be a dict")
        pulumi.set(__self__, "resource", resource)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique resource identifier of the ARM resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the ARM resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resource(self) -> Optional['outputs.SqlUserDefinedFunctionGetPropertiesResponseResource']:
        return pulumi.get(self, "resource")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB".
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetSqlResourceSqlUserDefinedFunctionResult(GetSqlResourceSqlUserDefinedFunctionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlResourceSqlUserDefinedFunctionResult(
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            resource=self.resource,
            tags=self.tags,
            type=self.type)


def get_sql_resource_sql_user_defined_function(account_name: Optional[str] = None,
                                               container_name: Optional[str] = None,
                                               database_name: Optional[str] = None,
                                               resource_group_name: Optional[str] = None,
                                               user_defined_function_name: Optional[str] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlResourceSqlUserDefinedFunctionResult:
    """
    Gets the SQL userDefinedFunction under an existing Azure Cosmos DB database account.


    :param str account_name: Cosmos DB database account name.
    :param str container_name: Cosmos DB container name.
    :param str database_name: Cosmos DB database name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str user_defined_function_name: Cosmos DB userDefinedFunction name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['containerName'] = container_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['userDefinedFunctionName'] = user_defined_function_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20231115preview:getSqlResourceSqlUserDefinedFunction', __args__, opts=opts, typ=GetSqlResourceSqlUserDefinedFunctionResult).value

    return AwaitableGetSqlResourceSqlUserDefinedFunctionResult(
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        resource=pulumi.get(__ret__, 'resource'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_sql_resource_sql_user_defined_function)
def get_sql_resource_sql_user_defined_function_output(account_name: Optional[pulumi.Input[str]] = None,
                                                      container_name: Optional[pulumi.Input[str]] = None,
                                                      database_name: Optional[pulumi.Input[str]] = None,
                                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                                      user_defined_function_name: Optional[pulumi.Input[str]] = None,
                                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlResourceSqlUserDefinedFunctionResult]:
    """
    Gets the SQL userDefinedFunction under an existing Azure Cosmos DB database account.


    :param str account_name: Cosmos DB database account name.
    :param str container_name: Cosmos DB container name.
    :param str database_name: Cosmos DB database name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str user_defined_function_name: Cosmos DB userDefinedFunction name.
    """
    ...
