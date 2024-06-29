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

__all__ = ['StorageTaskArgs', 'StorageTask']

@pulumi.input_type
class StorageTaskArgs:
    def __init__(__self__, *,
                 action: pulumi.Input['StorageTaskActionArgs'],
                 description: pulumi.Input[str],
                 enabled: pulumi.Input[bool],
                 identity: pulumi.Input['ManagedServiceIdentityArgs'],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 storage_task_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StorageTask resource.
        :param pulumi.Input['StorageTaskActionArgs'] action: The storage task action that is executed
        :param pulumi.Input[str] description: Text that describes the purpose of the storage task
        :param pulumi.Input[bool] enabled: Storage Task is enabled when set to true and disabled when set to false
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The managed service identity of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] storage_task_name: The name of the storage task within the specified resource group. Storage task names must be between 3 and 18 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "identity", identity)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if storage_task_name is not None:
            pulumi.set(__self__, "storage_task_name", storage_task_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input['StorageTaskActionArgs']:
        """
        The storage task action that is executed
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input['StorageTaskActionArgs']):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Text that describes the purpose of the storage task
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Storage Task is enabled when set to true and disabled when set to false
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Input['ManagedServiceIdentityArgs']:
        """
        The managed service identity of the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: pulumi.Input['ManagedServiceIdentityArgs']):
        pulumi.set(self, "identity", value)

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
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="storageTaskName")
    def storage_task_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the storage task within the specified resource group. Storage task names must be between 3 and 18 characters in length and use numbers and lower-case letters only.
        """
        return pulumi.get(self, "storage_task_name")

    @storage_task_name.setter
    def storage_task_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_task_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StorageTask(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['StorageTaskActionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_task_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents Storage Task.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['StorageTaskActionArgs']] action: The storage task action that is executed
        :param pulumi.Input[str] description: Text that describes the purpose of the storage task
        :param pulumi.Input[bool] enabled: Storage Task is enabled when set to true and disabled when set to false
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: The managed service identity of the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] storage_task_name: The name of the storage task within the specified resource group. Storage task names must be between 3 and 18 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageTaskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents Storage Task.

        :param str resource_name: The name of the resource.
        :param StorageTaskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageTaskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['StorageTaskActionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_task_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StorageTaskArgs.__new__(StorageTaskArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            if identity is None and not opts.urn:
                raise TypeError("Missing required property 'identity'")
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_task_name"] = storage_task_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time_in_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["task_version"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storageactions:StorageTask")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StorageTask, __self__).__init__(
            'azure-native:storageactions/v20230101:StorageTask',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageTask':
        """
        Get an existing StorageTask resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageTaskArgs.__new__(StorageTaskArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["creation_time_in_utc"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["task_version"] = None
        __props__.__dict__["type"] = None
        return StorageTask(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output['outputs.StorageTaskActionResponse']:
        """
        The storage task action that is executed
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="creationTimeInUtc")
    def creation_time_in_utc(self) -> pulumi.Output[str]:
        """
        The creation date and time of the storage task in UTC.
        """
        return pulumi.get(self, "creation_time_in_utc")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Text that describes the purpose of the storage task
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Storage Task is enabled when set to true and disabled when set to false
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.ManagedServiceIdentityResponse']:
        """
        The managed service identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

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
        Represents the provisioning state of the storage task.
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="taskVersion")
    def task_version(self) -> pulumi.Output[float]:
        """
        Storage task version.
        """
        return pulumi.get(self, "task_version")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

