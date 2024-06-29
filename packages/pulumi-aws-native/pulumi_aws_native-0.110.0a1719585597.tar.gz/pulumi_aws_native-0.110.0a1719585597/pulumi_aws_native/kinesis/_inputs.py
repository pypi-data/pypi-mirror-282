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
    'StreamEncryptionArgs',
    'StreamModeDetailsArgs',
]

@pulumi.input_type
class StreamEncryptionArgs:
    def __init__(__self__, *,
                 encryption_type: pulumi.Input['StreamEncryptionEncryptionType'],
                 key_id: pulumi.Input[str]):
        """
        When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream. Removing this property from your stack template and updating your stack disables encryption.
        :param pulumi.Input['StreamEncryptionEncryptionType'] encryption_type: The encryption type to use. The only valid value is KMS. 
        :param pulumi.Input[str] key_id: The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis.
        """
        pulumi.set(__self__, "encryption_type", encryption_type)
        pulumi.set(__self__, "key_id", key_id)

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> pulumi.Input['StreamEncryptionEncryptionType']:
        """
        The encryption type to use. The only valid value is KMS. 
        """
        return pulumi.get(self, "encryption_type")

    @encryption_type.setter
    def encryption_type(self, value: pulumi.Input['StreamEncryptionEncryptionType']):
        pulumi.set(self, "encryption_type", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[str]:
        """
        The GUID for the customer-managed AWS KMS key to use for encryption. This value can be a globally unique identifier, a fully specified Amazon Resource Name (ARN) to either an alias or a key, or an alias name prefixed by "alias/".You can also use a master key owned by Kinesis Data Streams by specifying the alias aws/kinesis.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_id", value)


@pulumi.input_type
class StreamModeDetailsArgs:
    def __init__(__self__, *,
                 stream_mode: pulumi.Input['StreamModeDetailsStreamMode']):
        """
        When specified, enables or updates the mode of stream. Default is PROVISIONED.
        :param pulumi.Input['StreamModeDetailsStreamMode'] stream_mode: The mode of the stream
        """
        pulumi.set(__self__, "stream_mode", stream_mode)

    @property
    @pulumi.getter(name="streamMode")
    def stream_mode(self) -> pulumi.Input['StreamModeDetailsStreamMode']:
        """
        The mode of the stream
        """
        return pulumi.get(self, "stream_mode")

    @stream_mode.setter
    def stream_mode(self, value: pulumi.Input['StreamModeDetailsStreamMode']):
        pulumi.set(self, "stream_mode", value)


