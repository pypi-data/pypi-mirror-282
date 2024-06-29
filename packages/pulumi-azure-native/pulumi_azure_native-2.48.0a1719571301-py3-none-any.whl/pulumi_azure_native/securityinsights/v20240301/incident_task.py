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

__all__ = ['IncidentTaskArgs', 'IncidentTask']

@pulumi.input_type
class IncidentTaskArgs:
    def __init__(__self__, *,
                 incident_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 status: pulumi.Input[Union[str, 'IncidentTaskStatus']],
                 title: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 created_by: Optional[pulumi.Input['ClientInfoArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 incident_task_id: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input['ClientInfoArgs']] = None):
        """
        The set of arguments for constructing a IncidentTask resource.
        :param pulumi.Input[str] incident_id: Incident ID
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'IncidentTaskStatus']] status: The status of the task
        :param pulumi.Input[str] title: The title of the task
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input['ClientInfoArgs'] created_by: Information on the client (user or application) that made some action
        :param pulumi.Input[str] description: The description of the task
        :param pulumi.Input[str] incident_task_id: Incident task ID
        :param pulumi.Input['ClientInfoArgs'] last_modified_by: Information on the client (user or application) that made some action
        """
        pulumi.set(__self__, "incident_id", incident_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if incident_task_id is not None:
            pulumi.set(__self__, "incident_task_id", incident_task_id)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)

    @property
    @pulumi.getter(name="incidentId")
    def incident_id(self) -> pulumi.Input[str]:
        """
        Incident ID
        """
        return pulumi.get(self, "incident_id")

    @incident_id.setter
    def incident_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "incident_id", value)

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
    def status(self) -> pulumi.Input[Union[str, 'IncidentTaskStatus']]:
        """
        The status of the task
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[Union[str, 'IncidentTaskStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The title of the task
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input['ClientInfoArgs']]:
        """
        Information on the client (user or application) that made some action
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input['ClientInfoArgs']]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the task
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="incidentTaskId")
    def incident_task_id(self) -> Optional[pulumi.Input[str]]:
        """
        Incident task ID
        """
        return pulumi.get(self, "incident_task_id")

    @incident_task_id.setter
    def incident_task_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "incident_task_id", value)

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input['ClientInfoArgs']]:
        """
        Information on the client (user or application) that made some action
        """
        return pulumi.get(self, "last_modified_by")

    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input['ClientInfoArgs']]):
        pulumi.set(self, "last_modified_by", value)


class IncidentTask(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_by: Optional[pulumi.Input[pulumi.InputType['ClientInfoArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 incident_id: Optional[pulumi.Input[str]] = None,
                 incident_task_id: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[pulumi.InputType['ClientInfoArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'IncidentTaskStatus']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Describes incident task properties

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClientInfoArgs']] created_by: Information on the client (user or application) that made some action
        :param pulumi.Input[str] description: The description of the task
        :param pulumi.Input[str] incident_id: Incident ID
        :param pulumi.Input[str] incident_task_id: Incident task ID
        :param pulumi.Input[pulumi.InputType['ClientInfoArgs']] last_modified_by: Information on the client (user or application) that made some action
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'IncidentTaskStatus']] status: The status of the task
        :param pulumi.Input[str] title: The title of the task
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IncidentTaskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes incident task properties

        :param str resource_name: The name of the resource.
        :param IncidentTaskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IncidentTaskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_by: Optional[pulumi.Input[pulumi.InputType['ClientInfoArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 incident_id: Optional[pulumi.Input[str]] = None,
                 incident_task_id: Optional[pulumi.Input[str]] = None,
                 last_modified_by: Optional[pulumi.Input[pulumi.InputType['ClientInfoArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'IncidentTaskStatus']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IncidentTaskArgs.__new__(IncidentTaskArgs)

            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["description"] = description
            if incident_id is None and not opts.urn:
                raise TypeError("Missing required property 'incident_id'")
            __props__.__dict__["incident_id"] = incident_id
            __props__.__dict__["incident_task_id"] = incident_task_id
            __props__.__dict__["last_modified_by"] = last_modified_by
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["created_time_utc"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["last_modified_time_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:IncidentTask"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:IncidentTask")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IncidentTask, __self__).__init__(
            'azure-native:securityinsights/v20240301:IncidentTask',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IncidentTask':
        """
        Get an existing IncidentTask resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IncidentTaskArgs.__new__(IncidentTaskArgs)

        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_time_utc"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_time_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        return IncidentTask(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional['outputs.ClientInfoResponse']]:
        """
        Information on the client (user or application) that made some action
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[str]:
        """
        The time the task was created
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the task
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional['outputs.ClientInfoResponse']]:
        """
        Information on the client (user or application) that made some action
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> pulumi.Output[str]:
        """
        The last time the task was updated
        """
        return pulumi.get(self, "last_modified_time_utc")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the task
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the task
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

