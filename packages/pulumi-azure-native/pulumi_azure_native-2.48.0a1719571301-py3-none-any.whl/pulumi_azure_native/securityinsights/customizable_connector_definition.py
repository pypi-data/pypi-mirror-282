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

__all__ = ['CustomizableConnectorDefinitionArgs', 'CustomizableConnectorDefinition']

@pulumi.input_type
class CustomizableConnectorDefinitionArgs:
    def __init__(__self__, *,
                 connector_ui_config: pulumi.Input['CustomizableConnectorUiConfigArgs'],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 connections_config: Optional[pulumi.Input['CustomizableConnectionsConfigArgs']] = None,
                 created_time_utc: Optional[pulumi.Input[str]] = None,
                 data_connector_definition_name: Optional[pulumi.Input[str]] = None,
                 last_modified_utc: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomizableConnectorDefinition resource.
        :param pulumi.Input['CustomizableConnectorUiConfigArgs'] connector_ui_config: The UiConfig for 'Customizable' connector definition kind.
        :param pulumi.Input[str] kind: The kind of the data connector definitions
               Expected value is 'Customizable'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input['CustomizableConnectionsConfigArgs'] connections_config: The UiConfig for 'Customizable' connector definition kind.
        :param pulumi.Input[str] created_time_utc: Gets or sets the connector definition created date in UTC format.
        :param pulumi.Input[str] data_connector_definition_name: The data connector definition name.
        :param pulumi.Input[str] last_modified_utc: Gets or sets the connector definition last modified date in UTC format.
        """
        pulumi.set(__self__, "connector_ui_config", connector_ui_config)
        pulumi.set(__self__, "kind", 'Customizable')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if connections_config is not None:
            pulumi.set(__self__, "connections_config", connections_config)
        if created_time_utc is not None:
            pulumi.set(__self__, "created_time_utc", created_time_utc)
        if data_connector_definition_name is not None:
            pulumi.set(__self__, "data_connector_definition_name", data_connector_definition_name)
        if last_modified_utc is not None:
            pulumi.set(__self__, "last_modified_utc", last_modified_utc)

    @property
    @pulumi.getter(name="connectorUiConfig")
    def connector_ui_config(self) -> pulumi.Input['CustomizableConnectorUiConfigArgs']:
        """
        The UiConfig for 'Customizable' connector definition kind.
        """
        return pulumi.get(self, "connector_ui_config")

    @connector_ui_config.setter
    def connector_ui_config(self, value: pulumi.Input['CustomizableConnectorUiConfigArgs']):
        pulumi.set(self, "connector_ui_config", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the data connector definitions
        Expected value is 'Customizable'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="connectionsConfig")
    def connections_config(self) -> Optional[pulumi.Input['CustomizableConnectionsConfigArgs']]:
        """
        The UiConfig for 'Customizable' connector definition kind.
        """
        return pulumi.get(self, "connections_config")

    @connections_config.setter
    def connections_config(self, value: Optional[pulumi.Input['CustomizableConnectionsConfigArgs']]):
        pulumi.set(self, "connections_config", value)

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the connector definition created date in UTC format.
        """
        return pulumi.get(self, "created_time_utc")

    @created_time_utc.setter
    def created_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_time_utc", value)

    @property
    @pulumi.getter(name="dataConnectorDefinitionName")
    def data_connector_definition_name(self) -> Optional[pulumi.Input[str]]:
        """
        The data connector definition name.
        """
        return pulumi.get(self, "data_connector_definition_name")

    @data_connector_definition_name.setter
    def data_connector_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_connector_definition_name", value)

    @property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the connector definition last modified date in UTC format.
        """
        return pulumi.get(self, "last_modified_utc")

    @last_modified_utc.setter
    def last_modified_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_utc", value)


class CustomizableConnectorDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections_config: Optional[pulumi.Input[pulumi.InputType['CustomizableConnectionsConfigArgs']]] = None,
                 connector_ui_config: Optional[pulumi.Input[pulumi.InputType['CustomizableConnectorUiConfigArgs']]] = None,
                 created_time_utc: Optional[pulumi.Input[str]] = None,
                 data_connector_definition_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 last_modified_utc: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Connector definition for kind 'Customizable'.
        Azure REST API version: 2023-07-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CustomizableConnectionsConfigArgs']] connections_config: The UiConfig for 'Customizable' connector definition kind.
        :param pulumi.Input[pulumi.InputType['CustomizableConnectorUiConfigArgs']] connector_ui_config: The UiConfig for 'Customizable' connector definition kind.
        :param pulumi.Input[str] created_time_utc: Gets or sets the connector definition created date in UTC format.
        :param pulumi.Input[str] data_connector_definition_name: The data connector definition name.
        :param pulumi.Input[str] kind: The kind of the data connector definitions
               Expected value is 'Customizable'.
        :param pulumi.Input[str] last_modified_utc: Gets or sets the connector definition last modified date in UTC format.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomizableConnectorDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Connector definition for kind 'Customizable'.
        Azure REST API version: 2023-07-01-preview.

        :param str resource_name: The name of the resource.
        :param CustomizableConnectorDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomizableConnectorDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections_config: Optional[pulumi.Input[pulumi.InputType['CustomizableConnectionsConfigArgs']]] = None,
                 connector_ui_config: Optional[pulumi.Input[pulumi.InputType['CustomizableConnectorUiConfigArgs']]] = None,
                 created_time_utc: Optional[pulumi.Input[str]] = None,
                 data_connector_definition_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 last_modified_utc: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomizableConnectorDefinitionArgs.__new__(CustomizableConnectorDefinitionArgs)

            __props__.__dict__["connections_config"] = connections_config
            if connector_ui_config is None and not opts.urn:
                raise TypeError("Missing required property 'connector_ui_config'")
            __props__.__dict__["connector_ui_config"] = connector_ui_config
            __props__.__dict__["created_time_utc"] = created_time_utc
            __props__.__dict__["data_connector_definition_name"] = data_connector_definition_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'Customizable'
            __props__.__dict__["last_modified_utc"] = last_modified_utc
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:CustomizableConnectorDefinition"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:CustomizableConnectorDefinition"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:CustomizableConnectorDefinition"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:CustomizableConnectorDefinition"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:CustomizableConnectorDefinition"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:CustomizableConnectorDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomizableConnectorDefinition, __self__).__init__(
            'azure-native:securityinsights:CustomizableConnectorDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomizableConnectorDefinition':
        """
        Get an existing CustomizableConnectorDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomizableConnectorDefinitionArgs.__new__(CustomizableConnectorDefinitionArgs)

        __props__.__dict__["connections_config"] = None
        __props__.__dict__["connector_ui_config"] = None
        __props__.__dict__["created_time_utc"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["last_modified_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CustomizableConnectorDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionsConfig")
    def connections_config(self) -> pulumi.Output[Optional['outputs.CustomizableConnectionsConfigResponse']]:
        """
        The UiConfig for 'Customizable' connector definition kind.
        """
        return pulumi.get(self, "connections_config")

    @property
    @pulumi.getter(name="connectorUiConfig")
    def connector_ui_config(self) -> pulumi.Output['outputs.CustomizableConnectorUiConfigResponse']:
        """
        The UiConfig for 'Customizable' connector definition kind.
        """
        return pulumi.get(self, "connector_ui_config")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the connector definition created date in UTC format.
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of the data connector definitions
        Expected value is 'Customizable'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the connector definition last modified date in UTC format.
        """
        return pulumi.get(self, "last_modified_utc")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

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

