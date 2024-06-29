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
    'GetWorkbookTemplateResult',
    'AwaitableGetWorkbookTemplateResult',
    'get_workbook_template',
    'get_workbook_template_output',
]

@pulumi.output_type
class GetWorkbookTemplateResult:
    """
    An Application Insights workbook template definition.
    """
    def __init__(__self__, author=None, galleries=None, id=None, localized=None, location=None, name=None, priority=None, tags=None, template_data=None, type=None):
        if author and not isinstance(author, str):
            raise TypeError("Expected argument 'author' to be a str")
        pulumi.set(__self__, "author", author)
        if galleries and not isinstance(galleries, list):
            raise TypeError("Expected argument 'galleries' to be a list")
        pulumi.set(__self__, "galleries", galleries)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if localized and not isinstance(localized, dict):
            raise TypeError("Expected argument 'localized' to be a dict")
        pulumi.set(__self__, "localized", localized)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if template_data and not isinstance(template_data, dict):
            raise TypeError("Expected argument 'template_data' to be a dict")
        pulumi.set(__self__, "template_data", template_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def author(self) -> Optional[str]:
        """
        Information about the author of the workbook template.
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def galleries(self) -> Sequence['outputs.WorkbookTemplateGalleryResponse']:
        """
        Workbook galleries supported by the template.
        """
        return pulumi.get(self, "galleries")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def localized(self) -> Optional[Mapping[str, Sequence['outputs.WorkbookTemplateLocalizedGalleryResponse']]]:
        """
        Key value pair of localized gallery. Each key is the locale code of languages supported by the Azure portal.
        """
        return pulumi.get(self, "localized")

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
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> Optional[int]:
        """
        Priority of the template. Determines which template to open when a workbook gallery is opened in viewer mode.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateData")
    def template_data(self) -> Any:
        """
        Valid JSON object containing workbook template payload.
        """
        return pulumi.get(self, "template_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkbookTemplateResult(GetWorkbookTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkbookTemplateResult(
            author=self.author,
            galleries=self.galleries,
            id=self.id,
            localized=self.localized,
            location=self.location,
            name=self.name,
            priority=self.priority,
            tags=self.tags,
            template_data=self.template_data,
            type=self.type)


def get_workbook_template(resource_group_name: Optional[str] = None,
                          resource_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkbookTemplateResult:
    """
    Get a single workbook template by its resourceName.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20201120:getWorkbookTemplate', __args__, opts=opts, typ=GetWorkbookTemplateResult).value

    return AwaitableGetWorkbookTemplateResult(
        author=pulumi.get(__ret__, 'author'),
        galleries=pulumi.get(__ret__, 'galleries'),
        id=pulumi.get(__ret__, 'id'),
        localized=pulumi.get(__ret__, 'localized'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        priority=pulumi.get(__ret__, 'priority'),
        tags=pulumi.get(__ret__, 'tags'),
        template_data=pulumi.get(__ret__, 'template_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workbook_template)
def get_workbook_template_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                 resource_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkbookTemplateResult]:
    """
    Get a single workbook template by its resourceName.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    """
    ...
