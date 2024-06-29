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
    'ListAccountKeysResult',
    'AwaitableListAccountKeysResult',
    'list_account_keys',
    'list_account_keys_output',
]

@pulumi.output_type
class ListAccountKeysResult:
    """
    The Purview Account access keys.
    """
    def __init__(__self__, atlas_kafka_primary_endpoint=None, atlas_kafka_secondary_endpoint=None):
        if atlas_kafka_primary_endpoint and not isinstance(atlas_kafka_primary_endpoint, str):
            raise TypeError("Expected argument 'atlas_kafka_primary_endpoint' to be a str")
        pulumi.set(__self__, "atlas_kafka_primary_endpoint", atlas_kafka_primary_endpoint)
        if atlas_kafka_secondary_endpoint and not isinstance(atlas_kafka_secondary_endpoint, str):
            raise TypeError("Expected argument 'atlas_kafka_secondary_endpoint' to be a str")
        pulumi.set(__self__, "atlas_kafka_secondary_endpoint", atlas_kafka_secondary_endpoint)

    @property
    @pulumi.getter(name="atlasKafkaPrimaryEndpoint")
    def atlas_kafka_primary_endpoint(self) -> Optional[str]:
        """
        Gets or sets the primary connection string.
        """
        return pulumi.get(self, "atlas_kafka_primary_endpoint")

    @property
    @pulumi.getter(name="atlasKafkaSecondaryEndpoint")
    def atlas_kafka_secondary_endpoint(self) -> Optional[str]:
        """
        Gets or sets the secondary connection string.
        """
        return pulumi.get(self, "atlas_kafka_secondary_endpoint")


class AwaitableListAccountKeysResult(ListAccountKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAccountKeysResult(
            atlas_kafka_primary_endpoint=self.atlas_kafka_primary_endpoint,
            atlas_kafka_secondary_endpoint=self.atlas_kafka_secondary_endpoint)


def list_account_keys(account_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAccountKeysResult:
    """
    List the authorization keys associated with this account.


    :param str account_name: The name of the account.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:purview/v20240401preview:listAccountKeys', __args__, opts=opts, typ=ListAccountKeysResult).value

    return AwaitableListAccountKeysResult(
        atlas_kafka_primary_endpoint=pulumi.get(__ret__, 'atlas_kafka_primary_endpoint'),
        atlas_kafka_secondary_endpoint=pulumi.get(__ret__, 'atlas_kafka_secondary_endpoint'))


@_utilities.lift_output_func(list_account_keys)
def list_account_keys_output(account_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAccountKeysResult]:
    """
    List the authorization keys associated with this account.


    :param str account_name: The name of the account.
    :param str resource_group_name: The resource group name.
    """
    ...
