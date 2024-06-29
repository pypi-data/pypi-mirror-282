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

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 azure_ad_only_authentication: Optional[pulumi.Input[bool]] = None,
                 csp_workspace_admin_properties: Optional[pulumi.Input['CspWorkspaceAdminPropertiesArgs']] = None,
                 default_data_lake_storage: Optional[pulumi.Input['DataLakeStorageAccountDetailsArgs']] = None,
                 encryption: Optional[pulumi.Input['EncryptionDetailsArgs']] = None,
                 identity: Optional[pulumi.Input['ManagedIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_name: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network_settings: Optional[pulumi.Input['ManagedVirtualNetworkSettingsArgs']] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'WorkspacePublicNetworkAccess']]] = None,
                 purview_configuration: Optional[pulumi.Input['PurviewConfigurationArgs']] = None,
                 sql_administrator_login: Optional[pulumi.Input[str]] = None,
                 sql_administrator_login_password: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_service_bypass_enabled: Optional[pulumi.Input[bool]] = None,
                 virtual_network_profile: Optional[pulumi.Input['VirtualNetworkProfileArgs']] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 workspace_repository_configuration: Optional[pulumi.Input['WorkspaceRepositoryConfigurationArgs']] = None):
        """
        The set of arguments for constructing a Workspace resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[bool] azure_ad_only_authentication: Enable or Disable AzureADOnlyAuthentication on All Workspace subresource
        :param pulumi.Input['CspWorkspaceAdminPropertiesArgs'] csp_workspace_admin_properties: Initial workspace AAD admin properties for a CSP subscription
        :param pulumi.Input['DataLakeStorageAccountDetailsArgs'] default_data_lake_storage: Workspace default data lake storage account details
        :param pulumi.Input['EncryptionDetailsArgs'] encryption: The encryption details of the workspace
        :param pulumi.Input['ManagedIdentityArgs'] identity: Identity of the workspace
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] managed_resource_group_name: Workspace managed resource group. The resource group name uniquely identifies the resource group within the user subscriptionId. The resource group name must be no longer than 90 characters long, and must be alphanumeric characters (Char.IsLetterOrDigit()) and '-', '_', '(', ')' and'.'. Note that the name cannot end with '.'
        :param pulumi.Input[str] managed_virtual_network: Setting this to 'default' will ensure that all compute for this workspace is in a virtual network managed on behalf of the user.
        :param pulumi.Input['ManagedVirtualNetworkSettingsArgs'] managed_virtual_network_settings: Managed Virtual Network Settings
        :param pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]] private_endpoint_connections: Private endpoint connections to the workspace
               These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        :param pulumi.Input[Union[str, 'WorkspacePublicNetworkAccess']] public_network_access: Enable or Disable public network access to workspace
        :param pulumi.Input['PurviewConfigurationArgs'] purview_configuration: Purview Configuration
        :param pulumi.Input[str] sql_administrator_login: Login for workspace SQL active directory administrator
        :param pulumi.Input[str] sql_administrator_login_password: SQL administrator login password
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] trusted_service_bypass_enabled: Is trustedServiceBypassEnabled for the workspace
        :param pulumi.Input['VirtualNetworkProfileArgs'] virtual_network_profile: Virtual Network profile
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input['WorkspaceRepositoryConfigurationArgs'] workspace_repository_configuration: Git integration settings
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if azure_ad_only_authentication is not None:
            pulumi.set(__self__, "azure_ad_only_authentication", azure_ad_only_authentication)
        if csp_workspace_admin_properties is not None:
            pulumi.set(__self__, "csp_workspace_admin_properties", csp_workspace_admin_properties)
        if default_data_lake_storage is not None:
            pulumi.set(__self__, "default_data_lake_storage", default_data_lake_storage)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_resource_group_name is not None:
            pulumi.set(__self__, "managed_resource_group_name", managed_resource_group_name)
        if managed_virtual_network is not None:
            pulumi.set(__self__, "managed_virtual_network", managed_virtual_network)
        if managed_virtual_network_settings is not None:
            pulumi.set(__self__, "managed_virtual_network_settings", managed_virtual_network_settings)
        if private_endpoint_connections is not None:
            pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access is None:
            public_network_access = 'Enabled'
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if purview_configuration is not None:
            pulumi.set(__self__, "purview_configuration", purview_configuration)
        if sql_administrator_login is not None:
            pulumi.set(__self__, "sql_administrator_login", sql_administrator_login)
        if sql_administrator_login_password is not None:
            pulumi.set(__self__, "sql_administrator_login_password", sql_administrator_login_password)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if trusted_service_bypass_enabled is None:
            trusted_service_bypass_enabled = False
        if trusted_service_bypass_enabled is not None:
            pulumi.set(__self__, "trusted_service_bypass_enabled", trusted_service_bypass_enabled)
        if virtual_network_profile is not None:
            pulumi.set(__self__, "virtual_network_profile", virtual_network_profile)
        if workspace_name is not None:
            pulumi.set(__self__, "workspace_name", workspace_name)
        if workspace_repository_configuration is not None:
            pulumi.set(__self__, "workspace_repository_configuration", workspace_repository_configuration)

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
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or Disable AzureADOnlyAuthentication on All Workspace subresource
        """
        return pulumi.get(self, "azure_ad_only_authentication")

    @azure_ad_only_authentication.setter
    def azure_ad_only_authentication(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "azure_ad_only_authentication", value)

    @property
    @pulumi.getter(name="cspWorkspaceAdminProperties")
    def csp_workspace_admin_properties(self) -> Optional[pulumi.Input['CspWorkspaceAdminPropertiesArgs']]:
        """
        Initial workspace AAD admin properties for a CSP subscription
        """
        return pulumi.get(self, "csp_workspace_admin_properties")

    @csp_workspace_admin_properties.setter
    def csp_workspace_admin_properties(self, value: Optional[pulumi.Input['CspWorkspaceAdminPropertiesArgs']]):
        pulumi.set(self, "csp_workspace_admin_properties", value)

    @property
    @pulumi.getter(name="defaultDataLakeStorage")
    def default_data_lake_storage(self) -> Optional[pulumi.Input['DataLakeStorageAccountDetailsArgs']]:
        """
        Workspace default data lake storage account details
        """
        return pulumi.get(self, "default_data_lake_storage")

    @default_data_lake_storage.setter
    def default_data_lake_storage(self, value: Optional[pulumi.Input['DataLakeStorageAccountDetailsArgs']]):
        pulumi.set(self, "default_data_lake_storage", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['EncryptionDetailsArgs']]:
        """
        The encryption details of the workspace
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['EncryptionDetailsArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedIdentityArgs']]:
        """
        Identity of the workspace
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedIdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Workspace managed resource group. The resource group name uniquely identifies the resource group within the user subscriptionId. The resource group name must be no longer than 90 characters long, and must be alphanumeric characters (Char.IsLetterOrDigit()) and '-', '_', '(', ')' and'.'. Note that the name cannot end with '.'
        """
        return pulumi.get(self, "managed_resource_group_name")

    @managed_resource_group_name.setter
    def managed_resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_resource_group_name", value)

    @property
    @pulumi.getter(name="managedVirtualNetwork")
    def managed_virtual_network(self) -> Optional[pulumi.Input[str]]:
        """
        Setting this to 'default' will ensure that all compute for this workspace is in a virtual network managed on behalf of the user.
        """
        return pulumi.get(self, "managed_virtual_network")

    @managed_virtual_network.setter
    def managed_virtual_network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_virtual_network", value)

    @property
    @pulumi.getter(name="managedVirtualNetworkSettings")
    def managed_virtual_network_settings(self) -> Optional[pulumi.Input['ManagedVirtualNetworkSettingsArgs']]:
        """
        Managed Virtual Network Settings
        """
        return pulumi.get(self, "managed_virtual_network_settings")

    @managed_virtual_network_settings.setter
    def managed_virtual_network_settings(self, value: Optional[pulumi.Input['ManagedVirtualNetworkSettingsArgs']]):
        pulumi.set(self, "managed_virtual_network_settings", value)

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]:
        """
        Private endpoint connections to the workspace
        These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @private_endpoint_connections.setter
    def private_endpoint_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]):
        pulumi.set(self, "private_endpoint_connections", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'WorkspacePublicNetworkAccess']]]:
        """
        Enable or Disable public network access to workspace
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'WorkspacePublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(self) -> Optional[pulumi.Input['PurviewConfigurationArgs']]:
        """
        Purview Configuration
        """
        return pulumi.get(self, "purview_configuration")

    @purview_configuration.setter
    def purview_configuration(self, value: Optional[pulumi.Input['PurviewConfigurationArgs']]):
        pulumi.set(self, "purview_configuration", value)

    @property
    @pulumi.getter(name="sqlAdministratorLogin")
    def sql_administrator_login(self) -> Optional[pulumi.Input[str]]:
        """
        Login for workspace SQL active directory administrator
        """
        return pulumi.get(self, "sql_administrator_login")

    @sql_administrator_login.setter
    def sql_administrator_login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_administrator_login", value)

    @property
    @pulumi.getter(name="sqlAdministratorLoginPassword")
    def sql_administrator_login_password(self) -> Optional[pulumi.Input[str]]:
        """
        SQL administrator login password
        """
        return pulumi.get(self, "sql_administrator_login_password")

    @sql_administrator_login_password.setter
    def sql_administrator_login_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_administrator_login_password", value)

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

    @property
    @pulumi.getter(name="trustedServiceBypassEnabled")
    def trusted_service_bypass_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Is trustedServiceBypassEnabled for the workspace
        """
        return pulumi.get(self, "trusted_service_bypass_enabled")

    @trusted_service_bypass_enabled.setter
    def trusted_service_bypass_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "trusted_service_bypass_enabled", value)

    @property
    @pulumi.getter(name="virtualNetworkProfile")
    def virtual_network_profile(self) -> Optional[pulumi.Input['VirtualNetworkProfileArgs']]:
        """
        Virtual Network profile
        """
        return pulumi.get(self, "virtual_network_profile")

    @virtual_network_profile.setter
    def virtual_network_profile(self, value: Optional[pulumi.Input['VirtualNetworkProfileArgs']]):
        pulumi.set(self, "virtual_network_profile", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="workspaceRepositoryConfiguration")
    def workspace_repository_configuration(self) -> Optional[pulumi.Input['WorkspaceRepositoryConfigurationArgs']]:
        """
        Git integration settings
        """
        return pulumi.get(self, "workspace_repository_configuration")

    @workspace_repository_configuration.setter
    def workspace_repository_configuration(self, value: Optional[pulumi.Input['WorkspaceRepositoryConfigurationArgs']]):
        pulumi.set(self, "workspace_repository_configuration", value)


class Workspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_ad_only_authentication: Optional[pulumi.Input[bool]] = None,
                 csp_workspace_admin_properties: Optional[pulumi.Input[pulumi.InputType['CspWorkspaceAdminPropertiesArgs']]] = None,
                 default_data_lake_storage: Optional[pulumi.Input[pulumi.InputType['DataLakeStorageAccountDetailsArgs']]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['EncryptionDetailsArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_name: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network_settings: Optional[pulumi.Input[pulumi.InputType['ManagedVirtualNetworkSettingsArgs']]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'WorkspacePublicNetworkAccess']]] = None,
                 purview_configuration: Optional[pulumi.Input[pulumi.InputType['PurviewConfigurationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_administrator_login: Optional[pulumi.Input[str]] = None,
                 sql_administrator_login_password: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_service_bypass_enabled: Optional[pulumi.Input[bool]] = None,
                 virtual_network_profile: Optional[pulumi.Input[pulumi.InputType['VirtualNetworkProfileArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 workspace_repository_configuration: Optional[pulumi.Input[pulumi.InputType['WorkspaceRepositoryConfigurationArgs']]] = None,
                 __props__=None):
        """
        A workspace
        Azure REST API version: 2021-06-01. Prior API version in Azure Native 1.x: 2021-03-01.

        Other available API versions: 2021-05-01, 2021-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] azure_ad_only_authentication: Enable or Disable AzureADOnlyAuthentication on All Workspace subresource
        :param pulumi.Input[pulumi.InputType['CspWorkspaceAdminPropertiesArgs']] csp_workspace_admin_properties: Initial workspace AAD admin properties for a CSP subscription
        :param pulumi.Input[pulumi.InputType['DataLakeStorageAccountDetailsArgs']] default_data_lake_storage: Workspace default data lake storage account details
        :param pulumi.Input[pulumi.InputType['EncryptionDetailsArgs']] encryption: The encryption details of the workspace
        :param pulumi.Input[pulumi.InputType['ManagedIdentityArgs']] identity: Identity of the workspace
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] managed_resource_group_name: Workspace managed resource group. The resource group name uniquely identifies the resource group within the user subscriptionId. The resource group name must be no longer than 90 characters long, and must be alphanumeric characters (Char.IsLetterOrDigit()) and '-', '_', '(', ')' and'.'. Note that the name cannot end with '.'
        :param pulumi.Input[str] managed_virtual_network: Setting this to 'default' will ensure that all compute for this workspace is in a virtual network managed on behalf of the user.
        :param pulumi.Input[pulumi.InputType['ManagedVirtualNetworkSettingsArgs']] managed_virtual_network_settings: Managed Virtual Network Settings
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]] private_endpoint_connections: Private endpoint connections to the workspace
               These are also available as standalone resources. Do not mix inline and standalone resource as they will conflict with each other, leading to resources deletion.
        :param pulumi.Input[Union[str, 'WorkspacePublicNetworkAccess']] public_network_access: Enable or Disable public network access to workspace
        :param pulumi.Input[pulumi.InputType['PurviewConfigurationArgs']] purview_configuration: Purview Configuration
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sql_administrator_login: Login for workspace SQL active directory administrator
        :param pulumi.Input[str] sql_administrator_login_password: SQL administrator login password
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[bool] trusted_service_bypass_enabled: Is trustedServiceBypassEnabled for the workspace
        :param pulumi.Input[pulumi.InputType['VirtualNetworkProfileArgs']] virtual_network_profile: Virtual Network profile
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[pulumi.InputType['WorkspaceRepositoryConfigurationArgs']] workspace_repository_configuration: Git integration settings
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A workspace
        Azure REST API version: 2021-06-01. Prior API version in Azure Native 1.x: 2021-03-01.

        Other available API versions: 2021-05-01, 2021-06-01-preview.

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_ad_only_authentication: Optional[pulumi.Input[bool]] = None,
                 csp_workspace_admin_properties: Optional[pulumi.Input[pulumi.InputType['CspWorkspaceAdminPropertiesArgs']]] = None,
                 default_data_lake_storage: Optional[pulumi.Input[pulumi.InputType['DataLakeStorageAccountDetailsArgs']]] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['EncryptionDetailsArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_name: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network: Optional[pulumi.Input[str]] = None,
                 managed_virtual_network_settings: Optional[pulumi.Input[pulumi.InputType['ManagedVirtualNetworkSettingsArgs']]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'WorkspacePublicNetworkAccess']]] = None,
                 purview_configuration: Optional[pulumi.Input[pulumi.InputType['PurviewConfigurationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_administrator_login: Optional[pulumi.Input[str]] = None,
                 sql_administrator_login_password: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 trusted_service_bypass_enabled: Optional[pulumi.Input[bool]] = None,
                 virtual_network_profile: Optional[pulumi.Input[pulumi.InputType['VirtualNetworkProfileArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 workspace_repository_configuration: Optional[pulumi.Input[pulumi.InputType['WorkspaceRepositoryConfigurationArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            __props__.__dict__["azure_ad_only_authentication"] = azure_ad_only_authentication
            __props__.__dict__["csp_workspace_admin_properties"] = csp_workspace_admin_properties
            __props__.__dict__["default_data_lake_storage"] = default_data_lake_storage
            __props__.__dict__["encryption"] = encryption
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_resource_group_name"] = managed_resource_group_name
            __props__.__dict__["managed_virtual_network"] = managed_virtual_network
            __props__.__dict__["managed_virtual_network_settings"] = managed_virtual_network_settings
            __props__.__dict__["private_endpoint_connections"] = private_endpoint_connections
            if public_network_access is None:
                public_network_access = 'Enabled'
            __props__.__dict__["public_network_access"] = public_network_access
            __props__.__dict__["purview_configuration"] = purview_configuration
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sql_administrator_login"] = sql_administrator_login
            __props__.__dict__["sql_administrator_login_password"] = sql_administrator_login_password
            __props__.__dict__["tags"] = tags
            if trusted_service_bypass_enabled is None:
                trusted_service_bypass_enabled = False
            __props__.__dict__["trusted_service_bypass_enabled"] = trusted_service_bypass_enabled
            __props__.__dict__["virtual_network_profile"] = virtual_network_profile
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["workspace_repository_configuration"] = workspace_repository_configuration
            __props__.__dict__["adla_resource_id"] = None
            __props__.__dict__["connectivity_endpoints"] = None
            __props__.__dict__["extra_properties"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["settings"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["workspace_uid"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse/v20190601preview:Workspace"), pulumi.Alias(type_="azure-native:synapse/v20201201:Workspace"), pulumi.Alias(type_="azure-native:synapse/v20210301:Workspace"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:Workspace"), pulumi.Alias(type_="azure-native:synapse/v20210501:Workspace"), pulumi.Alias(type_="azure-native:synapse/v20210601:Workspace"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:Workspace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Workspace, __self__).__init__(
            'azure-native:synapse:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

        __props__.__dict__["adla_resource_id"] = None
        __props__.__dict__["connectivity_endpoints"] = None
        __props__.__dict__["csp_workspace_admin_properties"] = None
        __props__.__dict__["default_data_lake_storage"] = None
        __props__.__dict__["encryption"] = None
        __props__.__dict__["extra_properties"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_resource_group_name"] = None
        __props__.__dict__["managed_virtual_network"] = None
        __props__.__dict__["managed_virtual_network_settings"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["purview_configuration"] = None
        __props__.__dict__["settings"] = None
        __props__.__dict__["sql_administrator_login"] = None
        __props__.__dict__["sql_administrator_login_password"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["trusted_service_bypass_enabled"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_profile"] = None
        __props__.__dict__["workspace_repository_configuration"] = None
        __props__.__dict__["workspace_uid"] = None
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adlaResourceId")
    def adla_resource_id(self) -> pulumi.Output[str]:
        """
        The ADLA resource ID.
        """
        return pulumi.get(self, "adla_resource_id")

    @property
    @pulumi.getter(name="connectivityEndpoints")
    def connectivity_endpoints(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Connectivity endpoints
        """
        return pulumi.get(self, "connectivity_endpoints")

    @property
    @pulumi.getter(name="cspWorkspaceAdminProperties")
    def csp_workspace_admin_properties(self) -> pulumi.Output[Optional['outputs.CspWorkspaceAdminPropertiesResponse']]:
        """
        Initial workspace AAD admin properties for a CSP subscription
        """
        return pulumi.get(self, "csp_workspace_admin_properties")

    @property
    @pulumi.getter(name="defaultDataLakeStorage")
    def default_data_lake_storage(self) -> pulumi.Output[Optional['outputs.DataLakeStorageAccountDetailsResponse']]:
        """
        Workspace default data lake storage account details
        """
        return pulumi.get(self, "default_data_lake_storage")

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional['outputs.EncryptionDetailsResponse']]:
        """
        The encryption details of the workspace
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="extraProperties")
    def extra_properties(self) -> pulumi.Output[Any]:
        """
        Workspace level configs and feature flags
        """
        return pulumi.get(self, "extra_properties")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedIdentityResponse']]:
        """
        Identity of the workspace
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
    @pulumi.getter(name="managedResourceGroupName")
    def managed_resource_group_name(self) -> pulumi.Output[Optional[str]]:
        """
        Workspace managed resource group. The resource group name uniquely identifies the resource group within the user subscriptionId. The resource group name must be no longer than 90 characters long, and must be alphanumeric characters (Char.IsLetterOrDigit()) and '-', '_', '(', ')' and'.'. Note that the name cannot end with '.'
        """
        return pulumi.get(self, "managed_resource_group_name")

    @property
    @pulumi.getter(name="managedVirtualNetwork")
    def managed_virtual_network(self) -> pulumi.Output[Optional[str]]:
        """
        Setting this to 'default' will ensure that all compute for this workspace is in a virtual network managed on behalf of the user.
        """
        return pulumi.get(self, "managed_virtual_network")

    @property
    @pulumi.getter(name="managedVirtualNetworkSettings")
    def managed_virtual_network_settings(self) -> pulumi.Output[Optional['outputs.ManagedVirtualNetworkSettingsResponse']]:
        """
        Managed Virtual Network Settings
        """
        return pulumi.get(self, "managed_virtual_network_settings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]]:
        """
        Private endpoint connections to the workspace
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Resource provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Enable or Disable public network access to workspace
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(self) -> pulumi.Output[Optional['outputs.PurviewConfigurationResponse']]:
        """
        Purview Configuration
        """
        return pulumi.get(self, "purview_configuration")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Workspace settings
        """
        return pulumi.get(self, "settings")

    @property
    @pulumi.getter(name="sqlAdministratorLogin")
    def sql_administrator_login(self) -> pulumi.Output[Optional[str]]:
        """
        Login for workspace SQL active directory administrator
        """
        return pulumi.get(self, "sql_administrator_login")

    @property
    @pulumi.getter(name="sqlAdministratorLoginPassword")
    def sql_administrator_login_password(self) -> pulumi.Output[Optional[str]]:
        """
        SQL administrator login password
        """
        return pulumi.get(self, "sql_administrator_login_password")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustedServiceBypassEnabled")
    def trusted_service_bypass_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Is trustedServiceBypassEnabled for the workspace
        """
        return pulumi.get(self, "trusted_service_bypass_enabled")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkProfile")
    def virtual_network_profile(self) -> pulumi.Output[Optional['outputs.VirtualNetworkProfileResponse']]:
        """
        Virtual Network profile
        """
        return pulumi.get(self, "virtual_network_profile")

    @property
    @pulumi.getter(name="workspaceRepositoryConfiguration")
    def workspace_repository_configuration(self) -> pulumi.Output[Optional['outputs.WorkspaceRepositoryConfigurationResponse']]:
        """
        Git integration settings
        """
        return pulumi.get(self, "workspace_repository_configuration")

    @property
    @pulumi.getter(name="workspaceUID")
    def workspace_uid(self) -> pulumi.Output[str]:
        """
        The workspace unique identifier
        """
        return pulumi.get(self, "workspace_uid")

