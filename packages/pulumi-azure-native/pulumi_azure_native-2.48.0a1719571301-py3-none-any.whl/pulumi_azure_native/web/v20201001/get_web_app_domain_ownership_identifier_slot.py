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
    'GetWebAppDomainOwnershipIdentifierSlotResult',
    'AwaitableGetWebAppDomainOwnershipIdentifierSlotResult',
    'get_web_app_domain_ownership_identifier_slot',
    'get_web_app_domain_ownership_identifier_slot_output',
]

@pulumi.output_type
class GetWebAppDomainOwnershipIdentifierSlotResult:
    """
    A domain specific resource identifier.
    """
    def __init__(__self__, id=None, kind=None, name=None, system_data=None, type=None, value=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        String representation of the identity.
        """
        return pulumi.get(self, "value")


class AwaitableGetWebAppDomainOwnershipIdentifierSlotResult(GetWebAppDomainOwnershipIdentifierSlotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAppDomainOwnershipIdentifierSlotResult(
            id=self.id,
            kind=self.kind,
            name=self.name,
            system_data=self.system_data,
            type=self.type,
            value=self.value)


def get_web_app_domain_ownership_identifier_slot(domain_ownership_identifier_name: Optional[str] = None,
                                                 name: Optional[str] = None,
                                                 resource_group_name: Optional[str] = None,
                                                 slot: Optional[str] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAppDomainOwnershipIdentifierSlotResult:
    """
    Get domain ownership identifier for web app.


    :param str domain_ownership_identifier_name: Name of domain ownership identifier.
    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    """
    __args__ = dict()
    __args__['domainOwnershipIdentifierName'] = domain_ownership_identifier_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['slot'] = slot
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20201001:getWebAppDomainOwnershipIdentifierSlot', __args__, opts=opts, typ=GetWebAppDomainOwnershipIdentifierSlotResult).value

    return AwaitableGetWebAppDomainOwnershipIdentifierSlotResult(
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_web_app_domain_ownership_identifier_slot)
def get_web_app_domain_ownership_identifier_slot_output(domain_ownership_identifier_name: Optional[pulumi.Input[str]] = None,
                                                        name: Optional[pulumi.Input[str]] = None,
                                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                                        slot: Optional[pulumi.Input[str]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAppDomainOwnershipIdentifierSlotResult]:
    """
    Get domain ownership identifier for web app.


    :param str domain_ownership_identifier_name: Name of domain ownership identifier.
    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    """
    ...
