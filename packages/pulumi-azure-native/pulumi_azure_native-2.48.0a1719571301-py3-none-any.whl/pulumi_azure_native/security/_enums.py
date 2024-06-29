# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ActionType',
    'AdditionalWorkspaceDataType',
    'AdditionalWorkspaceType',
    'ApplicationSourceResourceType',
    'AssessmentStatusCode',
    'AssessmentType',
    'AuthenticationType',
    'AutoDiscovery',
    'AutoProvision',
    'Categories',
    'CloudName',
    'DataSource',
    'DescendantBehavior',
    'DevOpsPolicyType',
    'DevOpsProvisioningState',
    'Enforce',
    'EnvironmentType',
    'EventSource',
    'ExportData',
    'GovernanceRuleOwnerSourceType',
    'GovernanceRuleSourceResourceType',
    'GovernanceRuleType',
    'ImplementationEffort',
    'IsEnabled',
    'MinimalSeverity',
    'OfferingType',
    'Operator',
    'OrganizationMembershipType',
    'PricingTier',
    'PropertyType',
    'Protocol',
    'RecommendationConfigStatus',
    'RecommendationType',
    'Roles',
    'RuleState',
    'ScanningMode',
    'SecuritySolutionStatus',
    'ServerVulnerabilityAssessmentsAzureSettingSelectedProvider',
    'ServerVulnerabilityAssessmentsSettingKind',
    'Severity',
    'SeverityEnum',
    'Source',
    'StandardSupportedClouds',
    'State',
    'Status',
    'StatusReason',
    'SubPlan',
    'SupportedCloudEnum',
    'Tactics',
    'Techniques',
    'Threats',
    'Type',
    'UnmaskedIpLoggingStatus',
    'UserImpact',
]


class ActionType(str, Enum):
    """
    The type of the action that will be triggered by the Automation
    """
    LOGIC_APP = "LogicApp"
    EVENT_HUB = "EventHub"
    WORKSPACE = "Workspace"


class AdditionalWorkspaceDataType(str, Enum):
    """
    Data types sent to workspace.
    """
    ALERTS = "Alerts"
    RAW_EVENTS = "RawEvents"


class AdditionalWorkspaceType(str, Enum):
    """
    Workspace type.
    """
    SENTINEL = "Sentinel"


class ApplicationSourceResourceType(str, Enum):
    """
    The application source, what it affects, e.g. Assessments
    """
    ASSESSMENTS = "Assessments"
    """
    The source of the application is assessments
    """


class AssessmentStatusCode(str, Enum):
    """
    Programmatic code for the status of the assessment
    """
    HEALTHY = "Healthy"
    """
    The resource is healthy
    """
    UNHEALTHY = "Unhealthy"
    """
    The resource has a security issue that needs to be addressed
    """
    NOT_APPLICABLE = "NotApplicable"
    """
    Assessment for this resource did not happen
    """


class AssessmentType(str, Enum):
    """
    BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition
    """
    BUILT_IN = "BuiltIn"
    """
    Microsoft Defender for Cloud managed assessments
    """
    CUSTOM_POLICY = "CustomPolicy"
    """
    User defined policies that are automatically ingested from Azure Policy to Microsoft Defender for Cloud
    """
    CUSTOMER_MANAGED = "CustomerManaged"
    """
    User assessments pushed directly by the user or other third party to Microsoft Defender for Cloud
    """


class AuthenticationType(str, Enum):
    """
    Connect to your cloud account, for AWS use either account credentials or role-based authentication. For GCP use account organization credentials.
    """
    AWS_CREDS = "awsCreds"
    """
    AWS cloud account connector user credentials authentication
    """
    AWS_ASSUME_ROLE = "awsAssumeRole"
    """
    AWS account connector assume role authentication
    """
    GCP_CREDENTIALS = "gcpCredentials"
    """
    GCP account connector service to service authentication
    """


class AutoDiscovery(str, Enum):
    """
    AutoDiscovery states.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    NOT_APPLICABLE = "NotApplicable"


class AutoProvision(str, Enum):
    """
    Whether or not to automatically install Azure Arc (hybrid compute) agents on machines
    """
    ON = "On"
    """
    Install missing Azure Arc agents on machines automatically
    """
    OFF = "Off"
    """
    Do not install Azure Arc agent on the machines automatically
    """


class Categories(str, Enum):
    """
    The categories of resource that is at risk when the assessment is unhealthy
    """
    COMPUTE = "Compute"
    NETWORKING = "Networking"
    DATA = "Data"
    IDENTITY_AND_ACCESS = "IdentityAndAccess"
    IO_T = "IoT"


class CloudName(str, Enum):
    """
    The multi cloud resource's cloud name.
    """
    AZURE = "Azure"
    AWS = "AWS"
    GCP = "GCP"
    GITHUB = "Github"
    AZURE_DEV_OPS = "AzureDevOps"
    GIT_LAB = "GitLab"


class DataSource(str, Enum):
    TWIN_DATA = "TwinData"
    """
    Devices twin data
    """


class DescendantBehavior(str, Enum):
    """
    The behavior of a policy on descendant resources.
    """
    UNKNOWN = "Unknown"
    OVERRIDE = "Override"
    FALL_BACK = "FallBack"


class DevOpsPolicyType(str, Enum):
    """
    DevOps Policy resource types.
    """
    UNKNOWN = "Unknown"
    PIPELINE = "Pipeline"


class DevOpsProvisioningState(str, Enum):
    """
    The provisioning state of the resource.
    
    Pending - Provisioning pending.
    Failed - Provisioning failed.
    Succeeded - Successful provisioning.
    Canceled - Provisioning canceled.
    PendingDeletion - Deletion pending.
    DeletionSuccess - Deletion successful.
    DeletionFailure - Deletion failure.
    """
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PENDING = "Pending"
    PENDING_DELETION = "PendingDeletion"
    DELETION_SUCCESS = "DeletionSuccess"
    DELETION_FAILURE = "DeletionFailure"


class Enforce(str, Enum):
    """
    If set to "False", it allows the descendants of this scope to override the pricing configuration set on this scope (allows setting inherited="False"). If set to "True", it prevents overrides and forces this pricing configuration on all the descendants of this scope. This field is only available for subscription-level pricing.
    """
    FALSE = "False"
    """
    Allows the descendants of this scope to override the pricing configuration set on this scope (allows setting inherited="False")
    """
    TRUE = "True"
    """
    Prevents overrides and forces the current scope's pricing configuration to all descendants
    """


class EnvironmentType(str, Enum):
    """
    The type of the environment data.
    """
    AWS_ACCOUNT = "AwsAccount"
    GCP_PROJECT = "GcpProject"
    GITHUB_SCOPE = "GithubScope"
    AZURE_DEV_OPS_SCOPE = "AzureDevOpsScope"
    GITLAB_SCOPE = "GitlabScope"


class EventSource(str, Enum):
    """
    A valid event source type.
    """
    ASSESSMENTS = "Assessments"
    ASSESSMENTS_SNAPSHOT = "AssessmentsSnapshot"
    SUB_ASSESSMENTS = "SubAssessments"
    SUB_ASSESSMENTS_SNAPSHOT = "SubAssessmentsSnapshot"
    ALERTS = "Alerts"
    SECURE_SCORES = "SecureScores"
    SECURE_SCORES_SNAPSHOT = "SecureScoresSnapshot"
    SECURE_SCORE_CONTROLS = "SecureScoreControls"
    SECURE_SCORE_CONTROLS_SNAPSHOT = "SecureScoreControlsSnapshot"
    REGULATORY_COMPLIANCE_ASSESSMENT = "RegulatoryComplianceAssessment"
    REGULATORY_COMPLIANCE_ASSESSMENT_SNAPSHOT = "RegulatoryComplianceAssessmentSnapshot"


class ExportData(str, Enum):
    RAW_EVENTS = "RawEvents"
    """
    Agent raw events
    """


class GovernanceRuleOwnerSourceType(str, Enum):
    """
    The owner type for the governance rule owner source
    """
    BY_TAG = "ByTag"
    """
    The rule source type defined using resource tag
    """
    MANUALLY = "Manually"
    """
    The rule source type defined manually
    """


class GovernanceRuleSourceResourceType(str, Enum):
    """
    The governance rule source, what the rule affects, e.g. Assessments
    """
    ASSESSMENTS = "Assessments"
    """
    The source of the governance rule is assessments
    """


class GovernanceRuleType(str, Enum):
    """
    The rule type of the governance rule, defines the source of the rule e.g. Integrated
    """
    INTEGRATED = "Integrated"
    """
    The source of the rule type definition is integrated
    """
    SERVICE_NOW = "ServiceNow"
    """
    The source of the rule type definition is ServiceNow
    """


class ImplementationEffort(str, Enum):
    """
    The implementation effort required to remediate this assessment
    """
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"


class IsEnabled(str, Enum):
    """
    Indicates whether the extension is enabled.
    """
    TRUE = "True"
    """
    Indicates the extension is enabled
    """
    FALSE = "False"
    """
    Indicates the extension is disabled
    """


class MinimalSeverity(str, Enum):
    """
    Defines the minimal alert severity which will be sent as email notifications
    """
    HIGH = "High"
    """
    Get notifications on new alerts with High severity
    """
    MEDIUM = "Medium"
    """
    Get notifications on new alerts with medium or high severity
    """
    LOW = "Low"
    """
    Don't get notifications on new alerts with low, medium or high severity
    """


class OfferingType(str, Enum):
    """
    The type of the security offering.
    """
    CSPM_MONITOR_AWS = "CspmMonitorAws"
    DEFENDER_FOR_CONTAINERS_AWS = "DefenderForContainersAws"
    DEFENDER_FOR_SERVERS_AWS = "DefenderForServersAws"
    DEFENDER_FOR_DATABASES_AWS = "DefenderForDatabasesAws"
    INFORMATION_PROTECTION_AWS = "InformationProtectionAws"
    CSPM_MONITOR_GCP = "CspmMonitorGcp"
    CSPM_MONITOR_GITHUB = "CspmMonitorGithub"
    CSPM_MONITOR_AZURE_DEV_OPS = "CspmMonitorAzureDevOps"
    DEFENDER_FOR_SERVERS_GCP = "DefenderForServersGcp"
    DEFENDER_FOR_CONTAINERS_GCP = "DefenderForContainersGcp"
    DEFENDER_FOR_DATABASES_GCP = "DefenderForDatabasesGcp"
    DEFENDER_CSPM_AWS = "DefenderCspmAws"
    DEFENDER_CSPM_GCP = "DefenderCspmGcp"
    DEFENDER_FOR_DEV_OPS_GITHUB = "DefenderForDevOpsGithub"
    DEFENDER_FOR_DEV_OPS_AZURE_DEV_OPS = "DefenderForDevOpsAzureDevOps"
    CSPM_MONITOR_GIT_LAB = "CspmMonitorGitLab"
    DEFENDER_FOR_DEV_OPS_GIT_LAB = "DefenderForDevOpsGitLab"


class Operator(str, Enum):
    """
    A valid comparer operator to use. A case-insensitive comparison will be applied for String PropertyType.
    """
    EQUALS = "Equals"
    """
    Applies for decimal and non-decimal operands
    """
    GREATER_THAN = "GreaterThan"
    """
    Applies only for decimal operands
    """
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    """
    Applies only for decimal operands
    """
    LESSER_THAN = "LesserThan"
    """
    Applies only for decimal operands
    """
    LESSER_THAN_OR_EQUAL_TO = "LesserThanOrEqualTo"
    """
    Applies only for decimal operands
    """
    NOT_EQUALS = "NotEquals"
    """
    Applies  for decimal and non-decimal operands
    """
    CONTAINS = "Contains"
    """
    Applies only for non-decimal operands
    """
    STARTS_WITH = "StartsWith"
    """
    Applies only for non-decimal operands
    """
    ENDS_WITH = "EndsWith"
    """
    Applies only for non-decimal operands
    """


class OrganizationMembershipType(str, Enum):
    """
    The multi cloud account's membership type in the organization
    """
    MEMBER = "Member"
    ORGANIZATION = "Organization"


class PricingTier(str, Enum):
    """
    Indicates whether the Defender plan is enabled on the selected scope. Microsoft Defender for Cloud is provided in two pricing tiers: free and standard. The standard tier offers advanced security capabilities, while the free tier offers basic security features.
    """
    FREE = "Free"
    """
    Get free Microsoft Defender for Cloud experience with basic security features
    """
    STANDARD = "Standard"
    """
    Get the standard Microsoft Defender for Cloud experience with advanced security features
    """


class PropertyType(str, Enum):
    """
    The data type of the compared operands (string, integer, floating point number or a boolean [true/false]]
    """
    STRING = "String"
    INTEGER = "Integer"
    NUMBER = "Number"
    BOOLEAN = "Boolean"


class Protocol(str, Enum):
    TCP = "TCP"
    UDP = "UDP"
    ALL = "*"


class RecommendationConfigStatus(str, Enum):
    """
    Recommendation status. When the recommendation status is disabled recommendations are not generated.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class RecommendationType(str, Enum):
    """
    The type of IoT Security recommendation.
    """
    IO_T_ACR_AUTHENTICATION = "IoT_ACRAuthentication"
    """
    Authentication schema used for pull an edge module from an ACR repository does not use Service Principal Authentication.
    """
    IO_T_AGENT_SENDS_UNUTILIZED_MESSAGES = "IoT_AgentSendsUnutilizedMessages"
    """
    IoT agent message size capacity is currently underutilized, causing an increase in the number of sent messages. Adjust message intervals for better utilization.
    """
    IO_T_BASELINE = "IoT_Baseline"
    """
    Identified security related system configuration issues.
    """
    IO_T_EDGE_HUB_MEM_OPTIMIZE = "IoT_EdgeHubMemOptimize"
    """
    You can optimize Edge Hub memory usage by turning off protocol heads for any protocols not used by Edge modules in your solution.
    """
    IO_T_EDGE_LOGGING_OPTIONS = "IoT_EdgeLoggingOptions"
    """
    Logging is disabled for this edge module.
    """
    IO_T_INCONSISTENT_MODULE_SETTINGS = "IoT_InconsistentModuleSettings"
    """
    A minority within a device security group has inconsistent Edge Module settings with the rest of their group.
    """
    IO_T_INSTALL_AGENT = "IoT_InstallAgent"
    """
    Install the Azure Security of Things Agent.
    """
    IO_T_IP_FILTER_DENY_ALL = "IoT_IPFilter_DenyAll"
    """
    IP Filter Configuration should have rules defined for allowed traffic and should deny all other traffic by default.
    """
    IO_T_IP_FILTER_PERMISSIVE_RULE = "IoT_IPFilter_PermissiveRule"
    """
    An Allow IP Filter rules source IP range is too large. Overly permissive rules might expose your IoT hub to malicious intenders.
    """
    IO_T_OPEN_PORTS = "IoT_OpenPorts"
    """
    A listening endpoint was found on the device.
    """
    IO_T_PERMISSIVE_FIREWALL_POLICY = "IoT_PermissiveFirewallPolicy"
    """
    An Allowed firewall policy was found (INPUT/OUTPUT). The policy should Deny all traffic by default and define rules to allow necessary communication to/from the device.
    """
    IO_T_PERMISSIVE_INPUT_FIREWALL_RULES = "IoT_PermissiveInputFirewallRules"
    """
    A rule in the firewall has been found that contains a permissive pattern for a wide range of IP addresses or Ports.
    """
    IO_T_PERMISSIVE_OUTPUT_FIREWALL_RULES = "IoT_PermissiveOutputFirewallRules"
    """
    A rule in the firewall has been found that contains a permissive pattern for a wide range of IP addresses or Ports.
    """
    IO_T_PRIVILEGED_DOCKER_OPTIONS = "IoT_PrivilegedDockerOptions"
    """
    Edge module is configured to run in privileged mode, with extensive Linux capabilities or with host-level network access (send/receive data to host machine).
    """
    IO_T_SHARED_CREDENTIALS = "IoT_SharedCredentials"
    """
    Same authentication credentials to the IoT Hub used by multiple devices. This could indicate an illegitimate device impersonating a legitimate device. It also exposes the risk of device impersonation by an attacker.
    """
    IO_T_VULNERABLE_TLS_CIPHER_SUITE = "IoT_VulnerableTLSCipherSuite"
    """
    Insecure TLS configurations detected. Immediate upgrade recommended.
    """


class Roles(str, Enum):
    """
    A possible role to configure sending security notification alerts to
    """
    ACCOUNT_ADMIN = "AccountAdmin"
    """
    If enabled, send notification on new alerts to the account admins
    """
    SERVICE_ADMIN = "ServiceAdmin"
    """
    If enabled, send notification on new alerts to the service admins
    """
    OWNER = "Owner"
    """
    If enabled, send notification on new alerts to the subscription owners
    """
    CONTRIBUTOR = "Contributor"
    """
    If enabled, send notification on new alerts to the subscription contributors
    """


class RuleState(str, Enum):
    """
    Possible states of the rule
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    EXPIRED = "Expired"


class ScanningMode(str, Enum):
    """
    The scanning mode for the VM scan.
    """
    DEFAULT = "Default"


class SecuritySolutionStatus(str, Enum):
    """
    Status of the IoT Security solution.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ServerVulnerabilityAssessmentsAzureSettingSelectedProvider(str, Enum):
    """
    The selected vulnerability assessments provider on Azure servers in the defined scope.
    """
    MDE_TVM = "MdeTvm"
    """
    Microsoft Defender for Endpoints threat and vulnerability management.
    """


class ServerVulnerabilityAssessmentsSettingKind(str, Enum):
    """
    The kind of the server vulnerability assessments setting.
    """
    AZURE_SERVERS_SETTING = "AzureServersSetting"


class Severity(str, Enum):
    """
    The severity level of the assessment
    """
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class SeverityEnum(str, Enum):
    """
    The severity to relate to the assessments generated by this assessment automation.
    """
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Source(str, Enum):
    """
    The platform where the assessed resource resides
    """
    AZURE = "Azure"
    """
    Resource is in Azure
    """
    ON_PREMISE = "OnPremise"
    """
    Resource in an on premise machine connected to Azure cloud
    """
    ON_PREMISE_SQL = "OnPremiseSql"
    """
    SQL Resource in an on premise machine connected to Azure cloud
    """


class StandardSupportedClouds(str, Enum):
    """
    The cloud that the standard is supported on.
    """
    AWS = "AWS"
    GCP = "GCP"


class State(str, Enum):
    """
    Defines whether to send email notifications from AMicrosoft Defender for Cloud to persons with specific RBAC roles on the subscription.
    """
    ON = "On"
    """
    Send notification on new alerts to the subscription's admins
    """
    OFF = "Off"
    """
    Don't send notification on new alerts to the subscription's admins
    """


class Status(str, Enum):
    """
    The status of the port
    """
    REVOKED = "Revoked"
    INITIATED = "Initiated"


class StatusReason(str, Enum):
    """
    A description of why the `status` has its value
    """
    EXPIRED = "Expired"
    USER_REQUESTED = "UserRequested"
    NEWER_REQUEST_INITIATED = "NewerRequestInitiated"


class SubPlan(str, Enum):
    """
    The available sub plans
    """
    P1 = "P1"
    P2 = "P2"


class SupportedCloudEnum(str, Enum):
    """
    Relevant cloud for the custom assessment automation.
    """
    AWS = "AWS"
    GCP = "GCP"


class Tactics(str, Enum):
    """
    Tactic of the assessment
    """
    RECONNAISSANCE = "Reconnaissance"
    RESOURCE_DEVELOPMENT = "Resource Development"
    INITIAL_ACCESS = "Initial Access"
    EXECUTION = "Execution"
    PERSISTENCE = "Persistence"
    PRIVILEGE_ESCALATION = "Privilege Escalation"
    DEFENSE_EVASION = "Defense Evasion"
    CREDENTIAL_ACCESS = "Credential Access"
    DISCOVERY = "Discovery"
    LATERAL_MOVEMENT = "Lateral Movement"
    COLLECTION = "Collection"
    COMMAND_AND_CONTROL = "Command and Control"
    EXFILTRATION = "Exfiltration"
    IMPACT = "Impact"


class Techniques(str, Enum):
    """
    Techniques of the assessment
    """
    ABUSE_ELEVATION_CONTROL_MECHANISM = "Abuse Elevation Control Mechanism"
    ACCESS_TOKEN_MANIPULATION = "Access Token Manipulation"
    ACCOUNT_DISCOVERY = "Account Discovery"
    ACCOUNT_MANIPULATION = "Account Manipulation"
    ACTIVE_SCANNING = "Active Scanning"
    APPLICATION_LAYER_PROTOCOL = "Application Layer Protocol"
    AUDIO_CAPTURE = "Audio Capture"
    BOOT_OR_LOGON_AUTOSTART_EXECUTION = "Boot or Logon Autostart Execution"
    BOOT_OR_LOGON_INITIALIZATION_SCRIPTS = "Boot or Logon Initialization Scripts"
    BRUTE_FORCE = "Brute Force"
    CLOUD_INFRASTRUCTURE_DISCOVERY = "Cloud Infrastructure Discovery"
    CLOUD_SERVICE_DASHBOARD = "Cloud Service Dashboard"
    CLOUD_SERVICE_DISCOVERY = "Cloud Service Discovery"
    COMMAND_AND_SCRIPTING_INTERPRETER = "Command and Scripting Interpreter"
    COMPROMISE_CLIENT_SOFTWARE_BINARY = "Compromise Client Software Binary"
    COMPROMISE_INFRASTRUCTURE = "Compromise Infrastructure"
    CONTAINER_AND_RESOURCE_DISCOVERY = "Container and Resource Discovery"
    CREATE_ACCOUNT = "Create Account"
    CREATE_OR_MODIFY_SYSTEM_PROCESS = "Create or Modify System Process"
    CREDENTIALS_FROM_PASSWORD_STORES = "Credentials from Password Stores"
    DATA_DESTRUCTION = "Data Destruction"
    DATA_ENCRYPTED_FOR_IMPACT = "Data Encrypted for Impact"
    DATA_FROM_CLOUD_STORAGE_OBJECT = "Data from Cloud Storage Object"
    DATA_FROM_CONFIGURATION_REPOSITORY = "Data from Configuration Repository"
    DATA_FROM_INFORMATION_REPOSITORIES = "Data from Information Repositories"
    DATA_FROM_LOCAL_SYSTEM = "Data from Local System"
    DATA_MANIPULATION = "Data Manipulation"
    DATA_STAGED = "Data Staged"
    DEFACEMENT = "Defacement"
    DEOBFUSCATE_DECODE_FILES_OR_INFORMATION = "Deobfuscate/Decode Files or Information"
    DISK_WIPE = "Disk Wipe"
    DOMAIN_TRUST_DISCOVERY = "Domain Trust Discovery"
    DRIVE_BY_COMPROMISE = "Drive-by Compromise"
    DYNAMIC_RESOLUTION = "Dynamic Resolution"
    ENDPOINT_DENIAL_OF_SERVICE = "Endpoint Denial of Service"
    EVENT_TRIGGERED_EXECUTION = "Event Triggered Execution"
    EXFILTRATION_OVER_ALTERNATIVE_PROTOCOL = "Exfiltration Over Alternative Protocol"
    EXPLOIT_PUBLIC_FACING_APPLICATION = "Exploit Public-Facing Application"
    EXPLOITATION_FOR_CLIENT_EXECUTION = "Exploitation for Client Execution"
    EXPLOITATION_FOR_CREDENTIAL_ACCESS = "Exploitation for Credential Access"
    EXPLOITATION_FOR_DEFENSE_EVASION = "Exploitation for Defense Evasion"
    EXPLOITATION_FOR_PRIVILEGE_ESCALATION = "Exploitation for Privilege Escalation"
    EXPLOITATION_OF_REMOTE_SERVICES = "Exploitation of Remote Services"
    EXTERNAL_REMOTE_SERVICES = "External Remote Services"
    FALLBACK_CHANNELS = "Fallback Channels"
    FILE_AND_DIRECTORY_DISCOVERY = "File and Directory Discovery"
    GATHER_VICTIM_NETWORK_INFORMATION = "Gather Victim Network Information"
    HIDE_ARTIFACTS = "Hide Artifacts"
    HIJACK_EXECUTION_FLOW = "Hijack Execution Flow"
    IMPAIR_DEFENSES = "Impair Defenses"
    IMPLANT_CONTAINER_IMAGE = "Implant Container Image"
    INDICATOR_REMOVAL_ON_HOST = "Indicator Removal on Host"
    INDIRECT_COMMAND_EXECUTION = "Indirect Command Execution"
    INGRESS_TOOL_TRANSFER = "Ingress Tool Transfer"
    INPUT_CAPTURE = "Input Capture"
    INTER_PROCESS_COMMUNICATION = "Inter-Process Communication"
    LATERAL_TOOL_TRANSFER = "Lateral Tool Transfer"
    MAN_IN_THE_MIDDLE = "Man-in-the-Middle"
    MASQUERADING = "Masquerading"
    MODIFY_AUTHENTICATION_PROCESS = "Modify Authentication Process"
    MODIFY_REGISTRY = "Modify Registry"
    NETWORK_DENIAL_OF_SERVICE = "Network Denial of Service"
    NETWORK_SERVICE_SCANNING = "Network Service Scanning"
    NETWORK_SNIFFING = "Network Sniffing"
    NON_APPLICATION_LAYER_PROTOCOL = "Non-Application Layer Protocol"
    NON_STANDARD_PORT = "Non-Standard Port"
    OBTAIN_CAPABILITIES = "Obtain Capabilities"
    OBFUSCATED_FILES_OR_INFORMATION = "Obfuscated Files or Information"
    OFFICE_APPLICATION_STARTUP = "Office Application Startup"
    O_S_CREDENTIAL_DUMPING = "OS Credential Dumping"
    PERMISSION_GROUPS_DISCOVERY = "Permission Groups Discovery"
    PHISHING = "Phishing"
    PRE_O_S_BOOT = "Pre-OS Boot"
    PROCESS_DISCOVERY = "Process Discovery"
    PROCESS_INJECTION = "Process Injection"
    PROTOCOL_TUNNELING = "Protocol Tunneling"
    PROXY = "Proxy"
    QUERY_REGISTRY = "Query Registry"
    REMOTE_ACCESS_SOFTWARE = "Remote Access Software"
    REMOTE_SERVICE_SESSION_HIJACKING = "Remote Service Session Hijacking"
    REMOTE_SERVICES = "Remote Services"
    REMOTE_SYSTEM_DISCOVERY = "Remote System Discovery"
    RESOURCE_HIJACKING = "Resource Hijacking"
    SCHEDULED_TASK_JOB = "Scheduled Task/Job"
    SCREEN_CAPTURE = "Screen Capture"
    SEARCH_VICTIM_OWNED_WEBSITES = "Search Victim-Owned Websites"
    SERVER_SOFTWARE_COMPONENT = "Server Software Component"
    SERVICE_STOP = "Service Stop"
    SIGNED_BINARY_PROXY_EXECUTION = "Signed Binary Proxy Execution"
    SOFTWARE_DEPLOYMENT_TOOLS = "Software Deployment Tools"
    SQ_L_STORED_PROCEDURES = "SQL Stored Procedures"
    STEAL_OR_FORGE_KERBEROS_TICKETS = "Steal or Forge Kerberos Tickets"
    SUBVERT_TRUST_CONTROLS = "Subvert Trust Controls"
    SUPPLY_CHAIN_COMPROMISE = "Supply Chain Compromise"
    SYSTEM_INFORMATION_DISCOVERY = "System Information Discovery"
    TAINT_SHARED_CONTENT = "Taint Shared Content"
    TRAFFIC_SIGNALING = "Traffic Signaling"
    TRANSFER_DATA_TO_CLOUD_ACCOUNT = "Transfer Data to Cloud Account"
    TRUSTED_RELATIONSHIP = "Trusted Relationship"
    UNSECURED_CREDENTIALS = "Unsecured Credentials"
    USER_EXECUTION = "User Execution"
    VALID_ACCOUNTS = "Valid Accounts"
    WINDOWS_MANAGEMENT_INSTRUMENTATION = "Windows Management Instrumentation"
    FILE_AND_DIRECTORY_PERMISSIONS_MODIFICATION = "File and Directory Permissions Modification"


class Threats(str, Enum):
    """
    Threats impact of the assessment
    """
    ACCOUNT_BREACH = "accountBreach"
    DATA_EXFILTRATION = "dataExfiltration"
    DATA_SPILLAGE = "dataSpillage"
    MALICIOUS_INSIDER = "maliciousInsider"
    ELEVATION_OF_PRIVILEGE = "elevationOfPrivilege"
    THREAT_RESISTANCE = "threatResistance"
    MISSING_COVERAGE = "missingCoverage"
    DENIAL_OF_SERVICE = "denialOfService"


class Type(str, Enum):
    """
    The Vulnerability Assessment solution to be provisioned. Can be either 'TVM' or 'Qualys'
    """
    QUALYS = "Qualys"
    TVM = "TVM"


class UnmaskedIpLoggingStatus(str, Enum):
    """
    Unmasked IP address logging status
    """
    DISABLED = "Disabled"
    """
    Unmasked IP logging is disabled
    """
    ENABLED = "Enabled"
    """
    Unmasked IP logging is enabled
    """


class UserImpact(str, Enum):
    """
    The user impact of the assessment
    """
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
