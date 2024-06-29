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
    'GetVcenterControllerResult',
    'AwaitableGetVcenterControllerResult',
    'get_vcenter_controller',
    'get_vcenter_controller_output',
]

@pulumi.output_type
class GetVcenterControllerResult:
    """
    A vcenter resource belonging to a site resource.
    """
    def __init__(__self__, created_timestamp=None, errors=None, fqdn=None, friendly_name=None, id=None, instance_uuid=None, name=None, perf_statistics_level=None, port=None, provisioning_state=None, run_as_account_id=None, system_data=None, type=None, updated_timestamp=None, version=None):
        if created_timestamp and not isinstance(created_timestamp, str):
            raise TypeError("Expected argument 'created_timestamp' to be a str")
        pulumi.set(__self__, "created_timestamp", created_timestamp)
        if errors and not isinstance(errors, list):
            raise TypeError("Expected argument 'errors' to be a list")
        pulumi.set(__self__, "errors", errors)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_uuid and not isinstance(instance_uuid, str):
            raise TypeError("Expected argument 'instance_uuid' to be a str")
        pulumi.set(__self__, "instance_uuid", instance_uuid)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if perf_statistics_level and not isinstance(perf_statistics_level, str):
            raise TypeError("Expected argument 'perf_statistics_level' to be a str")
        pulumi.set(__self__, "perf_statistics_level", perf_statistics_level)
        if port and not isinstance(port, str):
            raise TypeError("Expected argument 'port' to be a str")
        pulumi.set(__self__, "port", port)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if run_as_account_id and not isinstance(run_as_account_id, str):
            raise TypeError("Expected argument 'run_as_account_id' to be a str")
        pulumi.set(__self__, "run_as_account_id", run_as_account_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_timestamp and not isinstance(updated_timestamp, str):
            raise TypeError("Expected argument 'updated_timestamp' to be a str")
        pulumi.set(__self__, "updated_timestamp", updated_timestamp)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="createdTimestamp")
    def created_timestamp(self) -> str:
        """
        Gets the timestamp marking vCenter creation.
        """
        return pulumi.get(self, "created_timestamp")

    @property
    @pulumi.getter
    def errors(self) -> Sequence['outputs.HealthErrorDetailsResponse']:
        """
        Gets the errors.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[str]:
        """
        Gets or sets the FQDN/IPAddress of the vCenter.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        Gets or sets the friendly name of the vCenter.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> str:
        """
        Gets the instance UUID of the vCenter.
        """
        return pulumi.get(self, "instance_uuid")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perfStatisticsLevel")
    def perf_statistics_level(self) -> str:
        """
        Gets the performance statistics enabled on the vCenter.
        """
        return pulumi.get(self, "perf_statistics_level")

    @property
    @pulumi.getter
    def port(self) -> Optional[str]:
        """
        Gets or sets the port of the vCenter.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[str]:
        """
        Gets or sets the run as account ID of the vCenter.
        """
        return pulumi.get(self, "run_as_account_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedTimestamp")
    def updated_timestamp(self) -> str:
        """
        Gets the timestamp marking last updated on the vCenter.
        """
        return pulumi.get(self, "updated_timestamp")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Gets the version of the vCenter.
        """
        return pulumi.get(self, "version")


class AwaitableGetVcenterControllerResult(GetVcenterControllerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVcenterControllerResult(
            created_timestamp=self.created_timestamp,
            errors=self.errors,
            fqdn=self.fqdn,
            friendly_name=self.friendly_name,
            id=self.id,
            instance_uuid=self.instance_uuid,
            name=self.name,
            perf_statistics_level=self.perf_statistics_level,
            port=self.port,
            provisioning_state=self.provisioning_state,
            run_as_account_id=self.run_as_account_id,
            system_data=self.system_data,
            type=self.type,
            updated_timestamp=self.updated_timestamp,
            version=self.version)


def get_vcenter_controller(resource_group_name: Optional[str] = None,
                           site_name: Optional[str] = None,
                           vcenter_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVcenterControllerResult:
    """
    Get a Vcenter


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    :param str vcenter_name:  VCenters name
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['siteName'] = site_name
    __args__['vcenterName'] = vcenter_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:offazure/v20230606:getVcenterController', __args__, opts=opts, typ=GetVcenterControllerResult).value

    return AwaitableGetVcenterControllerResult(
        created_timestamp=pulumi.get(__ret__, 'created_timestamp'),
        errors=pulumi.get(__ret__, 'errors'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        friendly_name=pulumi.get(__ret__, 'friendly_name'),
        id=pulumi.get(__ret__, 'id'),
        instance_uuid=pulumi.get(__ret__, 'instance_uuid'),
        name=pulumi.get(__ret__, 'name'),
        perf_statistics_level=pulumi.get(__ret__, 'perf_statistics_level'),
        port=pulumi.get(__ret__, 'port'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        run_as_account_id=pulumi.get(__ret__, 'run_as_account_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        updated_timestamp=pulumi.get(__ret__, 'updated_timestamp'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_vcenter_controller)
def get_vcenter_controller_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                  site_name: Optional[pulumi.Input[str]] = None,
                                  vcenter_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVcenterControllerResult]:
    """
    Get a Vcenter


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    :param str vcenter_name:  VCenters name
    """
    ...
