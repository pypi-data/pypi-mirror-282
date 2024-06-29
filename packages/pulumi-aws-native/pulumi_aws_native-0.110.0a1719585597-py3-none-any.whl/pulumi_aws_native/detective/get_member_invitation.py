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
    'GetMemberInvitationResult',
    'AwaitableGetMemberInvitationResult',
    'get_member_invitation',
    'get_member_invitation_output',
]

@pulumi.output_type
class GetMemberInvitationResult:
    def __init__(__self__, member_email_address=None):
        if member_email_address and not isinstance(member_email_address, str):
            raise TypeError("Expected argument 'member_email_address' to be a str")
        pulumi.set(__self__, "member_email_address", member_email_address)

    @property
    @pulumi.getter(name="memberEmailAddress")
    def member_email_address(self) -> Optional[str]:
        """
        The root email address for the account to be invited, for validation. Updating this field has no effect.
        """
        return pulumi.get(self, "member_email_address")


class AwaitableGetMemberInvitationResult(GetMemberInvitationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMemberInvitationResult(
            member_email_address=self.member_email_address)


def get_member_invitation(graph_arn: Optional[str] = None,
                          member_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMemberInvitationResult:
    """
    Resource schema for AWS::Detective::MemberInvitation


    :param str graph_arn: The ARN of the graph to which the member account will be invited
    :param str member_id: The AWS account ID to be invited to join the graph as a member
    """
    __args__ = dict()
    __args__['graphArn'] = graph_arn
    __args__['memberId'] = member_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:detective:getMemberInvitation', __args__, opts=opts, typ=GetMemberInvitationResult).value

    return AwaitableGetMemberInvitationResult(
        member_email_address=pulumi.get(__ret__, 'member_email_address'))


@_utilities.lift_output_func(get_member_invitation)
def get_member_invitation_output(graph_arn: Optional[pulumi.Input[str]] = None,
                                 member_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMemberInvitationResult]:
    """
    Resource schema for AWS::Detective::MemberInvitation


    :param str graph_arn: The ARN of the graph to which the member account will be invited
    :param str member_id: The AWS account ID to be invited to join the graph as a member
    """
    ...
