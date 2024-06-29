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
    'GetSecuritySettingResult',
    'AwaitableGetSecuritySettingResult',
    'get_security_setting',
    'get_security_setting_output',
]

@pulumi.output_type
class GetSecuritySettingResult:
    """
    Security settings proxy resource
    """
    def __init__(__self__, id=None, name=None, provisioning_state=None, secured_core_compliance_assignment=None, security_compliance_status=None, smb_encryption_for_intra_cluster_traffic_compliance_assignment=None, system_data=None, type=None, wdac_compliance_assignment=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if secured_core_compliance_assignment and not isinstance(secured_core_compliance_assignment, str):
            raise TypeError("Expected argument 'secured_core_compliance_assignment' to be a str")
        pulumi.set(__self__, "secured_core_compliance_assignment", secured_core_compliance_assignment)
        if security_compliance_status and not isinstance(security_compliance_status, dict):
            raise TypeError("Expected argument 'security_compliance_status' to be a dict")
        pulumi.set(__self__, "security_compliance_status", security_compliance_status)
        if smb_encryption_for_intra_cluster_traffic_compliance_assignment and not isinstance(smb_encryption_for_intra_cluster_traffic_compliance_assignment, str):
            raise TypeError("Expected argument 'smb_encryption_for_intra_cluster_traffic_compliance_assignment' to be a str")
        pulumi.set(__self__, "smb_encryption_for_intra_cluster_traffic_compliance_assignment", smb_encryption_for_intra_cluster_traffic_compliance_assignment)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if wdac_compliance_assignment and not isinstance(wdac_compliance_assignment, str):
            raise TypeError("Expected argument 'wdac_compliance_assignment' to be a str")
        pulumi.set(__self__, "wdac_compliance_assignment", wdac_compliance_assignment)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securedCoreComplianceAssignment")
    def secured_core_compliance_assignment(self) -> Optional[str]:
        """
        Secured Core Compliance Assignment
        """
        return pulumi.get(self, "secured_core_compliance_assignment")

    @property
    @pulumi.getter(name="securityComplianceStatus")
    def security_compliance_status(self) -> 'outputs.SecurityComplianceStatusResponse':
        """
        Security Compliance Status
        """
        return pulumi.get(self, "security_compliance_status")

    @property
    @pulumi.getter(name="smbEncryptionForIntraClusterTrafficComplianceAssignment")
    def smb_encryption_for_intra_cluster_traffic_compliance_assignment(self) -> Optional[str]:
        """
        SMB encryption for intra-cluster traffic Compliance Assignment
        """
        return pulumi.get(self, "smb_encryption_for_intra_cluster_traffic_compliance_assignment")

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

    @property
    @pulumi.getter(name="wdacComplianceAssignment")
    def wdac_compliance_assignment(self) -> Optional[str]:
        """
        WDAC Compliance Assignment
        """
        return pulumi.get(self, "wdac_compliance_assignment")


class AwaitableGetSecuritySettingResult(GetSecuritySettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecuritySettingResult(
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            secured_core_compliance_assignment=self.secured_core_compliance_assignment,
            security_compliance_status=self.security_compliance_status,
            smb_encryption_for_intra_cluster_traffic_compliance_assignment=self.smb_encryption_for_intra_cluster_traffic_compliance_assignment,
            system_data=self.system_data,
            type=self.type,
            wdac_compliance_assignment=self.wdac_compliance_assignment)


def get_security_setting(cluster_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         security_settings_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecuritySettingResult:
    """
    Get a SecuritySetting


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str security_settings_name: Name of security setting
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['securitySettingsName'] = security_settings_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20240401:getSecuritySetting', __args__, opts=opts, typ=GetSecuritySettingResult).value

    return AwaitableGetSecuritySettingResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        secured_core_compliance_assignment=pulumi.get(__ret__, 'secured_core_compliance_assignment'),
        security_compliance_status=pulumi.get(__ret__, 'security_compliance_status'),
        smb_encryption_for_intra_cluster_traffic_compliance_assignment=pulumi.get(__ret__, 'smb_encryption_for_intra_cluster_traffic_compliance_assignment'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        wdac_compliance_assignment=pulumi.get(__ret__, 'wdac_compliance_assignment'))


@_utilities.lift_output_func(get_security_setting)
def get_security_setting_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                security_settings_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecuritySettingResult]:
    """
    Get a SecuritySetting


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str security_settings_name: Name of security setting
    """
    ...
