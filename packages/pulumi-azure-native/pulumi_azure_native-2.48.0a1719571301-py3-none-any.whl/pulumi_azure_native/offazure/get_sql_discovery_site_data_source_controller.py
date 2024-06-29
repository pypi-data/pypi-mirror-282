# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetSqlDiscoverySiteDataSourceControllerResult',
    'AwaitableGetSqlDiscoverySiteDataSourceControllerResult',
    'get_sql_discovery_site_data_source_controller',
    'get_sql_discovery_site_data_source_controller_output',
]

@pulumi.output_type
class GetSqlDiscoverySiteDataSourceControllerResult:
    """
    A SQL discovery site data source resource.
    """
    def __init__(__self__, discovery_site_id=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if discovery_site_id and not isinstance(discovery_site_id, str):
            raise TypeError("Expected argument 'discovery_site_id' to be a str")
        pulumi.set(__self__, "discovery_site_id", discovery_site_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[str]:
        """
        Gets or sets the discovery site Id.
        """
        return pulumi.get(self, "discovery_site_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
        provisioning state enum
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


class AwaitableGetSqlDiscoverySiteDataSourceControllerResult(GetSqlDiscoverySiteDataSourceControllerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlDiscoverySiteDataSourceControllerResult(
            discovery_site_id=self.discovery_site_id,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_sql_discovery_site_data_source_controller(discovery_site_data_source_name: Optional[str] = None,
                                                  resource_group_name: Optional[str] = None,
                                                  site_name: Optional[str] = None,
                                                  sql_site_name: Optional[str] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlDiscoverySiteDataSourceControllerResult:
    """
    Get a SqlDiscoverySiteDataSource
    Azure REST API version: 2023-06-06.

    Other available API versions: 2023-10-01-preview.


    :param str discovery_site_data_source_name: SQL Discovery site data source name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    :param str sql_site_name: SQL site name.
    """
    __args__ = dict()
    __args__['discoverySiteDataSourceName'] = discovery_site_data_source_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['siteName'] = site_name
    __args__['sqlSiteName'] = sql_site_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:offazure:getSqlDiscoverySiteDataSourceController', __args__, opts=opts, typ=GetSqlDiscoverySiteDataSourceControllerResult).value

    return AwaitableGetSqlDiscoverySiteDataSourceControllerResult(
        discovery_site_id=pulumi.get(__ret__, 'discovery_site_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_sql_discovery_site_data_source_controller)
def get_sql_discovery_site_data_source_controller_output(discovery_site_data_source_name: Optional[pulumi.Input[str]] = None,
                                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                                         site_name: Optional[pulumi.Input[str]] = None,
                                                         sql_site_name: Optional[pulumi.Input[str]] = None,
                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlDiscoverySiteDataSourceControllerResult]:
    """
    Get a SqlDiscoverySiteDataSource
    Azure REST API version: 2023-06-06.

    Other available API versions: 2023-10-01-preview.


    :param str discovery_site_data_source_name: SQL Discovery site data source name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str site_name: Site name
    :param str sql_site_name: SQL site name.
    """
    ...
