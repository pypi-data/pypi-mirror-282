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

__all__ = ['ApplicationResourceArgs', 'ApplicationResource']

@pulumi.input_type
class ApplicationResourceArgs:
    def __init__(__self__, *,
                 application_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_id: pulumi.Input[str],
                 resource_type: pulumi.Input[str],
                 space_name: pulumi.Input[str],
                 resource_kind: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApplicationResource resource.
        :param pulumi.Input[str] application_name: The name of the Application
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_id: The Arm id of the application resource.
        :param pulumi.Input[str] resource_type: The type of the application resource.
        :param pulumi.Input[str] space_name: The name of the space
        :param pulumi.Input[str] resource_kind: The kind of the application resource.
        :param pulumi.Input[str] resource_name: The name of the application resource.
        """
        pulumi.set(__self__, "application_name", application_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "resource_type", resource_type)
        pulumi.set(__self__, "space_name", space_name)
        if resource_kind is not None:
            pulumi.set(__self__, "resource_kind", resource_kind)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> pulumi.Input[str]:
        """
        The name of the Application
        """
        return pulumi.get(self, "application_name")

    @application_name.setter
    def application_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_name", value)

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
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The Arm id of the application resource.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        The type of the application resource.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="spaceName")
    def space_name(self) -> pulumi.Input[str]:
        """
        The name of the space
        """
        return pulumi.get(self, "space_name")

    @space_name.setter
    def space_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "space_name", value)

    @property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[pulumi.Input[str]]:
        """
        The kind of the application resource.
        """
        return pulumi.get(self, "resource_kind")

    @resource_kind.setter
    def resource_kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_kind", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the application resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)


class ApplicationResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_kind: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 space_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A resource under application.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_name: The name of the Application
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_id: The Arm id of the application resource.
        :param pulumi.Input[str] resource_kind: The kind of the application resource.
        :param pulumi.Input[str] resource_name_: The name of the application resource.
        :param pulumi.Input[str] resource_type: The type of the application resource.
        :param pulumi.Input[str] space_name: The name of the space
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A resource under application.

        :param str resource_name: The name of the resource.
        :param ApplicationResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 resource_kind: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 space_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationResourceArgs.__new__(ApplicationResourceArgs)

            if application_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_name'")
            __props__.__dict__["application_name"] = application_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["resource_kind"] = resource_kind
            __props__.__dict__["resource_name"] = resource_name_
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            if space_name is None and not opts.urn:
                raise TypeError("Missing required property 'space_name'")
            __props__.__dict__["space_name"] = space_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:integrationspaces:ApplicationResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApplicationResource, __self__).__init__(
            'azure-native:integrationspaces/v20231114preview:ApplicationResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationResource':
        """
        Get an existing ApplicationResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationResourceArgs.__new__(ApplicationResourceArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["resource_kind"] = None
        __props__.__dict__["resource_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ApplicationResource(resource_name, opts=opts, __props__=__props__)

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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The Arm id of the application resource.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> pulumi.Output[Optional[str]]:
        """
        The kind of the application resource.
        """
        return pulumi.get(self, "resource_kind")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[str]:
        """
        The type of the application resource.
        """
        return pulumi.get(self, "resource_type")

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

