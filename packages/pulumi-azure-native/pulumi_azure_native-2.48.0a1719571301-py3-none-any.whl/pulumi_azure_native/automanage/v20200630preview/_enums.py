# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EnableRealTimeProtection',
    'ResourceIdentityType',
    'RunScheduledScan',
    'ScanType',
]


class EnableRealTimeProtection(str, Enum):
    """
    Enables or disables Real Time Protection
    """
    TRUE = "True"
    FALSE = "False"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the Automanage account. Currently, the only supported type is 'SystemAssigned', which implicitly creates an identity.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"


class RunScheduledScan(str, Enum):
    """
    Enables or disables a periodic scan for antimalware
    """
    TRUE = "True"
    FALSE = "False"


class ScanType(str, Enum):
    """
    Type of scheduled scan
    """
    QUICK = "Quick"
    FULL = "Full"
