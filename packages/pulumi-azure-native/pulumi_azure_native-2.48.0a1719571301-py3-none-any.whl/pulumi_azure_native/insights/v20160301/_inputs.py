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
    'LocationThresholdRuleConditionArgs',
    'ManagementEventAggregationConditionArgs',
    'ManagementEventRuleConditionArgs',
    'RetentionPolicyArgs',
    'RuleEmailActionArgs',
    'RuleManagementEventClaimsDataSourceArgs',
    'RuleManagementEventDataSourceArgs',
    'RuleMetricDataSourceArgs',
    'RuleWebhookActionArgs',
    'ThresholdRuleConditionArgs',
]

@pulumi.input_type
class LocationThresholdRuleConditionArgs:
    def __init__(__self__, *,
                 failed_location_count: pulumi.Input[int],
                 odata_type: pulumi.Input[str],
                 data_source: Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]] = None,
                 window_size: Optional[pulumi.Input[str]] = None):
        """
        A rule condition based on a certain number of locations failing.
        :param pulumi.Input[int] failed_location_count: the number of locations that must fail to activate the alert.
        :param pulumi.Input[str] odata_type: specifies the type of condition. This can be one of three types: ManagementEventRuleCondition (occurrences of management events), LocationThresholdRuleCondition (based on the number of failures of a web test), and ThresholdRuleCondition (based on the threshold of a metric).
               Expected value is 'Microsoft.Azure.Management.Insights.Models.LocationThresholdRuleCondition'.
        :param pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']] data_source: the resource from which the rule collects its data. For this type dataSource will always be of type RuleMetricDataSource.
        :param pulumi.Input[str] window_size: the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. If specified then it must be between 5 minutes and 1 day.
        """
        pulumi.set(__self__, "failed_location_count", failed_location_count)
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Management.Insights.Models.LocationThresholdRuleCondition')
        if data_source is not None:
            pulumi.set(__self__, "data_source", data_source)
        if window_size is not None:
            pulumi.set(__self__, "window_size", window_size)

    @property
    @pulumi.getter(name="failedLocationCount")
    def failed_location_count(self) -> pulumi.Input[int]:
        """
        the number of locations that must fail to activate the alert.
        """
        return pulumi.get(self, "failed_location_count")

    @failed_location_count.setter
    def failed_location_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "failed_location_count", value)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        specifies the type of condition. This can be one of three types: ManagementEventRuleCondition (occurrences of management events), LocationThresholdRuleCondition (based on the number of failures of a web test), and ThresholdRuleCondition (based on the threshold of a metric).
        Expected value is 'Microsoft.Azure.Management.Insights.Models.LocationThresholdRuleCondition'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]]:
        """
        the resource from which the rule collects its data. For this type dataSource will always be of type RuleMetricDataSource.
        """
        return pulumi.get(self, "data_source")

    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]]):
        pulumi.set(self, "data_source", value)

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> Optional[pulumi.Input[str]]:
        """
        the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. If specified then it must be between 5 minutes and 1 day.
        """
        return pulumi.get(self, "window_size")

    @window_size.setter
    def window_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "window_size", value)


@pulumi.input_type
class ManagementEventAggregationConditionArgs:
    def __init__(__self__, *,
                 operator: Optional[pulumi.Input['ConditionOperator']] = None,
                 threshold: Optional[pulumi.Input[float]] = None,
                 window_size: Optional[pulumi.Input[str]] = None):
        """
        How the data that is collected should be combined over time.
        :param pulumi.Input['ConditionOperator'] operator: the condition operator.
        :param pulumi.Input[float] threshold: The threshold value that activates the alert.
        :param pulumi.Input[str] window_size: the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. If specified then it must be between 5 minutes and 1 day.
        """
        if operator is not None:
            pulumi.set(__self__, "operator", operator)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if window_size is not None:
            pulumi.set(__self__, "window_size", window_size)

    @property
    @pulumi.getter
    def operator(self) -> Optional[pulumi.Input['ConditionOperator']]:
        """
        the condition operator.
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: Optional[pulumi.Input['ConditionOperator']]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[float]]:
        """
        The threshold value that activates the alert.
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> Optional[pulumi.Input[str]]:
        """
        the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. If specified then it must be between 5 minutes and 1 day.
        """
        return pulumi.get(self, "window_size")

    @window_size.setter
    def window_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "window_size", value)


@pulumi.input_type
class ManagementEventRuleConditionArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 aggregation: Optional[pulumi.Input['ManagementEventAggregationConditionArgs']] = None,
                 data_source: Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]] = None):
        """
        A management event rule condition.
        :param pulumi.Input[str] odata_type: specifies the type of condition. This can be one of three types: ManagementEventRuleCondition (occurrences of management events), LocationThresholdRuleCondition (based on the number of failures of a web test), and ThresholdRuleCondition (based on the threshold of a metric).
               Expected value is 'Microsoft.Azure.Management.Insights.Models.ManagementEventRuleCondition'.
        :param pulumi.Input['ManagementEventAggregationConditionArgs'] aggregation: How the data that is collected should be combined over time and when the alert is activated. Note that for management event alerts aggregation is optional – if it is not provided then any event will cause the alert to activate.
        :param pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']] data_source: the resource from which the rule collects its data. For this type dataSource will always be of type RuleMetricDataSource.
        """
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Management.Insights.Models.ManagementEventRuleCondition')
        if aggregation is not None:
            pulumi.set(__self__, "aggregation", aggregation)
        if data_source is not None:
            pulumi.set(__self__, "data_source", data_source)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        specifies the type of condition. This can be one of three types: ManagementEventRuleCondition (occurrences of management events), LocationThresholdRuleCondition (based on the number of failures of a web test), and ThresholdRuleCondition (based on the threshold of a metric).
        Expected value is 'Microsoft.Azure.Management.Insights.Models.ManagementEventRuleCondition'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter
    def aggregation(self) -> Optional[pulumi.Input['ManagementEventAggregationConditionArgs']]:
        """
        How the data that is collected should be combined over time and when the alert is activated. Note that for management event alerts aggregation is optional – if it is not provided then any event will cause the alert to activate.
        """
        return pulumi.get(self, "aggregation")

    @aggregation.setter
    def aggregation(self, value: Optional[pulumi.Input['ManagementEventAggregationConditionArgs']]):
        pulumi.set(self, "aggregation", value)

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]]:
        """
        the resource from which the rule collects its data. For this type dataSource will always be of type RuleMetricDataSource.
        """
        return pulumi.get(self, "data_source")

    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]]):
        pulumi.set(self, "data_source", value)


@pulumi.input_type
class RetentionPolicyArgs:
    def __init__(__self__, *,
                 days: pulumi.Input[int],
                 enabled: pulumi.Input[bool]):
        """
        Specifies the retention policy for the log.
        :param pulumi.Input[int] days: the number of days for the retention in days. A value of 0 will retain the events indefinitely.
        :param pulumi.Input[bool] enabled: a value indicating whether the retention policy is enabled.
        """
        pulumi.set(__self__, "days", days)
        pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def days(self) -> pulumi.Input[int]:
        """
        the number of days for the retention in days. A value of 0 will retain the events indefinitely.
        """
        return pulumi.get(self, "days")

    @days.setter
    def days(self, value: pulumi.Input[int]):
        pulumi.set(self, "days", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        a value indicating whether the retention policy is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)


@pulumi.input_type
class RuleEmailActionArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 custom_emails: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 send_to_service_owners: Optional[pulumi.Input[bool]] = None):
        """
        Specifies the action to send email when the rule condition is evaluated. The discriminator is always RuleEmailAction in this case.
        :param pulumi.Input[str] odata_type: specifies the type of the action. There are two types of actions: RuleEmailAction and RuleWebhookAction.
               Expected value is 'Microsoft.Azure.Management.Insights.Models.RuleEmailAction'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_emails: the list of administrator's custom email addresses to notify of the activation of the alert.
        :param pulumi.Input[bool] send_to_service_owners: Whether the administrators (service and co-administrators) of the service should be notified when the alert is activated.
        """
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Management.Insights.Models.RuleEmailAction')
        if custom_emails is not None:
            pulumi.set(__self__, "custom_emails", custom_emails)
        if send_to_service_owners is not None:
            pulumi.set(__self__, "send_to_service_owners", send_to_service_owners)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        specifies the type of the action. There are two types of actions: RuleEmailAction and RuleWebhookAction.
        Expected value is 'Microsoft.Azure.Management.Insights.Models.RuleEmailAction'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter(name="customEmails")
    def custom_emails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        the list of administrator's custom email addresses to notify of the activation of the alert.
        """
        return pulumi.get(self, "custom_emails")

    @custom_emails.setter
    def custom_emails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "custom_emails", value)

    @property
    @pulumi.getter(name="sendToServiceOwners")
    def send_to_service_owners(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the administrators (service and co-administrators) of the service should be notified when the alert is activated.
        """
        return pulumi.get(self, "send_to_service_owners")

    @send_to_service_owners.setter
    def send_to_service_owners(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_to_service_owners", value)


@pulumi.input_type
class RuleManagementEventClaimsDataSourceArgs:
    def __init__(__self__, *,
                 email_address: Optional[pulumi.Input[str]] = None):
        """
        The claims for a rule management event data source.
        :param pulumi.Input[str] email_address: the email address.
        """
        if email_address is not None:
            pulumi.set(__self__, "email_address", email_address)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[str]]:
        """
        the email address.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_address", value)


@pulumi.input_type
class RuleManagementEventDataSourceArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 claims: Optional[pulumi.Input['RuleManagementEventClaimsDataSourceArgs']] = None,
                 event_name: Optional[pulumi.Input[str]] = None,
                 event_source: Optional[pulumi.Input[str]] = None,
                 legacy_resource_id: Optional[pulumi.Input[str]] = None,
                 level: Optional[pulumi.Input[str]] = None,
                 metric_namespace: Optional[pulumi.Input[str]] = None,
                 operation_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_location: Optional[pulumi.Input[str]] = None,
                 resource_provider_name: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 sub_status: Optional[pulumi.Input[str]] = None):
        """
        A rule management event data source. The discriminator fields is always RuleManagementEventDataSource in this case.
        :param pulumi.Input[str] odata_type: specifies the type of data source. There are two types of rule data sources: RuleMetricDataSource and RuleManagementEventDataSource
               Expected value is 'Microsoft.Azure.Management.Insights.Models.RuleManagementEventDataSource'.
        :param pulumi.Input['RuleManagementEventClaimsDataSourceArgs'] claims: the claims.
        :param pulumi.Input[str] event_name: the event name.
        :param pulumi.Input[str] event_source: the event source.
        :param pulumi.Input[str] legacy_resource_id: the legacy resource identifier of the resource the rule monitors. **NOTE**: this property cannot be updated for an existing rule.
        :param pulumi.Input[str] level: the level.
        :param pulumi.Input[str] metric_namespace: the namespace of the metric.
        :param pulumi.Input[str] operation_name: The name of the operation that should be checked for. If no name is provided, any operation will match.
        :param pulumi.Input[str] resource_group_name: the resource group name.
        :param pulumi.Input[str] resource_location: the location of the resource.
        :param pulumi.Input[str] resource_provider_name: the resource provider name.
        :param pulumi.Input[str] resource_uri: the resource identifier of the resource the rule monitors. **NOTE**: this property cannot be updated for an existing rule.
        :param pulumi.Input[str] status: The status of the operation that should be checked for. If no status is provided, any status will match.
        :param pulumi.Input[str] sub_status: the substatus.
        """
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Management.Insights.Models.RuleManagementEventDataSource')
        if claims is not None:
            pulumi.set(__self__, "claims", claims)
        if event_name is not None:
            pulumi.set(__self__, "event_name", event_name)
        if event_source is not None:
            pulumi.set(__self__, "event_source", event_source)
        if legacy_resource_id is not None:
            pulumi.set(__self__, "legacy_resource_id", legacy_resource_id)
        if level is not None:
            pulumi.set(__self__, "level", level)
        if metric_namespace is not None:
            pulumi.set(__self__, "metric_namespace", metric_namespace)
        if operation_name is not None:
            pulumi.set(__self__, "operation_name", operation_name)
        if resource_group_name is not None:
            pulumi.set(__self__, "resource_group_name", resource_group_name)
        if resource_location is not None:
            pulumi.set(__self__, "resource_location", resource_location)
        if resource_provider_name is not None:
            pulumi.set(__self__, "resource_provider_name", resource_provider_name)
        if resource_uri is not None:
            pulumi.set(__self__, "resource_uri", resource_uri)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if sub_status is not None:
            pulumi.set(__self__, "sub_status", sub_status)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        specifies the type of data source. There are two types of rule data sources: RuleMetricDataSource and RuleManagementEventDataSource
        Expected value is 'Microsoft.Azure.Management.Insights.Models.RuleManagementEventDataSource'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter
    def claims(self) -> Optional[pulumi.Input['RuleManagementEventClaimsDataSourceArgs']]:
        """
        the claims.
        """
        return pulumi.get(self, "claims")

    @claims.setter
    def claims(self, value: Optional[pulumi.Input['RuleManagementEventClaimsDataSourceArgs']]):
        pulumi.set(self, "claims", value)

    @property
    @pulumi.getter(name="eventName")
    def event_name(self) -> Optional[pulumi.Input[str]]:
        """
        the event name.
        """
        return pulumi.get(self, "event_name")

    @event_name.setter
    def event_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_name", value)

    @property
    @pulumi.getter(name="eventSource")
    def event_source(self) -> Optional[pulumi.Input[str]]:
        """
        the event source.
        """
        return pulumi.get(self, "event_source")

    @event_source.setter
    def event_source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_source", value)

    @property
    @pulumi.getter(name="legacyResourceId")
    def legacy_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        the legacy resource identifier of the resource the rule monitors. **NOTE**: this property cannot be updated for an existing rule.
        """
        return pulumi.get(self, "legacy_resource_id")

    @legacy_resource_id.setter
    def legacy_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "legacy_resource_id", value)

    @property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[str]]:
        """
        the level.
        """
        return pulumi.get(self, "level")

    @level.setter
    def level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "level", value)

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        the namespace of the metric.
        """
        return pulumi.get(self, "metric_namespace")

    @metric_namespace.setter
    def metric_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_namespace", value)

    @property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the operation that should be checked for. If no name is provided, any operation will match.
        """
        return pulumi.get(self, "operation_name")

    @operation_name.setter
    def operation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        the resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> Optional[pulumi.Input[str]]:
        """
        the location of the resource.
        """
        return pulumi.get(self, "resource_location")

    @resource_location.setter
    def resource_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_location", value)

    @property
    @pulumi.getter(name="resourceProviderName")
    def resource_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        the resource provider name.
        """
        return pulumi.get(self, "resource_provider_name")

    @resource_provider_name.setter
    def resource_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_provider_name", value)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> Optional[pulumi.Input[str]]:
        """
        the resource identifier of the resource the rule monitors. **NOTE**: this property cannot be updated for an existing rule.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_uri", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the operation that should be checked for. If no status is provided, any status will match.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="subStatus")
    def sub_status(self) -> Optional[pulumi.Input[str]]:
        """
        the substatus.
        """
        return pulumi.get(self, "sub_status")

    @sub_status.setter
    def sub_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sub_status", value)


@pulumi.input_type
class RuleMetricDataSourceArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 legacy_resource_id: Optional[pulumi.Input[str]] = None,
                 metric_name: Optional[pulumi.Input[str]] = None,
                 metric_namespace: Optional[pulumi.Input[str]] = None,
                 resource_location: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None):
        """
        A rule metric data source. The discriminator value is always RuleMetricDataSource in this case.
        :param pulumi.Input[str] odata_type: specifies the type of data source. There are two types of rule data sources: RuleMetricDataSource and RuleManagementEventDataSource
               Expected value is 'Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource'.
        :param pulumi.Input[str] legacy_resource_id: the legacy resource identifier of the resource the rule monitors. **NOTE**: this property cannot be updated for an existing rule.
        :param pulumi.Input[str] metric_name: the name of the metric that defines what the rule monitors.
        :param pulumi.Input[str] metric_namespace: the namespace of the metric.
        :param pulumi.Input[str] resource_location: the location of the resource.
        :param pulumi.Input[str] resource_uri: the resource identifier of the resource the rule monitors. **NOTE**: this property cannot be updated for an existing rule.
        """
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource')
        if legacy_resource_id is not None:
            pulumi.set(__self__, "legacy_resource_id", legacy_resource_id)
        if metric_name is not None:
            pulumi.set(__self__, "metric_name", metric_name)
        if metric_namespace is not None:
            pulumi.set(__self__, "metric_namespace", metric_namespace)
        if resource_location is not None:
            pulumi.set(__self__, "resource_location", resource_location)
        if resource_uri is not None:
            pulumi.set(__self__, "resource_uri", resource_uri)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        specifies the type of data source. There are two types of rule data sources: RuleMetricDataSource and RuleManagementEventDataSource
        Expected value is 'Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter(name="legacyResourceId")
    def legacy_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        the legacy resource identifier of the resource the rule monitors. **NOTE**: this property cannot be updated for an existing rule.
        """
        return pulumi.get(self, "legacy_resource_id")

    @legacy_resource_id.setter
    def legacy_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "legacy_resource_id", value)

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> Optional[pulumi.Input[str]]:
        """
        the name of the metric that defines what the rule monitors.
        """
        return pulumi.get(self, "metric_name")

    @metric_name.setter
    def metric_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_name", value)

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        the namespace of the metric.
        """
        return pulumi.get(self, "metric_namespace")

    @metric_namespace.setter
    def metric_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "metric_namespace", value)

    @property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> Optional[pulumi.Input[str]]:
        """
        the location of the resource.
        """
        return pulumi.get(self, "resource_location")

    @resource_location.setter
    def resource_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_location", value)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> Optional[pulumi.Input[str]]:
        """
        the resource identifier of the resource the rule monitors. **NOTE**: this property cannot be updated for an existing rule.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_uri", value)


@pulumi.input_type
class RuleWebhookActionArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 service_uri: Optional[pulumi.Input[str]] = None):
        """
        Specifies the action to post to service when the rule condition is evaluated. The discriminator is always RuleWebhookAction in this case.
        :param pulumi.Input[str] odata_type: specifies the type of the action. There are two types of actions: RuleEmailAction and RuleWebhookAction.
               Expected value is 'Microsoft.Azure.Management.Insights.Models.RuleWebhookAction'.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload.
        :param pulumi.Input[str] service_uri: the service uri to Post the notification when the alert activates or resolves.
        """
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Management.Insights.Models.RuleWebhookAction')
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if service_uri is not None:
            pulumi.set(__self__, "service_uri", service_uri)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        specifies the type of the action. There are two types of actions: RuleEmailAction and RuleWebhookAction.
        Expected value is 'Microsoft.Azure.Management.Insights.Models.RuleWebhookAction'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="serviceUri")
    def service_uri(self) -> Optional[pulumi.Input[str]]:
        """
        the service uri to Post the notification when the alert activates or resolves.
        """
        return pulumi.get(self, "service_uri")

    @service_uri.setter
    def service_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_uri", value)


@pulumi.input_type
class ThresholdRuleConditionArgs:
    def __init__(__self__, *,
                 odata_type: pulumi.Input[str],
                 operator: pulumi.Input['ConditionOperator'],
                 threshold: pulumi.Input[float],
                 data_source: Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]] = None,
                 time_aggregation: Optional[pulumi.Input['TimeAggregationOperator']] = None,
                 window_size: Optional[pulumi.Input[str]] = None):
        """
        A rule condition based on a metric crossing a threshold.
        :param pulumi.Input[str] odata_type: specifies the type of condition. This can be one of three types: ManagementEventRuleCondition (occurrences of management events), LocationThresholdRuleCondition (based on the number of failures of a web test), and ThresholdRuleCondition (based on the threshold of a metric).
               Expected value is 'Microsoft.Azure.Management.Insights.Models.ThresholdRuleCondition'.
        :param pulumi.Input['ConditionOperator'] operator: the operator used to compare the data and the threshold.
        :param pulumi.Input[float] threshold: the threshold value that activates the alert.
        :param pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']] data_source: the resource from which the rule collects its data. For this type dataSource will always be of type RuleMetricDataSource.
        :param pulumi.Input['TimeAggregationOperator'] time_aggregation: the time aggregation operator. How the data that are collected should be combined over time. The default value is the PrimaryAggregationType of the Metric.
        :param pulumi.Input[str] window_size: the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. If specified then it must be between 5 minutes and 1 day.
        """
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Management.Insights.Models.ThresholdRuleCondition')
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "threshold", threshold)
        if data_source is not None:
            pulumi.set(__self__, "data_source", data_source)
        if time_aggregation is not None:
            pulumi.set(__self__, "time_aggregation", time_aggregation)
        if window_size is not None:
            pulumi.set(__self__, "window_size", window_size)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> pulumi.Input[str]:
        """
        specifies the type of condition. This can be one of three types: ManagementEventRuleCondition (occurrences of management events), LocationThresholdRuleCondition (based on the number of failures of a web test), and ThresholdRuleCondition (based on the threshold of a metric).
        Expected value is 'Microsoft.Azure.Management.Insights.Models.ThresholdRuleCondition'.
        """
        return pulumi.get(self, "odata_type")

    @odata_type.setter
    def odata_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "odata_type", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input['ConditionOperator']:
        """
        the operator used to compare the data and the threshold.
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input['ConditionOperator']):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[float]:
        """
        the threshold value that activates the alert.
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: pulumi.Input[float]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]]:
        """
        the resource from which the rule collects its data. For this type dataSource will always be of type RuleMetricDataSource.
        """
        return pulumi.get(self, "data_source")

    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[Union['RuleManagementEventDataSourceArgs', 'RuleMetricDataSourceArgs']]]):
        pulumi.set(self, "data_source", value)

    @property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> Optional[pulumi.Input['TimeAggregationOperator']]:
        """
        the time aggregation operator. How the data that are collected should be combined over time. The default value is the PrimaryAggregationType of the Metric.
        """
        return pulumi.get(self, "time_aggregation")

    @time_aggregation.setter
    def time_aggregation(self, value: Optional[pulumi.Input['TimeAggregationOperator']]):
        pulumi.set(self, "time_aggregation", value)

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> Optional[pulumi.Input[str]]:
        """
        the period of time (in ISO 8601 duration format) that is used to monitor alert activity based on the threshold. If specified then it must be between 5 minutes and 1 day.
        """
        return pulumi.get(self, "window_size")

    @window_size.setter
    def window_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "window_size", value)


