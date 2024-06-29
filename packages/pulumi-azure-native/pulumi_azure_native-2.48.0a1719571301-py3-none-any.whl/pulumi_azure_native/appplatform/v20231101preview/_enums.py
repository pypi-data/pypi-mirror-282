# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApiPortalApiTryOutEnabledState',
    'ApmType',
    'BackendProtocol',
    'BindingType',
    'ConfigServerEnabledState',
    'ConfigurationServiceGeneration',
    'CustomizedAcceleratorType',
    'DevToolPortalFeatureState',
    'Frequency',
    'GatewayCertificateVerification',
    'GatewayRouteConfigProtocol',
    'GitImplementation',
    'HTTPSchemeType',
    'KeyVaultCertificateAutoSync',
    'ManagedIdentityType',
    'ProbeActionType',
    'SessionAffinity',
    'StorageType',
    'Type',
    'WeekDay',
]


class ApiPortalApiTryOutEnabledState(str, Enum):
    """
    Indicates whether the API try-out feature is enabled or disabled. When enabled, users can try out the API by sending requests and viewing responses in API portal. When disabled, users cannot try out the API.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ApmType(str, Enum):
    """
    Type of application performance monitoring
    """
    APPLICATION_INSIGHTS = "ApplicationInsights"
    APP_DYNAMICS = "AppDynamics"
    DYNATRACE = "Dynatrace"
    NEW_RELIC = "NewRelic"
    ELASTIC_APM = "ElasticAPM"


class BackendProtocol(str, Enum):
    """
    How ingress should communicate with this app backend service.
    """
    GRPC = "GRPC"
    DEFAULT = "Default"


class BindingType(str, Enum):
    """
    Buildpack Binding Type
    """
    APPLICATION_INSIGHTS = "ApplicationInsights"
    APACHE_SKY_WALKING = "ApacheSkyWalking"
    APP_DYNAMICS = "AppDynamics"
    DYNATRACE = "Dynatrace"
    NEW_RELIC = "NewRelic"
    ELASTIC_APM = "ElasticAPM"
    CA_CERTIFICATES = "CACertificates"


class ConfigServerEnabledState(str, Enum):
    """
    Enabled state of the config server. This is only used in Consumption tier.
    """
    ENABLED = "Enabled"
    """
    Enable the config server.
    """
    DISABLED = "Disabled"
    """
    Disable the config server.
    """


class ConfigurationServiceGeneration(str, Enum):
    """
    The generation of the Application Configuration Service.
    """
    GEN1 = "Gen1"
    GEN2 = "Gen2"


class CustomizedAcceleratorType(str, Enum):
    """
    Type of the customized accelerator.
    """
    ACCELERATOR = "Accelerator"
    FRAGMENT = "Fragment"


class DevToolPortalFeatureState(str, Enum):
    """
    State of the plugin
    """
    ENABLED = "Enabled"
    """
    Enable the plugin in Dev Tool Portal.
    """
    DISABLED = "Disabled"
    """
    Disable the plugin in Dev Tool Portal.
    """


class Frequency(str, Enum):
    """
    The frequency to run the maintenance job
    """
    WEEKLY = "Weekly"


class GatewayCertificateVerification(str, Enum):
    """
    Whether to enable certificate verification or not
    """
    ENABLED = "Enabled"
    """
    Enable certificate verification in Spring Cloud Gateway.
    """
    DISABLED = "Disabled"
    """
    Disable certificate verification in Spring Cloud Gateway.
    """


class GatewayRouteConfigProtocol(str, Enum):
    """
    Protocol of routed Azure Spring Apps applications.
    """
    HTTP = "HTTP"
    HTTPS = "HTTPS"


class GitImplementation(str, Enum):
    """
    Git libraries used to support various repository providers
    """
    GO_GIT = "go-git"
    LIBGIT2 = "libgit2"


class HTTPSchemeType(str, Enum):
    """
    Scheme to use for connecting to the host. Defaults to HTTP.

    Possible enum values:
     - `"HTTP"` means that the scheme used will be http://
     - `"HTTPS"` means that the scheme used will be https://
    """
    HTTP = "HTTP"
    HTTPS = "HTTPS"


class KeyVaultCertificateAutoSync(str, Enum):
    """
    Indicates whether to automatically synchronize certificate from key vault or not.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ManagedIdentityType(str, Enum):
    """
    Type of the managed identity
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class ProbeActionType(str, Enum):
    """
    The type of the action to take to perform the health check.
    """
    HTTP_GET_ACTION = "HTTPGetAction"
    TCP_SOCKET_ACTION = "TCPSocketAction"
    EXEC_ACTION = "ExecAction"


class SessionAffinity(str, Enum):
    """
    Type of the affinity, set this to Cookie to enable session affinity.
    """
    COOKIE = "Cookie"
    NONE = "None"


class StorageType(str, Enum):
    """
    The type of the storage.
    """
    STORAGE_ACCOUNT = "StorageAccount"


class Type(str, Enum):
    """
    The type of the underlying resource to mount as a persistent disk.
    """
    AZURE_FILE_VOLUME = "AzureFileVolume"


class WeekDay(str, Enum):
    """
    The day to run the maintenance job
    """
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
