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
from ._inputs import *

__all__ = ['ContainerAppsSourceControlArgs', 'ContainerAppsSourceControl']

@pulumi.input_type
class ContainerAppsSourceControlArgs:
    def __init__(__self__, *,
                 container_app_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 branch: Optional[pulumi.Input[str]] = None,
                 github_action_configuration: Optional[pulumi.Input['GithubActionConfigurationArgs']] = None,
                 repo_url: Optional[pulumi.Input[str]] = None,
                 source_control_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ContainerAppsSourceControl resource.
        :param pulumi.Input[str] container_app_name: Name of the Container App.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] branch: The branch which will trigger the auto deployment
        :param pulumi.Input['GithubActionConfigurationArgs'] github_action_configuration: Container App Revision Template with all possible settings and the
               defaults if user did not provide them. The defaults are populated
               as they were at the creation time
        :param pulumi.Input[str] repo_url: The repo url which will be integrated to ContainerApp.
        :param pulumi.Input[str] source_control_name: Name of the Container App SourceControl.
        """
        pulumi.set(__self__, "container_app_name", container_app_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if github_action_configuration is not None:
            pulumi.set(__self__, "github_action_configuration", github_action_configuration)
        if repo_url is not None:
            pulumi.set(__self__, "repo_url", repo_url)
        if source_control_name is not None:
            pulumi.set(__self__, "source_control_name", source_control_name)

    @property
    @pulumi.getter(name="containerAppName")
    def container_app_name(self) -> pulumi.Input[str]:
        """
        Name of the Container App.
        """
        return pulumi.get(self, "container_app_name")

    @container_app_name.setter
    def container_app_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_app_name", value)

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
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        The branch which will trigger the auto deployment
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="githubActionConfiguration")
    def github_action_configuration(self) -> Optional[pulumi.Input['GithubActionConfigurationArgs']]:
        """
        Container App Revision Template with all possible settings and the
        defaults if user did not provide them. The defaults are populated
        as they were at the creation time
        """
        return pulumi.get(self, "github_action_configuration")

    @github_action_configuration.setter
    def github_action_configuration(self, value: Optional[pulumi.Input['GithubActionConfigurationArgs']]):
        pulumi.set(self, "github_action_configuration", value)

    @property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> Optional[pulumi.Input[str]]:
        """
        The repo url which will be integrated to ContainerApp.
        """
        return pulumi.get(self, "repo_url")

    @repo_url.setter
    def repo_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_url", value)

    @property
    @pulumi.getter(name="sourceControlName")
    def source_control_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Container App SourceControl.
        """
        return pulumi.get(self, "source_control_name")

    @source_control_name.setter
    def source_control_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_control_name", value)


class ContainerAppsSourceControl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 container_app_name: Optional[pulumi.Input[str]] = None,
                 github_action_configuration: Optional[pulumi.Input[pulumi.InputType['GithubActionConfigurationArgs']]] = None,
                 repo_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_control_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Container App SourceControl.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: The branch which will trigger the auto deployment
        :param pulumi.Input[str] container_app_name: Name of the Container App.
        :param pulumi.Input[pulumi.InputType['GithubActionConfigurationArgs']] github_action_configuration: Container App Revision Template with all possible settings and the
               defaults if user did not provide them. The defaults are populated
               as they were at the creation time
        :param pulumi.Input[str] repo_url: The repo url which will be integrated to ContainerApp.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] source_control_name: Name of the Container App SourceControl.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerAppsSourceControlArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Container App SourceControl.

        :param str resource_name: The name of the resource.
        :param ContainerAppsSourceControlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerAppsSourceControlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 container_app_name: Optional[pulumi.Input[str]] = None,
                 github_action_configuration: Optional[pulumi.Input[pulumi.InputType['GithubActionConfigurationArgs']]] = None,
                 repo_url: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_control_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerAppsSourceControlArgs.__new__(ContainerAppsSourceControlArgs)

            __props__.__dict__["branch"] = branch
            if container_app_name is None and not opts.urn:
                raise TypeError("Missing required property 'container_app_name'")
            __props__.__dict__["container_app_name"] = container_app_name
            __props__.__dict__["github_action_configuration"] = github_action_configuration
            __props__.__dict__["repo_url"] = repo_url
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source_control_name"] = source_control_name
            __props__.__dict__["name"] = None
            __props__.__dict__["operation_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20220101preview:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20220301:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20220601preview:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20221001:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20221101preview:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20230401preview:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20230501:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20230502preview:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20231102preview:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20240202preview:ContainerAppsSourceControl"), pulumi.Alias(type_="azure-native:app/v20240301:ContainerAppsSourceControl")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ContainerAppsSourceControl, __self__).__init__(
            'azure-native:app/v20230801preview:ContainerAppsSourceControl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ContainerAppsSourceControl':
        """
        Get an existing ContainerAppsSourceControl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContainerAppsSourceControlArgs.__new__(ContainerAppsSourceControlArgs)

        __props__.__dict__["branch"] = None
        __props__.__dict__["github_action_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operation_state"] = None
        __props__.__dict__["repo_url"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ContainerAppsSourceControl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Output[Optional[str]]:
        """
        The branch which will trigger the auto deployment
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="githubActionConfiguration")
    def github_action_configuration(self) -> pulumi.Output[Optional['outputs.GithubActionConfigurationResponse']]:
        """
        Container App Revision Template with all possible settings and the
        defaults if user did not provide them. The defaults are populated
        as they were at the creation time
        """
        return pulumi.get(self, "github_action_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationState")
    def operation_state(self) -> pulumi.Output[str]:
        """
        Current provisioning State of the operation
        """
        return pulumi.get(self, "operation_state")

    @property
    @pulumi.getter(name="repoUrl")
    def repo_url(self) -> pulumi.Output[Optional[str]]:
        """
        The repo url which will be integrated to ContainerApp.
        """
        return pulumi.get(self, "repo_url")

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

