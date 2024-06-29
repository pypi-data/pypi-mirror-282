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

__all__ = [
    'GetCustomizableConnectorDefinitionResult',
    'AwaitableGetCustomizableConnectorDefinitionResult',
    'get_customizable_connector_definition',
    'get_customizable_connector_definition_output',
]

@pulumi.output_type
class GetCustomizableConnectorDefinitionResult:
    """
    Connector definition for kind 'Customizable'.
    """
    def __init__(__self__, connections_config=None, connector_ui_config=None, created_time_utc=None, etag=None, id=None, kind=None, last_modified_utc=None, name=None, system_data=None, type=None):
        if connections_config and not isinstance(connections_config, dict):
            raise TypeError("Expected argument 'connections_config' to be a dict")
        pulumi.set(__self__, "connections_config", connections_config)
        if connector_ui_config and not isinstance(connector_ui_config, dict):
            raise TypeError("Expected argument 'connector_ui_config' to be a dict")
        pulumi.set(__self__, "connector_ui_config", connector_ui_config)
        if created_time_utc and not isinstance(created_time_utc, str):
            raise TypeError("Expected argument 'created_time_utc' to be a str")
        pulumi.set(__self__, "created_time_utc", created_time_utc)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if last_modified_utc and not isinstance(last_modified_utc, str):
            raise TypeError("Expected argument 'last_modified_utc' to be a str")
        pulumi.set(__self__, "last_modified_utc", last_modified_utc)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="connectionsConfig")
    def connections_config(self) -> Optional['outputs.CustomizableConnectionsConfigResponse']:
        """
        The UiConfig for 'Customizable' connector definition kind.
        """
        return pulumi.get(self, "connections_config")

    @property
    @pulumi.getter(name="connectorUiConfig")
    def connector_ui_config(self) -> 'outputs.CustomizableConnectorUiConfigResponse':
        """
        The UiConfig for 'Customizable' connector definition kind.
        """
        return pulumi.get(self, "connector_ui_config")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> Optional[str]:
        """
        Gets or sets the connector definition created date in UTC format.
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the data connector definitions
        Expected value is 'Customizable'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> Optional[str]:
        """
        Gets or sets the connector definition last modified date in UTC format.
        """
        return pulumi.get(self, "last_modified_utc")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetCustomizableConnectorDefinitionResult(GetCustomizableConnectorDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomizableConnectorDefinitionResult(
            connections_config=self.connections_config,
            connector_ui_config=self.connector_ui_config,
            created_time_utc=self.created_time_utc,
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            last_modified_utc=self.last_modified_utc,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_customizable_connector_definition(data_connector_definition_name: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          workspace_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomizableConnectorDefinitionResult:
    """
    Gets a data connector definition.


    :param str data_connector_definition_name: The data connector definition name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['dataConnectorDefinitionName'] = data_connector_definition_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20231201preview:getCustomizableConnectorDefinition', __args__, opts=opts, typ=GetCustomizableConnectorDefinitionResult).value

    return AwaitableGetCustomizableConnectorDefinitionResult(
        connections_config=pulumi.get(__ret__, 'connections_config'),
        connector_ui_config=pulumi.get(__ret__, 'connector_ui_config'),
        created_time_utc=pulumi.get(__ret__, 'created_time_utc'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        last_modified_utc=pulumi.get(__ret__, 'last_modified_utc'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_customizable_connector_definition)
def get_customizable_connector_definition_output(data_connector_definition_name: Optional[pulumi.Input[str]] = None,
                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 workspace_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomizableConnectorDefinitionResult]:
    """
    Gets a data connector definition.


    :param str data_connector_definition_name: The data connector definition name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
