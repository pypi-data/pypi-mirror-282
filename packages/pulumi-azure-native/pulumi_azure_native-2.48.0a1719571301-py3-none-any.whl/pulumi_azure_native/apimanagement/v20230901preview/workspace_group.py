# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['WorkspaceGroupArgs', 'WorkspaceGroup']

@pulumi.input_type
class WorkspaceGroupArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 workspace_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['GroupType']] = None):
        """
        The set of arguments for constructing a WorkspaceGroup resource.
        :param pulumi.Input[str] display_name: Group name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] description: Group description.
        :param pulumi.Input[str] external_id: Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.
        :param pulumi.Input[str] group_id: Group identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input['GroupType'] type: Group type.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Group name.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        Workspace identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Group description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Group identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['GroupType']]:
        """
        Group type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['GroupType']]):
        pulumi.set(self, "type", value)


class WorkspaceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['GroupType']] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Contract details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Group description.
        :param pulumi.Input[str] display_name: Group name.
        :param pulumi.Input[str] external_id: Identifier of the external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.
        :param pulumi.Input[str] group_id: Group identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input['GroupType'] type: Group type.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Contract details.

        :param str resource_name: The name of the resource.
        :param WorkspaceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 external_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['GroupType']] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceGroupArgs.__new__(WorkspaceGroupArgs)

            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["external_id"] = external_id
            __props__.__dict__["group_id"] = group_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["type"] = type
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["built_in"] = None
            __props__.__dict__["name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:WorkspaceGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:WorkspaceGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:WorkspaceGroup"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:WorkspaceGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceGroup, __self__).__init__(
            'azure-native:apimanagement/v20230901preview:WorkspaceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceGroup':
        """
        Get an existing WorkspaceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceGroupArgs.__new__(WorkspaceGroupArgs)

        __props__.__dict__["built_in"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["external_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return WorkspaceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="builtIn")
    def built_in(self) -> pulumi.Output[bool]:
        """
        true if the group is one of the three system groups (Administrators, Developers, or Guests); otherwise false.
        """
        return pulumi.get(self, "built_in")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Group description. Can contain HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Group name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[Optional[str]]:
        """
        For external groups, this property contains the id of the group from the external identity provider, e.g. for Azure Active Directory `aad://<tenant>.onmicrosoft.com/groups/<group object id>`; otherwise the value is null.
        """
        return pulumi.get(self, "external_id")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

