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

__all__ = ['ImageDefinitionArgs', 'ImageDefinition']

@pulumi.input_type
class ImageDefinitionArgs:
    def __init__(__self__, *,
                 architecture: pulumi.Input[Union[str, 'ImageArchitecture']],
                 os_state: pulumi.Input[Union[str, 'ImageOSState']],
                 resource_group_name: pulumi.Input[str],
                 security_type: pulumi.Input[Union[str, 'ImageSecurityType']],
                 test_base_account_name: pulumi.Input[str],
                 image_definition_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ImageDefinition resource.
        :param pulumi.Input[Union[str, 'ImageArchitecture']] architecture: Custom image architecture.
        :param pulumi.Input[Union[str, 'ImageOSState']] os_state: Custom image OS state.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'ImageSecurityType']] security_type: Custom image security type.
        :param pulumi.Input[str] test_base_account_name: The resource name of the Test Base Account.
        :param pulumi.Input[str] image_definition_name: The resource name of the test base image definition.
        """
        pulumi.set(__self__, "architecture", architecture)
        pulumi.set(__self__, "os_state", os_state)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "security_type", security_type)
        pulumi.set(__self__, "test_base_account_name", test_base_account_name)
        if image_definition_name is not None:
            pulumi.set(__self__, "image_definition_name", image_definition_name)

    @property
    @pulumi.getter
    def architecture(self) -> pulumi.Input[Union[str, 'ImageArchitecture']]:
        """
        Custom image architecture.
        """
        return pulumi.get(self, "architecture")

    @architecture.setter
    def architecture(self, value: pulumi.Input[Union[str, 'ImageArchitecture']]):
        pulumi.set(self, "architecture", value)

    @property
    @pulumi.getter(name="osState")
    def os_state(self) -> pulumi.Input[Union[str, 'ImageOSState']]:
        """
        Custom image OS state.
        """
        return pulumi.get(self, "os_state")

    @os_state.setter
    def os_state(self, value: pulumi.Input[Union[str, 'ImageOSState']]):
        pulumi.set(self, "os_state", value)

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
    @pulumi.getter(name="securityType")
    def security_type(self) -> pulumi.Input[Union[str, 'ImageSecurityType']]:
        """
        Custom image security type.
        """
        return pulumi.get(self, "security_type")

    @security_type.setter
    def security_type(self, value: pulumi.Input[Union[str, 'ImageSecurityType']]):
        pulumi.set(self, "security_type", value)

    @property
    @pulumi.getter(name="testBaseAccountName")
    def test_base_account_name(self) -> pulumi.Input[str]:
        """
        The resource name of the Test Base Account.
        """
        return pulumi.get(self, "test_base_account_name")

    @test_base_account_name.setter
    def test_base_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "test_base_account_name", value)

    @property
    @pulumi.getter(name="imageDefinitionName")
    def image_definition_name(self) -> Optional[pulumi.Input[str]]:
        """
        The resource name of the test base image definition.
        """
        return pulumi.get(self, "image_definition_name")

    @image_definition_name.setter
    def image_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_definition_name", value)


class ImageDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture: Optional[pulumi.Input[Union[str, 'ImageArchitecture']]] = None,
                 image_definition_name: Optional[pulumi.Input[str]] = None,
                 os_state: Optional[pulumi.Input[Union[str, 'ImageOSState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_type: Optional[pulumi.Input[Union[str, 'ImageSecurityType']]] = None,
                 test_base_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The test base image definition resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'ImageArchitecture']] architecture: Custom image architecture.
        :param pulumi.Input[str] image_definition_name: The resource name of the test base image definition.
        :param pulumi.Input[Union[str, 'ImageOSState']] os_state: Custom image OS state.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'ImageSecurityType']] security_type: Custom image security type.
        :param pulumi.Input[str] test_base_account_name: The resource name of the Test Base Account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The test base image definition resource.

        :param str resource_name: The name of the resource.
        :param ImageDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 architecture: Optional[pulumi.Input[Union[str, 'ImageArchitecture']]] = None,
                 image_definition_name: Optional[pulumi.Input[str]] = None,
                 os_state: Optional[pulumi.Input[Union[str, 'ImageOSState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_type: Optional[pulumi.Input[Union[str, 'ImageSecurityType']]] = None,
                 test_base_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ImageDefinitionArgs.__new__(ImageDefinitionArgs)

            if architecture is None and not opts.urn:
                raise TypeError("Missing required property 'architecture'")
            __props__.__dict__["architecture"] = architecture
            __props__.__dict__["image_definition_name"] = image_definition_name
            if os_state is None and not opts.urn:
                raise TypeError("Missing required property 'os_state'")
            __props__.__dict__["os_state"] = os_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if security_type is None and not opts.urn:
                raise TypeError("Missing required property 'security_type'")
            __props__.__dict__["security_type"] = security_type
            if test_base_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'test_base_account_name'")
            __props__.__dict__["test_base_account_name"] = test_base_account_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:testbase:ImageDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ImageDefinition, __self__).__init__(
            'azure-native:testbase/v20231101preview:ImageDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ImageDefinition':
        """
        Get an existing ImageDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ImageDefinitionArgs.__new__(ImageDefinitionArgs)

        __props__.__dict__["architecture"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["os_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["security_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ImageDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def architecture(self) -> pulumi.Output[str]:
        """
        Custom image architecture.
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osState")
    def os_state(self) -> pulumi.Output[str]:
        """
        Custom image OS state.
        """
        return pulumi.get(self, "os_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securityType")
    def security_type(self) -> pulumi.Output[str]:
        """
        Custom image security type.
        """
        return pulumi.get(self, "security_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

