# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AllowedContentLevel',
    'DeploymentModelVersionUpgradeOption',
    'DeploymentScaleType',
    'EncryptionScopeState',
    'HostingModel',
    'KeySource',
    'NetworkRuleAction',
    'PrivateEndpointServiceConnectionStatus',
    'PublicNetworkAccess',
    'RaiPolicyContentSource',
    'RaiPolicyMode',
    'ResourceIdentityType',
    'RoutingMethods',
    'SkuTier',
]


class AllowedContentLevel(str, Enum):
    """
    Level at which content is filtered.
    """
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class DeploymentModelVersionUpgradeOption(str, Enum):
    """
    Deployment model version upgrade option.
    """
    ONCE_NEW_DEFAULT_VERSION_AVAILABLE = "OnceNewDefaultVersionAvailable"
    ONCE_CURRENT_VERSION_EXPIRED = "OnceCurrentVersionExpired"
    NO_AUTO_UPGRADE = "NoAutoUpgrade"


class DeploymentScaleType(str, Enum):
    """
    Deployment scale type.
    """
    STANDARD = "Standard"
    MANUAL = "Manual"


class EncryptionScopeState(str, Enum):
    """
    The encryptionScope state.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class HostingModel(str, Enum):
    """
    Account hosting model.
    """
    WEB = "Web"
    CONNECTED_CONTAINER = "ConnectedContainer"
    DISCONNECTED_CONTAINER = "DisconnectedContainer"
    PROVISIONED_WEB = "ProvisionedWeb"


class KeySource(str, Enum):
    """
    Enumerates the possible value of keySource for Encryption
    """
    MICROSOFT_COGNITIVE_SERVICES = "Microsoft.CognitiveServices"
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"


class NetworkRuleAction(str, Enum):
    """
    The default action when no rule from ipRules and from virtualNetworkRules match. This is only used after the bypass property has been evaluated.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicNetworkAccess(str, Enum):
    """
    Whether or not public endpoint access is allowed for this account.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RaiPolicyContentSource(str, Enum):
    """
    Content source to apply the Content Filters.
    """
    PROMPT = "Prompt"
    COMPLETION = "Completion"


class RaiPolicyMode(str, Enum):
    """
    Content Filters mode.
    """
    DEFAULT = "Default"
    DEFERRED = "Deferred"
    BLOCKING = "Blocking"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class RoutingMethods(str, Enum):
    """
    Multiregion routing methods.
    """
    PRIORITY = "Priority"
    WEIGHTED = "Weighted"
    PERFORMANCE = "Performance"


class SkuTier(str, Enum):
    """
    This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
    """
    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    ENTERPRISE = "Enterprise"
