# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AccessReviewHistoryInstanceArgs',
    'AccessReviewInstanceArgs',
    'AccessReviewReviewerArgs',
    'AccessReviewScopeArgs',
]

@pulumi.input_type
class AccessReviewHistoryInstanceArgs:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 expiration: Optional[pulumi.Input[str]] = None,
                 fulfilled_date_time: Optional[pulumi.Input[str]] = None,
                 review_history_period_end_date_time: Optional[pulumi.Input[str]] = None,
                 review_history_period_start_date_time: Optional[pulumi.Input[str]] = None,
                 run_date_time: Optional[pulumi.Input[str]] = None):
        """
        Access Review History Definition Instance.
        :param pulumi.Input[str] display_name: The display name for the parent history definition.
        :param pulumi.Input[str] expiration: Date time when history data report expires and the associated data is deleted.
        :param pulumi.Input[str] fulfilled_date_time: Date time when the history data report is scheduled to be generated.
        :param pulumi.Input[str] review_history_period_end_date_time: Date time used when selecting review data, all reviews included in data end on or before this date. For use only with one-time/non-recurring reports.
        :param pulumi.Input[str] review_history_period_start_date_time: Date time used when selecting review data, all reviews included in data start on or after this date. For use only with one-time/non-recurring reports.
        :param pulumi.Input[str] run_date_time: Date time when the history data report is scheduled to be generated.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if expiration is not None:
            pulumi.set(__self__, "expiration", expiration)
        if fulfilled_date_time is not None:
            pulumi.set(__self__, "fulfilled_date_time", fulfilled_date_time)
        if review_history_period_end_date_time is not None:
            pulumi.set(__self__, "review_history_period_end_date_time", review_history_period_end_date_time)
        if review_history_period_start_date_time is not None:
            pulumi.set(__self__, "review_history_period_start_date_time", review_history_period_start_date_time)
        if run_date_time is not None:
            pulumi.set(__self__, "run_date_time", run_date_time)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the parent history definition.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[str]]:
        """
        Date time when history data report expires and the associated data is deleted.
        """
        return pulumi.get(self, "expiration")

    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration", value)

    @property
    @pulumi.getter(name="fulfilledDateTime")
    def fulfilled_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        Date time when the history data report is scheduled to be generated.
        """
        return pulumi.get(self, "fulfilled_date_time")

    @fulfilled_date_time.setter
    def fulfilled_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fulfilled_date_time", value)

    @property
    @pulumi.getter(name="reviewHistoryPeriodEndDateTime")
    def review_history_period_end_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        Date time used when selecting review data, all reviews included in data end on or before this date. For use only with one-time/non-recurring reports.
        """
        return pulumi.get(self, "review_history_period_end_date_time")

    @review_history_period_end_date_time.setter
    def review_history_period_end_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "review_history_period_end_date_time", value)

    @property
    @pulumi.getter(name="reviewHistoryPeriodStartDateTime")
    def review_history_period_start_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        Date time used when selecting review data, all reviews included in data start on or after this date. For use only with one-time/non-recurring reports.
        """
        return pulumi.get(self, "review_history_period_start_date_time")

    @review_history_period_start_date_time.setter
    def review_history_period_start_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "review_history_period_start_date_time", value)

    @property
    @pulumi.getter(name="runDateTime")
    def run_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        Date time when the history data report is scheduled to be generated.
        """
        return pulumi.get(self, "run_date_time")

    @run_date_time.setter
    def run_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_date_time", value)


@pulumi.input_type
class AccessReviewInstanceArgs:
    def __init__(__self__, *,
                 backup_reviewers: Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewReviewerArgs']]]] = None,
                 end_date_time: Optional[pulumi.Input[str]] = None,
                 reviewers: Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewReviewerArgs']]]] = None,
                 start_date_time: Optional[pulumi.Input[str]] = None):
        """
        Access Review Instance.
        :param pulumi.Input[Sequence[pulumi.Input['AccessReviewReviewerArgs']]] backup_reviewers: This is the collection of backup reviewers.
        :param pulumi.Input[str] end_date_time: The DateTime when the review instance is scheduled to end.
        :param pulumi.Input[Sequence[pulumi.Input['AccessReviewReviewerArgs']]] reviewers: This is the collection of reviewers.
        :param pulumi.Input[str] start_date_time: The DateTime when the review instance is scheduled to be start.
        """
        if backup_reviewers is not None:
            pulumi.set(__self__, "backup_reviewers", backup_reviewers)
        if end_date_time is not None:
            pulumi.set(__self__, "end_date_time", end_date_time)
        if reviewers is not None:
            pulumi.set(__self__, "reviewers", reviewers)
        if start_date_time is not None:
            pulumi.set(__self__, "start_date_time", start_date_time)

    @property
    @pulumi.getter(name="backupReviewers")
    def backup_reviewers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewReviewerArgs']]]]:
        """
        This is the collection of backup reviewers.
        """
        return pulumi.get(self, "backup_reviewers")

    @backup_reviewers.setter
    def backup_reviewers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewReviewerArgs']]]]):
        pulumi.set(self, "backup_reviewers", value)

    @property
    @pulumi.getter(name="endDateTime")
    def end_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        The DateTime when the review instance is scheduled to end.
        """
        return pulumi.get(self, "end_date_time")

    @end_date_time.setter
    def end_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date_time", value)

    @property
    @pulumi.getter
    def reviewers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewReviewerArgs']]]]:
        """
        This is the collection of reviewers.
        """
        return pulumi.get(self, "reviewers")

    @reviewers.setter
    def reviewers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessReviewReviewerArgs']]]]):
        pulumi.set(self, "reviewers", value)

    @property
    @pulumi.getter(name="startDateTime")
    def start_date_time(self) -> Optional[pulumi.Input[str]]:
        """
        The DateTime when the review instance is scheduled to be start.
        """
        return pulumi.get(self, "start_date_time")

    @start_date_time.setter
    def start_date_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_date_time", value)


@pulumi.input_type
class AccessReviewReviewerArgs:
    def __init__(__self__, *,
                 principal_id: Optional[pulumi.Input[str]] = None):
        """
        Descriptor for what needs to be reviewed
        :param pulumi.Input[str] principal_id: The id of the reviewer(user/servicePrincipal)
        """
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the reviewer(user/servicePrincipal)
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)


@pulumi.input_type
class AccessReviewScopeArgs:
    def __init__(__self__, *,
                 exclude_resource_id: Optional[pulumi.Input[str]] = None,
                 exclude_role_definition_id: Optional[pulumi.Input[str]] = None,
                 expand_nested_memberships: Optional[pulumi.Input[bool]] = None,
                 inactive_duration: Optional[pulumi.Input[str]] = None,
                 include_access_below_resource: Optional[pulumi.Input[bool]] = None,
                 include_inherited_access: Optional[pulumi.Input[bool]] = None):
        """
        Descriptor for what needs to be reviewed
        :param pulumi.Input[str] exclude_resource_id: This is used to indicate the resource id(s) to exclude
        :param pulumi.Input[str] exclude_role_definition_id: This is used to indicate the role definition id(s) to exclude
        :param pulumi.Input[bool] expand_nested_memberships: Flag to indicate whether to expand nested memberships or not.
        :param pulumi.Input[str] inactive_duration: Duration users are inactive for. The value should be in ISO  8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations).This code can be used to convert TimeSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds))
        :param pulumi.Input[bool] include_access_below_resource: Flag to indicate whether to expand nested memberships or not.
        :param pulumi.Input[bool] include_inherited_access: Flag to indicate whether to expand nested memberships or not.
        """
        if exclude_resource_id is not None:
            pulumi.set(__self__, "exclude_resource_id", exclude_resource_id)
        if exclude_role_definition_id is not None:
            pulumi.set(__self__, "exclude_role_definition_id", exclude_role_definition_id)
        if expand_nested_memberships is not None:
            pulumi.set(__self__, "expand_nested_memberships", expand_nested_memberships)
        if inactive_duration is not None:
            pulumi.set(__self__, "inactive_duration", inactive_duration)
        if include_access_below_resource is not None:
            pulumi.set(__self__, "include_access_below_resource", include_access_below_resource)
        if include_inherited_access is not None:
            pulumi.set(__self__, "include_inherited_access", include_inherited_access)

    @property
    @pulumi.getter(name="excludeResourceId")
    def exclude_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        This is used to indicate the resource id(s) to exclude
        """
        return pulumi.get(self, "exclude_resource_id")

    @exclude_resource_id.setter
    def exclude_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exclude_resource_id", value)

    @property
    @pulumi.getter(name="excludeRoleDefinitionId")
    def exclude_role_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        This is used to indicate the role definition id(s) to exclude
        """
        return pulumi.get(self, "exclude_role_definition_id")

    @exclude_role_definition_id.setter
    def exclude_role_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "exclude_role_definition_id", value)

    @property
    @pulumi.getter(name="expandNestedMemberships")
    def expand_nested_memberships(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to indicate whether to expand nested memberships or not.
        """
        return pulumi.get(self, "expand_nested_memberships")

    @expand_nested_memberships.setter
    def expand_nested_memberships(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "expand_nested_memberships", value)

    @property
    @pulumi.getter(name="inactiveDuration")
    def inactive_duration(self) -> Optional[pulumi.Input[str]]:
        """
        Duration users are inactive for. The value should be in ISO  8601 format (http://en.wikipedia.org/wiki/ISO_8601#Durations).This code can be used to convert TimeSpan to a valid interval string: XmlConvert.ToString(new TimeSpan(hours, minutes, seconds))
        """
        return pulumi.get(self, "inactive_duration")

    @inactive_duration.setter
    def inactive_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inactive_duration", value)

    @property
    @pulumi.getter(name="includeAccessBelowResource")
    def include_access_below_resource(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to indicate whether to expand nested memberships or not.
        """
        return pulumi.get(self, "include_access_below_resource")

    @include_access_below_resource.setter
    def include_access_below_resource(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_access_below_resource", value)

    @property
    @pulumi.getter(name="includeInheritedAccess")
    def include_inherited_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to indicate whether to expand nested memberships or not.
        """
        return pulumi.get(self, "include_inherited_access")

    @include_inherited_access.setter
    def include_inherited_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_inherited_access", value)


