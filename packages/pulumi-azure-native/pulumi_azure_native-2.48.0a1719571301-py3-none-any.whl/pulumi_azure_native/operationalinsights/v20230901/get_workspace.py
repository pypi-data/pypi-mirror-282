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
    The top level Workspace resource container.
    """
    def __init__(__self__, created_date=None, customer_id=None, default_data_collection_rule_resource_id=None, etag=None, features=None, force_cmk_for_query=None, id=None, identity=None, location=None, modified_date=None, name=None, private_link_scoped_resources=None, provisioning_state=None, public_network_access_for_ingestion=None, public_network_access_for_query=None, retention_in_days=None, sku=None, system_data=None, tags=None, type=None, workspace_capping=None):
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if customer_id and not isinstance(customer_id, str):
            raise TypeError("Expected argument 'customer_id' to be a str")
        pulumi.set(__self__, "customer_id", customer_id)
        if default_data_collection_rule_resource_id and not isinstance(default_data_collection_rule_resource_id, str):
            raise TypeError("Expected argument 'default_data_collection_rule_resource_id' to be a str")
        pulumi.set(__self__, "default_data_collection_rule_resource_id", default_data_collection_rule_resource_id)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if features and not isinstance(features, dict):
            raise TypeError("Expected argument 'features' to be a dict")
        pulumi.set(__self__, "features", features)
        if force_cmk_for_query and not isinstance(force_cmk_for_query, bool):
            raise TypeError("Expected argument 'force_cmk_for_query' to be a bool")
        pulumi.set(__self__, "force_cmk_for_query", force_cmk_for_query)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if modified_date and not isinstance(modified_date, str):
            raise TypeError("Expected argument 'modified_date' to be a str")
        pulumi.set(__self__, "modified_date", modified_date)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_link_scoped_resources and not isinstance(private_link_scoped_resources, list):
            raise TypeError("Expected argument 'private_link_scoped_resources' to be a list")
        pulumi.set(__self__, "private_link_scoped_resources", private_link_scoped_resources)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access_for_ingestion and not isinstance(public_network_access_for_ingestion, str):
            raise TypeError("Expected argument 'public_network_access_for_ingestion' to be a str")
        pulumi.set(__self__, "public_network_access_for_ingestion", public_network_access_for_ingestion)
        if public_network_access_for_query and not isinstance(public_network_access_for_query, str):
            raise TypeError("Expected argument 'public_network_access_for_query' to be a str")
        pulumi.set(__self__, "public_network_access_for_query", public_network_access_for_query)
        if retention_in_days and not isinstance(retention_in_days, int):
            raise TypeError("Expected argument 'retention_in_days' to be a int")
        pulumi.set(__self__, "retention_in_days", retention_in_days)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if workspace_capping and not isinstance(workspace_capping, dict):
            raise TypeError("Expected argument 'workspace_capping' to be a dict")
        pulumi.set(__self__, "workspace_capping", workspace_capping)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        Workspace creation date.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> str:
        """
        This is a read-only property. Represents the ID associated with the workspace.
        """
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter(name="defaultDataCollectionRuleResourceId")
    def default_data_collection_rule_resource_id(self) -> Optional[str]:
        """
        The resource ID of the default Data Collection Rule to use for this workspace. Expected format is - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dcrName}.
        """
        return pulumi.get(self, "default_data_collection_rule_resource_id")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        The etag of the workspace.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def features(self) -> Optional['outputs.WorkspaceFeaturesResponse']:
        """
        Workspace features.
        """
        return pulumi.get(self, "features")

    @property
    @pulumi.getter(name="forceCmkForQuery")
    def force_cmk_for_query(self) -> Optional[bool]:
        """
        Indicates whether customer managed storage is mandatory for query management.
        """
        return pulumi.get(self, "force_cmk_for_query")

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
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="modifiedDate")
    def modified_date(self) -> str:
        """
        Workspace modification date.
        """
        return pulumi.get(self, "modified_date")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkScopedResources")
    def private_link_scoped_resources(self) -> Sequence['outputs.PrivateLinkScopedResourceResponse']:
        """
        List of linked private link scope resources.
        """
        return pulumi.get(self, "private_link_scoped_resources")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the workspace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccessForIngestion")
    def public_network_access_for_ingestion(self) -> Optional[str]:
        """
        The network access type for accessing Log Analytics ingestion.
        """
        return pulumi.get(self, "public_network_access_for_ingestion")

    @property
    @pulumi.getter(name="publicNetworkAccessForQuery")
    def public_network_access_for_query(self) -> Optional[str]:
        """
        The network access type for accessing Log Analytics query.
        """
        return pulumi.get(self, "public_network_access_for_query")

    @property
    @pulumi.getter(name="retentionInDays")
    def retention_in_days(self) -> Optional[int]:
        """
        The workspace data retention in days. Allowed values are per pricing plan. See pricing tiers documentation for details.
        """
        return pulumi.get(self, "retention_in_days")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.WorkspaceSkuResponse']:
        """
        The SKU of the workspace.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceCapping")
    def workspace_capping(self) -> Optional['outputs.WorkspaceCappingResponse']:
        """
        The daily volume cap for ingestion.
        """
        return pulumi.get(self, "workspace_capping")


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceResult(
            created_date=self.created_date,
            customer_id=self.customer_id,
            default_data_collection_rule_resource_id=self.default_data_collection_rule_resource_id,
            etag=self.etag,
            features=self.features,
            force_cmk_for_query=self.force_cmk_for_query,
            id=self.id,
            identity=self.identity,
            location=self.location,
            modified_date=self.modified_date,
            name=self.name,
            private_link_scoped_resources=self.private_link_scoped_resources,
            provisioning_state=self.provisioning_state,
            public_network_access_for_ingestion=self.public_network_access_for_ingestion,
            public_network_access_for_query=self.public_network_access_for_query,
            retention_in_days=self.retention_in_days,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            workspace_capping=self.workspace_capping)


def get_workspace(resource_group_name: Optional[str] = None,
                  workspace_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceResult:
    """
    Gets a workspace instance.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights/v20230901:getWorkspace', __args__, opts=opts, typ=GetWorkspaceResult).value

    return AwaitableGetWorkspaceResult(
        created_date=pulumi.get(__ret__, 'created_date'),
        customer_id=pulumi.get(__ret__, 'customer_id'),
        default_data_collection_rule_resource_id=pulumi.get(__ret__, 'default_data_collection_rule_resource_id'),
        etag=pulumi.get(__ret__, 'etag'),
        features=pulumi.get(__ret__, 'features'),
        force_cmk_for_query=pulumi.get(__ret__, 'force_cmk_for_query'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        modified_date=pulumi.get(__ret__, 'modified_date'),
        name=pulumi.get(__ret__, 'name'),
        private_link_scoped_resources=pulumi.get(__ret__, 'private_link_scoped_resources'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access_for_ingestion=pulumi.get(__ret__, 'public_network_access_for_ingestion'),
        public_network_access_for_query=pulumi.get(__ret__, 'public_network_access_for_query'),
        retention_in_days=pulumi.get(__ret__, 'retention_in_days'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        workspace_capping=pulumi.get(__ret__, 'workspace_capping'))


@_utilities.lift_output_func(get_workspace)
def get_workspace_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                         workspace_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceResult]:
    """
    Gets a workspace instance.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
