# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CleanupOptions',
    'ManagedServiceIdentityType',
    'ScriptType',
]


class CleanupOptions(str, Enum):
    """
    The clean up preference when the script execution gets in a terminal state. Default setting is 'Always'.
    """
    ALWAYS = "Always"
    ON_SUCCESS = "OnSuccess"
    ON_EXPIRATION = "OnExpiration"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of the managed identity.
    """
    USER_ASSIGNED = "UserAssigned"


class ScriptType(str, Enum):
    """
    Type of the script.
    """
    AZURE_POWER_SHELL = "AzurePowerShell"
    AZURE_CLI = "AzureCLI"
