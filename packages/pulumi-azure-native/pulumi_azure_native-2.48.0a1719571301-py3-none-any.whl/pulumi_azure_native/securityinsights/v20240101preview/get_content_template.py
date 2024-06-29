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
    'GetContentTemplateResult',
    'AwaitableGetContentTemplateResult',
    'get_content_template',
    'get_content_template_output',
]

@pulumi.output_type
class GetContentTemplateResult:
    """
    Template resource definition.
    """
    def __init__(__self__, author=None, categories=None, content_id=None, content_kind=None, content_product_id=None, content_schema_version=None, custom_version=None, dependant_templates=None, dependencies=None, display_name=None, etag=None, first_publish_date=None, icon=None, id=None, is_deprecated=None, last_publish_date=None, main_template=None, name=None, package_id=None, package_kind=None, package_name=None, package_version=None, preview_images=None, preview_images_dark=None, providers=None, source=None, support=None, system_data=None, threat_analysis_tactics=None, threat_analysis_techniques=None, type=None, version=None):
        if author and not isinstance(author, dict):
            raise TypeError("Expected argument 'author' to be a dict")
        pulumi.set(__self__, "author", author)
        if categories and not isinstance(categories, dict):
            raise TypeError("Expected argument 'categories' to be a dict")
        pulumi.set(__self__, "categories", categories)
        if content_id and not isinstance(content_id, str):
            raise TypeError("Expected argument 'content_id' to be a str")
        pulumi.set(__self__, "content_id", content_id)
        if content_kind and not isinstance(content_kind, str):
            raise TypeError("Expected argument 'content_kind' to be a str")
        pulumi.set(__self__, "content_kind", content_kind)
        if content_product_id and not isinstance(content_product_id, str):
            raise TypeError("Expected argument 'content_product_id' to be a str")
        pulumi.set(__self__, "content_product_id", content_product_id)
        if content_schema_version and not isinstance(content_schema_version, str):
            raise TypeError("Expected argument 'content_schema_version' to be a str")
        pulumi.set(__self__, "content_schema_version", content_schema_version)
        if custom_version and not isinstance(custom_version, str):
            raise TypeError("Expected argument 'custom_version' to be a str")
        pulumi.set(__self__, "custom_version", custom_version)
        if dependant_templates and not isinstance(dependant_templates, list):
            raise TypeError("Expected argument 'dependant_templates' to be a list")
        pulumi.set(__self__, "dependant_templates", dependant_templates)
        if dependencies and not isinstance(dependencies, dict):
            raise TypeError("Expected argument 'dependencies' to be a dict")
        pulumi.set(__self__, "dependencies", dependencies)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if first_publish_date and not isinstance(first_publish_date, str):
            raise TypeError("Expected argument 'first_publish_date' to be a str")
        pulumi.set(__self__, "first_publish_date", first_publish_date)
        if icon and not isinstance(icon, str):
            raise TypeError("Expected argument 'icon' to be a str")
        pulumi.set(__self__, "icon", icon)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_deprecated and not isinstance(is_deprecated, str):
            raise TypeError("Expected argument 'is_deprecated' to be a str")
        pulumi.set(__self__, "is_deprecated", is_deprecated)
        if last_publish_date and not isinstance(last_publish_date, str):
            raise TypeError("Expected argument 'last_publish_date' to be a str")
        pulumi.set(__self__, "last_publish_date", last_publish_date)
        if main_template and not isinstance(main_template, dict):
            raise TypeError("Expected argument 'main_template' to be a dict")
        pulumi.set(__self__, "main_template", main_template)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package_id and not isinstance(package_id, str):
            raise TypeError("Expected argument 'package_id' to be a str")
        pulumi.set(__self__, "package_id", package_id)
        if package_kind and not isinstance(package_kind, str):
            raise TypeError("Expected argument 'package_kind' to be a str")
        pulumi.set(__self__, "package_kind", package_kind)
        if package_name and not isinstance(package_name, str):
            raise TypeError("Expected argument 'package_name' to be a str")
        pulumi.set(__self__, "package_name", package_name)
        if package_version and not isinstance(package_version, str):
            raise TypeError("Expected argument 'package_version' to be a str")
        pulumi.set(__self__, "package_version", package_version)
        if preview_images and not isinstance(preview_images, list):
            raise TypeError("Expected argument 'preview_images' to be a list")
        pulumi.set(__self__, "preview_images", preview_images)
        if preview_images_dark and not isinstance(preview_images_dark, list):
            raise TypeError("Expected argument 'preview_images_dark' to be a list")
        pulumi.set(__self__, "preview_images_dark", preview_images_dark)
        if providers and not isinstance(providers, list):
            raise TypeError("Expected argument 'providers' to be a list")
        pulumi.set(__self__, "providers", providers)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if support and not isinstance(support, dict):
            raise TypeError("Expected argument 'support' to be a dict")
        pulumi.set(__self__, "support", support)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if threat_analysis_tactics and not isinstance(threat_analysis_tactics, list):
            raise TypeError("Expected argument 'threat_analysis_tactics' to be a list")
        pulumi.set(__self__, "threat_analysis_tactics", threat_analysis_tactics)
        if threat_analysis_techniques and not isinstance(threat_analysis_techniques, list):
            raise TypeError("Expected argument 'threat_analysis_techniques' to be a list")
        pulumi.set(__self__, "threat_analysis_techniques", threat_analysis_techniques)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def author(self) -> Optional['outputs.MetadataAuthorResponse']:
        """
        The creator of the content item.
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def categories(self) -> Optional['outputs.MetadataCategoriesResponse']:
        """
        Categories for the item
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter(name="contentId")
    def content_id(self) -> str:
        """
        Static ID for the content.  Used to identify dependencies and content from solutions or community.  Hard-coded/static for out of the box content and solutions. Dynamic for user-created.  This is the resource name
        """
        return pulumi.get(self, "content_id")

    @property
    @pulumi.getter(name="contentKind")
    def content_kind(self) -> str:
        """
        The kind of content the template is for.
        """
        return pulumi.get(self, "content_kind")

    @property
    @pulumi.getter(name="contentProductId")
    def content_product_id(self) -> str:
        """
        Unique ID for the content. It should be generated based on the contentId of the package, contentId of the template, contentKind of the template and the contentVersion of the template
        """
        return pulumi.get(self, "content_product_id")

    @property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> Optional[str]:
        """
        Schema version of the content. Can be used to distinguish between different flow based on the schema version
        """
        return pulumi.get(self, "content_schema_version")

    @property
    @pulumi.getter(name="customVersion")
    def custom_version(self) -> Optional[str]:
        """
        The custom version of the content. A optional free text
        """
        return pulumi.get(self, "custom_version")

    @property
    @pulumi.getter(name="dependantTemplates")
    def dependant_templates(self) -> Sequence['outputs.TemplatePropertiesResponse']:
        """
        Dependant templates. Expandable.
        """
        return pulumi.get(self, "dependant_templates")

    @property
    @pulumi.getter
    def dependencies(self) -> Optional['outputs.MetadataDependenciesResponse']:
        """
        Dependencies for the content item, what other content items it requires to work.  Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex formats.
        """
        return pulumi.get(self, "dependencies")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the template
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
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> Optional[str]:
        """
        first publish date content item
        """
        return pulumi.get(self, "first_publish_date")

    @property
    @pulumi.getter
    def icon(self) -> Optional[str]:
        """
        the icon identifier. this id can later be fetched from the content metadata
        """
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDeprecated")
    def is_deprecated(self) -> str:
        """
        Flag indicates if this template is deprecated
        """
        return pulumi.get(self, "is_deprecated")

    @property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[str]:
        """
        last publish date for the content item
        """
        return pulumi.get(self, "last_publish_date")

    @property
    @pulumi.getter(name="mainTemplate")
    def main_template(self) -> Optional[Any]:
        """
        The JSON of the ARM template to deploy active content. Expandable.
        """
        return pulumi.get(self, "main_template")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageId")
    def package_id(self) -> str:
        """
        the package Id contains this template
        """
        return pulumi.get(self, "package_id")

    @property
    @pulumi.getter(name="packageKind")
    def package_kind(self) -> Optional[str]:
        """
        the packageKind of the package contains this template
        """
        return pulumi.get(self, "package_kind")

    @property
    @pulumi.getter(name="packageName")
    def package_name(self) -> Optional[str]:
        """
        the name of the package contains this template
        """
        return pulumi.get(self, "package_name")

    @property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> str:
        """
        Version of the package.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM metadata best practices.  Can also be any string, but then we cannot guarantee any version checks
        """
        return pulumi.get(self, "package_version")

    @property
    @pulumi.getter(name="previewImages")
    def preview_images(self) -> Optional[Sequence[str]]:
        """
        preview image file names. These will be taken from the solution artifacts
        """
        return pulumi.get(self, "preview_images")

    @property
    @pulumi.getter(name="previewImagesDark")
    def preview_images_dark(self) -> Optional[Sequence[str]]:
        """
        preview image file names. These will be taken from the solution artifacts. used for dark theme support
        """
        return pulumi.get(self, "preview_images_dark")

    @property
    @pulumi.getter
    def providers(self) -> Optional[Sequence[str]]:
        """
        Providers for the content item
        """
        return pulumi.get(self, "providers")

    @property
    @pulumi.getter
    def source(self) -> 'outputs.MetadataSourceResponse':
        """
        Source of the content.  This is where/how it was created.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def support(self) -> Optional['outputs.MetadataSupportResponse']:
        """
        Support information for the template - type, name, contact information
        """
        return pulumi.get(self, "support")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> Optional[Sequence[str]]:
        """
        the tactics the resource covers
        """
        return pulumi.get(self, "threat_analysis_tactics")

    @property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> Optional[Sequence[str]]:
        """
        the techniques the resource covers, these have to be aligned with the tactics being used
        """
        return pulumi.get(self, "threat_analysis_techniques")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of the content.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM metadata best practices.  Can also be any string, but then we cannot guarantee any version checks
        """
        return pulumi.get(self, "version")


class AwaitableGetContentTemplateResult(GetContentTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContentTemplateResult(
            author=self.author,
            categories=self.categories,
            content_id=self.content_id,
            content_kind=self.content_kind,
            content_product_id=self.content_product_id,
            content_schema_version=self.content_schema_version,
            custom_version=self.custom_version,
            dependant_templates=self.dependant_templates,
            dependencies=self.dependencies,
            display_name=self.display_name,
            etag=self.etag,
            first_publish_date=self.first_publish_date,
            icon=self.icon,
            id=self.id,
            is_deprecated=self.is_deprecated,
            last_publish_date=self.last_publish_date,
            main_template=self.main_template,
            name=self.name,
            package_id=self.package_id,
            package_kind=self.package_kind,
            package_name=self.package_name,
            package_version=self.package_version,
            preview_images=self.preview_images,
            preview_images_dark=self.preview_images_dark,
            providers=self.providers,
            source=self.source,
            support=self.support,
            system_data=self.system_data,
            threat_analysis_tactics=self.threat_analysis_tactics,
            threat_analysis_techniques=self.threat_analysis_techniques,
            type=self.type,
            version=self.version)


def get_content_template(resource_group_name: Optional[str] = None,
                         template_id: Optional[str] = None,
                         workspace_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContentTemplateResult:
    """
    Gets a template byt its identifier.
    Expandable properties:
    - properties/mainTemplate
    - properties/dependantTemplates


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str template_id: template Id
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['templateId'] = template_id
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20240101preview:getContentTemplate', __args__, opts=opts, typ=GetContentTemplateResult).value

    return AwaitableGetContentTemplateResult(
        author=pulumi.get(__ret__, 'author'),
        categories=pulumi.get(__ret__, 'categories'),
        content_id=pulumi.get(__ret__, 'content_id'),
        content_kind=pulumi.get(__ret__, 'content_kind'),
        content_product_id=pulumi.get(__ret__, 'content_product_id'),
        content_schema_version=pulumi.get(__ret__, 'content_schema_version'),
        custom_version=pulumi.get(__ret__, 'custom_version'),
        dependant_templates=pulumi.get(__ret__, 'dependant_templates'),
        dependencies=pulumi.get(__ret__, 'dependencies'),
        display_name=pulumi.get(__ret__, 'display_name'),
        etag=pulumi.get(__ret__, 'etag'),
        first_publish_date=pulumi.get(__ret__, 'first_publish_date'),
        icon=pulumi.get(__ret__, 'icon'),
        id=pulumi.get(__ret__, 'id'),
        is_deprecated=pulumi.get(__ret__, 'is_deprecated'),
        last_publish_date=pulumi.get(__ret__, 'last_publish_date'),
        main_template=pulumi.get(__ret__, 'main_template'),
        name=pulumi.get(__ret__, 'name'),
        package_id=pulumi.get(__ret__, 'package_id'),
        package_kind=pulumi.get(__ret__, 'package_kind'),
        package_name=pulumi.get(__ret__, 'package_name'),
        package_version=pulumi.get(__ret__, 'package_version'),
        preview_images=pulumi.get(__ret__, 'preview_images'),
        preview_images_dark=pulumi.get(__ret__, 'preview_images_dark'),
        providers=pulumi.get(__ret__, 'providers'),
        source=pulumi.get(__ret__, 'source'),
        support=pulumi.get(__ret__, 'support'),
        system_data=pulumi.get(__ret__, 'system_data'),
        threat_analysis_tactics=pulumi.get(__ret__, 'threat_analysis_tactics'),
        threat_analysis_techniques=pulumi.get(__ret__, 'threat_analysis_techniques'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_content_template)
def get_content_template_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                template_id: Optional[pulumi.Input[str]] = None,
                                workspace_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContentTemplateResult]:
    """
    Gets a template byt its identifier.
    Expandable properties:
    - properties/mainTemplate
    - properties/dependantTemplates


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str template_id: template Id
    :param str workspace_name: The name of the workspace.
    """
    ...
