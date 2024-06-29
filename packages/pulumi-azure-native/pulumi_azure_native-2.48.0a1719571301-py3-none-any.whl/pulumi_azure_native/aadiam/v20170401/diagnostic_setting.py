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

__all__ = ['DiagnosticSettingArgs', 'DiagnosticSetting']

@pulumi.input_type
class DiagnosticSettingArgs:
    def __init__(__self__, *,
                 event_hub_authorization_rule_id: Optional[pulumi.Input[str]] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input['LogSettingsArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DiagnosticSetting resource.
        :param pulumi.Input[str] event_hub_authorization_rule_id: The resource Id for the event hub authorization rule.
        :param pulumi.Input[str] event_hub_name: The name of the event hub. If none is specified, the default event hub will be selected.
        :param pulumi.Input[Sequence[pulumi.Input['LogSettingsArgs']]] logs: The list of logs settings.
        :param pulumi.Input[str] name: The name of the diagnostic setting.
        :param pulumi.Input[str] service_bus_rule_id: The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        :param pulumi.Input[str] storage_account_id: The resource ID of the storage account to which you would like to send Diagnostic Logs.
        :param pulumi.Input[str] workspace_id: The workspace ID (resource ID of a Log Analytics workspace) for a Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        if event_hub_authorization_rule_id is not None:
            pulumi.set(__self__, "event_hub_authorization_rule_id", event_hub_authorization_rule_id)
        if event_hub_name is not None:
            pulumi.set(__self__, "event_hub_name", event_hub_name)
        if logs is not None:
            pulumi.set(__self__, "logs", logs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service_bus_rule_id is not None:
            pulumi.set(__self__, "service_bus_rule_id", service_bus_rule_id)
        if storage_account_id is not None:
            pulumi.set(__self__, "storage_account_id", storage_account_id)
        if workspace_id is not None:
            pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="eventHubAuthorizationRuleId")
    def event_hub_authorization_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource Id for the event hub authorization rule.
        """
        return pulumi.get(self, "event_hub_authorization_rule_id")

    @event_hub_authorization_rule_id.setter
    def event_hub_authorization_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_hub_authorization_rule_id", value)

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the event hub. If none is specified, the default event hub will be selected.
        """
        return pulumi.get(self, "event_hub_name")

    @event_hub_name.setter
    def event_hub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_hub_name", value)

    @property
    @pulumi.getter
    def logs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LogSettingsArgs']]]]:
        """
        The list of logs settings.
        """
        return pulumi.get(self, "logs")

    @logs.setter
    def logs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LogSettingsArgs']]]]):
        pulumi.set(self, "logs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the diagnostic setting.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> Optional[pulumi.Input[str]]:
        """
        The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        """
        return pulumi.get(self, "service_bus_rule_id")

    @service_bus_rule_id.setter
    def service_bus_rule_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_bus_rule_id", value)

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the storage account to which you would like to send Diagnostic Logs.
        """
        return pulumi.get(self, "storage_account_id")

    @storage_account_id.setter
    def storage_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_id", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The workspace ID (resource ID of a Log Analytics workspace) for a Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class DiagnosticSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 event_hub_authorization_rule_id: Optional[pulumi.Input[str]] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogSettingsArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The diagnostic setting resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] event_hub_authorization_rule_id: The resource Id for the event hub authorization rule.
        :param pulumi.Input[str] event_hub_name: The name of the event hub. If none is specified, the default event hub will be selected.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogSettingsArgs']]]] logs: The list of logs settings.
        :param pulumi.Input[str] name: The name of the diagnostic setting.
        :param pulumi.Input[str] service_bus_rule_id: The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        :param pulumi.Input[str] storage_account_id: The resource ID of the storage account to which you would like to send Diagnostic Logs.
        :param pulumi.Input[str] workspace_id: The workspace ID (resource ID of a Log Analytics workspace) for a Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DiagnosticSettingArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The diagnostic setting resource.

        :param str resource_name: The name of the resource.
        :param DiagnosticSettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiagnosticSettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 event_hub_authorization_rule_id: Optional[pulumi.Input[str]] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 logs: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LogSettingsArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_bus_rule_id: Optional[pulumi.Input[str]] = None,
                 storage_account_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DiagnosticSettingArgs.__new__(DiagnosticSettingArgs)

            __props__.__dict__["event_hub_authorization_rule_id"] = event_hub_authorization_rule_id
            __props__.__dict__["event_hub_name"] = event_hub_name
            __props__.__dict__["logs"] = logs
            __props__.__dict__["name"] = name
            __props__.__dict__["service_bus_rule_id"] = service_bus_rule_id
            __props__.__dict__["storage_account_id"] = storage_account_id
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:aadiam:DiagnosticSetting"), pulumi.Alias(type_="azure-native:aadiam/v20170401preview:DiagnosticSetting")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DiagnosticSetting, __self__).__init__(
            'azure-native:aadiam/v20170401:DiagnosticSetting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DiagnosticSetting':
        """
        Get an existing DiagnosticSetting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DiagnosticSettingArgs.__new__(DiagnosticSettingArgs)

        __props__.__dict__["event_hub_authorization_rule_id"] = None
        __props__.__dict__["event_hub_name"] = None
        __props__.__dict__["logs"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["service_bus_rule_id"] = None
        __props__.__dict__["storage_account_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workspace_id"] = None
        return DiagnosticSetting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eventHubAuthorizationRuleId")
    def event_hub_authorization_rule_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource Id for the event hub authorization rule.
        """
        return pulumi.get(self, "event_hub_authorization_rule_id")

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the event hub. If none is specified, the default event hub will be selected.
        """
        return pulumi.get(self, "event_hub_name")

    @property
    @pulumi.getter
    def logs(self) -> pulumi.Output[Optional[Sequence['outputs.LogSettingsResponse']]]:
        """
        The list of logs settings.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> pulumi.Output[Optional[str]]:
        """
        The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        """
        return pulumi.get(self, "service_bus_rule_id")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the storage account to which you would like to send Diagnostic Logs.
        """
        return pulumi.get(self, "storage_account_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[Optional[str]]:
        """
        The workspace ID (resource ID of a Log Analytics workspace) for a Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        return pulumi.get(self, "workspace_id")

