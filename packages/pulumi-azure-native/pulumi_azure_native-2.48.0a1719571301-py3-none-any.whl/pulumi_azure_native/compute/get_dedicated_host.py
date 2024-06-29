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
    'GetDedicatedHostResult',
    'AwaitableGetDedicatedHostResult',
    'get_dedicated_host',
    'get_dedicated_host_output',
]

@pulumi.output_type
class GetDedicatedHostResult:
    """
    Specifies information about the Dedicated host.
    """
    def __init__(__self__, auto_replace_on_failure=None, host_id=None, id=None, instance_view=None, license_type=None, location=None, name=None, platform_fault_domain=None, provisioning_state=None, provisioning_time=None, sku=None, tags=None, time_created=None, type=None, virtual_machines=None):
        if auto_replace_on_failure and not isinstance(auto_replace_on_failure, bool):
            raise TypeError("Expected argument 'auto_replace_on_failure' to be a bool")
        pulumi.set(__self__, "auto_replace_on_failure", auto_replace_on_failure)
        if host_id and not isinstance(host_id, str):
            raise TypeError("Expected argument 'host_id' to be a str")
        pulumi.set(__self__, "host_id", host_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_view and not isinstance(instance_view, dict):
            raise TypeError("Expected argument 'instance_view' to be a dict")
        pulumi.set(__self__, "instance_view", instance_view)
        if license_type and not isinstance(license_type, str):
            raise TypeError("Expected argument 'license_type' to be a str")
        pulumi.set(__self__, "license_type", license_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if platform_fault_domain and not isinstance(platform_fault_domain, int):
            raise TypeError("Expected argument 'platform_fault_domain' to be a int")
        pulumi.set(__self__, "platform_fault_domain", platform_fault_domain)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if provisioning_time and not isinstance(provisioning_time, str):
            raise TypeError("Expected argument 'provisioning_time' to be a str")
        pulumi.set(__self__, "provisioning_time", provisioning_time)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_machines and not isinstance(virtual_machines, list):
            raise TypeError("Expected argument 'virtual_machines' to be a list")
        pulumi.set(__self__, "virtual_machines", virtual_machines)

    @property
    @pulumi.getter(name="autoReplaceOnFailure")
    def auto_replace_on_failure(self) -> Optional[bool]:
        """
        Specifies whether the dedicated host should be replaced automatically in case of a failure. The value is defaulted to 'true' when not provided.
        """
        return pulumi.get(self, "auto_replace_on_failure")

    @property
    @pulumi.getter(name="hostId")
    def host_id(self) -> str:
        """
        A unique id generated and assigned to the dedicated host by the platform. Does not change throughout the lifetime of the host.
        """
        return pulumi.get(self, "host_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> 'outputs.DedicatedHostInstanceViewResponse':
        """
        The dedicated host instance view.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[str]:
        """
        Specifies the software license type that will be applied to the VMs deployed on the dedicated host. Possible values are: **None,** **Windows_Server_Hybrid,** **Windows_Server_Perpetual.** The default value is: **None.**
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="platformFaultDomain")
    def platform_fault_domain(self) -> Optional[int]:
        """
        Fault domain of the dedicated host within a dedicated host group.
        """
        return pulumi.get(self, "platform_fault_domain")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="provisioningTime")
    def provisioning_time(self) -> str:
        """
        The date when the host was first provisioned.
        """
        return pulumi.get(self, "provisioning_time")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        SKU of the dedicated host for Hardware Generation and VM family. Only name is required to be set. List Microsoft.Compute SKUs for a list of possible values.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        Specifies the time at which the Dedicated Host resource was created. Minimum api-version: 2021-11-01.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachines")
    def virtual_machines(self) -> Sequence['outputs.SubResourceReadOnlyResponse']:
        """
        A list of references to all virtual machines in the Dedicated Host.
        """
        return pulumi.get(self, "virtual_machines")


class AwaitableGetDedicatedHostResult(GetDedicatedHostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDedicatedHostResult(
            auto_replace_on_failure=self.auto_replace_on_failure,
            host_id=self.host_id,
            id=self.id,
            instance_view=self.instance_view,
            license_type=self.license_type,
            location=self.location,
            name=self.name,
            platform_fault_domain=self.platform_fault_domain,
            provisioning_state=self.provisioning_state,
            provisioning_time=self.provisioning_time,
            sku=self.sku,
            tags=self.tags,
            time_created=self.time_created,
            type=self.type,
            virtual_machines=self.virtual_machines)


def get_dedicated_host(expand: Optional[str] = None,
                       host_group_name: Optional[str] = None,
                       host_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDedicatedHostResult:
    """
    Retrieves information about a dedicated host.
    Azure REST API version: 2023-03-01.

    Other available API versions: 2023-07-01, 2023-09-01, 2024-03-01.


    :param str expand: The expand expression to apply on the operation. 'InstanceView' will retrieve the list of instance views of the dedicated host. 'UserData' is not supported for dedicated host.
    :param str host_group_name: The name of the dedicated host group.
    :param str host_name: The name of the dedicated host.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['hostGroupName'] = host_group_name
    __args__['hostName'] = host_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute:getDedicatedHost', __args__, opts=opts, typ=GetDedicatedHostResult).value

    return AwaitableGetDedicatedHostResult(
        auto_replace_on_failure=pulumi.get(__ret__, 'auto_replace_on_failure'),
        host_id=pulumi.get(__ret__, 'host_id'),
        id=pulumi.get(__ret__, 'id'),
        instance_view=pulumi.get(__ret__, 'instance_view'),
        license_type=pulumi.get(__ret__, 'license_type'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        platform_fault_domain=pulumi.get(__ret__, 'platform_fault_domain'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        provisioning_time=pulumi.get(__ret__, 'provisioning_time'),
        sku=pulumi.get(__ret__, 'sku'),
        tags=pulumi.get(__ret__, 'tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        type=pulumi.get(__ret__, 'type'),
        virtual_machines=pulumi.get(__ret__, 'virtual_machines'))


@_utilities.lift_output_func(get_dedicated_host)
def get_dedicated_host_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                              host_group_name: Optional[pulumi.Input[str]] = None,
                              host_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDedicatedHostResult]:
    """
    Retrieves information about a dedicated host.
    Azure REST API version: 2023-03-01.

    Other available API versions: 2023-07-01, 2023-09-01, 2024-03-01.


    :param str expand: The expand expression to apply on the operation. 'InstanceView' will retrieve the list of instance views of the dedicated host. 'UserData' is not supported for dedicated host.
    :param str host_group_name: The name of the dedicated host group.
    :param str host_name: The name of the dedicated host.
    :param str resource_group_name: The name of the resource group.
    """
    ...
