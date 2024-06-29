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
    'GetLocalRulestackResult',
    'AwaitableGetLocalRulestackResult',
    'get_local_rulestack',
    'get_local_rulestack_output',
]

@pulumi.output_type
class GetLocalRulestackResult:
    """
    PaloAltoNetworks LocalRulestack
    """
    def __init__(__self__, associated_subscriptions=None, default_mode=None, description=None, id=None, identity=None, location=None, min_app_id_version=None, name=None, pan_etag=None, pan_location=None, provisioning_state=None, scope=None, security_services=None, system_data=None, tags=None, type=None):
        if associated_subscriptions and not isinstance(associated_subscriptions, list):
            raise TypeError("Expected argument 'associated_subscriptions' to be a list")
        pulumi.set(__self__, "associated_subscriptions", associated_subscriptions)
        if default_mode and not isinstance(default_mode, str):
            raise TypeError("Expected argument 'default_mode' to be a str")
        pulumi.set(__self__, "default_mode", default_mode)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if min_app_id_version and not isinstance(min_app_id_version, str):
            raise TypeError("Expected argument 'min_app_id_version' to be a str")
        pulumi.set(__self__, "min_app_id_version", min_app_id_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pan_etag and not isinstance(pan_etag, str):
            raise TypeError("Expected argument 'pan_etag' to be a str")
        pulumi.set(__self__, "pan_etag", pan_etag)
        if pan_location and not isinstance(pan_location, str):
            raise TypeError("Expected argument 'pan_location' to be a str")
        pulumi.set(__self__, "pan_location", pan_location)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if security_services and not isinstance(security_services, dict):
            raise TypeError("Expected argument 'security_services' to be a dict")
        pulumi.set(__self__, "security_services", security_services)
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
    @pulumi.getter(name="associatedSubscriptions")
    def associated_subscriptions(self) -> Optional[Sequence[str]]:
        """
        subscription scope of global rulestack
        """
        return pulumi.get(self, "associated_subscriptions")

    @property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[str]:
        """
        Mode for default rules creation
        """
        return pulumi.get(self, "default_mode")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        rulestack description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.AzureResourceManagerManagedIdentityPropertiesResponse']:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minAppIdVersion")
    def min_app_id_version(self) -> Optional[str]:
        """
        minimum version
        """
        return pulumi.get(self, "min_app_id_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="panEtag")
    def pan_etag(self) -> Optional[str]:
        """
        PanEtag info
        """
        return pulumi.get(self, "pan_etag")

    @property
    @pulumi.getter(name="panLocation")
    def pan_location(self) -> Optional[str]:
        """
        Rulestack Location, Required for GlobalRulestacks, Not for LocalRulestacks
        """
        return pulumi.get(self, "pan_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        Rulestack Type
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="securityServices")
    def security_services(self) -> Optional['outputs.SecurityServicesResponse']:
        """
        Security Profile
        """
        return pulumi.get(self, "security_services")

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


class AwaitableGetLocalRulestackResult(GetLocalRulestackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalRulestackResult(
            associated_subscriptions=self.associated_subscriptions,
            default_mode=self.default_mode,
            description=self.description,
            id=self.id,
            identity=self.identity,
            location=self.location,
            min_app_id_version=self.min_app_id_version,
            name=self.name,
            pan_etag=self.pan_etag,
            pan_location=self.pan_location,
            provisioning_state=self.provisioning_state,
            scope=self.scope,
            security_services=self.security_services,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_local_rulestack(local_rulestack_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalRulestackResult:
    """
    Get a LocalRulestackResource


    :param str local_rulestack_name: LocalRulestack resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['localRulestackName'] = local_rulestack_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20220829:getLocalRulestack', __args__, opts=opts, typ=GetLocalRulestackResult).value

    return AwaitableGetLocalRulestackResult(
        associated_subscriptions=pulumi.get(__ret__, 'associated_subscriptions'),
        default_mode=pulumi.get(__ret__, 'default_mode'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        min_app_id_version=pulumi.get(__ret__, 'min_app_id_version'),
        name=pulumi.get(__ret__, 'name'),
        pan_etag=pulumi.get(__ret__, 'pan_etag'),
        pan_location=pulumi.get(__ret__, 'pan_location'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        scope=pulumi.get(__ret__, 'scope'),
        security_services=pulumi.get(__ret__, 'security_services'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_local_rulestack)
def get_local_rulestack_output(local_rulestack_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocalRulestackResult]:
    """
    Get a LocalRulestackResource


    :param str local_rulestack_name: LocalRulestack resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
