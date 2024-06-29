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
from ._inputs import *

__all__ = ['SourceControlArgs', 'SourceControl']

@pulumi.input_type
class SourceControlArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auto_sync: Optional[pulumi.Input[bool]] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder_path: Optional[pulumi.Input[str]] = None,
                 publish_runbook: Optional[pulumi.Input[bool]] = None,
                 repo_url: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input['SourceControlSecurityTokenPropertiesArgs']] = None,
                 source_control_name: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[Union[str, 'SourceType']]] = None):
        """
        The set of arguments for constructing a SourceControl resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[bool] auto_sync: The auto async of the source control. Default is false.
        :param pulumi.Input[str] branch: The repo branch of the source control. Include branch as empty string for VsoTfvc.
        :param pulumi.Input[str] description: The user description of the source control.
        :param pulumi.Input[str] folder_path: The folder path of the source control. Path must be relative.
        :param pulumi.Input[bool] publish_runbook: The auto publish of the source control. Default is true.
        :param pulumi.Input[str] repo_url: The repo url of the source control.
        :param pulumi.Input['SourceControlSecurityTokenPropertiesArgs'] security_token: The authorization token for the repo of the source control.
        :param pulumi.Input[str] source_control_name: The source control name.
        :param pulumi.Input[Union[str, 'SourceType']] source_type: The source type. Must be one of VsoGit, VsoTfvc, GitHub, case sensitive.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_sync is not None:
            pulumi.set(__self__, "auto_sync", auto_sync)
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if folder_path is not None:
            pulumi.set(__self__, "folder_path", folder_path)
        if publish_runbook is not None:
            pulumi.set(__self__, "publish_runbook", publish_runbook)
        if repo_url is not None:
            pulumi.set(__self__, "repo_url", repo_url)
        if security_token is not None:
            pulumi.set(__self__, "security_token", security_token)
        if source_control_name is not None:
            pulumi.set(__self__, "source_control_name", source_control_name)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)

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
    @pulumi.getter(name="autoSync")
    def auto_sync(self) -> Optional[pulumi.Input[bool]]:
        """
        The auto async of the source control. Default is false.
        """
        return pulumi.get(self, "auto_sync")

    @auto_sync.setter
    def auto_sync(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_sync", value)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        The repo branch of the source control. Include branch as empty string for VsoTfvc.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The user description of the source control.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[pulumi.Input[str]]:
        """
        The folder path of the source control. Path must be relative.
        """
        return pulumi.get(self, "folder_path")

    @folder_path.setter
    def folder_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_path", value)

    @property
    @pulumi.getter(name="publishRunbook")
    def publish_runbook(self) -> Optional[pulumi.Input[bool]]:
        """
        The auto publish of the source control. Default is true.
        """
        return pulumi.get(self, "publish_runbook")

    @publish_runbook.setter
    def publish_runbook(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "publish_runbook", value)

    @property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[pulumi.Input[str]]:
        """
        The repo url of the source control.
        """
        return pulumi.get(self, "repo_url")

    @repo_url.setter
    def repo_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_url", value)

    @property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[pulumi.Input['SourceControlSecurityTokenPropertiesArgs']]:
        """
        The authorization token for the repo of the source control.
        """
        return pulumi.get(self, "security_token")

    @security_token.setter
    def security_token(self, value: Optional[pulumi.Input['SourceControlSecurityTokenPropertiesArgs']]):
        pulumi.set(self, "security_token", value)

    @property
    @pulumi.getter(name="sourceControlName")
    def source_control_name(self) -> Optional[pulumi.Input[str]]:
        """
        The source control name.
        """
        return pulumi.get(self, "source_control_name")

    @source_control_name.setter
    def source_control_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_control_name", value)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[pulumi.Input[Union[str, 'SourceType']]]:
        """
        The source type. Must be one of VsoGit, VsoTfvc, GitHub, case sensitive.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: Optional[pulumi.Input[Union[str, 'SourceType']]]):
        pulumi.set(self, "source_type", value)


class SourceControl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_sync: Optional[pulumi.Input[bool]] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder_path: Optional[pulumi.Input[str]] = None,
                 publish_runbook: Optional[pulumi.Input[bool]] = None,
                 repo_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[pulumi.InputType['SourceControlSecurityTokenPropertiesArgs']]] = None,
                 source_control_name: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[Union[str, 'SourceType']]] = None,
                 __props__=None):
        """
        Definition of the source control.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_sync: The auto async of the source control. Default is false.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] branch: The repo branch of the source control. Include branch as empty string for VsoTfvc.
        :param pulumi.Input[str] description: The user description of the source control.
        :param pulumi.Input[str] folder_path: The folder path of the source control. Path must be relative.
        :param pulumi.Input[bool] publish_runbook: The auto publish of the source control. Default is true.
        :param pulumi.Input[str] repo_url: The repo url of the source control.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[pulumi.InputType['SourceControlSecurityTokenPropertiesArgs']] security_token: The authorization token for the repo of the source control.
        :param pulumi.Input[str] source_control_name: The source control name.
        :param pulumi.Input[Union[str, 'SourceType']] source_type: The source type. Must be one of VsoGit, VsoTfvc, GitHub, case sensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SourceControlArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the source control.

        :param str resource_name: The name of the resource.
        :param SourceControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SourceControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_sync: Optional[pulumi.Input[bool]] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 folder_path: Optional[pulumi.Input[str]] = None,
                 publish_runbook: Optional[pulumi.Input[bool]] = None,
                 repo_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[pulumi.InputType['SourceControlSecurityTokenPropertiesArgs']]] = None,
                 source_control_name: Optional[pulumi.Input[str]] = None,
                 source_type: Optional[pulumi.Input[Union[str, 'SourceType']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SourceControlArgs.__new__(SourceControlArgs)

            __props__.__dict__["auto_sync"] = auto_sync
            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["branch"] = branch
            __props__.__dict__["description"] = description
            __props__.__dict__["folder_path"] = folder_path
            __props__.__dict__["publish_runbook"] = publish_runbook
            __props__.__dict__["repo_url"] = repo_url
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["security_token"] = security_token
            __props__.__dict__["source_control_name"] = source_control_name
            __props__.__dict__["source_type"] = source_type
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automation:SourceControl"), pulumi.Alias(type_="azure-native:automation/v20170515preview:SourceControl"), pulumi.Alias(type_="azure-native:automation/v20190601:SourceControl"), pulumi.Alias(type_="azure-native:automation/v20200113preview:SourceControl"), pulumi.Alias(type_="azure-native:automation/v20230515preview:SourceControl"), pulumi.Alias(type_="azure-native:automation/v20231101:SourceControl")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SourceControl, __self__).__init__(
            'azure-native:automation/v20220808:SourceControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SourceControl':
        """
        Get an existing SourceControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SourceControlArgs.__new__(SourceControlArgs)

        __props__.__dict__["auto_sync"] = None
        __props__.__dict__["branch"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["folder_path"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["publish_runbook"] = None
        __props__.__dict__["repo_url"] = None
        __props__.__dict__["source_type"] = None
        __props__.__dict__["type"] = None
        return SourceControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoSync")
    def auto_sync(self) -> pulumi.Output[Optional[bool]]:
        """
        The auto sync of the source control. Default is false.
        """
        return pulumi.get(self, "auto_sync")

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Output[Optional[str]]:
        """
        The repo branch of the source control. Include branch as empty string for VsoTfvc.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        The creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> pulumi.Output[Optional[str]]:
        """
        The folder path of the source control.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        The last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publishRunbook")
    def publish_runbook(self) -> pulumi.Output[Optional[bool]]:
        """
        The auto publish of the source control. Default is true.
        """
        return pulumi.get(self, "publish_runbook")

    @property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> pulumi.Output[Optional[str]]:
        """
        The repo url of the source control.
        """
        return pulumi.get(self, "repo_url")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Output[Optional[str]]:
        """
        The source type. Must be one of VsoGit, VsoTfvc, GitHub.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

