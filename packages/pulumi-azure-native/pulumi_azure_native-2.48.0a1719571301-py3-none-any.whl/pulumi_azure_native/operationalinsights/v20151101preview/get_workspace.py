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
    'GetWorkspaceResult',
    'AwaitableGetWorkspaceResult',
    'get_workspace',
    'get_workspace_output',
]

@pulumi.output_type
class GetWorkspaceResult:
    """
    The top level Workspace resource container.
    """
    def __init__(__self__, customer_id=None, e_tag=None, id=None, location=None, name=None, portal_url=None, provisioning_state=None, retention_in_days=None, sku=None, source=None, tags=None, type=None):
        if customer_id and not isinstance(customer_id, str):
            raise TypeError("Expected argument 'customer_id' to be a str")
        pulumi.set(__self__, "customer_id", customer_id)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if portal_url and not isinstance(portal_url, str):
            raise TypeError("Expected argument 'portal_url' to be a str")
        pulumi.set(__self__, "portal_url", portal_url)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if retention_in_days and not isinstance(retention_in_days, int):
            raise TypeError("Expected argument 'retention_in_days' to be a int")
        pulumi.set(__self__, "retention_in_days", retention_in_days)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> str:
        """
        This is a read-only property. Represents the ID associated with the workspace.
        """
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        The ETag of the workspace.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portalUrl")
    def portal_url(self) -> str:
        """
        This is a legacy property and is not used anymore. Kept here for backward compatibility.
        """
        return pulumi.get(self, "portal_url")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning state of the workspace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[int]:
        """
        The workspace data retention in days. -1 means Unlimited retention for the Unlimited Sku. 730 days is the maximum allowed for all other Skus. 
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The SKU of the workspace.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        This is a read-only legacy property. It is always set to 'Azure' by the service. Kept here for backward compatibility.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceResult(
            customer_id=self.customer_id,
            e_tag=self.e_tag,
            id=self.id,
            location=self.location,
            name=self.name,
            portal_url=self.portal_url,
            provisioning_state=self.provisioning_state,
            retention_in_days=self.retention_in_days,
            sku=self.sku,
            source=self.source,
            tags=self.tags,
            type=self.type)


def get_workspace(resource_group_name: Optional[str] = None,
                  workspace_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceResult:
    """
    Gets a workspace instance.


    :param str resource_group_name: The resource group name of the workspace.
    :param str workspace_name: Name of the Log Analytics Workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights/v20151101preview:getWorkspace', __args__, opts=opts, typ=GetWorkspaceResult).value

    return AwaitableGetWorkspaceResult(
        customer_id=pulumi.get(__ret__, 'customer_id'),
        e_tag=pulumi.get(__ret__, 'e_tag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        portal_url=pulumi.get(__ret__, 'portal_url'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        retention_in_days=pulumi.get(__ret__, 'retention_in_days'),
        sku=pulumi.get(__ret__, 'sku'),
        source=pulumi.get(__ret__, 'source'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace)
def get_workspace_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                         workspace_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceResult]:
    """
    Gets a workspace instance.


    :param str resource_group_name: The resource group name of the workspace.
    :param str workspace_name: Name of the Log Analytics Workspace.
    """
    ...
