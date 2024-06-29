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
    'ListAccessClustersResult',
    'AwaitableListAccessClustersResult',
    'list_access_clusters',
    'list_access_clusters_output',
]

@pulumi.output_type
class ListAccessClustersResult:
    """
    List cluster success response
    """
    def __init__(__self__, data=None, kind=None, metadata=None):
        if data and not isinstance(data, list):
            raise TypeError("Expected argument 'data' to be a list")
        pulumi.set(__self__, "data", data)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)

    @property
    @pulumi.getter
    def data(self) -> Optional[Sequence['outputs.ClusterRecordResponse']]:
        """
        Data of the environments list
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Type of response
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['outputs.ConfluentListMetadataResponse']:
        """
        Metadata of the list
        """
        return pulumi.get(self, "metadata")


class AwaitableListAccessClustersResult(ListAccessClustersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAccessClustersResult(
            data=self.data,
            kind=self.kind,
            metadata=self.metadata)


def list_access_clusters(organization_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         search_filters: Optional[Mapping[str, str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAccessClustersResult:
    """
    List cluster success response


    :param str organization_name: Organization resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param Mapping[str, str] search_filters: Search filters for the request
    """
    __args__ = dict()
    __args__['organizationName'] = organization_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['searchFilters'] = search_filters
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:confluent/v20230822:listAccessClusters', __args__, opts=opts, typ=ListAccessClustersResult).value

    return AwaitableListAccessClustersResult(
        data=pulumi.get(__ret__, 'data'),
        kind=pulumi.get(__ret__, 'kind'),
        metadata=pulumi.get(__ret__, 'metadata'))


@_utilities.lift_output_func(list_access_clusters)
def list_access_clusters_output(organization_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                search_filters: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAccessClustersResult]:
    """
    List cluster success response


    :param str organization_name: Organization resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param Mapping[str, str] search_filters: Search filters for the request
    """
    ...
