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
    'DynamicMetricCriteriaResponse',
    'DynamicThresholdFailingPeriodsResponse',
    'MetricAlertActionResponse',
    'MetricAlertMultipleResourceMultipleMetricCriteriaResponse',
    'MetricAlertSingleResourceMultipleMetricCriteriaResponse',
    'MetricCriteriaResponse',
    'MetricDimensionResponse',
    'WebtestLocationAvailabilityCriteriaResponse',
]

@pulumi.output_type
class DynamicMetricCriteriaResponse(dict):
    """
    Criterion for dynamic threshold.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "alertSensitivity":
            suggest = "alert_sensitivity"
        elif key == "criterionType":
            suggest = "criterion_type"
        elif key == "failingPeriods":
            suggest = "failing_periods"
        elif key == "metricName":
            suggest = "metric_name"
        elif key == "timeAggregation":
            suggest = "time_aggregation"
        elif key == "ignoreDataBefore":
            suggest = "ignore_data_before"
        elif key == "metricNamespace":
            suggest = "metric_namespace"
        elif key == "skipMetricValidation":
            suggest = "skip_metric_validation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DynamicMetricCriteriaResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DynamicMetricCriteriaResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DynamicMetricCriteriaResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 alert_sensitivity: str,
                 criterion_type: str,
                 failing_periods: 'outputs.DynamicThresholdFailingPeriodsResponse',
                 metric_name: str,
                 name: str,
                 operator: str,
                 time_aggregation: str,
                 dimensions: Optional[Sequence['outputs.MetricDimensionResponse']] = None,
                 ignore_data_before: Optional[str] = None,
                 metric_namespace: Optional[str] = None,
                 skip_metric_validation: Optional[bool] = None):
        """
        Criterion for dynamic threshold.
        :param str alert_sensitivity: The extent of deviation required to trigger an alert. This will affect how tight the threshold is to the metric series pattern.
        :param str criterion_type: Specifies the type of threshold criteria
               Expected value is 'DynamicThresholdCriterion'.
        :param 'DynamicThresholdFailingPeriodsResponse' failing_periods: The minimum number of violations required within the selected lookback time window required to raise an alert.
        :param str metric_name: Name of the metric.
        :param str name: Name of the criteria.
        :param str operator: The operator used to compare the metric value against the threshold.
        :param str time_aggregation: the criteria time aggregation types.
        :param Sequence['MetricDimensionResponse'] dimensions: List of dimension conditions.
        :param str ignore_data_before: Use this option to set the date from which to start learning the metric historical data and calculate the dynamic thresholds (in ISO8601 format)
        :param str metric_namespace: Namespace of the metric.
        :param bool skip_metric_validation: Allows creating an alert rule on a custom metric that isn't yet emitted, by causing the metric validation to be skipped.
        """
        pulumi.set(__self__, "alert_sensitivity", alert_sensitivity)
        pulumi.set(__self__, "criterion_type", 'DynamicThresholdCriterion')
        pulumi.set(__self__, "failing_periods", failing_periods)
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "time_aggregation", time_aggregation)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if ignore_data_before is not None:
            pulumi.set(__self__, "ignore_data_before", ignore_data_before)
        if metric_namespace is not None:
            pulumi.set(__self__, "metric_namespace", metric_namespace)
        if skip_metric_validation is not None:
            pulumi.set(__self__, "skip_metric_validation", skip_metric_validation)

    @property
    @pulumi.getter(name="alertSensitivity")
    def alert_sensitivity(self) -> str:
        """
        The extent of deviation required to trigger an alert. This will affect how tight the threshold is to the metric series pattern.
        """
        return pulumi.get(self, "alert_sensitivity")

    @property
    @pulumi.getter(name="criterionType")
    def criterion_type(self) -> str:
        """
        Specifies the type of threshold criteria
        Expected value is 'DynamicThresholdCriterion'.
        """
        return pulumi.get(self, "criterion_type")

    @property
    @pulumi.getter(name="failingPeriods")
    def failing_periods(self) -> 'outputs.DynamicThresholdFailingPeriodsResponse':
        """
        The minimum number of violations required within the selected lookback time window required to raise an alert.
        """
        return pulumi.get(self, "failing_periods")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> str:
        """
        Name of the metric.
        """
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the criteria.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operator(self) -> str:
        """
        The operator used to compare the metric value against the threshold.
        """
        return pulumi.get(self, "operator")

    @property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> str:
        """
        the criteria time aggregation types.
        """
        return pulumi.get(self, "time_aggregation")

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.MetricDimensionResponse']]:
        """
        List of dimension conditions.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="ignoreDataBefore")
    def ignore_data_before(self) -> Optional[str]:
        """
        Use this option to set the date from which to start learning the metric historical data and calculate the dynamic thresholds (in ISO8601 format)
        """
        return pulumi.get(self, "ignore_data_before")

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[str]:
        """
        Namespace of the metric.
        """
        return pulumi.get(self, "metric_namespace")

    @property
    @pulumi.getter(name="skipMetricValidation")
    def skip_metric_validation(self) -> Optional[bool]:
        """
        Allows creating an alert rule on a custom metric that isn't yet emitted, by causing the metric validation to be skipped.
        """
        return pulumi.get(self, "skip_metric_validation")


@pulumi.output_type
class DynamicThresholdFailingPeriodsResponse(dict):
    """
    The minimum number of violations required within the selected lookback time window required to raise an alert.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "minFailingPeriodsToAlert":
            suggest = "min_failing_periods_to_alert"
        elif key == "numberOfEvaluationPeriods":
            suggest = "number_of_evaluation_periods"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DynamicThresholdFailingPeriodsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DynamicThresholdFailingPeriodsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DynamicThresholdFailingPeriodsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 min_failing_periods_to_alert: float,
                 number_of_evaluation_periods: float):
        """
        The minimum number of violations required within the selected lookback time window required to raise an alert.
        :param float min_failing_periods_to_alert: The number of violations to trigger an alert. Should be smaller or equal to numberOfEvaluationPeriods.
        :param float number_of_evaluation_periods: The number of aggregated lookback points. The lookback time window is calculated based on the aggregation granularity (windowSize) and the selected number of aggregated points.
        """
        pulumi.set(__self__, "min_failing_periods_to_alert", min_failing_periods_to_alert)
        pulumi.set(__self__, "number_of_evaluation_periods", number_of_evaluation_periods)

    @property
    @pulumi.getter(name="minFailingPeriodsToAlert")
    def min_failing_periods_to_alert(self) -> float:
        """
        The number of violations to trigger an alert. Should be smaller or equal to numberOfEvaluationPeriods.
        """
        return pulumi.get(self, "min_failing_periods_to_alert")

    @property
    @pulumi.getter(name="numberOfEvaluationPeriods")
    def number_of_evaluation_periods(self) -> float:
        """
        The number of aggregated lookback points. The lookback time window is calculated based on the aggregation granularity (windowSize) and the selected number of aggregated points.
        """
        return pulumi.get(self, "number_of_evaluation_periods")


@pulumi.output_type
class MetricAlertActionResponse(dict):
    """
    An alert action.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionGroupId":
            suggest = "action_group_id"
        elif key == "webHookProperties":
            suggest = "web_hook_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MetricAlertActionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MetricAlertActionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MetricAlertActionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_group_id: Optional[str] = None,
                 web_hook_properties: Optional[Mapping[str, str]] = None):
        """
        An alert action.
        :param str action_group_id: the id of the action group to use.
        :param Mapping[str, str] web_hook_properties: This field allows specifying custom properties, which would be appended to the alert payload sent as input to the webhook.
        """
        if action_group_id is not None:
            pulumi.set(__self__, "action_group_id", action_group_id)
        if web_hook_properties is not None:
            pulumi.set(__self__, "web_hook_properties", web_hook_properties)

    @property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> Optional[str]:
        """
        the id of the action group to use.
        """
        return pulumi.get(self, "action_group_id")

    @property
    @pulumi.getter(name="webHookProperties")
    def web_hook_properties(self) -> Optional[Mapping[str, str]]:
        """
        This field allows specifying custom properties, which would be appended to the alert payload sent as input to the webhook.
        """
        return pulumi.get(self, "web_hook_properties")


@pulumi.output_type
class MetricAlertMultipleResourceMultipleMetricCriteriaResponse(dict):
    """
    Specifies the metric alert criteria for multiple resource that has multiple metric criteria.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "odataType":
            suggest = "odata_type"
        elif key == "allOf":
            suggest = "all_of"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MetricAlertMultipleResourceMultipleMetricCriteriaResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MetricAlertMultipleResourceMultipleMetricCriteriaResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MetricAlertMultipleResourceMultipleMetricCriteriaResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 odata_type: str,
                 all_of: Optional[Sequence[Any]] = None):
        """
        Specifies the metric alert criteria for multiple resource that has multiple metric criteria.
        :param str odata_type: specifies the type of the alert criteria.
               Expected value is 'Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria'.
        :param Sequence[Union['DynamicMetricCriteriaResponse', 'MetricCriteriaResponse']] all_of: the list of multiple metric criteria for this 'all of' operation. 
        """
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria')
        if all_of is not None:
            pulumi.set(__self__, "all_of", all_of)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> str:
        """
        specifies the type of the alert criteria.
        Expected value is 'Microsoft.Azure.Monitor.MultipleResourceMultipleMetricCriteria'.
        """
        return pulumi.get(self, "odata_type")

    @property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Optional[Sequence[Any]]:
        """
        the list of multiple metric criteria for this 'all of' operation. 
        """
        return pulumi.get(self, "all_of")


@pulumi.output_type
class MetricAlertSingleResourceMultipleMetricCriteriaResponse(dict):
    """
    Specifies the metric alert criteria for a single resource that has multiple metric criteria.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "odataType":
            suggest = "odata_type"
        elif key == "allOf":
            suggest = "all_of"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MetricAlertSingleResourceMultipleMetricCriteriaResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MetricAlertSingleResourceMultipleMetricCriteriaResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MetricAlertSingleResourceMultipleMetricCriteriaResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 odata_type: str,
                 all_of: Optional[Sequence['outputs.MetricCriteriaResponse']] = None):
        """
        Specifies the metric alert criteria for a single resource that has multiple metric criteria.
        :param str odata_type: specifies the type of the alert criteria.
               Expected value is 'Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria'.
        :param Sequence['MetricCriteriaResponse'] all_of: The list of metric criteria for this 'all of' operation. 
        """
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria')
        if all_of is not None:
            pulumi.set(__self__, "all_of", all_of)

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> str:
        """
        specifies the type of the alert criteria.
        Expected value is 'Microsoft.Azure.Monitor.SingleResourceMultipleMetricCriteria'.
        """
        return pulumi.get(self, "odata_type")

    @property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Optional[Sequence['outputs.MetricCriteriaResponse']]:
        """
        The list of metric criteria for this 'all of' operation. 
        """
        return pulumi.get(self, "all_of")


@pulumi.output_type
class MetricCriteriaResponse(dict):
    """
    Criterion to filter metrics.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "criterionType":
            suggest = "criterion_type"
        elif key == "metricName":
            suggest = "metric_name"
        elif key == "timeAggregation":
            suggest = "time_aggregation"
        elif key == "metricNamespace":
            suggest = "metric_namespace"
        elif key == "skipMetricValidation":
            suggest = "skip_metric_validation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MetricCriteriaResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MetricCriteriaResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MetricCriteriaResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 criterion_type: str,
                 metric_name: str,
                 name: str,
                 operator: str,
                 threshold: float,
                 time_aggregation: str,
                 dimensions: Optional[Sequence['outputs.MetricDimensionResponse']] = None,
                 metric_namespace: Optional[str] = None,
                 skip_metric_validation: Optional[bool] = None):
        """
        Criterion to filter metrics.
        :param str criterion_type: Specifies the type of threshold criteria
               Expected value is 'StaticThresholdCriterion'.
        :param str metric_name: Name of the metric.
        :param str name: Name of the criteria.
        :param str operator: the criteria operator.
        :param float threshold: the criteria threshold value that activates the alert.
        :param str time_aggregation: the criteria time aggregation types.
        :param Sequence['MetricDimensionResponse'] dimensions: List of dimension conditions.
        :param str metric_namespace: Namespace of the metric.
        :param bool skip_metric_validation: Allows creating an alert rule on a custom metric that isn't yet emitted, by causing the metric validation to be skipped.
        """
        pulumi.set(__self__, "criterion_type", 'StaticThresholdCriterion')
        pulumi.set(__self__, "metric_name", metric_name)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "threshold", threshold)
        pulumi.set(__self__, "time_aggregation", time_aggregation)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if metric_namespace is not None:
            pulumi.set(__self__, "metric_namespace", metric_namespace)
        if skip_metric_validation is not None:
            pulumi.set(__self__, "skip_metric_validation", skip_metric_validation)

    @property
    @pulumi.getter(name="criterionType")
    def criterion_type(self) -> str:
        """
        Specifies the type of threshold criteria
        Expected value is 'StaticThresholdCriterion'.
        """
        return pulumi.get(self, "criterion_type")

    @property
    @pulumi.getter(name="metricName")
    def metric_name(self) -> str:
        """
        Name of the metric.
        """
        return pulumi.get(self, "metric_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the criteria.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operator(self) -> str:
        """
        the criteria operator.
        """
        return pulumi.get(self, "operator")

    @property
    @pulumi.getter
    def threshold(self) -> float:
        """
        the criteria threshold value that activates the alert.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter(name="timeAggregation")
    def time_aggregation(self) -> str:
        """
        the criteria time aggregation types.
        """
        return pulumi.get(self, "time_aggregation")

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.MetricDimensionResponse']]:
        """
        List of dimension conditions.
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="metricNamespace")
    def metric_namespace(self) -> Optional[str]:
        """
        Namespace of the metric.
        """
        return pulumi.get(self, "metric_namespace")

    @property
    @pulumi.getter(name="skipMetricValidation")
    def skip_metric_validation(self) -> Optional[bool]:
        """
        Allows creating an alert rule on a custom metric that isn't yet emitted, by causing the metric validation to be skipped.
        """
        return pulumi.get(self, "skip_metric_validation")


@pulumi.output_type
class MetricDimensionResponse(dict):
    """
    Specifies a metric dimension.
    """
    def __init__(__self__, *,
                 name: str,
                 operator: str,
                 values: Sequence[str]):
        """
        Specifies a metric dimension.
        :param str name: Name of the dimension.
        :param str operator: the dimension operator. Only 'Include' and 'Exclude' are supported
        :param Sequence[str] values: list of dimension values.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the dimension.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operator(self) -> str:
        """
        the dimension operator. Only 'Include' and 'Exclude' are supported
        """
        return pulumi.get(self, "operator")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        list of dimension values.
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class WebtestLocationAvailabilityCriteriaResponse(dict):
    """
    Specifies the metric alert rule criteria for a web test resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "componentId":
            suggest = "component_id"
        elif key == "failedLocationCount":
            suggest = "failed_location_count"
        elif key == "odataType":
            suggest = "odata_type"
        elif key == "webTestId":
            suggest = "web_test_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WebtestLocationAvailabilityCriteriaResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WebtestLocationAvailabilityCriteriaResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WebtestLocationAvailabilityCriteriaResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 component_id: str,
                 failed_location_count: float,
                 odata_type: str,
                 web_test_id: str):
        """
        Specifies the metric alert rule criteria for a web test resource.
        :param str component_id: The Application Insights resource Id.
        :param float failed_location_count: The number of failed locations.
        :param str odata_type: specifies the type of the alert criteria.
               Expected value is 'Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria'.
        :param str web_test_id: The Application Insights web test Id.
        """
        pulumi.set(__self__, "component_id", component_id)
        pulumi.set(__self__, "failed_location_count", failed_location_count)
        pulumi.set(__self__, "odata_type", 'Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria')
        pulumi.set(__self__, "web_test_id", web_test_id)

    @property
    @pulumi.getter(name="componentId")
    def component_id(self) -> str:
        """
        The Application Insights resource Id.
        """
        return pulumi.get(self, "component_id")

    @property
    @pulumi.getter(name="failedLocationCount")
    def failed_location_count(self) -> float:
        """
        The number of failed locations.
        """
        return pulumi.get(self, "failed_location_count")

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> str:
        """
        specifies the type of the alert criteria.
        Expected value is 'Microsoft.Azure.Monitor.WebtestLocationAvailabilityCriteria'.
        """
        return pulumi.get(self, "odata_type")

    @property
    @pulumi.getter(name="webTestId")
    def web_test_id(self) -> str:
        """
        The Application Insights web test Id.
        """
        return pulumi.get(self, "web_test_id")


