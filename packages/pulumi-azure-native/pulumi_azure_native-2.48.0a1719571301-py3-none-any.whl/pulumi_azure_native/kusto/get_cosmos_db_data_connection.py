# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetCosmosDbDataConnectionResult',
    'AwaitableGetCosmosDbDataConnectionResult',
    'get_cosmos_db_data_connection',
    'get_cosmos_db_data_connection_output',
]

@pulumi.output_type
class GetCosmosDbDataConnectionResult:
    """
    Class representing a CosmosDb data connection.
    """
    def __init__(__self__, cosmos_db_account_resource_id=None, cosmos_db_container=None, cosmos_db_database=None, id=None, kind=None, location=None, managed_identity_object_id=None, managed_identity_resource_id=None, mapping_rule_name=None, name=None, provisioning_state=None, retrieval_start_date=None, table_name=None, type=None):
        if cosmos_db_account_resource_id and not isinstance(cosmos_db_account_resource_id, str):
            raise TypeError("Expected argument 'cosmos_db_account_resource_id' to be a str")
        pulumi.set(__self__, "cosmos_db_account_resource_id", cosmos_db_account_resource_id)
        if cosmos_db_container and not isinstance(cosmos_db_container, str):
            raise TypeError("Expected argument 'cosmos_db_container' to be a str")
        pulumi.set(__self__, "cosmos_db_container", cosmos_db_container)
        if cosmos_db_database and not isinstance(cosmos_db_database, str):
            raise TypeError("Expected argument 'cosmos_db_database' to be a str")
        pulumi.set(__self__, "cosmos_db_database", cosmos_db_database)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_identity_object_id and not isinstance(managed_identity_object_id, str):
            raise TypeError("Expected argument 'managed_identity_object_id' to be a str")
        pulumi.set(__self__, "managed_identity_object_id", managed_identity_object_id)
        if managed_identity_resource_id and not isinstance(managed_identity_resource_id, str):
            raise TypeError("Expected argument 'managed_identity_resource_id' to be a str")
        pulumi.set(__self__, "managed_identity_resource_id", managed_identity_resource_id)
        if mapping_rule_name and not isinstance(mapping_rule_name, str):
            raise TypeError("Expected argument 'mapping_rule_name' to be a str")
        pulumi.set(__self__, "mapping_rule_name", mapping_rule_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if retrieval_start_date and not isinstance(retrieval_start_date, str):
            raise TypeError("Expected argument 'retrieval_start_date' to be a str")
        pulumi.set(__self__, "retrieval_start_date", retrieval_start_date)
        if table_name and not isinstance(table_name, str):
            raise TypeError("Expected argument 'table_name' to be a str")
        pulumi.set(__self__, "table_name", table_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="cosmosDbAccountResourceId")
    def cosmos_db_account_resource_id(self) -> str:
        """
        The resource ID of the Cosmos DB account used to create the data connection.
        """
        return pulumi.get(self, "cosmos_db_account_resource_id")

    @property
    @pulumi.getter(name="cosmosDbContainer")
    def cosmos_db_container(self) -> str:
        """
        The name of an existing container in the Cosmos DB database.
        """
        return pulumi.get(self, "cosmos_db_container")

    @property
    @pulumi.getter(name="cosmosDbDatabase")
    def cosmos_db_database(self) -> str:
        """
        The name of an existing database in the Cosmos DB account.
        """
        return pulumi.get(self, "cosmos_db_database")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of the endpoint for the data connection
        Expected value is 'CosmosDb'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedIdentityObjectId")
    def managed_identity_object_id(self) -> str:
        """
        The object ID of the managed identity resource.
        """
        return pulumi.get(self, "managed_identity_object_id")

    @property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> str:
        """
        The resource ID of a managed system or user-assigned identity. The identity is used to authenticate with Cosmos DB.
        """
        return pulumi.get(self, "managed_identity_resource_id")

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[str]:
        """
        The name of an existing mapping rule to use when ingesting the retrieved data.
        """
        return pulumi.get(self, "mapping_rule_name")

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
    @pulumi.getter(name="retrievalStartDate")
    def retrieval_start_date(self) -> Optional[str]:
        """
        Optional. If defined, the data connection retrieves Cosmos DB documents created or updated after the specified retrieval start date.
        """
        return pulumi.get(self, "retrieval_start_date")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> str:
        """
        The case-sensitive name of the existing target table in your cluster. Retrieved data is ingested into this table.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetCosmosDbDataConnectionResult(GetCosmosDbDataConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCosmosDbDataConnectionResult(
            cosmos_db_account_resource_id=self.cosmos_db_account_resource_id,
            cosmos_db_container=self.cosmos_db_container,
            cosmos_db_database=self.cosmos_db_database,
            id=self.id,
            kind=self.kind,
            location=self.location,
            managed_identity_object_id=self.managed_identity_object_id,
            managed_identity_resource_id=self.managed_identity_resource_id,
            mapping_rule_name=self.mapping_rule_name,
            name=self.name,
            provisioning_state=self.provisioning_state,
            retrieval_start_date=self.retrieval_start_date,
            table_name=self.table_name,
            type=self.type)


def get_cosmos_db_data_connection(cluster_name: Optional[str] = None,
                                  data_connection_name: Optional[str] = None,
                                  database_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCosmosDbDataConnectionResult:
    """
    Returns a data connection.
    Azure REST API version: 2022-12-29.


    :param str cluster_name: The name of the Kusto cluster.
    :param str data_connection_name: The name of the data connection.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['dataConnectionName'] = data_connection_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kusto:getCosmosDbDataConnection', __args__, opts=opts, typ=GetCosmosDbDataConnectionResult).value

    return AwaitableGetCosmosDbDataConnectionResult(
        cosmos_db_account_resource_id=pulumi.get(__ret__, 'cosmos_db_account_resource_id'),
        cosmos_db_container=pulumi.get(__ret__, 'cosmos_db_container'),
        cosmos_db_database=pulumi.get(__ret__, 'cosmos_db_database'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        managed_identity_object_id=pulumi.get(__ret__, 'managed_identity_object_id'),
        managed_identity_resource_id=pulumi.get(__ret__, 'managed_identity_resource_id'),
        mapping_rule_name=pulumi.get(__ret__, 'mapping_rule_name'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        retrieval_start_date=pulumi.get(__ret__, 'retrieval_start_date'),
        table_name=pulumi.get(__ret__, 'table_name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_cosmos_db_data_connection)
def get_cosmos_db_data_connection_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                         data_connection_name: Optional[pulumi.Input[str]] = None,
                                         database_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCosmosDbDataConnectionResult]:
    """
    Returns a data connection.
    Azure REST API version: 2022-12-29.


    :param str cluster_name: The name of the Kusto cluster.
    :param str data_connection_name: The name of the data connection.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
