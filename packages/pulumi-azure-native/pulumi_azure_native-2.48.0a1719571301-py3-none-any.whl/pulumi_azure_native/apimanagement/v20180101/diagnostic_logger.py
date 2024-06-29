# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['DiagnosticLoggerArgs', 'DiagnosticLogger']

@pulumi.input_type
class DiagnosticLoggerArgs:
    def __init__(__self__, *,
                 diagnostic_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 loggerid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DiagnosticLogger resource.
        :param pulumi.Input[str] diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] loggerid: Logger identifier. Must be unique in the API Management service instance.
        """
        pulumi.set(__self__, "diagnostic_id", diagnostic_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if loggerid is not None:
            pulumi.set(__self__, "loggerid", loggerid)

    @property
    @pulumi.getter(name="diagnosticId")
    def diagnostic_id(self) -> pulumi.Input[str]:
        """
        Diagnostic identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "diagnostic_id")

    @diagnostic_id.setter
    def diagnostic_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "diagnostic_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def loggerid(self) -> Optional[pulumi.Input[str]]:
        """
        Logger identifier. Must be unique in the API Management service instance.
        """
        return pulumi.get(self, "loggerid")

    @loggerid.setter
    def loggerid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "loggerid", value)


class DiagnosticLogger(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 diagnostic_id: Optional[pulumi.Input[str]] = None,
                 loggerid: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Logger details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] diagnostic_id: Diagnostic identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] loggerid: Logger identifier. Must be unique in the API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DiagnosticLoggerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Logger details.

        :param str resource_name: The name of the resource.
        :param DiagnosticLoggerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DiagnosticLoggerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 diagnostic_id: Optional[pulumi.Input[str]] = None,
                 loggerid: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DiagnosticLoggerArgs.__new__(DiagnosticLoggerArgs)

            if diagnostic_id is None and not opts.urn:
                raise TypeError("Missing required property 'diagnostic_id'")
            __props__.__dict__["diagnostic_id"] = diagnostic_id
            __props__.__dict__["loggerid"] = loggerid
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["credentials"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["is_buffered"] = None
            __props__.__dict__["logger_type"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20170301:DiagnosticLogger")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DiagnosticLogger, __self__).__init__(
            'azure-native:apimanagement/v20180101:DiagnosticLogger',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DiagnosticLogger':
        """
        Get an existing DiagnosticLogger resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DiagnosticLoggerArgs.__new__(DiagnosticLoggerArgs)

        __props__.__dict__["credentials"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["is_buffered"] = None
        __props__.__dict__["logger_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return DiagnosticLogger(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The name and SendRule connection string of the event hub for azureEventHub logger.
        Instrumentation key for applicationInsights logger.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Logger description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="isBuffered")
    def is_buffered(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether records are buffered in the logger before publishing. Default is assumed to be true.
        """
        return pulumi.get(self, "is_buffered")

    @property
    @pulumi.getter(name="loggerType")
    def logger_type(self) -> pulumi.Output[str]:
        """
        Logger type.
        """
        return pulumi.get(self, "logger_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

