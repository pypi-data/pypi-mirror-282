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
    'GetPrefixListGlobalRulestackResult',
    'AwaitableGetPrefixListGlobalRulestackResult',
    'get_prefix_list_global_rulestack',
    'get_prefix_list_global_rulestack_output',
]

@pulumi.output_type
class GetPrefixListGlobalRulestackResult:
    """
    GlobalRulestack prefixList
    """
    def __init__(__self__, audit_comment=None, description=None, etag=None, id=None, name=None, prefix_list=None, provisioning_state=None, system_data=None, type=None):
        if audit_comment and not isinstance(audit_comment, str):
            raise TypeError("Expected argument 'audit_comment' to be a str")
        pulumi.set(__self__, "audit_comment", audit_comment)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if prefix_list and not isinstance(prefix_list, list):
            raise TypeError("Expected argument 'prefix_list' to be a list")
        pulumi.set(__self__, "prefix_list", prefix_list)
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
        prefix description
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
    @pulumi.getter(name="prefixList")
    def prefix_list(self) -> Sequence[str]:
        """
        prefix list
        """
        return pulumi.get(self, "prefix_list")

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


class AwaitableGetPrefixListGlobalRulestackResult(GetPrefixListGlobalRulestackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrefixListGlobalRulestackResult(
            audit_comment=self.audit_comment,
            description=self.description,
            etag=self.etag,
            id=self.id,
            name=self.name,
            prefix_list=self.prefix_list,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_prefix_list_global_rulestack(global_rulestack_name: Optional[str] = None,
                                     name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrefixListGlobalRulestackResult:
    """
    Get a PrefixListGlobalRulestackResource


    :param str global_rulestack_name: GlobalRulestack resource name
    :param str name: Local Rule priority
    """
    __args__ = dict()
    __args__['globalRulestackName'] = global_rulestack_name
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20220829preview:getPrefixListGlobalRulestack', __args__, opts=opts, typ=GetPrefixListGlobalRulestackResult).value

    return AwaitableGetPrefixListGlobalRulestackResult(
        audit_comment=pulumi.get(__ret__, 'audit_comment'),
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        prefix_list=pulumi.get(__ret__, 'prefix_list'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_prefix_list_global_rulestack)
def get_prefix_list_global_rulestack_output(global_rulestack_name: Optional[pulumi.Input[str]] = None,
                                            name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrefixListGlobalRulestackResult]:
    """
    Get a PrefixListGlobalRulestackResource


    :param str global_rulestack_name: GlobalRulestack resource name
    :param str name: Local Rule priority
    """
    ...
