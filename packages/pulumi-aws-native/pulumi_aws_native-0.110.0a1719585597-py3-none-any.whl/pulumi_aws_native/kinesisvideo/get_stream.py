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
    'GetStreamResult',
    'AwaitableGetStreamResult',
    'get_stream',
    'get_stream_output',
]

@pulumi.output_type
class GetStreamResult:
    def __init__(__self__, arn=None, data_retention_in_hours=None, device_name=None, kms_key_id=None, media_type=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if data_retention_in_hours and not isinstance(data_retention_in_hours, int):
            raise TypeError("Expected argument 'data_retention_in_hours' to be a int")
        pulumi.set(__self__, "data_retention_in_hours", data_retention_in_hours)
        if device_name and not isinstance(device_name, str):
            raise TypeError("Expected argument 'device_name' to be a str")
        pulumi.set(__self__, "device_name", device_name)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if media_type and not isinstance(media_type, str):
            raise TypeError("Expected argument 'media_type' to be a str")
        pulumi.set(__self__, "media_type", media_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the Kinesis Video stream.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataRetentionInHours")
    def data_retention_in_hours(self) -> Optional[int]:
        """
        The number of hours till which Kinesis Video will retain the data in the stream
        """
        return pulumi.get(self, "data_retention_in_hours")

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> Optional[str]:
        """
        The name of the device that is writing to the stream.
        """
        return pulumi.get(self, "device_name")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> Optional[str]:
        """
        The media type of the stream. Consumers of the stream can use this information when processing the stream.
        """
        return pulumi.get(self, "media_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs associated with the Kinesis Video Stream.
        """
        return pulumi.get(self, "tags")


class AwaitableGetStreamResult(GetStreamResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamResult(
            arn=self.arn,
            data_retention_in_hours=self.data_retention_in_hours,
            device_name=self.device_name,
            kms_key_id=self.kms_key_id,
            media_type=self.media_type,
            tags=self.tags)


def get_stream(name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamResult:
    """
    Resource Type Definition for AWS::KinesisVideo::Stream


    :param str name: The name of the Kinesis Video stream.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:kinesisvideo:getStream', __args__, opts=opts, typ=GetStreamResult).value

    return AwaitableGetStreamResult(
        arn=pulumi.get(__ret__, 'arn'),
        data_retention_in_hours=pulumi.get(__ret__, 'data_retention_in_hours'),
        device_name=pulumi.get(__ret__, 'device_name'),
        kms_key_id=pulumi.get(__ret__, 'kms_key_id'),
        media_type=pulumi.get(__ret__, 'media_type'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_stream)
def get_stream_output(name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStreamResult]:
    """
    Resource Type Definition for AWS::KinesisVideo::Stream


    :param str name: The name of the Kinesis Video stream.
    """
    ...
