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
    'GetChannelPolicyResult',
    'AwaitableGetChannelPolicyResult',
    'get_channel_policy',
    'get_channel_policy_output',
]

@pulumi.output_type
class GetChannelPolicyResult:
    def __init__(__self__, policy=None):
        if policy and not isinstance(policy, dict):
            raise TypeError("Expected argument 'policy' to be a dict")
        pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter
    def policy(self) -> Optional[Any]:
        """
        The policy associated with the channel.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaPackageV2::ChannelPolicy` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy")


class AwaitableGetChannelPolicyResult(GetChannelPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetChannelPolicyResult(
            policy=self.policy)


def get_channel_policy(channel_group_name: Optional[str] = None,
                       channel_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetChannelPolicyResult:
    """
    <p>Represents a resource-based policy that allows or denies access to a channel.</p>


    :param str channel_group_name: The name of the channel group associated with the channel policy.
    :param str channel_name: The name of the channel associated with the channel policy.
    """
    __args__ = dict()
    __args__['channelGroupName'] = channel_group_name
    __args__['channelName'] = channel_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackagev2:getChannelPolicy', __args__, opts=opts, typ=GetChannelPolicyResult).value

    return AwaitableGetChannelPolicyResult(
        policy=pulumi.get(__ret__, 'policy'))


@_utilities.lift_output_func(get_channel_policy)
def get_channel_policy_output(channel_group_name: Optional[pulumi.Input[str]] = None,
                              channel_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetChannelPolicyResult]:
    """
    <p>Represents a resource-based policy that allows or denies access to a channel.</p>


    :param str channel_group_name: The name of the channel group associated with the channel policy.
    :param str channel_name: The name of the channel associated with the channel policy.
    """
    ...
