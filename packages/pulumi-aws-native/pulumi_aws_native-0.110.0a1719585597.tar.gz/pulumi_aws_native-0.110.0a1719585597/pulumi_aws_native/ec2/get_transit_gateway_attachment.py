# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from .. import outputs as _root_outputs

__all__ = [
    'GetTransitGatewayAttachmentResult',
    'AwaitableGetTransitGatewayAttachmentResult',
    'get_transit_gateway_attachment',
    'get_transit_gateway_attachment_output',
]

@pulumi.output_type
class GetTransitGatewayAttachmentResult:
    def __init__(__self__, id=None, options=None, subnet_ids=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if options and not isinstance(options, dict):
            raise TypeError("Expected argument 'options' to be a dict")
        pulumi.set(__self__, "options", options)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the attachment.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def options(self) -> Optional['outputs.OptionsProperties']:
        """
        The options for the transit gateway vpc attachment.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Optional[Sequence[str]]:
        """
        The IDs of one or more subnets. You can specify only one subnet per Availability Zone. You must specify at least one subnet, but we recommend that you specify two subnets for better availability. The transit gateway uses one IP address from each specified subnet.
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags for the attachment.
        """
        return pulumi.get(self, "tags")


class AwaitableGetTransitGatewayAttachmentResult(GetTransitGatewayAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransitGatewayAttachmentResult(
            id=self.id,
            options=self.options,
            subnet_ids=self.subnet_ids,
            tags=self.tags)


def get_transit_gateway_attachment(id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransitGatewayAttachmentResult:
    """
    Resource Type definition for AWS::EC2::TransitGatewayAttachment


    :param str id: The ID of the attachment.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getTransitGatewayAttachment', __args__, opts=opts, typ=GetTransitGatewayAttachmentResult).value

    return AwaitableGetTransitGatewayAttachmentResult(
        id=pulumi.get(__ret__, 'id'),
        options=pulumi.get(__ret__, 'options'),
        subnet_ids=pulumi.get(__ret__, 'subnet_ids'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_transit_gateway_attachment)
def get_transit_gateway_attachment_output(id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransitGatewayAttachmentResult]:
    """
    Resource Type definition for AWS::EC2::TransitGatewayAttachment


    :param str id: The ID of the attachment.
    """
    ...
