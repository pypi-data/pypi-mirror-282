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
    'GetWebAppAssessmentV2OperationResult',
    'AwaitableGetWebAppAssessmentV2OperationResult',
    'get_web_app_assessment_v2_operation',
    'get_web_app_assessment_v2_operation_output',
]

@pulumi.output_type
class GetWebAppAssessmentV2OperationResult:
    """
    Web app Assessment REST resource.
    """
    def __init__(__self__, app_svc_container_settings=None, app_svc_native_settings=None, assessment_type=None, azure_location=None, azure_offer_code=None, azure_security_offering_type=None, confidence_rating_in_percentage=None, created_timestamp=None, currency=None, discount_percentage=None, discovered_entity_light_summary=None, ea_subscription_id=None, entity_uptime=None, environment_type=None, group_type=None, id=None, name=None, percentile=None, perf_data_end_time=None, perf_data_start_time=None, prices_timestamp=None, provisioning_state=None, reserved_instance=None, scaling_factor=None, schema_version=None, sizing_criterion=None, stage=None, status=None, system_data=None, time_range=None, type=None, updated_timestamp=None):
        if app_svc_container_settings and not isinstance(app_svc_container_settings, dict):
            raise TypeError("Expected argument 'app_svc_container_settings' to be a dict")
        pulumi.set(__self__, "app_svc_container_settings", app_svc_container_settings)
        if app_svc_native_settings and not isinstance(app_svc_native_settings, dict):
            raise TypeError("Expected argument 'app_svc_native_settings' to be a dict")
        pulumi.set(__self__, "app_svc_native_settings", app_svc_native_settings)
        if assessment_type and not isinstance(assessment_type, str):
            raise TypeError("Expected argument 'assessment_type' to be a str")
        pulumi.set(__self__, "assessment_type", assessment_type)
        if azure_location and not isinstance(azure_location, str):
            raise TypeError("Expected argument 'azure_location' to be a str")
        pulumi.set(__self__, "azure_location", azure_location)
        if azure_offer_code and not isinstance(azure_offer_code, str):
            raise TypeError("Expected argument 'azure_offer_code' to be a str")
        pulumi.set(__self__, "azure_offer_code", azure_offer_code)
        if azure_security_offering_type and not isinstance(azure_security_offering_type, str):
            raise TypeError("Expected argument 'azure_security_offering_type' to be a str")
        pulumi.set(__self__, "azure_security_offering_type", azure_security_offering_type)
        if confidence_rating_in_percentage and not isinstance(confidence_rating_in_percentage, float):
            raise TypeError("Expected argument 'confidence_rating_in_percentage' to be a float")
        pulumi.set(__self__, "confidence_rating_in_percentage", confidence_rating_in_percentage)
        if created_timestamp and not isinstance(created_timestamp, str):
            raise TypeError("Expected argument 'created_timestamp' to be a str")
        pulumi.set(__self__, "created_timestamp", created_timestamp)
        if currency and not isinstance(currency, str):
            raise TypeError("Expected argument 'currency' to be a str")
        pulumi.set(__self__, "currency", currency)
        if discount_percentage and not isinstance(discount_percentage, float):
            raise TypeError("Expected argument 'discount_percentage' to be a float")
        pulumi.set(__self__, "discount_percentage", discount_percentage)
        if discovered_entity_light_summary and not isinstance(discovered_entity_light_summary, dict):
            raise TypeError("Expected argument 'discovered_entity_light_summary' to be a dict")
        pulumi.set(__self__, "discovered_entity_light_summary", discovered_entity_light_summary)
        if ea_subscription_id and not isinstance(ea_subscription_id, str):
            raise TypeError("Expected argument 'ea_subscription_id' to be a str")
        pulumi.set(__self__, "ea_subscription_id", ea_subscription_id)
        if entity_uptime and not isinstance(entity_uptime, dict):
            raise TypeError("Expected argument 'entity_uptime' to be a dict")
        pulumi.set(__self__, "entity_uptime", entity_uptime)
        if environment_type and not isinstance(environment_type, str):
            raise TypeError("Expected argument 'environment_type' to be a str")
        pulumi.set(__self__, "environment_type", environment_type)
        if group_type and not isinstance(group_type, str):
            raise TypeError("Expected argument 'group_type' to be a str")
        pulumi.set(__self__, "group_type", group_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if percentile and not isinstance(percentile, str):
            raise TypeError("Expected argument 'percentile' to be a str")
        pulumi.set(__self__, "percentile", percentile)
        if perf_data_end_time and not isinstance(perf_data_end_time, str):
            raise TypeError("Expected argument 'perf_data_end_time' to be a str")
        pulumi.set(__self__, "perf_data_end_time", perf_data_end_time)
        if perf_data_start_time and not isinstance(perf_data_start_time, str):
            raise TypeError("Expected argument 'perf_data_start_time' to be a str")
        pulumi.set(__self__, "perf_data_start_time", perf_data_start_time)
        if prices_timestamp and not isinstance(prices_timestamp, str):
            raise TypeError("Expected argument 'prices_timestamp' to be a str")
        pulumi.set(__self__, "prices_timestamp", prices_timestamp)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if reserved_instance and not isinstance(reserved_instance, str):
            raise TypeError("Expected argument 'reserved_instance' to be a str")
        pulumi.set(__self__, "reserved_instance", reserved_instance)
        if scaling_factor and not isinstance(scaling_factor, float):
            raise TypeError("Expected argument 'scaling_factor' to be a float")
        pulumi.set(__self__, "scaling_factor", scaling_factor)
        if schema_version and not isinstance(schema_version, str):
            raise TypeError("Expected argument 'schema_version' to be a str")
        pulumi.set(__self__, "schema_version", schema_version)
        if sizing_criterion and not isinstance(sizing_criterion, str):
            raise TypeError("Expected argument 'sizing_criterion' to be a str")
        pulumi.set(__self__, "sizing_criterion", sizing_criterion)
        if stage and not isinstance(stage, str):
            raise TypeError("Expected argument 'stage' to be a str")
        pulumi.set(__self__, "stage", stage)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if time_range and not isinstance(time_range, str):
            raise TypeError("Expected argument 'time_range' to be a str")
        pulumi.set(__self__, "time_range", time_range)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_timestamp and not isinstance(updated_timestamp, str):
            raise TypeError("Expected argument 'updated_timestamp' to be a str")
        pulumi.set(__self__, "updated_timestamp", updated_timestamp)

    @property
    @pulumi.getter(name="appSvcContainerSettings")
    def app_svc_container_settings(self) -> Optional['outputs.AppSvcContainerSettingsResponse']:
        """
        Gets or sets user configurable app service container database settings.
        """
        return pulumi.get(self, "app_svc_container_settings")

    @property
    @pulumi.getter(name="appSvcNativeSettings")
    def app_svc_native_settings(self) -> Optional['outputs.AppSvcNativeSettingsResponse']:
        """
        Gets or sets user configurable app service native settings.
        """
        return pulumi.get(self, "app_svc_native_settings")

    @property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> Optional[str]:
        """
        Assessment type of the assessment.
        """
        return pulumi.get(self, "assessment_type")

    @property
    @pulumi.getter(name="azureLocation")
    def azure_location(self) -> Optional[str]:
        """
        Azure Location or Azure region where to which the machines will be migrated.
        """
        return pulumi.get(self, "azure_location")

    @property
    @pulumi.getter(name="azureOfferCode")
    def azure_offer_code(self) -> Optional[str]:
        """
        Azure Offer Code.
        """
        return pulumi.get(self, "azure_offer_code")

    @property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(self) -> Optional[str]:
        """
        Gets or sets a value indicating azure security offering type.
        """
        return pulumi.get(self, "azure_security_offering_type")

    @property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> Optional[float]:
        """
        Confidence Rating in Percentage.
        """
        return pulumi.get(self, "confidence_rating_in_percentage")

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> str:
        """
        Date and Time when assessment was created.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter
    def currency(self) -> Optional[str]:
        """
        Currency in which prices should be reported.
        """
        return pulumi.get(self, "currency")

    @property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[float]:
        """
        Custom discount percentage.
        """
        return pulumi.get(self, "discount_percentage")

    @property
    @pulumi.getter(name="discoveredEntityLightSummary")
    def discovered_entity_light_summary(self) -> Optional['outputs.DiscoveredEntityLightSummaryResponse']:
        """
        Gets or sets user configurable discovered entity settings.
        """
        return pulumi.get(self, "discovered_entity_light_summary")

    @property
    @pulumi.getter(name="eaSubscriptionId")
    def ea_subscription_id(self) -> Optional[str]:
        """
        Gets or sets the Enterprise agreement subscription id.
        """
        return pulumi.get(self, "ea_subscription_id")

    @property
    @pulumi.getter(name="entityUptime")
    def entity_uptime(self) -> Optional['outputs.EntityUptimeResponse']:
        """
        Gets or sets the duration for which the entity (Web app, VMs) are up in the
        on-premises environment.
        """
        return pulumi.get(self, "entity_uptime")

    @property
    @pulumi.getter(name="environmentType")
    def environment_type(self) -> Optional[str]:
        """
        Gets or sets user configurable setting to display the environment type.
        """
        return pulumi.get(self, "environment_type")

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> Optional[str]:
        """
        Gets the group type for the assessment.
        """
        return pulumi.get(self, "group_type")

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
    @pulumi.getter
    def percentile(self) -> Optional[str]:
        """
        Percentile of the utilization data values to be considered while assessing
        machines.
        """
        return pulumi.get(self, "percentile")

    @property
    @pulumi.getter(name="perfDataEndTime")
    def perf_data_end_time(self) -> Optional[str]:
        """
        Gets or sets the end time to consider performance data for assessment.
        """
        return pulumi.get(self, "perf_data_end_time")

    @property
    @pulumi.getter(name="perfDataStartTime")
    def perf_data_start_time(self) -> Optional[str]:
        """
        Gets or sets the start time to consider performance data for assessment.
        """
        return pulumi.get(self, "perf_data_start_time")

    @property
    @pulumi.getter(name="pricesTimestamp")
    def prices_timestamp(self) -> str:
        """
        Last time when rates were queried.
        """
        return pulumi.get(self, "prices_timestamp")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="reservedInstance")
    def reserved_instance(self) -> Optional[str]:
        """
        Reserved instance.
        """
        return pulumi.get(self, "reserved_instance")

    @property
    @pulumi.getter(name="scalingFactor")
    def scaling_factor(self) -> Optional[float]:
        """
        Percentage of buffer that user wants on performance metrics when recommending
        Azure sizes.
        """
        return pulumi.get(self, "scaling_factor")

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> str:
        """
        Schema version.
        """
        return pulumi.get(self, "schema_version")

    @property
    @pulumi.getter(name="sizingCriterion")
    def sizing_criterion(self) -> Optional[str]:
        """
        Assessment sizing criterion.
        """
        return pulumi.get(self, "sizing_criterion")

    @property
    @pulumi.getter
    def stage(self) -> str:
        """
        User configurable setting to display the Stage of Assessment.
        """
        return pulumi.get(self, "stage")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Whether assessment is in valid state and all machines have been assessed.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="timeRange")
    def time_range(self) -> Optional[str]:
        """
        Time Range for which the historic utilization data should be considered for
        assessment.
        """
        return pulumi.get(self, "time_range")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> str:
        """
        Date and Time when assessment was last updated.
        """
        return pulumi.get(self, "updated_timestamp")


class AwaitableGetWebAppAssessmentV2OperationResult(GetWebAppAssessmentV2OperationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAppAssessmentV2OperationResult(
            app_svc_container_settings=self.app_svc_container_settings,
            app_svc_native_settings=self.app_svc_native_settings,
            assessment_type=self.assessment_type,
            azure_location=self.azure_location,
            azure_offer_code=self.azure_offer_code,
            azure_security_offering_type=self.azure_security_offering_type,
            confidence_rating_in_percentage=self.confidence_rating_in_percentage,
            created_timestamp=self.created_timestamp,
            currency=self.currency,
            discount_percentage=self.discount_percentage,
            discovered_entity_light_summary=self.discovered_entity_light_summary,
            ea_subscription_id=self.ea_subscription_id,
            entity_uptime=self.entity_uptime,
            environment_type=self.environment_type,
            group_type=self.group_type,
            id=self.id,
            name=self.name,
            percentile=self.percentile,
            perf_data_end_time=self.perf_data_end_time,
            perf_data_start_time=self.perf_data_start_time,
            prices_timestamp=self.prices_timestamp,
            provisioning_state=self.provisioning_state,
            reserved_instance=self.reserved_instance,
            scaling_factor=self.scaling_factor,
            schema_version=self.schema_version,
            sizing_criterion=self.sizing_criterion,
            stage=self.stage,
            status=self.status,
            system_data=self.system_data,
            time_range=self.time_range,
            type=self.type,
            updated_timestamp=self.updated_timestamp)


def get_web_app_assessment_v2_operation(assessment_name: Optional[str] = None,
                                        group_name: Optional[str] = None,
                                        project_name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAppAssessmentV2OperationResult:
    """
    Get a WebAppAssessmentV2


    :param str assessment_name: Web app Assessment arm name.
    :param str group_name: Group ARM name
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['assessmentName'] = assessment_name
    __args__['groupName'] = group_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate/v20230401preview:getWebAppAssessmentV2Operation', __args__, opts=opts, typ=GetWebAppAssessmentV2OperationResult).value

    return AwaitableGetWebAppAssessmentV2OperationResult(
        app_svc_container_settings=pulumi.get(__ret__, 'app_svc_container_settings'),
        app_svc_native_settings=pulumi.get(__ret__, 'app_svc_native_settings'),
        assessment_type=pulumi.get(__ret__, 'assessment_type'),
        azure_location=pulumi.get(__ret__, 'azure_location'),
        azure_offer_code=pulumi.get(__ret__, 'azure_offer_code'),
        azure_security_offering_type=pulumi.get(__ret__, 'azure_security_offering_type'),
        confidence_rating_in_percentage=pulumi.get(__ret__, 'confidence_rating_in_percentage'),
        created_timestamp=pulumi.get(__ret__, 'created_timestamp'),
        currency=pulumi.get(__ret__, 'currency'),
        discount_percentage=pulumi.get(__ret__, 'discount_percentage'),
        discovered_entity_light_summary=pulumi.get(__ret__, 'discovered_entity_light_summary'),
        ea_subscription_id=pulumi.get(__ret__, 'ea_subscription_id'),
        entity_uptime=pulumi.get(__ret__, 'entity_uptime'),
        environment_type=pulumi.get(__ret__, 'environment_type'),
        group_type=pulumi.get(__ret__, 'group_type'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        percentile=pulumi.get(__ret__, 'percentile'),
        perf_data_end_time=pulumi.get(__ret__, 'perf_data_end_time'),
        perf_data_start_time=pulumi.get(__ret__, 'perf_data_start_time'),
        prices_timestamp=pulumi.get(__ret__, 'prices_timestamp'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        reserved_instance=pulumi.get(__ret__, 'reserved_instance'),
        scaling_factor=pulumi.get(__ret__, 'scaling_factor'),
        schema_version=pulumi.get(__ret__, 'schema_version'),
        sizing_criterion=pulumi.get(__ret__, 'sizing_criterion'),
        stage=pulumi.get(__ret__, 'stage'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time_range=pulumi.get(__ret__, 'time_range'),
        type=pulumi.get(__ret__, 'type'),
        updated_timestamp=pulumi.get(__ret__, 'updated_timestamp'))


@_utilities.lift_output_func(get_web_app_assessment_v2_operation)
def get_web_app_assessment_v2_operation_output(assessment_name: Optional[pulumi.Input[str]] = None,
                                               group_name: Optional[pulumi.Input[str]] = None,
                                               project_name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAppAssessmentV2OperationResult]:
    """
    Get a WebAppAssessmentV2


    :param str assessment_name: Web app Assessment arm name.
    :param str group_name: Group ARM name
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
