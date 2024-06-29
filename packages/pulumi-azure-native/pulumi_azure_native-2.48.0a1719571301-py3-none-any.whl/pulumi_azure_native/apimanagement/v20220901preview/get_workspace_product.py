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
    'GetWorkspaceProductResult',
    'AwaitableGetWorkspaceProductResult',
    'get_workspace_product',
    'get_workspace_product_output',
]

@pulumi.output_type
class GetWorkspaceProductResult:
    """
    Product details.
    """
    def __init__(__self__, approval_required=None, description=None, display_name=None, id=None, name=None, state=None, subscription_required=None, subscriptions_limit=None, terms=None, type=None):
        if approval_required and not isinstance(approval_required, bool):
            raise TypeError("Expected argument 'approval_required' to be a bool")
        pulumi.set(__self__, "approval_required", approval_required)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if subscription_required and not isinstance(subscription_required, bool):
            raise TypeError("Expected argument 'subscription_required' to be a bool")
        pulumi.set(__self__, "subscription_required", subscription_required)
        if subscriptions_limit and not isinstance(subscriptions_limit, int):
            raise TypeError("Expected argument 'subscriptions_limit' to be a int")
        pulumi.set(__self__, "subscriptions_limit", subscriptions_limit)
        if terms and not isinstance(terms, str):
            raise TypeError("Expected argument 'terms' to be a str")
        pulumi.set(__self__, "terms", terms)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="approvalRequired")
    def approval_required(self) -> Optional[bool]:
        """
        whether subscription approval is required. If false, new subscriptions will be approved automatically enabling developers to call the product’s APIs immediately after subscribing. If true, administrators must manually approve the subscription before the developer can any of the product’s APIs. Can be present only if subscriptionRequired property is present and has a value of false.
        """
        return pulumi.get(self, "approval_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Product description. May include HTML formatting tags.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Product name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        whether product is published or not. Published products are discoverable by users of developer portal. Non published products are visible only to administrators. Default state of Product is notPublished.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="subscriptionRequired")
    def subscription_required(self) -> Optional[bool]:
        """
        Whether a product subscription is required for accessing APIs included in this product. If true, the product is referred to as "protected" and a valid subscription key is required for a request to an API included in the product to succeed. If false, the product is referred to as "open" and requests to an API included in the product can be made without a subscription key. If property is omitted when creating a new product it's value is assumed to be true.
        """
        return pulumi.get(self, "subscription_required")

    @property
    @pulumi.getter(name="subscriptionsLimit")
    def subscriptions_limit(self) -> Optional[int]:
        """
        Whether the number of subscriptions a user can have to this product at the same time. Set to null or omit to allow unlimited per user subscriptions. Can be present only if subscriptionRequired property is present and has a value of false.
        """
        return pulumi.get(self, "subscriptions_limit")

    @property
    @pulumi.getter
    def terms(self) -> Optional[str]:
        """
        Product terms of use. Developers trying to subscribe to the product will be presented and required to accept these terms before they can complete the subscription process.
        """
        return pulumi.get(self, "terms")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceProductResult(GetWorkspaceProductResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceProductResult(
            approval_required=self.approval_required,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            state=self.state,
            subscription_required=self.subscription_required,
            subscriptions_limit=self.subscriptions_limit,
            terms=self.terms,
            type=self.type)


def get_workspace_product(product_id: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          service_name: Optional[str] = None,
                          workspace_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceProductResult:
    """
    Gets the details of the product specified by its identifier.


    :param str product_id: Product identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    __args__ = dict()
    __args__['productId'] = product_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['workspaceId'] = workspace_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220901preview:getWorkspaceProduct', __args__, opts=opts, typ=GetWorkspaceProductResult).value

    return AwaitableGetWorkspaceProductResult(
        approval_required=pulumi.get(__ret__, 'approval_required'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        subscription_required=pulumi.get(__ret__, 'subscription_required'),
        subscriptions_limit=pulumi.get(__ret__, 'subscriptions_limit'),
        terms=pulumi.get(__ret__, 'terms'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workspace_product)
def get_workspace_product_output(product_id: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 service_name: Optional[pulumi.Input[str]] = None,
                                 workspace_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceProductResult]:
    """
    Gets the details of the product specified by its identifier.


    :param str product_id: Product identifier. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    :param str workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
    """
    ...
