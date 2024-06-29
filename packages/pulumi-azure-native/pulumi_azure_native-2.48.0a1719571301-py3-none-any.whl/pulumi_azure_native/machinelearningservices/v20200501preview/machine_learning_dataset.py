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
from ._inputs import *

__all__ = ['MachineLearningDatasetArgs', 'MachineLearningDataset']

@pulumi.input_type
class MachineLearningDatasetArgs:
    def __init__(__self__, *,
                 dataset_type: pulumi.Input[Union[str, 'DatasetType']],
                 parameters: pulumi.Input['DatasetCreateRequestParametersArgs'],
                 registration: pulumi.Input['DatasetCreateRequestRegistrationArgs'],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 dataset_name: Optional[pulumi.Input[str]] = None,
                 skip_validation: Optional[pulumi.Input[bool]] = None,
                 time_series: Optional[pulumi.Input['DatasetCreateRequestTimeSeriesArgs']] = None):
        """
        The set of arguments for constructing a MachineLearningDataset resource.
        :param pulumi.Input[Union[str, 'DatasetType']] dataset_type: Specifies dataset type.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] dataset_name: The Dataset name.
        :param pulumi.Input[bool] skip_validation: Skip validation that ensures data can be loaded from the dataset before registration.
        """
        pulumi.set(__self__, "dataset_type", dataset_type)
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "registration", registration)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if dataset_name is not None:
            pulumi.set(__self__, "dataset_name", dataset_name)
        if skip_validation is None:
            skip_validation = False
        if skip_validation is not None:
            pulumi.set(__self__, "skip_validation", skip_validation)
        if time_series is not None:
            pulumi.set(__self__, "time_series", time_series)

    @property
    @pulumi.getter(name="datasetType")
    def dataset_type(self) -> pulumi.Input[Union[str, 'DatasetType']]:
        """
        Specifies dataset type.
        """
        return pulumi.get(self, "dataset_type")

    @dataset_type.setter
    def dataset_type(self, value: pulumi.Input[Union[str, 'DatasetType']]):
        pulumi.set(self, "dataset_type", value)

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Input['DatasetCreateRequestParametersArgs']:
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: pulumi.Input['DatasetCreateRequestParametersArgs']):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def registration(self) -> pulumi.Input['DatasetCreateRequestRegistrationArgs']:
        return pulumi.get(self, "registration")

    @registration.setter
    def registration(self, value: pulumi.Input['DatasetCreateRequestRegistrationArgs']):
        pulumi.set(self, "registration", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group in which workspace is located.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="datasetName")
    def dataset_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Dataset name.
        """
        return pulumi.get(self, "dataset_name")

    @dataset_name.setter
    def dataset_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dataset_name", value)

    @property
    @pulumi.getter(name="skipValidation")
    def skip_validation(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip validation that ensures data can be loaded from the dataset before registration.
        """
        return pulumi.get(self, "skip_validation")

    @skip_validation.setter
    def skip_validation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_validation", value)

    @property
    @pulumi.getter(name="timeSeries")
    def time_series(self) -> Optional[pulumi.Input['DatasetCreateRequestTimeSeriesArgs']]:
        return pulumi.get(self, "time_series")

    @time_series.setter
    def time_series(self, value: Optional[pulumi.Input['DatasetCreateRequestTimeSeriesArgs']]):
        pulumi.set(self, "time_series", value)


class MachineLearningDataset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_name: Optional[pulumi.Input[str]] = None,
                 dataset_type: Optional[pulumi.Input[Union[str, 'DatasetType']]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['DatasetCreateRequestParametersArgs']]] = None,
                 registration: Optional[pulumi.Input[pulumi.InputType['DatasetCreateRequestRegistrationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 skip_validation: Optional[pulumi.Input[bool]] = None,
                 time_series: Optional[pulumi.Input[pulumi.InputType['DatasetCreateRequestTimeSeriesArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Machine Learning dataset object wrapped into ARM resource envelope.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dataset_name: The Dataset name.
        :param pulumi.Input[Union[str, 'DatasetType']] dataset_type: Specifies dataset type.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[bool] skip_validation: Skip validation that ensures data can be loaded from the dataset before registration.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MachineLearningDatasetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Machine Learning dataset object wrapped into ARM resource envelope.

        :param str resource_name: The name of the resource.
        :param MachineLearningDatasetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MachineLearningDatasetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dataset_name: Optional[pulumi.Input[str]] = None,
                 dataset_type: Optional[pulumi.Input[Union[str, 'DatasetType']]] = None,
                 parameters: Optional[pulumi.Input[pulumi.InputType['DatasetCreateRequestParametersArgs']]] = None,
                 registration: Optional[pulumi.Input[pulumi.InputType['DatasetCreateRequestRegistrationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 skip_validation: Optional[pulumi.Input[bool]] = None,
                 time_series: Optional[pulumi.Input[pulumi.InputType['DatasetCreateRequestTimeSeriesArgs']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MachineLearningDatasetArgs.__new__(MachineLearningDatasetArgs)

            __props__.__dict__["dataset_name"] = dataset_name
            if dataset_type is None and not opts.urn:
                raise TypeError("Missing required property 'dataset_type'")
            __props__.__dict__["dataset_type"] = dataset_type
            if parameters is None and not opts.urn:
                raise TypeError("Missing required property 'parameters'")
            __props__.__dict__["parameters"] = parameters
            if registration is None and not opts.urn:
                raise TypeError("Missing required property 'registration'")
            __props__.__dict__["registration"] = registration
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if skip_validation is None:
                skip_validation = False
            __props__.__dict__["skip_validation"] = skip_validation
            __props__.__dict__["time_series"] = time_series
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["identity"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["properties"] = None
            __props__.__dict__["sku"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices:MachineLearningDataset")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MachineLearningDataset, __self__).__init__(
            'azure-native:machinelearningservices/v20200501preview:MachineLearningDataset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MachineLearningDataset':
        """
        Get an existing MachineLearningDataset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MachineLearningDatasetArgs.__new__(MachineLearningDatasetArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return MachineLearningDataset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.DatasetResponse']:
        """
        Dataset properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the workspace.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the resource.
        """
        return pulumi.get(self, "type")

