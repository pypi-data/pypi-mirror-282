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
    'GetAvailabilityGroupListenerResult',
    'AwaitableGetAvailabilityGroupListenerResult',
    'get_availability_group_listener',
    'get_availability_group_listener_output',
]

@pulumi.output_type
class GetAvailabilityGroupListenerResult:
    """
    A SQL Server availability group listener.
    """
    def __init__(__self__, availability_group_configuration=None, availability_group_name=None, create_default_availability_group_if_not_exist=None, id=None, load_balancer_configurations=None, multi_subnet_ip_configurations=None, name=None, port=None, provisioning_state=None, system_data=None, type=None):
        if availability_group_configuration and not isinstance(availability_group_configuration, dict):
            raise TypeError("Expected argument 'availability_group_configuration' to be a dict")
        pulumi.set(__self__, "availability_group_configuration", availability_group_configuration)
        if availability_group_name and not isinstance(availability_group_name, str):
            raise TypeError("Expected argument 'availability_group_name' to be a str")
        pulumi.set(__self__, "availability_group_name", availability_group_name)
        if create_default_availability_group_if_not_exist and not isinstance(create_default_availability_group_if_not_exist, bool):
            raise TypeError("Expected argument 'create_default_availability_group_if_not_exist' to be a bool")
        pulumi.set(__self__, "create_default_availability_group_if_not_exist", create_default_availability_group_if_not_exist)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if load_balancer_configurations and not isinstance(load_balancer_configurations, list):
            raise TypeError("Expected argument 'load_balancer_configurations' to be a list")
        pulumi.set(__self__, "load_balancer_configurations", load_balancer_configurations)
        if multi_subnet_ip_configurations and not isinstance(multi_subnet_ip_configurations, list):
            raise TypeError("Expected argument 'multi_subnet_ip_configurations' to be a list")
        pulumi.set(__self__, "multi_subnet_ip_configurations", multi_subnet_ip_configurations)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="availabilityGroupConfiguration")
    def availability_group_configuration(self) -> Optional['outputs.AgConfigurationResponse']:
        """
        Availability Group configuration.
        """
        return pulumi.get(self, "availability_group_configuration")

    @property
    @pulumi.getter(name="availabilityGroupName")
    def availability_group_name(self) -> Optional[str]:
        """
        Name of the availability group.
        """
        return pulumi.get(self, "availability_group_name")

    @property
    @pulumi.getter(name="createDefaultAvailabilityGroupIfNotExist")
    def create_default_availability_group_if_not_exist(self) -> Optional[bool]:
        """
        Create a default availability group if it does not exist.
        """
        return pulumi.get(self, "create_default_availability_group_if_not_exist")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="loadBalancerConfigurations")
    def load_balancer_configurations(self) -> Optional[Sequence['outputs.LoadBalancerConfigurationResponse']]:
        """
        List of load balancer configurations for an availability group listener.
        """
        return pulumi.get(self, "load_balancer_configurations")

    @property
    @pulumi.getter(name="multiSubnetIpConfigurations")
    def multi_subnet_ip_configurations(self) -> Optional[Sequence['outputs.MultiSubnetIpConfigurationResponse']]:
        """
        List of multi subnet IP configurations for an AG listener.
        """
        return pulumi.get(self, "multi_subnet_ip_configurations")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        Listener port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state to track the async operation status.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetAvailabilityGroupListenerResult(GetAvailabilityGroupListenerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvailabilityGroupListenerResult(
            availability_group_configuration=self.availability_group_configuration,
            availability_group_name=self.availability_group_name,
            create_default_availability_group_if_not_exist=self.create_default_availability_group_if_not_exist,
            id=self.id,
            load_balancer_configurations=self.load_balancer_configurations,
            multi_subnet_ip_configurations=self.multi_subnet_ip_configurations,
            name=self.name,
            port=self.port,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_availability_group_listener(availability_group_listener_name: Optional[str] = None,
                                    expand: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    sql_virtual_machine_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAvailabilityGroupListenerResult:
    """
    Gets an availability group listener.


    :param str availability_group_listener_name: Name of the availability group listener.
    :param str expand: The child resources to include in the response.
    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_virtual_machine_group_name: Name of the SQL virtual machine group.
    """
    __args__ = dict()
    __args__['availabilityGroupListenerName'] = availability_group_listener_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['sqlVirtualMachineGroupName'] = sql_virtual_machine_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sqlvirtualmachine/v20220201:getAvailabilityGroupListener', __args__, opts=opts, typ=GetAvailabilityGroupListenerResult).value

    return AwaitableGetAvailabilityGroupListenerResult(
        availability_group_configuration=pulumi.get(__ret__, 'availability_group_configuration'),
        availability_group_name=pulumi.get(__ret__, 'availability_group_name'),
        create_default_availability_group_if_not_exist=pulumi.get(__ret__, 'create_default_availability_group_if_not_exist'),
        id=pulumi.get(__ret__, 'id'),
        load_balancer_configurations=pulumi.get(__ret__, 'load_balancer_configurations'),
        multi_subnet_ip_configurations=pulumi.get(__ret__, 'multi_subnet_ip_configurations'),
        name=pulumi.get(__ret__, 'name'),
        port=pulumi.get(__ret__, 'port'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_availability_group_listener)
def get_availability_group_listener_output(availability_group_listener_name: Optional[pulumi.Input[str]] = None,
                                           expand: Optional[pulumi.Input[Optional[str]]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           sql_virtual_machine_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAvailabilityGroupListenerResult]:
    """
    Gets an availability group listener.


    :param str availability_group_listener_name: Name of the availability group listener.
    :param str expand: The child resources to include in the response.
    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_virtual_machine_group_name: Name of the SQL virtual machine group.
    """
    ...
