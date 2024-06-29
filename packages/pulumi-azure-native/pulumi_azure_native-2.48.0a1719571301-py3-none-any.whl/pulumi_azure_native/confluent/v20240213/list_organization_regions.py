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
    'ListOrganizationRegionsResult',
    'AwaitableListOrganizationRegionsResult',
    'list_organization_regions',
    'list_organization_regions_output',
]

@pulumi.output_type
class ListOrganizationRegionsResult:
    """
    Result of POST request to list regions supported by confluent
    """
    def __init__(__self__, data=None):
        if data and not isinstance(data, list):
            raise TypeError("Expected argument 'data' to be a list")
        pulumi.set(__self__, "data", data)

    @property
    @pulumi.getter
    def data(self) -> Optional[Sequence['outputs.RegionRecordResponse']]:
        """
        List of regions supported by confluent
        """
        return pulumi.get(self, "data")


class AwaitableListOrganizationRegionsResult(ListOrganizationRegionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListOrganizationRegionsResult(
            data=self.data)


def list_organization_regions(organization_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              search_filters: Optional[Mapping[str, str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListOrganizationRegionsResult:
    """
    Result of POST request to list regions supported by confluent


    :param str organization_name: Organization resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param Mapping[str, str] search_filters: Search filters for the request
    """
    __args__ = dict()
    __args__['organizationName'] = organization_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['searchFilters'] = search_filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:confluent/v20240213:listOrganizationRegions', __args__, opts=opts, typ=ListOrganizationRegionsResult).value

    return AwaitableListOrganizationRegionsResult(
        data=pulumi.get(__ret__, 'data'))


@_utilities.lift_output_func(list_organization_regions)
def list_organization_regions_output(organization_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     search_filters: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListOrganizationRegionsResult]:
    """
    Result of POST request to list regions supported by confluent


    :param str organization_name: Organization resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param Mapping[str, str] search_filters: Search filters for the request
    """
    ...
