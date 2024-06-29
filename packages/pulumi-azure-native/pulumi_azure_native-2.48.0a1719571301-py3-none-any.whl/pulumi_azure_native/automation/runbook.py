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
from ._enums import *
from ._inputs import *

__all__ = ['RunbookArgs', 'Runbook']

@pulumi.input_type
class RunbookArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 runbook_type: pulumi.Input[Union[str, 'RunbookTypeEnum']],
                 description: Optional[pulumi.Input[str]] = None,
                 draft: Optional[pulumi.Input['RunbookDraftArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 log_activity_trace: Optional[pulumi.Input[int]] = None,
                 log_progress: Optional[pulumi.Input[bool]] = None,
                 log_verbose: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 publish_content_link: Optional[pulumi.Input['ContentLinkArgs']] = None,
                 runbook_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Runbook resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[Union[str, 'RunbookTypeEnum']] runbook_type: Gets or sets the type of the runbook.
        :param pulumi.Input[str] description: Gets or sets the description of the runbook.
        :param pulumi.Input['RunbookDraftArgs'] draft: Gets or sets the draft runbook properties.
        :param pulumi.Input[str] location: Gets or sets the location of the resource.
        :param pulumi.Input[int] log_activity_trace: Gets or sets the activity-level tracing options of the runbook.
        :param pulumi.Input[bool] log_progress: Gets or sets progress log option.
        :param pulumi.Input[bool] log_verbose: Gets or sets verbose log option.
        :param pulumi.Input[str] name: Gets or sets the name of the resource.
        :param pulumi.Input['ContentLinkArgs'] publish_content_link: Gets or sets the published runbook content link.
        :param pulumi.Input[str] runbook_name: The runbook name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the tags attached to the resource.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "runbook_type", runbook_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if draft is not None:
            pulumi.set(__self__, "draft", draft)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if log_activity_trace is not None:
            pulumi.set(__self__, "log_activity_trace", log_activity_trace)
        if log_progress is not None:
            pulumi.set(__self__, "log_progress", log_progress)
        if log_verbose is not None:
            pulumi.set(__self__, "log_verbose", log_verbose)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if publish_content_link is not None:
            pulumi.set(__self__, "publish_content_link", publish_content_link)
        if runbook_name is not None:
            pulumi.set(__self__, "runbook_name", runbook_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="runbookType")
    def runbook_type(self) -> pulumi.Input[Union[str, 'RunbookTypeEnum']]:
        """
        Gets or sets the type of the runbook.
        """
        return pulumi.get(self, "runbook_type")

    @runbook_type.setter
    def runbook_type(self, value: pulumi.Input[Union[str, 'RunbookTypeEnum']]):
        pulumi.set(self, "runbook_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the description of the runbook.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def draft(self) -> Optional[pulumi.Input['RunbookDraftArgs']]:
        """
        Gets or sets the draft runbook properties.
        """
        return pulumi.get(self, "draft")

    @draft.setter
    def draft(self, value: Optional[pulumi.Input['RunbookDraftArgs']]):
        pulumi.set(self, "draft", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="logActivityTrace")
    def log_activity_trace(self) -> Optional[pulumi.Input[int]]:
        """
        Gets or sets the activity-level tracing options of the runbook.
        """
        return pulumi.get(self, "log_activity_trace")

    @log_activity_trace.setter
    def log_activity_trace(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "log_activity_trace", value)

    @property
    @pulumi.getter(name="logProgress")
    def log_progress(self) -> Optional[pulumi.Input[bool]]:
        """
        Gets or sets progress log option.
        """
        return pulumi.get(self, "log_progress")

    @log_progress.setter
    def log_progress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "log_progress", value)

    @property
    @pulumi.getter(name="logVerbose")
    def log_verbose(self) -> Optional[pulumi.Input[bool]]:
        """
        Gets or sets verbose log option.
        """
        return pulumi.get(self, "log_verbose")

    @log_verbose.setter
    def log_verbose(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "log_verbose", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publishContentLink")
    def publish_content_link(self) -> Optional[pulumi.Input['ContentLinkArgs']]:
        """
        Gets or sets the published runbook content link.
        """
        return pulumi.get(self, "publish_content_link")

    @publish_content_link.setter
    def publish_content_link(self, value: Optional[pulumi.Input['ContentLinkArgs']]):
        pulumi.set(self, "publish_content_link", value)

    @property
    @pulumi.getter(name="runbookName")
    def runbook_name(self) -> Optional[pulumi.Input[str]]:
        """
        The runbook name.
        """
        return pulumi.get(self, "runbook_name")

    @runbook_name.setter
    def runbook_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "runbook_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the tags attached to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Runbook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 draft: Optional[pulumi.Input[pulumi.InputType['RunbookDraftArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 log_activity_trace: Optional[pulumi.Input[int]] = None,
                 log_progress: Optional[pulumi.Input[bool]] = None,
                 log_verbose: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 publish_content_link: Optional[pulumi.Input[pulumi.InputType['ContentLinkArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 runbook_name: Optional[pulumi.Input[str]] = None,
                 runbook_type: Optional[pulumi.Input[Union[str, 'RunbookTypeEnum']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Definition of the runbook type.
        Azure REST API version: 2022-08-08. Prior API version in Azure Native 1.x: 2019-06-01.

        Other available API versions: 2023-05-15-preview, 2023-11-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] description: Gets or sets the description of the runbook.
        :param pulumi.Input[pulumi.InputType['RunbookDraftArgs']] draft: Gets or sets the draft runbook properties.
        :param pulumi.Input[str] location: Gets or sets the location of the resource.
        :param pulumi.Input[int] log_activity_trace: Gets or sets the activity-level tracing options of the runbook.
        :param pulumi.Input[bool] log_progress: Gets or sets progress log option.
        :param pulumi.Input[bool] log_verbose: Gets or sets verbose log option.
        :param pulumi.Input[str] name: Gets or sets the name of the resource.
        :param pulumi.Input[pulumi.InputType['ContentLinkArgs']] publish_content_link: Gets or sets the published runbook content link.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[str] runbook_name: The runbook name.
        :param pulumi.Input[Union[str, 'RunbookTypeEnum']] runbook_type: Gets or sets the type of the runbook.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the tags attached to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RunbookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the runbook type.
        Azure REST API version: 2022-08-08. Prior API version in Azure Native 1.x: 2019-06-01.

        Other available API versions: 2023-05-15-preview, 2023-11-01.

        :param str resource_name: The name of the resource.
        :param RunbookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RunbookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 draft: Optional[pulumi.Input[pulumi.InputType['RunbookDraftArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 log_activity_trace: Optional[pulumi.Input[int]] = None,
                 log_progress: Optional[pulumi.Input[bool]] = None,
                 log_verbose: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 publish_content_link: Optional[pulumi.Input[pulumi.InputType['ContentLinkArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 runbook_name: Optional[pulumi.Input[str]] = None,
                 runbook_type: Optional[pulumi.Input[Union[str, 'RunbookTypeEnum']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RunbookArgs.__new__(RunbookArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["description"] = description
            __props__.__dict__["draft"] = draft
            __props__.__dict__["location"] = location
            __props__.__dict__["log_activity_trace"] = log_activity_trace
            __props__.__dict__["log_progress"] = log_progress
            __props__.__dict__["log_verbose"] = log_verbose
            __props__.__dict__["name"] = name
            __props__.__dict__["publish_content_link"] = publish_content_link
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["runbook_name"] = runbook_name
            if runbook_type is None and not opts.urn:
                raise TypeError("Missing required property 'runbook_type'")
            __props__.__dict__["runbook_type"] = runbook_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["job_count"] = None
            __props__.__dict__["last_modified_by"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["output_types"] = None
            __props__.__dict__["parameters"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automation/v20151031:Runbook"), pulumi.Alias(type_="azure-native:automation/v20180630:Runbook"), pulumi.Alias(type_="azure-native:automation/v20190601:Runbook"), pulumi.Alias(type_="azure-native:automation/v20220808:Runbook"), pulumi.Alias(type_="azure-native:automation/v20230515preview:Runbook"), pulumi.Alias(type_="azure-native:automation/v20231101:Runbook")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Runbook, __self__).__init__(
            'azure-native:automation:Runbook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Runbook':
        """
        Get an existing Runbook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RunbookArgs.__new__(RunbookArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["draft"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["job_count"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["log_activity_trace"] = None
        __props__.__dict__["log_progress"] = None
        __props__.__dict__["log_verbose"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["output_types"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["publish_content_link"] = None
        __props__.__dict__["runbook_type"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Runbook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def draft(self) -> pulumi.Output[Optional['outputs.RunbookDraftResponse']]:
        """
        Gets or sets the draft runbook properties.
        """
        return pulumi.get(self, "draft")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the etag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="jobCount")
    def job_count(self) -> pulumi.Output[Optional[int]]:
        """
        Gets or sets the job count of the runbook.
        """
        return pulumi.get(self, "job_count")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last modified by.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure Region where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logActivityTrace")
    def log_activity_trace(self) -> pulumi.Output[Optional[int]]:
        """
        Gets or sets the option to log activity trace of the runbook.
        """
        return pulumi.get(self, "log_activity_trace")

    @property
    @pulumi.getter(name="logProgress")
    def log_progress(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets progress log option.
        """
        return pulumi.get(self, "log_progress")

    @property
    @pulumi.getter(name="logVerbose")
    def log_verbose(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets verbose log option.
        """
        return pulumi.get(self, "log_verbose")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputTypes")
    def output_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Gets or sets the runbook output types.
        """
        return pulumi.get(self, "output_types")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.RunbookParameterResponse']]]:
        """
        Gets or sets the runbook parameters.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the provisioning state of the runbook.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publishContentLink")
    def publish_content_link(self) -> pulumi.Output[Optional['outputs.ContentLinkResponse']]:
        """
        Gets or sets the published runbook content link.
        """
        return pulumi.get(self, "publish_content_link")

    @property
    @pulumi.getter(name="runbookType")
    def runbook_type(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the type of the runbook.
        """
        return pulumi.get(self, "runbook_type")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the state of the runbook.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

