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
    'GetAvsAssessmentsOperationResult',
    'AwaitableGetAvsAssessmentsOperationResult',
    'get_avs_assessments_operation',
    'get_avs_assessments_operation_output',
]

@pulumi.output_type
class GetAvsAssessmentsOperationResult:
    """
    AVS assessment resource.
    """
    def __init__(__self__, assessment_error_summary=None, assessment_type=None, azure_location=None, azure_offer_code=None, confidence_rating_in_percentage=None, cpu_utilization=None, created_timestamp=None, currency=None, dedupe_compression=None, discount_percentage=None, failures_to_tolerate_and_raid_level=None, group_type=None, id=None, is_stretch_cluster_enabled=None, limiting_factor=None, mem_overcommit=None, name=None, node_type=None, number_of_machines=None, number_of_nodes=None, percentile=None, perf_data_end_time=None, perf_data_start_time=None, prices_timestamp=None, provisioning_state=None, ram_utilization=None, reserved_instance=None, scaling_factor=None, schema_version=None, sizing_criterion=None, stage=None, status=None, storage_utilization=None, suitability=None, suitability_explanation=None, suitability_summary=None, system_data=None, time_range=None, total_cpu_cores=None, total_monthly_cost=None, total_ram_in_gb=None, total_storage_in_gb=None, type=None, updated_timestamp=None, vcpu_oversubscription=None):
        if assessment_error_summary and not isinstance(assessment_error_summary, dict):
            raise TypeError("Expected argument 'assessment_error_summary' to be a dict")
        pulumi.set(__self__, "assessment_error_summary", assessment_error_summary)
        if assessment_type and not isinstance(assessment_type, str):
            raise TypeError("Expected argument 'assessment_type' to be a str")
        pulumi.set(__self__, "assessment_type", assessment_type)
        if azure_location and not isinstance(azure_location, str):
            raise TypeError("Expected argument 'azure_location' to be a str")
        pulumi.set(__self__, "azure_location", azure_location)
        if azure_offer_code and not isinstance(azure_offer_code, str):
            raise TypeError("Expected argument 'azure_offer_code' to be a str")
        pulumi.set(__self__, "azure_offer_code", azure_offer_code)
        if confidence_rating_in_percentage and not isinstance(confidence_rating_in_percentage, float):
            raise TypeError("Expected argument 'confidence_rating_in_percentage' to be a float")
        pulumi.set(__self__, "confidence_rating_in_percentage", confidence_rating_in_percentage)
        if cpu_utilization and not isinstance(cpu_utilization, float):
            raise TypeError("Expected argument 'cpu_utilization' to be a float")
        pulumi.set(__self__, "cpu_utilization", cpu_utilization)
        if created_timestamp and not isinstance(created_timestamp, str):
            raise TypeError("Expected argument 'created_timestamp' to be a str")
        pulumi.set(__self__, "created_timestamp", created_timestamp)
        if currency and not isinstance(currency, str):
            raise TypeError("Expected argument 'currency' to be a str")
        pulumi.set(__self__, "currency", currency)
        if dedupe_compression and not isinstance(dedupe_compression, float):
            raise TypeError("Expected argument 'dedupe_compression' to be a float")
        pulumi.set(__self__, "dedupe_compression", dedupe_compression)
        if discount_percentage and not isinstance(discount_percentage, float):
            raise TypeError("Expected argument 'discount_percentage' to be a float")
        pulumi.set(__self__, "discount_percentage", discount_percentage)
        if failures_to_tolerate_and_raid_level and not isinstance(failures_to_tolerate_and_raid_level, str):
            raise TypeError("Expected argument 'failures_to_tolerate_and_raid_level' to be a str")
        pulumi.set(__self__, "failures_to_tolerate_and_raid_level", failures_to_tolerate_and_raid_level)
        if group_type and not isinstance(group_type, str):
            raise TypeError("Expected argument 'group_type' to be a str")
        pulumi.set(__self__, "group_type", group_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_stretch_cluster_enabled and not isinstance(is_stretch_cluster_enabled, bool):
            raise TypeError("Expected argument 'is_stretch_cluster_enabled' to be a bool")
        pulumi.set(__self__, "is_stretch_cluster_enabled", is_stretch_cluster_enabled)
        if limiting_factor and not isinstance(limiting_factor, str):
            raise TypeError("Expected argument 'limiting_factor' to be a str")
        pulumi.set(__self__, "limiting_factor", limiting_factor)
        if mem_overcommit and not isinstance(mem_overcommit, float):
            raise TypeError("Expected argument 'mem_overcommit' to be a float")
        pulumi.set(__self__, "mem_overcommit", mem_overcommit)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_type and not isinstance(node_type, str):
            raise TypeError("Expected argument 'node_type' to be a str")
        pulumi.set(__self__, "node_type", node_type)
        if number_of_machines and not isinstance(number_of_machines, int):
            raise TypeError("Expected argument 'number_of_machines' to be a int")
        pulumi.set(__self__, "number_of_machines", number_of_machines)
        if number_of_nodes and not isinstance(number_of_nodes, int):
            raise TypeError("Expected argument 'number_of_nodes' to be a int")
        pulumi.set(__self__, "number_of_nodes", number_of_nodes)
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
        if ram_utilization and not isinstance(ram_utilization, float):
            raise TypeError("Expected argument 'ram_utilization' to be a float")
        pulumi.set(__self__, "ram_utilization", ram_utilization)
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
        if storage_utilization and not isinstance(storage_utilization, float):
            raise TypeError("Expected argument 'storage_utilization' to be a float")
        pulumi.set(__self__, "storage_utilization", storage_utilization)
        if suitability and not isinstance(suitability, str):
            raise TypeError("Expected argument 'suitability' to be a str")
        pulumi.set(__self__, "suitability", suitability)
        if suitability_explanation and not isinstance(suitability_explanation, str):
            raise TypeError("Expected argument 'suitability_explanation' to be a str")
        pulumi.set(__self__, "suitability_explanation", suitability_explanation)
        if suitability_summary and not isinstance(suitability_summary, dict):
            raise TypeError("Expected argument 'suitability_summary' to be a dict")
        pulumi.set(__self__, "suitability_summary", suitability_summary)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if time_range and not isinstance(time_range, str):
            raise TypeError("Expected argument 'time_range' to be a str")
        pulumi.set(__self__, "time_range", time_range)
        if total_cpu_cores and not isinstance(total_cpu_cores, float):
            raise TypeError("Expected argument 'total_cpu_cores' to be a float")
        pulumi.set(__self__, "total_cpu_cores", total_cpu_cores)
        if total_monthly_cost and not isinstance(total_monthly_cost, float):
            raise TypeError("Expected argument 'total_monthly_cost' to be a float")
        pulumi.set(__self__, "total_monthly_cost", total_monthly_cost)
        if total_ram_in_gb and not isinstance(total_ram_in_gb, float):
            raise TypeError("Expected argument 'total_ram_in_gb' to be a float")
        pulumi.set(__self__, "total_ram_in_gb", total_ram_in_gb)
        if total_storage_in_gb and not isinstance(total_storage_in_gb, float):
            raise TypeError("Expected argument 'total_storage_in_gb' to be a float")
        pulumi.set(__self__, "total_storage_in_gb", total_storage_in_gb)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_timestamp and not isinstance(updated_timestamp, str):
            raise TypeError("Expected argument 'updated_timestamp' to be a str")
        pulumi.set(__self__, "updated_timestamp", updated_timestamp)
        if vcpu_oversubscription and not isinstance(vcpu_oversubscription, float):
            raise TypeError("Expected argument 'vcpu_oversubscription' to be a float")
        pulumi.set(__self__, "vcpu_oversubscription", vcpu_oversubscription)

    @property
    @pulumi.getter(name="assessmentErrorSummary")
    def assessment_error_summary(self) -> Mapping[str, int]:
        """
        Gets the assessment error summary.
                    This is the number of machines
        affected by each type of error in this assessment.
        """
        return pulumi.get(self, "assessment_error_summary")

    @property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> str:
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
        Azure Offer code according to which cost estimation is done.
        """
        return pulumi.get(self, "azure_offer_code")

    @property
    @pulumi.getter(name="confidenceRatingInPercentage")
    def confidence_rating_in_percentage(self) -> float:
        """
        Confidence Rating in Percentage.
        """
        return pulumi.get(self, "confidence_rating_in_percentage")

    @property
    @pulumi.getter(name="cpuUtilization")
    def cpu_utilization(self) -> float:
        """
        Predicted CPU utilization.
        """
        return pulumi.get(self, "cpu_utilization")

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
    @pulumi.getter(name="dedupeCompression")
    def dedupe_compression(self) -> Optional[float]:
        """
        De-duplication compression.
        """
        return pulumi.get(self, "dedupe_compression")

    @property
    @pulumi.getter(name="discountPercentage")
    def discount_percentage(self) -> Optional[float]:
        """
        Custom discount percentage.
        """
        return pulumi.get(self, "discount_percentage")

    @property
    @pulumi.getter(name="failuresToTolerateAndRaidLevel")
    def failures_to_tolerate_and_raid_level(self) -> Optional[str]:
        """
        Failures to tolerate and RAID level in a common property.
        """
        return pulumi.get(self, "failures_to_tolerate_and_raid_level")

    @property
    @pulumi.getter(name="groupType")
    def group_type(self) -> str:
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
    @pulumi.getter(name="isStretchClusterEnabled")
    def is_stretch_cluster_enabled(self) -> Optional[bool]:
        """
        Is Stretch Cluster Enabled.
        """
        return pulumi.get(self, "is_stretch_cluster_enabled")

    @property
    @pulumi.getter(name="limitingFactor")
    def limiting_factor(self) -> str:
        """
        Limiting factor.
        """
        return pulumi.get(self, "limiting_factor")

    @property
    @pulumi.getter(name="memOvercommit")
    def mem_overcommit(self) -> Optional[float]:
        """
        Memory overcommit.
        """
        return pulumi.get(self, "mem_overcommit")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeType")
    def node_type(self) -> Optional[str]:
        """
        AVS node type.
        """
        return pulumi.get(self, "node_type")

    @property
    @pulumi.getter(name="numberOfMachines")
    def number_of_machines(self) -> int:
        """
        Number of machines part of the assessment.
        """
        return pulumi.get(self, "number_of_machines")

    @property
    @pulumi.getter(name="numberOfNodes")
    def number_of_nodes(self) -> int:
        """
        Recommended number of nodes.
        """
        return pulumi.get(self, "number_of_nodes")

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
        Time when the Azure Prices were queried. Date-Time represented in ISO-8601
        format.
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
    @pulumi.getter(name="ramUtilization")
    def ram_utilization(self) -> float:
        """
        Predicted RAM utilization.
        """
        return pulumi.get(self, "ram_utilization")

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
    @pulumi.getter(name="storageUtilization")
    def storage_utilization(self) -> float:
        """
        Predicted storage utilization.
        """
        return pulumi.get(self, "storage_utilization")

    @property
    @pulumi.getter
    def suitability(self) -> str:
        """
        Gets or sets the Assessment cloud suitability.
        """
        return pulumi.get(self, "suitability")

    @property
    @pulumi.getter(name="suitabilityExplanation")
    def suitability_explanation(self) -> str:
        """
        Gets or sets the Assessment suitability explanation.
        """
        return pulumi.get(self, "suitability_explanation")

    @property
    @pulumi.getter(name="suitabilitySummary")
    def suitability_summary(self) -> Mapping[str, int]:
        """
        Cloud suitability summary for all the machines in the assessment.
        """
        return pulumi.get(self, "suitability_summary")

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
    @pulumi.getter(name="totalCpuCores")
    def total_cpu_cores(self) -> float:
        """
        Predicted total CPU cores used.
        """
        return pulumi.get(self, "total_cpu_cores")

    @property
    @pulumi.getter(name="totalMonthlyCost")
    def total_monthly_cost(self) -> float:
        """
        Total monthly cost.
        """
        return pulumi.get(self, "total_monthly_cost")

    @property
    @pulumi.getter(name="totalRamInGB")
    def total_ram_in_gb(self) -> float:
        """
        Predicted total RAM used in GB.
        """
        return pulumi.get(self, "total_ram_in_gb")

    @property
    @pulumi.getter(name="totalStorageInGB")
    def total_storage_in_gb(self) -> float:
        """
        Predicted total Storage used in GB.
        """
        return pulumi.get(self, "total_storage_in_gb")

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

    @property
    @pulumi.getter(name="vcpuOversubscription")
    def vcpu_oversubscription(self) -> Optional[float]:
        """
        VCPU over subscription.
        """
        return pulumi.get(self, "vcpu_oversubscription")


class AwaitableGetAvsAssessmentsOperationResult(GetAvsAssessmentsOperationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvsAssessmentsOperationResult(
            assessment_error_summary=self.assessment_error_summary,
            assessment_type=self.assessment_type,
            azure_location=self.azure_location,
            azure_offer_code=self.azure_offer_code,
            confidence_rating_in_percentage=self.confidence_rating_in_percentage,
            cpu_utilization=self.cpu_utilization,
            created_timestamp=self.created_timestamp,
            currency=self.currency,
            dedupe_compression=self.dedupe_compression,
            discount_percentage=self.discount_percentage,
            failures_to_tolerate_and_raid_level=self.failures_to_tolerate_and_raid_level,
            group_type=self.group_type,
            id=self.id,
            is_stretch_cluster_enabled=self.is_stretch_cluster_enabled,
            limiting_factor=self.limiting_factor,
            mem_overcommit=self.mem_overcommit,
            name=self.name,
            node_type=self.node_type,
            number_of_machines=self.number_of_machines,
            number_of_nodes=self.number_of_nodes,
            percentile=self.percentile,
            perf_data_end_time=self.perf_data_end_time,
            perf_data_start_time=self.perf_data_start_time,
            prices_timestamp=self.prices_timestamp,
            provisioning_state=self.provisioning_state,
            ram_utilization=self.ram_utilization,
            reserved_instance=self.reserved_instance,
            scaling_factor=self.scaling_factor,
            schema_version=self.schema_version,
            sizing_criterion=self.sizing_criterion,
            stage=self.stage,
            status=self.status,
            storage_utilization=self.storage_utilization,
            suitability=self.suitability,
            suitability_explanation=self.suitability_explanation,
            suitability_summary=self.suitability_summary,
            system_data=self.system_data,
            time_range=self.time_range,
            total_cpu_cores=self.total_cpu_cores,
            total_monthly_cost=self.total_monthly_cost,
            total_ram_in_gb=self.total_ram_in_gb,
            total_storage_in_gb=self.total_storage_in_gb,
            type=self.type,
            updated_timestamp=self.updated_timestamp,
            vcpu_oversubscription=self.vcpu_oversubscription)


def get_avs_assessments_operation(assessment_name: Optional[str] = None,
                                  group_name: Optional[str] = None,
                                  project_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAvsAssessmentsOperationResult:
    """
    Get a AvsAssessment


    :param str assessment_name: AVS Assessment ARM name
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
    __ret__ = pulumi.runtime.invoke('azure-native:migrate/v20230315:getAvsAssessmentsOperation', __args__, opts=opts, typ=GetAvsAssessmentsOperationResult).value

    return AwaitableGetAvsAssessmentsOperationResult(
        assessment_error_summary=pulumi.get(__ret__, 'assessment_error_summary'),
        assessment_type=pulumi.get(__ret__, 'assessment_type'),
        azure_location=pulumi.get(__ret__, 'azure_location'),
        azure_offer_code=pulumi.get(__ret__, 'azure_offer_code'),
        confidence_rating_in_percentage=pulumi.get(__ret__, 'confidence_rating_in_percentage'),
        cpu_utilization=pulumi.get(__ret__, 'cpu_utilization'),
        created_timestamp=pulumi.get(__ret__, 'created_timestamp'),
        currency=pulumi.get(__ret__, 'currency'),
        dedupe_compression=pulumi.get(__ret__, 'dedupe_compression'),
        discount_percentage=pulumi.get(__ret__, 'discount_percentage'),
        failures_to_tolerate_and_raid_level=pulumi.get(__ret__, 'failures_to_tolerate_and_raid_level'),
        group_type=pulumi.get(__ret__, 'group_type'),
        id=pulumi.get(__ret__, 'id'),
        is_stretch_cluster_enabled=pulumi.get(__ret__, 'is_stretch_cluster_enabled'),
        limiting_factor=pulumi.get(__ret__, 'limiting_factor'),
        mem_overcommit=pulumi.get(__ret__, 'mem_overcommit'),
        name=pulumi.get(__ret__, 'name'),
        node_type=pulumi.get(__ret__, 'node_type'),
        number_of_machines=pulumi.get(__ret__, 'number_of_machines'),
        number_of_nodes=pulumi.get(__ret__, 'number_of_nodes'),
        percentile=pulumi.get(__ret__, 'percentile'),
        perf_data_end_time=pulumi.get(__ret__, 'perf_data_end_time'),
        perf_data_start_time=pulumi.get(__ret__, 'perf_data_start_time'),
        prices_timestamp=pulumi.get(__ret__, 'prices_timestamp'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        ram_utilization=pulumi.get(__ret__, 'ram_utilization'),
        reserved_instance=pulumi.get(__ret__, 'reserved_instance'),
        scaling_factor=pulumi.get(__ret__, 'scaling_factor'),
        schema_version=pulumi.get(__ret__, 'schema_version'),
        sizing_criterion=pulumi.get(__ret__, 'sizing_criterion'),
        stage=pulumi.get(__ret__, 'stage'),
        status=pulumi.get(__ret__, 'status'),
        storage_utilization=pulumi.get(__ret__, 'storage_utilization'),
        suitability=pulumi.get(__ret__, 'suitability'),
        suitability_explanation=pulumi.get(__ret__, 'suitability_explanation'),
        suitability_summary=pulumi.get(__ret__, 'suitability_summary'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time_range=pulumi.get(__ret__, 'time_range'),
        total_cpu_cores=pulumi.get(__ret__, 'total_cpu_cores'),
        total_monthly_cost=pulumi.get(__ret__, 'total_monthly_cost'),
        total_ram_in_gb=pulumi.get(__ret__, 'total_ram_in_gb'),
        total_storage_in_gb=pulumi.get(__ret__, 'total_storage_in_gb'),
        type=pulumi.get(__ret__, 'type'),
        updated_timestamp=pulumi.get(__ret__, 'updated_timestamp'),
        vcpu_oversubscription=pulumi.get(__ret__, 'vcpu_oversubscription'))


@_utilities.lift_output_func(get_avs_assessments_operation)
def get_avs_assessments_operation_output(assessment_name: Optional[pulumi.Input[str]] = None,
                                         group_name: Optional[pulumi.Input[str]] = None,
                                         project_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAvsAssessmentsOperationResult]:
    """
    Get a AvsAssessment


    :param str assessment_name: AVS Assessment ARM name
    :param str group_name: Group ARM name
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
