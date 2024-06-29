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

__all__ = ['ExtensionArgs', 'Extension']

@pulumi.input_type
class ExtensionArgs:
    def __init__(__self__, *,
                 arc_setting_name: pulumi.Input[str],
                 cluster_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auto_upgrade_minor_version: Optional[pulumi.Input[bool]] = None,
                 enable_automatic_upgrade: Optional[pulumi.Input[bool]] = None,
                 extension_name: Optional[pulumi.Input[str]] = None,
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 protected_settings: Optional[Any] = None,
                 publisher: Optional[pulumi.Input[str]] = None,
                 settings: Optional[Any] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_handler_version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Extension resource.
        :param pulumi.Input[str] arc_setting_name: The name of the proxy resource holding details of HCI ArcSetting information.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[bool] auto_upgrade_minor_version: Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
        :param pulumi.Input[bool] enable_automatic_upgrade: Indicates whether the extension should be automatically upgraded by the platform if there is a newer version available.
        :param pulumi.Input[str] extension_name: The name of the machine extension.
        :param pulumi.Input[str] force_update_tag: How the extension handler should be forced to update even if the extension configuration has not changed.
        :param Any protected_settings: Protected settings (may contain secrets).
        :param pulumi.Input[str] publisher: The name of the extension handler publisher.
        :param Any settings: Json formatted public settings for the extension.
        :param pulumi.Input[str] type: Specifies the type of the extension; an example is "CustomScriptExtension".
        :param pulumi.Input[str] type_handler_version: Specifies the version of the script handler. Latest version would be used if not specified.
        """
        pulumi.set(__self__, "arc_setting_name", arc_setting_name)
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_upgrade_minor_version is not None:
            pulumi.set(__self__, "auto_upgrade_minor_version", auto_upgrade_minor_version)
        if enable_automatic_upgrade is not None:
            pulumi.set(__self__, "enable_automatic_upgrade", enable_automatic_upgrade)
        if extension_name is not None:
            pulumi.set(__self__, "extension_name", extension_name)
        if force_update_tag is not None:
            pulumi.set(__self__, "force_update_tag", force_update_tag)
        if protected_settings is not None:
            pulumi.set(__self__, "protected_settings", protected_settings)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if type_handler_version is not None:
            pulumi.set(__self__, "type_handler_version", type_handler_version)

    @property
    @pulumi.getter(name="arcSettingName")
    def arc_setting_name(self) -> pulumi.Input[str]:
        """
        The name of the proxy resource holding details of HCI ArcSetting information.
        """
        return pulumi.get(self, "arc_setting_name")

    @arc_setting_name.setter
    def arc_setting_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "arc_setting_name", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

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
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
        """
        return pulumi.get(self, "auto_upgrade_minor_version")

    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_upgrade_minor_version", value)

    @property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the extension should be automatically upgraded by the platform if there is a newer version available.
        """
        return pulumi.get(self, "enable_automatic_upgrade")

    @enable_automatic_upgrade.setter
    def enable_automatic_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_automatic_upgrade", value)

    @property
    @pulumi.getter(name="extensionName")
    def extension_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the machine extension.
        """
        return pulumi.get(self, "extension_name")

    @extension_name.setter
    def extension_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extension_name", value)

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[str]]:
        """
        How the extension handler should be forced to update even if the extension configuration has not changed.
        """
        return pulumi.get(self, "force_update_tag")

    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "force_update_tag", value)

    @property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        """
        Protected settings (may contain secrets).
        """
        return pulumi.get(self, "protected_settings")

    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]):
        pulumi.set(self, "protected_settings", value)

    @property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the extension handler publisher.
        """
        return pulumi.get(self, "publisher")

    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publisher", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        """
        Json formatted public settings for the extension.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[Any]):
        pulumi.set(self, "settings", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of the extension; an example is "CustomScriptExtension".
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the version of the script handler. Latest version would be used if not specified.
        """
        return pulumi.get(self, "type_handler_version")

    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_handler_version", value)


class Extension(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arc_setting_name: Optional[pulumi.Input[str]] = None,
                 auto_upgrade_minor_version: Optional[pulumi.Input[bool]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 enable_automatic_upgrade: Optional[pulumi.Input[bool]] = None,
                 extension_name: Optional[pulumi.Input[str]] = None,
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 protected_settings: Optional[Any] = None,
                 publisher: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 settings: Optional[Any] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_handler_version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Details of a particular extension in HCI Cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arc_setting_name: The name of the proxy resource holding details of HCI ArcSetting information.
        :param pulumi.Input[bool] auto_upgrade_minor_version: Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
        :param pulumi.Input[str] cluster_name: The name of the cluster.
        :param pulumi.Input[bool] enable_automatic_upgrade: Indicates whether the extension should be automatically upgraded by the platform if there is a newer version available.
        :param pulumi.Input[str] extension_name: The name of the machine extension.
        :param pulumi.Input[str] force_update_tag: How the extension handler should be forced to update even if the extension configuration has not changed.
        :param Any protected_settings: Protected settings (may contain secrets).
        :param pulumi.Input[str] publisher: The name of the extension handler publisher.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param Any settings: Json formatted public settings for the extension.
        :param pulumi.Input[str] type: Specifies the type of the extension; an example is "CustomScriptExtension".
        :param pulumi.Input[str] type_handler_version: Specifies the version of the script handler. Latest version would be used if not specified.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExtensionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Details of a particular extension in HCI Cluster.

        :param str resource_name: The name of the resource.
        :param ExtensionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExtensionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arc_setting_name: Optional[pulumi.Input[str]] = None,
                 auto_upgrade_minor_version: Optional[pulumi.Input[bool]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 enable_automatic_upgrade: Optional[pulumi.Input[bool]] = None,
                 extension_name: Optional[pulumi.Input[str]] = None,
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 protected_settings: Optional[Any] = None,
                 publisher: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 settings: Optional[Any] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_handler_version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExtensionArgs.__new__(ExtensionArgs)

            if arc_setting_name is None and not opts.urn:
                raise TypeError("Missing required property 'arc_setting_name'")
            __props__.__dict__["arc_setting_name"] = arc_setting_name
            __props__.__dict__["auto_upgrade_minor_version"] = auto_upgrade_minor_version
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["enable_automatic_upgrade"] = enable_automatic_upgrade
            __props__.__dict__["extension_name"] = extension_name
            __props__.__dict__["force_update_tag"] = force_update_tag
            __props__.__dict__["protected_settings"] = protected_settings
            __props__.__dict__["publisher"] = publisher
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["settings"] = settings
            __props__.__dict__["type"] = type
            __props__.__dict__["type_handler_version"] = type_handler_version
            __props__.__dict__["aggregate_state"] = None
            __props__.__dict__["managed_by"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["per_node_extension_details"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20210101preview:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20210901:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20210901preview:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20220101:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20220301:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20220501:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20220901:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20221001:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20221201:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20230201:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20230301:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20230601:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20230801:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20230801preview:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20240215preview:Extension"), pulumi.Alias(type_="azure-native:azurestackhci/v20240401:Extension")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Extension, __self__).__init__(
            'azure-native:azurestackhci/v20231101preview:Extension',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Extension':
        """
        Get an existing Extension resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExtensionArgs.__new__(ExtensionArgs)

        __props__.__dict__["aggregate_state"] = None
        __props__.__dict__["auto_upgrade_minor_version"] = None
        __props__.__dict__["enable_automatic_upgrade"] = None
        __props__.__dict__["force_update_tag"] = None
        __props__.__dict__["managed_by"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["per_node_extension_details"] = None
        __props__.__dict__["protected_settings"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["publisher"] = None
        __props__.__dict__["settings"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["type_handler_version"] = None
        return Extension(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aggregateState")
    def aggregate_state(self) -> pulumi.Output[str]:
        """
        Aggregate state of Arc Extensions across the nodes in this HCI cluster.
        """
        return pulumi.get(self, "aggregate_state")

    @property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
        """
        return pulumi.get(self, "auto_upgrade_minor_version")

    @property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether the extension should be automatically upgraded by the platform if there is a newer version available.
        """
        return pulumi.get(self, "enable_automatic_upgrade")

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> pulumi.Output[Optional[str]]:
        """
        How the extension handler should be forced to update even if the extension configuration has not changed.
        """
        return pulumi.get(self, "force_update_tag")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> pulumi.Output[str]:
        """
        Indicates if the extension is managed by azure or the user.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perNodeExtensionDetails")
    def per_node_extension_details(self) -> pulumi.Output[Sequence['outputs.PerNodeExtensionStateResponse']]:
        """
        State of Arc Extension in each of the nodes.
        """
        return pulumi.get(self, "per_node_extension_details")

    @property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> pulumi.Output[Optional[Any]]:
        """
        Protected settings (may contain secrets).
        """
        return pulumi.get(self, "protected_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Extension proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def publisher(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the extension handler publisher.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional[Any]]:
        """
        Json formatted public settings for the extension.
        """
        return pulumi.get(self, "settings")

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

    @property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the version of the script handler. Latest version would be used if not specified.
        """
        return pulumi.get(self, "type_handler_version")

