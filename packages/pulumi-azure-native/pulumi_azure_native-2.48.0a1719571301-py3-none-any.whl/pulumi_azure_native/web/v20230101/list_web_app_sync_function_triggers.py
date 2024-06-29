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
    'ListWebAppSyncFunctionTriggersResult',
    'AwaitableListWebAppSyncFunctionTriggersResult',
    'list_web_app_sync_function_triggers',
    'list_web_app_sync_function_triggers_output',
]

@pulumi.output_type
class ListWebAppSyncFunctionTriggersResult:
    """
    Function secrets.
    """
    def __init__(__self__, key=None, trigger_url=None):
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if trigger_url and not isinstance(trigger_url, str):
            raise TypeError("Expected argument 'trigger_url' to be a str")
        pulumi.set(__self__, "trigger_url", trigger_url)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        Secret key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[str]:
        """
        Trigger URL.
        """
        return pulumi.get(self, "trigger_url")


class AwaitableListWebAppSyncFunctionTriggersResult(ListWebAppSyncFunctionTriggersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebAppSyncFunctionTriggersResult(
            key=self.key,
            trigger_url=self.trigger_url)


def list_web_app_sync_function_triggers(name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebAppSyncFunctionTriggersResult:
    """
    Description for This is to allow calling via powershell and ARM template.


    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20230101:listWebAppSyncFunctionTriggers', __args__, opts=opts, typ=ListWebAppSyncFunctionTriggersResult).value

    return AwaitableListWebAppSyncFunctionTriggersResult(
        key=pulumi.get(__ret__, 'key'),
        trigger_url=pulumi.get(__ret__, 'trigger_url'))


@_utilities.lift_output_func(list_web_app_sync_function_triggers)
def list_web_app_sync_function_triggers_output(name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWebAppSyncFunctionTriggersResult]:
    """
    Description for This is to allow calling via powershell and ARM template.


    :param str name: Name of the app.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
