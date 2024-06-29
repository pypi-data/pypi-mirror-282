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
    'GetBigDataPoolResult',
    'AwaitableGetBigDataPoolResult',
    'get_big_data_pool',
    'get_big_data_pool_output',
]

@pulumi.output_type
class GetBigDataPoolResult:
    """
    A Big Data pool
    """
    def __init__(__self__, auto_pause=None, auto_scale=None, cache_size=None, creation_date=None, custom_libraries=None, default_spark_log_folder=None, dynamic_executor_allocation=None, id=None, is_autotune_enabled=None, is_compute_isolation_enabled=None, last_succeeded_timestamp=None, library_requirements=None, location=None, name=None, node_count=None, node_size=None, node_size_family=None, provisioning_state=None, session_level_packages_enabled=None, spark_config_properties=None, spark_events_folder=None, spark_version=None, tags=None, type=None):
        if auto_pause and not isinstance(auto_pause, dict):
            raise TypeError("Expected argument 'auto_pause' to be a dict")
        pulumi.set(__self__, "auto_pause", auto_pause)
        if auto_scale and not isinstance(auto_scale, dict):
            raise TypeError("Expected argument 'auto_scale' to be a dict")
        pulumi.set(__self__, "auto_scale", auto_scale)
        if cache_size and not isinstance(cache_size, int):
            raise TypeError("Expected argument 'cache_size' to be a int")
        pulumi.set(__self__, "cache_size", cache_size)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if custom_libraries and not isinstance(custom_libraries, list):
            raise TypeError("Expected argument 'custom_libraries' to be a list")
        pulumi.set(__self__, "custom_libraries", custom_libraries)
        if default_spark_log_folder and not isinstance(default_spark_log_folder, str):
            raise TypeError("Expected argument 'default_spark_log_folder' to be a str")
        pulumi.set(__self__, "default_spark_log_folder", default_spark_log_folder)
        if dynamic_executor_allocation and not isinstance(dynamic_executor_allocation, dict):
            raise TypeError("Expected argument 'dynamic_executor_allocation' to be a dict")
        pulumi.set(__self__, "dynamic_executor_allocation", dynamic_executor_allocation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_autotune_enabled and not isinstance(is_autotune_enabled, bool):
            raise TypeError("Expected argument 'is_autotune_enabled' to be a bool")
        pulumi.set(__self__, "is_autotune_enabled", is_autotune_enabled)
        if is_compute_isolation_enabled and not isinstance(is_compute_isolation_enabled, bool):
            raise TypeError("Expected argument 'is_compute_isolation_enabled' to be a bool")
        pulumi.set(__self__, "is_compute_isolation_enabled", is_compute_isolation_enabled)
        if last_succeeded_timestamp and not isinstance(last_succeeded_timestamp, str):
            raise TypeError("Expected argument 'last_succeeded_timestamp' to be a str")
        pulumi.set(__self__, "last_succeeded_timestamp", last_succeeded_timestamp)
        if library_requirements and not isinstance(library_requirements, dict):
            raise TypeError("Expected argument 'library_requirements' to be a dict")
        pulumi.set(__self__, "library_requirements", library_requirements)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_count and not isinstance(node_count, int):
            raise TypeError("Expected argument 'node_count' to be a int")
        pulumi.set(__self__, "node_count", node_count)
        if node_size and not isinstance(node_size, str):
            raise TypeError("Expected argument 'node_size' to be a str")
        pulumi.set(__self__, "node_size", node_size)
        if node_size_family and not isinstance(node_size_family, str):
            raise TypeError("Expected argument 'node_size_family' to be a str")
        pulumi.set(__self__, "node_size_family", node_size_family)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if session_level_packages_enabled and not isinstance(session_level_packages_enabled, bool):
            raise TypeError("Expected argument 'session_level_packages_enabled' to be a bool")
        pulumi.set(__self__, "session_level_packages_enabled", session_level_packages_enabled)
        if spark_config_properties and not isinstance(spark_config_properties, dict):
            raise TypeError("Expected argument 'spark_config_properties' to be a dict")
        pulumi.set(__self__, "spark_config_properties", spark_config_properties)
        if spark_events_folder and not isinstance(spark_events_folder, str):
            raise TypeError("Expected argument 'spark_events_folder' to be a str")
        pulumi.set(__self__, "spark_events_folder", spark_events_folder)
        if spark_version and not isinstance(spark_version, str):
            raise TypeError("Expected argument 'spark_version' to be a str")
        pulumi.set(__self__, "spark_version", spark_version)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoPause")
    def auto_pause(self) -> Optional['outputs.AutoPausePropertiesResponse']:
        """
        Auto-pausing properties
        """
        return pulumi.get(self, "auto_pause")

    @property
    @pulumi.getter(name="autoScale")
    def auto_scale(self) -> Optional['outputs.AutoScalePropertiesResponse']:
        """
        Auto-scaling properties
        """
        return pulumi.get(self, "auto_scale")

    @property
    @pulumi.getter(name="cacheSize")
    def cache_size(self) -> Optional[int]:
        """
        The cache size
        """
        return pulumi.get(self, "cache_size")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The time when the Big Data pool was created.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="customLibraries")
    def custom_libraries(self) -> Optional[Sequence['outputs.LibraryInfoResponse']]:
        """
        List of custom libraries/packages associated with the spark pool.
        """
        return pulumi.get(self, "custom_libraries")

    @property
    @pulumi.getter(name="defaultSparkLogFolder")
    def default_spark_log_folder(self) -> Optional[str]:
        """
        The default folder where Spark logs will be written.
        """
        return pulumi.get(self, "default_spark_log_folder")

    @property
    @pulumi.getter(name="dynamicExecutorAllocation")
    def dynamic_executor_allocation(self) -> Optional['outputs.DynamicExecutorAllocationResponse']:
        """
        Dynamic Executor Allocation
        """
        return pulumi.get(self, "dynamic_executor_allocation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAutotuneEnabled")
    def is_autotune_enabled(self) -> Optional[bool]:
        """
        Whether autotune is required or not.
        """
        return pulumi.get(self, "is_autotune_enabled")

    @property
    @pulumi.getter(name="isComputeIsolationEnabled")
    def is_compute_isolation_enabled(self) -> Optional[bool]:
        """
        Whether compute isolation is required or not.
        """
        return pulumi.get(self, "is_compute_isolation_enabled")

    @property
    @pulumi.getter(name="lastSucceededTimestamp")
    def last_succeeded_timestamp(self) -> str:
        """
        The time when the Big Data pool was updated successfully.
        """
        return pulumi.get(self, "last_succeeded_timestamp")

    @property
    @pulumi.getter(name="libraryRequirements")
    def library_requirements(self) -> Optional['outputs.LibraryRequirementsResponse']:
        """
        Library version requirements
        """
        return pulumi.get(self, "library_requirements")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[int]:
        """
        The number of nodes in the Big Data pool.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="nodeSize")
    def node_size(self) -> Optional[str]:
        """
        The level of compute power that each node in the Big Data pool has.
        """
        return pulumi.get(self, "node_size")

    @property
    @pulumi.getter(name="nodeSizeFamily")
    def node_size_family(self) -> Optional[str]:
        """
        The kind of nodes that the Big Data pool provides.
        """
        return pulumi.get(self, "node_size_family")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The state of the Big Data pool.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sessionLevelPackagesEnabled")
    def session_level_packages_enabled(self) -> Optional[bool]:
        """
        Whether session level packages enabled.
        """
        return pulumi.get(self, "session_level_packages_enabled")

    @property
    @pulumi.getter(name="sparkConfigProperties")
    def spark_config_properties(self) -> Optional['outputs.SparkConfigPropertiesResponse']:
        """
        Spark configuration file to specify additional properties
        """
        return pulumi.get(self, "spark_config_properties")

    @property
    @pulumi.getter(name="sparkEventsFolder")
    def spark_events_folder(self) -> Optional[str]:
        """
        The Spark events folder
        """
        return pulumi.get(self, "spark_events_folder")

    @property
    @pulumi.getter(name="sparkVersion")
    def spark_version(self) -> Optional[str]:
        """
        The Apache Spark version.
        """
        return pulumi.get(self, "spark_version")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetBigDataPoolResult(GetBigDataPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBigDataPoolResult(
            auto_pause=self.auto_pause,
            auto_scale=self.auto_scale,
            cache_size=self.cache_size,
            creation_date=self.creation_date,
            custom_libraries=self.custom_libraries,
            default_spark_log_folder=self.default_spark_log_folder,
            dynamic_executor_allocation=self.dynamic_executor_allocation,
            id=self.id,
            is_autotune_enabled=self.is_autotune_enabled,
            is_compute_isolation_enabled=self.is_compute_isolation_enabled,
            last_succeeded_timestamp=self.last_succeeded_timestamp,
            library_requirements=self.library_requirements,
            location=self.location,
            name=self.name,
            node_count=self.node_count,
            node_size=self.node_size,
            node_size_family=self.node_size_family,
            provisioning_state=self.provisioning_state,
            session_level_packages_enabled=self.session_level_packages_enabled,
            spark_config_properties=self.spark_config_properties,
            spark_events_folder=self.spark_events_folder,
            spark_version=self.spark_version,
            tags=self.tags,
            type=self.type)


def get_big_data_pool(big_data_pool_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      workspace_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBigDataPoolResult:
    """
    Get a Big Data pool.


    :param str big_data_pool_name: Big Data pool name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['bigDataPoolName'] = big_data_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:synapse/v20210601:getBigDataPool', __args__, opts=opts, typ=GetBigDataPoolResult).value

    return AwaitableGetBigDataPoolResult(
        auto_pause=pulumi.get(__ret__, 'auto_pause'),
        auto_scale=pulumi.get(__ret__, 'auto_scale'),
        cache_size=pulumi.get(__ret__, 'cache_size'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        custom_libraries=pulumi.get(__ret__, 'custom_libraries'),
        default_spark_log_folder=pulumi.get(__ret__, 'default_spark_log_folder'),
        dynamic_executor_allocation=pulumi.get(__ret__, 'dynamic_executor_allocation'),
        id=pulumi.get(__ret__, 'id'),
        is_autotune_enabled=pulumi.get(__ret__, 'is_autotune_enabled'),
        is_compute_isolation_enabled=pulumi.get(__ret__, 'is_compute_isolation_enabled'),
        last_succeeded_timestamp=pulumi.get(__ret__, 'last_succeeded_timestamp'),
        library_requirements=pulumi.get(__ret__, 'library_requirements'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        node_count=pulumi.get(__ret__, 'node_count'),
        node_size=pulumi.get(__ret__, 'node_size'),
        node_size_family=pulumi.get(__ret__, 'node_size_family'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        session_level_packages_enabled=pulumi.get(__ret__, 'session_level_packages_enabled'),
        spark_config_properties=pulumi.get(__ret__, 'spark_config_properties'),
        spark_events_folder=pulumi.get(__ret__, 'spark_events_folder'),
        spark_version=pulumi.get(__ret__, 'spark_version'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_big_data_pool)
def get_big_data_pool_output(big_data_pool_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             workspace_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBigDataPoolResult]:
    """
    Get a Big Data pool.


    :param str big_data_pool_name: Big Data pool name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
