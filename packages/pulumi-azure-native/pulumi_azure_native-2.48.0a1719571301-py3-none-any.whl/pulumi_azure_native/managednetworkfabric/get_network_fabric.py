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

__all__ = [
    'GetNetworkFabricResult',
    'AwaitableGetNetworkFabricResult',
    'get_network_fabric',
    'get_network_fabric_output',
]

@pulumi.output_type
class GetNetworkFabricResult:
    """
    The NetworkFabric resource definition.
    """
    def __init__(__self__, annotation=None, fabric_asn=None, id=None, ipv4_prefix=None, ipv6_prefix=None, l2_isolation_domains=None, l3_isolation_domains=None, location=None, management_network_configuration=None, name=None, network_fabric_controller_id=None, network_fabric_sku=None, operational_state=None, provisioning_state=None, rack_count=None, racks=None, router_id=None, server_count_per_rack=None, system_data=None, tags=None, terminal_server_configuration=None, type=None):
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if fabric_asn and not isinstance(fabric_asn, int):
            raise TypeError("Expected argument 'fabric_asn' to be a int")
        pulumi.set(__self__, "fabric_asn", fabric_asn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv4_prefix and not isinstance(ipv4_prefix, str):
            raise TypeError("Expected argument 'ipv4_prefix' to be a str")
        pulumi.set(__self__, "ipv4_prefix", ipv4_prefix)
        if ipv6_prefix and not isinstance(ipv6_prefix, str):
            raise TypeError("Expected argument 'ipv6_prefix' to be a str")
        pulumi.set(__self__, "ipv6_prefix", ipv6_prefix)
        if l2_isolation_domains and not isinstance(l2_isolation_domains, list):
            raise TypeError("Expected argument 'l2_isolation_domains' to be a list")
        pulumi.set(__self__, "l2_isolation_domains", l2_isolation_domains)
        if l3_isolation_domains and not isinstance(l3_isolation_domains, list):
            raise TypeError("Expected argument 'l3_isolation_domains' to be a list")
        pulumi.set(__self__, "l3_isolation_domains", l3_isolation_domains)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if management_network_configuration and not isinstance(management_network_configuration, dict):
            raise TypeError("Expected argument 'management_network_configuration' to be a dict")
        pulumi.set(__self__, "management_network_configuration", management_network_configuration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_fabric_controller_id and not isinstance(network_fabric_controller_id, str):
            raise TypeError("Expected argument 'network_fabric_controller_id' to be a str")
        pulumi.set(__self__, "network_fabric_controller_id", network_fabric_controller_id)
        if network_fabric_sku and not isinstance(network_fabric_sku, str):
            raise TypeError("Expected argument 'network_fabric_sku' to be a str")
        pulumi.set(__self__, "network_fabric_sku", network_fabric_sku)
        if operational_state and not isinstance(operational_state, str):
            raise TypeError("Expected argument 'operational_state' to be a str")
        pulumi.set(__self__, "operational_state", operational_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rack_count and not isinstance(rack_count, int):
            raise TypeError("Expected argument 'rack_count' to be a int")
        pulumi.set(__self__, "rack_count", rack_count)
        if racks and not isinstance(racks, list):
            raise TypeError("Expected argument 'racks' to be a list")
        pulumi.set(__self__, "racks", racks)
        if router_id and not isinstance(router_id, str):
            raise TypeError("Expected argument 'router_id' to be a str")
        pulumi.set(__self__, "router_id", router_id)
        if server_count_per_rack and not isinstance(server_count_per_rack, int):
            raise TypeError("Expected argument 'server_count_per_rack' to be a int")
        pulumi.set(__self__, "server_count_per_rack", server_count_per_rack)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if terminal_server_configuration and not isinstance(terminal_server_configuration, dict):
            raise TypeError("Expected argument 'terminal_server_configuration' to be a dict")
        pulumi.set(__self__, "terminal_server_configuration", terminal_server_configuration)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="fabricASN")
    def fabric_asn(self) -> int:
        """
        ASN of CE devices for CE/PE connectivity.
        """
        return pulumi.get(self, "fabric_asn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv4Prefix")
    def ipv4_prefix(self) -> Optional[str]:
        """
        IPv4Prefix for Management Network. Example: 10.1.0.0/19.
        """
        return pulumi.get(self, "ipv4_prefix")

    @property
    @pulumi.getter(name="ipv6Prefix")
    def ipv6_prefix(self) -> Optional[str]:
        """
        IPv6Prefix for Management Network. Example: 3FFE:FFFF:0:CD40::/59.
        """
        return pulumi.get(self, "ipv6_prefix")

    @property
    @pulumi.getter(name="l2IsolationDomains")
    def l2_isolation_domains(self) -> Sequence[str]:
        """
        List of L2IsolationDomain resource IDs under the Network Fabric.
        """
        return pulumi.get(self, "l2_isolation_domains")

    @property
    @pulumi.getter(name="l3IsolationDomains")
    def l3_isolation_domains(self) -> Sequence[str]:
        """
        List of L3IsolationDomain resource IDs under the Network Fabric.
        """
        return pulumi.get(self, "l3_isolation_domains")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementNetworkConfiguration")
    def management_network_configuration(self) -> 'outputs.ManagementNetworkConfigurationResponse':
        """
        Configuration to be used to setup the management network.
        """
        return pulumi.get(self, "management_network_configuration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFabricControllerId")
    def network_fabric_controller_id(self) -> str:
        """
        Azure resource ID for the NetworkFabricController the NetworkFabric belongs.
        """
        return pulumi.get(self, "network_fabric_controller_id")

    @property
    @pulumi.getter(name="networkFabricSku")
    def network_fabric_sku(self) -> str:
        """
        Supported Network Fabric SKU.Example: Compute / Aggregate racks. Once the user chooses a particular SKU, only supported racks can be added to the Network Fabric. The SKU determines whether it is a single / multi rack Network Fabric.
        """
        return pulumi.get(self, "network_fabric_sku")

    @property
    @pulumi.getter(name="operationalState")
    def operational_state(self) -> str:
        """
        Gets the operational state of the resource.
        """
        return pulumi.get(self, "operational_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rackCount")
    def rack_count(self) -> int:
        """
        Number of racks associated to Network Fabric.Possible values are from 2-8.
        """
        return pulumi.get(self, "rack_count")

    @property
    @pulumi.getter
    def racks(self) -> Sequence[str]:
        """
        List of NetworkRack resource IDs under the Network Fabric. The number of racks allowed depends on the Network Fabric SKU.
        """
        return pulumi.get(self, "racks")

    @property
    @pulumi.getter(name="routerId")
    def router_id(self) -> str:
        """
        Router Id of CE to be used for MP-BGP between PE and CE
        """
        return pulumi.get(self, "router_id")

    @property
    @pulumi.getter(name="serverCountPerRack")
    def server_count_per_rack(self) -> int:
        """
        Number of servers.Possible values are from 1-16.
        """
        return pulumi.get(self, "server_count_per_rack")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="terminalServerConfiguration")
    def terminal_server_configuration(self) -> 'outputs.TerminalServerConfigurationResponse':
        """
        Network and credentials configuration currently applied to terminal server.
        """
        return pulumi.get(self, "terminal_server_configuration")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetNetworkFabricResult(GetNetworkFabricResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkFabricResult(
            annotation=self.annotation,
            fabric_asn=self.fabric_asn,
            id=self.id,
            ipv4_prefix=self.ipv4_prefix,
            ipv6_prefix=self.ipv6_prefix,
            l2_isolation_domains=self.l2_isolation_domains,
            l3_isolation_domains=self.l3_isolation_domains,
            location=self.location,
            management_network_configuration=self.management_network_configuration,
            name=self.name,
            network_fabric_controller_id=self.network_fabric_controller_id,
            network_fabric_sku=self.network_fabric_sku,
            operational_state=self.operational_state,
            provisioning_state=self.provisioning_state,
            rack_count=self.rack_count,
            racks=self.racks,
            router_id=self.router_id,
            server_count_per_rack=self.server_count_per_rack,
            system_data=self.system_data,
            tags=self.tags,
            terminal_server_configuration=self.terminal_server_configuration,
            type=self.type)


def get_network_fabric(network_fabric_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkFabricResult:
    """
    Get Network Fabric resource details.
    Azure REST API version: 2023-02-01-preview.

    Other available API versions: 2023-06-15.


    :param str network_fabric_name: Name of the Network Fabric
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['networkFabricName'] = network_fabric_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric:getNetworkFabric', __args__, opts=opts, typ=GetNetworkFabricResult).value

    return AwaitableGetNetworkFabricResult(
        annotation=pulumi.get(__ret__, 'annotation'),
        fabric_asn=pulumi.get(__ret__, 'fabric_asn'),
        id=pulumi.get(__ret__, 'id'),
        ipv4_prefix=pulumi.get(__ret__, 'ipv4_prefix'),
        ipv6_prefix=pulumi.get(__ret__, 'ipv6_prefix'),
        l2_isolation_domains=pulumi.get(__ret__, 'l2_isolation_domains'),
        l3_isolation_domains=pulumi.get(__ret__, 'l3_isolation_domains'),
        location=pulumi.get(__ret__, 'location'),
        management_network_configuration=pulumi.get(__ret__, 'management_network_configuration'),
        name=pulumi.get(__ret__, 'name'),
        network_fabric_controller_id=pulumi.get(__ret__, 'network_fabric_controller_id'),
        network_fabric_sku=pulumi.get(__ret__, 'network_fabric_sku'),
        operational_state=pulumi.get(__ret__, 'operational_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rack_count=pulumi.get(__ret__, 'rack_count'),
        racks=pulumi.get(__ret__, 'racks'),
        router_id=pulumi.get(__ret__, 'router_id'),
        server_count_per_rack=pulumi.get(__ret__, 'server_count_per_rack'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        terminal_server_configuration=pulumi.get(__ret__, 'terminal_server_configuration'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_network_fabric)
def get_network_fabric_output(network_fabric_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkFabricResult]:
    """
    Get Network Fabric resource details.
    Azure REST API version: 2023-02-01-preview.

    Other available API versions: 2023-06-15.


    :param str network_fabric_name: Name of the Network Fabric
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
