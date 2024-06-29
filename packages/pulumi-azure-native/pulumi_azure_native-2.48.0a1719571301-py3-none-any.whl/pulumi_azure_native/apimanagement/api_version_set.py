# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['ApiVersionSetArgs', 'ApiVersionSet']

@pulumi.input_type
class ApiVersionSetArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 versioning_scheme: pulumi.Input[Union[str, 'VersioningScheme']],
                 description: Optional[pulumi.Input[str]] = None,
                 version_header_name: Optional[pulumi.Input[str]] = None,
                 version_query_name: Optional[pulumi.Input[str]] = None,
                 version_set_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiVersionSet resource.
        :param pulumi.Input[str] display_name: Name of API Version Set
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Union[str, 'VersioningScheme']] versioning_scheme: An value that determines where the API Version identifier will be located in a HTTP request.
        :param pulumi.Input[str] description: Description of API Version Set.
        :param pulumi.Input[str] version_header_name: Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.
        :param pulumi.Input[str] version_query_name: Name of query parameter that indicates the API Version if versioningScheme is set to `query`.
        :param pulumi.Input[str] version_set_id: Api Version Set identifier. Must be unique in the current API Management service instance.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "versioning_scheme", versioning_scheme)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if version_header_name is not None:
            pulumi.set(__self__, "version_header_name", version_header_name)
        if version_query_name is not None:
            pulumi.set(__self__, "version_query_name", version_query_name)
        if version_set_id is not None:
            pulumi.set(__self__, "version_set_id", version_set_id)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Name of API Version Set
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

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
    @pulumi.getter(name="versioningScheme")
    def versioning_scheme(self) -> pulumi.Input[Union[str, 'VersioningScheme']]:
        """
        An value that determines where the API Version identifier will be located in a HTTP request.
        """
        return pulumi.get(self, "versioning_scheme")

    @versioning_scheme.setter
    def versioning_scheme(self, value: pulumi.Input[Union[str, 'VersioningScheme']]):
        pulumi.set(self, "versioning_scheme", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of API Version Set.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="versionHeaderName")
    def version_header_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.
        """
        return pulumi.get(self, "version_header_name")

    @version_header_name.setter
    def version_header_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_header_name", value)

    @property
    @pulumi.getter(name="versionQueryName")
    def version_query_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of query parameter that indicates the API Version if versioningScheme is set to `query`.
        """
        return pulumi.get(self, "version_query_name")

    @version_query_name.setter
    def version_query_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_query_name", value)

    @property
    @pulumi.getter(name="versionSetId")
    def version_set_id(self) -> Optional[pulumi.Input[str]]:
        """
        Api Version Set identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "version_set_id")

    @version_set_id.setter
    def version_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_set_id", value)


class ApiVersionSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 version_header_name: Optional[pulumi.Input[str]] = None,
                 version_query_name: Optional[pulumi.Input[str]] = None,
                 version_set_id: Optional[pulumi.Input[str]] = None,
                 versioning_scheme: Optional[pulumi.Input[Union[str, 'VersioningScheme']]] = None,
                 __props__=None):
        """
        API Version Set Contract details.
        Azure REST API version: 2022-08-01. Prior API version in Azure Native 1.x: 2020-12-01.

        Other available API versions: 2022-09-01-preview, 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of API Version Set.
        :param pulumi.Input[str] display_name: Name of API Version Set
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] version_header_name: Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.
        :param pulumi.Input[str] version_query_name: Name of query parameter that indicates the API Version if versioningScheme is set to `query`.
        :param pulumi.Input[str] version_set_id: Api Version Set identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[Union[str, 'VersioningScheme']] versioning_scheme: An value that determines where the API Version identifier will be located in a HTTP request.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiVersionSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        API Version Set Contract details.
        Azure REST API version: 2022-08-01. Prior API version in Azure Native 1.x: 2020-12-01.

        Other available API versions: 2022-09-01-preview, 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param ApiVersionSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiVersionSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 version_header_name: Optional[pulumi.Input[str]] = None,
                 version_query_name: Optional[pulumi.Input[str]] = None,
                 version_set_id: Optional[pulumi.Input[str]] = None,
                 versioning_scheme: Optional[pulumi.Input[Union[str, 'VersioningScheme']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiVersionSetArgs.__new__(ApiVersionSetArgs)

            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["version_header_name"] = version_header_name
            __props__.__dict__["version_query_name"] = version_query_name
            __props__.__dict__["version_set_id"] = version_set_id
            if versioning_scheme is None and not opts.urn:
                raise TypeError("Missing required property 'versioning_scheme'")
            __props__.__dict__["versioning_scheme"] = versioning_scheme
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20170301:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:ApiVersionSet"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:ApiVersionSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApiVersionSet, __self__).__init__(
            'azure-native:apimanagement:ApiVersionSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiVersionSet':
        """
        Get an existing ApiVersionSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiVersionSetArgs.__new__(ApiVersionSetArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version_header_name"] = None
        __props__.__dict__["version_query_name"] = None
        __props__.__dict__["versioning_scheme"] = None
        return ApiVersionSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of API Version Set.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Name of API Version Set
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="versionHeaderName")
    def version_header_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of HTTP header parameter that indicates the API Version if versioningScheme is set to `header`.
        """
        return pulumi.get(self, "version_header_name")

    @property
    @pulumi.getter(name="versionQueryName")
    def version_query_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of query parameter that indicates the API Version if versioningScheme is set to `query`.
        """
        return pulumi.get(self, "version_query_name")

    @property
    @pulumi.getter(name="versioningScheme")
    def versioning_scheme(self) -> pulumi.Output[str]:
        """
        An value that determines where the API Version identifier will be located in a HTTP request.
        """
        return pulumi.get(self, "versioning_scheme")

