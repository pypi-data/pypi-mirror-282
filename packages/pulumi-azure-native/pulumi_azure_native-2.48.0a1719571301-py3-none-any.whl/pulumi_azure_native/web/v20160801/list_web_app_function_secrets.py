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
    'ListWebAppFunctionSecretsResult',
    'AwaitableListWebAppFunctionSecretsResult',
    'list_web_app_function_secrets',
    'list_web_app_function_secrets_output',
]

@pulumi.output_type
class ListWebAppFunctionSecretsResult:
    """
    Function secrets.
    """
    def __init__(__self__, id=None, key=None, kind=None, name=None, trigger_url=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if trigger_url and not isinstance(trigger_url, str):
            raise TypeError("Expected argument 'trigger_url' to be a str")
        pulumi.set(__self__, "trigger_url", trigger_url)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        Secret key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[str]:
        """
        Trigger URL.
        """
        return pulumi.get(self, "trigger_url")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableListWebAppFunctionSecretsResult(ListWebAppFunctionSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebAppFunctionSecretsResult(
            id=self.id,
            key=self.key,
            kind=self.kind,
            name=self.name,
            trigger_url=self.trigger_url,
            type=self.type)


def list_web_app_function_secrets(function_name: Optional[str] = None,
                                  name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebAppFunctionSecretsResult:
    """
    Get function secrets for a function in a web site, or a deployment slot.


    :param str function_name: Function name.
    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['functionName'] = function_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20160801:listWebAppFunctionSecrets', __args__, opts=opts, typ=ListWebAppFunctionSecretsResult).value

    return AwaitableListWebAppFunctionSecretsResult(
        id=pulumi.get(__ret__, 'id'),
        key=pulumi.get(__ret__, 'key'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        trigger_url=pulumi.get(__ret__, 'trigger_url'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(list_web_app_function_secrets)
def list_web_app_function_secrets_output(function_name: Optional[pulumi.Input[str]] = None,
                                         name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWebAppFunctionSecretsResult]:
    """
    Get function secrets for a function in a web site, or a deployment slot.


    :param str function_name: Function name.
    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
