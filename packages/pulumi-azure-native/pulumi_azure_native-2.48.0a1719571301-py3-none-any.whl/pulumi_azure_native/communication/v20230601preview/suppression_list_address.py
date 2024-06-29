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

__all__ = ['SuppressionListAddressArgs', 'SuppressionListAddress']

@pulumi.input_type
class SuppressionListAddressArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 email: pulumi.Input[str],
                 email_service_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 suppression_list_name: pulumi.Input[str],
                 address_id: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SuppressionListAddress resource.
        :param pulumi.Input[str] domain_name: The name of the Domains resource.
        :param pulumi.Input[str] email: Email address of the recipient.
        :param pulumi.Input[str] email_service_name: The name of the EmailService resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] suppression_list_name: The name of the suppression list.
        :param pulumi.Input[str] address_id: The id of the address in a suppression list.
        :param pulumi.Input[str] first_name: The first name of the email recipient.
        :param pulumi.Input[str] last_name: The last name of the email recipient.
        :param pulumi.Input[str] notes: An optional property to provide contextual notes or a description for an address.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "email_service_name", email_service_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "suppression_list_name", suppression_list_name)
        if address_id is not None:
            pulumi.set(__self__, "address_id", address_id)
        if first_name is not None:
            pulumi.set(__self__, "first_name", first_name)
        if last_name is not None:
            pulumi.set(__self__, "last_name", last_name)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)

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
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        Email address of the recipient.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

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
    @pulumi.getter(name="suppressionListName")
    def suppression_list_name(self) -> pulumi.Input[str]:
        """
        The name of the suppression list.
        """
        return pulumi.get(self, "suppression_list_name")

    @suppression_list_name.setter
    def suppression_list_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "suppression_list_name", value)

    @property
    @pulumi.getter(name="addressId")
    def address_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the address in a suppression list.
        """
        return pulumi.get(self, "address_id")

    @address_id.setter
    def address_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_id", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        The first name of the email recipient.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        The last name of the email recipient.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        An optional property to provide contextual notes or a description for an address.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)


class SuppressionListAddress(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_id: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 email_service_name: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 suppression_list_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A object that represents a SuppressionList record.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_id: The id of the address in a suppression list.
        :param pulumi.Input[str] domain_name: The name of the Domains resource.
        :param pulumi.Input[str] email: Email address of the recipient.
        :param pulumi.Input[str] email_service_name: The name of the EmailService resource.
        :param pulumi.Input[str] first_name: The first name of the email recipient.
        :param pulumi.Input[str] last_name: The last name of the email recipient.
        :param pulumi.Input[str] notes: An optional property to provide contextual notes or a description for an address.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] suppression_list_name: The name of the suppression list.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SuppressionListAddressArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A object that represents a SuppressionList record.

        :param str resource_name: The name of the resource.
        :param SuppressionListAddressArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SuppressionListAddressArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_id: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 email_service_name: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 suppression_list_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SuppressionListAddressArgs.__new__(SuppressionListAddressArgs)

            __props__.__dict__["address_id"] = address_id
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            if email_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'email_service_name'")
            __props__.__dict__["email_service_name"] = email_service_name
            __props__.__dict__["first_name"] = first_name
            __props__.__dict__["last_name"] = last_name
            __props__.__dict__["notes"] = notes
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if suppression_list_name is None and not opts.urn:
                raise TypeError("Missing required property 'suppression_list_name'")
            __props__.__dict__["suppression_list_name"] = suppression_list_name
            __props__.__dict__["data_location"] = None
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:communication:SuppressionListAddress")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SuppressionListAddress, __self__).__init__(
            'azure-native:communication/v20230601preview:SuppressionListAddress',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SuppressionListAddress':
        """
        Get an existing SuppressionListAddress resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SuppressionListAddressArgs.__new__(SuppressionListAddressArgs)

        __props__.__dict__["data_location"] = None
        __props__.__dict__["email"] = None
        __props__.__dict__["first_name"] = None
        __props__.__dict__["last_modified"] = None
        __props__.__dict__["last_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SuppressionListAddress(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> pulumi.Output[str]:
        """
        The location where the SuppressionListAddress data is stored at rest. This value is inherited from the parent Domains resource.
        """
        return pulumi.get(self, "data_location")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        Email address of the recipient.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[Optional[str]]:
        """
        The first name of the email recipient.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The date the address was last updated in a suppression list.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[Optional[str]]:
        """
        The last name of the email recipient.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        An optional property to provide contextual notes or a description for an address.
        """
        return pulumi.get(self, "notes")

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

