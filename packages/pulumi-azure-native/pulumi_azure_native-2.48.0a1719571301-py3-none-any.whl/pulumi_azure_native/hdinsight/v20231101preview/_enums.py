# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AutoscaleType',
    'ComparisonOperator',
    'ContentEncoding',
    'DataDiskType',
    'DbConnectionAuthenticationMode',
    'DeploymentMode',
    'KeyVaultObjectType',
    'MetastoreDbConnectionAuthenticationMode',
    'OutboundType',
    'RangerUsersyncMode',
    'ScaleActionType',
    'ScheduleDay',
    'UpgradeMode',
]


class AutoscaleType(str, Enum):
    """
    User to specify which type of Autoscale to be implemented - Scheduled Based or Load Based.
    """
    SCHEDULE_BASED = "ScheduleBased"
    LOAD_BASED = "LoadBased"


class ComparisonOperator(str, Enum):
    """
    The comparison operator.
    """
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"


class ContentEncoding(str, Enum):
    """
    This property indicates if the content is encoded and is case-insensitive. Please set the value to base64 if the content is base64 encoded. Set it to none or skip it if the content is plain text.
    """
    BASE64 = "Base64"
    NONE = "None"


class DataDiskType(str, Enum):
    """
    Managed Disk Type.
    """
    STANDARD_HD_D_LRS = "Standard_HDD_LRS"
    STANDARD_SS_D_LRS = "Standard_SSD_LRS"
    STANDARD_SS_D_ZRS = "Standard_SSD_ZRS"
    PREMIUM_SS_D_LRS = "Premium_SSD_LRS"
    PREMIUM_SS_D_ZRS = "Premium_SSD_ZRS"
    PREMIUM_SS_D_V2_LRS = "Premium_SSD_v2_LRS"


class DbConnectionAuthenticationMode(str, Enum):
    """
    The authentication mode to connect to your Hive metastore database. More details: https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage?view=azuresql#authentication-and-authorization
    """
    SQL_AUTH = "SqlAuth"
    """
    The password-based authentication to connect to your Hive metastore database. 
    """
    IDENTITY_AUTH = "IdentityAuth"
    """
    The managed-identity-based authentication to connect to your Hive metastore database. 
    """


class DeploymentMode(str, Enum):
    """
    A string property that indicates the deployment mode of Flink cluster. It can have one of the following enum values => Application, Session. Default value is Session
    """
    APPLICATION = "Application"
    SESSION = "Session"


class KeyVaultObjectType(str, Enum):
    """
    Type of key vault object: secret, key or certificate.
    """
    KEY = "Key"
    SECRET = "Secret"
    CERTIFICATE = "Certificate"


class MetastoreDbConnectionAuthenticationMode(str, Enum):
    """
    The authentication mode to connect to your Hive metastore database. More details: https://learn.microsoft.com/en-us/azure/azure-sql/database/logins-create-manage?view=azuresql#authentication-and-authorization
    """
    SQL_AUTH = "SqlAuth"
    """
    The password-based authentication to connect to your Hive metastore database. 
    """
    IDENTITY_AUTH = "IdentityAuth"
    """
    The managed-identity-based authentication to connect to your Hive metastore database. 
    """


class OutboundType(str, Enum):
    """
    This can only be set at cluster pool creation time and cannot be changed later. 
    """
    LOAD_BALANCER = "loadBalancer"
    """
    The load balancer is used for egress through an AKS assigned public IP. This supports Kubernetes services of type 'loadBalancer'. 
    """
    USER_DEFINED_ROUTING = "userDefinedRouting"
    """
    Egress paths must be defined by the user. This is an advanced scenario and requires proper network configuration. 
    """


class RangerUsersyncMode(str, Enum):
    """
    User & groups can be synced automatically or via a static list that's refreshed.
    """
    STATIC = "static"
    AUTOMATIC = "automatic"


class ScaleActionType(str, Enum):
    """
    The action type.
    """
    SCALEUP = "scaleup"
    SCALEDOWN = "scaledown"


class ScheduleDay(str, Enum):
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class UpgradeMode(str, Enum):
    """
    A string property that indicates the upgrade mode to be performed on the Flink job. It can have one of the following enum values => STATELESS_UPDATE, UPDATE, LAST_STATE_UPDATE.
    """
    STATELES_S_UPDATE = "STATELESS_UPDATE"
    UPDATE = "UPDATE"
    LAS_T_STAT_E_UPDATE = "LAST_STATE_UPDATE"
