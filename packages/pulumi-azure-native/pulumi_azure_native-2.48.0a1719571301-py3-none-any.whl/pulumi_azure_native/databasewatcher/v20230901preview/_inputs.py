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
    'DatastoreArgs',
    'ManagedServiceIdentityArgs',
    'VaultSecretArgs',
]

@pulumi.input_type
class DatastoreArgs:
    def __init__(__self__, *,
                 kusto_cluster_uri: pulumi.Input[str],
                 kusto_data_ingestion_uri: pulumi.Input[str],
                 kusto_database_name: pulumi.Input[str],
                 kusto_management_url: pulumi.Input[str],
                 kusto_offering_type: pulumi.Input[Union[str, 'KustoOfferingType']],
                 adx_cluster_resource_id: Optional[pulumi.Input[str]] = None,
                 kusto_cluster_display_name: Optional[pulumi.Input[str]] = None):
        """
        The properties of a data store.
        :param pulumi.Input[str] kusto_cluster_uri: The Kusto cluster URI.
        :param pulumi.Input[str] kusto_data_ingestion_uri: The Kusto data ingestion URI.
        :param pulumi.Input[str] kusto_database_name: The name of a Kusto database.
        :param pulumi.Input[str] kusto_management_url: The Kusto management URL.
        :param pulumi.Input[Union[str, 'KustoOfferingType']] kusto_offering_type: The type of a Kusto offering.
        :param pulumi.Input[str] adx_cluster_resource_id: The Azure ResourceId of an Azure Data Explorer cluster.
        :param pulumi.Input[str] kusto_cluster_display_name: The Kusto cluster display name.
        """
        pulumi.set(__self__, "kusto_cluster_uri", kusto_cluster_uri)
        pulumi.set(__self__, "kusto_data_ingestion_uri", kusto_data_ingestion_uri)
        pulumi.set(__self__, "kusto_database_name", kusto_database_name)
        pulumi.set(__self__, "kusto_management_url", kusto_management_url)
        pulumi.set(__self__, "kusto_offering_type", kusto_offering_type)
        if adx_cluster_resource_id is not None:
            pulumi.set(__self__, "adx_cluster_resource_id", adx_cluster_resource_id)
        if kusto_cluster_display_name is not None:
            pulumi.set(__self__, "kusto_cluster_display_name", kusto_cluster_display_name)

    @property
    @pulumi.getter(name="kustoClusterUri")
    def kusto_cluster_uri(self) -> pulumi.Input[str]:
        """
        The Kusto cluster URI.
        """
        return pulumi.get(self, "kusto_cluster_uri")

    @kusto_cluster_uri.setter
    def kusto_cluster_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_cluster_uri", value)

    @property
    @pulumi.getter(name="kustoDataIngestionUri")
    def kusto_data_ingestion_uri(self) -> pulumi.Input[str]:
        """
        The Kusto data ingestion URI.
        """
        return pulumi.get(self, "kusto_data_ingestion_uri")

    @kusto_data_ingestion_uri.setter
    def kusto_data_ingestion_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_data_ingestion_uri", value)

    @property
    @pulumi.getter(name="kustoDatabaseName")
    def kusto_database_name(self) -> pulumi.Input[str]:
        """
        The name of a Kusto database.
        """
        return pulumi.get(self, "kusto_database_name")

    @kusto_database_name.setter
    def kusto_database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_database_name", value)

    @property
    @pulumi.getter(name="kustoManagementUrl")
    def kusto_management_url(self) -> pulumi.Input[str]:
        """
        The Kusto management URL.
        """
        return pulumi.get(self, "kusto_management_url")

    @kusto_management_url.setter
    def kusto_management_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_management_url", value)

    @property
    @pulumi.getter(name="kustoOfferingType")
    def kusto_offering_type(self) -> pulumi.Input[Union[str, 'KustoOfferingType']]:
        """
        The type of a Kusto offering.
        """
        return pulumi.get(self, "kusto_offering_type")

    @kusto_offering_type.setter
    def kusto_offering_type(self, value: pulumi.Input[Union[str, 'KustoOfferingType']]):
        pulumi.set(self, "kusto_offering_type", value)

    @property
    @pulumi.getter(name="adxClusterResourceId")
    def adx_cluster_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure ResourceId of an Azure Data Explorer cluster.
        """
        return pulumi.get(self, "adx_cluster_resource_id")

    @adx_cluster_resource_id.setter
    def adx_cluster_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adx_cluster_resource_id", value)

    @property
    @pulumi.getter(name="kustoClusterDisplayName")
    def kusto_cluster_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Kusto cluster display name.
        """
        return pulumi.get(self, "kusto_cluster_display_name")

    @kusto_cluster_display_name.setter
    def kusto_cluster_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kusto_cluster_display_name", value)


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
class VaultSecretArgs:
    def __init__(__self__, *,
                 akv_resource_id: Optional[pulumi.Input[str]] = None,
                 akv_target_password: Optional[pulumi.Input[str]] = None,
                 akv_target_user: Optional[pulumi.Input[str]] = None):
        """
        The vault specific details required if using SQL authentication to connect to a target.
        :param pulumi.Input[str] akv_resource_id: The Azure ResourceId of the Key Vault instance storing database authentication secrets.
        :param pulumi.Input[str] akv_target_password: The path to the Key Vault secret storing the password for authentication to a target.
        :param pulumi.Input[str] akv_target_user: The path to the Key Vault secret storing the login name (aka user name, aka account name) for authentication to a target.
        """
        if akv_resource_id is not None:
            pulumi.set(__self__, "akv_resource_id", akv_resource_id)
        if akv_target_password is not None:
            pulumi.set(__self__, "akv_target_password", akv_target_password)
        if akv_target_user is not None:
            pulumi.set(__self__, "akv_target_user", akv_target_user)

    @property
    @pulumi.getter(name="akvResourceId")
    def akv_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure ResourceId of the Key Vault instance storing database authentication secrets.
        """
        return pulumi.get(self, "akv_resource_id")

    @akv_resource_id.setter
    def akv_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "akv_resource_id", value)

    @property
    @pulumi.getter(name="akvTargetPassword")
    def akv_target_password(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the Key Vault secret storing the password for authentication to a target.
        """
        return pulumi.get(self, "akv_target_password")

    @akv_target_password.setter
    def akv_target_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "akv_target_password", value)

    @property
    @pulumi.getter(name="akvTargetUser")
    def akv_target_user(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the Key Vault secret storing the login name (aka user name, aka account name) for authentication to a target.
        """
        return pulumi.get(self, "akv_target_user")

    @akv_target_user.setter
    def akv_target_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "akv_target_user", value)


