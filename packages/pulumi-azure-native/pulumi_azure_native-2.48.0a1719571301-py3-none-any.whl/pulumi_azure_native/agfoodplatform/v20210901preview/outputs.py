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
    'ApiPropertiesResponse',
    'ErrorAdditionalInfoResponse',
    'ErrorDetailResponse',
    'ErrorResponseResponse',
    'IdentityResponse',
    'PrivateEndpointConnectionResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'SensorIntegrationResponse',
    'SolutionPropertiesResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class ApiPropertiesResponse(dict):
    """
    Api properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "apiFreshnessTimeInMinutes":
            suggest = "api_freshness_time_in_minutes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApiPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApiPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApiPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 api_freshness_time_in_minutes: Optional[int] = None):
        """
        Api properties.
        :param int api_freshness_time_in_minutes: Interval in minutes for which the weather data for the api needs to be refreshed.
        """
        if api_freshness_time_in_minutes is not None:
            pulumi.set(__self__, "api_freshness_time_in_minutes", api_freshness_time_in_minutes)

    @property
    @pulumi.getter(name="apiFreshnessTimeInMinutes")
    def api_freshness_time_in_minutes(self) -> Optional[int]:
        """
        Interval in minutes for which the weather data for the api needs to be refreshed.
        """
        return pulumi.get(self, "api_freshness_time_in_minutes")


@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    """
    The resource management error additional info.
    """
    def __init__(__self__, *,
                 info: Any,
                 type: str):
        """
        The resource management error additional info.
        :param Any info: The additional info.
        :param str type: The additional info type.
        """
        pulumi.set(__self__, "info", info)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def info(self) -> Any:
        """
        The additional info.
        """
        return pulumi.get(self, "info")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The additional info type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ErrorDetailResponse(dict):
    """
    The error detail.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalInfo":
            suggest = "additional_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ErrorDetailResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ErrorDetailResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ErrorDetailResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 additional_info: Sequence['outputs.ErrorAdditionalInfoResponse'],
                 code: str,
                 details: Sequence['outputs.ErrorDetailResponse'],
                 message: str,
                 target: str):
        """
        The error detail.
        :param Sequence['ErrorAdditionalInfoResponse'] additional_info: The error additional info.
        :param str code: The error code.
        :param Sequence['ErrorDetailResponse'] details: The error details.
        :param str message: The error message.
        :param str target: The error target.
        """
        pulumi.set(__self__, "additional_info", additional_info)
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "details", details)
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence['outputs.ErrorAdditionalInfoResponse']:
        """
        The error additional info.
        """
        return pulumi.get(self, "additional_info")

    @property
    @pulumi.getter
    def code(self) -> str:
        """
        The error code.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def details(self) -> Sequence['outputs.ErrorDetailResponse']:
        """
        The error details.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The error message.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def target(self) -> str:
        """
        The error target.
        """
        return pulumi.get(self, "target")


@pulumi.output_type
class ErrorResponseResponse(dict):
    """
    Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).
    """
    def __init__(__self__, *,
                 error: Optional['outputs.ErrorDetailResponse'] = None):
        """
        Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).
        :param 'ErrorDetailResponse' error: The error object.
        """
        if error is not None:
            pulumi.set(__self__, "error", error)

    @property
    @pulumi.getter
    def error(self) -> Optional['outputs.ErrorDetailResponse']:
        """
        The error object.
        """
        return pulumi.get(self, "error")


@pulumi.output_type
class IdentityResponse(dict):
    """
    Identity for the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Identity for the resource.
        :param str principal_id: The principal ID of resource identity. The value must be an UUID.
        :param str tenant_id: The tenant ID of resource. The value must be an UUID.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of resource identity. The value must be an UUID.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource. The value must be an UUID.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    The private endpoint connection resource.
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
        The private endpoint connection resource.
        :param Sequence[str] group_ids: The group ids for the private endpoint resource.
        :param str id: Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
class SensorIntegrationResponse(dict):
    """
    Sensor integration request model.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "provisioningInfo":
            suggest = "provisioning_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SensorIntegrationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SensorIntegrationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SensorIntegrationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provisioning_state: str,
                 enabled: Optional[str] = None,
                 provisioning_info: Optional['outputs.ErrorResponseResponse'] = None):
        """
        Sensor integration request model.
        :param str provisioning_state: Sensor integration instance provisioning state.
        :param str enabled: Sensor integration enable state. Allowed values are True, None
        :param 'ErrorResponseResponse' provisioning_info: Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).
        """
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if provisioning_info is not None:
            pulumi.set(__self__, "provisioning_info", provisioning_info)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Sensor integration instance provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[str]:
        """
        Sensor integration enable state. Allowed values are True, None
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="provisioningInfo")
    def provisioning_info(self) -> Optional['outputs.ErrorResponseResponse']:
        """
        Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).
        """
        return pulumi.get(self, "provisioning_info")


@pulumi.output_type
class SolutionPropertiesResponse(dict):
    """
    Solution resource properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "marketplacePublisherId":
            suggest = "marketplace_publisher_id"
        elif key == "offerId":
            suggest = "offer_id"
        elif key == "partnerId":
            suggest = "partner_id"
        elif key == "planId":
            suggest = "plan_id"
        elif key == "saasSubscriptionId":
            suggest = "saas_subscription_id"
        elif key == "saasSubscriptionName":
            suggest = "saas_subscription_name"
        elif key == "solutionId":
            suggest = "solution_id"
        elif key == "termId":
            suggest = "term_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SolutionPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SolutionPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SolutionPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 marketplace_publisher_id: str,
                 offer_id: str,
                 partner_id: str,
                 plan_id: str,
                 saas_subscription_id: str,
                 saas_subscription_name: str,
                 solution_id: str,
                 term_id: str):
        """
        Solution resource properties.
        :param str marketplace_publisher_id: SaaS application Publisher Id.
        :param str offer_id: SaaS application Offer Id.
        :param str partner_id: Partner Id of the Solution.
        :param str plan_id: SaaS application Plan Id.
        :param str saas_subscription_id: SaaS subscriptionId of the installed SaaS application.
        :param str saas_subscription_name: SaaS subscription name of the installed SaaS application.
        :param str solution_id: Solution Id.
        :param str term_id: SaaS application Term Id.
        """
        pulumi.set(__self__, "marketplace_publisher_id", marketplace_publisher_id)
        pulumi.set(__self__, "offer_id", offer_id)
        pulumi.set(__self__, "partner_id", partner_id)
        pulumi.set(__self__, "plan_id", plan_id)
        pulumi.set(__self__, "saas_subscription_id", saas_subscription_id)
        pulumi.set(__self__, "saas_subscription_name", saas_subscription_name)
        pulumi.set(__self__, "solution_id", solution_id)
        pulumi.set(__self__, "term_id", term_id)

    @property
    @pulumi.getter(name="marketplacePublisherId")
    def marketplace_publisher_id(self) -> str:
        """
        SaaS application Publisher Id.
        """
        return pulumi.get(self, "marketplace_publisher_id")

    @property
    @pulumi.getter(name="offerId")
    def offer_id(self) -> str:
        """
        SaaS application Offer Id.
        """
        return pulumi.get(self, "offer_id")

    @property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> str:
        """
        Partner Id of the Solution.
        """
        return pulumi.get(self, "partner_id")

    @property
    @pulumi.getter(name="planId")
    def plan_id(self) -> str:
        """
        SaaS application Plan Id.
        """
        return pulumi.get(self, "plan_id")

    @property
    @pulumi.getter(name="saasSubscriptionId")
    def saas_subscription_id(self) -> str:
        """
        SaaS subscriptionId of the installed SaaS application.
        """
        return pulumi.get(self, "saas_subscription_id")

    @property
    @pulumi.getter(name="saasSubscriptionName")
    def saas_subscription_name(self) -> str:
        """
        SaaS subscription name of the installed SaaS application.
        """
        return pulumi.get(self, "saas_subscription_name")

    @property
    @pulumi.getter(name="solutionId")
    def solution_id(self) -> str:
        """
        Solution Id.
        """
        return pulumi.get(self, "solution_id")

    @property
    @pulumi.getter(name="termId")
    def term_id(self) -> str:
        """
        SaaS application Term Id.
        """
        return pulumi.get(self, "term_id")


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


