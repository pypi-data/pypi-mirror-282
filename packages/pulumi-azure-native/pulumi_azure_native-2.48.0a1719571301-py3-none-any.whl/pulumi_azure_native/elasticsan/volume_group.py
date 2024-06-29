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

__all__ = ['VolumeGroupArgs', 'VolumeGroup']

@pulumi.input_type
class VolumeGroupArgs:
    def __init__(__self__, *,
                 elastic_san_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 encryption: Optional[pulumi.Input[Union[str, 'EncryptionType']]] = None,
                 network_acls: Optional[pulumi.Input['NetworkRuleSetArgs']] = None,
                 protocol_type: Optional[pulumi.Input[Union[str, 'StorageTargetType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_group_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VolumeGroup resource.
        :param pulumi.Input[str] elastic_san_name: The name of the ElasticSan.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'EncryptionType']] encryption: Type of encryption
        :param pulumi.Input['NetworkRuleSetArgs'] network_acls: A collection of rules governing the accessibility from specific network locations.
        :param pulumi.Input[Union[str, 'StorageTargetType']] protocol_type: Type of storage target
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Azure resource tags.
        :param pulumi.Input[str] volume_group_name: The name of the VolumeGroup.
        """
        pulumi.set(__self__, "elastic_san_name", elastic_san_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if network_acls is not None:
            pulumi.set(__self__, "network_acls", network_acls)
        if protocol_type is not None:
            pulumi.set(__self__, "protocol_type", protocol_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if volume_group_name is not None:
            pulumi.set(__self__, "volume_group_name", volume_group_name)

    @property
    @pulumi.getter(name="elasticSanName")
    def elastic_san_name(self) -> pulumi.Input[str]:
        """
        The name of the ElasticSan.
        """
        return pulumi.get(self, "elastic_san_name")

    @elastic_san_name.setter
    def elastic_san_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "elastic_san_name", value)

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
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input[Union[str, 'EncryptionType']]]:
        """
        Type of encryption
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input[Union[str, 'EncryptionType']]]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional[pulumi.Input['NetworkRuleSetArgs']]:
        """
        A collection of rules governing the accessibility from specific network locations.
        """
        return pulumi.get(self, "network_acls")

    @network_acls.setter
    def network_acls(self, value: Optional[pulumi.Input['NetworkRuleSetArgs']]):
        pulumi.set(self, "network_acls", value)

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> Optional[pulumi.Input[Union[str, 'StorageTargetType']]]:
        """
        Type of storage target
        """
        return pulumi.get(self, "protocol_type")

    @protocol_type.setter
    def protocol_type(self, value: Optional[pulumi.Input[Union[str, 'StorageTargetType']]]):
        pulumi.set(self, "protocol_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the VolumeGroup.
        """
        return pulumi.get(self, "volume_group_name")

    @volume_group_name.setter
    def volume_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_group_name", value)


class VolumeGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elastic_san_name: Optional[pulumi.Input[str]] = None,
                 encryption: Optional[pulumi.Input[Union[str, 'EncryptionType']]] = None,
                 network_acls: Optional[pulumi.Input[pulumi.InputType['NetworkRuleSetArgs']]] = None,
                 protocol_type: Optional[pulumi.Input[Union[str, 'StorageTargetType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Response for Volume Group request.
        Azure REST API version: 2021-11-20-preview. Prior API version in Azure Native 1.x: 2021-11-20-preview.

        Other available API versions: 2022-12-01-preview, 2023-01-01, 2024-05-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] elastic_san_name: The name of the ElasticSan.
        :param pulumi.Input[Union[str, 'EncryptionType']] encryption: Type of encryption
        :param pulumi.Input[pulumi.InputType['NetworkRuleSetArgs']] network_acls: A collection of rules governing the accessibility from specific network locations.
        :param pulumi.Input[Union[str, 'StorageTargetType']] protocol_type: Type of storage target
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Azure resource tags.
        :param pulumi.Input[str] volume_group_name: The name of the VolumeGroup.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Response for Volume Group request.
        Azure REST API version: 2021-11-20-preview. Prior API version in Azure Native 1.x: 2021-11-20-preview.

        Other available API versions: 2022-12-01-preview, 2023-01-01, 2024-05-01.

        :param str resource_name: The name of the resource.
        :param VolumeGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 elastic_san_name: Optional[pulumi.Input[str]] = None,
                 encryption: Optional[pulumi.Input[Union[str, 'EncryptionType']]] = None,
                 network_acls: Optional[pulumi.Input[pulumi.InputType['NetworkRuleSetArgs']]] = None,
                 protocol_type: Optional[pulumi.Input[Union[str, 'StorageTargetType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 volume_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VolumeGroupArgs.__new__(VolumeGroupArgs)

            if elastic_san_name is None and not opts.urn:
                raise TypeError("Missing required property 'elastic_san_name'")
            __props__.__dict__["elastic_san_name"] = elastic_san_name
            __props__.__dict__["encryption"] = encryption
            __props__.__dict__["network_acls"] = network_acls
            __props__.__dict__["protocol_type"] = protocol_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["volume_group_name"] = volume_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:elasticsan/v20211120preview:VolumeGroup"), pulumi.Alias(type_="azure-native:elasticsan/v20221201preview:VolumeGroup"), pulumi.Alias(type_="azure-native:elasticsan/v20230101:VolumeGroup"), pulumi.Alias(type_="azure-native:elasticsan/v20240501:VolumeGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VolumeGroup, __self__).__init__(
            'azure-native:elasticsan:VolumeGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VolumeGroup':
        """
        Get an existing VolumeGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeGroupArgs.__new__(VolumeGroupArgs)

        __props__.__dict__["encryption"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_acls"] = None
        __props__.__dict__["protocol_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return VolumeGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional[str]]:
        """
        Type of encryption
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> pulumi.Output[Optional['outputs.NetworkRuleSetResponse']]:
        """
        A collection of rules governing the accessibility from specific network locations.
        """
        return pulumi.get(self, "network_acls")

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of storage target
        """
        return pulumi.get(self, "protocol_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Resource metadata required by ARM RPC
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

