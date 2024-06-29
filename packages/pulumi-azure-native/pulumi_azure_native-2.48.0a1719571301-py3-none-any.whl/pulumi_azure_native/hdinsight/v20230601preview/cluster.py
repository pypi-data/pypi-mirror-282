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

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 cluster_pool_name: pulumi.Input[str],
                 cluster_profile: pulumi.Input['ClusterProfileArgs'],
                 cluster_type: pulumi.Input[str],
                 compute_profile: pulumi.Input['ComputeProfileArgs'],
                 resource_group_name: pulumi.Input[str],
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input[str] cluster_pool_name: The name of the cluster pool.
        :param pulumi.Input['ClusterProfileArgs'] cluster_profile: Cluster profile.
        :param pulumi.Input[str] cluster_type: The type of cluster.
        :param pulumi.Input['ComputeProfileArgs'] compute_profile: The compute profile.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] cluster_name: The name of the HDInsight cluster.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "cluster_pool_name", cluster_pool_name)
        pulumi.set(__self__, "cluster_profile", cluster_profile)
        pulumi.set(__self__, "cluster_type", cluster_type)
        pulumi.set(__self__, "compute_profile", compute_profile)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="clusterPoolName")
    def cluster_pool_name(self) -> pulumi.Input[str]:
        """
        The name of the cluster pool.
        """
        return pulumi.get(self, "cluster_pool_name")

    @cluster_pool_name.setter
    def cluster_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_pool_name", value)

    @property
    @pulumi.getter(name="clusterProfile")
    def cluster_profile(self) -> pulumi.Input['ClusterProfileArgs']:
        """
        Cluster profile.
        """
        return pulumi.get(self, "cluster_profile")

    @cluster_profile.setter
    def cluster_profile(self, value: pulumi.Input['ClusterProfileArgs']):
        pulumi.set(self, "cluster_profile", value)

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Input[str]:
        """
        The type of cluster.
        """
        return pulumi.get(self, "cluster_type")

    @cluster_type.setter
    def cluster_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_type", value)

    @property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> pulumi.Input['ComputeProfileArgs']:
        """
        The compute profile.
        """
        return pulumi.get(self, "compute_profile")

    @compute_profile.setter
    def compute_profile(self, value: pulumi.Input['ComputeProfileArgs']):
        pulumi.set(self, "compute_profile", value)

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
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the HDInsight cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

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


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_pool_name: Optional[pulumi.Input[str]] = None,
                 cluster_profile: Optional[pulumi.Input[pulumi.InputType['ClusterProfileArgs']]] = None,
                 cluster_type: Optional[pulumi.Input[str]] = None,
                 compute_profile: Optional[pulumi.Input[pulumi.InputType['ComputeProfileArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the HDInsight cluster.
        :param pulumi.Input[str] cluster_pool_name: The name of the cluster pool.
        :param pulumi.Input[pulumi.InputType['ClusterProfileArgs']] cluster_profile: Cluster profile.
        :param pulumi.Input[str] cluster_type: The type of cluster.
        :param pulumi.Input[pulumi.InputType['ComputeProfileArgs']] compute_profile: The compute profile.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The cluster.

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_pool_name: Optional[pulumi.Input[str]] = None,
                 cluster_profile: Optional[pulumi.Input[pulumi.InputType['ClusterProfileArgs']]] = None,
                 cluster_type: Optional[pulumi.Input[str]] = None,
                 compute_profile: Optional[pulumi.Input[pulumi.InputType['ComputeProfileArgs']]] = None,
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
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["cluster_name"] = cluster_name
            if cluster_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_pool_name'")
            __props__.__dict__["cluster_pool_name"] = cluster_pool_name
            if cluster_profile is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_profile'")
            __props__.__dict__["cluster_profile"] = cluster_profile
            if cluster_type is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_type'")
            __props__.__dict__["cluster_type"] = cluster_type
            if compute_profile is None and not opts.urn:
                raise TypeError("Missing required property 'compute_profile'")
            __props__.__dict__["compute_profile"] = compute_profile
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["deployment_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hdinsight/v20231101preview:Cluster"), pulumi.Alias(type_="azure-native:hdinsight/v20240501preview:Cluster")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Cluster, __self__).__init__(
            'azure-native:hdinsight/v20230601preview:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["cluster_profile"] = None
        __props__.__dict__["cluster_type"] = None
        __props__.__dict__["compute_profile"] = None
        __props__.__dict__["deployment_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterProfile")
    def cluster_profile(self) -> pulumi.Output['outputs.ClusterProfileResponse']:
        """
        Cluster profile.
        """
        return pulumi.get(self, "cluster_profile")

    @property
    @pulumi.getter(name="clusterType")
    def cluster_type(self) -> pulumi.Output[str]:
        """
        The type of cluster.
        """
        return pulumi.get(self, "cluster_type")

    @property
    @pulumi.getter(name="computeProfile")
    def compute_profile(self) -> pulumi.Output['outputs.ComputeProfileResponse']:
        """
        The compute profile.
        """
        return pulumi.get(self, "compute_profile")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        A unique id generated by the RP to identify the resource.
        """
        return pulumi.get(self, "deployment_id")

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
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Business status of the resource.
        """
        return pulumi.get(self, "status")

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

