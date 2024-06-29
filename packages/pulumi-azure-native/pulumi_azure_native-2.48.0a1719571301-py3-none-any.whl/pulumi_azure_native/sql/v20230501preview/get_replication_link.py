# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetReplicationLinkResult',
    'AwaitableGetReplicationLinkResult',
    'get_replication_link',
    'get_replication_link_output',
]

@pulumi.output_type
class GetReplicationLinkResult:
    """
    A replication link.
    """
    def __init__(__self__, id=None, is_termination_allowed=None, link_type=None, name=None, partner_database=None, partner_database_id=None, partner_location=None, partner_role=None, partner_server=None, percent_complete=None, replication_mode=None, replication_state=None, role=None, start_time=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_termination_allowed and not isinstance(is_termination_allowed, bool):
            raise TypeError("Expected argument 'is_termination_allowed' to be a bool")
        pulumi.set(__self__, "is_termination_allowed", is_termination_allowed)
        if link_type and not isinstance(link_type, str):
            raise TypeError("Expected argument 'link_type' to be a str")
        pulumi.set(__self__, "link_type", link_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partner_database and not isinstance(partner_database, str):
            raise TypeError("Expected argument 'partner_database' to be a str")
        pulumi.set(__self__, "partner_database", partner_database)
        if partner_database_id and not isinstance(partner_database_id, str):
            raise TypeError("Expected argument 'partner_database_id' to be a str")
        pulumi.set(__self__, "partner_database_id", partner_database_id)
        if partner_location and not isinstance(partner_location, str):
            raise TypeError("Expected argument 'partner_location' to be a str")
        pulumi.set(__self__, "partner_location", partner_location)
        if partner_role and not isinstance(partner_role, str):
            raise TypeError("Expected argument 'partner_role' to be a str")
        pulumi.set(__self__, "partner_role", partner_role)
        if partner_server and not isinstance(partner_server, str):
            raise TypeError("Expected argument 'partner_server' to be a str")
        pulumi.set(__self__, "partner_server", partner_server)
        if percent_complete and not isinstance(percent_complete, int):
            raise TypeError("Expected argument 'percent_complete' to be a int")
        pulumi.set(__self__, "percent_complete", percent_complete)
        if replication_mode and not isinstance(replication_mode, str):
            raise TypeError("Expected argument 'replication_mode' to be a str")
        pulumi.set(__self__, "replication_mode", replication_mode)
        if replication_state and not isinstance(replication_state, str):
            raise TypeError("Expected argument 'replication_state' to be a str")
        pulumi.set(__self__, "replication_state", replication_state)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isTerminationAllowed")
    def is_termination_allowed(self) -> bool:
        """
        Whether the user is currently allowed to terminate the link.
        """
        return pulumi.get(self, "is_termination_allowed")

    @property
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[str]:
        """
        Link type (GEO, NAMED, STANDBY). Update operation does not support NAMED.
        """
        return pulumi.get(self, "link_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerDatabase")
    def partner_database(self) -> str:
        """
        Resource partner database.
        """
        return pulumi.get(self, "partner_database")

    @property
    @pulumi.getter(name="partnerDatabaseId")
    def partner_database_id(self) -> str:
        """
        Resource partner database Id.
        """
        return pulumi.get(self, "partner_database_id")

    @property
    @pulumi.getter(name="partnerLocation")
    def partner_location(self) -> str:
        """
        Resource partner location.
        """
        return pulumi.get(self, "partner_location")

    @property
    @pulumi.getter(name="partnerRole")
    def partner_role(self) -> str:
        """
        Partner replication role.
        """
        return pulumi.get(self, "partner_role")

    @property
    @pulumi.getter(name="partnerServer")
    def partner_server(self) -> str:
        """
        Resource partner server.
        """
        return pulumi.get(self, "partner_server")

    @property
    @pulumi.getter(name="percentComplete")
    def percent_complete(self) -> int:
        """
        Seeding completion percentage for the link.
        """
        return pulumi.get(self, "percent_complete")

    @property
    @pulumi.getter(name="replicationMode")
    def replication_mode(self) -> str:
        """
        Replication mode.
        """
        return pulumi.get(self, "replication_mode")

    @property
    @pulumi.getter(name="replicationState")
    def replication_state(self) -> str:
        """
        Replication state (PENDING, SEEDING, CATCHUP, SUSPENDED).
        """
        return pulumi.get(self, "replication_state")

    @property
    @pulumi.getter
    def role(self) -> str:
        """
        Local replication role.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Time at which the link was created.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetReplicationLinkResult(GetReplicationLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationLinkResult(
            id=self.id,
            is_termination_allowed=self.is_termination_allowed,
            link_type=self.link_type,
            name=self.name,
            partner_database=self.partner_database,
            partner_database_id=self.partner_database_id,
            partner_location=self.partner_location,
            partner_role=self.partner_role,
            partner_server=self.partner_server,
            percent_complete=self.percent_complete,
            replication_mode=self.replication_mode,
            replication_state=self.replication_state,
            role=self.role,
            start_time=self.start_time,
            type=self.type)


def get_replication_link(database_name: Optional[str] = None,
                         link_id: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         server_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationLinkResult:
    """
    Gets a replication link.


    :param str database_name: The name of the database.
    :param str link_id: The name of the replication link.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['linkId'] = link_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230501preview:getReplicationLink', __args__, opts=opts, typ=GetReplicationLinkResult).value

    return AwaitableGetReplicationLinkResult(
        id=pulumi.get(__ret__, 'id'),
        is_termination_allowed=pulumi.get(__ret__, 'is_termination_allowed'),
        link_type=pulumi.get(__ret__, 'link_type'),
        name=pulumi.get(__ret__, 'name'),
        partner_database=pulumi.get(__ret__, 'partner_database'),
        partner_database_id=pulumi.get(__ret__, 'partner_database_id'),
        partner_location=pulumi.get(__ret__, 'partner_location'),
        partner_role=pulumi.get(__ret__, 'partner_role'),
        partner_server=pulumi.get(__ret__, 'partner_server'),
        percent_complete=pulumi.get(__ret__, 'percent_complete'),
        replication_mode=pulumi.get(__ret__, 'replication_mode'),
        replication_state=pulumi.get(__ret__, 'replication_state'),
        role=pulumi.get(__ret__, 'role'),
        start_time=pulumi.get(__ret__, 'start_time'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_replication_link)
def get_replication_link_output(database_name: Optional[pulumi.Input[str]] = None,
                                link_id: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                server_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationLinkResult]:
    """
    Gets a replication link.


    :param str database_name: The name of the database.
    :param str link_id: The name of the replication link.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
