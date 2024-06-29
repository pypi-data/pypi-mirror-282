# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'DatadogApiKeyResponse',
    'DatadogHostMetadataResponse',
    'DatadogHostResponse',
    'DatadogInstallMethodResponse',
    'DatadogLogsAgentResponse',
    'DatadogOrganizationPropertiesResponse',
    'IdentityPropertiesResponse',
    'LinkedResourceResponse',
    'MonitorPropertiesResponse',
    'MonitoredResourceResponse',
    'ResourceSkuResponse',
    'SystemDataResponse',
    'UserInfoResponse',
]

@pulumi.output_type
class DatadogApiKeyResponse(dict):
    def __init__(__self__, *,
                 key: str,
                 created: Optional[str] = None,
                 created_by: Optional[str] = None,
                 name: Optional[str] = None):
        """
        :param str key: The value of the API key.
        :param str created: The time of creation of the API key.
        :param str created_by: The user that created the API key.
        :param str name: The name of the API key.
        """
        pulumi.set(__self__, "key", key)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The value of the API key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def created(self) -> Optional[str]:
        """
        The time of creation of the API key.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The user that created the API key.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the API key.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class DatadogHostMetadataResponse(dict):
    def __init__(__self__, *,
                 agent_version: Optional[str] = None,
                 install_method: Optional['outputs.DatadogInstallMethodResponse'] = None,
                 logs_agent: Optional['outputs.DatadogLogsAgentResponse'] = None):
        """
        :param str agent_version: The agent version.
        """
        if agent_version is not None:
            pulumi.set(__self__, "agent_version", agent_version)
        if install_method is not None:
            pulumi.set(__self__, "install_method", install_method)
        if logs_agent is not None:
            pulumi.set(__self__, "logs_agent", logs_agent)

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[str]:
        """
        The agent version.
        """
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter(name="installMethod")
    def install_method(self) -> Optional['outputs.DatadogInstallMethodResponse']:
        return pulumi.get(self, "install_method")

    @property
    @pulumi.getter(name="logsAgent")
    def logs_agent(self) -> Optional['outputs.DatadogLogsAgentResponse']:
        return pulumi.get(self, "logs_agent")


@pulumi.output_type
class DatadogHostResponse(dict):
    def __init__(__self__, *,
                 aliases: Optional[Sequence[str]] = None,
                 apps: Optional[Sequence[str]] = None,
                 meta: Optional['outputs.DatadogHostMetadataResponse'] = None,
                 name: Optional[str] = None):
        """
        :param Sequence[str] aliases: The aliases for the host.
        :param Sequence[str] apps: The Datadog integrations reporting metrics for the host.
        :param str name: The name of the host.
        """
        if aliases is not None:
            pulumi.set(__self__, "aliases", aliases)
        if apps is not None:
            pulumi.set(__self__, "apps", apps)
        if meta is not None:
            pulumi.set(__self__, "meta", meta)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def aliases(self) -> Optional[Sequence[str]]:
        """
        The aliases for the host.
        """
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter
    def apps(self) -> Optional[Sequence[str]]:
        """
        The Datadog integrations reporting metrics for the host.
        """
        return pulumi.get(self, "apps")

    @property
    @pulumi.getter
    def meta(self) -> Optional['outputs.DatadogHostMetadataResponse']:
        return pulumi.get(self, "meta")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the host.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class DatadogInstallMethodResponse(dict):
    def __init__(__self__, *,
                 installer_version: Optional[str] = None,
                 tool: Optional[str] = None,
                 tool_version: Optional[str] = None):
        """
        :param str installer_version: The installer version.
        :param str tool: The tool.
        :param str tool_version: The tool version.
        """
        if installer_version is not None:
            pulumi.set(__self__, "installer_version", installer_version)
        if tool is not None:
            pulumi.set(__self__, "tool", tool)
        if tool_version is not None:
            pulumi.set(__self__, "tool_version", tool_version)

    @property
    @pulumi.getter(name="installerVersion")
    def installer_version(self) -> Optional[str]:
        """
        The installer version.
        """
        return pulumi.get(self, "installer_version")

    @property
    @pulumi.getter
    def tool(self) -> Optional[str]:
        """
        The tool.
        """
        return pulumi.get(self, "tool")

    @property
    @pulumi.getter(name="toolVersion")
    def tool_version(self) -> Optional[str]:
        """
        The tool version.
        """
        return pulumi.get(self, "tool_version")


@pulumi.output_type
class DatadogLogsAgentResponse(dict):
    def __init__(__self__, *,
                 transport: Optional[str] = None):
        """
        :param str transport: The transport.
        """
        if transport is not None:
            pulumi.set(__self__, "transport", transport)

    @property
    @pulumi.getter
    def transport(self) -> Optional[str]:
        """
        The transport.
        """
        return pulumi.get(self, "transport")


@pulumi.output_type
class DatadogOrganizationPropertiesResponse(dict):
    """
    Specify the Datadog organization name. In the case of linking to existing organizations, Id, ApiKey, and Applicationkey is required as well.
    """
    def __init__(__self__, *,
                 cspm: Optional[bool] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None):
        """
        Specify the Datadog organization name. In the case of linking to existing organizations, Id, ApiKey, and Applicationkey is required as well.
        :param bool cspm: The configuration which describes the state of cloud security posture management. This collects configuration information for all resources in a subscription and track conformance to industry benchmarks.
        :param str id: Id of the Datadog organization.
        :param str name: Name of the Datadog organization.
        """
        if cspm is not None:
            pulumi.set(__self__, "cspm", cspm)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def cspm(self) -> Optional[bool]:
        """
        The configuration which describes the state of cloud security posture management. This collects configuration information for all resources in a subscription and track conformance to industry benchmarks.
        """
        return pulumi.get(self, "cspm")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Id of the Datadog organization.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the Datadog organization.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class IdentityPropertiesResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        :param str principal_id: The identity ID.
        :param str tenant_id: The tenant ID of resource.
        :param str type: Specifies the identity type of the Datadog Monitor. At this time the only allowed value is 'SystemAssigned'.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The identity ID.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Specifies the identity type of the Datadog Monitor. At this time the only allowed value is 'SystemAssigned'.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class LinkedResourceResponse(dict):
    """
    The definition of a linked resource.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        The definition of a linked resource.
        :param str id: The ARM id of the linked resource.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ARM id of the linked resource.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class MonitorPropertiesResponse(dict):
    """
    Properties specific to the monitor resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "liftrResourceCategory":
            suggest = "liftr_resource_category"
        elif key == "liftrResourcePreference":
            suggest = "liftr_resource_preference"
        elif key == "marketplaceSubscriptionStatus":
            suggest = "marketplace_subscription_status"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "datadogOrganizationProperties":
            suggest = "datadog_organization_properties"
        elif key == "monitoringStatus":
            suggest = "monitoring_status"
        elif key == "userInfo":
            suggest = "user_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MonitorPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MonitorPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MonitorPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 liftr_resource_category: str,
                 liftr_resource_preference: int,
                 marketplace_subscription_status: str,
                 provisioning_state: str,
                 datadog_organization_properties: Optional['outputs.DatadogOrganizationPropertiesResponse'] = None,
                 monitoring_status: Optional[str] = None,
                 user_info: Optional['outputs.UserInfoResponse'] = None):
        """
        Properties specific to the monitor resource.
        :param int liftr_resource_preference: The priority of the resource.
        :param str marketplace_subscription_status: Flag specifying the Marketplace Subscription Status of the resource. If payment is not made in time, the resource will go in Suspended state.
        :param 'DatadogOrganizationPropertiesResponse' datadog_organization_properties: Specify the Datadog organization name. In the case of linking to existing organizations, Id, ApiKey, and Applicationkey is required as well.
        :param str monitoring_status: Flag specifying if the resource monitoring is enabled or disabled.
        :param 'UserInfoResponse' user_info: Includes name, email and optionally, phone number. User Information can't be null.
        """
        pulumi.set(__self__, "liftr_resource_category", liftr_resource_category)
        pulumi.set(__self__, "liftr_resource_preference", liftr_resource_preference)
        pulumi.set(__self__, "marketplace_subscription_status", marketplace_subscription_status)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if datadog_organization_properties is not None:
            pulumi.set(__self__, "datadog_organization_properties", datadog_organization_properties)
        if monitoring_status is not None:
            pulumi.set(__self__, "monitoring_status", monitoring_status)
        if user_info is not None:
            pulumi.set(__self__, "user_info", user_info)

    @property
    @pulumi.getter(name="liftrResourceCategory")
    def liftr_resource_category(self) -> str:
        return pulumi.get(self, "liftr_resource_category")

    @property
    @pulumi.getter(name="liftrResourcePreference")
    def liftr_resource_preference(self) -> int:
        """
        The priority of the resource.
        """
        return pulumi.get(self, "liftr_resource_preference")

    @property
    @pulumi.getter(name="marketplaceSubscriptionStatus")
    def marketplace_subscription_status(self) -> str:
        """
        Flag specifying the Marketplace Subscription Status of the resource. If payment is not made in time, the resource will go in Suspended state.
        """
        return pulumi.get(self, "marketplace_subscription_status")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="datadogOrganizationProperties")
    def datadog_organization_properties(self) -> Optional['outputs.DatadogOrganizationPropertiesResponse']:
        """
        Specify the Datadog organization name. In the case of linking to existing organizations, Id, ApiKey, and Applicationkey is required as well.
        """
        return pulumi.get(self, "datadog_organization_properties")

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> Optional[str]:
        """
        Flag specifying if the resource monitoring is enabled or disabled.
        """
        return pulumi.get(self, "monitoring_status")

    @property
    @pulumi.getter(name="userInfo")
    def user_info(self) -> Optional['outputs.UserInfoResponse']:
        """
        Includes name, email and optionally, phone number. User Information can't be null.
        """
        return pulumi.get(self, "user_info")


@pulumi.output_type
class MonitoredResourceResponse(dict):
    """
    The properties of a resource currently being monitored by the Datadog monitor resource.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 reason_for_logs_status: Optional[str] = None,
                 reason_for_metrics_status: Optional[str] = None,
                 sending_logs: Optional[bool] = None,
                 sending_metrics: Optional[bool] = None):
        """
        The properties of a resource currently being monitored by the Datadog monitor resource.
        :param str id: The ARM id of the resource.
        :param str reason_for_logs_status: Reason for why the resource is sending logs (or why it is not sending).
        :param str reason_for_metrics_status: Reason for why the resource is sending metrics (or why it is not sending).
        :param bool sending_logs: Flag indicating if resource is sending logs to Datadog.
        :param bool sending_metrics: Flag indicating if resource is sending metrics to Datadog.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if reason_for_logs_status is not None:
            pulumi.set(__self__, "reason_for_logs_status", reason_for_logs_status)
        if reason_for_metrics_status is not None:
            pulumi.set(__self__, "reason_for_metrics_status", reason_for_metrics_status)
        if sending_logs is not None:
            pulumi.set(__self__, "sending_logs", sending_logs)
        if sending_metrics is not None:
            pulumi.set(__self__, "sending_metrics", sending_metrics)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ARM id of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="reasonForLogsStatus")
    def reason_for_logs_status(self) -> Optional[str]:
        """
        Reason for why the resource is sending logs (or why it is not sending).
        """
        return pulumi.get(self, "reason_for_logs_status")

    @property
    @pulumi.getter(name="reasonForMetricsStatus")
    def reason_for_metrics_status(self) -> Optional[str]:
        """
        Reason for why the resource is sending metrics (or why it is not sending).
        """
        return pulumi.get(self, "reason_for_metrics_status")

    @property
    @pulumi.getter(name="sendingLogs")
    def sending_logs(self) -> Optional[bool]:
        """
        Flag indicating if resource is sending logs to Datadog.
        """
        return pulumi.get(self, "sending_logs")

    @property
    @pulumi.getter(name="sendingMetrics")
    def sending_metrics(self) -> Optional[bool]:
        """
        Flag indicating if resource is sending metrics to Datadog.
        """
        return pulumi.get(self, "sending_metrics")


@pulumi.output_type
class ResourceSkuResponse(dict):
    def __init__(__self__, *,
                 name: str):
        """
        :param str name: Name of the SKU in {PlanId} format. For Terraform, the only allowed value is 'linking'.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the SKU in {PlanId} format. For Terraform, the only allowed value is 'linking'.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class UserInfoResponse(dict):
    """
    Includes name, email and optionally, phone number. User Information can't be null.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "emailAddress":
            suggest = "email_address"
        elif key == "phoneNumber":
            suggest = "phone_number"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 email_address: Optional[str] = None,
                 name: Optional[str] = None,
                 phone_number: Optional[str] = None):
        """
        Includes name, email and optionally, phone number. User Information can't be null.
        :param str email_address: Email of the user used by Datadog for contacting them if needed
        :param str name: Name of the user
        :param str phone_number: Phone number of the user used by Datadog for contacting them if needed
        """
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if phone_number is not None:
            pulumi.set(__self__, "phone_number", phone_number)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[str]:
        """
        Email of the user used by Datadog for contacting them if needed
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the user
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[str]:
        """
        Phone number of the user used by Datadog for contacting them if needed
        """
        return pulumi.get(self, "phone_number")


