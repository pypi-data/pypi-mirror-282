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
from ._enums import *

__all__ = [
    'GetLocationNfsResult',
    'AwaitableGetLocationNfsResult',
    'get_location_nfs',
    'get_location_nfs_output',
]

@pulumi.output_type
class GetLocationNfsResult:
    def __init__(__self__, location_arn=None, location_uri=None, mount_options=None, on_prem_config=None, tags=None):
        if location_arn and not isinstance(location_arn, str):
            raise TypeError("Expected argument 'location_arn' to be a str")
        pulumi.set(__self__, "location_arn", location_arn)
        if location_uri and not isinstance(location_uri, str):
            raise TypeError("Expected argument 'location_uri' to be a str")
        pulumi.set(__self__, "location_uri", location_uri)
        if mount_options and not isinstance(mount_options, dict):
            raise TypeError("Expected argument 'mount_options' to be a dict")
        pulumi.set(__self__, "mount_options", mount_options)
        if on_prem_config and not isinstance(on_prem_config, dict):
            raise TypeError("Expected argument 'on_prem_config' to be a dict")
        pulumi.set(__self__, "on_prem_config", on_prem_config)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="locationArn")
    def location_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the NFS location.
        """
        return pulumi.get(self, "location_arn")

    @property
    @pulumi.getter(name="locationUri")
    def location_uri(self) -> Optional[str]:
        """
        The URL of the NFS location that was described.
        """
        return pulumi.get(self, "location_uri")

    @property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Optional['outputs.LocationNfsMountOptions']:
        """
        Specifies the options that DataSync can use to mount your NFS file server.
        """
        return pulumi.get(self, "mount_options")

    @property
    @pulumi.getter(name="onPremConfig")
    def on_prem_config(self) -> Optional['outputs.LocationNfsOnPremConfig']:
        """
        Specifies the Amazon Resource Name (ARN) of the DataSync agent that want to connect to your NFS file server.

        You can specify more than one agent. For more information, see [Using multiple agents for transfers](https://docs.aws.amazon.com/datasync/latest/userguide/multiple-agents.html) .
        """
        return pulumi.get(self, "on_prem_config")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetLocationNfsResult(GetLocationNfsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocationNfsResult(
            location_arn=self.location_arn,
            location_uri=self.location_uri,
            mount_options=self.mount_options,
            on_prem_config=self.on_prem_config,
            tags=self.tags)


def get_location_nfs(location_arn: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocationNfsResult:
    """
    Resource schema for AWS::DataSync::LocationNFS


    :param str location_arn: The Amazon Resource Name (ARN) of the NFS location.
    """
    __args__ = dict()
    __args__['locationArn'] = location_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:datasync:getLocationNfs', __args__, opts=opts, typ=GetLocationNfsResult).value

    return AwaitableGetLocationNfsResult(
        location_arn=pulumi.get(__ret__, 'location_arn'),
        location_uri=pulumi.get(__ret__, 'location_uri'),
        mount_options=pulumi.get(__ret__, 'mount_options'),
        on_prem_config=pulumi.get(__ret__, 'on_prem_config'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_location_nfs)
def get_location_nfs_output(location_arn: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocationNfsResult]:
    """
    Resource schema for AWS::DataSync::LocationNFS


    :param str location_arn: The Amazon Resource Name (ARN) of the NFS location.
    """
    ...
