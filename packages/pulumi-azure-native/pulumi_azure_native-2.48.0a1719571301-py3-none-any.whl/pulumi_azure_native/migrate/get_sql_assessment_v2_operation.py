# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetSqlAssessmentV2OperationResult',
    'AwaitableGetSqlAssessmentV2OperationResult',
    'get_sql_assessment_v2_operation',
    'get_sql_assessment_v2_operation_output',
]

@pulumi.output_type
class GetSqlAssessmentV2OperationResult:
    """
    SQL Assessment REST resource.
    """
    def __init__(__self__, assessment_type=None, async_commit_mode_intent=None, azure_location=None, azure_offer_code=None, azure_offer_code_for_vm=None, azure_security_offering_type=None, azure_sql_database_settings=None, azure_sql_managed_instance_settings=None, azure_sql_vm_settings=None, confidence_rating_in_percentage=None, created_timestamp=None, currency=None, disaster_recovery_location=None, discount_percentage=None, ea_subscription_id=None, enable_hadr_assessment=None, entity_uptime=None, environment_type=None, group_type=None, id=None, is_internet_access_available=None, multi_subnet_intent=None, name=None, optimization_logic=None, os_license=None, percentile=None, perf_data_end_time=None, perf_data_start_time=None, prices_timestamp=None, provisioning_state=None, reserved_instance=None, reserved_instance_for_vm=None, scaling_factor=None, schema_version=None, sizing_criterion=None, sql_server_license=None, stage=None, status=None, system_data=None, time_range=None, type=None, updated_timestamp=None):
        if assessment_type and not isinstance(assessment_type, str):
            raise TypeError("Expected argument 'assessment_type' to be a str")
        pulumi.set(__self__, "assessment_type", assessment_type)
        if async_commit_mode_intent and not isinstance(async_commit_mode_intent, str):
            raise TypeError("Expected argument 'async_commit_mode_intent' to be a str")
        pulumi.set(__self__, "async_commit_mode_intent", async_commit_mode_intent)
        if azure_location and not isinstance(azure_location, str):
            raise TypeError("Expected argument 'azure_location' to be a str")
        pulumi.set(__self__, "azure_location", azure_location)
        if azure_offer_code and not isinstance(azure_offer_code, str):
            raise TypeError("Expected argument 'azure_offer_code' to be a str")
        pulumi.set(__self__, "azure_offer_code", azure_offer_code)
        if azure_offer_code_for_vm and not isinstance(azure_offer_code_for_vm, str):
            raise TypeError("Expected argument 'azure_offer_code_for_vm' to be a str")
        pulumi.set(__self__, "azure_offer_code_for_vm", azure_offer_code_for_vm)
        if azure_security_offering_type and not isinstance(azure_security_offering_type, str):
            raise TypeError("Expected argument 'azure_security_offering_type' to be a str")
        pulumi.set(__self__, "azure_security_offering_type", azure_security_offering_type)
        if azure_sql_database_settings and not isinstance(azure_sql_database_settings, dict):
            raise TypeError("Expected argument 'azure_sql_database_settings' to be a dict")
        pulumi.set(__self__, "azure_sql_database_settings", azure_sql_database_settings)
        if azure_sql_managed_instance_settings and not isinstance(azure_sql_managed_instance_settings, dict):
            raise TypeError("Expected argument 'azure_sql_managed_instance_settings' to be a dict")
        pulumi.set(__self__, "azure_sql_managed_instance_settings", azure_sql_managed_instance_settings)
        if azure_sql_vm_settings and not isinstance(azure_sql_vm_settings, dict):
            raise TypeError("Expected argument 'azure_sql_vm_settings' to be a dict")
        pulumi.set(__self__, "azure_sql_vm_settings", azure_sql_vm_settings)
        if confidence_rating_in_percentage and not isinstance(confidence_rating_in_percentage, float):
            raise TypeError("Expected argument 'confidence_rating_in_percentage' to be a float")
        pulumi.set(__self__, "confidence_rating_in_percentage", confidence_rating_in_percentage)
        if created_timestamp and not isinstance(created_timestamp, str):
            raise TypeError("Expected argument 'created_timestamp' to be a str")
        pulumi.set(__self__, "created_timestamp", created_timestamp)
        if currency and not isinstance(currency, str):
            raise TypeError("Expected argument 'currency' to be a str")
        pulumi.set(__self__, "currency", currency)
        if disaster_recovery_location and not isinstance(disaster_recovery_location, str):
            raise TypeError("Expected argument 'disaster_recovery_location' to be a str")
        pulumi.set(__self__, "disaster_recovery_location", disaster_recovery_location)
        if discount_percentage and not isinstance(discount_percentage, float):
            raise TypeError("Expected argument 'discount_percentage' to be a float")
        pulumi.set(__self__, "discount_percentage", discount_percentage)
        if ea_subscription_id and not isinstance(ea_subscription_id, str):
            raise TypeError("Expected argument 'ea_subscription_id' to be a str")
        pulumi.set(__self__, "ea_subscription_id", ea_subscription_id)
        if enable_hadr_assessment and not isinstance(enable_hadr_assessment, bool):
            raise TypeError("Expected argument 'enable_hadr_assessment' to be a bool")
        pulumi.set(__self__, "enable_hadr_assessment", enable_hadr_assessment)
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
        if is_internet_access_available and not isinstance(is_internet_access_available, bool):
            raise TypeError("Expected argument 'is_internet_access_available' to be a bool")
        pulumi.set(__self__, "is_internet_access_available", is_internet_access_available)
        if multi_subnet_intent and not isinstance(multi_subnet_intent, str):
            raise TypeError("Expected argument 'multi_subnet_intent' to be a str")
        pulumi.set(__self__, "multi_subnet_intent", multi_subnet_intent)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if optimization_logic and not isinstance(optimization_logic, str):
            raise TypeError("Expected argument 'optimization_logic' to be a str")
        pulumi.set(__self__, "optimization_logic", optimization_logic)
        if os_license and not isinstance(os_license, str):
            raise TypeError("Expected argument 'os_license' to be a str")
        pulumi.set(__self__, "os_license", os_license)
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
        if reserved_instance_for_vm and not isinstance(reserved_instance_for_vm, str):
            raise TypeError("Expected argument 'reserved_instance_for_vm' to be a str")
        pulumi.set(__self__, "reserved_instance_for_vm", reserved_instance_for_vm)
        if scaling_factor and not isinstance(scaling_factor, float):
            raise TypeError("Expected argument 'scaling_factor' to be a float")
        pulumi.set(__self__, "scaling_factor", scaling_factor)
        if schema_version and not isinstance(schema_version, str):
            raise TypeError("Expected argument 'schema_version' to be a str")
        pulumi.set(__self__, "schema_version", schema_version)
        if sizing_criterion and not isinstance(sizing_criterion, str):
            raise TypeError("Expected argument 'sizing_criterion' to be a str")
        pulumi.set(__self__, "sizing_criterion", sizing_criterion)
        if sql_server_license and not isinstance(sql_server_license, str):
            raise TypeError("Expected argument 'sql_server_license' to be a str")
        pulumi.set(__self__, "sql_server_license", sql_server_license)
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
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> Optional[str]:
        """
        Assessment type of the assessment.
        """
        return pulumi.get(self, "assessment_type")

    @property
    @pulumi.getter(name="asyncCommitModeIntent")
    def async_commit_mode_intent(self) -> Optional[str]:
        """
        Gets or sets user preference indicating intent of async commit mode.
        """
        return pulumi.get(self, "async_commit_mode_intent")

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
    @pulumi.getter(name="azureOfferCodeForVm")
    def azure_offer_code_for_vm(self) -> Optional[str]:
        """
        Gets or sets Azure Offer Code for VM.
        """
        return pulumi.get(self, "azure_offer_code_for_vm")

    @property
    @pulumi.getter(name="azureSecurityOfferingType")
    def azure_security_offering_type(self) -> Optional[str]:
        """
        Gets or sets a value indicating azure security offering type.
        """
        return pulumi.get(self, "azure_security_offering_type")

    @property
    @pulumi.getter(name="azureSqlDatabaseSettings")
    def azure_sql_database_settings(self) -> Optional['outputs.SqlDbSettingsResponse']:
        """
        Gets or sets user configurable SQL database settings.
        """
        return pulumi.get(self, "azure_sql_database_settings")

    @property
    @pulumi.getter(name="azureSqlManagedInstanceSettings")
    def azure_sql_managed_instance_settings(self) -> Optional['outputs.SqlMiSettingsResponse']:
        """
        Gets or sets user configurable SQL managed instance settings.
        """
        return pulumi.get(self, "azure_sql_managed_instance_settings")

    @property
    @pulumi.getter(name="azureSqlVmSettings")
    def azure_sql_vm_settings(self) -> Optional['outputs.SqlVmSettingsResponse']:
        """
        Gets or sets user configurable SQL VM settings.
        """
        return pulumi.get(self, "azure_sql_vm_settings")

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
    @pulumi.getter(name="disasterRecoveryLocation")
    def disaster_recovery_location(self) -> Optional[str]:
        """
        Gets or sets the Azure Location or Azure region where to which the machines
        will be migrated.
        """
        return pulumi.get(self, "disaster_recovery_location")

    @property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[float]:
        """
        Custom discount percentage.
        """
        return pulumi.get(self, "discount_percentage")

    @property
    @pulumi.getter(name="eaSubscriptionId")
    def ea_subscription_id(self) -> Optional[str]:
        """
        Gets or sets the Enterprise agreement subscription id.
        """
        return pulumi.get(self, "ea_subscription_id")

    @property
    @pulumi.getter(name="enableHadrAssessment")
    def enable_hadr_assessment(self) -> Optional[bool]:
        """
        Gets or sets a value indicating whether HADR assessments needs to be created.
        """
        return pulumi.get(self, "enable_hadr_assessment")

    @property
    @pulumi.getter(name="entityUptime")
    def entity_uptime(self) -> Optional['outputs.EntityUptimeResponse']:
        """
        Gets or sets the duration for which the entity (SQL, VMs) are up in the
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
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isInternetAccessAvailable")
    def is_internet_access_available(self) -> Optional[bool]:
        """
        Gets or sets a value indicating whether internet access is available.
        """
        return pulumi.get(self, "is_internet_access_available")

    @property
    @pulumi.getter(name="multiSubnetIntent")
    def multi_subnet_intent(self) -> Optional[str]:
        """
        Gets or sets user preference indicating intent of multi-subnet configuration.
        """
        return pulumi.get(self, "multi_subnet_intent")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="optimizationLogic")
    def optimization_logic(self) -> Optional[str]:
        """
        Gets or sets SQL optimization logic.
        """
        return pulumi.get(self, "optimization_logic")

    @property
    @pulumi.getter(name="osLicense")
    def os_license(self) -> Optional[str]:
        """
        Gets or sets user configurable setting to display the azure hybrid use benefit.
        """
        return pulumi.get(self, "os_license")

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
    def provisioning_state(self) -> Optional[str]:
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
    @pulumi.getter(name="reservedInstanceForVm")
    def reserved_instance_for_vm(self) -> Optional[str]:
        """
        Gets or sets azure reserved instance for VM.
        """
        return pulumi.get(self, "reserved_instance_for_vm")

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
    @pulumi.getter(name="sqlServerLicense")
    def sql_server_license(self) -> Optional[str]:
        """
        SQL server license.
        """
        return pulumi.get(self, "sql_server_license")

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


class AwaitableGetSqlAssessmentV2OperationResult(GetSqlAssessmentV2OperationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlAssessmentV2OperationResult(
            assessment_type=self.assessment_type,
            async_commit_mode_intent=self.async_commit_mode_intent,
            azure_location=self.azure_location,
            azure_offer_code=self.azure_offer_code,
            azure_offer_code_for_vm=self.azure_offer_code_for_vm,
            azure_security_offering_type=self.azure_security_offering_type,
            azure_sql_database_settings=self.azure_sql_database_settings,
            azure_sql_managed_instance_settings=self.azure_sql_managed_instance_settings,
            azure_sql_vm_settings=self.azure_sql_vm_settings,
            confidence_rating_in_percentage=self.confidence_rating_in_percentage,
            created_timestamp=self.created_timestamp,
            currency=self.currency,
            disaster_recovery_location=self.disaster_recovery_location,
            discount_percentage=self.discount_percentage,
            ea_subscription_id=self.ea_subscription_id,
            enable_hadr_assessment=self.enable_hadr_assessment,
            entity_uptime=self.entity_uptime,
            environment_type=self.environment_type,
            group_type=self.group_type,
            id=self.id,
            is_internet_access_available=self.is_internet_access_available,
            multi_subnet_intent=self.multi_subnet_intent,
            name=self.name,
            optimization_logic=self.optimization_logic,
            os_license=self.os_license,
            percentile=self.percentile,
            perf_data_end_time=self.perf_data_end_time,
            perf_data_start_time=self.perf_data_start_time,
            prices_timestamp=self.prices_timestamp,
            provisioning_state=self.provisioning_state,
            reserved_instance=self.reserved_instance,
            reserved_instance_for_vm=self.reserved_instance_for_vm,
            scaling_factor=self.scaling_factor,
            schema_version=self.schema_version,
            sizing_criterion=self.sizing_criterion,
            sql_server_license=self.sql_server_license,
            stage=self.stage,
            status=self.status,
            system_data=self.system_data,
            time_range=self.time_range,
            type=self.type,
            updated_timestamp=self.updated_timestamp)


def get_sql_assessment_v2_operation(assessment_name: Optional[str] = None,
                                    group_name: Optional[str] = None,
                                    project_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlAssessmentV2OperationResult:
    """
    Get a SqlAssessmentV2
    Azure REST API version: 2023-03-15.

    Other available API versions: 2023-04-01-preview.


    :param str assessment_name: SQL Assessment arm name.
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
    __ret__ = pulumi.runtime.invoke('azure-native:migrate:getSqlAssessmentV2Operation', __args__, opts=opts, typ=GetSqlAssessmentV2OperationResult).value

    return AwaitableGetSqlAssessmentV2OperationResult(
        assessment_type=pulumi.get(__ret__, 'assessment_type'),
        async_commit_mode_intent=pulumi.get(__ret__, 'async_commit_mode_intent'),
        azure_location=pulumi.get(__ret__, 'azure_location'),
        azure_offer_code=pulumi.get(__ret__, 'azure_offer_code'),
        azure_offer_code_for_vm=pulumi.get(__ret__, 'azure_offer_code_for_vm'),
        azure_security_offering_type=pulumi.get(__ret__, 'azure_security_offering_type'),
        azure_sql_database_settings=pulumi.get(__ret__, 'azure_sql_database_settings'),
        azure_sql_managed_instance_settings=pulumi.get(__ret__, 'azure_sql_managed_instance_settings'),
        azure_sql_vm_settings=pulumi.get(__ret__, 'azure_sql_vm_settings'),
        confidence_rating_in_percentage=pulumi.get(__ret__, 'confidence_rating_in_percentage'),
        created_timestamp=pulumi.get(__ret__, 'created_timestamp'),
        currency=pulumi.get(__ret__, 'currency'),
        disaster_recovery_location=pulumi.get(__ret__, 'disaster_recovery_location'),
        discount_percentage=pulumi.get(__ret__, 'discount_percentage'),
        ea_subscription_id=pulumi.get(__ret__, 'ea_subscription_id'),
        enable_hadr_assessment=pulumi.get(__ret__, 'enable_hadr_assessment'),
        entity_uptime=pulumi.get(__ret__, 'entity_uptime'),
        environment_type=pulumi.get(__ret__, 'environment_type'),
        group_type=pulumi.get(__ret__, 'group_type'),
        id=pulumi.get(__ret__, 'id'),
        is_internet_access_available=pulumi.get(__ret__, 'is_internet_access_available'),
        multi_subnet_intent=pulumi.get(__ret__, 'multi_subnet_intent'),
        name=pulumi.get(__ret__, 'name'),
        optimization_logic=pulumi.get(__ret__, 'optimization_logic'),
        os_license=pulumi.get(__ret__, 'os_license'),
        percentile=pulumi.get(__ret__, 'percentile'),
        perf_data_end_time=pulumi.get(__ret__, 'perf_data_end_time'),
        perf_data_start_time=pulumi.get(__ret__, 'perf_data_start_time'),
        prices_timestamp=pulumi.get(__ret__, 'prices_timestamp'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        reserved_instance=pulumi.get(__ret__, 'reserved_instance'),
        reserved_instance_for_vm=pulumi.get(__ret__, 'reserved_instance_for_vm'),
        scaling_factor=pulumi.get(__ret__, 'scaling_factor'),
        schema_version=pulumi.get(__ret__, 'schema_version'),
        sizing_criterion=pulumi.get(__ret__, 'sizing_criterion'),
        sql_server_license=pulumi.get(__ret__, 'sql_server_license'),
        stage=pulumi.get(__ret__, 'stage'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time_range=pulumi.get(__ret__, 'time_range'),
        type=pulumi.get(__ret__, 'type'),
        updated_timestamp=pulumi.get(__ret__, 'updated_timestamp'))


@_utilities.lift_output_func(get_sql_assessment_v2_operation)
def get_sql_assessment_v2_operation_output(assessment_name: Optional[pulumi.Input[str]] = None,
                                           group_name: Optional[pulumi.Input[str]] = None,
                                           project_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlAssessmentV2OperationResult]:
    """
    Get a SqlAssessmentV2
    Azure REST API version: 2023-03-15.

    Other available API versions: 2023-04-01-preview.


    :param str assessment_name: SQL Assessment arm name.
    :param str group_name: Group ARM name
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
