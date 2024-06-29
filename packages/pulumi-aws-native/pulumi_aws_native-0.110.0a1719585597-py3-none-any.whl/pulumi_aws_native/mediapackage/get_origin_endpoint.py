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
    'GetOriginEndpointResult',
    'AwaitableGetOriginEndpointResult',
    'get_origin_endpoint',
    'get_origin_endpoint_output',
]

@pulumi.output_type
class GetOriginEndpointResult:
    def __init__(__self__, arn=None, authorization=None, channel_id=None, cmaf_package=None, dash_package=None, description=None, hls_package=None, manifest_name=None, mss_package=None, origination=None, startover_window_seconds=None, tags=None, time_delay_seconds=None, url=None, whitelist=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if authorization and not isinstance(authorization, dict):
            raise TypeError("Expected argument 'authorization' to be a dict")
        pulumi.set(__self__, "authorization", authorization)
        if channel_id and not isinstance(channel_id, str):
            raise TypeError("Expected argument 'channel_id' to be a str")
        pulumi.set(__self__, "channel_id", channel_id)
        if cmaf_package and not isinstance(cmaf_package, dict):
            raise TypeError("Expected argument 'cmaf_package' to be a dict")
        pulumi.set(__self__, "cmaf_package", cmaf_package)
        if dash_package and not isinstance(dash_package, dict):
            raise TypeError("Expected argument 'dash_package' to be a dict")
        pulumi.set(__self__, "dash_package", dash_package)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if hls_package and not isinstance(hls_package, dict):
            raise TypeError("Expected argument 'hls_package' to be a dict")
        pulumi.set(__self__, "hls_package", hls_package)
        if manifest_name and not isinstance(manifest_name, str):
            raise TypeError("Expected argument 'manifest_name' to be a str")
        pulumi.set(__self__, "manifest_name", manifest_name)
        if mss_package and not isinstance(mss_package, dict):
            raise TypeError("Expected argument 'mss_package' to be a dict")
        pulumi.set(__self__, "mss_package", mss_package)
        if origination and not isinstance(origination, str):
            raise TypeError("Expected argument 'origination' to be a str")
        pulumi.set(__self__, "origination", origination)
        if startover_window_seconds and not isinstance(startover_window_seconds, int):
            raise TypeError("Expected argument 'startover_window_seconds' to be a int")
        pulumi.set(__self__, "startover_window_seconds", startover_window_seconds)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if time_delay_seconds and not isinstance(time_delay_seconds, int):
            raise TypeError("Expected argument 'time_delay_seconds' to be a int")
        pulumi.set(__self__, "time_delay_seconds", time_delay_seconds)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)
        if whitelist and not isinstance(whitelist, list):
            raise TypeError("Expected argument 'whitelist' to be a list")
        pulumi.set(__self__, "whitelist", whitelist)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def authorization(self) -> Optional['outputs.OriginEndpointAuthorization']:
        """
        Parameters for CDN authorization.
        """
        return pulumi.get(self, "authorization")

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[str]:
        """
        The ID of the Channel the OriginEndpoint is associated with.
        """
        return pulumi.get(self, "channel_id")

    @property
    @pulumi.getter(name="cmafPackage")
    def cmaf_package(self) -> Optional['outputs.OriginEndpointCmafPackage']:
        """
        Parameters for Common Media Application Format (CMAF) packaging.
        """
        return pulumi.get(self, "cmaf_package")

    @property
    @pulumi.getter(name="dashPackage")
    def dash_package(self) -> Optional['outputs.OriginEndpointDashPackage']:
        """
        Parameters for DASH packaging.
        """
        return pulumi.get(self, "dash_package")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A short text description of the OriginEndpoint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hlsPackage")
    def hls_package(self) -> Optional['outputs.OriginEndpointHlsPackage']:
        """
        Parameters for Apple HLS packaging.
        """
        return pulumi.get(self, "hls_package")

    @property
    @pulumi.getter(name="manifestName")
    def manifest_name(self) -> Optional[str]:
        """
        A short string appended to the end of the OriginEndpoint URL.
        """
        return pulumi.get(self, "manifest_name")

    @property
    @pulumi.getter(name="mssPackage")
    def mss_package(self) -> Optional['outputs.OriginEndpointMssPackage']:
        """
        Parameters for Microsoft Smooth Streaming packaging.
        """
        return pulumi.get(self, "mss_package")

    @property
    @pulumi.getter
    def origination(self) -> Optional['OriginEndpointOrigination']:
        """
        Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
        """
        return pulumi.get(self, "origination")

    @property
    @pulumi.getter(name="startoverWindowSeconds")
    def startover_window_seconds(self) -> Optional[int]:
        """
        Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
        """
        return pulumi.get(self, "startover_window_seconds")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        A collection of tags associated with a resource
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeDelaySeconds")
    def time_delay_seconds(self) -> Optional[int]:
        """
        Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
        """
        return pulumi.get(self, "time_delay_seconds")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The URL of the packaged OriginEndpoint for consumption.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def whitelist(self) -> Optional[Sequence[str]]:
        """
        A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
        """
        return pulumi.get(self, "whitelist")


class AwaitableGetOriginEndpointResult(GetOriginEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOriginEndpointResult(
            arn=self.arn,
            authorization=self.authorization,
            channel_id=self.channel_id,
            cmaf_package=self.cmaf_package,
            dash_package=self.dash_package,
            description=self.description,
            hls_package=self.hls_package,
            manifest_name=self.manifest_name,
            mss_package=self.mss_package,
            origination=self.origination,
            startover_window_seconds=self.startover_window_seconds,
            tags=self.tags,
            time_delay_seconds=self.time_delay_seconds,
            url=self.url,
            whitelist=self.whitelist)


def get_origin_endpoint(id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOriginEndpointResult:
    """
    Resource schema for AWS::MediaPackage::OriginEndpoint


    :param str id: The ID of the OriginEndpoint.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackage:getOriginEndpoint', __args__, opts=opts, typ=GetOriginEndpointResult).value

    return AwaitableGetOriginEndpointResult(
        arn=pulumi.get(__ret__, 'arn'),
        authorization=pulumi.get(__ret__, 'authorization'),
        channel_id=pulumi.get(__ret__, 'channel_id'),
        cmaf_package=pulumi.get(__ret__, 'cmaf_package'),
        dash_package=pulumi.get(__ret__, 'dash_package'),
        description=pulumi.get(__ret__, 'description'),
        hls_package=pulumi.get(__ret__, 'hls_package'),
        manifest_name=pulumi.get(__ret__, 'manifest_name'),
        mss_package=pulumi.get(__ret__, 'mss_package'),
        origination=pulumi.get(__ret__, 'origination'),
        startover_window_seconds=pulumi.get(__ret__, 'startover_window_seconds'),
        tags=pulumi.get(__ret__, 'tags'),
        time_delay_seconds=pulumi.get(__ret__, 'time_delay_seconds'),
        url=pulumi.get(__ret__, 'url'),
        whitelist=pulumi.get(__ret__, 'whitelist'))


@_utilities.lift_output_func(get_origin_endpoint)
def get_origin_endpoint_output(id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOriginEndpointResult]:
    """
    Resource schema for AWS::MediaPackage::OriginEndpoint


    :param str id: The ID of the OriginEndpoint.
    """
    ...
