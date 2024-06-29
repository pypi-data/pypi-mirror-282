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

__all__ = ['LinkerArgs', 'Linker']

@pulumi.input_type
class LinkerArgs:
    def __init__(__self__, *,
                 resource_uri: pulumi.Input[str],
                 auth_info: Optional[pulumi.Input[Union['SecretAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgs']]] = None,
                 client_type: Optional[pulumi.Input[Union[str, 'ClientType']]] = None,
                 linker_name: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input['SecretStoreArgs']] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 v_net_solution: Optional[pulumi.Input['VNetSolutionArgs']] = None):
        """
        The set of arguments for constructing a Linker resource.
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
        :param pulumi.Input[Union['SecretAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgs']] auth_info: The authentication type.
        :param pulumi.Input[Union[str, 'ClientType']] client_type: The application client type
        :param pulumi.Input[str] linker_name: The name Linker resource.
        :param pulumi.Input['SecretStoreArgs'] secret_store: An option to store secret value in secure place
        :param pulumi.Input[str] target_id: The resource Id of target service.
        :param pulumi.Input['VNetSolutionArgs'] v_net_solution: The VNet solution.
        """
        pulumi.set(__self__, "resource_uri", resource_uri)
        if auth_info is not None:
            pulumi.set(__self__, "auth_info", auth_info)
        if client_type is not None:
            pulumi.set(__self__, "client_type", client_type)
        if linker_name is not None:
            pulumi.set(__self__, "linker_name", linker_name)
        if secret_store is not None:
            pulumi.set(__self__, "secret_store", secret_store)
        if target_id is not None:
            pulumi.set(__self__, "target_id", target_id)
        if v_net_solution is not None:
            pulumi.set(__self__, "v_net_solution", v_net_solution)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[str]:
        """
        The fully qualified Azure Resource manager identifier of the resource to be connected.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_uri", value)

    @property
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> Optional[pulumi.Input[Union['SecretAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgs']]]:
        """
        The authentication type.
        """
        return pulumi.get(self, "auth_info")

    @auth_info.setter
    def auth_info(self, value: Optional[pulumi.Input[Union['SecretAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgs']]]):
        pulumi.set(self, "auth_info", value)

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[pulumi.Input[Union[str, 'ClientType']]]:
        """
        The application client type
        """
        return pulumi.get(self, "client_type")

    @client_type.setter
    def client_type(self, value: Optional[pulumi.Input[Union[str, 'ClientType']]]):
        pulumi.set(self, "client_type", value)

    @property
    @pulumi.getter(name="linkerName")
    def linker_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name Linker resource.
        """
        return pulumi.get(self, "linker_name")

    @linker_name.setter
    def linker_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linker_name", value)

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[pulumi.Input['SecretStoreArgs']]:
        """
        An option to store secret value in secure place
        """
        return pulumi.get(self, "secret_store")

    @secret_store.setter
    def secret_store(self, value: Optional[pulumi.Input['SecretStoreArgs']]):
        pulumi.set(self, "secret_store", value)

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource Id of target service.
        """
        return pulumi.get(self, "target_id")

    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_id", value)

    @property
    @pulumi.getter(name="vNetSolution")
    def v_net_solution(self) -> Optional[pulumi.Input['VNetSolutionArgs']]:
        """
        The VNet solution.
        """
        return pulumi.get(self, "v_net_solution")

    @v_net_solution.setter
    def v_net_solution(self, value: Optional[pulumi.Input['VNetSolutionArgs']]):
        pulumi.set(self, "v_net_solution", value)


class Linker(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_info: Optional[pulumi.Input[Union[pulumi.InputType['SecretAuthInfoArgs'], pulumi.InputType['ServicePrincipalCertificateAuthInfoArgs'], pulumi.InputType['ServicePrincipalSecretAuthInfoArgs'], pulumi.InputType['SystemAssignedIdentityAuthInfoArgs'], pulumi.InputType['UserAssignedIdentityAuthInfoArgs']]]] = None,
                 client_type: Optional[pulumi.Input[Union[str, 'ClientType']]] = None,
                 linker_name: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input[pulumi.InputType['SecretStoreArgs']]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 v_net_solution: Optional[pulumi.Input[pulumi.InputType['VNetSolutionArgs']]] = None,
                 __props__=None):
        """
        Linker of source and target resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[pulumi.InputType['SecretAuthInfoArgs'], pulumi.InputType['ServicePrincipalCertificateAuthInfoArgs'], pulumi.InputType['ServicePrincipalSecretAuthInfoArgs'], pulumi.InputType['SystemAssignedIdentityAuthInfoArgs'], pulumi.InputType['UserAssignedIdentityAuthInfoArgs']]] auth_info: The authentication type.
        :param pulumi.Input[Union[str, 'ClientType']] client_type: The application client type
        :param pulumi.Input[str] linker_name: The name Linker resource.
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
        :param pulumi.Input[pulumi.InputType['SecretStoreArgs']] secret_store: An option to store secret value in secure place
        :param pulumi.Input[str] target_id: The resource Id of target service.
        :param pulumi.Input[pulumi.InputType['VNetSolutionArgs']] v_net_solution: The VNet solution.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Linker of source and target resource

        :param str resource_name: The name of the resource.
        :param LinkerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_info: Optional[pulumi.Input[Union[pulumi.InputType['SecretAuthInfoArgs'], pulumi.InputType['ServicePrincipalCertificateAuthInfoArgs'], pulumi.InputType['ServicePrincipalSecretAuthInfoArgs'], pulumi.InputType['SystemAssignedIdentityAuthInfoArgs'], pulumi.InputType['UserAssignedIdentityAuthInfoArgs']]]] = None,
                 client_type: Optional[pulumi.Input[Union[str, 'ClientType']]] = None,
                 linker_name: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input[pulumi.InputType['SecretStoreArgs']]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 v_net_solution: Optional[pulumi.Input[pulumi.InputType['VNetSolutionArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkerArgs.__new__(LinkerArgs)

            __props__.__dict__["auth_info"] = auth_info
            __props__.__dict__["client_type"] = client_type
            __props__.__dict__["linker_name"] = linker_name
            if resource_uri is None and not opts.urn:
                raise TypeError("Missing required property 'resource_uri'")
            __props__.__dict__["resource_uri"] = resource_uri
            __props__.__dict__["secret_store"] = secret_store
            __props__.__dict__["target_id"] = target_id
            __props__.__dict__["v_net_solution"] = v_net_solution
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicelinker:Linker"), pulumi.Alias(type_="azure-native:servicelinker/v20220101preview:Linker"), pulumi.Alias(type_="azure-native:servicelinker/v20220501:Linker"), pulumi.Alias(type_="azure-native:servicelinker/v20221101preview:Linker"), pulumi.Alias(type_="azure-native:servicelinker/v20230401preview:Linker"), pulumi.Alias(type_="azure-native:servicelinker/v20240401:Linker")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Linker, __self__).__init__(
            'azure-native:servicelinker/v20211101preview:Linker',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Linker':
        """
        Get an existing Linker resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LinkerArgs.__new__(LinkerArgs)

        __props__.__dict__["auth_info"] = None
        __props__.__dict__["client_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["secret_store"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["v_net_solution"] = None
        return Linker(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> pulumi.Output[Optional[Any]]:
        """
        The authentication type.
        """
        return pulumi.get(self, "auth_info")

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> pulumi.Output[Optional[str]]:
        """
        The application client type
        """
        return pulumi.get(self, "client_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state. 
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> pulumi.Output[Optional['outputs.SecretStoreResponse']]:
        """
        An option to store secret value in secure place
        """
        return pulumi.get(self, "secret_store")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource Id of target service.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vNetSolution")
    def v_net_solution(self) -> pulumi.Output[Optional['outputs.VNetSolutionResponse']]:
        """
        The VNet solution.
        """
        return pulumi.get(self, "v_net_solution")

