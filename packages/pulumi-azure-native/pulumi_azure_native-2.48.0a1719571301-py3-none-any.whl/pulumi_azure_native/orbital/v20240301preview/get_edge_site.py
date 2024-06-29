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
    'GetEdgeSiteResult',
    'AwaitableGetEdgeSiteResult',
    'get_edge_site',
    'get_edge_site_output',
]

@pulumi.output_type
class GetEdgeSiteResult:
    """
    A customer's reference to a global communications site site.
    """
    def __init__(__self__, global_communications_site=None, id=None, location=None, name=None, system_data=None, tags=None, type=None):
        if global_communications_site and not isinstance(global_communications_site, dict):
            raise TypeError("Expected argument 'global_communications_site' to be a dict")
        pulumi.set(__self__, "global_communications_site", global_communications_site)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="globalCommunicationsSite")
    def global_communications_site(self) -> 'outputs.EdgeSitesPropertiesResponseGlobalCommunicationsSite':
        """
        A reference to global communications site.
        """
        return pulumi.get(self, "global_communications_site")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

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


class AwaitableGetEdgeSiteResult(GetEdgeSiteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEdgeSiteResult(
            global_communications_site=self.global_communications_site,
            id=self.id,
            location=self.location,
            name=self.name,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_edge_site(edge_site_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEdgeSiteResult:
    """
    Gets the specified edge site in a specified resource group.


    :param str edge_site_name: Edge site name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['edgeSiteName'] = edge_site_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:orbital/v20240301preview:getEdgeSite', __args__, opts=opts, typ=GetEdgeSiteResult).value

    return AwaitableGetEdgeSiteResult(
        global_communications_site=pulumi.get(__ret__, 'global_communications_site'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_edge_site)
def get_edge_site_output(edge_site_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEdgeSiteResult]:
    """
    Gets the specified edge site in a specified resource group.


    :param str edge_site_name: Edge site name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
