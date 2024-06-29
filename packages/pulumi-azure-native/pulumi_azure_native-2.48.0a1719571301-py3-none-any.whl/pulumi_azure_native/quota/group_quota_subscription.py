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

__all__ = ['GroupQuotaSubscriptionArgs', 'GroupQuotaSubscription']

@pulumi.input_type
class GroupQuotaSubscriptionArgs:
    def __init__(__self__, *,
                 group_quota_name: pulumi.Input[str],
                 management_group_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a GroupQuotaSubscription resource.
        :param pulumi.Input[str] group_quota_name: The GroupQuota name. The name should be unique for the provided context tenantId/MgId.
        :param pulumi.Input[str] management_group_id: Management Group Id.
        """
        pulumi.set(__self__, "group_quota_name", group_quota_name)
        pulumi.set(__self__, "management_group_id", management_group_id)

    @property
    @pulumi.getter(name="groupQuotaName")
    def group_quota_name(self) -> pulumi.Input[str]:
        """
        The GroupQuota name. The name should be unique for the provided context tenantId/MgId.
        """
        return pulumi.get(self, "group_quota_name")

    @group_quota_name.setter
    def group_quota_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_quota_name", value)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[str]:
        """
        Management Group Id.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "management_group_id", value)


class GroupQuotaSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_quota_name: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This represents a Azure subscriptionId that is associated with a GroupQuotasEntity.
        Azure REST API version: 2023-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_quota_name: The GroupQuota name. The name should be unique for the provided context tenantId/MgId.
        :param pulumi.Input[str] management_group_id: Management Group Id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupQuotaSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This represents a Azure subscriptionId that is associated with a GroupQuotasEntity.
        Azure REST API version: 2023-06-01-preview.

        :param str resource_name: The name of the resource.
        :param GroupQuotaSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupQuotaSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_quota_name: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupQuotaSubscriptionArgs.__new__(GroupQuotaSubscriptionArgs)

            if group_quota_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_quota_name'")
            __props__.__dict__["group_quota_name"] = group_quota_name
            if management_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'management_group_id'")
            __props__.__dict__["management_group_id"] = management_group_id
            __props__.__dict__["name"] = None
            __props__.__dict__["properties"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:quota/v20230601preview:GroupQuotaSubscription")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GroupQuotaSubscription, __self__).__init__(
            'azure-native:quota:GroupQuotaSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GroupQuotaSubscription':
        """
        Get an existing GroupQuotaSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GroupQuotaSubscriptionArgs.__new__(GroupQuotaSubscriptionArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return GroupQuotaSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.GroupQuotaSubscriptionIdResponseProperties']:
        return pulumi.get(self, "properties")

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

