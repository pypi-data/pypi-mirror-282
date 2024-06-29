# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'B2CResourceSKUName',
    'B2CResourceSKUTier',
    'CIAMResourceSKUName',
]


class B2CResourceSKUName(str, Enum):
    """
    The name of the SKU for the tenant.
    """
    STANDARD = "Standard"
    """
    Azure AD B2C usage is billed to a linked Azure subscription and uses a monthly active users (MAU) billing model.
    """
    PREMIUM_P1 = "PremiumP1"
    """
    Azure AD B2C usage is billed to a linked Azure subscription and uses number of authentications based billing.
    """
    PREMIUM_P2 = "PremiumP2"
    """
    Azure AD B2C usage is billed to a linked Azure subscription and uses number of authentications based billing.
    """


class B2CResourceSKUTier(str, Enum):
    """
    The tier of the tenant.
    """
    A0 = "A0"
    """
    The SKU tier used for all Azure AD B2C tenants.
    """


class CIAMResourceSKUName(str, Enum):
    """
    The name of the SKU for the tenant.
    """
    STANDARD = "Standard"
    PREMIUM_P1 = "PremiumP1"
    PREMIUM_P2 = "PremiumP2"
