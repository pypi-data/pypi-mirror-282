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
    'GetServiceConfigurationResult',
    'AwaitableGetServiceConfigurationResult',
    'get_service_configuration',
    'get_service_configuration_output',
]

@pulumi.output_type
class GetServiceConfigurationResult:
    """
    The service configuration details associated with the target resource.
    """
    def __init__(__self__, created_at=None, created_by=None, created_by_type=None, id=None, last_modified_at=None, last_modified_by=None, last_modified_by_type=None, name=None, port=None, provisioning_state=None, resource_id=None, service_name=None, system_data=None, type=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if created_by_type and not isinstance(created_by_type, str):
            raise TypeError("Expected argument 'created_by_type' to be a str")
        pulumi.set(__self__, "created_by_type", created_by_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_at and not isinstance(last_modified_at, str):
            raise TypeError("Expected argument 'last_modified_at' to be a str")
        pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by and not isinstance(last_modified_by, str):
            raise TypeError("Expected argument 'last_modified_by' to be a str")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type and not isinstance(last_modified_by_type, str):
            raise TypeError("Expected argument 'last_modified_by_type' to be a str")
        pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if port and not isinstance(port, float):
            raise TypeError("Expected argument 'port' to be a float")
        pulumi.set(__self__, "port", port)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> Optional[float]:
        """
        The port on which service is enabled.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        The resource Id of the connectivity endpoint (optional).
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Name of the service.
        """
        return pulumi.get(self, "service_name")

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


class AwaitableGetServiceConfigurationResult(GetServiceConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceConfigurationResult(
            created_at=self.created_at,
            created_by=self.created_by,
            created_by_type=self.created_by_type,
            id=self.id,
            last_modified_at=self.last_modified_at,
            last_modified_by=self.last_modified_by,
            last_modified_by_type=self.last_modified_by_type,
            name=self.name,
            port=self.port,
            provisioning_state=self.provisioning_state,
            resource_id=self.resource_id,
            service_name=self.service_name,
            system_data=self.system_data,
            type=self.type)


def get_service_configuration(endpoint_name: Optional[str] = None,
                              resource_uri: Optional[str] = None,
                              service_configuration_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceConfigurationResult:
    """
    Gets the details about the service to the resource.
    Azure REST API version: 2023-03-15.


    :param str endpoint_name: The endpoint name.
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    :param str service_configuration_name: The service name.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['resourceUri'] = resource_uri
    __args__['serviceConfigurationName'] = service_configuration_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridconnectivity:getServiceConfiguration', __args__, opts=opts, typ=GetServiceConfigurationResult).value

    return AwaitableGetServiceConfigurationResult(
        created_at=pulumi.get(__ret__, 'created_at'),
        created_by=pulumi.get(__ret__, 'created_by'),
        created_by_type=pulumi.get(__ret__, 'created_by_type'),
        id=pulumi.get(__ret__, 'id'),
        last_modified_at=pulumi.get(__ret__, 'last_modified_at'),
        last_modified_by=pulumi.get(__ret__, 'last_modified_by'),
        last_modified_by_type=pulumi.get(__ret__, 'last_modified_by_type'),
        name=pulumi.get(__ret__, 'name'),
        port=pulumi.get(__ret__, 'port'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        service_name=pulumi.get(__ret__, 'service_name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_service_configuration)
def get_service_configuration_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                                     resource_uri: Optional[pulumi.Input[str]] = None,
                                     service_configuration_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceConfigurationResult]:
    """
    Gets the details about the service to the resource.
    Azure REST API version: 2023-03-15.


    :param str endpoint_name: The endpoint name.
    :param str resource_uri: The fully qualified Azure Resource manager identifier of the resource to be connected.
    :param str service_configuration_name: The service name.
    """
    ...
