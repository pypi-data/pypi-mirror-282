# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccountSkuName',
    'EventHubType',
    'EventStreamingState',
    'EventStreamingType',
    'KafkaConfigurationIdentityType',
    'ManagedEventHubState',
    'ManagedIdentityType',
    'PrivateEndpointConnectionStatus',
    'PublicNetworkAccess',
    'TenantEndpointState',
]


class AccountSkuName(str, Enum):
    """
    Gets or sets the sku name.
    """
    STANDARD = "Standard"
    FREE = "Free"


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


class KafkaConfigurationIdentityType(str, Enum):
    """
    Identity Type.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class ManagedEventHubState(str, Enum):
    """
    Gets or sets the state of managed eventhub. If enabled managed eventhub will be created, if disabled the managed eventhub will be removed.
    """
    NOT_SPECIFIED = "NotSpecified"
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ManagedIdentityType(str, Enum):
    """
    Identity Type
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class PrivateEndpointConnectionStatus(str, Enum):
    """
    The status.
    """
    UNKNOWN = "Unknown"
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class PublicNetworkAccess(str, Enum):
    """
    Gets or sets the public network access.
    """
    NOT_SPECIFIED = "NotSpecified"
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TenantEndpointState(str, Enum):
    """
    Gets or sets the state of tenant endpoint.
    """
    NOT_SPECIFIED = "NotSpecified"
    DISABLED = "Disabled"
    ENABLED = "Enabled"
