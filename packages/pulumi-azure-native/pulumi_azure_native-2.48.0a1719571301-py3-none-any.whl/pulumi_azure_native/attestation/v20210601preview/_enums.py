# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccessType',
]


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccessType(str, Enum):
    """
    Controls whether traffic from the public network is allowed to access the Attestation Provider APIs.
    """
    ENABLED = "Enabled"
    """
    Enables public network connectivity to the Attestation Provider REST APIs.
    """
    DISABLED = "Disabled"
    """
    Disables public network connectivity to the Attestation Provider REST APIs.
    """
