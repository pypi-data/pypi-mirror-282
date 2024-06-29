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
    'GetQueryPackResult',
    'AwaitableGetQueryPackResult',
    'get_query_pack',
    'get_query_pack_output',
]

@pulumi.output_type
class GetQueryPackResult:
    """
    An Log Analytics QueryPack definition.
    """
    def __init__(__self__, id=None, location=None, name=None, provisioning_state=None, query_pack_id=None, tags=None, time_created=None, time_modified=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if query_pack_id and not isinstance(query_pack_id, str):
            raise TypeError("Expected argument 'query_pack_id' to be a str")
        pulumi.set(__self__, "query_pack_id", query_pack_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if time_modified and not isinstance(time_modified, str):
            raise TypeError("Expected argument 'time_modified' to be a str")
        pulumi.set(__self__, "time_modified", time_modified)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

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
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Current state of this QueryPack: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="queryPackId")
    def query_pack_id(self) -> str:
        """
        The unique ID of your application. This field cannot be changed.
        """
        return pulumi.get(self, "query_pack_id")

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
        Creation Date for the Log Analytics QueryPack, in ISO 8601 format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> str:
        """
        Last modified date of the Log Analytics QueryPack, in ISO 8601 format.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetQueryPackResult(GetQueryPackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQueryPackResult(
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            query_pack_id=self.query_pack_id,
            tags=self.tags,
            time_created=self.time_created,
            time_modified=self.time_modified,
            type=self.type)


def get_query_pack(query_pack_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQueryPackResult:
    """
    Returns a Log Analytics QueryPack.


    :param str query_pack_name: The name of the Log Analytics QueryPack resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['queryPackName'] = query_pack_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights/v20190901:getQueryPack', __args__, opts=opts, typ=GetQueryPackResult).value

    return AwaitableGetQueryPackResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        query_pack_id=pulumi.get(__ret__, 'query_pack_id'),
        tags=pulumi.get(__ret__, 'tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        time_modified=pulumi.get(__ret__, 'time_modified'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_query_pack)
def get_query_pack_output(query_pack_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQueryPackResult]:
    """
    Returns a Log Analytics QueryPack.


    :param str query_pack_name: The name of the Log Analytics QueryPack resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
