# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['OriginGroupArgs', 'OriginGroup']

@pulumi.input_type
class OriginGroupArgs:
    def __init__(__self__, *,
                 endpoint_name: pulumi.Input[str],
                 origins: pulumi.Input[Sequence[pulumi.Input['ResourceReferenceArgs']]],
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 health_probe_settings: Optional[pulumi.Input['HealthProbeParametersArgs']] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 response_based_origin_error_detection_settings: Optional[pulumi.Input['ResponseBasedOriginErrorDetectionParametersArgs']] = None,
                 traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a OriginGroup resource.
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceReferenceArgs']]] origins: The source of the content being delivered via CDN within given origin group.
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input['HealthProbeParametersArgs'] health_probe_settings: Health probe settings to the origin that is used to determine the health of the origin.
        :param pulumi.Input[str] origin_group_name: Name of the origin group which is unique within the endpoint.
        :param pulumi.Input['ResponseBasedOriginErrorDetectionParametersArgs'] response_based_origin_error_detection_settings: The JSON object that contains the properties to determine origin health using real requests/responses. This property is currently not supported.
        :param pulumi.Input[int] traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.
        """
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        pulumi.set(__self__, "origins", origins)
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if health_probe_settings is not None:
            pulumi.set(__self__, "health_probe_settings", health_probe_settings)
        if origin_group_name is not None:
            pulumi.set(__self__, "origin_group_name", origin_group_name)
        if response_based_origin_error_detection_settings is not None:
            pulumi.set(__self__, "response_based_origin_error_detection_settings", response_based_origin_error_detection_settings)
        if traffic_restoration_time_to_healed_or_new_endpoints_in_minutes is not None:
            pulumi.set(__self__, "traffic_restoration_time_to_healed_or_new_endpoints_in_minutes", traffic_restoration_time_to_healed_or_new_endpoints_in_minutes)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[str]:
        """
        Name of the endpoint under the profile which is unique globally.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter
    def origins(self) -> pulumi.Input[Sequence[pulumi.Input['ResourceReferenceArgs']]]:
        """
        The source of the content being delivered via CDN within given origin group.
        """
        return pulumi.get(self, "origins")

    @origins.setter
    def origins(self, value: pulumi.Input[Sequence[pulumi.Input['ResourceReferenceArgs']]]):
        pulumi.set(self, "origins", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the CDN profile which is unique within the resource group.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> Optional[pulumi.Input['HealthProbeParametersArgs']]:
        """
        Health probe settings to the origin that is used to determine the health of the origin.
        """
        return pulumi.get(self, "health_probe_settings")

    @health_probe_settings.setter
    def health_probe_settings(self, value: Optional[pulumi.Input['HealthProbeParametersArgs']]):
        pulumi.set(self, "health_probe_settings", value)

    @property
    @pulumi.getter(name="originGroupName")
    def origin_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the origin group which is unique within the endpoint.
        """
        return pulumi.get(self, "origin_group_name")

    @origin_group_name.setter
    def origin_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_group_name", value)

    @property
    @pulumi.getter(name="responseBasedOriginErrorDetectionSettings")
    def response_based_origin_error_detection_settings(self) -> Optional[pulumi.Input['ResponseBasedOriginErrorDetectionParametersArgs']]:
        """
        The JSON object that contains the properties to determine origin health using real requests/responses. This property is currently not supported.
        """
        return pulumi.get(self, "response_based_origin_error_detection_settings")

    @response_based_origin_error_detection_settings.setter
    def response_based_origin_error_detection_settings(self, value: Optional[pulumi.Input['ResponseBasedOriginErrorDetectionParametersArgs']]):
        pulumi.set(self, "response_based_origin_error_detection_settings", value)

    @property
    @pulumi.getter(name="trafficRestorationTimeToHealedOrNewEndpointsInMinutes")
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.
        """
        return pulumi.get(self, "traffic_restoration_time_to_healed_or_new_endpoints_in_minutes")

    @traffic_restoration_time_to_healed_or_new_endpoints_in_minutes.setter
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "traffic_restoration_time_to_healed_or_new_endpoints_in_minutes", value)


class OriginGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 health_probe_settings: Optional[pulumi.Input[pulumi.InputType['HealthProbeParametersArgs']]] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 origins: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]]]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 response_based_origin_error_detection_settings: Optional[pulumi.Input[pulumi.InputType['ResponseBasedOriginErrorDetectionParametersArgs']]] = None,
                 traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Origin group comprising of origins is used for load balancing to origins when the content cannot be served from CDN.
        Azure REST API version: 2023-05-01. Prior API version in Azure Native 1.x: 2020-09-01.

        Other available API versions: 2023-07-01-preview, 2024-02-01, 2024-05-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input[pulumi.InputType['HealthProbeParametersArgs']] health_probe_settings: Health probe settings to the origin that is used to determine the health of the origin.
        :param pulumi.Input[str] origin_group_name: Name of the origin group which is unique within the endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]]] origins: The source of the content being delivered via CDN within given origin group.
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[pulumi.InputType['ResponseBasedOriginErrorDetectionParametersArgs']] response_based_origin_error_detection_settings: The JSON object that contains the properties to determine origin health using real requests/responses. This property is currently not supported.
        :param pulumi.Input[int] traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OriginGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Origin group comprising of origins is used for load balancing to origins when the content cannot be served from CDN.
        Azure REST API version: 2023-05-01. Prior API version in Azure Native 1.x: 2020-09-01.

        Other available API versions: 2023-07-01-preview, 2024-02-01, 2024-05-01-preview.

        :param str resource_name: The name of the resource.
        :param OriginGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OriginGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 health_probe_settings: Optional[pulumi.Input[pulumi.InputType['HealthProbeParametersArgs']]] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 origins: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]]]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 response_based_origin_error_detection_settings: Optional[pulumi.Input[pulumi.InputType['ResponseBasedOriginErrorDetectionParametersArgs']]] = None,
                 traffic_restoration_time_to_healed_or_new_endpoints_in_minutes: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OriginGroupArgs.__new__(OriginGroupArgs)

            if endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_name'")
            __props__.__dict__["endpoint_name"] = endpoint_name
            __props__.__dict__["health_probe_settings"] = health_probe_settings
            __props__.__dict__["origin_group_name"] = origin_group_name
            if origins is None and not opts.urn:
                raise TypeError("Missing required property 'origins'")
            __props__.__dict__["origins"] = origins
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["response_based_origin_error_detection_settings"] = response_based_origin_error_detection_settings
            __props__.__dict__["traffic_restoration_time_to_healed_or_new_endpoints_in_minutes"] = traffic_restoration_time_to_healed_or_new_endpoints_in_minutes
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn/v20191231:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20200331:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20200415:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20200901:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20210601:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20220501preview:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20221101preview:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20230501:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20230701preview:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20240201:OriginGroup"), pulumi.Alias(type_="azure-native:cdn/v20240501preview:OriginGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OriginGroup, __self__).__init__(
            'azure-native:cdn:OriginGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OriginGroup':
        """
        Get an existing OriginGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OriginGroupArgs.__new__(OriginGroupArgs)

        __props__.__dict__["health_probe_settings"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["origins"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["response_based_origin_error_detection_settings"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["traffic_restoration_time_to_healed_or_new_endpoints_in_minutes"] = None
        __props__.__dict__["type"] = None
        return OriginGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="healthProbeSettings")
    def health_probe_settings(self) -> pulumi.Output[Optional['outputs.HealthProbeParametersResponse']]:
        """
        Health probe settings to the origin that is used to determine the health of the origin.
        """
        return pulumi.get(self, "health_probe_settings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def origins(self) -> pulumi.Output[Sequence['outputs.ResourceReferenceResponse']]:
        """
        The source of the content being delivered via CDN within given origin group.
        """
        return pulumi.get(self, "origins")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status of the origin group.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status of the origin group.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="responseBasedOriginErrorDetectionSettings")
    def response_based_origin_error_detection_settings(self) -> pulumi.Output[Optional['outputs.ResponseBasedOriginErrorDetectionParametersResponse']]:
        """
        The JSON object that contains the properties to determine origin health using real requests/responses. This property is currently not supported.
        """
        return pulumi.get(self, "response_based_origin_error_detection_settings")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="trafficRestorationTimeToHealedOrNewEndpointsInMinutes")
    def traffic_restoration_time_to_healed_or_new_endpoints_in_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        Time in minutes to shift the traffic to the endpoint gradually when an unhealthy endpoint comes healthy or a new endpoint is added. Default is 10 mins. This property is currently not supported.
        """
        return pulumi.get(self, "traffic_restoration_time_to_healed_or_new_endpoints_in_minutes")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

