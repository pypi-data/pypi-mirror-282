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
    'GetB2CTenantResult',
    'AwaitableGetB2CTenantResult',
    'get_b2_c_tenant',
    'get_b2_c_tenant_output',
]

@pulumi.output_type
class GetB2CTenantResult:
    def __init__(__self__, billing_config=None, id=None, is_go_local_tenant=None, location=None, name=None, sku=None, system_data=None, tags=None, tenant_id=None, type=None):
        if billing_config and not isinstance(billing_config, dict):
            raise TypeError("Expected argument 'billing_config' to be a dict")
        pulumi.set(__self__, "billing_config", billing_config)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_go_local_tenant and not isinstance(is_go_local_tenant, bool):
            raise TypeError("Expected argument 'is_go_local_tenant' to be a bool")
        pulumi.set(__self__, "is_go_local_tenant", is_go_local_tenant)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="billingConfig")
    def billing_config(self) -> Optional['outputs.B2CTenantResourcePropertiesResponseBillingConfig']:
        """
        The billing configuration for the tenant.
        """
        return pulumi.get(self, "billing_config")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An identifier that represents the Azure AD B2C tenant resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isGoLocalTenant")
    def is_go_local_tenant(self) -> Optional[bool]:
        """
        Enable GoLocal add-on to store data at rest in the specific Geo. Refer to [aka.ms/B2CDataResidency](https://aka.ms/B2CDataResidency) to see local data residency options.
        """
        return pulumi.get(self, "is_go_local_tenant")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location in which the resource is hosted and data resides. Can be one of 'United States', 'Europe', 'Asia Pacific', or 'Australia'. Refer to [this documentation](https://aka.ms/B2CDataResidency) for more information.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Azure AD B2C tenant resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.B2CResourceSKUResponse':
        """
        SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling).
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource Tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        An identifier of the Azure AD B2C tenant.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the B2C tenant resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetB2CTenantResult(GetB2CTenantResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetB2CTenantResult(
            billing_config=self.billing_config,
            id=self.id,
            is_go_local_tenant=self.is_go_local_tenant,
            location=self.location,
            name=self.name,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            tenant_id=self.tenant_id,
            type=self.type)


def get_b2_c_tenant(resource_group_name: Optional[str] = None,
                    resource_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetB2CTenantResult:
    """
    Get the Azure AD B2C tenant resource.


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The initial domain name of the Azure AD B2C tenant.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azureactivedirectory/v20230517preview:getB2CTenant', __args__, opts=opts, typ=GetB2CTenantResult).value

    return AwaitableGetB2CTenantResult(
        billing_config=pulumi.get(__ret__, 'billing_config'),
        id=pulumi.get(__ret__, 'id'),
        is_go_local_tenant=pulumi.get(__ret__, 'is_go_local_tenant'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_b2_c_tenant)
def get_b2_c_tenant_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                           resource_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetB2CTenantResult]:
    """
    Get the Azure AD B2C tenant resource.


    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The initial domain name of the Azure AD B2C tenant.
    """
    ...
