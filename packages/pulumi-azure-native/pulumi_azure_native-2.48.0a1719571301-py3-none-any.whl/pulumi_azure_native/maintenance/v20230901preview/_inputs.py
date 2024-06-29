# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ConfigurationAssignmentFilterPropertiesArgs',
    'InputLinuxParametersArgs',
    'InputPatchConfigurationArgs',
    'InputWindowsParametersArgs',
    'TagSettingsPropertiesArgs',
]

@pulumi.input_type
class ConfigurationAssignmentFilterPropertiesArgs:
    def __init__(__self__, *,
                 locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 os_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tag_settings: Optional[pulumi.Input['TagSettingsPropertiesArgs']] = None):
        """
        Azure query for the update configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locations: List of locations to scope the query to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] os_types: List of allowed operating systems.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_groups: List of allowed resource groups.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] resource_types: List of allowed resources.
        :param pulumi.Input['TagSettingsPropertiesArgs'] tag_settings: Tag settings for the VM.
        """
        if locations is not None:
            pulumi.set(__self__, "locations", locations)
        if os_types is not None:
            pulumi.set(__self__, "os_types", os_types)
        if resource_groups is not None:
            pulumi.set(__self__, "resource_groups", resource_groups)
        if resource_types is not None:
            pulumi.set(__self__, "resource_types", resource_types)
        if tag_settings is not None:
            pulumi.set(__self__, "tag_settings", tag_settings)

    @property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of locations to scope the query to.
        """
        return pulumi.get(self, "locations")

    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "locations", value)

    @property
    @pulumi.getter(name="osTypes")
    def os_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of allowed operating systems.
        """
        return pulumi.get(self, "os_types")

    @os_types.setter
    def os_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "os_types", value)

    @property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of allowed resource groups.
        """
        return pulumi.get(self, "resource_groups")

    @resource_groups.setter
    def resource_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resource_groups", value)

    @property
    @pulumi.getter(name="resourceTypes")
    def resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of allowed resources.
        """
        return pulumi.get(self, "resource_types")

    @resource_types.setter
    def resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "resource_types", value)

    @property
    @pulumi.getter(name="tagSettings")
    def tag_settings(self) -> Optional[pulumi.Input['TagSettingsPropertiesArgs']]:
        """
        Tag settings for the VM.
        """
        return pulumi.get(self, "tag_settings")

    @tag_settings.setter
    def tag_settings(self, value: Optional[pulumi.Input['TagSettingsPropertiesArgs']]):
        pulumi.set(self, "tag_settings", value)


@pulumi.input_type
class InputLinuxParametersArgs:
    def __init__(__self__, *,
                 classifications_to_include: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 package_name_masks_to_exclude: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 package_name_masks_to_include: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties for patching a Linux machine.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] classifications_to_include: Classification category of patches to be patched
        :param pulumi.Input[Sequence[pulumi.Input[str]]] package_name_masks_to_exclude: Package names to be excluded for patching.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] package_name_masks_to_include: Package names to be included for patching.
        """
        if classifications_to_include is not None:
            pulumi.set(__self__, "classifications_to_include", classifications_to_include)
        if package_name_masks_to_exclude is not None:
            pulumi.set(__self__, "package_name_masks_to_exclude", package_name_masks_to_exclude)
        if package_name_masks_to_include is not None:
            pulumi.set(__self__, "package_name_masks_to_include", package_name_masks_to_include)

    @property
    @pulumi.getter(name="classificationsToInclude")
    def classifications_to_include(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Classification category of patches to be patched
        """
        return pulumi.get(self, "classifications_to_include")

    @classifications_to_include.setter
    def classifications_to_include(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "classifications_to_include", value)

    @property
    @pulumi.getter(name="packageNameMasksToExclude")
    def package_name_masks_to_exclude(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Package names to be excluded for patching.
        """
        return pulumi.get(self, "package_name_masks_to_exclude")

    @package_name_masks_to_exclude.setter
    def package_name_masks_to_exclude(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "package_name_masks_to_exclude", value)

    @property
    @pulumi.getter(name="packageNameMasksToInclude")
    def package_name_masks_to_include(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Package names to be included for patching.
        """
        return pulumi.get(self, "package_name_masks_to_include")

    @package_name_masks_to_include.setter
    def package_name_masks_to_include(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "package_name_masks_to_include", value)


@pulumi.input_type
class InputPatchConfigurationArgs:
    def __init__(__self__, *,
                 linux_parameters: Optional[pulumi.Input['InputLinuxParametersArgs']] = None,
                 reboot_setting: Optional[pulumi.Input[Union[str, 'RebootOptions']]] = None,
                 windows_parameters: Optional[pulumi.Input['InputWindowsParametersArgs']] = None):
        """
        Input configuration for a patch run
        :param pulumi.Input['InputLinuxParametersArgs'] linux_parameters: Input parameters specific to patching Linux machine. For Windows machines, do not pass this property.
        :param pulumi.Input[Union[str, 'RebootOptions']] reboot_setting: Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed.
        :param pulumi.Input['InputWindowsParametersArgs'] windows_parameters: Input parameters specific to patching a Windows machine. For Linux machines, do not pass this property.
        """
        if linux_parameters is not None:
            pulumi.set(__self__, "linux_parameters", linux_parameters)
        if reboot_setting is None:
            reboot_setting = 'IfRequired'
        if reboot_setting is not None:
            pulumi.set(__self__, "reboot_setting", reboot_setting)
        if windows_parameters is not None:
            pulumi.set(__self__, "windows_parameters", windows_parameters)

    @property
    @pulumi.getter(name="linuxParameters")
    def linux_parameters(self) -> Optional[pulumi.Input['InputLinuxParametersArgs']]:
        """
        Input parameters specific to patching Linux machine. For Windows machines, do not pass this property.
        """
        return pulumi.get(self, "linux_parameters")

    @linux_parameters.setter
    def linux_parameters(self, value: Optional[pulumi.Input['InputLinuxParametersArgs']]):
        pulumi.set(self, "linux_parameters", value)

    @property
    @pulumi.getter(name="rebootSetting")
    def reboot_setting(self) -> Optional[pulumi.Input[Union[str, 'RebootOptions']]]:
        """
        Possible reboot preference as defined by the user based on which it would be decided to reboot the machine or not after the patch operation is completed.
        """
        return pulumi.get(self, "reboot_setting")

    @reboot_setting.setter
    def reboot_setting(self, value: Optional[pulumi.Input[Union[str, 'RebootOptions']]]):
        pulumi.set(self, "reboot_setting", value)

    @property
    @pulumi.getter(name="windowsParameters")
    def windows_parameters(self) -> Optional[pulumi.Input['InputWindowsParametersArgs']]:
        """
        Input parameters specific to patching a Windows machine. For Linux machines, do not pass this property.
        """
        return pulumi.get(self, "windows_parameters")

    @windows_parameters.setter
    def windows_parameters(self, value: Optional[pulumi.Input['InputWindowsParametersArgs']]):
        pulumi.set(self, "windows_parameters", value)


@pulumi.input_type
class InputWindowsParametersArgs:
    def __init__(__self__, *,
                 classifications_to_include: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 exclude_kbs_requiring_reboot: Optional[pulumi.Input[bool]] = None,
                 kb_numbers_to_exclude: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 kb_numbers_to_include: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties for patching a Windows machine.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] classifications_to_include: Classification category of patches to be patched
        :param pulumi.Input[bool] exclude_kbs_requiring_reboot: Exclude patches which need reboot
        :param pulumi.Input[Sequence[pulumi.Input[str]]] kb_numbers_to_exclude: Windows KBID to be excluded for patching.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] kb_numbers_to_include: Windows KBID to be included for patching.
        """
        if classifications_to_include is not None:
            pulumi.set(__self__, "classifications_to_include", classifications_to_include)
        if exclude_kbs_requiring_reboot is not None:
            pulumi.set(__self__, "exclude_kbs_requiring_reboot", exclude_kbs_requiring_reboot)
        if kb_numbers_to_exclude is not None:
            pulumi.set(__self__, "kb_numbers_to_exclude", kb_numbers_to_exclude)
        if kb_numbers_to_include is not None:
            pulumi.set(__self__, "kb_numbers_to_include", kb_numbers_to_include)

    @property
    @pulumi.getter(name="classificationsToInclude")
    def classifications_to_include(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Classification category of patches to be patched
        """
        return pulumi.get(self, "classifications_to_include")

    @classifications_to_include.setter
    def classifications_to_include(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "classifications_to_include", value)

    @property
    @pulumi.getter(name="excludeKbsRequiringReboot")
    def exclude_kbs_requiring_reboot(self) -> Optional[pulumi.Input[bool]]:
        """
        Exclude patches which need reboot
        """
        return pulumi.get(self, "exclude_kbs_requiring_reboot")

    @exclude_kbs_requiring_reboot.setter
    def exclude_kbs_requiring_reboot(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "exclude_kbs_requiring_reboot", value)

    @property
    @pulumi.getter(name="kbNumbersToExclude")
    def kb_numbers_to_exclude(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Windows KBID to be excluded for patching.
        """
        return pulumi.get(self, "kb_numbers_to_exclude")

    @kb_numbers_to_exclude.setter
    def kb_numbers_to_exclude(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "kb_numbers_to_exclude", value)

    @property
    @pulumi.getter(name="kbNumbersToInclude")
    def kb_numbers_to_include(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Windows KBID to be included for patching.
        """
        return pulumi.get(self, "kb_numbers_to_include")

    @kb_numbers_to_include.setter
    def kb_numbers_to_include(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "kb_numbers_to_include", value)


@pulumi.input_type
class TagSettingsPropertiesArgs:
    def __init__(__self__, *,
                 filter_operator: Optional[pulumi.Input['TagOperators']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None):
        """
        Tag filter information for the VM.
        :param pulumi.Input['TagOperators'] filter_operator: Filter VMs by Any or All specified tags.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] tags: Dictionary of tags with its list of values.
        """
        if filter_operator is not None:
            pulumi.set(__self__, "filter_operator", filter_operator)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="filterOperator")
    def filter_operator(self) -> Optional[pulumi.Input['TagOperators']]:
        """
        Filter VMs by Any or All specified tags.
        """
        return pulumi.get(self, "filter_operator")

    @filter_operator.setter
    def filter_operator(self, value: Optional[pulumi.Input['TagOperators']]):
        pulumi.set(self, "filter_operator", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]:
        """
        Dictionary of tags with its list of values.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]):
        pulumi.set(self, "tags", value)


