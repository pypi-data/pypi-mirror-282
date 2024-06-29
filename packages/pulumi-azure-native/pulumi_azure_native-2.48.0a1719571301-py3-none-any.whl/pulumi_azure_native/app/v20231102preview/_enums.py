# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccessMode',
    'Action',
    'ActiveRevisionsMode',
    'Affinity',
    'AppProtocol',
    'BindingType',
    'CertificateType',
    'ClientCredentialMethod',
    'CookieExpirationConvention',
    'DotNetComponentType',
    'ExtendedLocationTypes',
    'ForwardProxyConvention',
    'IngressClientCertificateMode',
    'IngressTargetPortHttpScheme',
    'IngressTransportMethod',
    'JavaComponentType',
    'LogLevel',
    'ManagedCertificateDomainControlValidation',
    'ManagedServiceIdentityType',
    'Scheme',
    'StorageType',
    'TriggerType',
    'Type',
    'UnauthenticatedClientActionV2',
]


class AccessMode(str, Enum):
    """
    Access mode for storage
    """
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class Action(str, Enum):
    """
    Allow or Deny rules to determine for incoming IP. Note: Rules can only consist of ALL Allow or ALL Deny
    """
    ALLOW = "Allow"
    DENY = "Deny"


class ActiveRevisionsMode(str, Enum):
    """
    ActiveRevisionsMode controls how active revisions are handled for the Container app:
    <list><item>Multiple: multiple revisions can be active.</item><item>Single: Only one revision can be active at a time. Revision weights can not be used in this mode. If no value if provided, this is the default.</item></list>
    """
    MULTIPLE = "Multiple"
    SINGLE = "Single"


class Affinity(str, Enum):
    """
    Sticky Session Affinity
    """
    STICKY = "sticky"
    NONE = "none"


class AppProtocol(str, Enum):
    """
    Tells Dapr which protocol your application is using. Valid options are http and grpc. Default is http
    """
    HTTP = "http"
    GRPC = "grpc"


class BindingType(str, Enum):
    """
    Custom Domain binding type.
    """
    DISABLED = "Disabled"
    SNI_ENABLED = "SniEnabled"


class CertificateType(str, Enum):
    """
    The type of the certificate. Allowed values are `ServerSSLCertificate` and `ImagePullTrustedCA`
    """
    SERVER_SSL_CERTIFICATE = "ServerSSLCertificate"
    IMAGE_PULL_TRUSTED_CA = "ImagePullTrustedCA"


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


class DotNetComponentType(str, Enum):
    """
    Type of the .NET Component.
    """
    ASPIRE_DASHBOARD = "AspireDashboard"
    ASPIRE_RESOURCE_SERVER_API = "AspireResourceServerApi"


class ExtendedLocationTypes(str, Enum):
    """
    The type of the extended location.
    """
    CUSTOM_LOCATION = "CustomLocation"


class ForwardProxyConvention(str, Enum):
    """
    The convention used to determine the url of the request made.
    """
    NO_PROXY = "NoProxy"
    STANDARD = "Standard"
    CUSTOM = "Custom"


class IngressClientCertificateMode(str, Enum):
    """
    Client certificate mode for mTLS authentication. Ignore indicates server drops client certificate on forwarding. Accept indicates server forwards client certificate but does not require a client certificate. Require indicates server requires a client certificate.
    """
    IGNORE = "ignore"
    ACCEPT = "accept"
    REQUIRE = "require"


class IngressTargetPortHttpScheme(str, Enum):
    """
    Whether an http app listens on http or https
    """
    HTTP = "http"
    HTTPS = "https"


class IngressTransportMethod(str, Enum):
    """
    Ingress transport protocol
    """
    AUTO = "auto"
    HTTP = "http"
    HTTP2 = "http2"
    TCP = "tcp"


class JavaComponentType(str, Enum):
    """
    Type of the Java Component.
    """
    SPRING_BOOT_ADMIN = "SpringBootAdmin"
    SPRING_CLOUD_EUREKA = "SpringCloudEureka"
    SPRING_CLOUD_CONFIG = "SpringCloudConfig"


class LogLevel(str, Enum):
    """
    Sets the log level for the Dapr sidecar. Allowed values are debug, info, warn, error. Default is info.
    """
    INFO = "info"
    DEBUG = "debug"
    WARN = "warn"
    ERROR = "error"


class ManagedCertificateDomainControlValidation(str, Enum):
    """
    Selected type of domain control validation for managed certificates.
    """
    CNAME = "CNAME"
    HTTP = "HTTP"
    TXT = "TXT"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class Scheme(str, Enum):
    """
    Scheme to use for connecting to the host. Defaults to HTTP.
    """
    HTTP = "HTTP"
    HTTPS = "HTTPS"


class StorageType(str, Enum):
    """
    Storage type for the volume. If not provided, use EmptyDir.
    """
    AZURE_FILE = "AzureFile"
    EMPTY_DIR = "EmptyDir"
    SECRET = "Secret"
    NFS_AZURE_FILE = "NfsAzureFile"


class TriggerType(str, Enum):
    """
    Trigger type of the job
    """
    SCHEDULE = "Schedule"
    EVENT = "Event"
    MANUAL = "Manual"


class Type(str, Enum):
    """
    The type of probe.
    """
    LIVENESS = "Liveness"
    READINESS = "Readiness"
    STARTUP = "Startup"


class UnauthenticatedClientActionV2(str, Enum):
    """
    The action to take when an unauthenticated client attempts to access the app.
    """
    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"
    RETURN401 = "Return401"
    RETURN403 = "Return403"
