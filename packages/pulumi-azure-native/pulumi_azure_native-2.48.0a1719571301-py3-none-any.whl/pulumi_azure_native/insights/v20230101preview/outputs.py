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

__all__ = [
    'ActionGroupResponse',
    'ActionListResponse',
    'AlertRuleAllOfConditionResponse',
    'AlertRuleAnyOfOrLeafConditionResponse',
    'AlertRuleLeafConditionResponse',
]

@pulumi.output_type
class ActionGroupResponse(dict):
    """
    A pointer to an Azure Action Group.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionGroupId":
            suggest = "action_group_id"
        elif key == "actionProperties":
            suggest = "action_properties"
        elif key == "webhookProperties":
            suggest = "webhook_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ActionGroupResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ActionGroupResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ActionGroupResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_group_id: str,
                 action_properties: Optional[Mapping[str, str]] = None,
                 webhook_properties: Optional[Mapping[str, str]] = None):
        """
        A pointer to an Azure Action Group.
        :param str action_group_id: The resource ID of the Action Group. This cannot be null or empty.
        :param Mapping[str, str] action_properties: Predefined list of properties and configuration items for the action group.
        :param Mapping[str, str] webhook_properties: the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload.
        """
        pulumi.set(__self__, "action_group_id", action_group_id)
        if action_properties is not None:
            pulumi.set(__self__, "action_properties", action_properties)
        if webhook_properties is not None:
            pulumi.set(__self__, "webhook_properties", webhook_properties)

    @property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> str:
        """
        The resource ID of the Action Group. This cannot be null or empty.
        """
        return pulumi.get(self, "action_group_id")

    @property
    @pulumi.getter(name="actionProperties")
    def action_properties(self) -> Optional[Mapping[str, str]]:
        """
        Predefined list of properties and configuration items for the action group.
        """
        return pulumi.get(self, "action_properties")

    @property
    @pulumi.getter(name="webhookProperties")
    def webhook_properties(self) -> Optional[Mapping[str, str]]:
        """
        the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload.
        """
        return pulumi.get(self, "webhook_properties")


@pulumi.output_type
class ActionListResponse(dict):
    """
    A list of Activity Log Alert rule actions.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionGroups":
            suggest = "action_groups"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ActionListResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ActionListResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ActionListResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_groups: Optional[Sequence['outputs.ActionGroupResponse']] = None):
        """
        A list of Activity Log Alert rule actions.
        :param Sequence['ActionGroupResponse'] action_groups: The list of the Action Groups.
        """
        if action_groups is not None:
            pulumi.set(__self__, "action_groups", action_groups)

    @property
    @pulumi.getter(name="actionGroups")
    def action_groups(self) -> Optional[Sequence['outputs.ActionGroupResponse']]:
        """
        The list of the Action Groups.
        """
        return pulumi.get(self, "action_groups")


@pulumi.output_type
class AlertRuleAllOfConditionResponse(dict):
    """
    An Activity Log Alert rule condition that is met when all its member conditions are met.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allOf":
            suggest = "all_of"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AlertRuleAllOfConditionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AlertRuleAllOfConditionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AlertRuleAllOfConditionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 all_of: Sequence['outputs.AlertRuleAnyOfOrLeafConditionResponse']):
        """
        An Activity Log Alert rule condition that is met when all its member conditions are met.
        :param Sequence['AlertRuleAnyOfOrLeafConditionResponse'] all_of: The list of Activity Log Alert rule conditions.
        """
        pulumi.set(__self__, "all_of", all_of)

    @property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Sequence['outputs.AlertRuleAnyOfOrLeafConditionResponse']:
        """
        The list of Activity Log Alert rule conditions.
        """
        return pulumi.get(self, "all_of")


@pulumi.output_type
class AlertRuleAnyOfOrLeafConditionResponse(dict):
    """
    An Activity Log Alert rule condition that is met when all its member conditions are met.
    Each condition can be of one of the following types:
    __Important__: Each type has its unique subset of properties. Properties from different types CANNOT exist in one condition.
       * __Leaf Condition -__ must contain 'field' and either 'equals' or 'containsAny'.
      _Please note, 'anyOf' should __not__ be set in a Leaf Condition._
      * __AnyOf Condition -__ must contain __only__ 'anyOf' (which is an array of Leaf Conditions).
      _Please note, 'field', 'equals' and 'containsAny' should __not__ be set in an AnyOf Condition._
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "anyOf":
            suggest = "any_of"
        elif key == "containsAny":
            suggest = "contains_any"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AlertRuleAnyOfOrLeafConditionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AlertRuleAnyOfOrLeafConditionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AlertRuleAnyOfOrLeafConditionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 any_of: Optional[Sequence['outputs.AlertRuleLeafConditionResponse']] = None,
                 contains_any: Optional[Sequence[str]] = None,
                 equals: Optional[str] = None,
                 field: Optional[str] = None):
        """
        An Activity Log Alert rule condition that is met when all its member conditions are met.
        Each condition can be of one of the following types:
        __Important__: Each type has its unique subset of properties. Properties from different types CANNOT exist in one condition.
           * __Leaf Condition -__ must contain 'field' and either 'equals' or 'containsAny'.
          _Please note, 'anyOf' should __not__ be set in a Leaf Condition._
          * __AnyOf Condition -__ must contain __only__ 'anyOf' (which is an array of Leaf Conditions).
          _Please note, 'field', 'equals' and 'containsAny' should __not__ be set in an AnyOf Condition._

        :param Sequence['AlertRuleLeafConditionResponse'] any_of: An Activity Log Alert rule condition that is met when at least one of its member leaf conditions are met.
        :param Sequence[str] contains_any: The value of the event's field will be compared to the values in this array (case-insensitive) to determine if the condition is met.
        :param str equals: The value of the event's field will be compared to this value (case-insensitive) to determine if the condition is met.
        :param str field: The name of the Activity Log event's field that this condition will examine.
               The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties'.
        """
        if any_of is not None:
            pulumi.set(__self__, "any_of", any_of)
        if contains_any is not None:
            pulumi.set(__self__, "contains_any", contains_any)
        if equals is not None:
            pulumi.set(__self__, "equals", equals)
        if field is not None:
            pulumi.set(__self__, "field", field)

    @property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[Sequence['outputs.AlertRuleLeafConditionResponse']]:
        """
        An Activity Log Alert rule condition that is met when at least one of its member leaf conditions are met.
        """
        return pulumi.get(self, "any_of")

    @property
    @pulumi.getter(name="containsAny")
    def contains_any(self) -> Optional[Sequence[str]]:
        """
        The value of the event's field will be compared to the values in this array (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "contains_any")

    @property
    @pulumi.getter
    def equals(self) -> Optional[str]:
        """
        The value of the event's field will be compared to this value (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "equals")

    @property
    @pulumi.getter
    def field(self) -> Optional[str]:
        """
        The name of the Activity Log event's field that this condition will examine.
        The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties'.
        """
        return pulumi.get(self, "field")


@pulumi.output_type
class AlertRuleLeafConditionResponse(dict):
    """
    An Activity Log Alert rule condition that is met by comparing the field and value of an Activity Log event.
    This condition must contain 'field' and either 'equals' or 'containsAny'.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "containsAny":
            suggest = "contains_any"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AlertRuleLeafConditionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AlertRuleLeafConditionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AlertRuleLeafConditionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 contains_any: Optional[Sequence[str]] = None,
                 equals: Optional[str] = None,
                 field: Optional[str] = None):
        """
        An Activity Log Alert rule condition that is met by comparing the field and value of an Activity Log event.
        This condition must contain 'field' and either 'equals' or 'containsAny'.
        :param Sequence[str] contains_any: The value of the event's field will be compared to the values in this array (case-insensitive) to determine if the condition is met.
        :param str equals: The value of the event's field will be compared to this value (case-insensitive) to determine if the condition is met.
        :param str field: The name of the Activity Log event's field that this condition will examine.
               The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties'.
        """
        if contains_any is not None:
            pulumi.set(__self__, "contains_any", contains_any)
        if equals is not None:
            pulumi.set(__self__, "equals", equals)
        if field is not None:
            pulumi.set(__self__, "field", field)

    @property
    @pulumi.getter(name="containsAny")
    def contains_any(self) -> Optional[Sequence[str]]:
        """
        The value of the event's field will be compared to the values in this array (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "contains_any")

    @property
    @pulumi.getter
    def equals(self) -> Optional[str]:
        """
        The value of the event's field will be compared to this value (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "equals")

    @property
    @pulumi.getter
    def field(self) -> Optional[str]:
        """
        The name of the Activity Log event's field that this condition will examine.
        The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties'.
        """
        return pulumi.get(self, "field")


