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
    'CollectorAgentPropertiesBaseResponse',
    'CollectorAgentSpnPropertiesBaseResponse',
    'CostComponentResponse',
    'EntityUptimeResponse',
    'PrivateEndpointConnectionResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'SqlDbSettingsResponse',
    'SqlMiSettingsResponse',
    'SqlVmSettingsResponse',
    'SystemDataResponse',
    'VmUptimeResponse',
]

@pulumi.output_type
class CollectorAgentPropertiesBaseResponse(dict):
    """
    Collector agent property class.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lastHeartbeatUtc":
            suggest = "last_heartbeat_utc"
        elif key == "spnDetails":
            suggest = "spn_details"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CollectorAgentPropertiesBaseResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CollectorAgentPropertiesBaseResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CollectorAgentPropertiesBaseResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: Optional[str] = None,
                 last_heartbeat_utc: Optional[str] = None,
                 spn_details: Optional['outputs.CollectorAgentSpnPropertiesBaseResponse'] = None,
                 version: Optional[str] = None):
        """
        Collector agent property class.
        :param str id: Gets the collector agent id.
        :param str last_heartbeat_utc: Gets the collector last heartbeat time.
        :param 'CollectorAgentSpnPropertiesBaseResponse' spn_details: Gets or sets the SPN details.
        :param str version: Gets the collector agent version.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if last_heartbeat_utc is not None:
            pulumi.set(__self__, "last_heartbeat_utc", last_heartbeat_utc)
        if spn_details is not None:
            pulumi.set(__self__, "spn_details", spn_details)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Gets the collector agent id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastHeartbeatUtc")
    def last_heartbeat_utc(self) -> Optional[str]:
        """
        Gets the collector last heartbeat time.
        """
        return pulumi.get(self, "last_heartbeat_utc")

    @property
    @pulumi.getter(name="spnDetails")
    def spn_details(self) -> Optional['outputs.CollectorAgentSpnPropertiesBaseResponse']:
        """
        Gets or sets the SPN details.
        """
        return pulumi.get(self, "spn_details")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Gets the collector agent version.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class CollectorAgentSpnPropertiesBaseResponse(dict):
    """
    Collector agent SPN details class.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "applicationId":
            suggest = "application_id"
        elif key == "objectId":
            suggest = "object_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CollectorAgentSpnPropertiesBaseResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CollectorAgentSpnPropertiesBaseResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CollectorAgentSpnPropertiesBaseResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 application_id: Optional[str] = None,
                 audience: Optional[str] = None,
                 authority: Optional[str] = None,
                 object_id: Optional[str] = None,
                 tenant_id: Optional[str] = None):
        """
        Collector agent SPN details class.
        :param str application_id: Gets the AAD application id.
        :param str audience: Gets the AAD audience url.
        :param str authority: Gets the AAD authority endpoint.
        :param str object_id: Gets the object id of the AAD application.
        :param str tenant_id: Gets the tenant id of the AAD application.
        """
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if audience is not None:
            pulumi.set(__self__, "audience", audience)
        if authority is not None:
            pulumi.set(__self__, "authority", authority)
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[str]:
        """
        Gets the AAD application id.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def audience(self) -> Optional[str]:
        """
        Gets the AAD audience url.
        """
        return pulumi.get(self, "audience")

    @property
    @pulumi.getter
    def authority(self) -> Optional[str]:
        """
        Gets the AAD authority endpoint.
        """
        return pulumi.get(self, "authority")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[str]:
        """
        Gets the object id of the AAD application.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        Gets the tenant id of the AAD application.
        """
        return pulumi.get(self, "tenant_id")


@pulumi.output_type
class CostComponentResponse(dict):
    """
    Class to represent the component of the cost.
    """
    def __init__(__self__, *,
                 name: str,
                 description: Optional[str] = None,
                 value: Optional[float] = None):
        """
        Class to represent the component of the cost.
        :param str name: Gets the name of the component.
        :param str description: The textual description of the component.
        :param float value: The value of the component.
        """
        pulumi.set(__self__, "name", name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the name of the component.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The textual description of the component.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def value(self) -> Optional[float]:
        """
        The value of the component.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class EntityUptimeResponse(dict):
    """
    Entity Uptime.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "daysPerMonth":
            suggest = "days_per_month"
        elif key == "hoursPerDay":
            suggest = "hours_per_day"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EntityUptimeResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EntityUptimeResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EntityUptimeResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days_per_month: Optional[int] = None,
                 hours_per_day: Optional[int] = None):
        """
        Entity Uptime.
        :param int days_per_month: Gets the days per month.
        :param int hours_per_day: Gets the hours per day.
        """
        if days_per_month is not None:
            pulumi.set(__self__, "days_per_month", days_per_month)
        if hours_per_day is not None:
            pulumi.set(__self__, "hours_per_day", hours_per_day)

    @property
    @pulumi.getter(name="daysPerMonth")
    def days_per_month(self) -> Optional[int]:
        """
        Gets the days per month.
        """
        return pulumi.get(self, "days_per_month")

    @property
    @pulumi.getter(name="hoursPerDay")
    def hours_per_day(self) -> Optional[int]:
        """
        Gets the hours per day.
        """
        return pulumi.get(self, "hours_per_day")


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    Private endpoint connection resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupIds":
            suggest = "group_ids"
        elif key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "systemData":
            suggest = "system_data"
        elif key == "privateEndpoint":
            suggest = "private_endpoint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_ids: Sequence[str],
                 id: str,
                 name: str,
                 private_link_service_connection_state: 'outputs.PrivateLinkServiceConnectionStateResponse',
                 provisioning_state: str,
                 system_data: 'outputs.SystemDataResponse',
                 type: str,
                 private_endpoint: Optional['outputs.PrivateEndpointResponse'] = None):
        """
        Private endpoint connection resource.
        :param Sequence[str] group_ids: The group ids for the private endpoint resource.
        :param str id: Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param str name: The name of the resource
        :param 'PrivateLinkServiceConnectionStateResponse' private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param str provisioning_state: The provisioning state of the private endpoint connection resource.
        :param 'SystemDataResponse' system_data: Azure Resource Manager metadata containing createdBy and modifiedBy information.
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param 'PrivateEndpointResponse' private_endpoint: The private endpoint resource.
        """
        pulumi.set(__self__, "group_ids", group_ids)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "system_data", system_data)
        pulumi.set(__self__, "type", type)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[str]:
        """
        The group ids for the private endpoint resource.
        """
        return pulumi.get(self, "group_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> 'outputs.PrivateLinkServiceConnectionStateResponse':
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointResponse']:
        """
        The private endpoint resource.
        """
        return pulumi.get(self, "private_endpoint")


@pulumi.output_type
class PrivateEndpointResponse(dict):
    """
    The private endpoint resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The private endpoint resource.
        :param str id: The ARM identifier for private endpoint.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM identifier for private endpoint.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    A collection of information about the state of the connection between service consumer and provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param str actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param str description: The reason for approval/rejection of the connection.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class SqlDbSettingsResponse(dict):
    """
    SQL database assessment settings.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "azureSqlComputeTier":
            suggest = "azure_sql_compute_tier"
        elif key == "azureSqlDataBaseType":
            suggest = "azure_sql_data_base_type"
        elif key == "azureSqlPurchaseModel":
            suggest = "azure_sql_purchase_model"
        elif key == "azureSqlServiceTier":
            suggest = "azure_sql_service_tier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SqlDbSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SqlDbSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SqlDbSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 azure_sql_compute_tier: Optional[str] = None,
                 azure_sql_data_base_type: Optional[str] = None,
                 azure_sql_purchase_model: Optional[str] = None,
                 azure_sql_service_tier: Optional[str] = None):
        """
        SQL database assessment settings.
        :param str azure_sql_compute_tier: Gets or sets the azure SQL compute tier.
        :param str azure_sql_data_base_type: Gets or sets the azure PAAS SQL instance type.
        :param str azure_sql_purchase_model: Gets or sets the azure SQL purchase model.
        :param str azure_sql_service_tier: Gets or sets the azure SQL service tier.
        """
        if azure_sql_compute_tier is not None:
            pulumi.set(__self__, "azure_sql_compute_tier", azure_sql_compute_tier)
        if azure_sql_data_base_type is not None:
            pulumi.set(__self__, "azure_sql_data_base_type", azure_sql_data_base_type)
        if azure_sql_purchase_model is not None:
            pulumi.set(__self__, "azure_sql_purchase_model", azure_sql_purchase_model)
        if azure_sql_service_tier is not None:
            pulumi.set(__self__, "azure_sql_service_tier", azure_sql_service_tier)

    @property
    @pulumi.getter(name="azureSqlComputeTier")
    def azure_sql_compute_tier(self) -> Optional[str]:
        """
        Gets or sets the azure SQL compute tier.
        """
        return pulumi.get(self, "azure_sql_compute_tier")

    @property
    @pulumi.getter(name="azureSqlDataBaseType")
    def azure_sql_data_base_type(self) -> Optional[str]:
        """
        Gets or sets the azure PAAS SQL instance type.
        """
        return pulumi.get(self, "azure_sql_data_base_type")

    @property
    @pulumi.getter(name="azureSqlPurchaseModel")
    def azure_sql_purchase_model(self) -> Optional[str]:
        """
        Gets or sets the azure SQL purchase model.
        """
        return pulumi.get(self, "azure_sql_purchase_model")

    @property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(self) -> Optional[str]:
        """
        Gets or sets the azure SQL service tier.
        """
        return pulumi.get(self, "azure_sql_service_tier")


@pulumi.output_type
class SqlMiSettingsResponse(dict):
    """
    SQL managed instance assessment settings.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "azureSqlInstanceType":
            suggest = "azure_sql_instance_type"
        elif key == "azureSqlServiceTier":
            suggest = "azure_sql_service_tier"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SqlMiSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SqlMiSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SqlMiSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 azure_sql_instance_type: Optional[str] = None,
                 azure_sql_service_tier: Optional[str] = None):
        """
        SQL managed instance assessment settings.
        :param str azure_sql_instance_type: Gets or sets the azure PAAS SQL instance type.
        :param str azure_sql_service_tier: Gets or sets the azure SQL service tier.
        """
        if azure_sql_instance_type is not None:
            pulumi.set(__self__, "azure_sql_instance_type", azure_sql_instance_type)
        if azure_sql_service_tier is not None:
            pulumi.set(__self__, "azure_sql_service_tier", azure_sql_service_tier)

    @property
    @pulumi.getter(name="azureSqlInstanceType")
    def azure_sql_instance_type(self) -> Optional[str]:
        """
        Gets or sets the azure PAAS SQL instance type.
        """
        return pulumi.get(self, "azure_sql_instance_type")

    @property
    @pulumi.getter(name="azureSqlServiceTier")
    def azure_sql_service_tier(self) -> Optional[str]:
        """
        Gets or sets the azure SQL service tier.
        """
        return pulumi.get(self, "azure_sql_service_tier")


@pulumi.output_type
class SqlVmSettingsResponse(dict):
    """
    SQL VM assessment settings.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "instanceSeries":
            suggest = "instance_series"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SqlVmSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SqlVmSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SqlVmSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 instance_series: Optional[Sequence[str]] = None):
        """
        SQL VM assessment settings.
        :param Sequence[str] instance_series: Gets or sets the Azure VM families (calling instance series to keep it
               consistent with other targets).
        """
        if instance_series is not None:
            pulumi.set(__self__, "instance_series", instance_series)

    @property
    @pulumi.getter(name="instanceSeries")
    def instance_series(self) -> Optional[Sequence[str]]:
        """
        Gets or sets the Azure VM families (calling instance series to keep it
        consistent with other targets).
        """
        return pulumi.get(self, "instance_series")


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
class VmUptimeResponse(dict):
    """
    Details on the total up-time for the VM.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "daysPerMonth":
            suggest = "days_per_month"
        elif key == "hoursPerDay":
            suggest = "hours_per_day"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VmUptimeResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VmUptimeResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VmUptimeResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days_per_month: Optional[int] = None,
                 hours_per_day: Optional[int] = None):
        """
        Details on the total up-time for the VM.
        :param int days_per_month: Number of days in a month for VM uptime.
        :param int hours_per_day: Number of hours per day for VM uptime.
        """
        if days_per_month is not None:
            pulumi.set(__self__, "days_per_month", days_per_month)
        if hours_per_day is not None:
            pulumi.set(__self__, "hours_per_day", hours_per_day)

    @property
    @pulumi.getter(name="daysPerMonth")
    def days_per_month(self) -> Optional[int]:
        """
        Number of days in a month for VM uptime.
        """
        return pulumi.get(self, "days_per_month")

    @property
    @pulumi.getter(name="hoursPerDay")
    def hours_per_day(self) -> Optional[int]:
        """
        Number of hours per day for VM uptime.
        """
        return pulumi.get(self, "hours_per_day")


