# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AKSIdentityType',
    'LevelType',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccessType',
    'ResourceIdentityType',
]


class AKSIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"


class LevelType(str, Enum):
    """
    Level of the status.
    """
    ERROR = "Error"
    WARNING = "Warning"
    INFORMATION = "Information"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccessType(str, Enum):
    """
    Indicates whether machines associated with the private link scope can also use public Azure Arc service endpoints.
    """
    ENABLED = "Enabled"
    """
    Allows Azure Arc agents to communicate with Azure Arc services over both public (internet) and private endpoints.
    """
    DISABLED = "Disabled"
    """
    Does not allow Azure Arc agents to communicate with Azure Arc services over public (internet) endpoints. The agents must use the private link.
    """


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
