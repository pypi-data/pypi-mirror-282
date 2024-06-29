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
    'GetWatchlistResult',
    'AwaitableGetWatchlistResult',
    'get_watchlist',
    'get_watchlist_output',
]

@pulumi.output_type
class GetWatchlistResult:
    """
    Represents a Watchlist in Azure Security Insights.
    """
    def __init__(__self__, content_type=None, created=None, created_by=None, default_duration=None, description=None, display_name=None, etag=None, id=None, is_deleted=None, items_search_key=None, labels=None, name=None, number_of_lines_to_skip=None, provider=None, raw_content=None, source=None, system_data=None, tenant_id=None, type=None, updated=None, updated_by=None, upload_status=None, watchlist_alias=None, watchlist_id=None, watchlist_type=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if created_by and not isinstance(created_by, dict):
            raise TypeError("Expected argument 'created_by' to be a dict")
        pulumi.set(__self__, "created_by", created_by)
        if default_duration and not isinstance(default_duration, str):
            raise TypeError("Expected argument 'default_duration' to be a str")
        pulumi.set(__self__, "default_duration", default_duration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_deleted and not isinstance(is_deleted, bool):
            raise TypeError("Expected argument 'is_deleted' to be a bool")
        pulumi.set(__self__, "is_deleted", is_deleted)
        if items_search_key and not isinstance(items_search_key, str):
            raise TypeError("Expected argument 'items_search_key' to be a str")
        pulumi.set(__self__, "items_search_key", items_search_key)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if number_of_lines_to_skip and not isinstance(number_of_lines_to_skip, int):
            raise TypeError("Expected argument 'number_of_lines_to_skip' to be a int")
        pulumi.set(__self__, "number_of_lines_to_skip", number_of_lines_to_skip)
        if provider and not isinstance(provider, str):
            raise TypeError("Expected argument 'provider' to be a str")
        pulumi.set(__self__, "provider", provider)
        if raw_content and not isinstance(raw_content, str):
            raise TypeError("Expected argument 'raw_content' to be a str")
        pulumi.set(__self__, "raw_content", raw_content)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)
        if updated_by and not isinstance(updated_by, dict):
            raise TypeError("Expected argument 'updated_by' to be a dict")
        pulumi.set(__self__, "updated_by", updated_by)
        if upload_status and not isinstance(upload_status, str):
            raise TypeError("Expected argument 'upload_status' to be a str")
        pulumi.set(__self__, "upload_status", upload_status)
        if watchlist_alias and not isinstance(watchlist_alias, str):
            raise TypeError("Expected argument 'watchlist_alias' to be a str")
        pulumi.set(__self__, "watchlist_alias", watchlist_alias)
        if watchlist_id and not isinstance(watchlist_id, str):
            raise TypeError("Expected argument 'watchlist_id' to be a str")
        pulumi.set(__self__, "watchlist_id", watchlist_id)
        if watchlist_type and not isinstance(watchlist_type, str):
            raise TypeError("Expected argument 'watchlist_type' to be a str")
        pulumi.set(__self__, "watchlist_type", watchlist_type)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        """
        The content type of the raw content. For now, only text/csv is valid
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def created(self) -> Optional[str]:
        """
        The time the watchlist was created
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional['outputs.WatchlistUserInfoResponse']:
        """
        Describes a user that created the watchlist
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="defaultDuration")
    def default_duration(self) -> Optional[str]:
        """
        The default duration of a watchlist (in ISO 8601 duration format)
        """
        return pulumi.get(self, "default_duration")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the watchlist
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the watchlist
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> Optional[bool]:
        """
        A flag that indicates if the watchlist is deleted or not
        """
        return pulumi.get(self, "is_deleted")

    @property
    @pulumi.getter(name="itemsSearchKey")
    def items_search_key(self) -> str:
        """
        The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address.
        """
        return pulumi.get(self, "items_search_key")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[str]]:
        """
        List of labels relevant to this watchlist
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
    @pulumi.getter(name="numberOfLinesToSkip")
    def number_of_lines_to_skip(self) -> Optional[int]:
        """
        The number of lines in a csv content to skip before the header
        """
        return pulumi.get(self, "number_of_lines_to_skip")

    @property
    @pulumi.getter
    def provider(self) -> str:
        """
        The provider of the watchlist
        """
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter(name="rawContent")
    def raw_content(self) -> Optional[str]:
        """
        The raw content that represents to watchlist items to create. Example : This line will be skipped
        header1,header2
        value1,value2
        """
        return pulumi.get(self, "raw_content")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The source of the watchlist
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The tenantId where the watchlist belongs to
        """
        return pulumi.get(self, "tenant_id")

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
        The last time the watchlist was updated
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional['outputs.WatchlistUserInfoResponse']:
        """
        Describes a user that updated the watchlist
        """
        return pulumi.get(self, "updated_by")

    @property
    @pulumi.getter(name="uploadStatus")
    def upload_status(self) -> Optional[str]:
        """
        The status of the Watchlist upload : New, InProgress or Complete. **Note** : When a Watchlist upload status is InProgress, the Watchlist cannot be deleted
        """
        return pulumi.get(self, "upload_status")

    @property
    @pulumi.getter(name="watchlistAlias")
    def watchlist_alias(self) -> Optional[str]:
        """
        The alias of the watchlist
        """
        return pulumi.get(self, "watchlist_alias")

    @property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> Optional[str]:
        """
        The id (a Guid) of the watchlist
        """
        return pulumi.get(self, "watchlist_id")

    @property
    @pulumi.getter(name="watchlistType")
    def watchlist_type(self) -> Optional[str]:
        """
        The type of the watchlist
        """
        return pulumi.get(self, "watchlist_type")


class AwaitableGetWatchlistResult(GetWatchlistResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWatchlistResult(
            content_type=self.content_type,
            created=self.created,
            created_by=self.created_by,
            default_duration=self.default_duration,
            description=self.description,
            display_name=self.display_name,
            etag=self.etag,
            id=self.id,
            is_deleted=self.is_deleted,
            items_search_key=self.items_search_key,
            labels=self.labels,
            name=self.name,
            number_of_lines_to_skip=self.number_of_lines_to_skip,
            provider=self.provider,
            raw_content=self.raw_content,
            source=self.source,
            system_data=self.system_data,
            tenant_id=self.tenant_id,
            type=self.type,
            updated=self.updated,
            updated_by=self.updated_by,
            upload_status=self.upload_status,
            watchlist_alias=self.watchlist_alias,
            watchlist_id=self.watchlist_id,
            watchlist_type=self.watchlist_type)


def get_watchlist(resource_group_name: Optional[str] = None,
                  watchlist_alias: Optional[str] = None,
                  workspace_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWatchlistResult:
    """
    Get a watchlist, without its watchlist items.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str watchlist_alias: The watchlist alias
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['watchlistAlias'] = watchlist_alias
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20230201:getWatchlist', __args__, opts=opts, typ=GetWatchlistResult).value

    return AwaitableGetWatchlistResult(
        content_type=pulumi.get(__ret__, 'content_type'),
        created=pulumi.get(__ret__, 'created'),
        created_by=pulumi.get(__ret__, 'created_by'),
        default_duration=pulumi.get(__ret__, 'default_duration'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        is_deleted=pulumi.get(__ret__, 'is_deleted'),
        items_search_key=pulumi.get(__ret__, 'items_search_key'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        number_of_lines_to_skip=pulumi.get(__ret__, 'number_of_lines_to_skip'),
        provider=pulumi.get(__ret__, 'provider'),
        raw_content=pulumi.get(__ret__, 'raw_content'),
        source=pulumi.get(__ret__, 'source'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'),
        updated=pulumi.get(__ret__, 'updated'),
        updated_by=pulumi.get(__ret__, 'updated_by'),
        upload_status=pulumi.get(__ret__, 'upload_status'),
        watchlist_alias=pulumi.get(__ret__, 'watchlist_alias'),
        watchlist_id=pulumi.get(__ret__, 'watchlist_id'),
        watchlist_type=pulumi.get(__ret__, 'watchlist_type'))


@_utilities.lift_output_func(get_watchlist)
def get_watchlist_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                         watchlist_alias: Optional[pulumi.Input[str]] = None,
                         workspace_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWatchlistResult]:
    """
    Get a watchlist, without its watchlist items.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str watchlist_alias: The watchlist alias
    :param str workspace_name: The name of the workspace.
    """
    ...
