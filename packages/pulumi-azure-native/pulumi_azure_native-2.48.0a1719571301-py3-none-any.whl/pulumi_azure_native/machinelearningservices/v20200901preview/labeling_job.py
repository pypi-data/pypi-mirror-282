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

__all__ = ['LabelingJobArgs', 'LabelingJob']

@pulumi.input_type
class LabelingJobArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 labeling_job_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['LabelingJobPropertiesArgs']] = None):
        """
        The set of arguments for constructing a LabelingJob resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] labeling_job_id: Name and identifier for LabelingJob.
        :param pulumi.Input['LabelingJobPropertiesArgs'] properties: Definition of a labeling job.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if labeling_job_id is not None:
            pulumi.set(__self__, "labeling_job_id", labeling_job_id)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

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
    @pulumi.getter(name="labelingJobId")
    def labeling_job_id(self) -> Optional[pulumi.Input[str]]:
        """
        Name and identifier for LabelingJob.
        """
        return pulumi.get(self, "labeling_job_id")

    @labeling_job_id.setter
    def labeling_job_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "labeling_job_id", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['LabelingJobPropertiesArgs']]:
        """
        Definition of a labeling job.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['LabelingJobPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class LabelingJob(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labeling_job_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['LabelingJobPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Machine Learning labeling job object wrapped into ARM resource envelope.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] labeling_job_id: Name and identifier for LabelingJob.
        :param pulumi.Input[pulumi.InputType['LabelingJobPropertiesArgs']] properties: Definition of a labeling job.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LabelingJobArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Machine Learning labeling job object wrapped into ARM resource envelope.

        :param str resource_name: The name of the resource.
        :param LabelingJobArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LabelingJobArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labeling_job_id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['LabelingJobPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LabelingJobArgs.__new__(LabelingJobArgs)

            __props__.__dict__["labeling_job_id"] = labeling_job_id
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210301preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220601preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221001preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221201preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230201preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230401preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230601preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230801preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240101preview:LabelingJob"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240401preview:LabelingJob")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LabelingJob, __self__).__init__(
            'azure-native:machinelearningservices/v20200901preview:LabelingJob',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LabelingJob':
        """
        Get an existing LabelingJob resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LabelingJobArgs.__new__(LabelingJobArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return LabelingJob(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource entity.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.LabelingJobPropertiesResponse']:
        """
        Definition of a labeling job.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource provider and type.
        """
        return pulumi.get(self, "type")

