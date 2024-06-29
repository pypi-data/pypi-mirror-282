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
    'ListFeaturesetVersionMaterializationJobsResult',
    'AwaitableListFeaturesetVersionMaterializationJobsResult',
    'list_featureset_version_materialization_jobs',
    'list_featureset_version_materialization_jobs_output',
]

@pulumi.output_type
class ListFeaturesetVersionMaterializationJobsResult:
    """
    A paginated list of FeaturesetJob entities.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The link to the next page of FeaturesetJob objects. If null, there are no additional pages.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.FeaturesetJobResponse']]:
        """
        An array of objects of type FeaturesetJob.
        """
        return pulumi.get(self, "value")


class AwaitableListFeaturesetVersionMaterializationJobsResult(ListFeaturesetVersionMaterializationJobsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListFeaturesetVersionMaterializationJobsResult(
            next_link=self.next_link,
            value=self.value)


def list_featureset_version_materialization_jobs(feature_window_end: Optional[str] = None,
                                                 feature_window_start: Optional[str] = None,
                                                 filters: Optional[str] = None,
                                                 name: Optional[str] = None,
                                                 resource_group_name: Optional[str] = None,
                                                 skip: Optional[str] = None,
                                                 version: Optional[str] = None,
                                                 workspace_name: Optional[str] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListFeaturesetVersionMaterializationJobsResult:
    """
    A paginated list of FeaturesetJob entities.


    :param str feature_window_end: End time of the feature window to filter materialization jobs.
    :param str feature_window_start: Start time of the feature window to filter materialization jobs.
    :param str filters: Comma-separated list of tag names (and optionally values). Example: tag1,tag2=value2
    :param str name: Container name. This is case-sensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str skip: Continuation token for pagination.
    :param str version: Version identifier. This is case-sensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['featureWindowEnd'] = feature_window_end
    __args__['featureWindowStart'] = feature_window_start
    __args__['filters'] = filters
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['skip'] = skip
    __args__['version'] = version
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20230601preview:listFeaturesetVersionMaterializationJobs', __args__, opts=opts, typ=ListFeaturesetVersionMaterializationJobsResult).value

    return AwaitableListFeaturesetVersionMaterializationJobsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_featureset_version_materialization_jobs)
def list_featureset_version_materialization_jobs_output(feature_window_end: Optional[pulumi.Input[Optional[str]]] = None,
                                                        feature_window_start: Optional[pulumi.Input[Optional[str]]] = None,
                                                        filters: Optional[pulumi.Input[Optional[str]]] = None,
                                                        name: Optional[pulumi.Input[str]] = None,
                                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                                        skip: Optional[pulumi.Input[Optional[str]]] = None,
                                                        version: Optional[pulumi.Input[str]] = None,
                                                        workspace_name: Optional[pulumi.Input[str]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListFeaturesetVersionMaterializationJobsResult]:
    """
    A paginated list of FeaturesetJob entities.


    :param str feature_window_end: End time of the feature window to filter materialization jobs.
    :param str feature_window_start: Start time of the feature window to filter materialization jobs.
    :param str filters: Comma-separated list of tag names (and optionally values). Example: tag1,tag2=value2
    :param str name: Container name. This is case-sensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str skip: Continuation token for pagination.
    :param str version: Version identifier. This is case-sensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
