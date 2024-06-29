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

__all__ = ['AnomalySecurityMLAnalyticsSettingsArgs', 'AnomalySecurityMLAnalyticsSettings']

@pulumi.input_type
class AnomalySecurityMLAnalyticsSettingsArgs:
    def __init__(__self__, *,
                 anomaly_version: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 enabled: pulumi.Input[bool],
                 frequency: pulumi.Input[str],
                 is_default_settings: pulumi.Input[bool],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 settings_status: pulumi.Input[Union[str, 'SettingsStatus']],
                 workspace_name: pulumi.Input[str],
                 anomaly_settings_version: Optional[pulumi.Input[int]] = None,
                 customizable_observations: Optional[Any] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 required_data_connectors: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityMLAnalyticsSettingsDataSourceArgs']]]] = None,
                 settings_definition_id: Optional[pulumi.Input[str]] = None,
                 settings_resource_name: Optional[pulumi.Input[str]] = None,
                 tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]] = None,
                 techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AnomalySecurityMLAnalyticsSettings resource.
        :param pulumi.Input[str] anomaly_version: The anomaly version of the AnomalySecurityMLAnalyticsSettings.
        :param pulumi.Input[str] display_name: The display name for settings created by this SecurityMLAnalyticsSettings.
        :param pulumi.Input[bool] enabled: Determines whether this settings is enabled or disabled.
        :param pulumi.Input[str] frequency: The frequency that this SecurityMLAnalyticsSettings will be run.
        :param pulumi.Input[bool] is_default_settings: Determines whether this anomaly security ml analytics settings is a default settings
        :param pulumi.Input[str] kind: The kind of security ML analytics settings
               Expected value is 'Anomaly'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'SettingsStatus']] settings_status: The anomaly SecurityMLAnalyticsSettings status
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[int] anomaly_settings_version: The anomaly settings version of the Anomaly security ml analytics settings that dictates whether job version gets updated or not.
        :param Any customizable_observations: The customizable observations of the AnomalySecurityMLAnalyticsSettings.
        :param pulumi.Input[str] description: The description of the SecurityMLAnalyticsSettings.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityMLAnalyticsSettingsDataSourceArgs']]] required_data_connectors: The required data sources for this SecurityMLAnalyticsSettings
        :param pulumi.Input[str] settings_definition_id: The anomaly settings definition Id
        :param pulumi.Input[str] settings_resource_name: Security ML Analytics Settings resource name
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]] tactics: The tactics of the SecurityMLAnalyticsSettings
        :param pulumi.Input[Sequence[pulumi.Input[str]]] techniques: The techniques of the SecurityMLAnalyticsSettings
        """
        pulumi.set(__self__, "anomaly_version", anomaly_version)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "is_default_settings", is_default_settings)
        pulumi.set(__self__, "kind", 'Anomaly')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "settings_status", settings_status)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if anomaly_settings_version is not None:
            pulumi.set(__self__, "anomaly_settings_version", anomaly_settings_version)
        if customizable_observations is not None:
            pulumi.set(__self__, "customizable_observations", customizable_observations)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if required_data_connectors is not None:
            pulumi.set(__self__, "required_data_connectors", required_data_connectors)
        if settings_definition_id is not None:
            pulumi.set(__self__, "settings_definition_id", settings_definition_id)
        if settings_resource_name is not None:
            pulumi.set(__self__, "settings_resource_name", settings_resource_name)
        if tactics is not None:
            pulumi.set(__self__, "tactics", tactics)
        if techniques is not None:
            pulumi.set(__self__, "techniques", techniques)

    @property
    @pulumi.getter(name="anomalyVersion")
    def anomaly_version(self) -> pulumi.Input[str]:
        """
        The anomaly version of the AnomalySecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "anomaly_version")

    @anomaly_version.setter
    def anomaly_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "anomaly_version", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name for settings created by this SecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Determines whether this settings is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Input[str]:
        """
        The frequency that this SecurityMLAnalyticsSettings will be run.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: pulumi.Input[str]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter(name="isDefaultSettings")
    def is_default_settings(self) -> pulumi.Input[bool]:
        """
        Determines whether this anomaly security ml analytics settings is a default settings
        """
        return pulumi.get(self, "is_default_settings")

    @is_default_settings.setter
    def is_default_settings(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_default_settings", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of security ML analytics settings
        Expected value is 'Anomaly'.
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
    @pulumi.getter(name="settingsStatus")
    def settings_status(self) -> pulumi.Input[Union[str, 'SettingsStatus']]:
        """
        The anomaly SecurityMLAnalyticsSettings status
        """
        return pulumi.get(self, "settings_status")

    @settings_status.setter
    def settings_status(self, value: pulumi.Input[Union[str, 'SettingsStatus']]):
        pulumi.set(self, "settings_status", value)

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
    @pulumi.getter(name="anomalySettingsVersion")
    def anomaly_settings_version(self) -> Optional[pulumi.Input[int]]:
        """
        The anomaly settings version of the Anomaly security ml analytics settings that dictates whether job version gets updated or not.
        """
        return pulumi.get(self, "anomaly_settings_version")

    @anomaly_settings_version.setter
    def anomaly_settings_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "anomaly_settings_version", value)

    @property
    @pulumi.getter(name="customizableObservations")
    def customizable_observations(self) -> Optional[Any]:
        """
        The customizable observations of the AnomalySecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "customizable_observations")

    @customizable_observations.setter
    def customizable_observations(self, value: Optional[Any]):
        pulumi.set(self, "customizable_observations", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the SecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="requiredDataConnectors")
    def required_data_connectors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityMLAnalyticsSettingsDataSourceArgs']]]]:
        """
        The required data sources for this SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "required_data_connectors")

    @required_data_connectors.setter
    def required_data_connectors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityMLAnalyticsSettingsDataSourceArgs']]]]):
        pulumi.set(self, "required_data_connectors", value)

    @property
    @pulumi.getter(name="settingsDefinitionId")
    def settings_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The anomaly settings definition Id
        """
        return pulumi.get(self, "settings_definition_id")

    @settings_definition_id.setter
    def settings_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "settings_definition_id", value)

    @property
    @pulumi.getter(name="settingsResourceName")
    def settings_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Security ML Analytics Settings resource name
        """
        return pulumi.get(self, "settings_resource_name")

    @settings_resource_name.setter
    def settings_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "settings_resource_name", value)

    @property
    @pulumi.getter
    def tactics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]]:
        """
        The tactics of the SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "tactics")

    @tactics.setter
    def tactics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]]):
        pulumi.set(self, "tactics", value)

    @property
    @pulumi.getter
    def techniques(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The techniques of the SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "techniques")

    @techniques.setter
    def techniques(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "techniques", value)


class AnomalySecurityMLAnalyticsSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 anomaly_settings_version: Optional[pulumi.Input[int]] = None,
                 anomaly_version: Optional[pulumi.Input[str]] = None,
                 customizable_observations: Optional[Any] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 is_default_settings: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 required_data_connectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityMLAnalyticsSettingsDataSourceArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 settings_definition_id: Optional[pulumi.Input[str]] = None,
                 settings_resource_name: Optional[pulumi.Input[str]] = None,
                 settings_status: Optional[pulumi.Input[Union[str, 'SettingsStatus']]] = None,
                 tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]] = None,
                 techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents Anomaly Security ML Analytics Settings

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] anomaly_settings_version: The anomaly settings version of the Anomaly security ml analytics settings that dictates whether job version gets updated or not.
        :param pulumi.Input[str] anomaly_version: The anomaly version of the AnomalySecurityMLAnalyticsSettings.
        :param Any customizable_observations: The customizable observations of the AnomalySecurityMLAnalyticsSettings.
        :param pulumi.Input[str] description: The description of the SecurityMLAnalyticsSettings.
        :param pulumi.Input[str] display_name: The display name for settings created by this SecurityMLAnalyticsSettings.
        :param pulumi.Input[bool] enabled: Determines whether this settings is enabled or disabled.
        :param pulumi.Input[str] frequency: The frequency that this SecurityMLAnalyticsSettings will be run.
        :param pulumi.Input[bool] is_default_settings: Determines whether this anomaly security ml analytics settings is a default settings
        :param pulumi.Input[str] kind: The kind of security ML analytics settings
               Expected value is 'Anomaly'.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityMLAnalyticsSettingsDataSourceArgs']]]] required_data_connectors: The required data sources for this SecurityMLAnalyticsSettings
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] settings_definition_id: The anomaly settings definition Id
        :param pulumi.Input[str] settings_resource_name: Security ML Analytics Settings resource name
        :param pulumi.Input[Union[str, 'SettingsStatus']] settings_status: The anomaly SecurityMLAnalyticsSettings status
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]] tactics: The tactics of the SecurityMLAnalyticsSettings
        :param pulumi.Input[Sequence[pulumi.Input[str]]] techniques: The techniques of the SecurityMLAnalyticsSettings
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnomalySecurityMLAnalyticsSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents Anomaly Security ML Analytics Settings

        :param str resource_name: The name of the resource.
        :param AnomalySecurityMLAnalyticsSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnomalySecurityMLAnalyticsSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 anomaly_settings_version: Optional[pulumi.Input[int]] = None,
                 anomaly_version: Optional[pulumi.Input[str]] = None,
                 customizable_observations: Optional[Any] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 frequency: Optional[pulumi.Input[str]] = None,
                 is_default_settings: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 required_data_connectors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityMLAnalyticsSettingsDataSourceArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 settings_definition_id: Optional[pulumi.Input[str]] = None,
                 settings_resource_name: Optional[pulumi.Input[str]] = None,
                 settings_status: Optional[pulumi.Input[Union[str, 'SettingsStatus']]] = None,
                 tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AttackTactic']]]]] = None,
                 techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnomalySecurityMLAnalyticsSettingsArgs.__new__(AnomalySecurityMLAnalyticsSettingsArgs)

            __props__.__dict__["anomaly_settings_version"] = anomaly_settings_version
            if anomaly_version is None and not opts.urn:
                raise TypeError("Missing required property 'anomaly_version'")
            __props__.__dict__["anomaly_version"] = anomaly_version
            __props__.__dict__["customizable_observations"] = customizable_observations
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            if frequency is None and not opts.urn:
                raise TypeError("Missing required property 'frequency'")
            __props__.__dict__["frequency"] = frequency
            if is_default_settings is None and not opts.urn:
                raise TypeError("Missing required property 'is_default_settings'")
            __props__.__dict__["is_default_settings"] = is_default_settings
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'Anomaly'
            __props__.__dict__["required_data_connectors"] = required_data_connectors
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["settings_definition_id"] = settings_definition_id
            __props__.__dict__["settings_resource_name"] = settings_resource_name
            if settings_status is None and not opts.urn:
                raise TypeError("Missing required property 'settings_status'")
            __props__.__dict__["settings_status"] = settings_status
            __props__.__dict__["tactics"] = tactics
            __props__.__dict__["techniques"] = techniques
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["last_modified_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20221101:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20230201:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20231101:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:AnomalySecurityMLAnalyticsSettings"), pulumi.Alias(type_="azure-native:securityinsights/v20240301:AnomalySecurityMLAnalyticsSettings")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AnomalySecurityMLAnalyticsSettings, __self__).__init__(
            'azure-native:securityinsights/v20230701preview:AnomalySecurityMLAnalyticsSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AnomalySecurityMLAnalyticsSettings':
        """
        Get an existing AnomalySecurityMLAnalyticsSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AnomalySecurityMLAnalyticsSettingsArgs.__new__(AnomalySecurityMLAnalyticsSettingsArgs)

        __props__.__dict__["anomaly_settings_version"] = None
        __props__.__dict__["anomaly_version"] = None
        __props__.__dict__["customizable_observations"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["frequency"] = None
        __props__.__dict__["is_default_settings"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["last_modified_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["required_data_connectors"] = None
        __props__.__dict__["settings_definition_id"] = None
        __props__.__dict__["settings_status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tactics"] = None
        __props__.__dict__["techniques"] = None
        __props__.__dict__["type"] = None
        return AnomalySecurityMLAnalyticsSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="anomalySettingsVersion")
    def anomaly_settings_version(self) -> pulumi.Output[Optional[int]]:
        """
        The anomaly settings version of the Anomaly security ml analytics settings that dictates whether job version gets updated or not.
        """
        return pulumi.get(self, "anomaly_settings_version")

    @property
    @pulumi.getter(name="anomalyVersion")
    def anomaly_version(self) -> pulumi.Output[str]:
        """
        The anomaly version of the AnomalySecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "anomaly_version")

    @property
    @pulumi.getter(name="customizableObservations")
    def customizable_observations(self) -> pulumi.Output[Optional[Any]]:
        """
        The customizable observations of the AnomalySecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "customizable_observations")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the SecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name for settings created by this SecurityMLAnalyticsSettings.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Determines whether this settings is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[str]:
        """
        The frequency that this SecurityMLAnalyticsSettings will be run.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter(name="isDefaultSettings")
    def is_default_settings(self) -> pulumi.Output[bool]:
        """
        Determines whether this anomaly security ml analytics settings is a default settings
        """
        return pulumi.get(self, "is_default_settings")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The kind of security ML analytics settings
        Expected value is 'Anomaly'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> pulumi.Output[str]:
        """
        The last time that this SecurityMLAnalyticsSettings has been modified.
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
    @pulumi.getter(name="requiredDataConnectors")
    def required_data_connectors(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityMLAnalyticsSettingsDataSourceResponse']]]:
        """
        The required data sources for this SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "required_data_connectors")

    @property
    @pulumi.getter(name="settingsDefinitionId")
    def settings_definition_id(self) -> pulumi.Output[Optional[str]]:
        """
        The anomaly settings definition Id
        """
        return pulumi.get(self, "settings_definition_id")

    @property
    @pulumi.getter(name="settingsStatus")
    def settings_status(self) -> pulumi.Output[str]:
        """
        The anomaly SecurityMLAnalyticsSettings status
        """
        return pulumi.get(self, "settings_status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tactics(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tactics of the SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "tactics")

    @property
    @pulumi.getter
    def techniques(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The techniques of the SecurityMLAnalyticsSettings
        """
        return pulumi.get(self, "techniques")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

