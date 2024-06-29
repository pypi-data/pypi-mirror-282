# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['VariableArgs', 'Variable']

@pulumi.input_type
class VariableArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 is_encrypted: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 variable_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Variable resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] name: Gets or sets the name of the variable.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] description: Gets or sets the description of the variable.
        :param pulumi.Input[bool] is_encrypted: Gets or sets the encrypted flag of the variable.
        :param pulumi.Input[str] value: Gets or sets the value of the variable.
        :param pulumi.Input[str] variable_name: The variable name.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if is_encrypted is not None:
            pulumi.set(__self__, "is_encrypted", is_encrypted)
        if value is not None:
            pulumi.set(__self__, "value", value)
        if variable_name is not None:
            pulumi.set(__self__, "variable_name", variable_name)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Gets or sets the name of the variable.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the description of the variable.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="isEncrypted")
    def is_encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
        Gets or sets the encrypted flag of the variable.
        """
        return pulumi.get(self, "is_encrypted")

    @is_encrypted.setter
    def is_encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_encrypted", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the value of the variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="variableName")
    def variable_name(self) -> Optional[pulumi.Input[str]]:
        """
        The variable name.
        """
        return pulumi.get(self, "variable_name")

    @variable_name.setter
    def variable_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "variable_name", value)


class Variable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_encrypted: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 variable_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Definition of the variable.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] description: Gets or sets the description of the variable.
        :param pulumi.Input[bool] is_encrypted: Gets or sets the encrypted flag of the variable.
        :param pulumi.Input[str] name: Gets or sets the name of the variable.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] value: Gets or sets the value of the variable.
        :param pulumi.Input[str] variable_name: The variable name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VariableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the variable.

        :param str resource_name: The name of the resource.
        :param VariableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VariableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_encrypted: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 variable_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VariableArgs.__new__(VariableArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["description"] = description
            __props__.__dict__["is_encrypted"] = is_encrypted
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["value"] = value
            __props__.__dict__["variable_name"] = variable_name
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automation:Variable"), pulumi.Alias(type_="azure-native:automation/v20151031:Variable"), pulumi.Alias(type_="azure-native:automation/v20190601:Variable"), pulumi.Alias(type_="azure-native:automation/v20200113preview:Variable"), pulumi.Alias(type_="azure-native:automation/v20220808:Variable"), pulumi.Alias(type_="azure-native:automation/v20230515preview:Variable")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Variable, __self__).__init__(
            'azure-native:automation/v20231101:Variable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Variable':
        """
        Get an existing Variable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VariableArgs.__new__(VariableArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["is_encrypted"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        return Variable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="isEncrypted")
    def is_encrypted(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets the encrypted flag of the variable.
        """
        return pulumi.get(self, "is_encrypted")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the value of the variable.
        """
        return pulumi.get(self, "value")

