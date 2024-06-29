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
    'CommandArgs',
    'DistributionGroupListReceiverValueArgs',
    'NotificationEventReceiverArgs',
    'NotificationReceiverValueArgs',
    'SubscriptionReceiverValueArgs',
    'TargetOSInfoArgs',
    'TestBaseAccountSKUArgs',
    'TestArgs',
    'UserObjectReceiverValueArgs',
]

@pulumi.input_type
class CommandArgs:
    def __init__(__self__, *,
                 action: pulumi.Input[Union[str, 'Action']],
                 content: pulumi.Input[str],
                 content_type: pulumi.Input[Union[str, 'ContentType']],
                 name: pulumi.Input[str],
                 always_run: Optional[pulumi.Input[bool]] = None,
                 apply_update_before: Optional[pulumi.Input[bool]] = None,
                 max_run_time: Optional[pulumi.Input[int]] = None,
                 restart_after: Optional[pulumi.Input[bool]] = None,
                 run_as_interactive: Optional[pulumi.Input[bool]] = None,
                 run_elevated: Optional[pulumi.Input[bool]] = None):
        """
        The command used in the test
        :param pulumi.Input[Union[str, 'Action']] action: The action of the command.
        :param pulumi.Input[str] content: The content of the command. The content depends on source type.
        :param pulumi.Input[Union[str, 'ContentType']] content_type: The type of command content.
        :param pulumi.Input[str] name: The name of the command.
        :param pulumi.Input[bool] always_run: Specifies whether to run the command even if a previous command is failed.
        :param pulumi.Input[bool] apply_update_before: Specifies whether to apply update before the command.
        :param pulumi.Input[int] max_run_time: Specifies the max run time of the command.
        :param pulumi.Input[bool] restart_after: Specifies whether to restart the VM after the command executed.
        :param pulumi.Input[bool] run_as_interactive: Specifies whether to run the command in interactive mode.
        :param pulumi.Input[bool] run_elevated: Specifies whether to run the command as administrator.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "content_type", content_type)
        pulumi.set(__self__, "name", name)
        if always_run is not None:
            pulumi.set(__self__, "always_run", always_run)
        if apply_update_before is not None:
            pulumi.set(__self__, "apply_update_before", apply_update_before)
        if max_run_time is not None:
            pulumi.set(__self__, "max_run_time", max_run_time)
        if restart_after is not None:
            pulumi.set(__self__, "restart_after", restart_after)
        if run_as_interactive is not None:
            pulumi.set(__self__, "run_as_interactive", run_as_interactive)
        if run_elevated is not None:
            pulumi.set(__self__, "run_elevated", run_elevated)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input[Union[str, 'Action']]:
        """
        The action of the command.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input[Union[str, 'Action']]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        The content of the command. The content depends on source type.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Input[Union[str, 'ContentType']]:
        """
        The type of command content.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: pulumi.Input[Union[str, 'ContentType']]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the command.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="alwaysRun")
    def always_run(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to run the command even if a previous command is failed.
        """
        return pulumi.get(self, "always_run")

    @always_run.setter
    def always_run(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "always_run", value)

    @property
    @pulumi.getter(name="applyUpdateBefore")
    def apply_update_before(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to apply update before the command.
        """
        return pulumi.get(self, "apply_update_before")

    @apply_update_before.setter
    def apply_update_before(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "apply_update_before", value)

    @property
    @pulumi.getter(name="maxRunTime")
    def max_run_time(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the max run time of the command.
        """
        return pulumi.get(self, "max_run_time")

    @max_run_time.setter
    def max_run_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_run_time", value)

    @property
    @pulumi.getter(name="restartAfter")
    def restart_after(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to restart the VM after the command executed.
        """
        return pulumi.get(self, "restart_after")

    @restart_after.setter
    def restart_after(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "restart_after", value)

    @property
    @pulumi.getter(name="runAsInteractive")
    def run_as_interactive(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to run the command in interactive mode.
        """
        return pulumi.get(self, "run_as_interactive")

    @run_as_interactive.setter
    def run_as_interactive(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "run_as_interactive", value)

    @property
    @pulumi.getter(name="runElevated")
    def run_elevated(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether to run the command as administrator.
        """
        return pulumi.get(self, "run_elevated")

    @run_elevated.setter
    def run_elevated(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "run_elevated", value)


@pulumi.input_type
class DistributionGroupListReceiverValueArgs:
    def __init__(__self__, *,
                 distribution_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The user object receiver value.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] distribution_groups: The list of distribution groups.
        """
        if distribution_groups is not None:
            pulumi.set(__self__, "distribution_groups", distribution_groups)

    @property
    @pulumi.getter(name="distributionGroups")
    def distribution_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of distribution groups.
        """
        return pulumi.get(self, "distribution_groups")

    @distribution_groups.setter
    def distribution_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "distribution_groups", value)


@pulumi.input_type
class NotificationEventReceiverArgs:
    def __init__(__self__, *,
                 receiver_type: Optional[pulumi.Input[str]] = None,
                 receiver_value: Optional[pulumi.Input['NotificationReceiverValueArgs']] = None):
        """
        A notification event receivers.
        :param pulumi.Input[str] receiver_type: The type of the notification event receiver.
        :param pulumi.Input['NotificationReceiverValueArgs'] receiver_value: The notification event receiver value.
        """
        if receiver_type is not None:
            pulumi.set(__self__, "receiver_type", receiver_type)
        if receiver_value is not None:
            pulumi.set(__self__, "receiver_value", receiver_value)

    @property
    @pulumi.getter(name="receiverType")
    def receiver_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the notification event receiver.
        """
        return pulumi.get(self, "receiver_type")

    @receiver_type.setter
    def receiver_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "receiver_type", value)

    @property
    @pulumi.getter(name="receiverValue")
    def receiver_value(self) -> Optional[pulumi.Input['NotificationReceiverValueArgs']]:
        """
        The notification event receiver value.
        """
        return pulumi.get(self, "receiver_value")

    @receiver_value.setter
    def receiver_value(self, value: Optional[pulumi.Input['NotificationReceiverValueArgs']]):
        pulumi.set(self, "receiver_value", value)


@pulumi.input_type
class NotificationReceiverValueArgs:
    def __init__(__self__, *,
                 distribution_group_list_receiver_value: Optional[pulumi.Input['DistributionGroupListReceiverValueArgs']] = None,
                 subscription_receiver_value: Optional[pulumi.Input['SubscriptionReceiverValueArgs']] = None,
                 user_object_receiver_value: Optional[pulumi.Input['UserObjectReceiverValueArgs']] = None):
        """
        A notification event receiver value.
        :param pulumi.Input['DistributionGroupListReceiverValueArgs'] distribution_group_list_receiver_value: The user object receiver value.
        :param pulumi.Input['SubscriptionReceiverValueArgs'] subscription_receiver_value: The user object receiver value.
        :param pulumi.Input['UserObjectReceiverValueArgs'] user_object_receiver_value: The user object receiver value.
        """
        if distribution_group_list_receiver_value is not None:
            pulumi.set(__self__, "distribution_group_list_receiver_value", distribution_group_list_receiver_value)
        if subscription_receiver_value is not None:
            pulumi.set(__self__, "subscription_receiver_value", subscription_receiver_value)
        if user_object_receiver_value is not None:
            pulumi.set(__self__, "user_object_receiver_value", user_object_receiver_value)

    @property
    @pulumi.getter(name="distributionGroupListReceiverValue")
    def distribution_group_list_receiver_value(self) -> Optional[pulumi.Input['DistributionGroupListReceiverValueArgs']]:
        """
        The user object receiver value.
        """
        return pulumi.get(self, "distribution_group_list_receiver_value")

    @distribution_group_list_receiver_value.setter
    def distribution_group_list_receiver_value(self, value: Optional[pulumi.Input['DistributionGroupListReceiverValueArgs']]):
        pulumi.set(self, "distribution_group_list_receiver_value", value)

    @property
    @pulumi.getter(name="subscriptionReceiverValue")
    def subscription_receiver_value(self) -> Optional[pulumi.Input['SubscriptionReceiverValueArgs']]:
        """
        The user object receiver value.
        """
        return pulumi.get(self, "subscription_receiver_value")

    @subscription_receiver_value.setter
    def subscription_receiver_value(self, value: Optional[pulumi.Input['SubscriptionReceiverValueArgs']]):
        pulumi.set(self, "subscription_receiver_value", value)

    @property
    @pulumi.getter(name="userObjectReceiverValue")
    def user_object_receiver_value(self) -> Optional[pulumi.Input['UserObjectReceiverValueArgs']]:
        """
        The user object receiver value.
        """
        return pulumi.get(self, "user_object_receiver_value")

    @user_object_receiver_value.setter
    def user_object_receiver_value(self, value: Optional[pulumi.Input['UserObjectReceiverValueArgs']]):
        pulumi.set(self, "user_object_receiver_value", value)


@pulumi.input_type
class SubscriptionReceiverValueArgs:
    def __init__(__self__, *,
                 role: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 subscription_name: Optional[pulumi.Input[str]] = None):
        """
        The subscription role receiver value.
        :param pulumi.Input[str] role: The role of the notification receiver.
        :param pulumi.Input[str] subscription_id: The subscription id of the notification receiver.
        :param pulumi.Input[str] subscription_name: The subscription name of the notification receiver.
        """
        if role is not None:
            pulumi.set(__self__, "role", role)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if subscription_name is not None:
            pulumi.set(__self__, "subscription_name", subscription_name)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role of the notification receiver.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The subscription id of the notification receiver.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter(name="subscriptionName")
    def subscription_name(self) -> Optional[pulumi.Input[str]]:
        """
        The subscription name of the notification receiver.
        """
        return pulumi.get(self, "subscription_name")

    @subscription_name.setter
    def subscription_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_name", value)


@pulumi.input_type
class TargetOSInfoArgs:
    def __init__(__self__, *,
                 os_update_type: pulumi.Input[str],
                 target_oss: pulumi.Input[Sequence[pulumi.Input[str]]],
                 baseline_oss: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The information of the target OS to be tested.
        :param pulumi.Input[str] os_update_type: Specifies the OS update type to test against, e.g., 'Security updates' or 'Feature updates'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_oss: Specifies the target OSs to be tested.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] baseline_oss: Specifies the baseline OSs to be tested.
        """
        pulumi.set(__self__, "os_update_type", os_update_type)
        pulumi.set(__self__, "target_oss", target_oss)
        if baseline_oss is not None:
            pulumi.set(__self__, "baseline_oss", baseline_oss)

    @property
    @pulumi.getter(name="osUpdateType")
    def os_update_type(self) -> pulumi.Input[str]:
        """
        Specifies the OS update type to test against, e.g., 'Security updates' or 'Feature updates'.
        """
        return pulumi.get(self, "os_update_type")

    @os_update_type.setter
    def os_update_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "os_update_type", value)

    @property
    @pulumi.getter(name="targetOSs")
    def target_oss(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Specifies the target OSs to be tested.
        """
        return pulumi.get(self, "target_oss")

    @target_oss.setter
    def target_oss(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "target_oss", value)

    @property
    @pulumi.getter(name="baselineOSs")
    def baseline_oss(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the baseline OSs to be tested.
        """
        return pulumi.get(self, "baseline_oss")

    @baseline_oss.setter
    def baseline_oss(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "baseline_oss", value)


@pulumi.input_type
class TestBaseAccountSKUArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 tier: pulumi.Input[Union[str, 'Tier']],
                 locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None):
        """
        Describes a Test Base Account SKU.
        :param pulumi.Input[str] name: The name of the SKU. This is typically a letter + number code, such as B0 or S0.
        :param pulumi.Input[Union[str, 'Tier']] tier: The tier of this particular SKU.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locations: The locations that the SKU is available.
        :param pulumi.Input[str] resource_type: The type of resource the SKU applies to.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "tier", tier)
        if locations is not None:
            pulumi.set(__self__, "locations", locations)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the SKU. This is typically a letter + number code, such as B0 or S0.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[str, 'Tier']]:
        """
        The tier of this particular SKU.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: pulumi.Input[Union[str, 'Tier']]):
        pulumi.set(self, "tier", value)

    @property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The locations that the SKU is available.
        """
        return pulumi.get(self, "locations")

    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "locations", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of resource the SKU applies to.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)


@pulumi.input_type
class TestArgs:
    def __init__(__self__, *,
                 commands: pulumi.Input[Sequence[pulumi.Input['CommandArgs']]],
                 test_type: pulumi.Input[Union[str, 'TestType']],
                 is_active: Optional[pulumi.Input[bool]] = None):
        """
        The definition of a Test.
        :param pulumi.Input[Sequence[pulumi.Input['CommandArgs']]] commands: The commands used in the test.
        :param pulumi.Input[Union[str, 'TestType']] test_type: The type of the test.
        :param pulumi.Input[bool] is_active: Indicates if this test is active.It doesn't schedule test for not active Test.
        """
        pulumi.set(__self__, "commands", commands)
        pulumi.set(__self__, "test_type", test_type)
        if is_active is not None:
            pulumi.set(__self__, "is_active", is_active)

    @property
    @pulumi.getter
    def commands(self) -> pulumi.Input[Sequence[pulumi.Input['CommandArgs']]]:
        """
        The commands used in the test.
        """
        return pulumi.get(self, "commands")

    @commands.setter
    def commands(self, value: pulumi.Input[Sequence[pulumi.Input['CommandArgs']]]):
        pulumi.set(self, "commands", value)

    @property
    @pulumi.getter(name="testType")
    def test_type(self) -> pulumi.Input[Union[str, 'TestType']]:
        """
        The type of the test.
        """
        return pulumi.get(self, "test_type")

    @test_type.setter
    def test_type(self, value: pulumi.Input[Union[str, 'TestType']]):
        pulumi.set(self, "test_type", value)

    @property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if this test is active.It doesn't schedule test for not active Test.
        """
        return pulumi.get(self, "is_active")

    @is_active.setter
    def is_active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_active", value)


@pulumi.input_type
class UserObjectReceiverValueArgs:
    def __init__(__self__, *,
                 user_object_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The user object receiver value.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_object_ids: user object ids.
        """
        if user_object_ids is not None:
            pulumi.set(__self__, "user_object_ids", user_object_ids)

    @property
    @pulumi.getter(name="userObjectIds")
    def user_object_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        user object ids.
        """
        return pulumi.get(self, "user_object_ids")

    @user_object_ids.setter
    def user_object_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_object_ids", value)


