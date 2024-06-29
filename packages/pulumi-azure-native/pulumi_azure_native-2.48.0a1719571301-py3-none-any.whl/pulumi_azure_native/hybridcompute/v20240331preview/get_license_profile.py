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
    'GetLicenseProfileResult',
    'AwaitableGetLicenseProfileResult',
    'get_license_profile',
    'get_license_profile_output',
]

@pulumi.output_type
class GetLicenseProfileResult:
    """
    Describes a license profile in a hybrid machine.
    """
    def __init__(__self__, assigned_license=None, assigned_license_immutable_id=None, billing_start_date=None, disenrollment_date=None, enrollment_date=None, esu_eligibility=None, esu_key_state=None, esu_keys=None, id=None, location=None, name=None, product_features=None, product_type=None, provisioning_state=None, server_type=None, software_assurance_customer=None, subscription_status=None, system_data=None, tags=None, type=None):
        if assigned_license and not isinstance(assigned_license, str):
            raise TypeError("Expected argument 'assigned_license' to be a str")
        pulumi.set(__self__, "assigned_license", assigned_license)
        if assigned_license_immutable_id and not isinstance(assigned_license_immutable_id, str):
            raise TypeError("Expected argument 'assigned_license_immutable_id' to be a str")
        pulumi.set(__self__, "assigned_license_immutable_id", assigned_license_immutable_id)
        if billing_start_date and not isinstance(billing_start_date, str):
            raise TypeError("Expected argument 'billing_start_date' to be a str")
        pulumi.set(__self__, "billing_start_date", billing_start_date)
        if disenrollment_date and not isinstance(disenrollment_date, str):
            raise TypeError("Expected argument 'disenrollment_date' to be a str")
        pulumi.set(__self__, "disenrollment_date", disenrollment_date)
        if enrollment_date and not isinstance(enrollment_date, str):
            raise TypeError("Expected argument 'enrollment_date' to be a str")
        pulumi.set(__self__, "enrollment_date", enrollment_date)
        if esu_eligibility and not isinstance(esu_eligibility, str):
            raise TypeError("Expected argument 'esu_eligibility' to be a str")
        pulumi.set(__self__, "esu_eligibility", esu_eligibility)
        if esu_key_state and not isinstance(esu_key_state, str):
            raise TypeError("Expected argument 'esu_key_state' to be a str")
        pulumi.set(__self__, "esu_key_state", esu_key_state)
        if esu_keys and not isinstance(esu_keys, list):
            raise TypeError("Expected argument 'esu_keys' to be a list")
        pulumi.set(__self__, "esu_keys", esu_keys)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if product_features and not isinstance(product_features, list):
            raise TypeError("Expected argument 'product_features' to be a list")
        pulumi.set(__self__, "product_features", product_features)
        if product_type and not isinstance(product_type, str):
            raise TypeError("Expected argument 'product_type' to be a str")
        pulumi.set(__self__, "product_type", product_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if server_type and not isinstance(server_type, str):
            raise TypeError("Expected argument 'server_type' to be a str")
        pulumi.set(__self__, "server_type", server_type)
        if software_assurance_customer and not isinstance(software_assurance_customer, bool):
            raise TypeError("Expected argument 'software_assurance_customer' to be a bool")
        pulumi.set(__self__, "software_assurance_customer", software_assurance_customer)
        if subscription_status and not isinstance(subscription_status, str):
            raise TypeError("Expected argument 'subscription_status' to be a str")
        pulumi.set(__self__, "subscription_status", subscription_status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="assignedLicense")
    def assigned_license(self) -> Optional[str]:
        """
        The resource id of the license.
        """
        return pulumi.get(self, "assigned_license")

    @property
    @pulumi.getter(name="assignedLicenseImmutableId")
    def assigned_license_immutable_id(self) -> str:
        """
        The guid id of the license.
        """
        return pulumi.get(self, "assigned_license_immutable_id")

    @property
    @pulumi.getter(name="billingStartDate")
    def billing_start_date(self) -> str:
        """
        The timestamp in UTC when the billing starts.
        """
        return pulumi.get(self, "billing_start_date")

    @property
    @pulumi.getter(name="disenrollmentDate")
    def disenrollment_date(self) -> str:
        """
        The timestamp in UTC when the user disenrolled the feature.
        """
        return pulumi.get(self, "disenrollment_date")

    @property
    @pulumi.getter(name="enrollmentDate")
    def enrollment_date(self) -> str:
        """
        The timestamp in UTC when the user enrolls the feature.
        """
        return pulumi.get(self, "enrollment_date")

    @property
    @pulumi.getter(name="esuEligibility")
    def esu_eligibility(self) -> str:
        """
        Indicates the eligibility state of Esu.
        """
        return pulumi.get(self, "esu_eligibility")

    @property
    @pulumi.getter(name="esuKeyState")
    def esu_key_state(self) -> str:
        """
        Indicates whether there is an ESU Key currently active for the machine.
        """
        return pulumi.get(self, "esu_key_state")

    @property
    @pulumi.getter(name="esuKeys")
    def esu_keys(self) -> Sequence['outputs.EsuKeyResponse']:
        """
        The list of ESU keys.
        """
        return pulumi.get(self, "esu_keys")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="productFeatures")
    def product_features(self) -> Optional[Sequence['outputs.ProductFeatureResponse']]:
        """
        The list of product features.
        """
        return pulumi.get(self, "product_features")

    @property
    @pulumi.getter(name="productType")
    def product_type(self) -> Optional[str]:
        """
        Indicates the product type of the license.
        """
        return pulumi.get(self, "product_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> str:
        """
        The type of the Esu servers.
        """
        return pulumi.get(self, "server_type")

    @property
    @pulumi.getter(name="softwareAssuranceCustomer")
    def software_assurance_customer(self) -> Optional[bool]:
        """
        Specifies if this machine is licensed as part of a Software Assurance agreement.
        """
        return pulumi.get(self, "software_assurance_customer")

    @property
    @pulumi.getter(name="subscriptionStatus")
    def subscription_status(self) -> Optional[str]:
        """
        Indicates the subscription status of the product.
        """
        return pulumi.get(self, "subscription_status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetLicenseProfileResult(GetLicenseProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLicenseProfileResult(
            assigned_license=self.assigned_license,
            assigned_license_immutable_id=self.assigned_license_immutable_id,
            billing_start_date=self.billing_start_date,
            disenrollment_date=self.disenrollment_date,
            enrollment_date=self.enrollment_date,
            esu_eligibility=self.esu_eligibility,
            esu_key_state=self.esu_key_state,
            esu_keys=self.esu_keys,
            id=self.id,
            location=self.location,
            name=self.name,
            product_features=self.product_features,
            product_type=self.product_type,
            provisioning_state=self.provisioning_state,
            server_type=self.server_type,
            software_assurance_customer=self.software_assurance_customer,
            subscription_status=self.subscription_status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_license_profile(license_profile_name: Optional[str] = None,
                        machine_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLicenseProfileResult:
    """
    Retrieves information about the view of a license profile.


    :param str license_profile_name: The name of the license profile.
    :param str machine_name: The name of the hybrid machine.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['licenseProfileName'] = license_profile_name
    __args__['machineName'] = machine_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridcompute/v20240331preview:getLicenseProfile', __args__, opts=opts, typ=GetLicenseProfileResult).value

    return AwaitableGetLicenseProfileResult(
        assigned_license=pulumi.get(__ret__, 'assigned_license'),
        assigned_license_immutable_id=pulumi.get(__ret__, 'assigned_license_immutable_id'),
        billing_start_date=pulumi.get(__ret__, 'billing_start_date'),
        disenrollment_date=pulumi.get(__ret__, 'disenrollment_date'),
        enrollment_date=pulumi.get(__ret__, 'enrollment_date'),
        esu_eligibility=pulumi.get(__ret__, 'esu_eligibility'),
        esu_key_state=pulumi.get(__ret__, 'esu_key_state'),
        esu_keys=pulumi.get(__ret__, 'esu_keys'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        product_features=pulumi.get(__ret__, 'product_features'),
        product_type=pulumi.get(__ret__, 'product_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        server_type=pulumi.get(__ret__, 'server_type'),
        software_assurance_customer=pulumi.get(__ret__, 'software_assurance_customer'),
        subscription_status=pulumi.get(__ret__, 'subscription_status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_license_profile)
def get_license_profile_output(license_profile_name: Optional[pulumi.Input[str]] = None,
                               machine_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLicenseProfileResult]:
    """
    Retrieves information about the view of a license profile.


    :param str license_profile_name: The name of the license profile.
    :param str machine_name: The name of the hybrid machine.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
