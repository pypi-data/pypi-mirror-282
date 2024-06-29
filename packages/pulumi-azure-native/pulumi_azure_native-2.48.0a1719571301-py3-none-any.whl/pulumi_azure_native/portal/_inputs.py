# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'ConsoleCreatePropertiesArgs',
    'DashboardLensArgs',
    'DashboardPartMetadataArgs',
    'DashboardPartsPositionArgs',
    'DashboardPartsArgs',
    'StorageProfileArgs',
    'TerminalSettingsArgs',
    'UserPropertiesArgs',
]

@pulumi.input_type
class ConsoleCreatePropertiesArgs:
    def __init__(__self__, *,
                 os_type: pulumi.Input[Union[str, 'OsType']],
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        Cloud shell properties for creating a console.
        :param pulumi.Input[Union[str, 'OsType']] os_type: The operating system type of the cloud shell.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: Provisioning state of the console.
        :param pulumi.Input[str] uri: Uri of the console.
        """
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Input[Union[str, 'OsType']]:
        """
        The operating system type of the cloud shell.
        """
        return pulumi.get(self, "os_type")

    @os_type.setter
    def os_type(self, value: pulumi.Input[Union[str, 'OsType']]):
        pulumi.set(self, "os_type", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningState']]]:
        """
        Provisioning state of the console.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        Uri of the console.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


@pulumi.input_type
class DashboardLensArgs:
    def __init__(__self__, *,
                 order: pulumi.Input[int],
                 parts: pulumi.Input[Sequence[pulumi.Input['DashboardPartsArgs']]],
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        A dashboard lens.
        :param pulumi.Input[int] order: The lens order.
        :param pulumi.Input[Sequence[pulumi.Input['DashboardPartsArgs']]] parts: The dashboard parts.
        :param pulumi.Input[Mapping[str, Any]] metadata: The dashboard len's metadata.
        """
        pulumi.set(__self__, "order", order)
        pulumi.set(__self__, "parts", parts)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[int]:
        """
        The lens order.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[int]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def parts(self) -> pulumi.Input[Sequence[pulumi.Input['DashboardPartsArgs']]]:
        """
        The dashboard parts.
        """
        return pulumi.get(self, "parts")

    @parts.setter
    def parts(self, value: pulumi.Input[Sequence[pulumi.Input['DashboardPartsArgs']]]):
        pulumi.set(self, "parts", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The dashboard len's metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "metadata", value)


@pulumi.input_type
class DashboardPartMetadataArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 inputs: Optional[pulumi.Input[Sequence[Any]]] = None,
                 settings: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        A dashboard part metadata.
        :param pulumi.Input[str] type: The type of dashboard part.
        :param pulumi.Input[Sequence[Any]] inputs: Inputs to dashboard part.
        :param pulumi.Input[Mapping[str, Any]] settings: Settings of dashboard part.
        """
        pulumi.set(__self__, "type", type)
        if inputs is not None:
            pulumi.set(__self__, "inputs", inputs)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of dashboard part.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def inputs(self) -> Optional[pulumi.Input[Sequence[Any]]]:
        """
        Inputs to dashboard part.
        """
        return pulumi.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: Optional[pulumi.Input[Sequence[Any]]]):
        pulumi.set(self, "inputs", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Settings of dashboard part.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "settings", value)


@pulumi.input_type
class DashboardPartsPositionArgs:
    def __init__(__self__, *,
                 col_span: pulumi.Input[int],
                 row_span: pulumi.Input[int],
                 x: pulumi.Input[int],
                 y: pulumi.Input[int],
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The dashboard's part position.
        :param pulumi.Input[int] col_span: The dashboard's part column span.
        :param pulumi.Input[int] row_span: The dashboard's part row span.
        :param pulumi.Input[int] x: The dashboard's part x coordinate.
        :param pulumi.Input[int] y: The dashboard's part y coordinate.
        :param pulumi.Input[Mapping[str, Any]] metadata: The dashboard part's metadata.
        """
        pulumi.set(__self__, "col_span", col_span)
        pulumi.set(__self__, "row_span", row_span)
        pulumi.set(__self__, "x", x)
        pulumi.set(__self__, "y", y)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)

    @property
    @pulumi.getter(name="colSpan")
    def col_span(self) -> pulumi.Input[int]:
        """
        The dashboard's part column span.
        """
        return pulumi.get(self, "col_span")

    @col_span.setter
    def col_span(self, value: pulumi.Input[int]):
        pulumi.set(self, "col_span", value)

    @property
    @pulumi.getter(name="rowSpan")
    def row_span(self) -> pulumi.Input[int]:
        """
        The dashboard's part row span.
        """
        return pulumi.get(self, "row_span")

    @row_span.setter
    def row_span(self, value: pulumi.Input[int]):
        pulumi.set(self, "row_span", value)

    @property
    @pulumi.getter
    def x(self) -> pulumi.Input[int]:
        """
        The dashboard's part x coordinate.
        """
        return pulumi.get(self, "x")

    @x.setter
    def x(self, value: pulumi.Input[int]):
        pulumi.set(self, "x", value)

    @property
    @pulumi.getter
    def y(self) -> pulumi.Input[int]:
        """
        The dashboard's part y coordinate.
        """
        return pulumi.get(self, "y")

    @y.setter
    def y(self, value: pulumi.Input[int]):
        pulumi.set(self, "y", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The dashboard part's metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "metadata", value)


@pulumi.input_type
class DashboardPartsArgs:
    def __init__(__self__, *,
                 position: pulumi.Input['DashboardPartsPositionArgs'],
                 metadata: Optional[pulumi.Input['DashboardPartMetadataArgs']] = None):
        """
        A dashboard part.
        :param pulumi.Input['DashboardPartsPositionArgs'] position: The dashboard's part position.
        :param pulumi.Input['DashboardPartMetadataArgs'] metadata: The dashboard's part metadata.
        """
        pulumi.set(__self__, "position", position)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input['DashboardPartsPositionArgs']:
        """
        The dashboard's part position.
        """
        return pulumi.get(self, "position")

    @position.setter
    def position(self, value: pulumi.Input['DashboardPartsPositionArgs']):
        pulumi.set(self, "position", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['DashboardPartMetadataArgs']]:
        """
        The dashboard's part metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['DashboardPartMetadataArgs']]):
        pulumi.set(self, "metadata", value)


@pulumi.input_type
class StorageProfileArgs:
    def __init__(__self__, *,
                 disk_size_in_gb: Optional[pulumi.Input[int]] = None,
                 file_share_name: Optional[pulumi.Input[str]] = None,
                 storage_account_resource_id: Optional[pulumi.Input[str]] = None):
        """
        The storage profile of the user settings.
        :param pulumi.Input[int] disk_size_in_gb: Size of file share
        :param pulumi.Input[str] file_share_name: Name of the mounted file share. 63 characters or less, lowercase alphabet, numbers, and -
        :param pulumi.Input[str] storage_account_resource_id: Full resource ID of storage account.
        """
        if disk_size_in_gb is not None:
            pulumi.set(__self__, "disk_size_in_gb", disk_size_in_gb)
        if file_share_name is not None:
            pulumi.set(__self__, "file_share_name", file_share_name)
        if storage_account_resource_id is not None:
            pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)

    @property
    @pulumi.getter(name="diskSizeInGB")
    def disk_size_in_gb(self) -> Optional[pulumi.Input[int]]:
        """
        Size of file share
        """
        return pulumi.get(self, "disk_size_in_gb")

    @disk_size_in_gb.setter
    def disk_size_in_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_size_in_gb", value)

    @property
    @pulumi.getter(name="fileShareName")
    def file_share_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the mounted file share. 63 characters or less, lowercase alphabet, numbers, and -
        """
        return pulumi.get(self, "file_share_name")

    @file_share_name.setter
    def file_share_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_share_name", value)

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Full resource ID of storage account.
        """
        return pulumi.get(self, "storage_account_resource_id")

    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_resource_id", value)


@pulumi.input_type
class TerminalSettingsArgs:
    def __init__(__self__, *,
                 font_size: Optional[pulumi.Input[Union[str, 'FontSize']]] = None,
                 font_style: Optional[pulumi.Input[Union[str, 'FontStyle']]] = None):
        """
        Settings for terminal appearance.
        :param pulumi.Input[Union[str, 'FontSize']] font_size: Size of terminal font.
        :param pulumi.Input[Union[str, 'FontStyle']] font_style: Style of terminal font.
        """
        if font_size is not None:
            pulumi.set(__self__, "font_size", font_size)
        if font_style is not None:
            pulumi.set(__self__, "font_style", font_style)

    @property
    @pulumi.getter(name="fontSize")
    def font_size(self) -> Optional[pulumi.Input[Union[str, 'FontSize']]]:
        """
        Size of terminal font.
        """
        return pulumi.get(self, "font_size")

    @font_size.setter
    def font_size(self, value: Optional[pulumi.Input[Union[str, 'FontSize']]]):
        pulumi.set(self, "font_size", value)

    @property
    @pulumi.getter(name="fontStyle")
    def font_style(self) -> Optional[pulumi.Input[Union[str, 'FontStyle']]]:
        """
        Style of terminal font.
        """
        return pulumi.get(self, "font_style")

    @font_style.setter
    def font_style(self, value: Optional[pulumi.Input[Union[str, 'FontStyle']]]):
        pulumi.set(self, "font_style", value)


@pulumi.input_type
class UserPropertiesArgs:
    def __init__(__self__, *,
                 preferred_location: pulumi.Input[str],
                 preferred_os_type: pulumi.Input[Union[str, 'OsType']],
                 preferred_shell_type: pulumi.Input[Union[str, 'ShellType']],
                 storage_profile: pulumi.Input['StorageProfileArgs'],
                 terminal_settings: pulumi.Input['TerminalSettingsArgs']):
        """
        The cloud shell user settings properties.
        :param pulumi.Input[str] preferred_location: The preferred location of the cloud shell.
        :param pulumi.Input[Union[str, 'OsType']] preferred_os_type: The operating system type of the cloud shell. Deprecated, use preferredShellType.
        :param pulumi.Input[Union[str, 'ShellType']] preferred_shell_type: The shell type of the cloud shell.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: The storage profile of the user settings.
        :param pulumi.Input['TerminalSettingsArgs'] terminal_settings: Settings for terminal appearance.
        """
        pulumi.set(__self__, "preferred_location", preferred_location)
        pulumi.set(__self__, "preferred_os_type", preferred_os_type)
        pulumi.set(__self__, "preferred_shell_type", preferred_shell_type)
        pulumi.set(__self__, "storage_profile", storage_profile)
        pulumi.set(__self__, "terminal_settings", terminal_settings)

    @property
    @pulumi.getter(name="preferredLocation")
    def preferred_location(self) -> pulumi.Input[str]:
        """
        The preferred location of the cloud shell.
        """
        return pulumi.get(self, "preferred_location")

    @preferred_location.setter
    def preferred_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "preferred_location", value)

    @property
    @pulumi.getter(name="preferredOsType")
    def preferred_os_type(self) -> pulumi.Input[Union[str, 'OsType']]:
        """
        The operating system type of the cloud shell. Deprecated, use preferredShellType.
        """
        return pulumi.get(self, "preferred_os_type")

    @preferred_os_type.setter
    def preferred_os_type(self, value: pulumi.Input[Union[str, 'OsType']]):
        pulumi.set(self, "preferred_os_type", value)

    @property
    @pulumi.getter(name="preferredShellType")
    def preferred_shell_type(self) -> pulumi.Input[Union[str, 'ShellType']]:
        """
        The shell type of the cloud shell.
        """
        return pulumi.get(self, "preferred_shell_type")

    @preferred_shell_type.setter
    def preferred_shell_type(self, value: pulumi.Input[Union[str, 'ShellType']]):
        pulumi.set(self, "preferred_shell_type", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> pulumi.Input['StorageProfileArgs']:
        """
        The storage profile of the user settings.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: pulumi.Input['StorageProfileArgs']):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter(name="terminalSettings")
    def terminal_settings(self) -> pulumi.Input['TerminalSettingsArgs']:
        """
        Settings for terminal appearance.
        """
        return pulumi.get(self, "terminal_settings")

    @terminal_settings.setter
    def terminal_settings(self, value: pulumi.Input['TerminalSettingsArgs']):
        pulumi.set(self, "terminal_settings", value)


