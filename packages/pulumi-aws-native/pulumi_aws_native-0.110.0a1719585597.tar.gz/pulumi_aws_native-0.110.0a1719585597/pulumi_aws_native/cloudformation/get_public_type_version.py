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
    'GetPublicTypeVersionResult',
    'AwaitableGetPublicTypeVersionResult',
    'get_public_type_version',
    'get_public_type_version_output',
]

@pulumi.output_type
class GetPublicTypeVersionResult:
    def __init__(__self__, public_type_arn=None, publisher_id=None, type_version_arn=None):
        if public_type_arn and not isinstance(public_type_arn, str):
            raise TypeError("Expected argument 'public_type_arn' to be a str")
        pulumi.set(__self__, "public_type_arn", public_type_arn)
        if publisher_id and not isinstance(publisher_id, str):
            raise TypeError("Expected argument 'publisher_id' to be a str")
        pulumi.set(__self__, "publisher_id", publisher_id)
        if type_version_arn and not isinstance(type_version_arn, str):
            raise TypeError("Expected argument 'type_version_arn' to be a str")
        pulumi.set(__self__, "type_version_arn", type_version_arn)

    @property
    @pulumi.getter(name="publicTypeArn")
    def public_type_arn(self) -> Optional[str]:
        """
        The Amazon Resource Number (ARN) assigned to the public extension upon publication
        """
        return pulumi.get(self, "public_type_arn")

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> Optional[str]:
        """
        The publisher id assigned by CloudFormation for publishing in this region.
        """
        return pulumi.get(self, "publisher_id")

    @property
    @pulumi.getter(name="typeVersionArn")
    def type_version_arn(self) -> Optional[str]:
        """
        The Amazon Resource Number (ARN) of the extension with the versionId.
        """
        return pulumi.get(self, "type_version_arn")


class AwaitableGetPublicTypeVersionResult(GetPublicTypeVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPublicTypeVersionResult(
            public_type_arn=self.public_type_arn,
            publisher_id=self.publisher_id,
            type_version_arn=self.type_version_arn)


def get_public_type_version(public_type_arn: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPublicTypeVersionResult:
    """
    Test and Publish a resource that has been registered in the CloudFormation Registry.


    :param str public_type_arn: The Amazon Resource Number (ARN) assigned to the public extension upon publication
    """
    __args__ = dict()
    __args__['publicTypeArn'] = public_type_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:cloudformation:getPublicTypeVersion', __args__, opts=opts, typ=GetPublicTypeVersionResult).value

    return AwaitableGetPublicTypeVersionResult(
        public_type_arn=pulumi.get(__ret__, 'public_type_arn'),
        publisher_id=pulumi.get(__ret__, 'publisher_id'),
        type_version_arn=pulumi.get(__ret__, 'type_version_arn'))


@_utilities.lift_output_func(get_public_type_version)
def get_public_type_version_output(public_type_arn: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPublicTypeVersionResult]:
    """
    Test and Publish a resource that has been registered in the CloudFormation Registry.


    :param str public_type_arn: The Amazon Resource Number (ARN) assigned to the public extension upon publication
    """
    ...
