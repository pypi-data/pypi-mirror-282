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
    'GetRoleAssignmentResult',
    'AwaitableGetRoleAssignmentResult',
    'get_role_assignment',
    'get_role_assignment_output',
]

@pulumi.output_type
class GetRoleAssignmentResult:
    """
    The Role Assignment resource format.
    """
    def __init__(__self__, assignment_name=None, conflation_policies=None, connectors=None, description=None, display_name=None, id=None, interactions=None, kpis=None, links=None, name=None, principals=None, profiles=None, provisioning_state=None, relationship_links=None, relationships=None, role=None, role_assignments=None, sas_policies=None, segments=None, tenant_id=None, type=None, views=None, widget_types=None):
        if assignment_name and not isinstance(assignment_name, str):
            raise TypeError("Expected argument 'assignment_name' to be a str")
        pulumi.set(__self__, "assignment_name", assignment_name)
        if conflation_policies and not isinstance(conflation_policies, dict):
            raise TypeError("Expected argument 'conflation_policies' to be a dict")
        pulumi.set(__self__, "conflation_policies", conflation_policies)
        if connectors and not isinstance(connectors, dict):
            raise TypeError("Expected argument 'connectors' to be a dict")
        pulumi.set(__self__, "connectors", connectors)
        if description and not isinstance(description, dict):
            raise TypeError("Expected argument 'description' to be a dict")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, dict):
            raise TypeError("Expected argument 'display_name' to be a dict")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interactions and not isinstance(interactions, dict):
            raise TypeError("Expected argument 'interactions' to be a dict")
        pulumi.set(__self__, "interactions", interactions)
        if kpis and not isinstance(kpis, dict):
            raise TypeError("Expected argument 'kpis' to be a dict")
        pulumi.set(__self__, "kpis", kpis)
        if links and not isinstance(links, dict):
            raise TypeError("Expected argument 'links' to be a dict")
        pulumi.set(__self__, "links", links)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if principals and not isinstance(principals, list):
            raise TypeError("Expected argument 'principals' to be a list")
        pulumi.set(__self__, "principals", principals)
        if profiles and not isinstance(profiles, dict):
            raise TypeError("Expected argument 'profiles' to be a dict")
        pulumi.set(__self__, "profiles", profiles)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if relationship_links and not isinstance(relationship_links, dict):
            raise TypeError("Expected argument 'relationship_links' to be a dict")
        pulumi.set(__self__, "relationship_links", relationship_links)
        if relationships and not isinstance(relationships, dict):
            raise TypeError("Expected argument 'relationships' to be a dict")
        pulumi.set(__self__, "relationships", relationships)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if role_assignments and not isinstance(role_assignments, dict):
            raise TypeError("Expected argument 'role_assignments' to be a dict")
        pulumi.set(__self__, "role_assignments", role_assignments)
        if sas_policies and not isinstance(sas_policies, dict):
            raise TypeError("Expected argument 'sas_policies' to be a dict")
        pulumi.set(__self__, "sas_policies", sas_policies)
        if segments and not isinstance(segments, dict):
            raise TypeError("Expected argument 'segments' to be a dict")
        pulumi.set(__self__, "segments", segments)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if views and not isinstance(views, dict):
            raise TypeError("Expected argument 'views' to be a dict")
        pulumi.set(__self__, "views", views)
        if widget_types and not isinstance(widget_types, dict):
            raise TypeError("Expected argument 'widget_types' to be a dict")
        pulumi.set(__self__, "widget_types", widget_types)

    @property
    @pulumi.getter(name="assignmentName")
    def assignment_name(self) -> str:
        """
        The name of the metadata object.
        """
        return pulumi.get(self, "assignment_name")

    @property
    @pulumi.getter(name="conflationPolicies")
    def conflation_policies(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Widget types set for the assignment.
        """
        return pulumi.get(self, "conflation_policies")

    @property
    @pulumi.getter
    def connectors(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Connectors set for the assignment.
        """
        return pulumi.get(self, "connectors")

    @property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, str]]:
        """
        Localized description for the metadata.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, str]]:
        """
        Localized display names for the metadata.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def interactions(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Interactions set for the assignment.
        """
        return pulumi.get(self, "interactions")

    @property
    @pulumi.getter
    def kpis(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Kpis set for the assignment.
        """
        return pulumi.get(self, "kpis")

    @property
    @pulumi.getter
    def links(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Links set for the assignment.
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def principals(self) -> Sequence['outputs.AssignmentPrincipalResponse']:
        """
        The principals being assigned to.
        """
        return pulumi.get(self, "principals")

    @property
    @pulumi.getter
    def profiles(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Profiles set for the assignment.
        """
        return pulumi.get(self, "profiles")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="relationshipLinks")
    def relationship_links(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        The Role assignments set for the relationship links.
        """
        return pulumi.get(self, "relationship_links")

    @property
    @pulumi.getter
    def relationships(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        The Role assignments set for the relationships.
        """
        return pulumi.get(self, "relationships")

    @property
    @pulumi.getter
    def role(self) -> str:
        """
        Type of roles.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="roleAssignments")
    def role_assignments(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        The Role assignments set for the assignment.
        """
        return pulumi.get(self, "role_assignments")

    @property
    @pulumi.getter(name="sasPolicies")
    def sas_policies(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Sas Policies set for the assignment.
        """
        return pulumi.get(self, "sas_policies")

    @property
    @pulumi.getter
    def segments(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        The Role assignments set for the assignment.
        """
        return pulumi.get(self, "segments")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def views(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Views set for the assignment.
        """
        return pulumi.get(self, "views")

    @property
    @pulumi.getter(name="widgetTypes")
    def widget_types(self) -> Optional['outputs.ResourceSetDescriptionResponse']:
        """
        Widget types set for the assignment.
        """
        return pulumi.get(self, "widget_types")


class AwaitableGetRoleAssignmentResult(GetRoleAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleAssignmentResult(
            assignment_name=self.assignment_name,
            conflation_policies=self.conflation_policies,
            connectors=self.connectors,
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            interactions=self.interactions,
            kpis=self.kpis,
            links=self.links,
            name=self.name,
            principals=self.principals,
            profiles=self.profiles,
            provisioning_state=self.provisioning_state,
            relationship_links=self.relationship_links,
            relationships=self.relationships,
            role=self.role,
            role_assignments=self.role_assignments,
            sas_policies=self.sas_policies,
            segments=self.segments,
            tenant_id=self.tenant_id,
            type=self.type,
            views=self.views,
            widget_types=self.widget_types)


def get_role_assignment(assignment_name: Optional[str] = None,
                        hub_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleAssignmentResult:
    """
    Gets the role assignment in the hub.


    :param str assignment_name: The name of the role assignment.
    :param str hub_name: The name of the hub.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['assignmentName'] = assignment_name
    __args__['hubName'] = hub_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:customerinsights/v20170426:getRoleAssignment', __args__, opts=opts, typ=GetRoleAssignmentResult).value

    return AwaitableGetRoleAssignmentResult(
        assignment_name=pulumi.get(__ret__, 'assignment_name'),
        conflation_policies=pulumi.get(__ret__, 'conflation_policies'),
        connectors=pulumi.get(__ret__, 'connectors'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        interactions=pulumi.get(__ret__, 'interactions'),
        kpis=pulumi.get(__ret__, 'kpis'),
        links=pulumi.get(__ret__, 'links'),
        name=pulumi.get(__ret__, 'name'),
        principals=pulumi.get(__ret__, 'principals'),
        profiles=pulumi.get(__ret__, 'profiles'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        relationship_links=pulumi.get(__ret__, 'relationship_links'),
        relationships=pulumi.get(__ret__, 'relationships'),
        role=pulumi.get(__ret__, 'role'),
        role_assignments=pulumi.get(__ret__, 'role_assignments'),
        sas_policies=pulumi.get(__ret__, 'sas_policies'),
        segments=pulumi.get(__ret__, 'segments'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'),
        views=pulumi.get(__ret__, 'views'),
        widget_types=pulumi.get(__ret__, 'widget_types'))


@_utilities.lift_output_func(get_role_assignment)
def get_role_assignment_output(assignment_name: Optional[pulumi.Input[str]] = None,
                               hub_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleAssignmentResult]:
    """
    Gets the role assignment in the hub.


    :param str assignment_name: The name of the role assignment.
    :param str hub_name: The name of the hub.
    :param str resource_group_name: The name of the resource group.
    """
    ...
