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
    'GetIntegrationAccountPartnerResult',
    'AwaitableGetIntegrationAccountPartnerResult',
    'get_integration_account_partner',
    'get_integration_account_partner_output',
]

@pulumi.output_type
class GetIntegrationAccountPartnerResult:
    def __init__(__self__, changed_time=None, content=None, created_time=None, id=None, location=None, metadata=None, name=None, partner_type=None, tags=None, type=None):
        if changed_time and not isinstance(changed_time, str):
            raise TypeError("Expected argument 'changed_time' to be a str")
        pulumi.set(__self__, "changed_time", changed_time)
        if content and not isinstance(content, dict):
            raise TypeError("Expected argument 'content' to be a dict")
        pulumi.set(__self__, "content", content)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_type and not isinstance(partner_type, str):
            raise TypeError("Expected argument 'partner_type' to be a str")
        pulumi.set(__self__, "partner_type", partner_type)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> str:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter
    def content(self) -> Optional['outputs.PartnerContentResponse']:
        """
        The partner content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerType")
    def partner_type(self) -> Optional[str]:
        """
        The partner type.
        """
        return pulumi.get(self, "partner_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIntegrationAccountPartnerResult(GetIntegrationAccountPartnerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationAccountPartnerResult(
            changed_time=self.changed_time,
            content=self.content,
            created_time=self.created_time,
            id=self.id,
            location=self.location,
            metadata=self.metadata,
            name=self.name,
            partner_type=self.partner_type,
            tags=self.tags,
            type=self.type)


def get_integration_account_partner(integration_account_name: Optional[str] = None,
                                    partner_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationAccountPartnerResult:
    """
    Gets an integration account partner.


    :param str integration_account_name: The integration account name.
    :param str partner_name: The integration account partner name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['integrationAccountName'] = integration_account_name
    __args__['partnerName'] = partner_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:logic/v20150801preview:getIntegrationAccountPartner', __args__, opts=opts, typ=GetIntegrationAccountPartnerResult).value

    return AwaitableGetIntegrationAccountPartnerResult(
        changed_time=pulumi.get(__ret__, 'changed_time'),
        content=pulumi.get(__ret__, 'content'),
        created_time=pulumi.get(__ret__, 'created_time'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        partner_type=pulumi.get(__ret__, 'partner_type'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_integration_account_partner)
def get_integration_account_partner_output(integration_account_name: Optional[pulumi.Input[str]] = None,
                                           partner_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIntegrationAccountPartnerResult]:
    """
    Gets an integration account partner.


    :param str integration_account_name: The integration account name.
    :param str partner_name: The integration account partner name.
    :param str resource_group_name: The resource group name.
    """
    ...
