# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AuthorizationArgs',
    'DevOpsConfigurationPropertiesArgs',
]

@pulumi.input_type
class AuthorizationArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[str]] = None):
        """
        Authorization payload.
        :param pulumi.Input[str] code: Gets or sets one-time OAuth code to exchange for refresh and access tokens.
               
               Only used during PUT/PATCH operations. The secret is cleared during GET.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets one-time OAuth code to exchange for refresh and access tokens.
        
        Only used during PUT/PATCH operations. The secret is cleared during GET.
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code", value)


@pulumi.input_type
class DevOpsConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 authorization: Optional[pulumi.Input['AuthorizationArgs']] = None,
                 auto_discovery: Optional[pulumi.Input[Union[str, 'AutoDiscovery']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'DevOpsProvisioningState']]] = None,
                 top_level_inventory_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        DevOps Configuration properties.
        :param pulumi.Input['AuthorizationArgs'] authorization: Authorization payload.
        :param pulumi.Input[Union[str, 'AutoDiscovery']] auto_discovery: AutoDiscovery states.
        :param pulumi.Input[Union[str, 'DevOpsProvisioningState']] provisioning_state: The provisioning state of the resource.
               
               Pending - Provisioning pending.
               Failed - Provisioning failed.
               Succeeded - Successful provisioning.
               Canceled - Provisioning canceled.
               PendingDeletion - Deletion pending.
               DeletionSuccess - Deletion successful.
               DeletionFailure - Deletion failure.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] top_level_inventory_list: List of top-level inventory to select when AutoDiscovery is disabled.
               This field is ignored when AutoDiscovery is enabled.
        """
        if authorization is not None:
            pulumi.set(__self__, "authorization", authorization)
        if auto_discovery is not None:
            pulumi.set(__self__, "auto_discovery", auto_discovery)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if top_level_inventory_list is not None:
            pulumi.set(__self__, "top_level_inventory_list", top_level_inventory_list)

    @property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input['AuthorizationArgs']]:
        """
        Authorization payload.
        """
        return pulumi.get(self, "authorization")

    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input['AuthorizationArgs']]):
        pulumi.set(self, "authorization", value)

    @property
    @pulumi.getter(name="autoDiscovery")
    def auto_discovery(self) -> Optional[pulumi.Input[Union[str, 'AutoDiscovery']]]:
        """
        AutoDiscovery states.
        """
        return pulumi.get(self, "auto_discovery")

    @auto_discovery.setter
    def auto_discovery(self, value: Optional[pulumi.Input[Union[str, 'AutoDiscovery']]]):
        pulumi.set(self, "auto_discovery", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'DevOpsProvisioningState']]]:
        """
        The provisioning state of the resource.
        
        Pending - Provisioning pending.
        Failed - Provisioning failed.
        Succeeded - Successful provisioning.
        Canceled - Provisioning canceled.
        PendingDeletion - Deletion pending.
        DeletionSuccess - Deletion successful.
        DeletionFailure - Deletion failure.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'DevOpsProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="topLevelInventoryList")
    def top_level_inventory_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of top-level inventory to select when AutoDiscovery is disabled.
        This field is ignored when AutoDiscovery is enabled.
        """
        return pulumi.get(self, "top_level_inventory_list")

    @top_level_inventory_list.setter
    def top_level_inventory_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "top_level_inventory_list", value)


