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

__all__ = ['AuthorizationArgs', 'Authorization']

@pulumi.input_type
class AuthorizationArgs:
    def __init__(__self__, *,
                 authorization_provider_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 authorization_id: Optional[pulumi.Input[str]] = None,
                 authorization_type: Optional[pulumi.Input[Union[str, 'AuthorizationType']]] = None,
                 error: Optional[pulumi.Input['AuthorizationErrorArgs']] = None,
                 o_auth2_grant_type: Optional[pulumi.Input[Union[str, 'OAuth2GrantType']]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Authorization resource.
        :param pulumi.Input[str] authorization_provider_id: Identifier of the authorization provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] authorization_id: Identifier of the authorization.
        :param pulumi.Input[Union[str, 'AuthorizationType']] authorization_type: Authorization type options
        :param pulumi.Input['AuthorizationErrorArgs'] error: Authorization error details.
        :param pulumi.Input[Union[str, 'OAuth2GrantType']] o_auth2_grant_type: OAuth2 grant type options
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Authorization parameters
        :param pulumi.Input[str] status: Status of the Authorization
        """
        pulumi.set(__self__, "authorization_provider_id", authorization_provider_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if authorization_id is not None:
            pulumi.set(__self__, "authorization_id", authorization_id)
        if authorization_type is not None:
            pulumi.set(__self__, "authorization_type", authorization_type)
        if error is not None:
            pulumi.set(__self__, "error", error)
        if o_auth2_grant_type is not None:
            pulumi.set(__self__, "o_auth2_grant_type", o_auth2_grant_type)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="authorizationProviderId")
    def authorization_provider_id(self) -> pulumi.Input[str]:
        """
        Identifier of the authorization provider.
        """
        return pulumi.get(self, "authorization_provider_id")

    @authorization_provider_id.setter
    def authorization_provider_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "authorization_provider_id", value)

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
    @pulumi.getter(name="authorizationId")
    def authorization_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the authorization.
        """
        return pulumi.get(self, "authorization_id")

    @authorization_id.setter
    def authorization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_id", value)

    @property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[pulumi.Input[Union[str, 'AuthorizationType']]]:
        """
        Authorization type options
        """
        return pulumi.get(self, "authorization_type")

    @authorization_type.setter
    def authorization_type(self, value: Optional[pulumi.Input[Union[str, 'AuthorizationType']]]):
        pulumi.set(self, "authorization_type", value)

    @property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input['AuthorizationErrorArgs']]:
        """
        Authorization error details.
        """
        return pulumi.get(self, "error")

    @error.setter
    def error(self, value: Optional[pulumi.Input['AuthorizationErrorArgs']]):
        pulumi.set(self, "error", value)

    @property
    @pulumi.getter(name="oAuth2GrantType")
    def o_auth2_grant_type(self) -> Optional[pulumi.Input[Union[str, 'OAuth2GrantType']]]:
        """
        OAuth2 grant type options
        """
        return pulumi.get(self, "o_auth2_grant_type")

    @o_auth2_grant_type.setter
    def o_auth2_grant_type(self, value: Optional[pulumi.Input[Union[str, 'OAuth2GrantType']]]):
        pulumi.set(self, "o_auth2_grant_type", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Authorization parameters
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Status of the Authorization
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class Authorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_id: Optional[pulumi.Input[str]] = None,
                 authorization_provider_id: Optional[pulumi.Input[str]] = None,
                 authorization_type: Optional[pulumi.Input[Union[str, 'AuthorizationType']]] = None,
                 error: Optional[pulumi.Input[pulumi.InputType['AuthorizationErrorArgs']]] = None,
                 o_auth2_grant_type: Optional[pulumi.Input[Union[str, 'OAuth2GrantType']]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Authorization contract.
        Azure REST API version: 2022-08-01.

        Other available API versions: 2022-09-01-preview, 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_id: Identifier of the authorization.
        :param pulumi.Input[str] authorization_provider_id: Identifier of the authorization provider.
        :param pulumi.Input[Union[str, 'AuthorizationType']] authorization_type: Authorization type options
        :param pulumi.Input[pulumi.InputType['AuthorizationErrorArgs']] error: Authorization error details.
        :param pulumi.Input[Union[str, 'OAuth2GrantType']] o_auth2_grant_type: OAuth2 grant type options
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: Authorization parameters
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] status: Status of the Authorization
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Authorization contract.
        Azure REST API version: 2022-08-01.

        Other available API versions: 2022-09-01-preview, 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param AuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_id: Optional[pulumi.Input[str]] = None,
                 authorization_provider_id: Optional[pulumi.Input[str]] = None,
                 authorization_type: Optional[pulumi.Input[Union[str, 'AuthorizationType']]] = None,
                 error: Optional[pulumi.Input[pulumi.InputType['AuthorizationErrorArgs']]] = None,
                 o_auth2_grant_type: Optional[pulumi.Input[Union[str, 'OAuth2GrantType']]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuthorizationArgs.__new__(AuthorizationArgs)

            __props__.__dict__["authorization_id"] = authorization_id
            if authorization_provider_id is None and not opts.urn:
                raise TypeError("Missing required property 'authorization_provider_id'")
            __props__.__dict__["authorization_provider_id"] = authorization_provider_id
            __props__.__dict__["authorization_type"] = authorization_type
            __props__.__dict__["error"] = error
            __props__.__dict__["o_auth2_grant_type"] = o_auth2_grant_type
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["status"] = status
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:Authorization"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:Authorization"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:Authorization"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:Authorization"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:Authorization"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:Authorization")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Authorization, __self__).__init__(
            'azure-native:apimanagement:Authorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Authorization':
        """
        Get an existing Authorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AuthorizationArgs.__new__(AuthorizationArgs)

        __props__.__dict__["authorization_type"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["o_auth2_grant_type"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return Authorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> pulumi.Output[Optional[str]]:
        """
        Authorization type options
        """
        return pulumi.get(self, "authorization_type")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output[Optional['outputs.AuthorizationErrorResponse']]:
        """
        Authorization error details.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oAuth2GrantType")
    def o_auth2_grant_type(self) -> pulumi.Output[Optional[str]]:
        """
        OAuth2 grant type options
        """
        return pulumi.get(self, "o_auth2_grant_type")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Authorization parameters
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Status of the Authorization
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

