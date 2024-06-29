# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['SqlPoolWorkloadClassifierArgs', 'SqlPoolWorkloadClassifier']

@pulumi.input_type
class SqlPoolWorkloadClassifierArgs:
    def __init__(__self__, *,
                 member_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sql_pool_name: pulumi.Input[str],
                 workload_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 context: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_classifier_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SqlPoolWorkloadClassifier resource.
        :param pulumi.Input[str] member_name: The workload classifier member name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sql_pool_name: SQL pool name
        :param pulumi.Input[str] workload_group_name: The name of the workload group.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] context: The workload classifier context.
        :param pulumi.Input[str] end_time: The workload classifier end time for classification.
        :param pulumi.Input[str] importance: The workload classifier importance.
        :param pulumi.Input[str] label: The workload classifier label.
        :param pulumi.Input[str] start_time: The workload classifier start time for classification.
        :param pulumi.Input[str] workload_classifier_name: The name of the workload classifier.
        """
        pulumi.set(__self__, "member_name", member_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sql_pool_name", sql_pool_name)
        pulumi.set(__self__, "workload_group_name", workload_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if context is not None:
            pulumi.set(__self__, "context", context)
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if importance is not None:
            pulumi.set(__self__, "importance", importance)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)
        if workload_classifier_name is not None:
            pulumi.set(__self__, "workload_classifier_name", workload_classifier_name)

    @property
    @pulumi.getter(name="memberName")
    def member_name(self) -> pulumi.Input[str]:
        """
        The workload classifier member name.
        """
        return pulumi.get(self, "member_name")

    @member_name.setter
    def member_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "member_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sqlPoolName")
    def sql_pool_name(self) -> pulumi.Input[str]:
        """
        SQL pool name
        """
        return pulumi.get(self, "sql_pool_name")

    @sql_pool_name.setter
    def sql_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_pool_name", value)

    @property
    @pulumi.getter(name="workloadGroupName")
    def workload_group_name(self) -> pulumi.Input[str]:
        """
        The name of the workload group.
        """
        return pulumi.get(self, "workload_group_name")

    @workload_group_name.setter
    def workload_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workload_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier context.
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier end time for classification.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter
    def importance(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier importance.
        """
        return pulumi.get(self, "importance")

    @importance.setter
    def importance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "importance", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier label.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier start time for classification.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter(name="workloadClassifierName")
    def workload_classifier_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the workload classifier.
        """
        return pulumi.get(self, "workload_classifier_name")

    @workload_classifier_name.setter
    def workload_classifier_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workload_classifier_name", value)


class SqlPoolWorkloadClassifier(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 member_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_classifier_name: Optional[pulumi.Input[str]] = None,
                 workload_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Workload classifier operations for a data warehouse

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] context: The workload classifier context.
        :param pulumi.Input[str] end_time: The workload classifier end time for classification.
        :param pulumi.Input[str] importance: The workload classifier importance.
        :param pulumi.Input[str] label: The workload classifier label.
        :param pulumi.Input[str] member_name: The workload classifier member name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sql_pool_name: SQL pool name
        :param pulumi.Input[str] start_time: The workload classifier start time for classification.
        :param pulumi.Input[str] workload_classifier_name: The name of the workload classifier.
        :param pulumi.Input[str] workload_group_name: The name of the workload group.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlPoolWorkloadClassifierArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Workload classifier operations for a data warehouse

        :param str resource_name: The name of the resource.
        :param SqlPoolWorkloadClassifierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlPoolWorkloadClassifierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 member_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_classifier_name: Optional[pulumi.Input[str]] = None,
                 workload_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlPoolWorkloadClassifierArgs.__new__(SqlPoolWorkloadClassifierArgs)

            __props__.__dict__["context"] = context
            __props__.__dict__["end_time"] = end_time
            __props__.__dict__["importance"] = importance
            __props__.__dict__["label"] = label
            if member_name is None and not opts.urn:
                raise TypeError("Missing required property 'member_name'")
            __props__.__dict__["member_name"] = member_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sql_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'sql_pool_name'")
            __props__.__dict__["sql_pool_name"] = sql_pool_name
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["workload_classifier_name"] = workload_classifier_name
            if workload_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'workload_group_name'")
            __props__.__dict__["workload_group_name"] = workload_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse:SqlPoolWorkloadClassifier"), pulumi.Alias(type_="azure-native:synapse/v20190601preview:SqlPoolWorkloadClassifier"), pulumi.Alias(type_="azure-native:synapse/v20201201:SqlPoolWorkloadClassifier"), pulumi.Alias(type_="azure-native:synapse/v20210301:SqlPoolWorkloadClassifier"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:SqlPoolWorkloadClassifier"), pulumi.Alias(type_="azure-native:synapse/v20210501:SqlPoolWorkloadClassifier"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:SqlPoolWorkloadClassifier")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlPoolWorkloadClassifier, __self__).__init__(
            'azure-native:synapse/v20210601:SqlPoolWorkloadClassifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlPoolWorkloadClassifier':
        """
        Get an existing SqlPoolWorkloadClassifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlPoolWorkloadClassifierArgs.__new__(SqlPoolWorkloadClassifierArgs)

        __props__.__dict__["context"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["importance"] = None
        __props__.__dict__["label"] = None
        __props__.__dict__["member_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["type"] = None
        return SqlPoolWorkloadClassifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier context.
        """
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier end time for classification.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def importance(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier importance.
        """
        return pulumi.get(self, "importance")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier label.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="memberName")
    def member_name(self) -> pulumi.Output[str]:
        """
        The workload classifier member name.
        """
        return pulumi.get(self, "member_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier start time for classification.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

