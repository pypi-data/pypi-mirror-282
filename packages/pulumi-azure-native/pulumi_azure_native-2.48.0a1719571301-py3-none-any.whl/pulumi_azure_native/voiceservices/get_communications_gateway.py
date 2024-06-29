# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetCommunicationsGatewayResult',
    'AwaitableGetCommunicationsGatewayResult',
    'get_communications_gateway',
    'get_communications_gateway_output',
]

@pulumi.output_type
class GetCommunicationsGatewayResult:
    """
    A CommunicationsGateway resource
    """
    def __init__(__self__, api_bridge=None, auto_generated_domain_name_label=None, auto_generated_domain_name_label_scope=None, codecs=None, connectivity=None, e911_type=None, emergency_dial_strings=None, id=None, identity=None, integrated_mcp_enabled=None, location=None, name=None, on_prem_mcp_enabled=None, platforms=None, provisioning_state=None, service_locations=None, status=None, system_data=None, tags=None, teams_voicemail_pilot_number=None, type=None):
        if api_bridge and not isinstance(api_bridge, dict):
            raise TypeError("Expected argument 'api_bridge' to be a dict")
        pulumi.set(__self__, "api_bridge", api_bridge)
        if auto_generated_domain_name_label and not isinstance(auto_generated_domain_name_label, str):
            raise TypeError("Expected argument 'auto_generated_domain_name_label' to be a str")
        pulumi.set(__self__, "auto_generated_domain_name_label", auto_generated_domain_name_label)
        if auto_generated_domain_name_label_scope and not isinstance(auto_generated_domain_name_label_scope, str):
            raise TypeError("Expected argument 'auto_generated_domain_name_label_scope' to be a str")
        pulumi.set(__self__, "auto_generated_domain_name_label_scope", auto_generated_domain_name_label_scope)
        if codecs and not isinstance(codecs, list):
            raise TypeError("Expected argument 'codecs' to be a list")
        pulumi.set(__self__, "codecs", codecs)
        if connectivity and not isinstance(connectivity, str):
            raise TypeError("Expected argument 'connectivity' to be a str")
        pulumi.set(__self__, "connectivity", connectivity)
        if e911_type and not isinstance(e911_type, str):
            raise TypeError("Expected argument 'e911_type' to be a str")
        pulumi.set(__self__, "e911_type", e911_type)
        if emergency_dial_strings and not isinstance(emergency_dial_strings, list):
            raise TypeError("Expected argument 'emergency_dial_strings' to be a list")
        pulumi.set(__self__, "emergency_dial_strings", emergency_dial_strings)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if integrated_mcp_enabled and not isinstance(integrated_mcp_enabled, bool):
            raise TypeError("Expected argument 'integrated_mcp_enabled' to be a bool")
        pulumi.set(__self__, "integrated_mcp_enabled", integrated_mcp_enabled)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if on_prem_mcp_enabled and not isinstance(on_prem_mcp_enabled, bool):
            raise TypeError("Expected argument 'on_prem_mcp_enabled' to be a bool")
        pulumi.set(__self__, "on_prem_mcp_enabled", on_prem_mcp_enabled)
        if platforms and not isinstance(platforms, list):
            raise TypeError("Expected argument 'platforms' to be a list")
        pulumi.set(__self__, "platforms", platforms)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_locations and not isinstance(service_locations, list):
            raise TypeError("Expected argument 'service_locations' to be a list")
        pulumi.set(__self__, "service_locations", service_locations)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if teams_voicemail_pilot_number and not isinstance(teams_voicemail_pilot_number, str):
            raise TypeError("Expected argument 'teams_voicemail_pilot_number' to be a str")
        pulumi.set(__self__, "teams_voicemail_pilot_number", teams_voicemail_pilot_number)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="apiBridge")
    def api_bridge(self) -> Optional[Any]:
        """
        Details of API bridge functionality, if required
        """
        return pulumi.get(self, "api_bridge")

    @property
    @pulumi.getter(name="autoGeneratedDomainNameLabel")
    def auto_generated_domain_name_label(self) -> str:
        """
        The autogenerated label used as part of the FQDNs for accessing the Communications Gateway
        """
        return pulumi.get(self, "auto_generated_domain_name_label")

    @property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(self) -> Optional[str]:
        """
        The scope at which the auto-generated domain name can be re-used
        """
        return pulumi.get(self, "auto_generated_domain_name_label_scope")

    @property
    @pulumi.getter
    def codecs(self) -> Sequence[str]:
        """
        Voice codecs to support
        """
        return pulumi.get(self, "codecs")

    @property
    @pulumi.getter
    def connectivity(self) -> str:
        """
        How to connect back to the operator network, e.g. MAPS
        """
        return pulumi.get(self, "connectivity")

    @property
    @pulumi.getter(name="e911Type")
    def e911_type(self) -> str:
        """
        How to handle 911 calls
        """
        return pulumi.get(self, "e911_type")

    @property
    @pulumi.getter(name="emergencyDialStrings")
    def emergency_dial_strings(self) -> Optional[Sequence[str]]:
        """
        A list of dial strings used for emergency calling.
        """
        return pulumi.get(self, "emergency_dial_strings")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="integratedMcpEnabled")
    def integrated_mcp_enabled(self) -> Optional[bool]:
        """
        Whether an integrated Mobile Control Point is in use.
        """
        return pulumi.get(self, "integrated_mcp_enabled")

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
    @pulumi.getter(name="onPremMcpEnabled")
    def on_prem_mcp_enabled(self) -> Optional[bool]:
        """
        Whether an on-premises Mobile Control Point is in use.
        """
        return pulumi.get(self, "on_prem_mcp_enabled")

    @property
    @pulumi.getter
    def platforms(self) -> Sequence[str]:
        """
        What platforms to support
        """
        return pulumi.get(self, "platforms")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceLocations")
    def service_locations(self) -> Sequence['outputs.ServiceRegionPropertiesResponse']:
        """
        The regions in which to deploy the resources needed for Teams Calling
        """
        return pulumi.get(self, "service_locations")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The current status of the deployment.
        """
        return pulumi.get(self, "status")

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
    @pulumi.getter(name="teamsVoicemailPilotNumber")
    def teams_voicemail_pilot_number(self) -> Optional[str]:
        """
        This number is used in Teams Phone Mobile scenarios for access to the voicemail IVR from the native dialer.
        """
        return pulumi.get(self, "teams_voicemail_pilot_number")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetCommunicationsGatewayResult(GetCommunicationsGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCommunicationsGatewayResult(
            api_bridge=self.api_bridge,
            auto_generated_domain_name_label=self.auto_generated_domain_name_label,
            auto_generated_domain_name_label_scope=self.auto_generated_domain_name_label_scope,
            codecs=self.codecs,
            connectivity=self.connectivity,
            e911_type=self.e911_type,
            emergency_dial_strings=self.emergency_dial_strings,
            id=self.id,
            identity=self.identity,
            integrated_mcp_enabled=self.integrated_mcp_enabled,
            location=self.location,
            name=self.name,
            on_prem_mcp_enabled=self.on_prem_mcp_enabled,
            platforms=self.platforms,
            provisioning_state=self.provisioning_state,
            service_locations=self.service_locations,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            teams_voicemail_pilot_number=self.teams_voicemail_pilot_number,
            type=self.type)


def get_communications_gateway(communications_gateway_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCommunicationsGatewayResult:
    """
    Get a CommunicationsGateway
    Azure REST API version: 2023-04-03.

    Other available API versions: 2023-09-01.


    :param str communications_gateway_name: Unique identifier for this deployment
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['communicationsGatewayName'] = communications_gateway_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:voiceservices:getCommunicationsGateway', __args__, opts=opts, typ=GetCommunicationsGatewayResult).value

    return AwaitableGetCommunicationsGatewayResult(
        api_bridge=pulumi.get(__ret__, 'api_bridge'),
        auto_generated_domain_name_label=pulumi.get(__ret__, 'auto_generated_domain_name_label'),
        auto_generated_domain_name_label_scope=pulumi.get(__ret__, 'auto_generated_domain_name_label_scope'),
        codecs=pulumi.get(__ret__, 'codecs'),
        connectivity=pulumi.get(__ret__, 'connectivity'),
        e911_type=pulumi.get(__ret__, 'e911_type'),
        emergency_dial_strings=pulumi.get(__ret__, 'emergency_dial_strings'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        integrated_mcp_enabled=pulumi.get(__ret__, 'integrated_mcp_enabled'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        on_prem_mcp_enabled=pulumi.get(__ret__, 'on_prem_mcp_enabled'),
        platforms=pulumi.get(__ret__, 'platforms'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        service_locations=pulumi.get(__ret__, 'service_locations'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        teams_voicemail_pilot_number=pulumi.get(__ret__, 'teams_voicemail_pilot_number'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_communications_gateway)
def get_communications_gateway_output(communications_gateway_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCommunicationsGatewayResult]:
    """
    Get a CommunicationsGateway
    Azure REST API version: 2023-04-03.

    Other available API versions: 2023-09-01.


    :param str communications_gateway_name: Unique identifier for this deployment
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
