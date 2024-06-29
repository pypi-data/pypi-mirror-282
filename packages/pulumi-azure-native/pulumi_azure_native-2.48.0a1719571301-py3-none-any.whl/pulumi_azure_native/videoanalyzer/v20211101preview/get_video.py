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
    'GetVideoResult',
    'AwaitableGetVideoResult',
    'get_video',
    'get_video_output',
]

@pulumi.output_type
class GetVideoResult:
    """
    Represents a video resource within Azure Video Analyzer. Videos can be ingested from RTSP cameras through live pipelines or can be created by exporting sequences from existing captured video through a pipeline job. Videos ingested through live pipelines can be streamed through Azure Video Analyzer Player Widget or compatible players. Exported videos can be downloaded as MP4 files.
    """
    def __init__(__self__, archival=None, content_urls=None, description=None, flags=None, id=None, media_info=None, name=None, system_data=None, title=None, type=None):
        if archival and not isinstance(archival, dict):
            raise TypeError("Expected argument 'archival' to be a dict")
        pulumi.set(__self__, "archival", archival)
        if content_urls and not isinstance(content_urls, dict):
            raise TypeError("Expected argument 'content_urls' to be a dict")
        pulumi.set(__self__, "content_urls", content_urls)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if flags and not isinstance(flags, dict):
            raise TypeError("Expected argument 'flags' to be a dict")
        pulumi.set(__self__, "flags", flags)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if media_info and not isinstance(media_info, dict):
            raise TypeError("Expected argument 'media_info' to be a dict")
        pulumi.set(__self__, "media_info", media_info)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def archival(self) -> Optional['outputs.VideoArchivalResponse']:
        """
        Video archival properties.
        """
        return pulumi.get(self, "archival")

    @property
    @pulumi.getter(name="contentUrls")
    def content_urls(self) -> 'outputs.VideoContentUrlsResponse':
        """
        Set of URLs to the video content.
        """
        return pulumi.get(self, "content_urls")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Optional video description provided by the user. Value can be up to 2048 characters long.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def flags(self) -> 'outputs.VideoFlagsResponse':
        """
        Video flags contain information about the available video actions and its dynamic properties based on the current video state.
        """
        return pulumi.get(self, "flags")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="mediaInfo")
    def media_info(self) -> Optional['outputs.VideoMediaInfoResponse']:
        """
        Contains information about the video and audio content.
        """
        return pulumi.get(self, "media_info")

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
    def title(self) -> Optional[str]:
        """
        Optional video title provided by the user. Value can be up to 256 characters long.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetVideoResult(GetVideoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVideoResult(
            archival=self.archival,
            content_urls=self.content_urls,
            description=self.description,
            flags=self.flags,
            id=self.id,
            media_info=self.media_info,
            name=self.name,
            system_data=self.system_data,
            title=self.title,
            type=self.type)


def get_video(account_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              video_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVideoResult:
    """
    Retrieves an existing video resource with the given name.


    :param str account_name: The Azure Video Analyzer account name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str video_name: The Video name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['videoName'] = video_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:videoanalyzer/v20211101preview:getVideo', __args__, opts=opts, typ=GetVideoResult).value

    return AwaitableGetVideoResult(
        archival=pulumi.get(__ret__, 'archival'),
        content_urls=pulumi.get(__ret__, 'content_urls'),
        description=pulumi.get(__ret__, 'description'),
        flags=pulumi.get(__ret__, 'flags'),
        id=pulumi.get(__ret__, 'id'),
        media_info=pulumi.get(__ret__, 'media_info'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        title=pulumi.get(__ret__, 'title'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_video)
def get_video_output(account_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     video_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVideoResult]:
    """
    Retrieves an existing video resource with the given name.


    :param str account_name: The Azure Video Analyzer account name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str video_name: The Video name.
    """
    ...
