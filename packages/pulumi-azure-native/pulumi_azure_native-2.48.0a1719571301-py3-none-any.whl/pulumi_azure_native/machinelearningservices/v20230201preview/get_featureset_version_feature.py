# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetFeaturesetVersionFeatureResult',
    'AwaitableGetFeaturesetVersionFeatureResult',
    'get_featureset_version_feature',
    'get_featureset_version_feature_output',
]

@pulumi.output_type
class GetFeaturesetVersionFeatureResult:
    """
    Dto object representing feature
    """
    def __init__(__self__, data_type=None, description=None, feature_name=None, tags=None):
        if data_type and not isinstance(data_type, str):
            raise TypeError("Expected argument 'data_type' to be a str")
        pulumi.set(__self__, "data_type", data_type)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if feature_name and not isinstance(feature_name, str):
            raise TypeError("Expected argument 'feature_name' to be a str")
        pulumi.set(__self__, "feature_name", feature_name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[str]:
        """
        Specifies type
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Specifies description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> Optional[str]:
        """
        Specifies name
        """
        return pulumi.get(self, "feature_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Specifies tags
        """
        return pulumi.get(self, "tags")


class AwaitableGetFeaturesetVersionFeatureResult(GetFeaturesetVersionFeatureResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFeaturesetVersionFeatureResult(
            data_type=self.data_type,
            description=self.description,
            feature_name=self.feature_name,
            tags=self.tags)


def get_featureset_version_feature(feature_name: Optional[str] = None,
                                   name: Optional[str] = None,
                                   resource_group_name: Optional[str] = None,
                                   version: Optional[str] = None,
                                   workspace_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFeaturesetVersionFeatureResult:
    """
    Dto object representing feature


    :param str feature_name: Specifies name of the feature.
    :param str name: Feature set name. This is case-sensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str version: Feature set version identifier. This is case-sensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['featureName'] = feature_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['version'] = version
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20230201preview:getFeaturesetVersionFeature', __args__, opts=opts, typ=GetFeaturesetVersionFeatureResult).value

    return AwaitableGetFeaturesetVersionFeatureResult(
        data_type=pulumi.get(__ret__, 'data_type'),
        description=pulumi.get(__ret__, 'description'),
        feature_name=pulumi.get(__ret__, 'feature_name'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_featureset_version_feature)
def get_featureset_version_feature_output(feature_name: Optional[pulumi.Input[Optional[str]]] = None,
                                          name: Optional[pulumi.Input[str]] = None,
                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                          version: Optional[pulumi.Input[str]] = None,
                                          workspace_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFeaturesetVersionFeatureResult]:
    """
    Dto object representing feature


    :param str feature_name: Specifies name of the feature.
    :param str name: Feature set name. This is case-sensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str version: Feature set version identifier. This is case-sensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
