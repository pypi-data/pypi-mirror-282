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
    'GetManagementLockByScopeResult',
    'AwaitableGetManagementLockByScopeResult',
    'get_management_lock_by_scope',
    'get_management_lock_by_scope_output',
]

@pulumi.output_type
class GetManagementLockByScopeResult:
    """
    The lock information.
    """
    def __init__(__self__, id=None, level=None, name=None, notes=None, owners=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if level and not isinstance(level, str):
            raise TypeError("Expected argument 'level' to be a str")
        pulumi.set(__self__, "level", level)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if owners and not isinstance(owners, list):
            raise TypeError("Expected argument 'owners' to be a list")
        pulumi.set(__self__, "owners", owners)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID of the lock.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def level(self) -> str:
        """
        The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it.
        """
        return pulumi.get(self, "level")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the lock.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        """
        Notes about the lock. Maximum of 512 characters.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def owners(self) -> Optional[Sequence['outputs.ManagementLockOwnerResponse']]:
        """
        The owners of the lock.
        """
        return pulumi.get(self, "owners")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type of the lock - Microsoft.Authorization/locks.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagementLockByScopeResult(GetManagementLockByScopeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagementLockByScopeResult(
            id=self.id,
            level=self.level,
            name=self.name,
            notes=self.notes,
            owners=self.owners,
            system_data=self.system_data,
            type=self.type)


def get_management_lock_by_scope(lock_name: Optional[str] = None,
                                 scope: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagementLockByScopeResult:
    """
    Get a management lock by scope.


    :param str lock_name: The name of lock.
    :param str scope: The scope for the lock. 
    """
    __args__ = dict()
    __args__['lockName'] = lock_name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization/v20200501:getManagementLockByScope', __args__, opts=opts, typ=GetManagementLockByScopeResult).value

    return AwaitableGetManagementLockByScopeResult(
        id=pulumi.get(__ret__, 'id'),
        level=pulumi.get(__ret__, 'level'),
        name=pulumi.get(__ret__, 'name'),
        notes=pulumi.get(__ret__, 'notes'),
        owners=pulumi.get(__ret__, 'owners'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_management_lock_by_scope)
def get_management_lock_by_scope_output(lock_name: Optional[pulumi.Input[str]] = None,
                                        scope: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagementLockByScopeResult]:
    """
    Get a management lock by scope.


    :param str lock_name: The name of lock.
    :param str scope: The scope for the lock. 
    """
    ...
