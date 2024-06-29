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
    'GetOriginEndpointPolicyResult',
    'AwaitableGetOriginEndpointPolicyResult',
    'get_origin_endpoint_policy',
    'get_origin_endpoint_policy_output',
]

@pulumi.output_type
class GetOriginEndpointPolicyResult:
    def __init__(__self__, policy=None):
        if policy and not isinstance(policy, dict):
            raise TypeError("Expected argument 'policy' to be a dict")
        pulumi.set(__self__, "policy", policy)

    @property
    @pulumi.getter
    def policy(self) -> Optional[Any]:
        """
        The policy associated with the origin endpoint.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaPackageV2::OriginEndpointPolicy` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy")


class AwaitableGetOriginEndpointPolicyResult(GetOriginEndpointPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOriginEndpointPolicyResult(
            policy=self.policy)


def get_origin_endpoint_policy(channel_group_name: Optional[str] = None,
                               channel_name: Optional[str] = None,
                               origin_endpoint_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOriginEndpointPolicyResult:
    """
    <p>Represents a resource policy that allows or denies access to an origin endpoint.</p>


    :param str channel_group_name: The name of the channel group associated with the origin endpoint policy.
    :param str channel_name: The channel name associated with the origin endpoint policy.
    :param str origin_endpoint_name: The name of the origin endpoint associated with the origin endpoint policy.
    """
    __args__ = dict()
    __args__['channelGroupName'] = channel_group_name
    __args__['channelName'] = channel_name
    __args__['originEndpointName'] = origin_endpoint_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackagev2:getOriginEndpointPolicy', __args__, opts=opts, typ=GetOriginEndpointPolicyResult).value

    return AwaitableGetOriginEndpointPolicyResult(
        policy=pulumi.get(__ret__, 'policy'))


@_utilities.lift_output_func(get_origin_endpoint_policy)
def get_origin_endpoint_policy_output(channel_group_name: Optional[pulumi.Input[str]] = None,
                                      channel_name: Optional[pulumi.Input[str]] = None,
                                      origin_endpoint_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOriginEndpointPolicyResult]:
    """
    <p>Represents a resource policy that allows or denies access to an origin endpoint.</p>


    :param str channel_group_name: The name of the channel group associated with the origin endpoint policy.
    :param str channel_name: The channel name associated with the origin endpoint policy.
    :param str origin_endpoint_name: The name of the origin endpoint associated with the origin endpoint policy.
    """
    ...
