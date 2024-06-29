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

__all__ = ['ProjectCatalogArgs', 'ProjectCatalog']

@pulumi.input_type
class ProjectCatalogArgs:
    def __init__(__self__, *,
                 project_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 ado_git: Optional[pulumi.Input['GitCatalogArgs']] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 git_hub: Optional[pulumi.Input['GitCatalogArgs']] = None,
                 sync_type: Optional[pulumi.Input[Union[str, 'CatalogSyncType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ProjectCatalog resource.
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['GitCatalogArgs'] ado_git: Properties for an Azure DevOps catalog type.
        :param pulumi.Input[str] catalog_name: The name of the Catalog.
        :param pulumi.Input['GitCatalogArgs'] git_hub: Properties for a GitHub catalog type.
        :param pulumi.Input[Union[str, 'CatalogSyncType']] sync_type: Indicates the type of sync that is configured for the catalog.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if ado_git is not None:
            pulumi.set(__self__, "ado_git", ado_git)
        if catalog_name is not None:
            pulumi.set(__self__, "catalog_name", catalog_name)
        if git_hub is not None:
            pulumi.set(__self__, "git_hub", git_hub)
        if sync_type is not None:
            pulumi.set(__self__, "sync_type", sync_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        The name of the project.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

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
    @pulumi.getter(name="adoGit")
    def ado_git(self) -> Optional[pulumi.Input['GitCatalogArgs']]:
        """
        Properties for an Azure DevOps catalog type.
        """
        return pulumi.get(self, "ado_git")

    @ado_git.setter
    def ado_git(self, value: Optional[pulumi.Input['GitCatalogArgs']]):
        pulumi.set(self, "ado_git", value)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Catalog.
        """
        return pulumi.get(self, "catalog_name")

    @catalog_name.setter
    def catalog_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_name", value)

    @property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> Optional[pulumi.Input['GitCatalogArgs']]:
        """
        Properties for a GitHub catalog type.
        """
        return pulumi.get(self, "git_hub")

    @git_hub.setter
    def git_hub(self, value: Optional[pulumi.Input['GitCatalogArgs']]):
        pulumi.set(self, "git_hub", value)

    @property
    @pulumi.getter(name="syncType")
    def sync_type(self) -> Optional[pulumi.Input[Union[str, 'CatalogSyncType']]]:
        """
        Indicates the type of sync that is configured for the catalog.
        """
        return pulumi.get(self, "sync_type")

    @sync_type.setter
    def sync_type(self, value: Optional[pulumi.Input[Union[str, 'CatalogSyncType']]]):
        pulumi.set(self, "sync_type", value)

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


class ProjectCatalog(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ado_git: Optional[pulumi.Input[pulumi.InputType['GitCatalogArgs']]] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 git_hub: Optional[pulumi.Input[pulumi.InputType['GitCatalogArgs']]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sync_type: Optional[pulumi.Input[Union[str, 'CatalogSyncType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents a catalog.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GitCatalogArgs']] ado_git: Properties for an Azure DevOps catalog type.
        :param pulumi.Input[str] catalog_name: The name of the Catalog.
        :param pulumi.Input[pulumi.InputType['GitCatalogArgs']] git_hub: Properties for a GitHub catalog type.
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'CatalogSyncType']] sync_type: Indicates the type of sync that is configured for the catalog.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectCatalogArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a catalog.

        :param str resource_name: The name of the resource.
        :param ProjectCatalogArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectCatalogArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ado_git: Optional[pulumi.Input[pulumi.InputType['GitCatalogArgs']]] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 git_hub: Optional[pulumi.Input[pulumi.InputType['GitCatalogArgs']]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sync_type: Optional[pulumi.Input[Union[str, 'CatalogSyncType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectCatalogArgs.__new__(ProjectCatalogArgs)

            __props__.__dict__["ado_git"] = ado_git
            __props__.__dict__["catalog_name"] = catalog_name
            __props__.__dict__["git_hub"] = git_hub
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sync_type"] = sync_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["connection_state"] = None
            __props__.__dict__["last_connection_time"] = None
            __props__.__dict__["last_sync_stats"] = None
            __props__.__dict__["last_sync_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["sync_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter:ProjectCatalog"), pulumi.Alias(type_="azure-native:devcenter/v20240201:ProjectCatalog"), pulumi.Alias(type_="azure-native:devcenter/v20240501preview:ProjectCatalog")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProjectCatalog, __self__).__init__(
            'azure-native:devcenter/v20240601preview:ProjectCatalog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProjectCatalog':
        """
        Get an existing ProjectCatalog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProjectCatalogArgs.__new__(ProjectCatalogArgs)

        __props__.__dict__["ado_git"] = None
        __props__.__dict__["connection_state"] = None
        __props__.__dict__["git_hub"] = None
        __props__.__dict__["last_connection_time"] = None
        __props__.__dict__["last_sync_stats"] = None
        __props__.__dict__["last_sync_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sync_state"] = None
        __props__.__dict__["sync_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ProjectCatalog(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adoGit")
    def ado_git(self) -> pulumi.Output[Optional['outputs.GitCatalogResponse']]:
        """
        Properties for an Azure DevOps catalog type.
        """
        return pulumi.get(self, "ado_git")

    @property
    @pulumi.getter(name="connectionState")
    def connection_state(self) -> pulumi.Output[str]:
        """
        The connection state of the catalog.
        """
        return pulumi.get(self, "connection_state")

    @property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> pulumi.Output[Optional['outputs.GitCatalogResponse']]:
        """
        Properties for a GitHub catalog type.
        """
        return pulumi.get(self, "git_hub")

    @property
    @pulumi.getter(name="lastConnectionTime")
    def last_connection_time(self) -> pulumi.Output[str]:
        """
        When the catalog was last connected.
        """
        return pulumi.get(self, "last_connection_time")

    @property
    @pulumi.getter(name="lastSyncStats")
    def last_sync_stats(self) -> pulumi.Output['outputs.SyncStatsResponse']:
        """
        Stats of the latest synchronization.
        """
        return pulumi.get(self, "last_sync_stats")

    @property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> pulumi.Output[str]:
        """
        When the catalog was last synced.
        """
        return pulumi.get(self, "last_sync_time")

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
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> pulumi.Output[str]:
        """
        The synchronization state of the catalog.
        """
        return pulumi.get(self, "sync_state")

    @property
    @pulumi.getter(name="syncType")
    def sync_type(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates the type of sync that is configured for the catalog.
        """
        return pulumi.get(self, "sync_type")

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
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

