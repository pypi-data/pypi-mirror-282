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
    'GetBookmarkResult',
    'AwaitableGetBookmarkResult',
    'get_bookmark',
    'get_bookmark_output',
]

@pulumi.output_type
class GetBookmarkResult:
    """
    Represents a bookmark in Azure Security Insights.
    """
    def __init__(__self__, created=None, created_by=None, display_name=None, entity_mappings=None, etag=None, event_time=None, id=None, incident_info=None, labels=None, name=None, notes=None, query=None, query_end_time=None, query_result=None, query_start_time=None, system_data=None, tactics=None, techniques=None, type=None, updated=None, updated_by=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if created_by and not isinstance(created_by, dict):
            raise TypeError("Expected argument 'created_by' to be a dict")
        pulumi.set(__self__, "created_by", created_by)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if entity_mappings and not isinstance(entity_mappings, list):
            raise TypeError("Expected argument 'entity_mappings' to be a list")
        pulumi.set(__self__, "entity_mappings", entity_mappings)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if event_time and not isinstance(event_time, str):
            raise TypeError("Expected argument 'event_time' to be a str")
        pulumi.set(__self__, "event_time", event_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if incident_info and not isinstance(incident_info, dict):
            raise TypeError("Expected argument 'incident_info' to be a dict")
        pulumi.set(__self__, "incident_info", incident_info)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if query and not isinstance(query, str):
            raise TypeError("Expected argument 'query' to be a str")
        pulumi.set(__self__, "query", query)
        if query_end_time and not isinstance(query_end_time, str):
            raise TypeError("Expected argument 'query_end_time' to be a str")
        pulumi.set(__self__, "query_end_time", query_end_time)
        if query_result and not isinstance(query_result, str):
            raise TypeError("Expected argument 'query_result' to be a str")
        pulumi.set(__self__, "query_result", query_result)
        if query_start_time and not isinstance(query_start_time, str):
            raise TypeError("Expected argument 'query_start_time' to be a str")
        pulumi.set(__self__, "query_start_time", query_start_time)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tactics and not isinstance(tactics, list):
            raise TypeError("Expected argument 'tactics' to be a list")
        pulumi.set(__self__, "tactics", tactics)
        if techniques and not isinstance(techniques, list):
            raise TypeError("Expected argument 'techniques' to be a list")
        pulumi.set(__self__, "techniques", techniques)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)
        if updated_by and not isinstance(updated_by, dict):
            raise TypeError("Expected argument 'updated_by' to be a dict")
        pulumi.set(__self__, "updated_by", updated_by)

    @property
    @pulumi.getter
    def created(self) -> Optional[str]:
        """
        The time the bookmark was created
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional['outputs.UserInfoResponse']:
        """
        Describes a user that created the bookmark
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the bookmark
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entityMappings")
    def entity_mappings(self) -> Optional[Sequence['outputs.BookmarkEntityMappingsResponse']]:
        """
        Describes the entity mappings of the bookmark
        """
        return pulumi.get(self, "entity_mappings")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> Optional[str]:
        """
        The bookmark event time
        """
        return pulumi.get(self, "event_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="incidentInfo")
    def incident_info(self) -> Optional['outputs.IncidentInfoResponse']:
        """
        Describes an incident that relates to bookmark
        """
        return pulumi.get(self, "incident_info")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[str]]:
        """
        List of labels relevant to this bookmark
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        """
        The notes of the bookmark
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def query(self) -> str:
        """
        The query of the bookmark.
        """
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="queryEndTime")
    def query_end_time(self) -> Optional[str]:
        """
        The end time for the query
        """
        return pulumi.get(self, "query_end_time")

    @property
    @pulumi.getter(name="queryResult")
    def query_result(self) -> Optional[str]:
        """
        The query result of the bookmark.
        """
        return pulumi.get(self, "query_result")

    @property
    @pulumi.getter(name="queryStartTime")
    def query_start_time(self) -> Optional[str]:
        """
        The start time for the query
        """
        return pulumi.get(self, "query_start_time")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tactics(self) -> Optional[Sequence[str]]:
        """
        A list of relevant mitre attacks
        """
        return pulumi.get(self, "tactics")

    @property
    @pulumi.getter
    def techniques(self) -> Optional[Sequence[str]]:
        """
        A list of relevant mitre techniques
        """
        return pulumi.get(self, "techniques")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def updated(self) -> Optional[str]:
        """
        The last time the bookmark was updated
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional['outputs.UserInfoResponse']:
        """
        Describes a user that updated the bookmark
        """
        return pulumi.get(self, "updated_by")


class AwaitableGetBookmarkResult(GetBookmarkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBookmarkResult(
            created=self.created,
            created_by=self.created_by,
            display_name=self.display_name,
            entity_mappings=self.entity_mappings,
            etag=self.etag,
            event_time=self.event_time,
            id=self.id,
            incident_info=self.incident_info,
            labels=self.labels,
            name=self.name,
            notes=self.notes,
            query=self.query,
            query_end_time=self.query_end_time,
            query_result=self.query_result,
            query_start_time=self.query_start_time,
            system_data=self.system_data,
            tactics=self.tactics,
            techniques=self.techniques,
            type=self.type,
            updated=self.updated,
            updated_by=self.updated_by)


def get_bookmark(bookmark_id: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 workspace_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBookmarkResult:
    """
    Gets a bookmark.


    :param str bookmark_id: Bookmark ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['bookmarkId'] = bookmark_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20230901preview:getBookmark', __args__, opts=opts, typ=GetBookmarkResult).value

    return AwaitableGetBookmarkResult(
        created=pulumi.get(__ret__, 'created'),
        created_by=pulumi.get(__ret__, 'created_by'),
        display_name=pulumi.get(__ret__, 'display_name'),
        entity_mappings=pulumi.get(__ret__, 'entity_mappings'),
        etag=pulumi.get(__ret__, 'etag'),
        event_time=pulumi.get(__ret__, 'event_time'),
        id=pulumi.get(__ret__, 'id'),
        incident_info=pulumi.get(__ret__, 'incident_info'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        notes=pulumi.get(__ret__, 'notes'),
        query=pulumi.get(__ret__, 'query'),
        query_end_time=pulumi.get(__ret__, 'query_end_time'),
        query_result=pulumi.get(__ret__, 'query_result'),
        query_start_time=pulumi.get(__ret__, 'query_start_time'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tactics=pulumi.get(__ret__, 'tactics'),
        techniques=pulumi.get(__ret__, 'techniques'),
        type=pulumi.get(__ret__, 'type'),
        updated=pulumi.get(__ret__, 'updated'),
        updated_by=pulumi.get(__ret__, 'updated_by'))


@_utilities.lift_output_func(get_bookmark)
def get_bookmark_output(bookmark_id: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        workspace_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBookmarkResult]:
    """
    Gets a bookmark.


    :param str bookmark_id: Bookmark ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
