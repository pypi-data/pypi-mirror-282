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

__all__ = ['StandbyVirtualMachinePoolArgs', 'StandbyVirtualMachinePool']

@pulumi.input_type
class StandbyVirtualMachinePoolArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_machine_state: pulumi.Input[Union[str, 'VirtualMachineState']],
                 attached_virtual_machine_scale_set_id: Optional[pulumi.Input[str]] = None,
                 elasticity_profile: Optional[pulumi.Input['StandbyVirtualMachinePoolElasticityProfileArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 standby_virtual_machine_pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StandbyVirtualMachinePool resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'VirtualMachineState']] virtual_machine_state: Specifies the desired state of virtual machines in the pool.
        :param pulumi.Input[str] attached_virtual_machine_scale_set_id: Specifies the fully qualified resource ID of a virtual machine scale set the pool is attached to.
        :param pulumi.Input['StandbyVirtualMachinePoolElasticityProfileArgs'] elasticity_profile: Specifies the elasticity profile of the standby virtual machine pools.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] standby_virtual_machine_pool_name: Name of the standby virtual machine pool
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_machine_state", virtual_machine_state)
        if attached_virtual_machine_scale_set_id is not None:
            pulumi.set(__self__, "attached_virtual_machine_scale_set_id", attached_virtual_machine_scale_set_id)
        if elasticity_profile is not None:
            pulumi.set(__self__, "elasticity_profile", elasticity_profile)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if standby_virtual_machine_pool_name is not None:
            pulumi.set(__self__, "standby_virtual_machine_pool_name", standby_virtual_machine_pool_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="virtualMachineState")
    def virtual_machine_state(self) -> pulumi.Input[Union[str, 'VirtualMachineState']]:
        """
        Specifies the desired state of virtual machines in the pool.
        """
        return pulumi.get(self, "virtual_machine_state")

    @virtual_machine_state.setter
    def virtual_machine_state(self, value: pulumi.Input[Union[str, 'VirtualMachineState']]):
        pulumi.set(self, "virtual_machine_state", value)

    @property
    @pulumi.getter(name="attachedVirtualMachineScaleSetId")
    def attached_virtual_machine_scale_set_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the fully qualified resource ID of a virtual machine scale set the pool is attached to.
        """
        return pulumi.get(self, "attached_virtual_machine_scale_set_id")

    @attached_virtual_machine_scale_set_id.setter
    def attached_virtual_machine_scale_set_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attached_virtual_machine_scale_set_id", value)

    @property
    @pulumi.getter(name="elasticityProfile")
    def elasticity_profile(self) -> Optional[pulumi.Input['StandbyVirtualMachinePoolElasticityProfileArgs']]:
        """
        Specifies the elasticity profile of the standby virtual machine pools.
        """
        return pulumi.get(self, "elasticity_profile")

    @elasticity_profile.setter
    def elasticity_profile(self, value: Optional[pulumi.Input['StandbyVirtualMachinePoolElasticityProfileArgs']]):
        pulumi.set(self, "elasticity_profile", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="standbyVirtualMachinePoolName")
    def standby_virtual_machine_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the standby virtual machine pool
        """
        return pulumi.get(self, "standby_virtual_machine_pool_name")

    @standby_virtual_machine_pool_name.setter
    def standby_virtual_machine_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "standby_virtual_machine_pool_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StandbyVirtualMachinePool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_virtual_machine_scale_set_id: Optional[pulumi.Input[str]] = None,
                 elasticity_profile: Optional[pulumi.Input[pulumi.InputType['StandbyVirtualMachinePoolElasticityProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 standby_virtual_machine_pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_machine_state: Optional[pulumi.Input[Union[str, 'VirtualMachineState']]] = None,
                 __props__=None):
        """
        A StandbyVirtualMachinePoolResource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attached_virtual_machine_scale_set_id: Specifies the fully qualified resource ID of a virtual machine scale set the pool is attached to.
        :param pulumi.Input[pulumi.InputType['StandbyVirtualMachinePoolElasticityProfileArgs']] elasticity_profile: Specifies the elasticity profile of the standby virtual machine pools.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] standby_virtual_machine_pool_name: Name of the standby virtual machine pool
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'VirtualMachineState']] virtual_machine_state: Specifies the desired state of virtual machines in the pool.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StandbyVirtualMachinePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A StandbyVirtualMachinePoolResource.

        :param str resource_name: The name of the resource.
        :param StandbyVirtualMachinePoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StandbyVirtualMachinePoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_virtual_machine_scale_set_id: Optional[pulumi.Input[str]] = None,
                 elasticity_profile: Optional[pulumi.Input[pulumi.InputType['StandbyVirtualMachinePoolElasticityProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 standby_virtual_machine_pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_machine_state: Optional[pulumi.Input[Union[str, 'VirtualMachineState']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StandbyVirtualMachinePoolArgs.__new__(StandbyVirtualMachinePoolArgs)

            __props__.__dict__["attached_virtual_machine_scale_set_id"] = attached_virtual_machine_scale_set_id
            __props__.__dict__["elasticity_profile"] = elasticity_profile
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["standby_virtual_machine_pool_name"] = standby_virtual_machine_pool_name
            __props__.__dict__["tags"] = tags
            if virtual_machine_state is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_state'")
            __props__.__dict__["virtual_machine_state"] = virtual_machine_state
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:standbypool:StandbyVirtualMachinePool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StandbyVirtualMachinePool, __self__).__init__(
            'azure-native:standbypool/v20231201preview:StandbyVirtualMachinePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StandbyVirtualMachinePool':
        """
        Get an existing StandbyVirtualMachinePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StandbyVirtualMachinePoolArgs.__new__(StandbyVirtualMachinePoolArgs)

        __props__.__dict__["attached_virtual_machine_scale_set_id"] = None
        __props__.__dict__["elasticity_profile"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machine_state"] = None
        return StandbyVirtualMachinePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachedVirtualMachineScaleSetId")
    def attached_virtual_machine_scale_set_id(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the fully qualified resource ID of a virtual machine scale set the pool is attached to.
        """
        return pulumi.get(self, "attached_virtual_machine_scale_set_id")

    @property
    @pulumi.getter(name="elasticityProfile")
    def elasticity_profile(self) -> pulumi.Output[Optional['outputs.StandbyVirtualMachinePoolElasticityProfileResponse']]:
        """
        Specifies the elasticity profile of the standby virtual machine pools.
        """
        return pulumi.get(self, "elasticity_profile")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachineState")
    def virtual_machine_state(self) -> pulumi.Output[str]:
        """
        Specifies the desired state of virtual machines in the pool.
        """
        return pulumi.get(self, "virtual_machine_state")

