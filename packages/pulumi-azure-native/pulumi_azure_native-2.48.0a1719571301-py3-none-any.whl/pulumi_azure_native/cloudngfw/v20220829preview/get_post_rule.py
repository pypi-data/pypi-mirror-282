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
    'GetPostRuleResult',
    'AwaitableGetPostRuleResult',
    'get_post_rule',
    'get_post_rule_output',
]

@pulumi.output_type
class GetPostRuleResult:
    """
    PostRulestack rule list
    """
    def __init__(__self__, action_type=None, applications=None, audit_comment=None, category=None, decryption_rule_type=None, description=None, destination=None, enable_logging=None, etag=None, id=None, inbound_inspection_certificate=None, name=None, negate_destination=None, negate_source=None, priority=None, protocol=None, protocol_port_list=None, provisioning_state=None, rule_name=None, rule_state=None, source=None, system_data=None, tags=None, type=None):
        if action_type and not isinstance(action_type, str):
            raise TypeError("Expected argument 'action_type' to be a str")
        pulumi.set(__self__, "action_type", action_type)
        if applications and not isinstance(applications, list):
            raise TypeError("Expected argument 'applications' to be a list")
        pulumi.set(__self__, "applications", applications)
        if audit_comment and not isinstance(audit_comment, str):
            raise TypeError("Expected argument 'audit_comment' to be a str")
        pulumi.set(__self__, "audit_comment", audit_comment)
        if category and not isinstance(category, dict):
            raise TypeError("Expected argument 'category' to be a dict")
        pulumi.set(__self__, "category", category)
        if decryption_rule_type and not isinstance(decryption_rule_type, str):
            raise TypeError("Expected argument 'decryption_rule_type' to be a str")
        pulumi.set(__self__, "decryption_rule_type", decryption_rule_type)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if destination and not isinstance(destination, dict):
            raise TypeError("Expected argument 'destination' to be a dict")
        pulumi.set(__self__, "destination", destination)
        if enable_logging and not isinstance(enable_logging, str):
            raise TypeError("Expected argument 'enable_logging' to be a str")
        pulumi.set(__self__, "enable_logging", enable_logging)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inbound_inspection_certificate and not isinstance(inbound_inspection_certificate, str):
            raise TypeError("Expected argument 'inbound_inspection_certificate' to be a str")
        pulumi.set(__self__, "inbound_inspection_certificate", inbound_inspection_certificate)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if negate_destination and not isinstance(negate_destination, str):
            raise TypeError("Expected argument 'negate_destination' to be a str")
        pulumi.set(__self__, "negate_destination", negate_destination)
        if negate_source and not isinstance(negate_source, str):
            raise TypeError("Expected argument 'negate_source' to be a str")
        pulumi.set(__self__, "negate_source", negate_source)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if protocol_port_list and not isinstance(protocol_port_list, list):
            raise TypeError("Expected argument 'protocol_port_list' to be a list")
        pulumi.set(__self__, "protocol_port_list", protocol_port_list)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rule_name and not isinstance(rule_name, str):
            raise TypeError("Expected argument 'rule_name' to be a str")
        pulumi.set(__self__, "rule_name", rule_name)
        if rule_state and not isinstance(rule_state, str):
            raise TypeError("Expected argument 'rule_state' to be a str")
        pulumi.set(__self__, "rule_state", rule_state)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="actionType")
    def action_type(self) -> Optional[str]:
        """
        rule action
        """
        return pulumi.get(self, "action_type")

    @property
    @pulumi.getter
    def applications(self) -> Optional[Sequence[str]]:
        """
        array of rule applications
        """
        return pulumi.get(self, "applications")

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[str]:
        """
        rule comment
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter
    def category(self) -> Optional['outputs.CategoryResponse']:
        """
        rule category
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="decryptionRuleType")
    def decryption_rule_type(self) -> Optional[str]:
        """
        enable or disable decryption
        """
        return pulumi.get(self, "decryption_rule_type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        rule description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def destination(self) -> Optional['outputs.DestinationAddrResponse']:
        """
        destination address
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="enableLogging")
    def enable_logging(self) -> Optional[str]:
        """
        enable or disable logging
        """
        return pulumi.get(self, "enable_logging")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        etag info
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inboundInspectionCertificate")
    def inbound_inspection_certificate(self) -> Optional[str]:
        """
        inbound Inspection Certificate
        """
        return pulumi.get(self, "inbound_inspection_certificate")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="negateDestination")
    def negate_destination(self) -> Optional[str]:
        """
        cidr should not be 'any'
        """
        return pulumi.get(self, "negate_destination")

    @property
    @pulumi.getter(name="negateSource")
    def negate_source(self) -> Optional[str]:
        """
        cidr should not be 'any'
        """
        return pulumi.get(self, "negate_source")

    @property
    @pulumi.getter
    def priority(self) -> int:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[str]:
        """
        any, application-default, TCP:number, UDP:number
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="protocolPortList")
    def protocol_port_list(self) -> Optional[Sequence[str]]:
        """
        prot port list
        """
        return pulumi.get(self, "protocol_port_list")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> str:
        """
        rule name
        """
        return pulumi.get(self, "rule_name")

    @property
    @pulumi.getter(name="ruleState")
    def rule_state(self) -> Optional[str]:
        """
        state of this rule
        """
        return pulumi.get(self, "rule_state")

    @property
    @pulumi.getter
    def source(self) -> Optional['outputs.SourceAddrResponse']:
        """
        source address
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TagInfoResponse']]:
        """
        tag for rule
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetPostRuleResult(GetPostRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPostRuleResult(
            action_type=self.action_type,
            applications=self.applications,
            audit_comment=self.audit_comment,
            category=self.category,
            decryption_rule_type=self.decryption_rule_type,
            description=self.description,
            destination=self.destination,
            enable_logging=self.enable_logging,
            etag=self.etag,
            id=self.id,
            inbound_inspection_certificate=self.inbound_inspection_certificate,
            name=self.name,
            negate_destination=self.negate_destination,
            negate_source=self.negate_source,
            priority=self.priority,
            protocol=self.protocol,
            protocol_port_list=self.protocol_port_list,
            provisioning_state=self.provisioning_state,
            rule_name=self.rule_name,
            rule_state=self.rule_state,
            source=self.source,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_post_rule(global_rulestack_name: Optional[str] = None,
                  priority: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPostRuleResult:
    """
    Get a PostRulesResource


    :param str global_rulestack_name: GlobalRulestack resource name
    :param str priority: Post Rule priority
    """
    __args__ = dict()
    __args__['globalRulestackName'] = global_rulestack_name
    __args__['priority'] = priority
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20220829preview:getPostRule', __args__, opts=opts, typ=GetPostRuleResult).value

    return AwaitableGetPostRuleResult(
        action_type=pulumi.get(__ret__, 'action_type'),
        applications=pulumi.get(__ret__, 'applications'),
        audit_comment=pulumi.get(__ret__, 'audit_comment'),
        category=pulumi.get(__ret__, 'category'),
        decryption_rule_type=pulumi.get(__ret__, 'decryption_rule_type'),
        description=pulumi.get(__ret__, 'description'),
        destination=pulumi.get(__ret__, 'destination'),
        enable_logging=pulumi.get(__ret__, 'enable_logging'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        inbound_inspection_certificate=pulumi.get(__ret__, 'inbound_inspection_certificate'),
        name=pulumi.get(__ret__, 'name'),
        negate_destination=pulumi.get(__ret__, 'negate_destination'),
        negate_source=pulumi.get(__ret__, 'negate_source'),
        priority=pulumi.get(__ret__, 'priority'),
        protocol=pulumi.get(__ret__, 'protocol'),
        protocol_port_list=pulumi.get(__ret__, 'protocol_port_list'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rule_name=pulumi.get(__ret__, 'rule_name'),
        rule_state=pulumi.get(__ret__, 'rule_state'),
        source=pulumi.get(__ret__, 'source'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_post_rule)
def get_post_rule_output(global_rulestack_name: Optional[pulumi.Input[str]] = None,
                         priority: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPostRuleResult]:
    """
    Get a PostRulesResource


    :param str global_rulestack_name: GlobalRulestack resource name
    :param str priority: Post Rule priority
    """
    ...
