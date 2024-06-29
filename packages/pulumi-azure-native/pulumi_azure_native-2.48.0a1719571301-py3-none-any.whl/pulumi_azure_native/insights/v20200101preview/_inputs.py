# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ManagementGroupLogSettingsArgs',
]

@pulumi.input_type
class ManagementGroupLogSettingsArgs:
    def __init__(__self__, *,
                 category: pulumi.Input[str],
                 enabled: pulumi.Input[bool]):
        """
        Part of Management Group diagnostic setting. Specifies the settings for a particular log.
        :param pulumi.Input[str] category: Name of a Management Group Diagnostic Log category for a resource type this setting is applied to.
        :param pulumi.Input[bool] enabled: a value indicating whether this log is enabled.
        """
        pulumi.set(__self__, "category", category)
        pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Input[str]:
        """
        Name of a Management Group Diagnostic Log category for a resource type this setting is applied to.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: pulumi.Input[str]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        a value indicating whether this log is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)


