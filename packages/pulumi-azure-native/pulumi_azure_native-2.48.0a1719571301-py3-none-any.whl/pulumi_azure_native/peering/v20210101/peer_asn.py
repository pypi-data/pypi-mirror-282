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
from ._enums import *
from ._inputs import *

__all__ = ['PeerAsnArgs', 'PeerAsn']

@pulumi.input_type
class PeerAsnArgs:
    def __init__(__self__, *,
                 peer_asn: Optional[pulumi.Input[int]] = None,
                 peer_asn_name: Optional[pulumi.Input[str]] = None,
                 peer_contact_detail: Optional[pulumi.Input[Sequence[pulumi.Input['ContactDetailArgs']]]] = None,
                 peer_name: Optional[pulumi.Input[str]] = None,
                 validation_state: Optional[pulumi.Input[Union[str, 'ValidationState']]] = None):
        """
        The set of arguments for constructing a PeerAsn resource.
        :param pulumi.Input[int] peer_asn: The Autonomous System Number (ASN) of the peer.
        :param pulumi.Input[str] peer_asn_name: The peer ASN name.
        :param pulumi.Input[Sequence[pulumi.Input['ContactDetailArgs']]] peer_contact_detail: The contact details of the peer.
        :param pulumi.Input[str] peer_name: The name of the peer.
        :param pulumi.Input[Union[str, 'ValidationState']] validation_state: The validation state of the ASN associated with the peer.
        """
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)
        if peer_asn_name is not None:
            pulumi.set(__self__, "peer_asn_name", peer_asn_name)
        if peer_contact_detail is not None:
            pulumi.set(__self__, "peer_contact_detail", peer_contact_detail)
        if peer_name is not None:
            pulumi.set(__self__, "peer_name", peer_name)
        if validation_state is not None:
            pulumi.set(__self__, "validation_state", validation_state)

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> Optional[pulumi.Input[int]]:
        """
        The Autonomous System Number (ASN) of the peer.
        """
        return pulumi.get(self, "peer_asn")

    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "peer_asn", value)

    @property
    @pulumi.getter(name="peerAsnName")
    def peer_asn_name(self) -> Optional[pulumi.Input[str]]:
        """
        The peer ASN name.
        """
        return pulumi.get(self, "peer_asn_name")

    @peer_asn_name.setter
    def peer_asn_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_asn_name", value)

    @property
    @pulumi.getter(name="peerContactDetail")
    def peer_contact_detail(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContactDetailArgs']]]]:
        """
        The contact details of the peer.
        """
        return pulumi.get(self, "peer_contact_detail")

    @peer_contact_detail.setter
    def peer_contact_detail(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContactDetailArgs']]]]):
        pulumi.set(self, "peer_contact_detail", value)

    @property
    @pulumi.getter(name="peerName")
    def peer_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peer.
        """
        return pulumi.get(self, "peer_name")

    @peer_name.setter
    def peer_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_name", value)

    @property
    @pulumi.getter(name="validationState")
    def validation_state(self) -> Optional[pulumi.Input[Union[str, 'ValidationState']]]:
        """
        The validation state of the ASN associated with the peer.
        """
        return pulumi.get(self, "validation_state")

    @validation_state.setter
    def validation_state(self, value: Optional[pulumi.Input[Union[str, 'ValidationState']]]):
        pulumi.set(self, "validation_state", value)


class PeerAsn(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 peer_asn: Optional[pulumi.Input[int]] = None,
                 peer_asn_name: Optional[pulumi.Input[str]] = None,
                 peer_contact_detail: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactDetailArgs']]]]] = None,
                 peer_name: Optional[pulumi.Input[str]] = None,
                 validation_state: Optional[pulumi.Input[Union[str, 'ValidationState']]] = None,
                 __props__=None):
        """
        The essential information related to the peer's ASN.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] peer_asn: The Autonomous System Number (ASN) of the peer.
        :param pulumi.Input[str] peer_asn_name: The peer ASN name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactDetailArgs']]]] peer_contact_detail: The contact details of the peer.
        :param pulumi.Input[str] peer_name: The name of the peer.
        :param pulumi.Input[Union[str, 'ValidationState']] validation_state: The validation state of the ASN associated with the peer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PeerAsnArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The essential information related to the peer's ASN.

        :param str resource_name: The name of the resource.
        :param PeerAsnArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PeerAsnArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 peer_asn: Optional[pulumi.Input[int]] = None,
                 peer_asn_name: Optional[pulumi.Input[str]] = None,
                 peer_contact_detail: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContactDetailArgs']]]]] = None,
                 peer_name: Optional[pulumi.Input[str]] = None,
                 validation_state: Optional[pulumi.Input[Union[str, 'ValidationState']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PeerAsnArgs.__new__(PeerAsnArgs)

            __props__.__dict__["peer_asn"] = peer_asn
            __props__.__dict__["peer_asn_name"] = peer_asn_name
            __props__.__dict__["peer_contact_detail"] = peer_contact_detail
            __props__.__dict__["peer_name"] = peer_name
            __props__.__dict__["validation_state"] = validation_state
            __props__.__dict__["error_message"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:peering:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20190801preview:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20190901preview:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20200101preview:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20200401:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20201001:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20210601:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20220101:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20220601:PeerAsn"), pulumi.Alias(type_="azure-native:peering/v20221001:PeerAsn")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PeerAsn, __self__).__init__(
            'azure-native:peering/v20210101:PeerAsn',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PeerAsn':
        """
        Get an existing PeerAsn resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PeerAsnArgs.__new__(PeerAsnArgs)

        __props__.__dict__["error_message"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peer_asn"] = None
        __props__.__dict__["peer_contact_detail"] = None
        __props__.__dict__["peer_name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["validation_state"] = None
        return PeerAsn(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[str]:
        """
        The error message for the validation state
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerAsn")
    def peer_asn(self) -> pulumi.Output[Optional[int]]:
        """
        The Autonomous System Number (ASN) of the peer.
        """
        return pulumi.get(self, "peer_asn")

    @property
    @pulumi.getter(name="peerContactDetail")
    def peer_contact_detail(self) -> pulumi.Output[Optional[Sequence['outputs.ContactDetailResponse']]]:
        """
        The contact details of the peer.
        """
        return pulumi.get(self, "peer_contact_detail")

    @property
    @pulumi.getter(name="peerName")
    def peer_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the peer.
        """
        return pulumi.get(self, "peer_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validationState")
    def validation_state(self) -> pulumi.Output[Optional[str]]:
        """
        The validation state of the ASN associated with the peer.
        """
        return pulumi.get(self, "validation_state")

