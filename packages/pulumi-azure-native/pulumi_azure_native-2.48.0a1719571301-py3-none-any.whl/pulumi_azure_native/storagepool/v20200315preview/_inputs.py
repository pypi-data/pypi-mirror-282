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
    'AclArgs',
    'AttributesArgs',
    'DiskArgs',
    'IscsiLunArgs',
    'TargetPortalGroupCreateArgs',
]

@pulumi.input_type
class AclArgs:
    def __init__(__self__, *,
                 initiator_iqn: pulumi.Input[str],
                 mapped_luns: pulumi.Input[Sequence[pulumi.Input[str]]],
                 password: pulumi.Input[str],
                 username: pulumi.Input[str]):
        """
        Access Control List (ACL) for an iSCSI target portal group
        :param pulumi.Input[str] initiator_iqn: iSCSI initiator IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:client".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mapped_luns: List of LUN names mapped to the ACL.
        :param pulumi.Input[str] password: Password for Challenge Handshake Authentication Protocol (CHAP) authentication.
        :param pulumi.Input[str] username: Username for Challenge Handshake Authentication Protocol (CHAP) authentication.
        """
        pulumi.set(__self__, "initiator_iqn", initiator_iqn)
        pulumi.set(__self__, "mapped_luns", mapped_luns)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="initiatorIqn")
    def initiator_iqn(self) -> pulumi.Input[str]:
        """
        iSCSI initiator IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:client".
        """
        return pulumi.get(self, "initiator_iqn")

    @initiator_iqn.setter
    def initiator_iqn(self, value: pulumi.Input[str]):
        pulumi.set(self, "initiator_iqn", value)

    @property
    @pulumi.getter(name="mappedLuns")
    def mapped_luns(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of LUN names mapped to the ACL.
        """
        return pulumi.get(self, "mapped_luns")

    @mapped_luns.setter
    def mapped_luns(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "mapped_luns", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        Password for Challenge Handshake Authentication Protocol (CHAP) authentication.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        Username for Challenge Handshake Authentication Protocol (CHAP) authentication.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class AttributesArgs:
    def __init__(__self__, *,
                 authentication: pulumi.Input[bool],
                 prod_mode_write_protect: pulumi.Input[bool]):
        """
        Attributes of a iSCSI target portal group.
        :param pulumi.Input[bool] authentication: Indicates whether or not authentication is enabled on the ACL.
        :param pulumi.Input[bool] prod_mode_write_protect: Indicates whether or not write protect is enabled on the LUNs.
        """
        pulumi.set(__self__, "authentication", authentication)
        pulumi.set(__self__, "prod_mode_write_protect", prod_mode_write_protect)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Input[bool]:
        """
        Indicates whether or not authentication is enabled on the ACL.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: pulumi.Input[bool]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="prodModeWriteProtect")
    def prod_mode_write_protect(self) -> pulumi.Input[bool]:
        """
        Indicates whether or not write protect is enabled on the LUNs.
        """
        return pulumi.get(self, "prod_mode_write_protect")

    @prod_mode_write_protect.setter
    def prod_mode_write_protect(self, value: pulumi.Input[bool]):
        pulumi.set(self, "prod_mode_write_protect", value)


@pulumi.input_type
class DiskArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Azure Managed Disk to attach to the Disk pool.
        :param pulumi.Input[str] id: Unique Azure Resource ID of the Managed Disk.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Unique Azure Resource ID of the Managed Disk.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class IscsiLunArgs:
    def __init__(__self__, *,
                 managed_disk_azure_resource_id: pulumi.Input[str],
                 name: pulumi.Input[str]):
        """
        LUN to expose the Azure Managed Disk.
        :param pulumi.Input[str] managed_disk_azure_resource_id: Azure Resource ID of the Managed Disk.
        :param pulumi.Input[str] name: User defined name for iSCSI LUN; example: "lun0"
        """
        pulumi.set(__self__, "managed_disk_azure_resource_id", managed_disk_azure_resource_id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="managedDiskAzureResourceId")
    def managed_disk_azure_resource_id(self) -> pulumi.Input[str]:
        """
        Azure Resource ID of the Managed Disk.
        """
        return pulumi.get(self, "managed_disk_azure_resource_id")

    @managed_disk_azure_resource_id.setter
    def managed_disk_azure_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_disk_azure_resource_id", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        User defined name for iSCSI LUN; example: "lun0"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class TargetPortalGroupCreateArgs:
    def __init__(__self__, *,
                 acls: pulumi.Input[Sequence[pulumi.Input['AclArgs']]],
                 attributes: pulumi.Input['AttributesArgs'],
                 luns: pulumi.Input[Sequence[pulumi.Input['IscsiLunArgs']]]):
        """
        Target portal group properties for create or update iSCSI target request.
        :param pulumi.Input[Sequence[pulumi.Input['AclArgs']]] acls: Access Control List (ACL) for an iSCSI target portal group.
        :param pulumi.Input['AttributesArgs'] attributes: Attributes of an iSCSI target portal group.
        :param pulumi.Input[Sequence[pulumi.Input['IscsiLunArgs']]] luns: List of LUNs to be exposed through the iSCSI target portal group.
        """
        pulumi.set(__self__, "acls", acls)
        pulumi.set(__self__, "attributes", attributes)
        pulumi.set(__self__, "luns", luns)

    @property
    @pulumi.getter
    def acls(self) -> pulumi.Input[Sequence[pulumi.Input['AclArgs']]]:
        """
        Access Control List (ACL) for an iSCSI target portal group.
        """
        return pulumi.get(self, "acls")

    @acls.setter
    def acls(self, value: pulumi.Input[Sequence[pulumi.Input['AclArgs']]]):
        pulumi.set(self, "acls", value)

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Input['AttributesArgs']:
        """
        Attributes of an iSCSI target portal group.
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: pulumi.Input['AttributesArgs']):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter
    def luns(self) -> pulumi.Input[Sequence[pulumi.Input['IscsiLunArgs']]]:
        """
        List of LUNs to be exposed through the iSCSI target portal group.
        """
        return pulumi.get(self, "luns")

    @luns.setter
    def luns(self, value: pulumi.Input[Sequence[pulumi.Input['IscsiLunArgs']]]):
        pulumi.set(self, "luns", value)


