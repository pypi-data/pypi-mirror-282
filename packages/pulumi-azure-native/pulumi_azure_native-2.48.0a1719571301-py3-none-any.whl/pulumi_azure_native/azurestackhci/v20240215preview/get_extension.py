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
    'GetExtensionResult',
    'AwaitableGetExtensionResult',
    'get_extension',
    'get_extension_output',
]

@pulumi.output_type
class GetExtensionResult:
    """
    Details of a particular extension in HCI Cluster.
    """
    def __init__(__self__, aggregate_state=None, auto_upgrade_minor_version=None, enable_automatic_upgrade=None, force_update_tag=None, id=None, managed_by=None, name=None, per_node_extension_details=None, protected_settings=None, provisioning_state=None, publisher=None, settings=None, system_data=None, type=None, type_handler_version=None):
        if aggregate_state and not isinstance(aggregate_state, str):
            raise TypeError("Expected argument 'aggregate_state' to be a str")
        pulumi.set(__self__, "aggregate_state", aggregate_state)
        if auto_upgrade_minor_version and not isinstance(auto_upgrade_minor_version, bool):
            raise TypeError("Expected argument 'auto_upgrade_minor_version' to be a bool")
        pulumi.set(__self__, "auto_upgrade_minor_version", auto_upgrade_minor_version)
        if enable_automatic_upgrade and not isinstance(enable_automatic_upgrade, bool):
            raise TypeError("Expected argument 'enable_automatic_upgrade' to be a bool")
        pulumi.set(__self__, "enable_automatic_upgrade", enable_automatic_upgrade)
        if force_update_tag and not isinstance(force_update_tag, str):
            raise TypeError("Expected argument 'force_update_tag' to be a str")
        pulumi.set(__self__, "force_update_tag", force_update_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if per_node_extension_details and not isinstance(per_node_extension_details, list):
            raise TypeError("Expected argument 'per_node_extension_details' to be a list")
        pulumi.set(__self__, "per_node_extension_details", per_node_extension_details)
        if protected_settings and not isinstance(protected_settings, dict):
            raise TypeError("Expected argument 'protected_settings' to be a dict")
        pulumi.set(__self__, "protected_settings", protected_settings)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if publisher and not isinstance(publisher, str):
            raise TypeError("Expected argument 'publisher' to be a str")
        pulumi.set(__self__, "publisher", publisher)
        if settings and not isinstance(settings, dict):
            raise TypeError("Expected argument 'settings' to be a dict")
        pulumi.set(__self__, "settings", settings)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if type_handler_version and not isinstance(type_handler_version, str):
            raise TypeError("Expected argument 'type_handler_version' to be a str")
        pulumi.set(__self__, "type_handler_version", type_handler_version)

    @property
    @pulumi.getter(name="aggregateState")
    def aggregate_state(self) -> str:
        """
        Aggregate state of Arc Extensions across the nodes in this HCI cluster.
        """
        return pulumi.get(self, "aggregate_state")

    @property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[bool]:
        """
        Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
        """
        return pulumi.get(self, "auto_upgrade_minor_version")

    @property
    @pulumi.getter(name="enableAutomaticUpgrade")
    def enable_automatic_upgrade(self) -> Optional[bool]:
        """
        Indicates whether the extension should be automatically upgraded by the platform if there is a newer version available.
        """
        return pulumi.get(self, "enable_automatic_upgrade")

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[str]:
        """
        How the extension handler should be forced to update even if the extension configuration has not changed.
        """
        return pulumi.get(self, "force_update_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> str:
        """
        Indicates if the extension is managed by azure or the user.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perNodeExtensionDetails")
    def per_node_extension_details(self) -> Sequence['outputs.PerNodeExtensionStateResponse']:
        """
        State of Arc Extension in each of the nodes.
        """
        return pulumi.get(self, "per_node_extension_details")

    @property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        """
        Protected settings (may contain secrets).
        """
        return pulumi.get(self, "protected_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Extension proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def publisher(self) -> Optional[str]:
        """
        The name of the extension handler publisher.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        """
        Json formatted public settings for the extension.
        """
        return pulumi.get(self, "settings")

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
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[str]:
        """
        Specifies the version of the script handler. Latest version would be used if not specified.
        """
        return pulumi.get(self, "type_handler_version")


class AwaitableGetExtensionResult(GetExtensionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExtensionResult(
            aggregate_state=self.aggregate_state,
            auto_upgrade_minor_version=self.auto_upgrade_minor_version,
            enable_automatic_upgrade=self.enable_automatic_upgrade,
            force_update_tag=self.force_update_tag,
            id=self.id,
            managed_by=self.managed_by,
            name=self.name,
            per_node_extension_details=self.per_node_extension_details,
            protected_settings=self.protected_settings,
            provisioning_state=self.provisioning_state,
            publisher=self.publisher,
            settings=self.settings,
            system_data=self.system_data,
            type=self.type,
            type_handler_version=self.type_handler_version)


def get_extension(arc_setting_name: Optional[str] = None,
                  cluster_name: Optional[str] = None,
                  extension_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExtensionResult:
    """
    Get particular Arc Extension of HCI Cluster.


    :param str arc_setting_name: The name of the proxy resource holding details of HCI ArcSetting information.
    :param str cluster_name: The name of the cluster.
    :param str extension_name: The name of the machine extension.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['arcSettingName'] = arc_setting_name
    __args__['clusterName'] = cluster_name
    __args__['extensionName'] = extension_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20240215preview:getExtension', __args__, opts=opts, typ=GetExtensionResult).value

    return AwaitableGetExtensionResult(
        aggregate_state=pulumi.get(__ret__, 'aggregate_state'),
        auto_upgrade_minor_version=pulumi.get(__ret__, 'auto_upgrade_minor_version'),
        enable_automatic_upgrade=pulumi.get(__ret__, 'enable_automatic_upgrade'),
        force_update_tag=pulumi.get(__ret__, 'force_update_tag'),
        id=pulumi.get(__ret__, 'id'),
        managed_by=pulumi.get(__ret__, 'managed_by'),
        name=pulumi.get(__ret__, 'name'),
        per_node_extension_details=pulumi.get(__ret__, 'per_node_extension_details'),
        protected_settings=pulumi.get(__ret__, 'protected_settings'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        publisher=pulumi.get(__ret__, 'publisher'),
        settings=pulumi.get(__ret__, 'settings'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        type_handler_version=pulumi.get(__ret__, 'type_handler_version'))


@_utilities.lift_output_func(get_extension)
def get_extension_output(arc_setting_name: Optional[pulumi.Input[str]] = None,
                         cluster_name: Optional[pulumi.Input[str]] = None,
                         extension_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExtensionResult]:
    """
    Get particular Arc Extension of HCI Cluster.


    :param str arc_setting_name: The name of the proxy resource holding details of HCI ArcSetting information.
    :param str cluster_name: The name of the cluster.
    :param str extension_name: The name of the machine extension.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
