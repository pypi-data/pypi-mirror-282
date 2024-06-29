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

__all__ = ['SenderUsernameArgs', 'SenderUsername']

@pulumi.input_type
class SenderUsernameArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 email_service_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 username: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 sender_username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SenderUsername resource.
        :param pulumi.Input[str] domain_name: The name of the Domains resource.
        :param pulumi.Input[str] email_service_name: The name of the EmailService resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] username: A sender senderUsername to be used when sending emails.
        :param pulumi.Input[str] display_name: The display name for the senderUsername.
        :param pulumi.Input[str] sender_username: The valid sender Username.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "email_service_name", email_service_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "username", username)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if sender_username is not None:
            pulumi.set(__self__, "sender_username", sender_username)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The name of the Domains resource.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="emailServiceName")
    def email_service_name(self) -> pulumi.Input[str]:
        """
        The name of the EmailService resource.
        """
        return pulumi.get(self, "email_service_name")

    @email_service_name.setter
    def email_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_service_name", value)

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
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        A sender senderUsername to be used when sending emails.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the senderUsername.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="senderUsername")
    def sender_username(self) -> Optional[pulumi.Input[str]]:
        """
        The valid sender Username.
        """
        return pulumi.get(self, "sender_username")

    @sender_username.setter
    def sender_username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sender_username", value)


class SenderUsername(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 email_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sender_username: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A class representing a SenderUsername resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The display name for the senderUsername.
        :param pulumi.Input[str] domain_name: The name of the Domains resource.
        :param pulumi.Input[str] email_service_name: The name of the EmailService resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sender_username: The valid sender Username.
        :param pulumi.Input[str] username: A sender senderUsername to be used when sending emails.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SenderUsernameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A class representing a SenderUsername resource.

        :param str resource_name: The name of the resource.
        :param SenderUsernameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SenderUsernameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 email_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sender_username: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SenderUsernameArgs.__new__(SenderUsernameArgs)

            __props__.__dict__["display_name"] = display_name
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            if email_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'email_service_name'")
            __props__.__dict__["email_service_name"] = email_service_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sender_username"] = sender_username
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
            __props__.__dict__["data_location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:communication:SenderUsername"), pulumi.Alias(type_="azure-native:communication/v20230301preview:SenderUsername"), pulumi.Alias(type_="azure-native:communication/v20230401:SenderUsername"), pulumi.Alias(type_="azure-native:communication/v20230401preview:SenderUsername"), pulumi.Alias(type_="azure-native:communication/v20230601preview:SenderUsername")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SenderUsername, __self__).__init__(
            'azure-native:communication/v20230331:SenderUsername',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SenderUsername':
        """
        Get an existing SenderUsername resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SenderUsernameArgs.__new__(SenderUsernameArgs)

        __props__.__dict__["data_location"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["username"] = None
        return SenderUsername(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> pulumi.Output[str]:
        """
        The location where the SenderUsername resource data is stored at rest.
        """
        return pulumi.get(self, "data_location")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name for the senderUsername.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource. Unknown is the default state for Communication Services.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        A sender senderUsername to be used when sending emails.
        """
        return pulumi.get(self, "username")

