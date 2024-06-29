# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs

__all__ = [
    'GetTransitGatewayConnectResult',
    'AwaitableGetTransitGatewayConnectResult',
    'get_transit_gateway_connect',
    'get_transit_gateway_connect_output',
]

@pulumi.output_type
class GetTransitGatewayConnectResult:
    def __init__(__self__, creation_time=None, state=None, tags=None, transit_gateway_attachment_id=None, transit_gateway_id=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if transit_gateway_attachment_id and not isinstance(transit_gateway_attachment_id, str):
            raise TypeError("Expected argument 'transit_gateway_attachment_id' to be a str")
        pulumi.set(__self__, "transit_gateway_attachment_id", transit_gateway_attachment_id)
        if transit_gateway_id and not isinstance(transit_gateway_id, str):
            raise TypeError("Expected argument 'transit_gateway_id' to be a str")
        pulumi.set(__self__, "transit_gateway_id", transit_gateway_id)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        The creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of the attachment.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags for the attachment.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transitGatewayAttachmentId")
    def transit_gateway_attachment_id(self) -> Optional[str]:
        """
        The ID of the Connect attachment.
        """
        return pulumi.get(self, "transit_gateway_attachment_id")

    @property
    @pulumi.getter(name="transitGatewayId")
    def transit_gateway_id(self) -> Optional[str]:
        """
        The ID of the transit gateway.
        """
        return pulumi.get(self, "transit_gateway_id")


class AwaitableGetTransitGatewayConnectResult(GetTransitGatewayConnectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransitGatewayConnectResult(
            creation_time=self.creation_time,
            state=self.state,
            tags=self.tags,
            transit_gateway_attachment_id=self.transit_gateway_attachment_id,
            transit_gateway_id=self.transit_gateway_id)


def get_transit_gateway_connect(transit_gateway_attachment_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransitGatewayConnectResult:
    """
    The AWS::EC2::TransitGatewayConnect type


    :param str transit_gateway_attachment_id: The ID of the Connect attachment.
    """
    __args__ = dict()
    __args__['transitGatewayAttachmentId'] = transit_gateway_attachment_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getTransitGatewayConnect', __args__, opts=opts, typ=GetTransitGatewayConnectResult).value

    return AwaitableGetTransitGatewayConnectResult(
        creation_time=pulumi.get(__ret__, 'creation_time'),
        state=pulumi.get(__ret__, 'state'),
        tags=pulumi.get(__ret__, 'tags'),
        transit_gateway_attachment_id=pulumi.get(__ret__, 'transit_gateway_attachment_id'),
        transit_gateway_id=pulumi.get(__ret__, 'transit_gateway_id'))


@_utilities.lift_output_func(get_transit_gateway_connect)
def get_transit_gateway_connect_output(transit_gateway_attachment_id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransitGatewayConnectResult]:
    """
    The AWS::EC2::TransitGatewayConnect type


    :param str transit_gateway_attachment_id: The ID of the Connect attachment.
    """
    ...
