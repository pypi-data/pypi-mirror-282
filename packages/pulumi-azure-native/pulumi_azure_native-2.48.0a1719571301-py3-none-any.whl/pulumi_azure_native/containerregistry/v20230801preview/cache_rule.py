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

__all__ = ['CacheRuleArgs', 'CacheRule']

@pulumi.input_type
class CacheRuleArgs:
    def __init__(__self__, *,
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 cache_rule_name: Optional[pulumi.Input[str]] = None,
                 credential_set_resource_id: Optional[pulumi.Input[str]] = None,
                 source_repository: Optional[pulumi.Input[str]] = None,
                 target_repository: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CacheRule resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] cache_rule_name: The name of the cache rule.
        :param pulumi.Input[str] credential_set_resource_id: The ARM resource ID of the credential store which is associated with the cache rule.
        :param pulumi.Input[str] source_repository: Source repository pulled from upstream.
        :param pulumi.Input[str] target_repository: Target repository specified in docker pull command.
               Eg: docker pull myregistry.azurecr.io/{targetRepository}:{tag}
        """
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cache_rule_name is not None:
            pulumi.set(__self__, "cache_rule_name", cache_rule_name)
        if credential_set_resource_id is not None:
            pulumi.set(__self__, "credential_set_resource_id", credential_set_resource_id)
        if source_repository is not None:
            pulumi.set(__self__, "source_repository", source_repository)
        if target_repository is not None:
            pulumi.set(__self__, "target_repository", target_repository)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

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
    @pulumi.getter(name="cacheRuleName")
    def cache_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the cache rule.
        """
        return pulumi.get(self, "cache_rule_name")

    @cache_rule_name.setter
    def cache_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_rule_name", value)

    @property
    @pulumi.getter(name="credentialSetResourceId")
    def credential_set_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ARM resource ID of the credential store which is associated with the cache rule.
        """
        return pulumi.get(self, "credential_set_resource_id")

    @credential_set_resource_id.setter
    def credential_set_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_set_resource_id", value)

    @property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> Optional[pulumi.Input[str]]:
        """
        Source repository pulled from upstream.
        """
        return pulumi.get(self, "source_repository")

    @source_repository.setter
    def source_repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_repository", value)

    @property
    @pulumi.getter(name="targetRepository")
    def target_repository(self) -> Optional[pulumi.Input[str]]:
        """
        Target repository specified in docker pull command.
        Eg: docker pull myregistry.azurecr.io/{targetRepository}:{tag}
        """
        return pulumi.get(self, "target_repository")

    @target_repository.setter
    def target_repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_repository", value)


class CacheRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_rule_name: Optional[pulumi.Input[str]] = None,
                 credential_set_resource_id: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_repository: Optional[pulumi.Input[str]] = None,
                 target_repository: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object that represents a cache rule for a container registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cache_rule_name: The name of the cache rule.
        :param pulumi.Input[str] credential_set_resource_id: The ARM resource ID of the credential store which is associated with the cache rule.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] source_repository: Source repository pulled from upstream.
        :param pulumi.Input[str] target_repository: Target repository specified in docker pull command.
               Eg: docker pull myregistry.azurecr.io/{targetRepository}:{tag}
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CacheRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents a cache rule for a container registry.

        :param str resource_name: The name of the resource.
        :param CacheRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CacheRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_rule_name: Optional[pulumi.Input[str]] = None,
                 credential_set_resource_id: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_repository: Optional[pulumi.Input[str]] = None,
                 target_repository: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CacheRuleArgs.__new__(CacheRuleArgs)

            __props__.__dict__["cache_rule_name"] = cache_rule_name
            __props__.__dict__["credential_set_resource_id"] = credential_set_resource_id
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source_repository"] = source_repository
            __props__.__dict__["target_repository"] = target_repository
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerregistry:CacheRule"), pulumi.Alias(type_="azure-native:containerregistry/v20230101preview:CacheRule"), pulumi.Alias(type_="azure-native:containerregistry/v20230601preview:CacheRule"), pulumi.Alias(type_="azure-native:containerregistry/v20230701:CacheRule"), pulumi.Alias(type_="azure-native:containerregistry/v20231101preview:CacheRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CacheRule, __self__).__init__(
            'azure-native:containerregistry/v20230801preview:CacheRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CacheRule':
        """
        Get an existing CacheRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CacheRuleArgs.__new__(CacheRuleArgs)

        __props__.__dict__["creation_date"] = None
        __props__.__dict__["credential_set_resource_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_repository"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_repository"] = None
        __props__.__dict__["type"] = None
        return CacheRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The creation date of the cache rule.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="credentialSetResourceId")
    def credential_set_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ARM resource ID of the credential store which is associated with the cache rule.
        """
        return pulumi.get(self, "credential_set_resource_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceRepository")
    def source_repository(self) -> pulumi.Output[Optional[str]]:
        """
        Source repository pulled from upstream.
        """
        return pulumi.get(self, "source_repository")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetRepository")
    def target_repository(self) -> pulumi.Output[Optional[str]]:
        """
        Target repository specified in docker pull command.
        Eg: docker pull myregistry.azurecr.io/{targetRepository}:{tag}
        """
        return pulumi.get(self, "target_repository")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

