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

__all__ = [
    'ErrorAdditionalInfoResponse',
    'ErrorDetailResponse',
    'FleetCredentialResultResponse',
    'ManagedClusterUpdateResponse',
    'ManagedClusterUpgradeSpecResponse',
    'ManagedServiceIdentityResponse',
    'MemberUpdateStatusResponse',
    'NodeImageSelectionResponse',
    'NodeImageSelectionStatusResponse',
    'NodeImageVersionResponse',
    'SystemDataResponse',
    'UpdateGroupResponse',
    'UpdateGroupStatusResponse',
    'UpdateRunStatusResponse',
    'UpdateRunStrategyResponse',
    'UpdateStageResponse',
    'UpdateStageStatusResponse',
    'UpdateStatusResponse',
    'UserAssignedIdentityResponse',
    'WaitStatusResponse',
]

@pulumi.output_type
class ErrorAdditionalInfoResponse(dict):
    """
    The resource management error additional info.
    """
    def __init__(__self__, *,
                 info: Any,
                 type: str):
        """
        The resource management error additional info.
        :param Any info: The additional info.
        :param str type: The additional info type.
        """
        pulumi.set(__self__, "info", info)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def info(self) -> Any:
        """
        The additional info.
        """
        return pulumi.get(self, "info")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The additional info type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ErrorDetailResponse(dict):
    """
    The error detail.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "additionalInfo":
            suggest = "additional_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ErrorDetailResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ErrorDetailResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ErrorDetailResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 additional_info: Sequence['outputs.ErrorAdditionalInfoResponse'],
                 code: str,
                 details: Sequence['outputs.ErrorDetailResponse'],
                 message: str,
                 target: str):
        """
        The error detail.
        :param Sequence['ErrorAdditionalInfoResponse'] additional_info: The error additional info.
        :param str code: The error code.
        :param Sequence['ErrorDetailResponse'] details: The error details.
        :param str message: The error message.
        :param str target: The error target.
        """
        pulumi.set(__self__, "additional_info", additional_info)
        pulumi.set(__self__, "code", code)
        pulumi.set(__self__, "details", details)
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="additionalInfo")
    def additional_info(self) -> Sequence['outputs.ErrorAdditionalInfoResponse']:
        """
        The error additional info.
        """
        return pulumi.get(self, "additional_info")

    @property
    @pulumi.getter
    def code(self) -> str:
        """
        The error code.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def details(self) -> Sequence['outputs.ErrorDetailResponse']:
        """
        The error details.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The error message.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def target(self) -> str:
        """
        The error target.
        """
        return pulumi.get(self, "target")


@pulumi.output_type
class FleetCredentialResultResponse(dict):
    """
    One credential result item.
    """
    def __init__(__self__, *,
                 name: str,
                 value: str):
        """
        One credential result item.
        :param str name: The name of the credential.
        :param str value: Base64-encoded Kubernetes configuration file.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the credential.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Base64-encoded Kubernetes configuration file.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ManagedClusterUpdateResponse(dict):
    """
    The update to be applied to the ManagedClusters.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nodeImageSelection":
            suggest = "node_image_selection"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedClusterUpdateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedClusterUpdateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedClusterUpdateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 upgrade: 'outputs.ManagedClusterUpgradeSpecResponse',
                 node_image_selection: Optional['outputs.NodeImageSelectionResponse'] = None):
        """
        The update to be applied to the ManagedClusters.
        :param 'ManagedClusterUpgradeSpecResponse' upgrade: The upgrade to apply to the ManagedClusters.
        :param 'NodeImageSelectionResponse' node_image_selection: The node image upgrade to be applied to the target nodes in update run.
        """
        pulumi.set(__self__, "upgrade", upgrade)
        if node_image_selection is not None:
            pulumi.set(__self__, "node_image_selection", node_image_selection)

    @property
    @pulumi.getter
    def upgrade(self) -> 'outputs.ManagedClusterUpgradeSpecResponse':
        """
        The upgrade to apply to the ManagedClusters.
        """
        return pulumi.get(self, "upgrade")

    @property
    @pulumi.getter(name="nodeImageSelection")
    def node_image_selection(self) -> Optional['outputs.NodeImageSelectionResponse']:
        """
        The node image upgrade to be applied to the target nodes in update run.
        """
        return pulumi.get(self, "node_image_selection")


@pulumi.output_type
class ManagedClusterUpgradeSpecResponse(dict):
    """
    The upgrade to apply to a ManagedCluster.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "kubernetesVersion":
            suggest = "kubernetes_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedClusterUpgradeSpecResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedClusterUpgradeSpecResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedClusterUpgradeSpecResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 kubernetes_version: Optional[str] = None):
        """
        The upgrade to apply to a ManagedCluster.
        :param str type: ManagedClusterUpgradeType is the type of upgrade to be applied.
        :param str kubernetes_version: The Kubernetes version to upgrade the member clusters to.
        """
        pulumi.set(__self__, "type", type)
        if kubernetes_version is not None:
            pulumi.set(__self__, "kubernetes_version", kubernetes_version)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        ManagedClusterUpgradeType is the type of upgrade to be applied.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[str]:
        """
        The Kubernetes version to upgrade the member clusters to.
        """
        return pulumi.get(self, "kubernetes_version")


@pulumi.output_type
class ManagedServiceIdentityResponse(dict):
    """
    Managed service identity (system assigned and/or user assigned identities)
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "userAssignedIdentities":
            suggest = "user_assigned_identities"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedServiceIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedServiceIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedServiceIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']] = None):
        """
        Managed service identity (system assigned and/or user assigned identities)
        :param str principal_id: The service principal ID of the system assigned identity. This property will only be provided for a system assigned identity.
        :param str tenant_id: The tenant ID of the system assigned identity. This property will only be provided for a system assigned identity.
        :param str type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        :param Mapping[str, 'UserAssignedIdentityResponse'] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The service principal ID of the system assigned identity. This property will only be provided for a system assigned identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the system assigned identity. This property will only be provided for a system assigned identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")


@pulumi.output_type
class MemberUpdateStatusResponse(dict):
    """
    The status of a member update operation.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clusterResourceId":
            suggest = "cluster_resource_id"
        elif key == "operationId":
            suggest = "operation_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MemberUpdateStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MemberUpdateStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MemberUpdateStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cluster_resource_id: str,
                 message: str,
                 name: str,
                 operation_id: str,
                 status: 'outputs.UpdateStatusResponse'):
        """
        The status of a member update operation.
        :param str cluster_resource_id: The Azure resource id of the target Kubernetes cluster.
        :param str message: The status message after processing the member update operation.
        :param str name: The name of the FleetMember.
        :param str operation_id: The operation resource id of the latest attempt to perform the operation.
        :param 'UpdateStatusResponse' status: The status of the MemberUpdate operation.
        """
        pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "operation_id", operation_id)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> str:
        """
        The Azure resource id of the target Kubernetes cluster.
        """
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter
    def message(self) -> str:
        """
        The status message after processing the member update operation.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the FleetMember.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> str:
        """
        The operation resource id of the latest attempt to perform the operation.
        """
        return pulumi.get(self, "operation_id")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.UpdateStatusResponse':
        """
        The status of the MemberUpdate operation.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class NodeImageSelectionResponse(dict):
    """
    The node image upgrade to be applied to the target nodes in update run.
    """
    def __init__(__self__, *,
                 type: str):
        """
        The node image upgrade to be applied to the target nodes in update run.
        :param str type: The node image upgrade type.
        """
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The node image upgrade type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class NodeImageSelectionStatusResponse(dict):
    """
    The node image upgrade specs for the update run.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "selectedNodeImageVersions":
            suggest = "selected_node_image_versions"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodeImageSelectionStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodeImageSelectionStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodeImageSelectionStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 selected_node_image_versions: Sequence['outputs.NodeImageVersionResponse']):
        """
        The node image upgrade specs for the update run.
        :param Sequence['NodeImageVersionResponse'] selected_node_image_versions: The image versions to upgrade the nodes to.
        """
        pulumi.set(__self__, "selected_node_image_versions", selected_node_image_versions)

    @property
    @pulumi.getter(name="selectedNodeImageVersions")
    def selected_node_image_versions(self) -> Sequence['outputs.NodeImageVersionResponse']:
        """
        The image versions to upgrade the nodes to.
        """
        return pulumi.get(self, "selected_node_image_versions")


@pulumi.output_type
class NodeImageVersionResponse(dict):
    """
    The node upgrade image version.
    """
    def __init__(__self__, *,
                 version: str):
        """
        The node upgrade image version.
        :param str version: The image version to upgrade the nodes to (e.g., 'AKSUbuntu-1804gen2containerd-2022.12.13').
        """
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The image version to upgrade the nodes to (e.g., 'AKSUbuntu-1804gen2containerd-2022.12.13').
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class UpdateGroupResponse(dict):
    """
    A group to be updated.
    """
    def __init__(__self__, *,
                 name: str):
        """
        A group to be updated.
        :param str name: Name of the group.
               It must match a group name of an existing fleet member. 
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the group.
        It must match a group name of an existing fleet member. 
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class UpdateGroupStatusResponse(dict):
    """
    The status of a UpdateGroup.
    """
    def __init__(__self__, *,
                 members: Sequence['outputs.MemberUpdateStatusResponse'],
                 name: str,
                 status: 'outputs.UpdateStatusResponse'):
        """
        The status of a UpdateGroup.
        :param Sequence['MemberUpdateStatusResponse'] members: The list of member this UpdateGroup updates.
        :param str name: The name of the UpdateGroup.
        :param 'UpdateStatusResponse' status: The status of the UpdateGroup.
        """
        pulumi.set(__self__, "members", members)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def members(self) -> Sequence['outputs.MemberUpdateStatusResponse']:
        """
        The list of member this UpdateGroup updates.
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the UpdateGroup.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.UpdateStatusResponse':
        """
        The status of the UpdateGroup.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class UpdateRunStatusResponse(dict):
    """
    The status of a UpdateRun.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nodeImageSelection":
            suggest = "node_image_selection"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UpdateRunStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UpdateRunStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UpdateRunStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 node_image_selection: 'outputs.NodeImageSelectionStatusResponse',
                 stages: Sequence['outputs.UpdateStageStatusResponse'],
                 status: 'outputs.UpdateStatusResponse'):
        """
        The status of a UpdateRun.
        :param 'NodeImageSelectionStatusResponse' node_image_selection: The node image upgrade specs for the update run. It is only set in update run when `NodeImageSelection.type` is `Consistent`.
        :param Sequence['UpdateStageStatusResponse'] stages: The stages composing an update run. Stages are run sequentially withing an UpdateRun.
        :param 'UpdateStatusResponse' status: The status of the UpdateRun.
        """
        pulumi.set(__self__, "node_image_selection", node_image_selection)
        pulumi.set(__self__, "stages", stages)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="nodeImageSelection")
    def node_image_selection(self) -> 'outputs.NodeImageSelectionStatusResponse':
        """
        The node image upgrade specs for the update run. It is only set in update run when `NodeImageSelection.type` is `Consistent`.
        """
        return pulumi.get(self, "node_image_selection")

    @property
    @pulumi.getter
    def stages(self) -> Sequence['outputs.UpdateStageStatusResponse']:
        """
        The stages composing an update run. Stages are run sequentially withing an UpdateRun.
        """
        return pulumi.get(self, "stages")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.UpdateStatusResponse':
        """
        The status of the UpdateRun.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class UpdateRunStrategyResponse(dict):
    """
    Defines the update sequence of the clusters via stages and groups.

    Stages within a run are executed sequentially one after another.
    Groups within a stage are executed in parallel.
    Member clusters within a group are updated sequentially one after another.

    A valid strategy contains no duplicate groups within or across stages.
    """
    def __init__(__self__, *,
                 stages: Sequence['outputs.UpdateStageResponse']):
        """
        Defines the update sequence of the clusters via stages and groups.

        Stages within a run are executed sequentially one after another.
        Groups within a stage are executed in parallel.
        Member clusters within a group are updated sequentially one after another.

        A valid strategy contains no duplicate groups within or across stages.
        :param Sequence['UpdateStageResponse'] stages: The list of stages that compose this update run. Min size: 1.
        """
        pulumi.set(__self__, "stages", stages)

    @property
    @pulumi.getter
    def stages(self) -> Sequence['outputs.UpdateStageResponse']:
        """
        The list of stages that compose this update run. Min size: 1.
        """
        return pulumi.get(self, "stages")


@pulumi.output_type
class UpdateStageResponse(dict):
    """
    Defines a stage which contains the groups to update and the steps to take (e.g., wait for a time period) before starting the next stage.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "afterStageWaitInSeconds":
            suggest = "after_stage_wait_in_seconds"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UpdateStageResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UpdateStageResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UpdateStageResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 after_stage_wait_in_seconds: Optional[int] = None,
                 groups: Optional[Sequence['outputs.UpdateGroupResponse']] = None):
        """
        Defines a stage which contains the groups to update and the steps to take (e.g., wait for a time period) before starting the next stage.
        :param str name: The name of the stage. Must be unique within the UpdateRun.
        :param int after_stage_wait_in_seconds: The time in seconds to wait at the end of this stage before starting the next one. Defaults to 0 seconds if unspecified.
        :param Sequence['UpdateGroupResponse'] groups: Defines the groups to be executed in parallel in this stage. Duplicate groups are not allowed. Min size: 1.
        """
        pulumi.set(__self__, "name", name)
        if after_stage_wait_in_seconds is not None:
            pulumi.set(__self__, "after_stage_wait_in_seconds", after_stage_wait_in_seconds)
        if groups is not None:
            pulumi.set(__self__, "groups", groups)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the stage. Must be unique within the UpdateRun.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="afterStageWaitInSeconds")
    def after_stage_wait_in_seconds(self) -> Optional[int]:
        """
        The time in seconds to wait at the end of this stage before starting the next one. Defaults to 0 seconds if unspecified.
        """
        return pulumi.get(self, "after_stage_wait_in_seconds")

    @property
    @pulumi.getter
    def groups(self) -> Optional[Sequence['outputs.UpdateGroupResponse']]:
        """
        Defines the groups to be executed in parallel in this stage. Duplicate groups are not allowed. Min size: 1.
        """
        return pulumi.get(self, "groups")


@pulumi.output_type
class UpdateStageStatusResponse(dict):
    """
    The status of a UpdateStage.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "afterStageWaitStatus":
            suggest = "after_stage_wait_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UpdateStageStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UpdateStageStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UpdateStageStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 after_stage_wait_status: 'outputs.WaitStatusResponse',
                 groups: Sequence['outputs.UpdateGroupStatusResponse'],
                 name: str,
                 status: 'outputs.UpdateStatusResponse'):
        """
        The status of a UpdateStage.
        :param 'WaitStatusResponse' after_stage_wait_status: The status of the wait period configured on the UpdateStage.
        :param Sequence['UpdateGroupStatusResponse'] groups: The list of groups to be updated as part of this UpdateStage.
        :param str name: The name of the UpdateStage.
        :param 'UpdateStatusResponse' status: The status of the UpdateStage.
        """
        pulumi.set(__self__, "after_stage_wait_status", after_stage_wait_status)
        pulumi.set(__self__, "groups", groups)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="afterStageWaitStatus")
    def after_stage_wait_status(self) -> 'outputs.WaitStatusResponse':
        """
        The status of the wait period configured on the UpdateStage.
        """
        return pulumi.get(self, "after_stage_wait_status")

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.UpdateGroupStatusResponse']:
        """
        The list of groups to be updated as part of this UpdateStage.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the UpdateStage.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.UpdateStatusResponse':
        """
        The status of the UpdateStage.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class UpdateStatusResponse(dict):
    """
    The status for an operation or group of operations.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "completedTime":
            suggest = "completed_time"
        elif key == "startTime":
            suggest = "start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UpdateStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UpdateStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UpdateStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 completed_time: str,
                 error: 'outputs.ErrorDetailResponse',
                 start_time: str,
                 state: str):
        """
        The status for an operation or group of operations.
        :param str completed_time: The time the operation or group was completed.
        :param 'ErrorDetailResponse' error: The error details when a failure is encountered.
        :param str start_time: The time the operation or group was started.
        :param str state: The State of the operation or group.
        """
        pulumi.set(__self__, "completed_time", completed_time)
        pulumi.set(__self__, "error", error)
        pulumi.set(__self__, "start_time", start_time)
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="completedTime")
    def completed_time(self) -> str:
        """
        The time the operation or group was completed.
        """
        return pulumi.get(self, "completed_time")

    @property
    @pulumi.getter
    def error(self) -> 'outputs.ErrorDetailResponse':
        """
        The error details when a failure is encountered.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        The time the operation or group was started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The State of the operation or group.
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    """
    User assigned identity properties
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAssignedIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 principal_id: str):
        """
        User assigned identity properties
        :param str client_id: The client ID of the assigned identity.
        :param str principal_id: The principal ID of the assigned identity.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The client ID of the assigned identity.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of the assigned identity.
        """
        return pulumi.get(self, "principal_id")


@pulumi.output_type
class WaitStatusResponse(dict):
    """
    The status of the wait duration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "waitDurationInSeconds":
            suggest = "wait_duration_in_seconds"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WaitStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WaitStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WaitStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 status: 'outputs.UpdateStatusResponse',
                 wait_duration_in_seconds: int):
        """
        The status of the wait duration.
        :param 'UpdateStatusResponse' status: The status of the wait duration.
        :param int wait_duration_in_seconds: The wait duration configured in seconds.
        """
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "wait_duration_in_seconds", wait_duration_in_seconds)

    @property
    @pulumi.getter
    def status(self) -> 'outputs.UpdateStatusResponse':
        """
        The status of the wait duration.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="waitDurationInSeconds")
    def wait_duration_in_seconds(self) -> int:
        """
        The wait duration configured in seconds.
        """
        return pulumi.get(self, "wait_duration_in_seconds")


