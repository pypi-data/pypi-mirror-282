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
    'ApplicationInsightsComponentAnalyticsItemPropertiesResponse',
    'ApplicationInsightsComponentDataVolumeCapResponse',
    'ApplicationInsightsComponentProactiveDetectionConfigurationResponseRuleDefinitions',
]

@pulumi.output_type
class ApplicationInsightsComponentAnalyticsItemPropertiesResponse(dict):
    """
    A set of properties that can be defined in the context of a specific item type. Each type may have its own properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "functionAlias":
            suggest = "function_alias"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationInsightsComponentAnalyticsItemPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationInsightsComponentAnalyticsItemPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationInsightsComponentAnalyticsItemPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 function_alias: Optional[str] = None):
        """
        A set of properties that can be defined in the context of a specific item type. Each type may have its own properties.
        :param str function_alias: A function alias, used when the type of the item is Function
        """
        if function_alias is not None:
            pulumi.set(__self__, "function_alias", function_alias)

    @property
    @pulumi.getter(name="functionAlias")
    def function_alias(self) -> Optional[str]:
        """
        A function alias, used when the type of the item is Function
        """
        return pulumi.get(self, "function_alias")


@pulumi.output_type
class ApplicationInsightsComponentDataVolumeCapResponse(dict):
    """
    An Application Insights component daily data volume cap
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maxHistoryCap":
            suggest = "max_history_cap"
        elif key == "resetTime":
            suggest = "reset_time"
        elif key == "stopSendNotificationWhenHitCap":
            suggest = "stop_send_notification_when_hit_cap"
        elif key == "stopSendNotificationWhenHitThreshold":
            suggest = "stop_send_notification_when_hit_threshold"
        elif key == "warningThreshold":
            suggest = "warning_threshold"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationInsightsComponentDataVolumeCapResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationInsightsComponentDataVolumeCapResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationInsightsComponentDataVolumeCapResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 max_history_cap: float,
                 reset_time: int,
                 cap: Optional[float] = None,
                 stop_send_notification_when_hit_cap: Optional[bool] = None,
                 stop_send_notification_when_hit_threshold: Optional[bool] = None,
                 warning_threshold: Optional[int] = None):
        """
        An Application Insights component daily data volume cap
        :param float max_history_cap: Maximum daily data volume cap that the user can set for this component.
        :param int reset_time: Daily data volume cap UTC reset hour.
        :param float cap: Daily data volume cap in GB.
        :param bool stop_send_notification_when_hit_cap: Do not send a notification email when the daily data volume cap is met.
        :param bool stop_send_notification_when_hit_threshold: Reserved, not used for now.
        :param int warning_threshold: Reserved, not used for now.
        """
        pulumi.set(__self__, "max_history_cap", max_history_cap)
        pulumi.set(__self__, "reset_time", reset_time)
        if cap is not None:
            pulumi.set(__self__, "cap", cap)
        if stop_send_notification_when_hit_cap is not None:
            pulumi.set(__self__, "stop_send_notification_when_hit_cap", stop_send_notification_when_hit_cap)
        if stop_send_notification_when_hit_threshold is not None:
            pulumi.set(__self__, "stop_send_notification_when_hit_threshold", stop_send_notification_when_hit_threshold)
        if warning_threshold is not None:
            pulumi.set(__self__, "warning_threshold", warning_threshold)

    @property
    @pulumi.getter(name="maxHistoryCap")
    def max_history_cap(self) -> float:
        """
        Maximum daily data volume cap that the user can set for this component.
        """
        return pulumi.get(self, "max_history_cap")

    @property
    @pulumi.getter(name="resetTime")
    def reset_time(self) -> int:
        """
        Daily data volume cap UTC reset hour.
        """
        return pulumi.get(self, "reset_time")

    @property
    @pulumi.getter
    def cap(self) -> Optional[float]:
        """
        Daily data volume cap in GB.
        """
        return pulumi.get(self, "cap")

    @property
    @pulumi.getter(name="stopSendNotificationWhenHitCap")
    def stop_send_notification_when_hit_cap(self) -> Optional[bool]:
        """
        Do not send a notification email when the daily data volume cap is met.
        """
        return pulumi.get(self, "stop_send_notification_when_hit_cap")

    @property
    @pulumi.getter(name="stopSendNotificationWhenHitThreshold")
    def stop_send_notification_when_hit_threshold(self) -> Optional[bool]:
        """
        Reserved, not used for now.
        """
        return pulumi.get(self, "stop_send_notification_when_hit_threshold")

    @property
    @pulumi.getter(name="warningThreshold")
    def warning_threshold(self) -> Optional[int]:
        """
        Reserved, not used for now.
        """
        return pulumi.get(self, "warning_threshold")


@pulumi.output_type
class ApplicationInsightsComponentProactiveDetectionConfigurationResponseRuleDefinitions(dict):
    """
    Static definitions of the ProactiveDetection configuration rule (same values for all components).
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "displayName":
            suggest = "display_name"
        elif key == "helpUrl":
            suggest = "help_url"
        elif key == "isEnabledByDefault":
            suggest = "is_enabled_by_default"
        elif key == "isHidden":
            suggest = "is_hidden"
        elif key == "isInPreview":
            suggest = "is_in_preview"
        elif key == "supportsEmailNotifications":
            suggest = "supports_email_notifications"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationInsightsComponentProactiveDetectionConfigurationResponseRuleDefinitions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationInsightsComponentProactiveDetectionConfigurationResponseRuleDefinitions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationInsightsComponentProactiveDetectionConfigurationResponseRuleDefinitions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: Optional[str] = None,
                 display_name: Optional[str] = None,
                 help_url: Optional[str] = None,
                 is_enabled_by_default: Optional[bool] = None,
                 is_hidden: Optional[bool] = None,
                 is_in_preview: Optional[bool] = None,
                 name: Optional[str] = None,
                 supports_email_notifications: Optional[bool] = None):
        """
        Static definitions of the ProactiveDetection configuration rule (same values for all components).
        :param str description: The rule description
        :param str display_name: The rule name as it is displayed in UI
        :param str help_url: URL which displays additional info about the proactive detection rule
        :param bool is_enabled_by_default: A flag indicating whether the rule is enabled by default
        :param bool is_hidden: A flag indicating whether the rule is hidden (from the UI)
        :param bool is_in_preview: A flag indicating whether the rule is in preview
        :param str name: The rule name
        :param bool supports_email_notifications: A flag indicating whether email notifications are supported for detections for this rule
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if help_url is not None:
            pulumi.set(__self__, "help_url", help_url)
        if is_enabled_by_default is not None:
            pulumi.set(__self__, "is_enabled_by_default", is_enabled_by_default)
        if is_hidden is not None:
            pulumi.set(__self__, "is_hidden", is_hidden)
        if is_in_preview is not None:
            pulumi.set(__self__, "is_in_preview", is_in_preview)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if supports_email_notifications is not None:
            pulumi.set(__self__, "supports_email_notifications", supports_email_notifications)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The rule description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The rule name as it is displayed in UI
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="helpUrl")
    def help_url(self) -> Optional[str]:
        """
        URL which displays additional info about the proactive detection rule
        """
        return pulumi.get(self, "help_url")

    @property
    @pulumi.getter(name="isEnabledByDefault")
    def is_enabled_by_default(self) -> Optional[bool]:
        """
        A flag indicating whether the rule is enabled by default
        """
        return pulumi.get(self, "is_enabled_by_default")

    @property
    @pulumi.getter(name="isHidden")
    def is_hidden(self) -> Optional[bool]:
        """
        A flag indicating whether the rule is hidden (from the UI)
        """
        return pulumi.get(self, "is_hidden")

    @property
    @pulumi.getter(name="isInPreview")
    def is_in_preview(self) -> Optional[bool]:
        """
        A flag indicating whether the rule is in preview
        """
        return pulumi.get(self, "is_in_preview")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The rule name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="supportsEmailNotifications")
    def supports_email_notifications(self) -> Optional[bool]:
        """
        A flag indicating whether email notifications are supported for detections for this rule
        """
        return pulumi.get(self, "supports_email_notifications")


