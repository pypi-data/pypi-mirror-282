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
from ._inputs import *

__all__ = ['AttestationAtResourceGroupArgs', 'AttestationAtResourceGroup']

@pulumi.input_type
class AttestationAtResourceGroupArgs:
    def __init__(__self__, *,
                 policy_assignment_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 assessment_date: Optional[pulumi.Input[str]] = None,
                 attestation_name: Optional[pulumi.Input[str]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 compliance_state: Optional[pulumi.Input[Union[str, 'ComplianceState']]] = None,
                 evidence: Optional[pulumi.Input[Sequence[pulumi.Input['AttestationEvidenceArgs']]]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AttestationAtResourceGroup resource.
        :param pulumi.Input[str] policy_assignment_id: The resource ID of the policy assignment that the attestation is setting the state for.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] assessment_date: The time the evidence was assessed
        :param pulumi.Input[str] attestation_name: The name of the attestation.
        :param pulumi.Input[str] comments: Comments describing why this attestation was created.
        :param pulumi.Input[Union[str, 'ComplianceState']] compliance_state: The compliance state that should be set on the resource.
        :param pulumi.Input[Sequence[pulumi.Input['AttestationEvidenceArgs']]] evidence: The evidence supporting the compliance state set in this attestation.
        :param pulumi.Input[str] expires_on: The time the compliance state should expire.
        :param Any metadata: Additional metadata for this attestation
        :param pulumi.Input[str] owner: The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.
        :param pulumi.Input[str] policy_definition_reference_id: The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.
        """
        pulumi.set(__self__, "policy_assignment_id", policy_assignment_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if assessment_date is not None:
            pulumi.set(__self__, "assessment_date", assessment_date)
        if attestation_name is not None:
            pulumi.set(__self__, "attestation_name", attestation_name)
        if comments is not None:
            pulumi.set(__self__, "comments", comments)
        if compliance_state is not None:
            pulumi.set(__self__, "compliance_state", compliance_state)
        if evidence is not None:
            pulumi.set(__self__, "evidence", evidence)
        if expires_on is not None:
            pulumi.set(__self__, "expires_on", expires_on)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if policy_definition_reference_id is not None:
            pulumi.set(__self__, "policy_definition_reference_id", policy_definition_reference_id)

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the policy assignment that the attestation is setting the state for.
        """
        return pulumi.get(self, "policy_assignment_id")

    @policy_assignment_id.setter
    def policy_assignment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_assignment_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="assessmentDate")
    def assessment_date(self) -> Optional[pulumi.Input[str]]:
        """
        The time the evidence was assessed
        """
        return pulumi.get(self, "assessment_date")

    @assessment_date.setter
    def assessment_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_date", value)

    @property
    @pulumi.getter(name="attestationName")
    def attestation_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the attestation.
        """
        return pulumi.get(self, "attestation_name")

    @attestation_name.setter
    def attestation_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attestation_name", value)

    @property
    @pulumi.getter
    def comments(self) -> Optional[pulumi.Input[str]]:
        """
        Comments describing why this attestation was created.
        """
        return pulumi.get(self, "comments")

    @comments.setter
    def comments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comments", value)

    @property
    @pulumi.getter(name="complianceState")
    def compliance_state(self) -> Optional[pulumi.Input[Union[str, 'ComplianceState']]]:
        """
        The compliance state that should be set on the resource.
        """
        return pulumi.get(self, "compliance_state")

    @compliance_state.setter
    def compliance_state(self, value: Optional[pulumi.Input[Union[str, 'ComplianceState']]]):
        pulumi.set(self, "compliance_state", value)

    @property
    @pulumi.getter
    def evidence(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AttestationEvidenceArgs']]]]:
        """
        The evidence supporting the compliance state set in this attestation.
        """
        return pulumi.get(self, "evidence")

    @evidence.setter
    def evidence(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AttestationEvidenceArgs']]]]):
        pulumi.set(self, "evidence", value)

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[pulumi.Input[str]]:
        """
        The time the compliance state should expire.
        """
        return pulumi.get(self, "expires_on")

    @expires_on.setter
    def expires_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_on", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        Additional metadata for this attestation
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> Optional[pulumi.Input[str]]:
        """
        The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @policy_definition_reference_id.setter
    def policy_definition_reference_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_reference_id", value)


class AttestationAtResourceGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_date: Optional[pulumi.Input[str]] = None,
                 attestation_name: Optional[pulumi.Input[str]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 compliance_state: Optional[pulumi.Input[Union[str, 'ComplianceState']]] = None,
                 evidence: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AttestationEvidenceArgs']]]]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An attestation resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assessment_date: The time the evidence was assessed
        :param pulumi.Input[str] attestation_name: The name of the attestation.
        :param pulumi.Input[str] comments: Comments describing why this attestation was created.
        :param pulumi.Input[Union[str, 'ComplianceState']] compliance_state: The compliance state that should be set on the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AttestationEvidenceArgs']]]] evidence: The evidence supporting the compliance state set in this attestation.
        :param pulumi.Input[str] expires_on: The time the compliance state should expire.
        :param Any metadata: Additional metadata for this attestation
        :param pulumi.Input[str] owner: The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.
        :param pulumi.Input[str] policy_assignment_id: The resource ID of the policy assignment that the attestation is setting the state for.
        :param pulumi.Input[str] policy_definition_reference_id: The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttestationAtResourceGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An attestation resource.

        :param str resource_name: The name of the resource.
        :param AttestationAtResourceGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttestationAtResourceGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_date: Optional[pulumi.Input[str]] = None,
                 attestation_name: Optional[pulumi.Input[str]] = None,
                 comments: Optional[pulumi.Input[str]] = None,
                 compliance_state: Optional[pulumi.Input[Union[str, 'ComplianceState']]] = None,
                 evidence: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AttestationEvidenceArgs']]]]] = None,
                 expires_on: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 policy_assignment_id: Optional[pulumi.Input[str]] = None,
                 policy_definition_reference_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AttestationAtResourceGroupArgs.__new__(AttestationAtResourceGroupArgs)

            __props__.__dict__["assessment_date"] = assessment_date
            __props__.__dict__["attestation_name"] = attestation_name
            __props__.__dict__["comments"] = comments
            __props__.__dict__["compliance_state"] = compliance_state
            __props__.__dict__["evidence"] = evidence
            __props__.__dict__["expires_on"] = expires_on
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["owner"] = owner
            if policy_assignment_id is None and not opts.urn:
                raise TypeError("Missing required property 'policy_assignment_id'")
            __props__.__dict__["policy_assignment_id"] = policy_assignment_id
            __props__.__dict__["policy_definition_reference_id"] = policy_definition_reference_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["last_compliance_state_change_at"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:policyinsights:AttestationAtResourceGroup"), pulumi.Alias(type_="azure-native:policyinsights/v20210101:AttestationAtResourceGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AttestationAtResourceGroup, __self__).__init__(
            'azure-native:policyinsights/v20220901:AttestationAtResourceGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AttestationAtResourceGroup':
        """
        Get an existing AttestationAtResourceGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AttestationAtResourceGroupArgs.__new__(AttestationAtResourceGroupArgs)

        __props__.__dict__["assessment_date"] = None
        __props__.__dict__["comments"] = None
        __props__.__dict__["compliance_state"] = None
        __props__.__dict__["evidence"] = None
        __props__.__dict__["expires_on"] = None
        __props__.__dict__["last_compliance_state_change_at"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["policy_assignment_id"] = None
        __props__.__dict__["policy_definition_reference_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return AttestationAtResourceGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assessmentDate")
    def assessment_date(self) -> pulumi.Output[Optional[str]]:
        """
        The time the evidence was assessed
        """
        return pulumi.get(self, "assessment_date")

    @property
    @pulumi.getter
    def comments(self) -> pulumi.Output[Optional[str]]:
        """
        Comments describing why this attestation was created.
        """
        return pulumi.get(self, "comments")

    @property
    @pulumi.getter(name="complianceState")
    def compliance_state(self) -> pulumi.Output[Optional[str]]:
        """
        The compliance state that should be set on the resource.
        """
        return pulumi.get(self, "compliance_state")

    @property
    @pulumi.getter
    def evidence(self) -> pulumi.Output[Optional[Sequence['outputs.AttestationEvidenceResponse']]]:
        """
        The evidence supporting the compliance state set in this attestation.
        """
        return pulumi.get(self, "evidence")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> pulumi.Output[Optional[str]]:
        """
        The time the compliance state should expire.
        """
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter(name="lastComplianceStateChangeAt")
    def last_compliance_state_change_at(self) -> pulumi.Output[str]:
        """
        The time the compliance state was last changed in this attestation.
        """
        return pulumi.get(self, "last_compliance_state_change_at")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        Additional metadata for this attestation
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional[str]]:
        """
        The person responsible for setting the state of the resource. This value is typically an Azure Active Directory object ID.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="policyAssignmentId")
    def policy_assignment_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the policy assignment that the attestation is setting the state for.
        """
        return pulumi.get(self, "policy_assignment_id")

    @property
    @pulumi.getter(name="policyDefinitionReferenceId")
    def policy_definition_reference_id(self) -> pulumi.Output[Optional[str]]:
        """
        The policy definition reference ID from a policy set definition that the attestation is setting the state for. If the policy assignment assigns a policy set definition the attestation can choose a definition within the set definition with this property or omit this and set the state for the entire set definition.
        """
        return pulumi.get(self, "policy_definition_reference_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the attestation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

