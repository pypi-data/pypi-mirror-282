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
    'GetEntityResult',
    'AwaitableGetEntityResult',
    'get_entity',
    'get_entity_output',
]

@pulumi.output_type
class GetEntityResult:
    """
    Describes the result of the request to view entities.
    """
    def __init__(__self__, count=None, next_link=None, value=None):
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        Total count of records that match the filter
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        The URL to use for getting the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.EntityInfoResponse']]:
        """
        The list of entities.
        """
        return pulumi.get(self, "value")


class AwaitableGetEntityResult(GetEntityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEntityResult(
            count=self.count,
            next_link=self.next_link,
            value=self.value)


def get_entity(filter: Optional[str] = None,
               group_name: Optional[str] = None,
               search: Optional[str] = None,
               select: Optional[str] = None,
               skip: Optional[int] = None,
               skiptoken: Optional[str] = None,
               top: Optional[int] = None,
               view: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEntityResult:
    """
    List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.


    :param str filter: The filter parameter allows you to filter on the the name or display name fields. You can check for equality on the name field (e.g. name eq '{entityName}')  and you can check for substrings on either the name or display name fields(e.g. contains(name, '{substringToSearch}'), contains(displayName, '{substringToSearch')). Note that the '{entityName}' and '{substringToSearch}' fields are checked case insensitively.
    :param str group_name: A filter which allows the get entities call to focus on a particular group (i.e. "$filter=name eq 'groupName'")
    :param str search: The $search parameter is used in conjunction with the $filter parameter to return three different outputs depending on the parameter passed in. 
           With $search=AllowedParents the API will return the entity info of all groups that the requested entity will be able to reparent to as determined by the user's permissions.
           With $search=AllowedChildren the API will return the entity info of all entities that can be added as children of the requested entity.
           With $search=ParentAndFirstLevelChildren the API will return the parent and  first level of children that the user has either direct access to or indirect access via one of their descendants.
           With $search=ParentOnly the API will return only the group if the user has access to at least one of the descendants of the group.
           With $search=ChildrenOnly the API will return only the first level of children of the group entity info specified in $filter.  The user must have direct access to the children entities or one of it's descendants for it to show up in the results.
    :param str select: This parameter specifies the fields to include in the response. Can include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. '$select=Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain'. When specified the $select parameter can override select in $skipToken.
    :param int skip: Number of entities to skip over when retrieving results. Passing this in will override $skipToken.
    :param str skiptoken: Page continuation token is only used if a previous operation returned a partial result. 
           If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
    :param int top: Number of elements to return when retrieving results. Passing this in will override $skipToken.
    :param str view: The view parameter allows clients to filter the type of data that is returned by the getEntities call.
    """
    __args__ = dict()
    __args__['filter'] = filter
    __args__['groupName'] = group_name
    __args__['search'] = search
    __args__['select'] = select
    __args__['skip'] = skip
    __args__['skiptoken'] = skiptoken
    __args__['top'] = top
    __args__['view'] = view
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:management/v20200501:getEntity', __args__, opts=opts, typ=GetEntityResult).value

    return AwaitableGetEntityResult(
        count=pulumi.get(__ret__, 'count'),
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_entity)
def get_entity_output(filter: Optional[pulumi.Input[Optional[str]]] = None,
                      group_name: Optional[pulumi.Input[Optional[str]]] = None,
                      search: Optional[pulumi.Input[Optional[str]]] = None,
                      select: Optional[pulumi.Input[Optional[str]]] = None,
                      skip: Optional[pulumi.Input[Optional[int]]] = None,
                      skiptoken: Optional[pulumi.Input[Optional[str]]] = None,
                      top: Optional[pulumi.Input[Optional[int]]] = None,
                      view: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEntityResult]:
    """
    List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.


    :param str filter: The filter parameter allows you to filter on the the name or display name fields. You can check for equality on the name field (e.g. name eq '{entityName}')  and you can check for substrings on either the name or display name fields(e.g. contains(name, '{substringToSearch}'), contains(displayName, '{substringToSearch')). Note that the '{entityName}' and '{substringToSearch}' fields are checked case insensitively.
    :param str group_name: A filter which allows the get entities call to focus on a particular group (i.e. "$filter=name eq 'groupName'")
    :param str search: The $search parameter is used in conjunction with the $filter parameter to return three different outputs depending on the parameter passed in. 
           With $search=AllowedParents the API will return the entity info of all groups that the requested entity will be able to reparent to as determined by the user's permissions.
           With $search=AllowedChildren the API will return the entity info of all entities that can be added as children of the requested entity.
           With $search=ParentAndFirstLevelChildren the API will return the parent and  first level of children that the user has either direct access to or indirect access via one of their descendants.
           With $search=ParentOnly the API will return only the group if the user has access to at least one of the descendants of the group.
           With $search=ChildrenOnly the API will return only the first level of children of the group entity info specified in $filter.  The user must have direct access to the children entities or one of it's descendants for it to show up in the results.
    :param str select: This parameter specifies the fields to include in the response. Can include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. '$select=Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain'. When specified the $select parameter can override select in $skipToken.
    :param int skip: Number of entities to skip over when retrieving results. Passing this in will override $skipToken.
    :param str skiptoken: Page continuation token is only used if a previous operation returned a partial result. 
           If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
    :param int top: Number of elements to return when retrieving results. Passing this in will override $skipToken.
    :param str view: The view parameter allows clients to filter the type of data that is returned by the getEntities call.
    """
    ...
