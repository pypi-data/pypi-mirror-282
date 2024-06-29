# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['AuthorizationAccessPolicyArgs', 'AuthorizationAccessPolicy']

@pulumi.input_type
class AuthorizationAccessPolicyArgs:
    def __init__(__self__, *,
                 authorization_id: pulumi.Input[str],
                 authorization_provider_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 authorization_access_policy_id: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AuthorizationAccessPolicy resource.
        :param pulumi.Input[str] authorization_id: Identifier of the authorization.
        :param pulumi.Input[str] authorization_provider_id: Identifier of the authorization provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] authorization_access_policy_id: Identifier of the authorization access policy.
        :param pulumi.Input[str] object_id: The Object Id
        :param pulumi.Input[str] tenant_id: The Tenant Id
        """
        pulumi.set(__self__, "authorization_id", authorization_id)
        pulumi.set(__self__, "authorization_provider_id", authorization_provider_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if authorization_access_policy_id is not None:
            pulumi.set(__self__, "authorization_access_policy_id", authorization_access_policy_id)
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="authorizationId")
    def authorization_id(self) -> pulumi.Input[str]:
        """
        Identifier of the authorization.
        """
        return pulumi.get(self, "authorization_id")

    @authorization_id.setter
    def authorization_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "authorization_id", value)

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
    @pulumi.getter(name="authorizationAccessPolicyId")
    def authorization_access_policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the authorization access policy.
        """
        return pulumi.get(self, "authorization_access_policy_id")

    @authorization_access_policy_id.setter
    def authorization_access_policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_access_policy_id", value)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Object Id
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant Id
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class AuthorizationAccessPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_access_policy_id: Optional[pulumi.Input[str]] = None,
                 authorization_id: Optional[pulumi.Input[str]] = None,
                 authorization_provider_id: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Authorization access policy contract.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_access_policy_id: Identifier of the authorization access policy.
        :param pulumi.Input[str] authorization_id: Identifier of the authorization.
        :param pulumi.Input[str] authorization_provider_id: Identifier of the authorization provider.
        :param pulumi.Input[str] object_id: The Object Id
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] tenant_id: The Tenant Id
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AuthorizationAccessPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Authorization access policy contract.

        :param str resource_name: The name of the resource.
        :param AuthorizationAccessPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AuthorizationAccessPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_access_policy_id: Optional[pulumi.Input[str]] = None,
                 authorization_id: Optional[pulumi.Input[str]] = None,
                 authorization_provider_id: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AuthorizationAccessPolicyArgs.__new__(AuthorizationAccessPolicyArgs)

            __props__.__dict__["authorization_access_policy_id"] = authorization_access_policy_id
            if authorization_id is None and not opts.urn:
                raise TypeError("Missing required property 'authorization_id'")
            __props__.__dict__["authorization_id"] = authorization_id
            if authorization_provider_id is None and not opts.urn:
                raise TypeError("Missing required property 'authorization_provider_id'")
            __props__.__dict__["authorization_provider_id"] = authorization_provider_id
            __props__.__dict__["object_id"] = object_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:AuthorizationAccessPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:AuthorizationAccessPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:AuthorizationAccessPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:AuthorizationAccessPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:AuthorizationAccessPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:AuthorizationAccessPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AuthorizationAccessPolicy, __self__).__init__(
            'azure-native:apimanagement/v20230301preview:AuthorizationAccessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AuthorizationAccessPolicy':
        """
        Get an existing AuthorizationAccessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AuthorizationAccessPolicyArgs.__new__(AuthorizationAccessPolicyArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["object_id"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return AuthorizationAccessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Object Id
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Tenant Id
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

