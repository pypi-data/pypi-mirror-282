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
    'GetEnvironmentDefinitionErrorDetailsResult',
    'AwaitableGetEnvironmentDefinitionErrorDetailsResult',
    'get_environment_definition_error_details',
    'get_environment_definition_error_details_output',
]

@pulumi.output_type
class GetEnvironmentDefinitionErrorDetailsResult:
    """
    List of validator error details. Populated when changes are made to the resource or its dependent resources that impact the validity of the Catalog resource.
    """
    def __init__(__self__, errors=None):
        if errors and not isinstance(errors, list):
            raise TypeError("Expected argument 'errors' to be a list")
        pulumi.set(__self__, "errors", errors)

    @property
    @pulumi.getter
    def errors(self) -> Sequence['outputs.CatalogErrorDetailsResponse']:
        """
        Errors associated with resources synchronized from the catalog.
        """
        return pulumi.get(self, "errors")


class AwaitableGetEnvironmentDefinitionErrorDetailsResult(GetEnvironmentDefinitionErrorDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentDefinitionErrorDetailsResult(
            errors=self.errors)


def get_environment_definition_error_details(catalog_name: Optional[str] = None,
                                             dev_center_name: Optional[str] = None,
                                             environment_definition_name: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentDefinitionErrorDetailsResult:
    """
    Gets Environment Definition error details


    :param str catalog_name: The name of the Catalog.
    :param str dev_center_name: The name of the devcenter.
    :param str environment_definition_name: The name of the Environment Definition.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['catalogName'] = catalog_name
    __args__['devCenterName'] = dev_center_name
    __args__['environmentDefinitionName'] = environment_definition_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20240601preview:getEnvironmentDefinitionErrorDetails', __args__, opts=opts, typ=GetEnvironmentDefinitionErrorDetailsResult).value

    return AwaitableGetEnvironmentDefinitionErrorDetailsResult(
        errors=pulumi.get(__ret__, 'errors'))


@_utilities.lift_output_func(get_environment_definition_error_details)
def get_environment_definition_error_details_output(catalog_name: Optional[pulumi.Input[str]] = None,
                                                    dev_center_name: Optional[pulumi.Input[str]] = None,
                                                    environment_definition_name: Optional[pulumi.Input[str]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentDefinitionErrorDetailsResult]:
    """
    Gets Environment Definition error details


    :param str catalog_name: The name of the Catalog.
    :param str dev_center_name: The name of the devcenter.
    :param str environment_definition_name: The name of the Environment Definition.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
