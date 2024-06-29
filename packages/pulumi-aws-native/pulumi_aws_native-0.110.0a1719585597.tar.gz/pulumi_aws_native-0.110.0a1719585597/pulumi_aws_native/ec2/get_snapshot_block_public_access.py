# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'GetSnapshotBlockPublicAccessResult',
    'AwaitableGetSnapshotBlockPublicAccessResult',
    'get_snapshot_block_public_access',
    'get_snapshot_block_public_access_output',
]

@pulumi.output_type
class GetSnapshotBlockPublicAccessResult:
    def __init__(__self__, account_id=None, state=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        """
        The identifier for the specified AWS account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def state(self) -> Optional['SnapshotBlockPublicAccessState']:
        """
        The state of EBS Snapshot Block Public Access.
        """
        return pulumi.get(self, "state")


class AwaitableGetSnapshotBlockPublicAccessResult(GetSnapshotBlockPublicAccessResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotBlockPublicAccessResult(
            account_id=self.account_id,
            state=self.state)


def get_snapshot_block_public_access(account_id: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotBlockPublicAccessResult:
    """
    Resource Type definition for AWS::EC2::SnapshotBlockPublicAccess


    :param str account_id: The identifier for the specified AWS account.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getSnapshotBlockPublicAccess', __args__, opts=opts, typ=GetSnapshotBlockPublicAccessResult).value

    return AwaitableGetSnapshotBlockPublicAccessResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        state=pulumi.get(__ret__, 'state'))


@_utilities.lift_output_func(get_snapshot_block_public_access)
def get_snapshot_block_public_access_output(account_id: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSnapshotBlockPublicAccessResult]:
    """
    Resource Type definition for AWS::EC2::SnapshotBlockPublicAccess


    :param str account_id: The identifier for the specified AWS account.
    """
    ...
