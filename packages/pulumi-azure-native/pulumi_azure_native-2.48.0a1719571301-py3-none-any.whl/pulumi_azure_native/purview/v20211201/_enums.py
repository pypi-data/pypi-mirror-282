# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CredentialsType',
    'EventHubType',
    'EventStreamingState',
    'EventStreamingType',
    'ManagedEventHubState',
    'ManagedResourcesPublicNetworkAccess',
    'PublicNetworkAccess',
    'Status',
    'Type',
]


class CredentialsType(str, Enum):
    """
    Identity Type.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class EventHubType(str, Enum):
    """
    The event hub type.
    """
    NOTIFICATION = "Notification"
    HOOK = "Hook"


class EventStreamingState(str, Enum):
    """
    The state of the event streaming service
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class EventStreamingType(str, Enum):
    """
    The event streaming service type
    """
    NONE = "None"
    MANAGED = "Managed"
    AZURE = "Azure"


class ManagedEventHubState(str, Enum):
    """
     Gets or sets the state of managed eventhub. If enabled managed eventhub will be created, if disabled the managed eventhub will be removed.
    """
    NOT_SPECIFIED = "NotSpecified"
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ManagedResourcesPublicNetworkAccess(str, Enum):
    """
    Gets or sets the public network access for managed resources.
    """
    NOT_SPECIFIED = "NotSpecified"
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class PublicNetworkAccess(str, Enum):
    """
    Gets or sets the public network access.
    """
    NOT_SPECIFIED = "NotSpecified"
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class Status(str, Enum):
    """
    The status.
    """
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class Type(str, Enum):
    """
    Identity Type
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
