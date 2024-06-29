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
    'ListDeploymentInfoResult',
    'AwaitableListDeploymentInfoResult',
    'list_deployment_info',
    'list_deployment_info_output',
]

@pulumi.output_type
class ListDeploymentInfoResult:
    """
    The properties of deployment in Elastic cloud corresponding to the Elastic monitor resource.
    """
    def __init__(__self__, deployment_url=None, disk_capacity=None, marketplace_saas_info=None, memory_capacity=None, status=None, version=None):
        if deployment_url and not isinstance(deployment_url, str):
            raise TypeError("Expected argument 'deployment_url' to be a str")
        pulumi.set(__self__, "deployment_url", deployment_url)
        if disk_capacity and not isinstance(disk_capacity, str):
            raise TypeError("Expected argument 'disk_capacity' to be a str")
        pulumi.set(__self__, "disk_capacity", disk_capacity)
        if marketplace_saas_info and not isinstance(marketplace_saas_info, dict):
            raise TypeError("Expected argument 'marketplace_saas_info' to be a dict")
        pulumi.set(__self__, "marketplace_saas_info", marketplace_saas_info)
        if memory_capacity and not isinstance(memory_capacity, str):
            raise TypeError("Expected argument 'memory_capacity' to be a str")
        pulumi.set(__self__, "memory_capacity", memory_capacity)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="deploymentUrl")
    def deployment_url(self) -> str:
        """
        Deployment URL of the elasticsearch in Elastic cloud deployment.
        """
        return pulumi.get(self, "deployment_url")

    @property
    @pulumi.getter(name="diskCapacity")
    def disk_capacity(self) -> str:
        """
        Disk capacity of the elasticsearch in Elastic cloud deployment.
        """
        return pulumi.get(self, "disk_capacity")

    @property
    @pulumi.getter(name="marketplaceSaasInfo")
    def marketplace_saas_info(self) -> 'outputs.MarketplaceSaaSInfoResponse':
        """
        Marketplace SaaS Info of the resource.
        """
        return pulumi.get(self, "marketplace_saas_info")

    @property
    @pulumi.getter(name="memoryCapacity")
    def memory_capacity(self) -> str:
        """
        RAM capacity of the elasticsearch in Elastic cloud deployment.
        """
        return pulumi.get(self, "memory_capacity")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The Elastic deployment status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of the elasticsearch in Elastic cloud deployment.
        """
        return pulumi.get(self, "version")


class AwaitableListDeploymentInfoResult(ListDeploymentInfoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDeploymentInfoResult(
            deployment_url=self.deployment_url,
            disk_capacity=self.disk_capacity,
            marketplace_saas_info=self.marketplace_saas_info,
            memory_capacity=self.memory_capacity,
            status=self.status,
            version=self.version)


def list_deployment_info(monitor_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDeploymentInfoResult:
    """
    The properties of deployment in Elastic cloud corresponding to the Elastic monitor resource.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group to which the Elastic resource belongs.
    """
    __args__ = dict()
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic/v20230615preview:listDeploymentInfo', __args__, opts=opts, typ=ListDeploymentInfoResult).value

    return AwaitableListDeploymentInfoResult(
        deployment_url=pulumi.get(__ret__, 'deployment_url'),
        disk_capacity=pulumi.get(__ret__, 'disk_capacity'),
        marketplace_saas_info=pulumi.get(__ret__, 'marketplace_saas_info'),
        memory_capacity=pulumi.get(__ret__, 'memory_capacity'),
        status=pulumi.get(__ret__, 'status'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(list_deployment_info)
def list_deployment_info_output(monitor_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDeploymentInfoResult]:
    """
    The properties of deployment in Elastic cloud corresponding to the Elastic monitor resource.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group to which the Elastic resource belongs.
    """
    ...
