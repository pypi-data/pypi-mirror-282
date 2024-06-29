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
from ._enums import *

__all__ = [
    'GetAccessPointResult',
    'AwaitableGetAccessPointResult',
    'get_access_point',
    'get_access_point_output',
]

@pulumi.output_type
class GetAccessPointResult:
    def __init__(__self__, alias=None, arn=None, network_origin=None, policy=None, public_access_block_configuration=None):
        if alias and not isinstance(alias, str):
            raise TypeError("Expected argument 'alias' to be a str")
        pulumi.set(__self__, "alias", alias)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if network_origin and not isinstance(network_origin, str):
            raise TypeError("Expected argument 'network_origin' to be a str")
        pulumi.set(__self__, "network_origin", network_origin)
        if policy and not isinstance(policy, dict):
            raise TypeError("Expected argument 'policy' to be a dict")
        pulumi.set(__self__, "policy", policy)
        if public_access_block_configuration and not isinstance(public_access_block_configuration, dict):
            raise TypeError("Expected argument 'public_access_block_configuration' to be a dict")
        pulumi.set(__self__, "public_access_block_configuration", public_access_block_configuration)

    @property
    @pulumi.getter
    def alias(self) -> Optional[str]:
        """
        The alias of this Access Point. This alias can be used for compatibility purposes with other AWS services and third-party applications.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the specified accesspoint.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="networkOrigin")
    def network_origin(self) -> Optional['AccessPointNetworkOrigin']:
        """
        Indicates whether this Access Point allows access from the public Internet. If VpcConfiguration is specified for this Access Point, then NetworkOrigin is VPC, and the Access Point doesn't allow access from the public Internet. Otherwise, NetworkOrigin is Internet, and the Access Point allows access from the public Internet, subject to the Access Point and bucket access policies.
        """
        return pulumi.get(self, "network_origin")

    @property
    @pulumi.getter
    def policy(self) -> Optional[Any]:
        """
        The Access Point Policy you want to apply to this access point.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::S3::AccessPoint` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="publicAccessBlockConfiguration")
    def public_access_block_configuration(self) -> Optional['outputs.AccessPointPublicAccessBlockConfiguration']:
        """
        The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.
        """
        return pulumi.get(self, "public_access_block_configuration")


class AwaitableGetAccessPointResult(GetAccessPointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessPointResult(
            alias=self.alias,
            arn=self.arn,
            network_origin=self.network_origin,
            policy=self.policy,
            public_access_block_configuration=self.public_access_block_configuration)


def get_access_point(name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessPointResult:
    """
    The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.


    :param str name: The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:s3:getAccessPoint', __args__, opts=opts, typ=GetAccessPointResult).value

    return AwaitableGetAccessPointResult(
        alias=pulumi.get(__ret__, 'alias'),
        arn=pulumi.get(__ret__, 'arn'),
        network_origin=pulumi.get(__ret__, 'network_origin'),
        policy=pulumi.get(__ret__, 'policy'),
        public_access_block_configuration=pulumi.get(__ret__, 'public_access_block_configuration'))


@_utilities.lift_output_func(get_access_point)
def get_access_point_output(name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessPointResult]:
    """
    The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.


    :param str name: The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.
    """
    ...
