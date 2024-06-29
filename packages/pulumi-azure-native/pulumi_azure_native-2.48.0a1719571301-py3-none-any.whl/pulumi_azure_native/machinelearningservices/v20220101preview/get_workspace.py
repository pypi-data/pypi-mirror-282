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
    'GetWorkspaceResult',
    'AwaitableGetWorkspaceResult',
    'get_workspace',
    'get_workspace_output',
]

@pulumi.output_type
class GetWorkspaceResult:
    """
    An object that represents a machine learning workspace.
    """
    def __init__(__self__, allow_public_access_when_behind_vnet=None, allow_recover_soft_deleted_workspace=None, application_insights=None, container_registry=None, description=None, discovery_url=None, encryption=None, friendly_name=None, hbi_workspace=None, id=None, identity=None, image_build_compute=None, key_vault=None, location=None, ml_flow_tracking_uri=None, name=None, notebook_info=None, primary_user_assigned_identity=None, private_endpoint_connections=None, private_link_count=None, provisioning_state=None, public_network_access=None, service_managed_resources_settings=None, service_provisioned_resource_group=None, shared_private_link_resources=None, sku=None, soft_delete_enabled=None, storage_account=None, storage_hns_enabled=None, system_data=None, tags=None, tenant_id=None, type=None, workspace_id=None):
        if allow_public_access_when_behind_vnet and not isinstance(allow_public_access_when_behind_vnet, bool):
            raise TypeError("Expected argument 'allow_public_access_when_behind_vnet' to be a bool")
        pulumi.set(__self__, "allow_public_access_when_behind_vnet", allow_public_access_when_behind_vnet)
        if allow_recover_soft_deleted_workspace and not isinstance(allow_recover_soft_deleted_workspace, str):
            raise TypeError("Expected argument 'allow_recover_soft_deleted_workspace' to be a str")
        pulumi.set(__self__, "allow_recover_soft_deleted_workspace", allow_recover_soft_deleted_workspace)
        if application_insights and not isinstance(application_insights, str):
            raise TypeError("Expected argument 'application_insights' to be a str")
        pulumi.set(__self__, "application_insights", application_insights)
        if container_registry and not isinstance(container_registry, str):
            raise TypeError("Expected argument 'container_registry' to be a str")
        pulumi.set(__self__, "container_registry", container_registry)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if discovery_url and not isinstance(discovery_url, str):
            raise TypeError("Expected argument 'discovery_url' to be a str")
        pulumi.set(__self__, "discovery_url", discovery_url)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if hbi_workspace and not isinstance(hbi_workspace, bool):
            raise TypeError("Expected argument 'hbi_workspace' to be a bool")
        pulumi.set(__self__, "hbi_workspace", hbi_workspace)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if image_build_compute and not isinstance(image_build_compute, str):
            raise TypeError("Expected argument 'image_build_compute' to be a str")
        pulumi.set(__self__, "image_build_compute", image_build_compute)
        if key_vault and not isinstance(key_vault, str):
            raise TypeError("Expected argument 'key_vault' to be a str")
        pulumi.set(__self__, "key_vault", key_vault)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if ml_flow_tracking_uri and not isinstance(ml_flow_tracking_uri, str):
            raise TypeError("Expected argument 'ml_flow_tracking_uri' to be a str")
        pulumi.set(__self__, "ml_flow_tracking_uri", ml_flow_tracking_uri)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notebook_info and not isinstance(notebook_info, dict):
            raise TypeError("Expected argument 'notebook_info' to be a dict")
        pulumi.set(__self__, "notebook_info", notebook_info)
        if primary_user_assigned_identity and not isinstance(primary_user_assigned_identity, str):
            raise TypeError("Expected argument 'primary_user_assigned_identity' to be a str")
        pulumi.set(__self__, "primary_user_assigned_identity", primary_user_assigned_identity)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if private_link_count and not isinstance(private_link_count, int):
            raise TypeError("Expected argument 'private_link_count' to be a int")
        pulumi.set(__self__, "private_link_count", private_link_count)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if service_managed_resources_settings and not isinstance(service_managed_resources_settings, dict):
            raise TypeError("Expected argument 'service_managed_resources_settings' to be a dict")
        pulumi.set(__self__, "service_managed_resources_settings", service_managed_resources_settings)
        if service_provisioned_resource_group and not isinstance(service_provisioned_resource_group, str):
            raise TypeError("Expected argument 'service_provisioned_resource_group' to be a str")
        pulumi.set(__self__, "service_provisioned_resource_group", service_provisioned_resource_group)
        if shared_private_link_resources and not isinstance(shared_private_link_resources, list):
            raise TypeError("Expected argument 'shared_private_link_resources' to be a list")
        pulumi.set(__self__, "shared_private_link_resources", shared_private_link_resources)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if soft_delete_enabled and not isinstance(soft_delete_enabled, str):
            raise TypeError("Expected argument 'soft_delete_enabled' to be a str")
        pulumi.set(__self__, "soft_delete_enabled", soft_delete_enabled)
        if storage_account and not isinstance(storage_account, str):
            raise TypeError("Expected argument 'storage_account' to be a str")
        pulumi.set(__self__, "storage_account", storage_account)
        if storage_hns_enabled and not isinstance(storage_hns_enabled, bool):
            raise TypeError("Expected argument 'storage_hns_enabled' to be a bool")
        pulumi.set(__self__, "storage_hns_enabled", storage_hns_enabled)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if workspace_id and not isinstance(workspace_id, str):
            raise TypeError("Expected argument 'workspace_id' to be a str")
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="allowPublicAccessWhenBehindVnet")
    def allow_public_access_when_behind_vnet(self) -> Optional[bool]:
        """
        The flag to indicate whether to allow public access when behind VNet.
        """
        return pulumi.get(self, "allow_public_access_when_behind_vnet")

    @property
    @pulumi.getter(name="allowRecoverSoftDeletedWorkspace")
    def allow_recover_soft_deleted_workspace(self) -> Optional[str]:
        """
        Allow a soft deleted workspace to be recovered
        """
        return pulumi.get(self, "allow_recover_soft_deleted_workspace")

    @property
    @pulumi.getter(name="applicationInsights")
    def application_insights(self) -> Optional[str]:
        """
        ARM id of the application insights associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "application_insights")

    @property
    @pulumi.getter(name="containerRegistry")
    def container_registry(self) -> Optional[str]:
        """
        ARM id of the container registry associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "container_registry")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of this workspace.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="discoveryUrl")
    def discovery_url(self) -> Optional[str]:
        """
        Url for the discovery service to identify regional endpoints for machine learning experimentation services
        """
        return pulumi.get(self, "discovery_url")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionPropertyResponse']:
        """
        The encryption settings of Azure ML workspace.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        The friendly name for this workspace. This name in mutable
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hbiWorkspace")
    def hbi_workspace(self) -> Optional[bool]:
        """
        The flag to signal HBI data in the workspace and reduce diagnostic data collected by the service
        """
        return pulumi.get(self, "hbi_workspace")

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
    @pulumi.getter(name="imageBuildCompute")
    def image_build_compute(self) -> Optional[str]:
        """
        The compute name for image build
        """
        return pulumi.get(self, "image_build_compute")

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[str]:
        """
        ARM id of the key vault associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "key_vault")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mlFlowTrackingUri")
    def ml_flow_tracking_uri(self) -> str:
        """
        The URI associated with this workspace that machine learning flow must point at to set up tracking.
        """
        return pulumi.get(self, "ml_flow_tracking_uri")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notebookInfo")
    def notebook_info(self) -> 'outputs.NotebookResourceInfoResponse':
        """
        The notebook info of Azure ML workspace.
        """
        return pulumi.get(self, "notebook_info")

    @property
    @pulumi.getter(name="primaryUserAssignedIdentity")
    def primary_user_assigned_identity(self) -> Optional[str]:
        """
        The user assigned identity resource id that represents the workspace identity.
        """
        return pulumi.get(self, "primary_user_assigned_identity")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        The list of private endpoint connections in the workspace.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="privateLinkCount")
    def private_link_count(self) -> int:
        """
        Count of private connections in the workspace
        """
        return pulumi.get(self, "private_link_count")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment state of workspace resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Whether requests from Public Network are allowed.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="serviceManagedResourcesSettings")
    def service_managed_resources_settings(self) -> Optional['outputs.ServiceManagedResourcesSettingsResponse']:
        """
        The service managed resource settings.
        """
        return pulumi.get(self, "service_managed_resources_settings")

    @property
    @pulumi.getter(name="serviceProvisionedResourceGroup")
    def service_provisioned_resource_group(self) -> str:
        """
        The name of the managed resource group created by workspace RP in customer subscription if the workspace is CMK workspace
        """
        return pulumi.get(self, "service_provisioned_resource_group")

    @property
    @pulumi.getter(name="sharedPrivateLinkResources")
    def shared_private_link_resources(self) -> Optional[Sequence['outputs.SharedPrivateLinkResourceResponse']]:
        """
        The list of shared private link resources in this workspace.
        """
        return pulumi.get(self, "shared_private_link_resources")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The sku of the workspace.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="softDeleteEnabled")
    def soft_delete_enabled(self) -> Optional[str]:
        """
        create a workspace with soft delete capability
        """
        return pulumi.get(self, "soft_delete_enabled")

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[str]:
        """
        ARM id of the storage account associated with this workspace. This cannot be changed once the workspace has been created
        """
        return pulumi.get(self, "storage_account")

    @property
    @pulumi.getter(name="storageHnsEnabled")
    def storage_hns_enabled(self) -> bool:
        """
        If the storage associated with the workspace has hierarchical namespace(HNS) enabled.
        """
        return pulumi.get(self, "storage_hns_enabled")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant id associated with this workspace.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> str:
        """
        The immutable id associated with this workspace.
        """
        return pulumi.get(self, "workspace_id")


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceResult(
            allow_public_access_when_behind_vnet=self.allow_public_access_when_behind_vnet,
            allow_recover_soft_deleted_workspace=self.allow_recover_soft_deleted_workspace,
            application_insights=self.application_insights,
            container_registry=self.container_registry,
            description=self.description,
            discovery_url=self.discovery_url,
            encryption=self.encryption,
            friendly_name=self.friendly_name,
            hbi_workspace=self.hbi_workspace,
            id=self.id,
            identity=self.identity,
            image_build_compute=self.image_build_compute,
            key_vault=self.key_vault,
            location=self.location,
            ml_flow_tracking_uri=self.ml_flow_tracking_uri,
            name=self.name,
            notebook_info=self.notebook_info,
            primary_user_assigned_identity=self.primary_user_assigned_identity,
            private_endpoint_connections=self.private_endpoint_connections,
            private_link_count=self.private_link_count,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            service_managed_resources_settings=self.service_managed_resources_settings,
            service_provisioned_resource_group=self.service_provisioned_resource_group,
            shared_private_link_resources=self.shared_private_link_resources,
            sku=self.sku,
            soft_delete_enabled=self.soft_delete_enabled,
            storage_account=self.storage_account,
            storage_hns_enabled=self.storage_hns_enabled,
            system_data=self.system_data,
            tags=self.tags,
            tenant_id=self.tenant_id,
            type=self.type,
            workspace_id=self.workspace_id)


def get_workspace(resource_group_name: Optional[str] = None,
                  workspace_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceResult:
    """
    Gets the properties of the specified machine learning workspace.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20220101preview:getWorkspace', __args__, opts=opts, typ=GetWorkspaceResult).value

    return AwaitableGetWorkspaceResult(
        allow_public_access_when_behind_vnet=pulumi.get(__ret__, 'allow_public_access_when_behind_vnet'),
        allow_recover_soft_deleted_workspace=pulumi.get(__ret__, 'allow_recover_soft_deleted_workspace'),
        application_insights=pulumi.get(__ret__, 'application_insights'),
        container_registry=pulumi.get(__ret__, 'container_registry'),
        description=pulumi.get(__ret__, 'description'),
        discovery_url=pulumi.get(__ret__, 'discovery_url'),
        encryption=pulumi.get(__ret__, 'encryption'),
        friendly_name=pulumi.get(__ret__, 'friendly_name'),
        hbi_workspace=pulumi.get(__ret__, 'hbi_workspace'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        image_build_compute=pulumi.get(__ret__, 'image_build_compute'),
        key_vault=pulumi.get(__ret__, 'key_vault'),
        location=pulumi.get(__ret__, 'location'),
        ml_flow_tracking_uri=pulumi.get(__ret__, 'ml_flow_tracking_uri'),
        name=pulumi.get(__ret__, 'name'),
        notebook_info=pulumi.get(__ret__, 'notebook_info'),
        primary_user_assigned_identity=pulumi.get(__ret__, 'primary_user_assigned_identity'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        private_link_count=pulumi.get(__ret__, 'private_link_count'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        service_managed_resources_settings=pulumi.get(__ret__, 'service_managed_resources_settings'),
        service_provisioned_resource_group=pulumi.get(__ret__, 'service_provisioned_resource_group'),
        shared_private_link_resources=pulumi.get(__ret__, 'shared_private_link_resources'),
        sku=pulumi.get(__ret__, 'sku'),
        soft_delete_enabled=pulumi.get(__ret__, 'soft_delete_enabled'),
        storage_account=pulumi.get(__ret__, 'storage_account'),
        storage_hns_enabled=pulumi.get(__ret__, 'storage_hns_enabled'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'),
        workspace_id=pulumi.get(__ret__, 'workspace_id'))


@_utilities.lift_output_func(get_workspace)
def get_workspace_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                         workspace_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceResult]:
    """
    Gets the properties of the specified machine learning workspace.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
