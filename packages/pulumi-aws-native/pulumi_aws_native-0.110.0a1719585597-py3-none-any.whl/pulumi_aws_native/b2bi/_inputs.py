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
    'CapabilityConfigurationPropertiesArgs',
    'CapabilityEdiConfigurationArgs',
    'CapabilityEdiTypePropertiesArgs',
    'CapabilityS3LocationArgs',
    'CapabilityX12DetailsArgs',
    'TransformerEdiTypePropertiesArgs',
    'TransformerX12DetailsArgs',
]

@pulumi.input_type
class CapabilityConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 edi: pulumi.Input['CapabilityEdiConfigurationArgs']):
        pulumi.set(__self__, "edi", edi)

    @property
    @pulumi.getter
    def edi(self) -> pulumi.Input['CapabilityEdiConfigurationArgs']:
        return pulumi.get(self, "edi")

    @edi.setter
    def edi(self, value: pulumi.Input['CapabilityEdiConfigurationArgs']):
        pulumi.set(self, "edi", value)


@pulumi.input_type
class CapabilityEdiConfigurationArgs:
    def __init__(__self__, *,
                 input_location: pulumi.Input['CapabilityS3LocationArgs'],
                 output_location: pulumi.Input['CapabilityS3LocationArgs'],
                 transformer_id: pulumi.Input[str],
                 type: pulumi.Input['CapabilityEdiTypePropertiesArgs']):
        pulumi.set(__self__, "input_location", input_location)
        pulumi.set(__self__, "output_location", output_location)
        pulumi.set(__self__, "transformer_id", transformer_id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="inputLocation")
    def input_location(self) -> pulumi.Input['CapabilityS3LocationArgs']:
        return pulumi.get(self, "input_location")

    @input_location.setter
    def input_location(self, value: pulumi.Input['CapabilityS3LocationArgs']):
        pulumi.set(self, "input_location", value)

    @property
    @pulumi.getter(name="outputLocation")
    def output_location(self) -> pulumi.Input['CapabilityS3LocationArgs']:
        return pulumi.get(self, "output_location")

    @output_location.setter
    def output_location(self, value: pulumi.Input['CapabilityS3LocationArgs']):
        pulumi.set(self, "output_location", value)

    @property
    @pulumi.getter(name="transformerId")
    def transformer_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "transformer_id")

    @transformer_id.setter
    def transformer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "transformer_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['CapabilityEdiTypePropertiesArgs']:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['CapabilityEdiTypePropertiesArgs']):
        pulumi.set(self, "type", value)


@pulumi.input_type
class CapabilityEdiTypePropertiesArgs:
    def __init__(__self__, *,
                 x12_details: pulumi.Input['CapabilityX12DetailsArgs']):
        pulumi.set(__self__, "x12_details", x12_details)

    @property
    @pulumi.getter(name="x12Details")
    def x12_details(self) -> pulumi.Input['CapabilityX12DetailsArgs']:
        return pulumi.get(self, "x12_details")

    @x12_details.setter
    def x12_details(self, value: pulumi.Input['CapabilityX12DetailsArgs']):
        pulumi.set(self, "x12_details", value)


@pulumi.input_type
class CapabilityS3LocationArgs:
    def __init__(__self__, *,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None):
        if bucket_name is not None:
            pulumi.set(__self__, "bucket_name", bucket_name)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


@pulumi.input_type
class CapabilityX12DetailsArgs:
    def __init__(__self__, *,
                 transaction_set: Optional[pulumi.Input['CapabilityX12TransactionSet']] = None,
                 version: Optional[pulumi.Input['CapabilityX12Version']] = None):
        if transaction_set is not None:
            pulumi.set(__self__, "transaction_set", transaction_set)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="transactionSet")
    def transaction_set(self) -> Optional[pulumi.Input['CapabilityX12TransactionSet']]:
        return pulumi.get(self, "transaction_set")

    @transaction_set.setter
    def transaction_set(self, value: Optional[pulumi.Input['CapabilityX12TransactionSet']]):
        pulumi.set(self, "transaction_set", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input['CapabilityX12Version']]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input['CapabilityX12Version']]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class TransformerEdiTypePropertiesArgs:
    def __init__(__self__, *,
                 x12_details: pulumi.Input['TransformerX12DetailsArgs']):
        pulumi.set(__self__, "x12_details", x12_details)

    @property
    @pulumi.getter(name="x12Details")
    def x12_details(self) -> pulumi.Input['TransformerX12DetailsArgs']:
        return pulumi.get(self, "x12_details")

    @x12_details.setter
    def x12_details(self, value: pulumi.Input['TransformerX12DetailsArgs']):
        pulumi.set(self, "x12_details", value)


@pulumi.input_type
class TransformerX12DetailsArgs:
    def __init__(__self__, *,
                 transaction_set: Optional[pulumi.Input['TransformerX12TransactionSet']] = None,
                 version: Optional[pulumi.Input['TransformerX12Version']] = None):
        if transaction_set is not None:
            pulumi.set(__self__, "transaction_set", transaction_set)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="transactionSet")
    def transaction_set(self) -> Optional[pulumi.Input['TransformerX12TransactionSet']]:
        return pulumi.get(self, "transaction_set")

    @transaction_set.setter
    def transaction_set(self, value: Optional[pulumi.Input['TransformerX12TransactionSet']]):
        pulumi.set(self, "transaction_set", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input['TransformerX12Version']]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input['TransformerX12Version']]):
        pulumi.set(self, "version", value)


