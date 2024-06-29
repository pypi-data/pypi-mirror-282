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

__all__ = ['LoadBalancerArgs', 'LoadBalancer']

@pulumi.input_type
class LoadBalancerArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 primary_agent_pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 allow_service_placement: Optional[pulumi.Input[bool]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 node_selector: Optional[pulumi.Input['LabelSelectorArgs']] = None,
                 service_label_selector: Optional[pulumi.Input['LabelSelectorArgs']] = None,
                 service_namespace_selector: Optional[pulumi.Input['LabelSelectorArgs']] = None):
        """
        The set of arguments for constructing a LoadBalancer resource.
        :param pulumi.Input[str] name: Name of the public load balancer. There will be an internal load balancer created if needed, and the name will be `<name>-internal`. The internal lb shares the same configurations as the external one. The internal lbs are not needed to be included in LoadBalancer list. There must be a name of kubernetes in the list.
        :param pulumi.Input[str] primary_agent_pool_name: Required field. A string value that must specify the ID of an existing agent pool. All nodes in the given pool will always be added to this load balancer. This agent pool must have at least one node and minCount>=1 for autoscaling operations. An agent pool can only be the primary pool for a single load balancer.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name: The name of the managed cluster resource.
        :param pulumi.Input[bool] allow_service_placement: Whether to automatically place services on the load balancer. If not supplied, the default value is true. If set to false manually, both of the external and the internal load balancer will not be selected for services unless they explicitly target it.
        :param pulumi.Input[str] load_balancer_name: The name of the load balancer.
        :param pulumi.Input['LabelSelectorArgs'] node_selector: Nodes that match this selector will be possible members of this load balancer.
        :param pulumi.Input['LabelSelectorArgs'] service_label_selector: Only services that must match this selector can be placed on this load balancer.
        :param pulumi.Input['LabelSelectorArgs'] service_namespace_selector: Services created in namespaces that match the selector can be placed on this load balancer.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "primary_agent_pool_name", primary_agent_pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if allow_service_placement is not None:
            pulumi.set(__self__, "allow_service_placement", allow_service_placement)
        if load_balancer_name is not None:
            pulumi.set(__self__, "load_balancer_name", load_balancer_name)
        if node_selector is not None:
            pulumi.set(__self__, "node_selector", node_selector)
        if service_label_selector is not None:
            pulumi.set(__self__, "service_label_selector", service_label_selector)
        if service_namespace_selector is not None:
            pulumi.set(__self__, "service_namespace_selector", service_namespace_selector)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the public load balancer. There will be an internal load balancer created if needed, and the name will be `<name>-internal`. The internal lb shares the same configurations as the external one. The internal lbs are not needed to be included in LoadBalancer list. There must be a name of kubernetes in the list.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="primaryAgentPoolName")
    def primary_agent_pool_name(self) -> pulumi.Input[str]:
        """
        Required field. A string value that must specify the ID of an existing agent pool. All nodes in the given pool will always be added to this load balancer. This agent pool must have at least one node and minCount>=1 for autoscaling operations. An agent pool can only be the primary pool for a single load balancer.
        """
        return pulumi.get(self, "primary_agent_pool_name")

    @primary_agent_pool_name.setter
    def primary_agent_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary_agent_pool_name", value)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the managed cluster resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="allowServicePlacement")
    def allow_service_placement(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to automatically place services on the load balancer. If not supplied, the default value is true. If set to false manually, both of the external and the internal load balancer will not be selected for services unless they explicitly target it.
        """
        return pulumi.get(self, "allow_service_placement")

    @allow_service_placement.setter
    def allow_service_placement(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_service_placement", value)

    @property
    @pulumi.getter(name="loadBalancerName")
    def load_balancer_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the load balancer.
        """
        return pulumi.get(self, "load_balancer_name")

    @load_balancer_name.setter
    def load_balancer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "load_balancer_name", value)

    @property
    @pulumi.getter(name="nodeSelector")
    def node_selector(self) -> Optional[pulumi.Input['LabelSelectorArgs']]:
        """
        Nodes that match this selector will be possible members of this load balancer.
        """
        return pulumi.get(self, "node_selector")

    @node_selector.setter
    def node_selector(self, value: Optional[pulumi.Input['LabelSelectorArgs']]):
        pulumi.set(self, "node_selector", value)

    @property
    @pulumi.getter(name="serviceLabelSelector")
    def service_label_selector(self) -> Optional[pulumi.Input['LabelSelectorArgs']]:
        """
        Only services that must match this selector can be placed on this load balancer.
        """
        return pulumi.get(self, "service_label_selector")

    @service_label_selector.setter
    def service_label_selector(self, value: Optional[pulumi.Input['LabelSelectorArgs']]):
        pulumi.set(self, "service_label_selector", value)

    @property
    @pulumi.getter(name="serviceNamespaceSelector")
    def service_namespace_selector(self) -> Optional[pulumi.Input['LabelSelectorArgs']]:
        """
        Services created in namespaces that match the selector can be placed on this load balancer.
        """
        return pulumi.get(self, "service_namespace_selector")

    @service_namespace_selector.setter
    def service_namespace_selector(self, value: Optional[pulumi.Input['LabelSelectorArgs']]):
        pulumi.set(self, "service_namespace_selector", value)


class LoadBalancer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_service_placement: Optional[pulumi.Input[bool]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_selector: Optional[pulumi.Input[pulumi.InputType['LabelSelectorArgs']]] = None,
                 primary_agent_pool_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 service_label_selector: Optional[pulumi.Input[pulumi.InputType['LabelSelectorArgs']]] = None,
                 service_namespace_selector: Optional[pulumi.Input[pulumi.InputType['LabelSelectorArgs']]] = None,
                 __props__=None):
        """
        The configurations regarding multiple standard load balancers. If not supplied, single load balancer mode will be used. Multiple standard load balancers mode will be used if at lease one configuration is supplied. There has to be a configuration named `kubernetes`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_service_placement: Whether to automatically place services on the load balancer. If not supplied, the default value is true. If set to false manually, both of the external and the internal load balancer will not be selected for services unless they explicitly target it.
        :param pulumi.Input[str] load_balancer_name: The name of the load balancer.
        :param pulumi.Input[str] name: Name of the public load balancer. There will be an internal load balancer created if needed, and the name will be `<name>-internal`. The internal lb shares the same configurations as the external one. The internal lbs are not needed to be included in LoadBalancer list. There must be a name of kubernetes in the list.
        :param pulumi.Input[pulumi.InputType['LabelSelectorArgs']] node_selector: Nodes that match this selector will be possible members of this load balancer.
        :param pulumi.Input[str] primary_agent_pool_name: Required field. A string value that must specify the ID of an existing agent pool. All nodes in the given pool will always be added to this load balancer. This agent pool must have at least one node and minCount>=1 for autoscaling operations. An agent pool can only be the primary pool for a single load balancer.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the managed cluster resource.
        :param pulumi.Input[pulumi.InputType['LabelSelectorArgs']] service_label_selector: Only services that must match this selector can be placed on this load balancer.
        :param pulumi.Input[pulumi.InputType['LabelSelectorArgs']] service_namespace_selector: Services created in namespaces that match the selector can be placed on this load balancer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LoadBalancerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The configurations regarding multiple standard load balancers. If not supplied, single load balancer mode will be used. Multiple standard load balancers mode will be used if at lease one configuration is supplied. There has to be a configuration named `kubernetes`.

        :param str resource_name: The name of the resource.
        :param LoadBalancerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LoadBalancerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_service_placement: Optional[pulumi.Input[bool]] = None,
                 load_balancer_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_selector: Optional[pulumi.Input[pulumi.InputType['LabelSelectorArgs']]] = None,
                 primary_agent_pool_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 service_label_selector: Optional[pulumi.Input[pulumi.InputType['LabelSelectorArgs']]] = None,
                 service_namespace_selector: Optional[pulumi.Input[pulumi.InputType['LabelSelectorArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LoadBalancerArgs.__new__(LoadBalancerArgs)

            __props__.__dict__["allow_service_placement"] = allow_service_placement
            __props__.__dict__["load_balancer_name"] = load_balancer_name
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["node_selector"] = node_selector
            if primary_agent_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'primary_agent_pool_name'")
            __props__.__dict__["primary_agent_pool_name"] = primary_agent_pool_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["service_label_selector"] = service_label_selector
            __props__.__dict__["service_namespace_selector"] = service_namespace_selector
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerservice:LoadBalancer"), pulumi.Alias(type_="azure-native:containerservice/v20240302preview:LoadBalancer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LoadBalancer, __self__).__init__(
            'azure-native:containerservice/v20240402preview:LoadBalancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LoadBalancer':
        """
        Get an existing LoadBalancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LoadBalancerArgs.__new__(LoadBalancerArgs)

        __props__.__dict__["allow_service_placement"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_selector"] = None
        __props__.__dict__["primary_agent_pool_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_label_selector"] = None
        __props__.__dict__["service_namespace_selector"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return LoadBalancer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowServicePlacement")
    def allow_service_placement(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to automatically place services on the load balancer. If not supplied, the default value is true. If set to false manually, both of the external and the internal load balancer will not be selected for services unless they explicitly target it.
        """
        return pulumi.get(self, "allow_service_placement")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeSelector")
    def node_selector(self) -> pulumi.Output[Optional['outputs.LabelSelectorResponse']]:
        """
        Nodes that match this selector will be possible members of this load balancer.
        """
        return pulumi.get(self, "node_selector")

    @property
    @pulumi.getter(name="primaryAgentPoolName")
    def primary_agent_pool_name(self) -> pulumi.Output[str]:
        """
        Required field. A string value that must specify the ID of an existing agent pool. All nodes in the given pool will always be added to this load balancer. This agent pool must have at least one node and minCount>=1 for autoscaling operations. An agent pool can only be the primary pool for a single load balancer.
        """
        return pulumi.get(self, "primary_agent_pool_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceLabelSelector")
    def service_label_selector(self) -> pulumi.Output[Optional['outputs.LabelSelectorResponse']]:
        """
        Only services that must match this selector can be placed on this load balancer.
        """
        return pulumi.get(self, "service_label_selector")

    @property
    @pulumi.getter(name="serviceNamespaceSelector")
    def service_namespace_selector(self) -> pulumi.Output[Optional['outputs.LabelSelectorResponse']]:
        """
        Services created in namespaces that match the selector can be placed on this load balancer.
        """
        return pulumi.get(self, "service_namespace_selector")

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

