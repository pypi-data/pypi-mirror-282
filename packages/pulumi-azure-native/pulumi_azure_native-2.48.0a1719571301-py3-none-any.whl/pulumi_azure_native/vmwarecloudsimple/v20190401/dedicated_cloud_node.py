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

__all__ = ['DedicatedCloudNodeArgs', 'DedicatedCloudNode']

@pulumi.input_type
class DedicatedCloudNodeArgs:
    def __init__(__self__, *,
                 availability_zone_id: pulumi.Input[str],
                 id: pulumi.Input[str],
                 name: pulumi.Input[str],
                 nodes_count: pulumi.Input[int],
                 placement_group_id: pulumi.Input[str],
                 purchase_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 dedicated_cloud_node_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DedicatedCloudNode resource.
        :param pulumi.Input[str] availability_zone_id: Availability Zone id, e.g. "az1"
        :param pulumi.Input[str] id: SKU's id
        :param pulumi.Input[str] name: SKU's name
        :param pulumi.Input[int] nodes_count: count of nodes to create
        :param pulumi.Input[str] placement_group_id: Placement Group id, e.g. "n1"
        :param pulumi.Input[str] purchase_id: purchase id
        :param pulumi.Input[str] resource_group_name: The name of the resource group
        :param pulumi.Input[str] dedicated_cloud_node_name: dedicated cloud node name
        :param pulumi.Input[str] location: Azure region
        :param pulumi.Input['SkuArgs'] sku: Dedicated Cloud Nodes SKU
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Dedicated Cloud Nodes tags
        """
        pulumi.set(__self__, "availability_zone_id", availability_zone_id)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "nodes_count", nodes_count)
        pulumi.set(__self__, "placement_group_id", placement_group_id)
        pulumi.set(__self__, "purchase_id", purchase_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dedicated_cloud_node_name is not None:
            pulumi.set(__self__, "dedicated_cloud_node_name", dedicated_cloud_node_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Input[str]:
        """
        Availability Zone id, e.g. "az1"
        """
        return pulumi.get(self, "availability_zone_id")

    @availability_zone_id.setter
    def availability_zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "availability_zone_id", value)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        SKU's id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        SKU's name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodesCount")
    def nodes_count(self) -> pulumi.Input[int]:
        """
        count of nodes to create
        """
        return pulumi.get(self, "nodes_count")

    @nodes_count.setter
    def nodes_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "nodes_count", value)

    @property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> pulumi.Input[str]:
        """
        Placement Group id, e.g. "n1"
        """
        return pulumi.get(self, "placement_group_id")

    @placement_group_id.setter
    def placement_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "placement_group_id", value)

    @property
    @pulumi.getter(name="purchaseId")
    def purchase_id(self) -> pulumi.Input[str]:
        """
        purchase id
        """
        return pulumi.get(self, "purchase_id")

    @purchase_id.setter
    def purchase_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "purchase_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dedicatedCloudNodeName")
    def dedicated_cloud_node_name(self) -> Optional[pulumi.Input[str]]:
        """
        dedicated cloud node name
        """
        return pulumi.get(self, "dedicated_cloud_node_name")

    @dedicated_cloud_node_name.setter
    def dedicated_cloud_node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dedicated_cloud_node_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Azure region
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        Dedicated Cloud Nodes SKU
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Dedicated Cloud Nodes tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DedicatedCloudNode(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone_id: Optional[pulumi.Input[str]] = None,
                 dedicated_cloud_node_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nodes_count: Optional[pulumi.Input[int]] = None,
                 placement_group_id: Optional[pulumi.Input[str]] = None,
                 purchase_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Dedicated cloud node model

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] availability_zone_id: Availability Zone id, e.g. "az1"
        :param pulumi.Input[str] dedicated_cloud_node_name: dedicated cloud node name
        :param pulumi.Input[str] id: SKU's id
        :param pulumi.Input[str] location: Azure region
        :param pulumi.Input[str] name: SKU's name
        :param pulumi.Input[int] nodes_count: count of nodes to create
        :param pulumi.Input[str] placement_group_id: Placement Group id, e.g. "n1"
        :param pulumi.Input[str] purchase_id: purchase id
        :param pulumi.Input[str] resource_group_name: The name of the resource group
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: Dedicated Cloud Nodes SKU
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Dedicated Cloud Nodes tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DedicatedCloudNodeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Dedicated cloud node model

        :param str resource_name: The name of the resource.
        :param DedicatedCloudNodeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DedicatedCloudNodeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 availability_zone_id: Optional[pulumi.Input[str]] = None,
                 dedicated_cloud_node_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nodes_count: Optional[pulumi.Input[int]] = None,
                 placement_group_id: Optional[pulumi.Input[str]] = None,
                 purchase_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DedicatedCloudNodeArgs.__new__(DedicatedCloudNodeArgs)

            if availability_zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'availability_zone_id'")
            __props__.__dict__["availability_zone_id"] = availability_zone_id
            __props__.__dict__["dedicated_cloud_node_name"] = dedicated_cloud_node_name
            if id is None and not opts.urn:
                raise TypeError("Missing required property 'id'")
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if nodes_count is None and not opts.urn:
                raise TypeError("Missing required property 'nodes_count'")
            __props__.__dict__["nodes_count"] = nodes_count
            if placement_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'placement_group_id'")
            __props__.__dict__["placement_group_id"] = placement_group_id
            if purchase_id is None and not opts.urn:
                raise TypeError("Missing required property 'purchase_id'")
            __props__.__dict__["purchase_id"] = purchase_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["availability_zone_name"] = None
            __props__.__dict__["cloud_rack_name"] = None
            __props__.__dict__["created"] = None
            __props__.__dict__["placement_group_name"] = None
            __props__.__dict__["private_cloud_id"] = None
            __props__.__dict__["private_cloud_name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["vmware_cluster_name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:vmwarecloudsimple:DedicatedCloudNode")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DedicatedCloudNode, __self__).__init__(
            'azure-native:vmwarecloudsimple/v20190401:DedicatedCloudNode',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DedicatedCloudNode':
        """
        Get an existing DedicatedCloudNode resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DedicatedCloudNodeArgs.__new__(DedicatedCloudNodeArgs)

        __props__.__dict__["availability_zone_id"] = None
        __props__.__dict__["availability_zone_name"] = None
        __props__.__dict__["cloud_rack_name"] = None
        __props__.__dict__["created"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["nodes_count"] = None
        __props__.__dict__["placement_group_id"] = None
        __props__.__dict__["placement_group_name"] = None
        __props__.__dict__["private_cloud_id"] = None
        __props__.__dict__["private_cloud_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["purchase_id"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vmware_cluster_name"] = None
        return DedicatedCloudNode(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availabilityZoneId")
    def availability_zone_id(self) -> pulumi.Output[str]:
        """
        Availability Zone id, e.g. "az1"
        """
        return pulumi.get(self, "availability_zone_id")

    @property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> pulumi.Output[str]:
        """
        Availability Zone name, e.g. "Availability Zone 1"
        """
        return pulumi.get(self, "availability_zone_name")

    @property
    @pulumi.getter(name="cloudRackName")
    def cloud_rack_name(self) -> pulumi.Output[str]:
        """
        VMWare Cloud Rack Name
        """
        return pulumi.get(self, "cloud_rack_name")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        date time the resource was created
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Azure region
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        SKU's name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodesCount")
    def nodes_count(self) -> pulumi.Output[int]:
        """
        count of nodes to create
        """
        return pulumi.get(self, "nodes_count")

    @property
    @pulumi.getter(name="placementGroupId")
    def placement_group_id(self) -> pulumi.Output[str]:
        """
        Placement Group id, e.g. "n1"
        """
        return pulumi.get(self, "placement_group_id")

    @property
    @pulumi.getter(name="placementGroupName")
    def placement_group_name(self) -> pulumi.Output[str]:
        """
        Placement Name, e.g. "Placement Group 1"
        """
        return pulumi.get(self, "placement_group_name")

    @property
    @pulumi.getter(name="privateCloudId")
    def private_cloud_id(self) -> pulumi.Output[str]:
        """
        Private Cloud Id
        """
        return pulumi.get(self, "private_cloud_id")

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Output[str]:
        """
        Resource Pool Name
        """
        return pulumi.get(self, "private_cloud_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning status of the resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="purchaseId")
    def purchase_id(self) -> pulumi.Output[str]:
        """
        purchase id
        """
        return pulumi.get(self, "purchase_id")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        Dedicated Cloud Nodes SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Node status, indicates is private cloud set up on this node or not
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Dedicated Cloud Nodes tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        {resourceProviderNamespace}/{resourceType}
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmwareClusterName")
    def vmware_cluster_name(self) -> pulumi.Output[str]:
        """
        VMWare Cluster Name
        """
        return pulumi.get(self, "vmware_cluster_name")

