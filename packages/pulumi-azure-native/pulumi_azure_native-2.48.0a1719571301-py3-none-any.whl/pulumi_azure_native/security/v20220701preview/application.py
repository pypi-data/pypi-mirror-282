# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ApplicationArgs', 'Application']

@pulumi.input_type
class ApplicationArgs:
    def __init__(__self__, *,
                 source_resource_type: pulumi.Input[Union[str, 'ApplicationSourceResourceType']],
                 application_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Application resource.
        :param pulumi.Input[Union[str, 'ApplicationSourceResourceType']] source_resource_type: The application source, what it affects, e.g. Assessments
        :param pulumi.Input[str] application_id: The security Application key - unique key for the standard application
        :param pulumi.Input[str] description: description of the application
        :param pulumi.Input[str] display_name: display name of the application
        """
        pulumi.set(__self__, "source_resource_type", source_resource_type)
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(self) -> pulumi.Input[Union[str, 'ApplicationSourceResourceType']]:
        """
        The application source, what it affects, e.g. Assessments
        """
        return pulumi.get(self, "source_resource_type")

    @source_resource_type.setter
    def source_resource_type(self, value: pulumi.Input[Union[str, 'ApplicationSourceResourceType']]):
        pulumi.set(self, "source_resource_type", value)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The security Application key - unique key for the standard application
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        description of the application
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        display name of the application
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


class Application(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 source_resource_type: Optional[pulumi.Input[Union[str, 'ApplicationSourceResourceType']]] = None,
                 __props__=None):
        """
        Security Application over a given scope

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_id: The security Application key - unique key for the standard application
        :param pulumi.Input[str] description: description of the application
        :param pulumi.Input[str] display_name: display name of the application
        :param pulumi.Input[Union[str, 'ApplicationSourceResourceType']] source_resource_type: The application source, what it affects, e.g. Assessments
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Security Application over a given scope

        :param str resource_name: The name of the resource.
        :param ApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 source_resource_type: Optional[pulumi.Input[Union[str, 'ApplicationSourceResourceType']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationArgs.__new__(ApplicationArgs)

            __props__.__dict__["application_id"] = application_id
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if source_resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'source_resource_type'")
            __props__.__dict__["source_resource_type"] = source_resource_type
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:Application")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Application, __self__).__init__(
            'azure-native:security/v20220701preview:Application',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Application':
        """
        Get an existing Application resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationArgs.__new__(ApplicationArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["source_resource_type"] = None
        __props__.__dict__["type"] = None
        return Application(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        description of the application
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        display name of the application
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sourceResourceType")
    def source_resource_type(self) -> pulumi.Output[str]:
        """
        The application source, what it affects, e.g. Assessments
        """
        return pulumi.get(self, "source_resource_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

