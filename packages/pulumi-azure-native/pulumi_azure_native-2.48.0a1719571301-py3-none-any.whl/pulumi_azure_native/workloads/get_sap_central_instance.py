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
    'GetSAPCentralInstanceResult',
    'AwaitableGetSAPCentralInstanceResult',
    'get_sap_central_instance',
    'get_sap_central_instance_output',
]

@pulumi.output_type
class GetSAPCentralInstanceResult:
    """
    Define the SAP Central Services Instance resource.
    """
    def __init__(__self__, enqueue_replication_server_properties=None, enqueue_server_properties=None, errors=None, gateway_server_properties=None, health=None, id=None, instance_no=None, kernel_patch=None, kernel_version=None, load_balancer_details=None, location=None, message_server_properties=None, name=None, provisioning_state=None, status=None, subnet=None, system_data=None, tags=None, type=None, vm_details=None):
        if enqueue_replication_server_properties and not isinstance(enqueue_replication_server_properties, dict):
            raise TypeError("Expected argument 'enqueue_replication_server_properties' to be a dict")
        pulumi.set(__self__, "enqueue_replication_server_properties", enqueue_replication_server_properties)
        if enqueue_server_properties and not isinstance(enqueue_server_properties, dict):
            raise TypeError("Expected argument 'enqueue_server_properties' to be a dict")
        pulumi.set(__self__, "enqueue_server_properties", enqueue_server_properties)
        if errors and not isinstance(errors, dict):
            raise TypeError("Expected argument 'errors' to be a dict")
        pulumi.set(__self__, "errors", errors)
        if gateway_server_properties and not isinstance(gateway_server_properties, dict):
            raise TypeError("Expected argument 'gateway_server_properties' to be a dict")
        pulumi.set(__self__, "gateway_server_properties", gateway_server_properties)
        if health and not isinstance(health, str):
            raise TypeError("Expected argument 'health' to be a str")
        pulumi.set(__self__, "health", health)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_no and not isinstance(instance_no, str):
            raise TypeError("Expected argument 'instance_no' to be a str")
        pulumi.set(__self__, "instance_no", instance_no)
        if kernel_patch and not isinstance(kernel_patch, str):
            raise TypeError("Expected argument 'kernel_patch' to be a str")
        pulumi.set(__self__, "kernel_patch", kernel_patch)
        if kernel_version and not isinstance(kernel_version, str):
            raise TypeError("Expected argument 'kernel_version' to be a str")
        pulumi.set(__self__, "kernel_version", kernel_version)
        if load_balancer_details and not isinstance(load_balancer_details, dict):
            raise TypeError("Expected argument 'load_balancer_details' to be a dict")
        pulumi.set(__self__, "load_balancer_details", load_balancer_details)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if message_server_properties and not isinstance(message_server_properties, dict):
            raise TypeError("Expected argument 'message_server_properties' to be a dict")
        pulumi.set(__self__, "message_server_properties", message_server_properties)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subnet and not isinstance(subnet, str):
            raise TypeError("Expected argument 'subnet' to be a str")
        pulumi.set(__self__, "subnet", subnet)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_details and not isinstance(vm_details, list):
            raise TypeError("Expected argument 'vm_details' to be a list")
        pulumi.set(__self__, "vm_details", vm_details)

    @property
    @pulumi.getter(name="enqueueReplicationServerProperties")
    def enqueue_replication_server_properties(self) -> Optional['outputs.EnqueueReplicationServerPropertiesResponse']:
        """
        Defines the SAP Enqueue Replication Server (ERS) properties.
        """
        return pulumi.get(self, "enqueue_replication_server_properties")

    @property
    @pulumi.getter(name="enqueueServerProperties")
    def enqueue_server_properties(self) -> Optional['outputs.EnqueueServerPropertiesResponse']:
        """
        Defines the SAP Enqueue Server properties.
        """
        return pulumi.get(self, "enqueue_server_properties")

    @property
    @pulumi.getter
    def errors(self) -> 'outputs.SAPVirtualInstanceErrorResponse':
        """
        Defines the errors related to SAP Central Services Instance resource.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter(name="gatewayServerProperties")
    def gateway_server_properties(self) -> Optional['outputs.GatewayServerPropertiesResponse']:
        """
        Defines the SAP Gateway Server properties.
        """
        return pulumi.get(self, "gateway_server_properties")

    @property
    @pulumi.getter
    def health(self) -> str:
        """
        Defines the health of SAP Instances.
        """
        return pulumi.get(self, "health")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceNo")
    def instance_no(self) -> str:
        """
        The central services instance number.
        """
        return pulumi.get(self, "instance_no")

    @property
    @pulumi.getter(name="kernelPatch")
    def kernel_patch(self) -> str:
        """
        The central services instance Kernel Patch level.
        """
        return pulumi.get(self, "kernel_patch")

    @property
    @pulumi.getter(name="kernelVersion")
    def kernel_version(self) -> str:
        """
        The central services instance Kernel Version.
        """
        return pulumi.get(self, "kernel_version")

    @property
    @pulumi.getter(name="loadBalancerDetails")
    def load_balancer_details(self) -> 'outputs.LoadBalancerDetailsResponse':
        """
        The Load Balancer details such as LoadBalancer ID attached to ASCS Virtual Machines
        """
        return pulumi.get(self, "load_balancer_details")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="messageServerProperties")
    def message_server_properties(self) -> Optional['outputs.MessageServerPropertiesResponse']:
        """
        Defines the SAP Message Server properties.
        """
        return pulumi.get(self, "message_server_properties")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Defines the provisioning states.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Defines the SAP Instance status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnet(self) -> str:
        """
        The central services instance subnet.
        """
        return pulumi.get(self, "subnet")

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

    @property
    @pulumi.getter(name="vmDetails")
    def vm_details(self) -> Sequence['outputs.CentralServerVmDetailsResponse']:
        """
        The list of virtual machines corresponding to the Central Services instance.
        """
        return pulumi.get(self, "vm_details")


class AwaitableGetSAPCentralInstanceResult(GetSAPCentralInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSAPCentralInstanceResult(
            enqueue_replication_server_properties=self.enqueue_replication_server_properties,
            enqueue_server_properties=self.enqueue_server_properties,
            errors=self.errors,
            gateway_server_properties=self.gateway_server_properties,
            health=self.health,
            id=self.id,
            instance_no=self.instance_no,
            kernel_patch=self.kernel_patch,
            kernel_version=self.kernel_version,
            load_balancer_details=self.load_balancer_details,
            location=self.location,
            message_server_properties=self.message_server_properties,
            name=self.name,
            provisioning_state=self.provisioning_state,
            status=self.status,
            subnet=self.subnet,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vm_details=self.vm_details)


def get_sap_central_instance(central_instance_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             sap_virtual_instance_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSAPCentralInstanceResult:
    """
    Gets the SAP Central Services Instance resource.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-10-01-preview.


    :param str central_instance_name: Central Services Instance resource name string modeled as parameter for auto generation to work correctly.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sap_virtual_instance_name: The name of the Virtual Instances for SAP solutions resource
    """
    __args__ = dict()
    __args__['centralInstanceName'] = central_instance_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sapVirtualInstanceName'] = sap_virtual_instance_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:workloads:getSAPCentralInstance', __args__, opts=opts, typ=GetSAPCentralInstanceResult).value

    return AwaitableGetSAPCentralInstanceResult(
        enqueue_replication_server_properties=pulumi.get(__ret__, 'enqueue_replication_server_properties'),
        enqueue_server_properties=pulumi.get(__ret__, 'enqueue_server_properties'),
        errors=pulumi.get(__ret__, 'errors'),
        gateway_server_properties=pulumi.get(__ret__, 'gateway_server_properties'),
        health=pulumi.get(__ret__, 'health'),
        id=pulumi.get(__ret__, 'id'),
        instance_no=pulumi.get(__ret__, 'instance_no'),
        kernel_patch=pulumi.get(__ret__, 'kernel_patch'),
        kernel_version=pulumi.get(__ret__, 'kernel_version'),
        load_balancer_details=pulumi.get(__ret__, 'load_balancer_details'),
        location=pulumi.get(__ret__, 'location'),
        message_server_properties=pulumi.get(__ret__, 'message_server_properties'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        subnet=pulumi.get(__ret__, 'subnet'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vm_details=pulumi.get(__ret__, 'vm_details'))


@_utilities.lift_output_func(get_sap_central_instance)
def get_sap_central_instance_output(central_instance_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    sap_virtual_instance_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSAPCentralInstanceResult]:
    """
    Gets the SAP Central Services Instance resource.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-10-01-preview.


    :param str central_instance_name: Central Services Instance resource name string modeled as parameter for auto generation to work correctly.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sap_virtual_instance_name: The name of the Virtual Instances for SAP solutions resource
    """
    ...
