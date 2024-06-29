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

__all__ = ['BlobContainerDataSetArgs', 'BlobContainerDataSet']

@pulumi.input_type
class BlobContainerDataSetArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 container_name: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 resource_group: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 share_name: pulumi.Input[str],
                 storage_account_name: pulumi.Input[str],
                 subscription_id: pulumi.Input[str],
                 data_set_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BlobContainerDataSet resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] container_name: BLOB Container name.
        :param pulumi.Input[str] kind: Kind of data set.
               Expected value is 'Container'.
        :param pulumi.Input[str] resource_group: Resource group of storage account
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_name: The name of the share to add the data set to.
        :param pulumi.Input[str] storage_account_name: Storage account name of the source data set
        :param pulumi.Input[str] subscription_id: Subscription id of storage account
        :param pulumi.Input[str] data_set_name: The name of the dataSet.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "container_name", container_name)
        pulumi.set(__self__, "kind", 'Container')
        pulumi.set(__self__, "resource_group", resource_group)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "share_name", share_name)
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        pulumi.set(__self__, "subscription_id", subscription_id)
        if data_set_name is not None:
            pulumi.set(__self__, "data_set_name", data_set_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the share account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[str]:
        """
        BLOB Container name.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Kind of data set.
        Expected value is 'Container'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Input[str]:
        """
        Resource group of storage account
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="shareName")
    def share_name(self) -> pulumi.Input[str]:
        """
        The name of the share to add the data set to.
        """
        return pulumi.get(self, "share_name")

    @share_name.setter
    def share_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "share_name", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Input[str]:
        """
        Storage account name of the source data set
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_name", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[str]:
        """
        Subscription id of storage account
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter(name="dataSetName")
    def data_set_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dataSet.
        """
        return pulumi.get(self, "data_set_name")

    @data_set_name.setter
    def data_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_set_name", value)


class BlobContainerDataSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 data_set_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure storage blob container data set.
        Azure REST API version: 2021-08-01. Prior API version in Azure Native 1.x: 2020-09-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] container_name: BLOB Container name.
        :param pulumi.Input[str] data_set_name: The name of the dataSet.
        :param pulumi.Input[str] kind: Kind of data set.
               Expected value is 'Container'.
        :param pulumi.Input[str] resource_group: Resource group of storage account
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_name: The name of the share to add the data set to.
        :param pulumi.Input[str] storage_account_name: Storage account name of the source data set
        :param pulumi.Input[str] subscription_id: Subscription id of storage account
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BlobContainerDataSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure storage blob container data set.
        Azure REST API version: 2021-08-01. Prior API version in Azure Native 1.x: 2020-09-01.

        :param str resource_name: The name of the resource.
        :param BlobContainerDataSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BlobContainerDataSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 data_set_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BlobContainerDataSetArgs.__new__(BlobContainerDataSetArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if container_name is None and not opts.urn:
                raise TypeError("Missing required property 'container_name'")
            __props__.__dict__["container_name"] = container_name
            __props__.__dict__["data_set_name"] = data_set_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'Container'
            if resource_group is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group'")
            __props__.__dict__["resource_group"] = resource_group
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if share_name is None and not opts.urn:
                raise TypeError("Missing required property 'share_name'")
            __props__.__dict__["share_name"] = share_name
            if storage_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_name'")
            __props__.__dict__["storage_account_name"] = storage_account_name
            if subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_id'")
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["data_set_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datashare/v20181101preview:BlobContainerDataSet"), pulumi.Alias(type_="azure-native:datashare/v20191101:BlobContainerDataSet"), pulumi.Alias(type_="azure-native:datashare/v20200901:BlobContainerDataSet"), pulumi.Alias(type_="azure-native:datashare/v20201001preview:BlobContainerDataSet"), pulumi.Alias(type_="azure-native:datashare/v20210801:BlobContainerDataSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BlobContainerDataSet, __self__).__init__(
            'azure-native:datashare:BlobContainerDataSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BlobContainerDataSet':
        """
        Get an existing BlobContainerDataSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BlobContainerDataSetArgs.__new__(BlobContainerDataSetArgs)

        __props__.__dict__["container_name"] = None
        __props__.__dict__["data_set_id"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["resource_group"] = None
        __props__.__dict__["storage_account_name"] = None
        __props__.__dict__["subscription_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return BlobContainerDataSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Output[str]:
        """
        BLOB Container name.
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Output[str]:
        """
        Unique id for identifying a data set resource
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of data set.
        Expected value is 'Container'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output[str]:
        """
        Resource group of storage account
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Output[str]:
        """
        Storage account name of the source data set
        """
        return pulumi.get(self, "storage_account_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[str]:
        """
        Subscription id of storage account
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

