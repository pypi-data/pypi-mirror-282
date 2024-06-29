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
    'GetNetworkProfileResult',
    'AwaitableGetNetworkProfileResult',
    'get_network_profile',
    'get_network_profile_output',
]

@pulumi.output_type
class GetNetworkProfileResult:
    def __init__(__self__, arn=None, description=None, downlink_bandwidth_bits=None, downlink_delay_ms=None, downlink_jitter_ms=None, downlink_loss_percent=None, name=None, tags=None, uplink_bandwidth_bits=None, uplink_delay_ms=None, uplink_jitter_ms=None, uplink_loss_percent=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if downlink_bandwidth_bits and not isinstance(downlink_bandwidth_bits, int):
            raise TypeError("Expected argument 'downlink_bandwidth_bits' to be a int")
        pulumi.set(__self__, "downlink_bandwidth_bits", downlink_bandwidth_bits)
        if downlink_delay_ms and not isinstance(downlink_delay_ms, int):
            raise TypeError("Expected argument 'downlink_delay_ms' to be a int")
        pulumi.set(__self__, "downlink_delay_ms", downlink_delay_ms)
        if downlink_jitter_ms and not isinstance(downlink_jitter_ms, int):
            raise TypeError("Expected argument 'downlink_jitter_ms' to be a int")
        pulumi.set(__self__, "downlink_jitter_ms", downlink_jitter_ms)
        if downlink_loss_percent and not isinstance(downlink_loss_percent, int):
            raise TypeError("Expected argument 'downlink_loss_percent' to be a int")
        pulumi.set(__self__, "downlink_loss_percent", downlink_loss_percent)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if uplink_bandwidth_bits and not isinstance(uplink_bandwidth_bits, int):
            raise TypeError("Expected argument 'uplink_bandwidth_bits' to be a int")
        pulumi.set(__self__, "uplink_bandwidth_bits", uplink_bandwidth_bits)
        if uplink_delay_ms and not isinstance(uplink_delay_ms, int):
            raise TypeError("Expected argument 'uplink_delay_ms' to be a int")
        pulumi.set(__self__, "uplink_delay_ms", uplink_delay_ms)
        if uplink_jitter_ms and not isinstance(uplink_jitter_ms, int):
            raise TypeError("Expected argument 'uplink_jitter_ms' to be a int")
        pulumi.set(__self__, "uplink_jitter_ms", uplink_jitter_ms)
        if uplink_loss_percent and not isinstance(uplink_loss_percent, int):
            raise TypeError("Expected argument 'uplink_loss_percent' to be a int")
        pulumi.set(__self__, "uplink_loss_percent", uplink_loss_percent)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the network profile. See [Amazon resource names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference guide* .
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the network profile.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="downlinkBandwidthBits")
    def downlink_bandwidth_bits(self) -> Optional[int]:
        """
        The data throughput rate in bits per second, as an integer from 0 to 104857600.
        """
        return pulumi.get(self, "downlink_bandwidth_bits")

    @property
    @pulumi.getter(name="downlinkDelayMs")
    def downlink_delay_ms(self) -> Optional[int]:
        """
        Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        """
        return pulumi.get(self, "downlink_delay_ms")

    @property
    @pulumi.getter(name="downlinkJitterMs")
    def downlink_jitter_ms(self) -> Optional[int]:
        """
        Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        """
        return pulumi.get(self, "downlink_jitter_ms")

    @property
    @pulumi.getter(name="downlinkLossPercent")
    def downlink_loss_percent(self) -> Optional[int]:
        """
        Proportion of received packets that fail to arrive from 0 to 100 percent.
        """
        return pulumi.get(self, "downlink_loss_percent")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the network profile.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *guide* .
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="uplinkBandwidthBits")
    def uplink_bandwidth_bits(self) -> Optional[int]:
        """
        The data throughput rate in bits per second, as an integer from 0 to 104857600.
        """
        return pulumi.get(self, "uplink_bandwidth_bits")

    @property
    @pulumi.getter(name="uplinkDelayMs")
    def uplink_delay_ms(self) -> Optional[int]:
        """
        Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.
        """
        return pulumi.get(self, "uplink_delay_ms")

    @property
    @pulumi.getter(name="uplinkJitterMs")
    def uplink_jitter_ms(self) -> Optional[int]:
        """
        Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.
        """
        return pulumi.get(self, "uplink_jitter_ms")

    @property
    @pulumi.getter(name="uplinkLossPercent")
    def uplink_loss_percent(self) -> Optional[int]:
        """
        Proportion of transmitted packets that fail to arrive from 0 to 100 percent.
        """
        return pulumi.get(self, "uplink_loss_percent")


class AwaitableGetNetworkProfileResult(GetNetworkProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkProfileResult(
            arn=self.arn,
            description=self.description,
            downlink_bandwidth_bits=self.downlink_bandwidth_bits,
            downlink_delay_ms=self.downlink_delay_ms,
            downlink_jitter_ms=self.downlink_jitter_ms,
            downlink_loss_percent=self.downlink_loss_percent,
            name=self.name,
            tags=self.tags,
            uplink_bandwidth_bits=self.uplink_bandwidth_bits,
            uplink_delay_ms=self.uplink_delay_ms,
            uplink_jitter_ms=self.uplink_jitter_ms,
            uplink_loss_percent=self.uplink_loss_percent)


def get_network_profile(arn: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkProfileResult:
    """
    AWS::DeviceFarm::NetworkProfile creates a new DF Network Profile


    :param str arn: The Amazon Resource Name (ARN) of the network profile. See [Amazon resource names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference guide* .
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:devicefarm:getNetworkProfile', __args__, opts=opts, typ=GetNetworkProfileResult).value

    return AwaitableGetNetworkProfileResult(
        arn=pulumi.get(__ret__, 'arn'),
        description=pulumi.get(__ret__, 'description'),
        downlink_bandwidth_bits=pulumi.get(__ret__, 'downlink_bandwidth_bits'),
        downlink_delay_ms=pulumi.get(__ret__, 'downlink_delay_ms'),
        downlink_jitter_ms=pulumi.get(__ret__, 'downlink_jitter_ms'),
        downlink_loss_percent=pulumi.get(__ret__, 'downlink_loss_percent'),
        name=pulumi.get(__ret__, 'name'),
        tags=pulumi.get(__ret__, 'tags'),
        uplink_bandwidth_bits=pulumi.get(__ret__, 'uplink_bandwidth_bits'),
        uplink_delay_ms=pulumi.get(__ret__, 'uplink_delay_ms'),
        uplink_jitter_ms=pulumi.get(__ret__, 'uplink_jitter_ms'),
        uplink_loss_percent=pulumi.get(__ret__, 'uplink_loss_percent'))


@_utilities.lift_output_func(get_network_profile)
def get_network_profile_output(arn: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkProfileResult]:
    """
    AWS::DeviceFarm::NetworkProfile creates a new DF Network Profile


    :param str arn: The Amazon Resource Name (ARN) of the network profile. See [Amazon resource names](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference guide* .
    """
    ...
