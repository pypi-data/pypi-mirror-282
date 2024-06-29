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
from ._inputs import *

__all__ = ['AssignmentArgs', 'Assignment']

@pulumi.input_type
class AssignmentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 additional_data: Optional[pulumi.Input['AssignmentPropertiesAdditionalDataArgs']] = None,
                 assigned_component: Optional[pulumi.Input['AssignedComponentItemArgs']] = None,
                 assigned_standard: Optional[pulumi.Input['AssignedStandardItemArgs']] = None,
                 assignment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 effect: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Assignment resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input['AssignmentPropertiesAdditionalDataArgs'] additional_data: Additional data about the assignment
        :param pulumi.Input['AssignedComponentItemArgs'] assigned_component: Component item with key as applied to this standard assignment over the given scope
        :param pulumi.Input['AssignedStandardItemArgs'] assigned_standard: Standard item with key as applied to this standard assignment over the given scope
        :param pulumi.Input[str] assignment_id: The security assignment key - unique key for the standard assignment
        :param pulumi.Input[str] description: description of the standardAssignment
        :param pulumi.Input[str] display_name: display name of the standardAssignment
        :param pulumi.Input[str] effect: expected effect of this assignment (Disable/Exempt/etc)
        :param pulumi.Input[str] expires_on: Expiration date of this assignment as a full ISO date
        :param pulumi.Input[str] kind: Kind of the resource
        :param pulumi.Input[str] location: Location where the resource is stored
        :param Any metadata: The assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[str] scope: Scope to which the standardAssignment applies - can be a subscription path or a resource group under that subscription
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A list of key value pairs that describe the resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if additional_data is not None:
            pulumi.set(__self__, "additional_data", additional_data)
        if assigned_component is not None:
            pulumi.set(__self__, "assigned_component", assigned_component)
        if assigned_standard is not None:
            pulumi.set(__self__, "assigned_standard", assigned_standard)
        if assignment_id is not None:
            pulumi.set(__self__, "assignment_id", assignment_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if effect is not None:
            pulumi.set(__self__, "effect", effect)
        if expires_on is not None:
            pulumi.set(__self__, "expires_on", expires_on)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> Optional[pulumi.Input['AssignmentPropertiesAdditionalDataArgs']]:
        """
        Additional data about the assignment
        """
        return pulumi.get(self, "additional_data")

    @additional_data.setter
    def additional_data(self, value: Optional[pulumi.Input['AssignmentPropertiesAdditionalDataArgs']]):
        pulumi.set(self, "additional_data", value)

    @property
    @pulumi.getter(name="assignedComponent")
    def assigned_component(self) -> Optional[pulumi.Input['AssignedComponentItemArgs']]:
        """
        Component item with key as applied to this standard assignment over the given scope
        """
        return pulumi.get(self, "assigned_component")

    @assigned_component.setter
    def assigned_component(self, value: Optional[pulumi.Input['AssignedComponentItemArgs']]):
        pulumi.set(self, "assigned_component", value)

    @property
    @pulumi.getter(name="assignedStandard")
    def assigned_standard(self) -> Optional[pulumi.Input['AssignedStandardItemArgs']]:
        """
        Standard item with key as applied to this standard assignment over the given scope
        """
        return pulumi.get(self, "assigned_standard")

    @assigned_standard.setter
    def assigned_standard(self, value: Optional[pulumi.Input['AssignedStandardItemArgs']]):
        pulumi.set(self, "assigned_standard", value)

    @property
    @pulumi.getter(name="assignmentId")
    def assignment_id(self) -> Optional[pulumi.Input[str]]:
        """
        The security assignment key - unique key for the standard assignment
        """
        return pulumi.get(self, "assignment_id")

    @assignment_id.setter
    def assignment_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assignment_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        description of the standardAssignment
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        display name of the standardAssignment
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def effect(self) -> Optional[pulumi.Input[str]]:
        """
        expected effect of this assignment (Disable/Exempt/etc)
        """
        return pulumi.get(self, "effect")

    @effect.setter
    def effect(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "effect", value)

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration date of this assignment as a full ISO date
        """
        return pulumi.get(self, "expires_on")

    @expires_on.setter
    def expires_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_on", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location where the resource is stored
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        Scope to which the standardAssignment applies - can be a subscription path or a resource group under that subscription
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A list of key value pairs that describe the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Assignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_data: Optional[pulumi.Input[pulumi.InputType['AssignmentPropertiesAdditionalDataArgs']]] = None,
                 assigned_component: Optional[pulumi.Input[pulumi.InputType['AssignedComponentItemArgs']]] = None,
                 assigned_standard: Optional[pulumi.Input[pulumi.InputType['AssignedStandardItemArgs']]] = None,
                 assignment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 effect: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Security Assignment on a resource group over a given scope
        Azure REST API version: 2021-08-01-preview. Prior API version in Azure Native 1.x: 2021-08-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AssignmentPropertiesAdditionalDataArgs']] additional_data: Additional data about the assignment
        :param pulumi.Input[pulumi.InputType['AssignedComponentItemArgs']] assigned_component: Component item with key as applied to this standard assignment over the given scope
        :param pulumi.Input[pulumi.InputType['AssignedStandardItemArgs']] assigned_standard: Standard item with key as applied to this standard assignment over the given scope
        :param pulumi.Input[str] assignment_id: The security assignment key - unique key for the standard assignment
        :param pulumi.Input[str] description: description of the standardAssignment
        :param pulumi.Input[str] display_name: display name of the standardAssignment
        :param pulumi.Input[str] effect: expected effect of this assignment (Disable/Exempt/etc)
        :param pulumi.Input[str] expires_on: Expiration date of this assignment as a full ISO date
        :param pulumi.Input[str] kind: Kind of the resource
        :param pulumi.Input[str] location: Location where the resource is stored
        :param Any metadata: The assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] scope: Scope to which the standardAssignment applies - can be a subscription path or a resource group under that subscription
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A list of key value pairs that describe the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Security Assignment on a resource group over a given scope
        Azure REST API version: 2021-08-01-preview. Prior API version in Azure Native 1.x: 2021-08-01-preview.

        :param str resource_name: The name of the resource.
        :param AssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_data: Optional[pulumi.Input[pulumi.InputType['AssignmentPropertiesAdditionalDataArgs']]] = None,
                 assigned_component: Optional[pulumi.Input[pulumi.InputType['AssignedComponentItemArgs']]] = None,
                 assigned_standard: Optional[pulumi.Input[pulumi.InputType['AssignedStandardItemArgs']]] = None,
                 assignment_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 effect: Optional[pulumi.Input[str]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssignmentArgs.__new__(AssignmentArgs)

            __props__.__dict__["additional_data"] = additional_data
            __props__.__dict__["assigned_component"] = assigned_component
            __props__.__dict__["assigned_standard"] = assigned_standard
            __props__.__dict__["assignment_id"] = assignment_id
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["effect"] = effect
            __props__.__dict__["expires_on"] = expires_on
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scope"] = scope
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security/v20210801preview:Assignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Assignment, __self__).__init__(
            'azure-native:security:Assignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Assignment':
        """
        Get an existing Assignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssignmentArgs.__new__(AssignmentArgs)

        __props__.__dict__["additional_data"] = None
        __props__.__dict__["assigned_component"] = None
        __props__.__dict__["assigned_standard"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["effect"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["expires_on"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Assignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> pulumi.Output[Optional['outputs.AssignmentPropertiesResponseAdditionalData']]:
        """
        Additional data about the assignment
        """
        return pulumi.get(self, "additional_data")

    @property
    @pulumi.getter(name="assignedComponent")
    def assigned_component(self) -> pulumi.Output[Optional['outputs.AssignedComponentItemResponse']]:
        """
        Component item with key as applied to this standard assignment over the given scope
        """
        return pulumi.get(self, "assigned_component")

    @property
    @pulumi.getter(name="assignedStandard")
    def assigned_standard(self) -> pulumi.Output[Optional['outputs.AssignedStandardItemResponse']]:
        """
        Standard item with key as applied to this standard assignment over the given scope
        """
        return pulumi.get(self, "assigned_standard")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        description of the standardAssignment
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        display name of the standardAssignment
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def effect(self) -> pulumi.Output[Optional[str]]:
        """
        expected effect of this assignment (Disable/Exempt/etc)
        """
        return pulumi.get(self, "effect")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Entity tag is used for comparing two or more entities from the same requested resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> pulumi.Output[Optional[str]]:
        """
        Expiration date of this assignment as a full ISO date
        """
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Location where the resource is stored
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        Scope to which the standardAssignment applies - can be a subscription path or a resource group under that subscription
        """
        return pulumi.get(self, "scope")

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
        A list of key value pairs that describe the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

