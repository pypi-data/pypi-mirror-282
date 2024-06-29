# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ClientCredentialMethod',
    'CookieExpirationConvention',
    'ForwardProxyConvention',
    'ManagedServiceIdentityType',
    'StagingEnvironmentPolicy',
    'UnauthenticatedClientActionV2',
]


class ClientCredentialMethod(str, Enum):
    """
    The method that should be used to authenticate the user.
    """
    CLIENT_SECRET_POST = "ClientSecretPost"


class CookieExpirationConvention(str, Enum):
    """
    The convention used when determining the session cookie's expiration.
    """
    FIXED_TIME = "FixedTime"
    IDENTITY_PROVIDER_DERIVED = "IdentityProviderDerived"


class ForwardProxyConvention(str, Enum):
    """
    The convention used to determine the url of the request made.
    """
    NO_PROXY = "NoProxy"
    STANDARD = "Standard"
    CUSTOM = "Custom"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class StagingEnvironmentPolicy(str, Enum):
    """
    State indicating whether staging environments are allowed or not allowed for a static web app.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class UnauthenticatedClientActionV2(str, Enum):
    """
    The action to take when an unauthenticated client attempts to access the app.
    """
    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"
    RETURN401 = "Return401"
    RETURN403 = "Return403"
