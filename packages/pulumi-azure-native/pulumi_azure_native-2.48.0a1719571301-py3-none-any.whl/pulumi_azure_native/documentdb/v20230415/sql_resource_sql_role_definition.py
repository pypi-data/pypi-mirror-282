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

__all__ = ['SqlResourceSqlRoleDefinitionArgs', 'SqlResourceSqlRoleDefinition']

@pulumi.input_type
class SqlResourceSqlRoleDefinitionArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionArgs']]]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['RoleDefinitionType']] = None):
        """
        The set of arguments for constructing a SqlResourceSqlRoleDefinition resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assignable_scopes: A set of fully qualified Scopes at or below which Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.
        :param pulumi.Input[Sequence[pulumi.Input['PermissionArgs']]] permissions: The set of operations allowed through this Role Definition.
        :param pulumi.Input[str] role_definition_id: The GUID for the Role Definition.
        :param pulumi.Input[str] role_name: A user-friendly name for the Role Definition. Must be unique for the database account.
        :param pulumi.Input['RoleDefinitionType'] type: Indicates whether the Role Definition was built-in or user created.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if assignable_scopes is not None:
            pulumi.set(__self__, "assignable_scopes", assignable_scopes)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if role_definition_id is not None:
            pulumi.set(__self__, "role_definition_id", role_definition_id)
        if role_name is not None:
            pulumi.set(__self__, "role_name", role_name)
        if type is not None:
            pulumi.set(__self__, "type", type)

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
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of fully qualified Scopes at or below which Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.
        """
        return pulumi.get(self, "assignable_scopes")

    @assignable_scopes.setter
    def assignable_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "assignable_scopes", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PermissionArgs']]]]:
        """
        The set of operations allowed through this Role Definition.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The GUID for the Role Definition.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_definition_id", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-friendly name for the Role Definition. Must be unique for the database account.
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['RoleDefinitionType']]:
        """
        Indicates whether the Role Definition was built-in or user created.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['RoleDefinitionType']]):
        pulumi.set(self, "type", value)


class SqlResourceSqlRoleDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['RoleDefinitionType']] = None,
                 __props__=None):
        """
        An Azure Cosmos DB SQL Role Definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Cosmos DB database account name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assignable_scopes: A set of fully qualified Scopes at or below which Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionArgs']]]] permissions: The set of operations allowed through this Role Definition.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] role_definition_id: The GUID for the Role Definition.
        :param pulumi.Input[str] role_name: A user-friendly name for the Role Definition. Must be unique for the database account.
        :param pulumi.Input['RoleDefinitionType'] type: Indicates whether the Role Definition was built-in or user created.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlResourceSqlRoleDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure Cosmos DB SQL Role Definition.

        :param str resource_name: The name of the resource.
        :param SqlResourceSqlRoleDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlResourceSqlRoleDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PermissionArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['RoleDefinitionType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlResourceSqlRoleDefinitionArgs.__new__(SqlResourceSqlRoleDefinitionArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["assignable_scopes"] = assignable_scopes
            __props__.__dict__["permissions"] = permissions
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["role_definition_id"] = role_definition_id
            __props__.__dict__["role_name"] = role_name
            __props__.__dict__["type"] = type
            __props__.__dict__["name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:documentdb:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20200601preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20210301preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20210401preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20210415:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20210515:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20210615:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20210701preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20211015:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20211015preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20211115preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220215preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220515:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220515preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220815:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20220815preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20221115:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20221115preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230301preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230315:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230315preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230915:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20230915preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20231115:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20231115preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20240215preview:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20240515:SqlResourceSqlRoleDefinition"), pulumi.Alias(type_="azure-native:documentdb/v20240515preview:SqlResourceSqlRoleDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlResourceSqlRoleDefinition, __self__).__init__(
            'azure-native:documentdb/v20230415:SqlResourceSqlRoleDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlResourceSqlRoleDefinition':
        """
        Get an existing SqlResourceSqlRoleDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlResourceSqlRoleDefinitionArgs.__new__(SqlResourceSqlRoleDefinitionArgs)

        __props__.__dict__["assignable_scopes"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["role_name"] = None
        __props__.__dict__["type"] = None
        return SqlResourceSqlRoleDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A set of fully qualified Scopes at or below which Role Assignments may be created using this Role Definition. This will allow application of this Role Definition on the entire database account or any underlying Database / Collection. Must have at least one element. Scopes higher than Database account are not enforceable as assignable Scopes. Note that resources referenced in assignable Scopes need not exist.
        """
        return pulumi.get(self, "assignable_scopes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence['outputs.PermissionResponse']]]:
        """
        The set of operations allowed through this Role Definition.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[Optional[str]]:
        """
        A user-friendly name for the Role Definition. Must be unique for the database account.
        """
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")

