# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetAccountAliasResult',
    'AwaitableGetAccountAliasResult',
    'get_account_alias',
    'get_account_alias_output',
]

@pulumi.output_type
class GetAccountAliasResult:
    def __init__(__self__, account_alias=None, account_alias_resource_id=None):
        if account_alias and not isinstance(account_alias, str):
            raise TypeError("Expected argument 'account_alias' to be a str")
        pulumi.set(__self__, "account_alias", account_alias)
        if account_alias_resource_id and not isinstance(account_alias_resource_id, str):
            raise TypeError("Expected argument 'account_alias_resource_id' to be a str")
        pulumi.set(__self__, "account_alias_resource_id", account_alias_resource_id)

    @property
    @pulumi.getter(name="accountAlias")
    def account_alias(self) -> Optional[str]:
        """
        An account alias associated with a customer's account.
        """
        return pulumi.get(self, "account_alias")

    @property
    @pulumi.getter(name="accountAliasResourceId")
    def account_alias_resource_id(self) -> Optional[str]:
        """
        Unique identifier representing an alias tied to an account
        """
        return pulumi.get(self, "account_alias_resource_id")


class AwaitableGetAccountAliasResult(GetAccountAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountAliasResult(
            account_alias=self.account_alias,
            account_alias_resource_id=self.account_alias_resource_id)


def get_account_alias(account_alias_resource_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountAliasResult:
    """
    An AWS Support App resource that creates, updates, reads, and deletes a customer's account alias.


    :param str account_alias_resource_id: Unique identifier representing an alias tied to an account
    """
    __args__ = dict()
    __args__['accountAliasResourceId'] = account_alias_resource_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:supportapp:getAccountAlias', __args__, opts=opts, typ=GetAccountAliasResult).value

    return AwaitableGetAccountAliasResult(
        account_alias=pulumi.get(__ret__, 'account_alias'),
        account_alias_resource_id=pulumi.get(__ret__, 'account_alias_resource_id'))


@_utilities.lift_output_func(get_account_alias)
def get_account_alias_output(account_alias_resource_id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountAliasResult]:
    """
    An AWS Support App resource that creates, updates, reads, and deletes a customer's account alias.


    :param str account_alias_resource_id: Unique identifier representing an alias tied to an account
    """
    ...
