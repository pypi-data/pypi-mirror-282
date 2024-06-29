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
from ._inputs import *

__all__ = ['AppResiliencyArgs', 'AppResiliency']

@pulumi.input_type
class AppResiliencyArgs:
    def __init__(__self__, *,
                 app_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 circuit_breaker_policy: Optional[pulumi.Input['CircuitBreakerPolicyArgs']] = None,
                 http_connection_pool: Optional[pulumi.Input['HttpConnectionPoolArgs']] = None,
                 http_retry_policy: Optional[pulumi.Input['HttpRetryPolicyArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tcp_connection_pool: Optional[pulumi.Input['TcpConnectionPoolArgs']] = None,
                 tcp_retry_policy: Optional[pulumi.Input['TcpRetryPolicyArgs']] = None,
                 timeout_policy: Optional[pulumi.Input['TimeoutPolicyArgs']] = None):
        """
        The set of arguments for constructing a AppResiliency resource.
        :param pulumi.Input[str] app_name: Name of the Container App.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['CircuitBreakerPolicyArgs'] circuit_breaker_policy: Policy that defines circuit breaker conditions
        :param pulumi.Input['HttpConnectionPoolArgs'] http_connection_pool: Defines parameters for http connection pooling
        :param pulumi.Input['HttpRetryPolicyArgs'] http_retry_policy: Policy that defines http request retry conditions
        :param pulumi.Input[str] name: Name of the resiliency policy.
        :param pulumi.Input['TcpConnectionPoolArgs'] tcp_connection_pool: Defines parameters for tcp connection pooling
        :param pulumi.Input['TcpRetryPolicyArgs'] tcp_retry_policy: Policy that defines tcp request retry conditions
        :param pulumi.Input['TimeoutPolicyArgs'] timeout_policy: Policy to set request timeouts
        """
        pulumi.set(__self__, "app_name", app_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if circuit_breaker_policy is not None:
            pulumi.set(__self__, "circuit_breaker_policy", circuit_breaker_policy)
        if http_connection_pool is not None:
            pulumi.set(__self__, "http_connection_pool", http_connection_pool)
        if http_retry_policy is not None:
            pulumi.set(__self__, "http_retry_policy", http_retry_policy)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tcp_connection_pool is not None:
            pulumi.set(__self__, "tcp_connection_pool", tcp_connection_pool)
        if tcp_retry_policy is not None:
            pulumi.set(__self__, "tcp_retry_policy", tcp_retry_policy)
        if timeout_policy is not None:
            pulumi.set(__self__, "timeout_policy", timeout_policy)

    @property
    @pulumi.getter(name="appName")
    def app_name(self) -> pulumi.Input[str]:
        """
        Name of the Container App.
        """
        return pulumi.get(self, "app_name")

    @app_name.setter
    def app_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_name", value)

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
    @pulumi.getter(name="circuitBreakerPolicy")
    def circuit_breaker_policy(self) -> Optional[pulumi.Input['CircuitBreakerPolicyArgs']]:
        """
        Policy that defines circuit breaker conditions
        """
        return pulumi.get(self, "circuit_breaker_policy")

    @circuit_breaker_policy.setter
    def circuit_breaker_policy(self, value: Optional[pulumi.Input['CircuitBreakerPolicyArgs']]):
        pulumi.set(self, "circuit_breaker_policy", value)

    @property
    @pulumi.getter(name="httpConnectionPool")
    def http_connection_pool(self) -> Optional[pulumi.Input['HttpConnectionPoolArgs']]:
        """
        Defines parameters for http connection pooling
        """
        return pulumi.get(self, "http_connection_pool")

    @http_connection_pool.setter
    def http_connection_pool(self, value: Optional[pulumi.Input['HttpConnectionPoolArgs']]):
        pulumi.set(self, "http_connection_pool", value)

    @property
    @pulumi.getter(name="httpRetryPolicy")
    def http_retry_policy(self) -> Optional[pulumi.Input['HttpRetryPolicyArgs']]:
        """
        Policy that defines http request retry conditions
        """
        return pulumi.get(self, "http_retry_policy")

    @http_retry_policy.setter
    def http_retry_policy(self, value: Optional[pulumi.Input['HttpRetryPolicyArgs']]):
        pulumi.set(self, "http_retry_policy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resiliency policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="tcpConnectionPool")
    def tcp_connection_pool(self) -> Optional[pulumi.Input['TcpConnectionPoolArgs']]:
        """
        Defines parameters for tcp connection pooling
        """
        return pulumi.get(self, "tcp_connection_pool")

    @tcp_connection_pool.setter
    def tcp_connection_pool(self, value: Optional[pulumi.Input['TcpConnectionPoolArgs']]):
        pulumi.set(self, "tcp_connection_pool", value)

    @property
    @pulumi.getter(name="tcpRetryPolicy")
    def tcp_retry_policy(self) -> Optional[pulumi.Input['TcpRetryPolicyArgs']]:
        """
        Policy that defines tcp request retry conditions
        """
        return pulumi.get(self, "tcp_retry_policy")

    @tcp_retry_policy.setter
    def tcp_retry_policy(self, value: Optional[pulumi.Input['TcpRetryPolicyArgs']]):
        pulumi.set(self, "tcp_retry_policy", value)

    @property
    @pulumi.getter(name="timeoutPolicy")
    def timeout_policy(self) -> Optional[pulumi.Input['TimeoutPolicyArgs']]:
        """
        Policy to set request timeouts
        """
        return pulumi.get(self, "timeout_policy")

    @timeout_policy.setter
    def timeout_policy(self, value: Optional[pulumi.Input['TimeoutPolicyArgs']]):
        pulumi.set(self, "timeout_policy", value)


class AppResiliency(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_name: Optional[pulumi.Input[str]] = None,
                 circuit_breaker_policy: Optional[pulumi.Input[pulumi.InputType['CircuitBreakerPolicyArgs']]] = None,
                 http_connection_pool: Optional[pulumi.Input[pulumi.InputType['HttpConnectionPoolArgs']]] = None,
                 http_retry_policy: Optional[pulumi.Input[pulumi.InputType['HttpRetryPolicyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tcp_connection_pool: Optional[pulumi.Input[pulumi.InputType['TcpConnectionPoolArgs']]] = None,
                 tcp_retry_policy: Optional[pulumi.Input[pulumi.InputType['TcpRetryPolicyArgs']]] = None,
                 timeout_policy: Optional[pulumi.Input[pulumi.InputType['TimeoutPolicyArgs']]] = None,
                 __props__=None):
        """
        Configuration to setup App Resiliency

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_name: Name of the Container App.
        :param pulumi.Input[pulumi.InputType['CircuitBreakerPolicyArgs']] circuit_breaker_policy: Policy that defines circuit breaker conditions
        :param pulumi.Input[pulumi.InputType['HttpConnectionPoolArgs']] http_connection_pool: Defines parameters for http connection pooling
        :param pulumi.Input[pulumi.InputType['HttpRetryPolicyArgs']] http_retry_policy: Policy that defines http request retry conditions
        :param pulumi.Input[str] name: Name of the resiliency policy.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['TcpConnectionPoolArgs']] tcp_connection_pool: Defines parameters for tcp connection pooling
        :param pulumi.Input[pulumi.InputType['TcpRetryPolicyArgs']] tcp_retry_policy: Policy that defines tcp request retry conditions
        :param pulumi.Input[pulumi.InputType['TimeoutPolicyArgs']] timeout_policy: Policy to set request timeouts
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppResiliencyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Configuration to setup App Resiliency

        :param str resource_name: The name of the resource.
        :param AppResiliencyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppResiliencyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_name: Optional[pulumi.Input[str]] = None,
                 circuit_breaker_policy: Optional[pulumi.Input[pulumi.InputType['CircuitBreakerPolicyArgs']]] = None,
                 http_connection_pool: Optional[pulumi.Input[pulumi.InputType['HttpConnectionPoolArgs']]] = None,
                 http_retry_policy: Optional[pulumi.Input[pulumi.InputType['HttpRetryPolicyArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tcp_connection_pool: Optional[pulumi.Input[pulumi.InputType['TcpConnectionPoolArgs']]] = None,
                 tcp_retry_policy: Optional[pulumi.Input[pulumi.InputType['TcpRetryPolicyArgs']]] = None,
                 timeout_policy: Optional[pulumi.Input[pulumi.InputType['TimeoutPolicyArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AppResiliencyArgs.__new__(AppResiliencyArgs)

            if app_name is None and not opts.urn:
                raise TypeError("Missing required property 'app_name'")
            __props__.__dict__["app_name"] = app_name
            __props__.__dict__["circuit_breaker_policy"] = circuit_breaker_policy
            __props__.__dict__["http_connection_pool"] = http_connection_pool
            __props__.__dict__["http_retry_policy"] = http_retry_policy
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tcp_connection_pool"] = tcp_connection_pool
            __props__.__dict__["tcp_retry_policy"] = tcp_retry_policy
            __props__.__dict__["timeout_policy"] = timeout_policy
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app:AppResiliency"), pulumi.Alias(type_="azure-native:app/v20231102preview:AppResiliency"), pulumi.Alias(type_="azure-native:app/v20240202preview:AppResiliency")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AppResiliency, __self__).__init__(
            'azure-native:app/v20230801preview:AppResiliency',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AppResiliency':
        """
        Get an existing AppResiliency resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AppResiliencyArgs.__new__(AppResiliencyArgs)

        __props__.__dict__["circuit_breaker_policy"] = None
        __props__.__dict__["http_connection_pool"] = None
        __props__.__dict__["http_retry_policy"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tcp_connection_pool"] = None
        __props__.__dict__["tcp_retry_policy"] = None
        __props__.__dict__["timeout_policy"] = None
        __props__.__dict__["type"] = None
        return AppResiliency(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="circuitBreakerPolicy")
    def circuit_breaker_policy(self) -> pulumi.Output[Optional['outputs.CircuitBreakerPolicyResponse']]:
        """
        Policy that defines circuit breaker conditions
        """
        return pulumi.get(self, "circuit_breaker_policy")

    @property
    @pulumi.getter(name="httpConnectionPool")
    def http_connection_pool(self) -> pulumi.Output[Optional['outputs.HttpConnectionPoolResponse']]:
        """
        Defines parameters for http connection pooling
        """
        return pulumi.get(self, "http_connection_pool")

    @property
    @pulumi.getter(name="httpRetryPolicy")
    def http_retry_policy(self) -> pulumi.Output[Optional['outputs.HttpRetryPolicyResponse']]:
        """
        Policy that defines http request retry conditions
        """
        return pulumi.get(self, "http_retry_policy")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tcpConnectionPool")
    def tcp_connection_pool(self) -> pulumi.Output[Optional['outputs.TcpConnectionPoolResponse']]:
        """
        Defines parameters for tcp connection pooling
        """
        return pulumi.get(self, "tcp_connection_pool")

    @property
    @pulumi.getter(name="tcpRetryPolicy")
    def tcp_retry_policy(self) -> pulumi.Output[Optional['outputs.TcpRetryPolicyResponse']]:
        """
        Policy that defines tcp request retry conditions
        """
        return pulumi.get(self, "tcp_retry_policy")

    @property
    @pulumi.getter(name="timeoutPolicy")
    def timeout_policy(self) -> pulumi.Output[Optional['outputs.TimeoutPolicyResponse']]:
        """
        Policy to set request timeouts
        """
        return pulumi.get(self, "timeout_policy")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

