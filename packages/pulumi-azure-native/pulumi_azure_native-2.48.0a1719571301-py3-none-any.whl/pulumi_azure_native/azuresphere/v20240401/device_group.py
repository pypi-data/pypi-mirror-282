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

__all__ = ['DeviceGroupArgs', 'DeviceGroup']

@pulumi.input_type
class DeviceGroupArgs:
    def __init__(__self__, *,
                 catalog_name: pulumi.Input[str],
                 product_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 allow_crash_dumps_collection: Optional[pulumi.Input[Union[str, 'AllowCrashDumpCollection']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_group_name: Optional[pulumi.Input[str]] = None,
                 os_feed_type: Optional[pulumi.Input[Union[str, 'OSFeedType']]] = None,
                 regional_data_boundary: Optional[pulumi.Input[Union[str, 'RegionalDataBoundary']]] = None,
                 update_policy: Optional[pulumi.Input[Union[str, 'UpdatePolicy']]] = None):
        """
        The set of arguments for constructing a DeviceGroup resource.
        :param pulumi.Input[str] catalog_name: Name of catalog
        :param pulumi.Input[str] product_name: Name of product.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'AllowCrashDumpCollection']] allow_crash_dumps_collection: Flag to define if the user allows for crash dump collection.
        :param pulumi.Input[str] description: Description of the device group.
        :param pulumi.Input[str] device_group_name: Name of device group.
        :param pulumi.Input[Union[str, 'OSFeedType']] os_feed_type: Operating system feed type of the device group.
        :param pulumi.Input[Union[str, 'RegionalDataBoundary']] regional_data_boundary: Regional data boundary for the device group.
        :param pulumi.Input[Union[str, 'UpdatePolicy']] update_policy: Update policy of the device group.
        """
        pulumi.set(__self__, "catalog_name", catalog_name)
        pulumi.set(__self__, "product_name", product_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if allow_crash_dumps_collection is not None:
            pulumi.set(__self__, "allow_crash_dumps_collection", allow_crash_dumps_collection)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_group_name is not None:
            pulumi.set(__self__, "device_group_name", device_group_name)
        if os_feed_type is not None:
            pulumi.set(__self__, "os_feed_type", os_feed_type)
        if regional_data_boundary is not None:
            pulumi.set(__self__, "regional_data_boundary", regional_data_boundary)
        if update_policy is not None:
            pulumi.set(__self__, "update_policy", update_policy)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> pulumi.Input[str]:
        """
        Name of catalog
        """
        return pulumi.get(self, "catalog_name")

    @catalog_name.setter
    def catalog_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "catalog_name", value)

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> pulumi.Input[str]:
        """
        Name of product.
        """
        return pulumi.get(self, "product_name")

    @product_name.setter
    def product_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "product_name", value)

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
    @pulumi.getter(name="allowCrashDumpsCollection")
    def allow_crash_dumps_collection(self) -> Optional[pulumi.Input[Union[str, 'AllowCrashDumpCollection']]]:
        """
        Flag to define if the user allows for crash dump collection.
        """
        return pulumi.get(self, "allow_crash_dumps_collection")

    @allow_crash_dumps_collection.setter
    def allow_crash_dumps_collection(self, value: Optional[pulumi.Input[Union[str, 'AllowCrashDumpCollection']]]):
        pulumi.set(self, "allow_crash_dumps_collection", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the device group.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceGroupName")
    def device_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of device group.
        """
        return pulumi.get(self, "device_group_name")

    @device_group_name.setter
    def device_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_group_name", value)

    @property
    @pulumi.getter(name="osFeedType")
    def os_feed_type(self) -> Optional[pulumi.Input[Union[str, 'OSFeedType']]]:
        """
        Operating system feed type of the device group.
        """
        return pulumi.get(self, "os_feed_type")

    @os_feed_type.setter
    def os_feed_type(self, value: Optional[pulumi.Input[Union[str, 'OSFeedType']]]):
        pulumi.set(self, "os_feed_type", value)

    @property
    @pulumi.getter(name="regionalDataBoundary")
    def regional_data_boundary(self) -> Optional[pulumi.Input[Union[str, 'RegionalDataBoundary']]]:
        """
        Regional data boundary for the device group.
        """
        return pulumi.get(self, "regional_data_boundary")

    @regional_data_boundary.setter
    def regional_data_boundary(self, value: Optional[pulumi.Input[Union[str, 'RegionalDataBoundary']]]):
        pulumi.set(self, "regional_data_boundary", value)

    @property
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> Optional[pulumi.Input[Union[str, 'UpdatePolicy']]]:
        """
        Update policy of the device group.
        """
        return pulumi.get(self, "update_policy")

    @update_policy.setter
    def update_policy(self, value: Optional[pulumi.Input[Union[str, 'UpdatePolicy']]]):
        pulumi.set(self, "update_policy", value)


class DeviceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_crash_dumps_collection: Optional[pulumi.Input[Union[str, 'AllowCrashDumpCollection']]] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_group_name: Optional[pulumi.Input[str]] = None,
                 os_feed_type: Optional[pulumi.Input[Union[str, 'OSFeedType']]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 regional_data_boundary: Optional[pulumi.Input[Union[str, 'RegionalDataBoundary']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 update_policy: Optional[pulumi.Input[Union[str, 'UpdatePolicy']]] = None,
                 __props__=None):
        """
        An device group resource belonging to a product resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'AllowCrashDumpCollection']] allow_crash_dumps_collection: Flag to define if the user allows for crash dump collection.
        :param pulumi.Input[str] catalog_name: Name of catalog
        :param pulumi.Input[str] description: Description of the device group.
        :param pulumi.Input[str] device_group_name: Name of device group.
        :param pulumi.Input[Union[str, 'OSFeedType']] os_feed_type: Operating system feed type of the device group.
        :param pulumi.Input[str] product_name: Name of product.
        :param pulumi.Input[Union[str, 'RegionalDataBoundary']] regional_data_boundary: Regional data boundary for the device group.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'UpdatePolicy']] update_policy: Update policy of the device group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeviceGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An device group resource belonging to a product resource.

        :param str resource_name: The name of the resource.
        :param DeviceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_crash_dumps_collection: Optional[pulumi.Input[Union[str, 'AllowCrashDumpCollection']]] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_group_name: Optional[pulumi.Input[str]] = None,
                 os_feed_type: Optional[pulumi.Input[Union[str, 'OSFeedType']]] = None,
                 product_name: Optional[pulumi.Input[str]] = None,
                 regional_data_boundary: Optional[pulumi.Input[Union[str, 'RegionalDataBoundary']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 update_policy: Optional[pulumi.Input[Union[str, 'UpdatePolicy']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeviceGroupArgs.__new__(DeviceGroupArgs)

            __props__.__dict__["allow_crash_dumps_collection"] = allow_crash_dumps_collection
            if catalog_name is None and not opts.urn:
                raise TypeError("Missing required property 'catalog_name'")
            __props__.__dict__["catalog_name"] = catalog_name
            __props__.__dict__["description"] = description
            __props__.__dict__["device_group_name"] = device_group_name
            __props__.__dict__["os_feed_type"] = os_feed_type
            if product_name is None and not opts.urn:
                raise TypeError("Missing required property 'product_name'")
            __props__.__dict__["product_name"] = product_name
            __props__.__dict__["regional_data_boundary"] = regional_data_boundary
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["update_policy"] = update_policy
            __props__.__dict__["has_deployment"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azuresphere:DeviceGroup"), pulumi.Alias(type_="azure-native:azuresphere/v20220901preview:DeviceGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DeviceGroup, __self__).__init__(
            'azure-native:azuresphere/v20240401:DeviceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeviceGroup':
        """
        Get an existing DeviceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeviceGroupArgs.__new__(DeviceGroupArgs)

        __props__.__dict__["allow_crash_dumps_collection"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["has_deployment"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["os_feed_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["regional_data_boundary"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["update_policy"] = None
        return DeviceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowCrashDumpsCollection")
    def allow_crash_dumps_collection(self) -> pulumi.Output[Optional[str]]:
        """
        Flag to define if the user allows for crash dump collection.
        """
        return pulumi.get(self, "allow_crash_dumps_collection")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the device group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hasDeployment")
    def has_deployment(self) -> pulumi.Output[bool]:
        """
        Deployment status for the device group.
        """
        return pulumi.get(self, "has_deployment")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osFeedType")
    def os_feed_type(self) -> pulumi.Output[Optional[str]]:
        """
        Operating system feed type of the device group.
        """
        return pulumi.get(self, "os_feed_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="regionalDataBoundary")
    def regional_data_boundary(self) -> pulumi.Output[Optional[str]]:
        """
        Regional data boundary for the device group.
        """
        return pulumi.get(self, "regional_data_boundary")

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
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> pulumi.Output[Optional[str]]:
        """
        Update policy of the device group.
        """
        return pulumi.get(self, "update_policy")

