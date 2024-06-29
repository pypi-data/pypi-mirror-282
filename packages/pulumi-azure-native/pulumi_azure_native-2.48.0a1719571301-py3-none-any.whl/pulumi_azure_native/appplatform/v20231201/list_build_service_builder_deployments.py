# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListBuildServiceBuilderDeploymentsResult',
    'AwaitableListBuildServiceBuilderDeploymentsResult',
    'list_build_service_builder_deployments',
    'list_build_service_builder_deployments_output',
]

@pulumi.output_type
class ListBuildServiceBuilderDeploymentsResult:
    """
    A list of deployments resource ids.
    """
    def __init__(__self__, deployments=None):
        if deployments and not isinstance(deployments, list):
            raise TypeError("Expected argument 'deployments' to be a list")
        pulumi.set(__self__, "deployments", deployments)

    @property
    @pulumi.getter
    def deployments(self) -> Optional[Sequence[str]]:
        """
        A list of deployment resource ids.
        """
        return pulumi.get(self, "deployments")


class AwaitableListBuildServiceBuilderDeploymentsResult(ListBuildServiceBuilderDeploymentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListBuildServiceBuilderDeploymentsResult(
            deployments=self.deployments)


def list_build_service_builder_deployments(build_service_name: Optional[str] = None,
                                           builder_name: Optional[str] = None,
                                           resource_group_name: Optional[str] = None,
                                           service_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListBuildServiceBuilderDeploymentsResult:
    """
    List deployments that are using the builder.


    :param str build_service_name: The name of the build service resource.
    :param str builder_name: The name of the builder resource.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    __args__ = dict()
    __args__['buildServiceName'] = build_service_name
    __args__['builderName'] = builder_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appplatform/v20231201:listBuildServiceBuilderDeployments', __args__, opts=opts, typ=ListBuildServiceBuilderDeploymentsResult).value

    return AwaitableListBuildServiceBuilderDeploymentsResult(
        deployments=pulumi.get(__ret__, 'deployments'))


@_utilities.lift_output_func(list_build_service_builder_deployments)
def list_build_service_builder_deployments_output(build_service_name: Optional[pulumi.Input[str]] = None,
                                                  builder_name: Optional[pulumi.Input[str]] = None,
                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  service_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListBuildServiceBuilderDeploymentsResult]:
    """
    List deployments that are using the builder.


    :param str build_service_name: The name of the build service resource.
    :param str builder_name: The name of the builder resource.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    ...
