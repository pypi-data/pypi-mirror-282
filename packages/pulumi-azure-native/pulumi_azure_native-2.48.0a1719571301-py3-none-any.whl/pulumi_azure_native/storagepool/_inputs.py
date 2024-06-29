# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AclArgs',
    'DiskArgs',
    'IscsiLunArgs',
    'SkuArgs',
]

@pulumi.input_type
class AclArgs:
    def __init__(__self__, *,
                 initiator_iqn: pulumi.Input[str],
                 mapped_luns: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        Access Control List (ACL) for an iSCSI Target; defines LUN masking policy
        :param pulumi.Input[str] initiator_iqn: iSCSI initiator IQN (iSCSI Qualified Name); example: "iqn.2005-03.org.iscsi:client".
        :param pulumi.Input[Sequence[pulumi.Input[str]]] mapped_luns: List of LUN names mapped to the ACL.
        """
        pulumi.set(__self__, "initiator_iqn", initiator_iqn)
        pulumi.set(__self__, "mapped_luns", mapped_luns)

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


@pulumi.input_type
class DiskArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Azure Managed Disk to attach to the Disk Pool.
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
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 tier: Optional[pulumi.Input[str]] = None):
        """
        Sku for ARM resource
        :param pulumi.Input[str] name: Sku name
        :param pulumi.Input[str] tier: Sku tier
        """
        pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Sku name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        Sku tier
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


