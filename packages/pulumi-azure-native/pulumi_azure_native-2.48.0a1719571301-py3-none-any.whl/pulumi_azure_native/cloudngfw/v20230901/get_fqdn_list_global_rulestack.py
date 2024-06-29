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
    'GetFqdnListGlobalRulestackResult',
    'AwaitableGetFqdnListGlobalRulestackResult',
    'get_fqdn_list_global_rulestack',
    'get_fqdn_list_global_rulestack_output',
]

@pulumi.output_type
class GetFqdnListGlobalRulestackResult:
    """
    GlobalRulestack fqdnList
    """
    def __init__(__self__, audit_comment=None, description=None, etag=None, fqdn_list=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if audit_comment and not isinstance(audit_comment, str):
            raise TypeError("Expected argument 'audit_comment' to be a str")
        pulumi.set(__self__, "audit_comment", audit_comment)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if fqdn_list and not isinstance(fqdn_list, list):
            raise TypeError("Expected argument 'fqdn_list' to be a list")
        pulumi.set(__self__, "fqdn_list", fqdn_list)
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
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[str]:
        """
        comment for this object
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        fqdn object description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        etag info
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="fqdnList")
    def fqdn_list(self) -> Sequence[str]:
        """
        fqdn list
        """
        return pulumi.get(self, "fqdn_list")

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
        Provisioning state of the resource.
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


class AwaitableGetFqdnListGlobalRulestackResult(GetFqdnListGlobalRulestackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFqdnListGlobalRulestackResult(
            audit_comment=self.audit_comment,
            description=self.description,
            etag=self.etag,
            fqdn_list=self.fqdn_list,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_fqdn_list_global_rulestack(global_rulestack_name: Optional[str] = None,
                                   name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFqdnListGlobalRulestackResult:
    """
    Get a FqdnListGlobalRulestackResource


    :param str global_rulestack_name: GlobalRulestack resource name
    :param str name: fqdn list name
    """
    __args__ = dict()
    __args__['globalRulestackName'] = global_rulestack_name
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20230901:getFqdnListGlobalRulestack', __args__, opts=opts, typ=GetFqdnListGlobalRulestackResult).value

    return AwaitableGetFqdnListGlobalRulestackResult(
        audit_comment=pulumi.get(__ret__, 'audit_comment'),
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        fqdn_list=pulumi.get(__ret__, 'fqdn_list'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_fqdn_list_global_rulestack)
def get_fqdn_list_global_rulestack_output(global_rulestack_name: Optional[pulumi.Input[str]] = None,
                                          name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFqdnListGlobalRulestackResult]:
    """
    Get a FqdnListGlobalRulestackResource


    :param str global_rulestack_name: GlobalRulestack resource name
    :param str name: fqdn list name
    """
    ...
