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

__all__ = ['DefenderForStorageArgs', 'DefenderForStorage']

@pulumi.input_type
class DefenderForStorageArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[str],
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 malware_scanning: Optional[pulumi.Input['MalwareScanningPropertiesArgs']] = None,
                 override_subscription_level_settings: Optional[pulumi.Input[bool]] = None,
                 sensitive_data_discovery: Optional[pulumi.Input['SensitiveDataDiscoveryPropertiesArgs']] = None,
                 setting_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DefenderForStorage resource.
        :param pulumi.Input[str] resource_id: The identifier of the resource.
        :param pulumi.Input[bool] is_enabled: Indicates whether Defender for Storage is enabled on this storage account.
        :param pulumi.Input['MalwareScanningPropertiesArgs'] malware_scanning: Properties of Malware Scanning.
        :param pulumi.Input[bool] override_subscription_level_settings: Indicates whether the settings defined for this storage account should override the settings defined for the subscription.
        :param pulumi.Input['SensitiveDataDiscoveryPropertiesArgs'] sensitive_data_discovery: Properties of Sensitive Data Discovery.
        :param pulumi.Input[str] setting_name: Defender for Storage setting name.
        """
        pulumi.set(__self__, "resource_id", resource_id)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if malware_scanning is not None:
            pulumi.set(__self__, "malware_scanning", malware_scanning)
        if override_subscription_level_settings is not None:
            pulumi.set(__self__, "override_subscription_level_settings", override_subscription_level_settings)
        if sensitive_data_discovery is not None:
            pulumi.set(__self__, "sensitive_data_discovery", sensitive_data_discovery)
        if setting_name is not None:
            pulumi.set(__self__, "setting_name", setting_name)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether Defender for Storage is enabled on this storage account.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter(name="malwareScanning")
    def malware_scanning(self) -> Optional[pulumi.Input['MalwareScanningPropertiesArgs']]:
        """
        Properties of Malware Scanning.
        """
        return pulumi.get(self, "malware_scanning")

    @malware_scanning.setter
    def malware_scanning(self, value: Optional[pulumi.Input['MalwareScanningPropertiesArgs']]):
        pulumi.set(self, "malware_scanning", value)

    @property
    @pulumi.getter(name="overrideSubscriptionLevelSettings")
    def override_subscription_level_settings(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the settings defined for this storage account should override the settings defined for the subscription.
        """
        return pulumi.get(self, "override_subscription_level_settings")

    @override_subscription_level_settings.setter
    def override_subscription_level_settings(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "override_subscription_level_settings", value)

    @property
    @pulumi.getter(name="sensitiveDataDiscovery")
    def sensitive_data_discovery(self) -> Optional[pulumi.Input['SensitiveDataDiscoveryPropertiesArgs']]:
        """
        Properties of Sensitive Data Discovery.
        """
        return pulumi.get(self, "sensitive_data_discovery")

    @sensitive_data_discovery.setter
    def sensitive_data_discovery(self, value: Optional[pulumi.Input['SensitiveDataDiscoveryPropertiesArgs']]):
        pulumi.set(self, "sensitive_data_discovery", value)

    @property
    @pulumi.getter(name="settingName")
    def setting_name(self) -> Optional[pulumi.Input[str]]:
        """
        Defender for Storage setting name.
        """
        return pulumi.get(self, "setting_name")

    @setting_name.setter
    def setting_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "setting_name", value)


class DefenderForStorage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 malware_scanning: Optional[pulumi.Input[pulumi.InputType['MalwareScanningPropertiesArgs']]] = None,
                 override_subscription_level_settings: Optional[pulumi.Input[bool]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 sensitive_data_discovery: Optional[pulumi.Input[pulumi.InputType['SensitiveDataDiscoveryPropertiesArgs']]] = None,
                 setting_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Defender for Storage resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] is_enabled: Indicates whether Defender for Storage is enabled on this storage account.
        :param pulumi.Input[pulumi.InputType['MalwareScanningPropertiesArgs']] malware_scanning: Properties of Malware Scanning.
        :param pulumi.Input[bool] override_subscription_level_settings: Indicates whether the settings defined for this storage account should override the settings defined for the subscription.
        :param pulumi.Input[str] resource_id: The identifier of the resource.
        :param pulumi.Input[pulumi.InputType['SensitiveDataDiscoveryPropertiesArgs']] sensitive_data_discovery: Properties of Sensitive Data Discovery.
        :param pulumi.Input[str] setting_name: Defender for Storage setting name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DefenderForStorageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Defender for Storage resource.

        :param str resource_name: The name of the resource.
        :param DefenderForStorageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefenderForStorageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 malware_scanning: Optional[pulumi.Input[pulumi.InputType['MalwareScanningPropertiesArgs']]] = None,
                 override_subscription_level_settings: Optional[pulumi.Input[bool]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 sensitive_data_discovery: Optional[pulumi.Input[pulumi.InputType['SensitiveDataDiscoveryPropertiesArgs']]] = None,
                 setting_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefenderForStorageArgs.__new__(DefenderForStorageArgs)

            __props__.__dict__["is_enabled"] = is_enabled
            __props__.__dict__["malware_scanning"] = malware_scanning
            __props__.__dict__["override_subscription_level_settings"] = override_subscription_level_settings
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["sensitive_data_discovery"] = sensitive_data_discovery
            __props__.__dict__["setting_name"] = setting_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:DefenderForStorage")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DefenderForStorage, __self__).__init__(
            'azure-native:security/v20221201preview:DefenderForStorage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DefenderForStorage':
        """
        Get an existing DefenderForStorage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DefenderForStorageArgs.__new__(DefenderForStorageArgs)

        __props__.__dict__["is_enabled"] = None
        __props__.__dict__["malware_scanning"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["override_subscription_level_settings"] = None
        __props__.__dict__["sensitive_data_discovery"] = None
        __props__.__dict__["type"] = None
        return DefenderForStorage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether Defender for Storage is enabled on this storage account.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="malwareScanning")
    def malware_scanning(self) -> pulumi.Output[Optional['outputs.MalwareScanningPropertiesResponse']]:
        """
        Properties of Malware Scanning.
        """
        return pulumi.get(self, "malware_scanning")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="overrideSubscriptionLevelSettings")
    def override_subscription_level_settings(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the settings defined for this storage account should override the settings defined for the subscription.
        """
        return pulumi.get(self, "override_subscription_level_settings")

    @property
    @pulumi.getter(name="sensitiveDataDiscovery")
    def sensitive_data_discovery(self) -> pulumi.Output[Optional['outputs.SensitiveDataDiscoveryPropertiesResponse']]:
        """
        Properties of Sensitive Data Discovery.
        """
        return pulumi.get(self, "sensitive_data_discovery")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

