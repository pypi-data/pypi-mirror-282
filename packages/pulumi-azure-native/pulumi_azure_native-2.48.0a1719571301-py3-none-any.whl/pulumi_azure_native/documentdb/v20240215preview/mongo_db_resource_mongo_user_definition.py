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
from ._inputs import *

__all__ = ['MongoDBResourceMongoUserDefinitionArgs', 'MongoDBResourceMongoUserDefinition']

@pulumi.input_type
class MongoDBResourceMongoUserDefinitionArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 custom_data: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 mechanisms: Optional[pulumi.Input[str]] = None,
                 mongo_user_definition_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input['RoleArgs']]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MongoDBResourceMongoUserDefinition resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] custom_data: A custom definition for the USer Definition.
        :param pulumi.Input[str] database_name: The database name for which access is being granted for this User Definition.
        :param pulumi.Input[str] mechanisms: The Mongo Auth mechanism. For now, we only support auth mechanism SCRAM-SHA-256.
        :param pulumi.Input[str] mongo_user_definition_id: The ID for the User Definition {dbName.userName}.
        :param pulumi.Input[str] password: The password for User Definition. Response does not contain user password.
        :param pulumi.Input[Sequence[pulumi.Input['RoleArgs']]] roles: The set of roles inherited by the User Definition.
        :param pulumi.Input[str] user_name: The user name for User Definition.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if custom_data is not None:
            pulumi.set(__self__, "custom_data", custom_data)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if mechanisms is not None:
            pulumi.set(__self__, "mechanisms", mechanisms)
        if mongo_user_definition_id is not None:
            pulumi.set(__self__, "mongo_user_definition_id", mongo_user_definition_id)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if roles is not None:
            pulumi.set(__self__, "roles", roles)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Cosmos DB database account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

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
    @pulumi.getter(name="customData")
    def custom_data(self) -> Optional[pulumi.Input[str]]:
        """
        A custom definition for the USer Definition.
        """
        return pulumi.get(self, "custom_data")

    @custom_data.setter
    def custom_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_data", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The database name for which access is being granted for this User Definition.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter
    def mechanisms(self) -> Optional[pulumi.Input[str]]:
        """
        The Mongo Auth mechanism. For now, we only support auth mechanism SCRAM-SHA-256.
        """
        return pulumi.get(self, "mechanisms")

    @mechanisms.setter
    def mechanisms(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mechanisms", value)

    @property
    @pulumi.getter(name="mongoUserDefinitionId")
    def mongo_user_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID for the User Definition {dbName.userName}.
        """
        return pulumi.get(self, "mongo_user_definition_id")

    @mongo_user_definition_id.setter
    def mongo_user_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mongo_user_definition_id", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for User Definition. Response does not contain user password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def roles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoleArgs']]]]:
        """
        The set of roles inherited by the User Definition.
        """
        return pulumi.get(self, "roles")

    @roles.setter
    def roles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoleArgs']]]]):
        pulumi.set(self, "roles", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        The user name for User Definition.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


class MongoDBResourceMongoUserDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 custom_data: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 mechanisms: Optional[pulumi.Input[str]] = None,
                 mongo_user_definition_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleArgs']]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure Cosmos DB User Definition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] custom_data: A custom definition for the USer Definition.
        :param pulumi.Input[str] database_name: The database name for which access is being granted for this User Definition.
        :param pulumi.Input[str] mechanisms: The Mongo Auth mechanism. For now, we only support auth mechanism SCRAM-SHA-256.
        :param pulumi.Input[str] mongo_user_definition_id: The ID for the User Definition {dbName.userName}.
        :param pulumi.Input[str] password: The password for User Definition. Response does not contain user password.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleArgs']]]] roles: The set of roles inherited by the User Definition.
        :param pulumi.Input[str] user_name: The user name for User Definition.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MongoDBResourceMongoUserDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure Cosmos DB User Definition

        :param str resource_name: The name of the resource.
        :param MongoDBResourceMongoUserDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MongoDBResourceMongoUserDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 custom_data: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 mechanisms: Optional[pulumi.Input[str]] = None,
                 mongo_user_definition_id: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoleArgs']]]]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MongoDBResourceMongoUserDefinitionArgs.__new__(MongoDBResourceMongoUserDefinitionArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["custom_data"] = custom_data
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["mechanisms"] = mechanisms
            __props__.__dict__["mongo_user_definition_id"] = mongo_user_definition_id
            __props__.__dict__["password"] = password
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["roles"] = roles
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:documentdb:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20211015preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20211115preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220215preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220515preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220815:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220815preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20221115:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20221115preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230301preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230315:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230315preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230415:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230915:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230915preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20231115:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20231115preview:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20240515:MongoDBResourceMongoUserDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20240515preview:MongoDBResourceMongoUserDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MongoDBResourceMongoUserDefinition, __self__).__init__(
            'azure-native:documentdb/v20240215preview:MongoDBResourceMongoUserDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MongoDBResourceMongoUserDefinition':
        """
        Get an existing MongoDBResourceMongoUserDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MongoDBResourceMongoUserDefinitionArgs.__new__(MongoDBResourceMongoUserDefinitionArgs)

        __props__.__dict__["custom_data"] = None
        __props__.__dict__["database_name"] = None
        __props__.__dict__["mechanisms"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["roles"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_name"] = None
        return MongoDBResourceMongoUserDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customData")
    def custom_data(self) -> pulumi.Output[Optional[str]]:
        """
        A custom definition for the USer Definition.
        """
        return pulumi.get(self, "custom_data")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[str]]:
        """
        The database name for which access is being granted for this User Definition.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def mechanisms(self) -> pulumi.Output[Optional[str]]:
        """
        The Mongo Auth mechanism. For now, we only support auth mechanism SCRAM-SHA-256.
        """
        return pulumi.get(self, "mechanisms")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The password for User Definition. Response does not contain user password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Optional[Sequence['outputs.RoleResponse']]]:
        """
        The set of roles inherited by the User Definition.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[Optional[str]]:
        """
        The user name for User Definition.
        """
        return pulumi.get(self, "user_name")

