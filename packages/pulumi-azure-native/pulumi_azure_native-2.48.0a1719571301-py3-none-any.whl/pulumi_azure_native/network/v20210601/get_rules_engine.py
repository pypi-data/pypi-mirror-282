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
    'GetRulesEngineResult',
    'AwaitableGetRulesEngineResult',
    'get_rules_engine',
    'get_rules_engine_output',
]

@pulumi.output_type
class GetRulesEngineResult:
    """
    A rules engine configuration containing a list of rules that will run to modify the runtime behavior of the request and response.
    """
    def __init__(__self__, id=None, name=None, resource_state=None, rules=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
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
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        Resource status.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.RulesEngineRuleResponse']]:
        """
        A list of rules that define a particular Rules Engine Configuration.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetRulesEngineResult(GetRulesEngineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRulesEngineResult(
            id=self.id,
            name=self.name,
            resource_state=self.resource_state,
            rules=self.rules,
            type=self.type)


def get_rules_engine(front_door_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     rules_engine_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRulesEngineResult:
    """
    Gets a Rules Engine Configuration with the specified name within the specified Front Door.


    :param str front_door_name: Name of the Front Door which is globally unique.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str rules_engine_name: Name of the Rules Engine which is unique within the Front Door.
    """
    __args__ = dict()
    __args__['frontDoorName'] = front_door_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['rulesEngineName'] = rules_engine_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20210601:getRulesEngine', __args__, opts=opts, typ=GetRulesEngineResult).value

    return AwaitableGetRulesEngineResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        resource_state=pulumi.get(__ret__, 'resource_state'),
        rules=pulumi.get(__ret__, 'rules'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_rules_engine)
def get_rules_engine_output(front_door_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            rules_engine_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRulesEngineResult]:
    """
    Gets a Rules Engine Configuration with the specified name within the specified Front Door.


    :param str front_door_name: Name of the Front Door which is globally unique.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str rules_engine_name: Name of the Rules Engine which is unique within the Front Door.
    """
    ...
