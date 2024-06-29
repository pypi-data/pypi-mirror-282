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

__all__ = ['L2NetworkArgs', 'L2Network']

@pulumi.input_type
class L2NetworkArgs:
    def __init__(__self__, *,
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 l2_isolation_domain_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 hybrid_aks_plugin_type: Optional[pulumi.Input[Union[str, 'HybridAksPluginType']]] = None,
                 interface_name: Optional[pulumi.Input[str]] = None,
                 l2_network_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a L2Network resource.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[str] l2_isolation_domain_id: The resource ID of the Network Fabric l2IsolationDomain.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'HybridAksPluginType']] hybrid_aks_plugin_type: Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS.
        :param pulumi.Input[str] interface_name: The default interface name for this L2 network in the virtual machine. This name can be overridden by the name supplied in the network attachment configuration of that virtual machine.
        :param pulumi.Input[str] l2_network_name: The name of the L2 network.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "l2_isolation_domain_id", l2_isolation_domain_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if hybrid_aks_plugin_type is None:
            hybrid_aks_plugin_type = 'SRIOV'
        if hybrid_aks_plugin_type is not None:
            pulumi.set(__self__, "hybrid_aks_plugin_type", hybrid_aks_plugin_type)
        if interface_name is not None:
            pulumi.set(__self__, "interface_name", interface_name)
        if l2_network_name is not None:
            pulumi.set(__self__, "l2_network_name", l2_network_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="l2IsolationDomainId")
    def l2_isolation_domain_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Network Fabric l2IsolationDomain.
        """
        return pulumi.get(self, "l2_isolation_domain_id")

    @l2_isolation_domain_id.setter
    def l2_isolation_domain_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "l2_isolation_domain_id", value)

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
    @pulumi.getter(name="hybridAksPluginType")
    def hybrid_aks_plugin_type(self) -> Optional[pulumi.Input[Union[str, 'HybridAksPluginType']]]:
        """
        Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS.
        """
        return pulumi.get(self, "hybrid_aks_plugin_type")

    @hybrid_aks_plugin_type.setter
    def hybrid_aks_plugin_type(self, value: Optional[pulumi.Input[Union[str, 'HybridAksPluginType']]]):
        pulumi.set(self, "hybrid_aks_plugin_type", value)

    @property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> Optional[pulumi.Input[str]]:
        """
        The default interface name for this L2 network in the virtual machine. This name can be overridden by the name supplied in the network attachment configuration of that virtual machine.
        """
        return pulumi.get(self, "interface_name")

    @interface_name.setter
    def interface_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_name", value)

    @property
    @pulumi.getter(name="l2NetworkName")
    def l2_network_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the L2 network.
        """
        return pulumi.get(self, "l2_network_name")

    @l2_network_name.setter
    def l2_network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "l2_network_name", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class L2Network(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hybrid_aks_plugin_type: Optional[pulumi.Input[Union[str, 'HybridAksPluginType']]] = None,
                 interface_name: Optional[pulumi.Input[str]] = None,
                 l2_isolation_domain_id: Optional[pulumi.Input[str]] = None,
                 l2_network_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Create a L2Network resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[Union[str, 'HybridAksPluginType']] hybrid_aks_plugin_type: Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS.
        :param pulumi.Input[str] interface_name: The default interface name for this L2 network in the virtual machine. This name can be overridden by the name supplied in the network attachment configuration of that virtual machine.
        :param pulumi.Input[str] l2_isolation_domain_id: The resource ID of the Network Fabric l2IsolationDomain.
        :param pulumi.Input[str] l2_network_name: The name of the L2 network.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: L2NetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a L2Network resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param L2NetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(L2NetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 hybrid_aks_plugin_type: Optional[pulumi.Input[Union[str, 'HybridAksPluginType']]] = None,
                 interface_name: Optional[pulumi.Input[str]] = None,
                 l2_isolation_domain_id: Optional[pulumi.Input[str]] = None,
                 l2_network_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = L2NetworkArgs.__new__(L2NetworkArgs)

            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            if hybrid_aks_plugin_type is None:
                hybrid_aks_plugin_type = 'SRIOV'
            __props__.__dict__["hybrid_aks_plugin_type"] = hybrid_aks_plugin_type
            __props__.__dict__["interface_name"] = interface_name
            if l2_isolation_domain_id is None and not opts.urn:
                raise TypeError("Missing required property 'l2_isolation_domain_id'")
            __props__.__dict__["l2_isolation_domain_id"] = l2_isolation_domain_id
            __props__.__dict__["l2_network_name"] = l2_network_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["associated_resource_ids"] = None
            __props__.__dict__["cluster_id"] = None
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["hybrid_aks_clusters_associated_ids"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["virtual_machines_associated_ids"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud:L2Network"), pulumi.Alias(type_="azure-native:networkcloud/v20230701:L2Network")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(L2Network, __self__).__init__(
            'azure-native:networkcloud/v20231001preview:L2Network',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'L2Network':
        """
        Get an existing L2Network resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = L2NetworkArgs.__new__(L2NetworkArgs)

        __props__.__dict__["associated_resource_ids"] = None
        __props__.__dict__["cluster_id"] = None
        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["hybrid_aks_clusters_associated_ids"] = None
        __props__.__dict__["hybrid_aks_plugin_type"] = None
        __props__.__dict__["interface_name"] = None
        __props__.__dict__["l2_isolation_domain_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machines_associated_ids"] = None
        return L2Network(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedResourceIds")
    def associated_resource_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of resource IDs for the other Microsoft.NetworkCloud resources that have attached this network.
        """
        return pulumi.get(self, "associated_resource_ids")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Network Cloud cluster this L2 network is associated with.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The more detailed status of the L2 network.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[str]:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hybridAksClustersAssociatedIds")
    def hybrid_aks_clusters_associated_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Field Deprecated. These fields will be empty/omitted. The list of Hybrid AKS cluster resource ID(s) that are associated with this L2 network.
        """
        return pulumi.get(self, "hybrid_aks_clusters_associated_ids")

    @property
    @pulumi.getter(name="hybridAksPluginType")
    def hybrid_aks_plugin_type(self) -> pulumi.Output[Optional[str]]:
        """
        Field Deprecated. The field was previously optional, now it will have no defined behavior and will be ignored. The network plugin type for Hybrid AKS.
        """
        return pulumi.get(self, "hybrid_aks_plugin_type")

    @property
    @pulumi.getter(name="interfaceName")
    def interface_name(self) -> pulumi.Output[Optional[str]]:
        """
        The default interface name for this L2 network in the virtual machine. This name can be overridden by the name supplied in the network attachment configuration of that virtual machine.
        """
        return pulumi.get(self, "interface_name")

    @property
    @pulumi.getter(name="l2IsolationDomainId")
    def l2_isolation_domain_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the Network Fabric l2IsolationDomain.
        """
        return pulumi.get(self, "l2_isolation_domain_id")

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
        The provisioning state of the L2 network.
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
    @pulumi.getter(name="virtualMachinesAssociatedIds")
    def virtual_machines_associated_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Field Deprecated. These fields will be empty/omitted. The list of virtual machine resource ID(s), excluding any Hybrid AKS virtual machines, that are currently using this L2 network.
        """
        return pulumi.get(self, "virtual_machines_associated_ids")

