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
    'GetLocationFSxLustreResult',
    'AwaitableGetLocationFSxLustreResult',
    'get_location_f_sx_lustre',
    'get_location_f_sx_lustre_output',
]

@pulumi.output_type
class GetLocationFSxLustreResult:
    def __init__(__self__, location_arn=None, location_uri=None, tags=None):
        if location_arn and not isinstance(location_arn, str):
            raise TypeError("Expected argument 'location_arn' to be a str")
        pulumi.set(__self__, "location_arn", location_arn)
        if location_uri and not isinstance(location_uri, str):
            raise TypeError("Expected argument 'location_uri' to be a str")
        pulumi.set(__self__, "location_uri", location_uri)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the Amazon FSx for Lustre file system location that is created.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[str]:
        """
        The URL of the FSx for Lustre location that was described.
        """
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetLocationFSxLustreResult(GetLocationFSxLustreResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocationFSxLustreResult(
            location_arn=self.location_arn,
            location_uri=self.location_uri,
            tags=self.tags)


def get_location_f_sx_lustre(location_arn: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocationFSxLustreResult:
    """
    Resource schema for AWS::DataSync::LocationFSxLustre.


    :param str location_arn: The Amazon Resource Name (ARN) of the Amazon FSx for Lustre file system location that is created.
    """
    __args__ = dict()
    __args__['locationArn'] = location_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:datasync:getLocationFSxLustre', __args__, opts=opts, typ=GetLocationFSxLustreResult).value

    return AwaitableGetLocationFSxLustreResult(
        location_arn=pulumi.get(__ret__, 'location_arn'),
        location_uri=pulumi.get(__ret__, 'location_uri'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_location_f_sx_lustre)
def get_location_f_sx_lustre_output(location_arn: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocationFSxLustreResult]:
    """
    Resource schema for AWS::DataSync::LocationFSxLustre.


    :param str location_arn: The Amazon Resource Name (ARN) of the Amazon FSx for Lustre file system location that is created.
    """
    ...
