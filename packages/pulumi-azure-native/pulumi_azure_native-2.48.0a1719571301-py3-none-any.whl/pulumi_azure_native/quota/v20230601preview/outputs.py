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
    'AdditionalAttributesResponse',
    'GroupQuotaSubscriptionIdResponseProperties',
    'GroupQuotasEntityBaseResponse',
    'GroupingIdResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class AdditionalAttributesResponse(dict):
    """
    Additional attribute or filter to allow subscriptions meeting the requirements to be part of the GroupQuota.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupId":
            suggest = "group_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AdditionalAttributesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AdditionalAttributesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AdditionalAttributesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_id: 'outputs.GroupingIdResponse',
                 environment: Optional[Any] = None):
        """
        Additional attribute or filter to allow subscriptions meeting the requirements to be part of the GroupQuota.
        :param 'GroupingIdResponse' group_id: The grouping Id for the group quota. It can be Billing Id or ServiceTreeId if applicable. 
        """
        pulumi.set(__self__, "group_id", group_id)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> 'outputs.GroupingIdResponse':
        """
        The grouping Id for the group quota. It can be Billing Id or ServiceTreeId if applicable. 
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def environment(self) -> Optional[Any]:
        return pulumi.get(self, "environment")


@pulumi.output_type
class GroupQuotaSubscriptionIdResponseProperties(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "subscriptionId":
            suggest = "subscription_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupQuotaSubscriptionIdResponseProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupQuotaSubscriptionIdResponseProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupQuotaSubscriptionIdResponseProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provisioning_state: str,
                 subscription_id: str):
        """
        :param str provisioning_state: Status of this subscriptionId being associated with the GroupQuotasEntity.
        :param str subscription_id: An Azure subscriptionId.
        """
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Status of this subscriptionId being associated with the GroupQuotasEntity.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        An Azure subscriptionId.
        """
        return pulumi.get(self, "subscription_id")


@pulumi.output_type
class GroupQuotasEntityBaseResponse(dict):
    """
    Properties and filters for ShareQuota. The request parameter is optional, if there are no filters specified.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "additionalAttributes":
            suggest = "additional_attributes"
        elif key == "displayName":
            suggest = "display_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupQuotasEntityBaseResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupQuotasEntityBaseResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupQuotasEntityBaseResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provisioning_state: str,
                 additional_attributes: Optional['outputs.AdditionalAttributesResponse'] = None,
                 display_name: Optional[str] = None):
        """
        Properties and filters for ShareQuota. The request parameter is optional, if there are no filters specified.
        :param str provisioning_state: Provisioning state of the operation.
        :param 'AdditionalAttributesResponse' additional_attributes: Additional attributes to filter/restrict the subscriptions, which can be added to the subscriptionIds.
        :param str display_name: Display name of the GroupQuota entity.
        """
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if additional_attributes is not None:
            pulumi.set(__self__, "additional_attributes", additional_attributes)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="additionalAttributes")
    def additional_attributes(self) -> Optional['outputs.AdditionalAttributesResponse']:
        """
        Additional attributes to filter/restrict the subscriptions, which can be added to the subscriptionIds.
        """
        return pulumi.get(self, "additional_attributes")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        Display name of the GroupQuota entity.
        """
        return pulumi.get(self, "display_name")


@pulumi.output_type
class GroupingIdResponse(dict):
    """
    The grouping Id for the group quota. It can be Billing Id or ServiceTreeId if applicable. 
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupingIdType":
            suggest = "grouping_id_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in GroupingIdResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        GroupingIdResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        GroupingIdResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 grouping_id_type: Optional[str] = None,
                 value: Optional[str] = None):
        """
        The grouping Id for the group quota. It can be Billing Id or ServiceTreeId if applicable. 
        :param str grouping_id_type: GroupingId type. It is a required property. More types of groupIds can be supported in future.
        :param str value: GroupId value based on the groupingType selected - Billing Id or ServiceTreeId.
        """
        if grouping_id_type is not None:
            pulumi.set(__self__, "grouping_id_type", grouping_id_type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="groupingIdType")
    def grouping_id_type(self) -> Optional[str]:
        """
        GroupingId type. It is a required property. More types of groupIds can be supported in future.
        """
        return pulumi.get(self, "grouping_id_type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        GroupId value based on the groupingType selected - Billing Id or ServiceTreeId.
        """
        return pulumi.get(self, "value")


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


