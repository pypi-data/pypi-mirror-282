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
    'GetPartnerDestinationResult',
    'AwaitableGetPartnerDestinationResult',
    'get_partner_destination',
    'get_partner_destination_output',
]

@pulumi.output_type
class GetPartnerDestinationResult:
    """
    Event Grid Partner Destination.
    """
    def __init__(__self__, activation_state=None, endpoint_base_url=None, endpoint_service_context=None, expiration_time_if_not_activated_utc=None, id=None, location=None, message_for_activation=None, name=None, partner_registration_immutable_id=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if activation_state and not isinstance(activation_state, str):
            raise TypeError("Expected argument 'activation_state' to be a str")
        pulumi.set(__self__, "activation_state", activation_state)
        if endpoint_base_url and not isinstance(endpoint_base_url, str):
            raise TypeError("Expected argument 'endpoint_base_url' to be a str")
        pulumi.set(__self__, "endpoint_base_url", endpoint_base_url)
        if endpoint_service_context and not isinstance(endpoint_service_context, str):
            raise TypeError("Expected argument 'endpoint_service_context' to be a str")
        pulumi.set(__self__, "endpoint_service_context", endpoint_service_context)
        if expiration_time_if_not_activated_utc and not isinstance(expiration_time_if_not_activated_utc, str):
            raise TypeError("Expected argument 'expiration_time_if_not_activated_utc' to be a str")
        pulumi.set(__self__, "expiration_time_if_not_activated_utc", expiration_time_if_not_activated_utc)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if message_for_activation and not isinstance(message_for_activation, str):
            raise TypeError("Expected argument 'message_for_activation' to be a str")
        pulumi.set(__self__, "message_for_activation", message_for_activation)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_registration_immutable_id and not isinstance(partner_registration_immutable_id, str):
            raise TypeError("Expected argument 'partner_registration_immutable_id' to be a str")
        pulumi.set(__self__, "partner_registration_immutable_id", partner_registration_immutable_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
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
    @pulumi.getter(name="activationState")
    def activation_state(self) -> Optional[str]:
        """
        Activation state of the partner destination.
        """
        return pulumi.get(self, "activation_state")

    @property
    @pulumi.getter(name="endpointBaseUrl")
    def endpoint_base_url(self) -> Optional[str]:
        """
        Endpoint Base URL of the partner destination
        """
        return pulumi.get(self, "endpoint_base_url")

    @property
    @pulumi.getter(name="endpointServiceContext")
    def endpoint_service_context(self) -> Optional[str]:
        """
        Endpoint context associated with this partner destination.
        """
        return pulumi.get(self, "endpoint_service_context")

    @property
    @pulumi.getter(name="expirationTimeIfNotActivatedUtc")
    def expiration_time_if_not_activated_utc(self) -> Optional[str]:
        """
        Expiration time of the partner destination. If this timer expires and the partner destination was never activated,
        the partner destination and corresponding channel are deleted.
        """
        return pulumi.get(self, "expiration_time_if_not_activated_utc")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="messageForActivation")
    def message_for_activation(self) -> Optional[str]:
        """
        Context or helpful message that can be used during the approval process.
        """
        return pulumi.get(self, "message_for_activation")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerRegistrationImmutableId")
    def partner_registration_immutable_id(self) -> Optional[str]:
        """
        The immutable Id of the corresponding partner registration.
        """
        return pulumi.get(self, "partner_registration_immutable_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the partner destination.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to Partner Destination resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPartnerDestinationResult(GetPartnerDestinationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPartnerDestinationResult(
            activation_state=self.activation_state,
            endpoint_base_url=self.endpoint_base_url,
            endpoint_service_context=self.endpoint_service_context,
            expiration_time_if_not_activated_utc=self.expiration_time_if_not_activated_utc,
            id=self.id,
            location=self.location,
            message_for_activation=self.message_for_activation,
            name=self.name,
            partner_registration_immutable_id=self.partner_registration_immutable_id,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_partner_destination(partner_destination_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPartnerDestinationResult:
    """
    Get properties of a partner destination.


    :param str partner_destination_name: Name of the partner destination.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['partnerDestinationName'] = partner_destination_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20240601preview:getPartnerDestination', __args__, opts=opts, typ=GetPartnerDestinationResult).value

    return AwaitableGetPartnerDestinationResult(
        activation_state=pulumi.get(__ret__, 'activation_state'),
        endpoint_base_url=pulumi.get(__ret__, 'endpoint_base_url'),
        endpoint_service_context=pulumi.get(__ret__, 'endpoint_service_context'),
        expiration_time_if_not_activated_utc=pulumi.get(__ret__, 'expiration_time_if_not_activated_utc'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        message_for_activation=pulumi.get(__ret__, 'message_for_activation'),
        name=pulumi.get(__ret__, 'name'),
        partner_registration_immutable_id=pulumi.get(__ret__, 'partner_registration_immutable_id'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_partner_destination)
def get_partner_destination_output(partner_destination_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPartnerDestinationResult]:
    """
    Get properties of a partner destination.


    :param str partner_destination_name: Name of the partner destination.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
