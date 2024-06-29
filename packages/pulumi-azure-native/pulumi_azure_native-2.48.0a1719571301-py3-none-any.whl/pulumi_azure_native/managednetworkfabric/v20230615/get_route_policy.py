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

__all__ = [
    'GetRoutePolicyResult',
    'AwaitableGetRoutePolicyResult',
    'get_route_policy',
    'get_route_policy_output',
]

@pulumi.output_type
class GetRoutePolicyResult:
    """
    The RoutePolicy resource definition.
    """
    def __init__(__self__, address_family_type=None, administrative_state=None, annotation=None, configuration_state=None, default_action=None, id=None, location=None, name=None, network_fabric_id=None, provisioning_state=None, statements=None, system_data=None, tags=None, type=None):
        if address_family_type and not isinstance(address_family_type, str):
            raise TypeError("Expected argument 'address_family_type' to be a str")
        pulumi.set(__self__, "address_family_type", address_family_type)
        if administrative_state and not isinstance(administrative_state, str):
            raise TypeError("Expected argument 'administrative_state' to be a str")
        pulumi.set(__self__, "administrative_state", administrative_state)
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if configuration_state and not isinstance(configuration_state, str):
            raise TypeError("Expected argument 'configuration_state' to be a str")
        pulumi.set(__self__, "configuration_state", configuration_state)
        if default_action and not isinstance(default_action, str):
            raise TypeError("Expected argument 'default_action' to be a str")
        pulumi.set(__self__, "default_action", default_action)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_fabric_id and not isinstance(network_fabric_id, str):
            raise TypeError("Expected argument 'network_fabric_id' to be a str")
        pulumi.set(__self__, "network_fabric_id", network_fabric_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if statements and not isinstance(statements, list):
            raise TypeError("Expected argument 'statements' to be a list")
        pulumi.set(__self__, "statements", statements)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="addressFamilyType")
    def address_family_type(self) -> Optional[str]:
        """
        AddressFamilyType. This parameter decides whether the given ipv4 or ipv6 route policy.
        """
        return pulumi.get(self, "address_family_type")

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> str:
        """
        Administrative state of the resource.
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> str:
        """
        Configuration state of the resource.
        """
        return pulumi.get(self, "configuration_state")

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[str]:
        """
        Default action that needs to be applied when no condition is matched. Example: Permit | Deny.
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> str:
        """
        Arm Resource ID of Network Fabric.
        """
        return pulumi.get(self, "network_fabric_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def statements(self) -> Sequence['outputs.RoutePolicyStatementPropertiesResponse']:
        """
        Route Policy statements.
        """
        return pulumi.get(self, "statements")

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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetRoutePolicyResult(GetRoutePolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoutePolicyResult(
            address_family_type=self.address_family_type,
            administrative_state=self.administrative_state,
            annotation=self.annotation,
            configuration_state=self.configuration_state,
            default_action=self.default_action,
            id=self.id,
            location=self.location,
            name=self.name,
            network_fabric_id=self.network_fabric_id,
            provisioning_state=self.provisioning_state,
            statements=self.statements,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_route_policy(resource_group_name: Optional[str] = None,
                     route_policy_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoutePolicyResult:
    """
    Implements Route Policy GET method.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str route_policy_name: Name of the Route Policy.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['routePolicyName'] = route_policy_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric/v20230615:getRoutePolicy', __args__, opts=opts, typ=GetRoutePolicyResult).value

    return AwaitableGetRoutePolicyResult(
        address_family_type=pulumi.get(__ret__, 'address_family_type'),
        administrative_state=pulumi.get(__ret__, 'administrative_state'),
        annotation=pulumi.get(__ret__, 'annotation'),
        configuration_state=pulumi.get(__ret__, 'configuration_state'),
        default_action=pulumi.get(__ret__, 'default_action'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_fabric_id=pulumi.get(__ret__, 'network_fabric_id'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        statements=pulumi.get(__ret__, 'statements'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_route_policy)
def get_route_policy_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                            route_policy_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoutePolicyResult]:
    """
    Implements Route Policy GET method.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str route_policy_name: Name of the Route Policy.
    """
    ...
