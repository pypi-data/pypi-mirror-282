# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BillingType',
    'ClusterSkuNameEnum',
    'ColumnDataTypeHintEnum',
    'ColumnTypeEnum',
    'DataSourceKind',
    'IdentityType',
    'LinkedServiceEntityStatus',
    'MachineGroupType',
    'PublicNetworkAccessType',
    'TablePlanEnum',
    'WorkspaceSkuNameEnum',
]


class BillingType(str, Enum):
    """
    The cluster's billing type.
    """
    CLUSTER = "Cluster"
    WORKSPACES = "Workspaces"


class ClusterSkuNameEnum(str, Enum):
    """
    The name of the SKU.
    """
    CAPACITY_RESERVATION = "CapacityReservation"


class ColumnDataTypeHintEnum(str, Enum):
    """
    Column data type logical hint.
    """
    URI = "uri"
    """
    A string that matches the pattern of a URI, for example, scheme://username:password@host:1234/this/is/a/path?k1=v1&k2=v2#fragment
    """
    GUID = "guid"
    """
    A standard 128-bit GUID following the standard shape, xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    """
    ARM_PATH = "armPath"
    """
    An Azure Resource Model (ARM) path: /subscriptions/{...}/resourceGroups/{...}/providers/Microsoft.{...}/{...}/{...}/{...}...
    """
    IP = "ip"
    """
    A standard V4/V6 ip address following the standard shape, x.x.x.x/y:y:y:y:y:y:y:y
    """


class ColumnTypeEnum(str, Enum):
    """
    Column data type.
    """
    STRING = "string"
    INT = "int"
    LONG = "long"
    REAL = "real"
    BOOLEAN = "boolean"
    DATE_TIME = "dateTime"
    GUID = "guid"
    DYNAMIC = "dynamic"


class DataSourceKind(str, Enum):
    """
    The kind of the DataSource.
    """
    WINDOWS_EVENT = "WindowsEvent"
    WINDOWS_PERFORMANCE_COUNTER = "WindowsPerformanceCounter"
    IIS_LOGS = "IISLogs"
    LINUX_SYSLOG = "LinuxSyslog"
    LINUX_SYSLOG_COLLECTION = "LinuxSyslogCollection"
    LINUX_PERFORMANCE_OBJECT = "LinuxPerformanceObject"
    LINUX_PERFORMANCE_COLLECTION = "LinuxPerformanceCollection"
    CUSTOM_LOG = "CustomLog"
    CUSTOM_LOG_COLLECTION = "CustomLogCollection"
    AZURE_AUDIT_LOG = "AzureAuditLog"
    AZURE_ACTIVITY_LOG = "AzureActivityLog"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    CHANGE_TRACKING_CUSTOM_PATH = "ChangeTrackingCustomPath"
    CHANGE_TRACKING_PATH = "ChangeTrackingPath"
    CHANGE_TRACKING_SERVICES = "ChangeTrackingServices"
    CHANGE_TRACKING_DATA_TYPE_CONFIGURATION = "ChangeTrackingDataTypeConfiguration"
    CHANGE_TRACKING_DEFAULT_REGISTRY = "ChangeTrackingDefaultRegistry"
    CHANGE_TRACKING_REGISTRY = "ChangeTrackingRegistry"
    CHANGE_TRACKING_LINUX_PATH = "ChangeTrackingLinuxPath"
    LINUX_CHANGE_TRACKING_PATH = "LinuxChangeTrackingPath"
    CHANGE_TRACKING_CONTENT_LOCATION = "ChangeTrackingContentLocation"
    WINDOWS_TELEMETRY = "WindowsTelemetry"
    OFFICE365 = "Office365"
    SECURITY_WINDOWS_BASELINE_CONFIGURATION = "SecurityWindowsBaselineConfiguration"
    SECURITY_CENTER_SECURITY_WINDOWS_BASELINE_CONFIGURATION = "SecurityCenterSecurityWindowsBaselineConfiguration"
    SECURITY_EVENT_COLLECTION_CONFIGURATION = "SecurityEventCollectionConfiguration"
    SECURITY_INSIGHTS_SECURITY_EVENT_COLLECTION_CONFIGURATION = "SecurityInsightsSecurityEventCollectionConfiguration"
    IMPORT_COMPUTER_GROUP = "ImportComputerGroup"
    NETWORK_MONITORING = "NetworkMonitoring"
    ITSM = "Itsm"
    DNS_ANALYTICS = "DnsAnalytics"
    APPLICATION_INSIGHTS = "ApplicationInsights"
    SQL_DATA_CLASSIFICATION = "SqlDataClassification"


class IdentityType(str, Enum):
    """
    Type of managed service identity.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class LinkedServiceEntityStatus(str, Enum):
    """
    The provisioning state of the linked service.
    """
    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    PROVISIONING_ACCOUNT = "ProvisioningAccount"
    UPDATING = "Updating"


class MachineGroupType(str, Enum):
    """
    Type of the machine group
    """
    UNKNOWN = "unknown"
    AZURE_CS = "azure-cs"
    AZURE_SF = "azure-sf"
    AZURE_VMSS = "azure-vmss"
    USER_STATIC = "user-static"


class PublicNetworkAccessType(str, Enum):
    """
    The network access type for accessing Log Analytics query.
    """
    ENABLED = "Enabled"
    """
    Enables connectivity to Log Analytics through public DNS.
    """
    DISABLED = "Disabled"
    """
    Disables public connectivity to Log Analytics through public DNS.
    """


class TablePlanEnum(str, Enum):
    """
    Instruct the system how to handle and charge the logs ingested to this table.
    """
    BASIC = "Basic"
    """
    Logs  that are adjusted to support high volume low value verbose logs.
    """
    ANALYTICS = "Analytics"
    """
    Logs  that allow monitoring and analytics.
    """


class WorkspaceSkuNameEnum(str, Enum):
    """
    The name of the SKU.
    """
    FREE = "Free"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PER_NODE = "PerNode"
    PER_GB2018 = "PerGB2018"
    STANDALONE = "Standalone"
    CAPACITY_RESERVATION = "CapacityReservation"
    LA_CLUSTER = "LACluster"
