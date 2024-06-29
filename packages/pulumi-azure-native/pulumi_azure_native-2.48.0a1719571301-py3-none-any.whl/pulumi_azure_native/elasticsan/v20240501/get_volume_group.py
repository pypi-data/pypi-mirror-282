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
    'GetVolumeGroupResult',
    'AwaitableGetVolumeGroupResult',
    'get_volume_group',
    'get_volume_group_output',
]

@pulumi.output_type
class GetVolumeGroupResult:
    """
    Response for Volume Group request.
    """
    def __init__(__self__, encryption=None, encryption_properties=None, enforce_data_integrity_check_for_iscsi=None, id=None, identity=None, name=None, network_acls=None, private_endpoint_connections=None, protocol_type=None, provisioning_state=None, system_data=None, type=None):
        if encryption and not isinstance(encryption, str):
            raise TypeError("Expected argument 'encryption' to be a str")
        pulumi.set(__self__, "encryption", encryption)
        if encryption_properties and not isinstance(encryption_properties, dict):
            raise TypeError("Expected argument 'encryption_properties' to be a dict")
        pulumi.set(__self__, "encryption_properties", encryption_properties)
        if enforce_data_integrity_check_for_iscsi and not isinstance(enforce_data_integrity_check_for_iscsi, bool):
            raise TypeError("Expected argument 'enforce_data_integrity_check_for_iscsi' to be a bool")
        pulumi.set(__self__, "enforce_data_integrity_check_for_iscsi", enforce_data_integrity_check_for_iscsi)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_acls and not isinstance(network_acls, dict):
            raise TypeError("Expected argument 'network_acls' to be a dict")
        pulumi.set(__self__, "network_acls", network_acls)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if protocol_type and not isinstance(protocol_type, str):
            raise TypeError("Expected argument 'protocol_type' to be a str")
        pulumi.set(__self__, "protocol_type", protocol_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[str]:
        """
        Type of encryption
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="encryptionProperties")
    def encryption_properties(self) -> Optional['outputs.EncryptionPropertiesResponse']:
        """
        Encryption Properties describing Key Vault and Identity information
        """
        return pulumi.get(self, "encryption_properties")

    @property
    @pulumi.getter(name="enforceDataIntegrityCheckForIscsi")
    def enforce_data_integrity_check_for_iscsi(self) -> Optional[bool]:
        """
        A boolean indicating whether or not Data Integrity Check is enabled
        """
        return pulumi.get(self, "enforce_data_integrity_check_for_iscsi")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional['outputs.NetworkRuleSetResponse']:
        """
        A collection of rules governing the accessibility from specific network locations.
        """
        return pulumi.get(self, "network_acls")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        The list of Private Endpoint Connections.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> Optional[str]:
        """
        Type of storage target
        """
        return pulumi.get(self, "protocol_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the operation on the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetVolumeGroupResult(GetVolumeGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeGroupResult(
            encryption=self.encryption,
            encryption_properties=self.encryption_properties,
            enforce_data_integrity_check_for_iscsi=self.enforce_data_integrity_check_for_iscsi,
            id=self.id,
            identity=self.identity,
            name=self.name,
            network_acls=self.network_acls,
            private_endpoint_connections=self.private_endpoint_connections,
            protocol_type=self.protocol_type,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_volume_group(elastic_san_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     volume_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeGroupResult:
    """
    Get an VolumeGroups.


    :param str elastic_san_name: The name of the ElasticSan.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str volume_group_name: The name of the VolumeGroup.
    """
    __args__ = dict()
    __args__['elasticSanName'] = elastic_san_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['volumeGroupName'] = volume_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elasticsan/v20240501:getVolumeGroup', __args__, opts=opts, typ=GetVolumeGroupResult).value

    return AwaitableGetVolumeGroupResult(
        encryption=pulumi.get(__ret__, 'encryption'),
        encryption_properties=pulumi.get(__ret__, 'encryption_properties'),
        enforce_data_integrity_check_for_iscsi=pulumi.get(__ret__, 'enforce_data_integrity_check_for_iscsi'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        name=pulumi.get(__ret__, 'name'),
        network_acls=pulumi.get(__ret__, 'network_acls'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        protocol_type=pulumi.get(__ret__, 'protocol_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_volume_group)
def get_volume_group_output(elastic_san_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            volume_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeGroupResult]:
    """
    Get an VolumeGroups.


    :param str elastic_san_name: The name of the ElasticSan.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str volume_group_name: The name of the VolumeGroup.
    """
    ...
