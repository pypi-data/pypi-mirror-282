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
    'ApiEntityReferenceArgs',
    'InstanceViewStatusArgs',
    'VirtualMachineExtensionInstanceViewArgs',
]

@pulumi.input_type
class ApiEntityReferenceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        The API entity reference.
        :param pulumi.Input[str] id: The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARM resource id in the form of /subscriptions/{SubscriptionId}/resourceGroups/{ResourceGroupName}/...
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class InstanceViewStatusArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[str]] = None,
                 display_status: Optional[pulumi.Input[str]] = None,
                 level: Optional[pulumi.Input['StatusLevelTypes']] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 time: Optional[pulumi.Input[str]] = None):
        """
        Instance view status.
        :param pulumi.Input[str] code: The status code.
        :param pulumi.Input[str] display_status: The short localizable label for the status.
        :param pulumi.Input['StatusLevelTypes'] level: The level code.
        :param pulumi.Input[str] message: The detailed status message, including for alerts and error messages.
        :param pulumi.Input[str] time: The time of the status.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if display_status is not None:
            pulumi.set(__self__, "display_status", display_status)
        if level is not None:
            pulumi.set(__self__, "level", level)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if time is not None:
            pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[str]]:
        """
        The status code.
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code", value)

    @property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> Optional[pulumi.Input[str]]:
        """
        The short localizable label for the status.
        """
        return pulumi.get(self, "display_status")

    @display_status.setter
    def display_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_status", value)

    @property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input['StatusLevelTypes']]:
        """
        The level code.
        """
        return pulumi.get(self, "level")

    @level.setter
    def level(self, value: Optional[pulumi.Input['StatusLevelTypes']]):
        pulumi.set(self, "level", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        The detailed status message, including for alerts and error messages.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[str]]:
        """
        The time of the status.
        """
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time", value)


@pulumi.input_type
class VirtualMachineExtensionInstanceViewArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceViewStatusArgs']]]] = None,
                 substatuses: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceViewStatusArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_handler_version: Optional[pulumi.Input[str]] = None):
        """
        The instance view of a virtual machine extension.
        :param pulumi.Input[str] name: The virtual machine extension name.
        :param pulumi.Input[Sequence[pulumi.Input['InstanceViewStatusArgs']]] statuses: The resource status information.
        :param pulumi.Input[Sequence[pulumi.Input['InstanceViewStatusArgs']]] substatuses: The resource status information.
        :param pulumi.Input[str] type: Specifies the type of the extension; an example is "CustomScriptExtension".
        :param pulumi.Input[str] type_handler_version: Specifies the version of the script handler.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if statuses is not None:
            pulumi.set(__self__, "statuses", statuses)
        if substatuses is not None:
            pulumi.set(__self__, "substatuses", substatuses)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if type_handler_version is not None:
            pulumi.set(__self__, "type_handler_version", type_handler_version)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The virtual machine extension name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceViewStatusArgs']]]]:
        """
        The resource status information.
        """
        return pulumi.get(self, "statuses")

    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceViewStatusArgs']]]]):
        pulumi.set(self, "statuses", value)

    @property
    @pulumi.getter
    def substatuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InstanceViewStatusArgs']]]]:
        """
        The resource status information.
        """
        return pulumi.get(self, "substatuses")

    @substatuses.setter
    def substatuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InstanceViewStatusArgs']]]]):
        pulumi.set(self, "substatuses", value)

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
        Specifies the version of the script handler.
        """
        return pulumi.get(self, "type_handler_version")

    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_handler_version", value)


