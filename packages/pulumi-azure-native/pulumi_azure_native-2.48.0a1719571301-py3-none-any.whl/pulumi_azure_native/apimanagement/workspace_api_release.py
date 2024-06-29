# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WorkspaceApiReleaseArgs', 'WorkspaceApiRelease']

@pulumi.input_type
class WorkspaceApiReleaseArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 workspace_id: pulumi.Input[str],
                 notes: Optional[pulumi.Input[str]] = None,
                 release_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceApiRelease resource.
        :param pulumi.Input[str] api_id: Identifier of the API the release belongs to.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] notes: Release Notes
        :param pulumi.Input[str] release_id: Release identifier within an API. Must be unique in the current API Management service instance.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if release_id is not None:
            pulumi.set(__self__, "release_id", release_id)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        Identifier of the API the release belongs to.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

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
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        Release Notes
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter(name="releaseId")
    def release_id(self) -> Optional[pulumi.Input[str]]:
        """
        Release identifier within an API. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "release_id")

    @release_id.setter
    def release_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "release_id", value)


class WorkspaceApiRelease(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 release_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ApiRelease details.
        Azure REST API version: 2022-09-01-preview.

        Other available API versions: 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: Identifier of the API the release belongs to.
        :param pulumi.Input[str] notes: Release Notes
        :param pulumi.Input[str] release_id: Release identifier within an API. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceApiReleaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ApiRelease details.
        Azure REST API version: 2022-09-01-preview.

        Other available API versions: 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param WorkspaceApiReleaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceApiReleaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 release_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceApiReleaseArgs.__new__(WorkspaceApiReleaseArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["notes"] = notes
            __props__.__dict__["release_id"] = release_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["created_date_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_date_time"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:WorkspaceApiRelease"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:WorkspaceApiRelease"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:WorkspaceApiRelease"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:WorkspaceApiRelease")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceApiRelease, __self__).__init__(
            'azure-native:apimanagement:WorkspaceApiRelease',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceApiRelease':
        """
        Get an existing WorkspaceApiRelease resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceApiReleaseArgs.__new__(WorkspaceApiReleaseArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["created_date_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_date_time"] = None
        return WorkspaceApiRelease(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[Optional[str]]:
        """
        Identifier of the API the release belongs to.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> pulumi.Output[str]:
        """
        The time the API was released. The date conforms to the following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "created_date_time")

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
        Release Notes
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedDateTime")
    def updated_date_time(self) -> pulumi.Output[str]:
        """
        The time the API release was updated.
        """
        return pulumi.get(self, "updated_date_time")

