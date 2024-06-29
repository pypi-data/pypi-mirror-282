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

__all__ = ['AssessmentArgs', 'Assessment']

@pulumi.input_type
class AssessmentArgs:
    def __init__(__self__, *,
                 group_name: pulumi.Input[str],
                 project_name: pulumi.Input[str],
                 properties: pulumi.Input['AssessmentPropertiesArgs'],
                 resource_group_name: pulumi.Input[str],
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Assessment resource.
        :param pulumi.Input[str] group_name: Unique name of a group within a project.
        :param pulumi.Input[str] project_name: Name of the Azure Migrate project.
        :param pulumi.Input['AssessmentPropertiesArgs'] properties: Properties of the assessment.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input[str] assessment_name: Unique name of an assessment within a project.
        :param pulumi.Input[str] e_tag: For optimistic concurrency control.
        """
        pulumi.set(__self__, "group_name", group_name)
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if assessment_name is not None:
            pulumi.set(__self__, "assessment_name", assessment_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Input[str]:
        """
        Unique name of a group within a project.
        """
        return pulumi.get(self, "group_name")

    @group_name.setter
    def group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_name", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Migrate project.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['AssessmentPropertiesArgs']:
        """
        Properties of the assessment.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['AssessmentPropertiesArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Resource Group that project is part of.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="assessmentName")
    def assessment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name of an assessment within a project.
        """
        return pulumi.get(self, "assessment_name")

    @assessment_name.setter
    def assessment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_name", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        For optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)


class Assessment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['AssessmentPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An assessment created for a group in the Migration project.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assessment_name: Unique name of an assessment within a project.
        :param pulumi.Input[str] e_tag: For optimistic concurrency control.
        :param pulumi.Input[str] group_name: Unique name of a group within a project.
        :param pulumi.Input[str] project_name: Name of the Azure Migrate project.
        :param pulumi.Input[pulumi.InputType['AssessmentPropertiesArgs']] properties: Properties of the assessment.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssessmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An assessment created for a group in the Migration project.

        :param str resource_name: The name of the resource.
        :param AssessmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssessmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['AssessmentPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssessmentArgs.__new__(AssessmentArgs)

            __props__.__dict__["assessment_name"] = assessment_name
            __props__.__dict__["e_tag"] = e_tag
            if group_name is None and not opts.urn:
                raise TypeError("Missing required property 'group_name'")
            __props__.__dict__["group_name"] = group_name
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:migrate:Assessment"), pulumi.Alias(type_="azure-native:migrate/v20230315:Assessment"), pulumi.Alias(type_="azure-native:migrate/v20230401preview:Assessment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Assessment, __self__).__init__(
            'azure-native:migrate/v20191001:Assessment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Assessment':
        """
        Get an existing Assessment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssessmentArgs.__new__(AssessmentArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return Assessment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        For optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique name of an assessment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.AssessmentPropertiesResponse']:
        """
        Properties of the assessment.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the object = [Microsoft.Migrate/assessmentProjects/groups/assessments].
        """
        return pulumi.get(self, "type")

