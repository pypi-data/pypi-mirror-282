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
    def __init__(__self__, arn=None, container_type=None, created_at=None, dash_manifest_urls=None, dash_manifests=None, description=None, hls_manifest_urls=None, hls_manifests=None, low_latency_hls_manifest_urls=None, low_latency_hls_manifests=None, modified_at=None, segment=None, startover_window_seconds=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if container_type and not isinstance(container_type, str):
            raise TypeError("Expected argument 'container_type' to be a str")
        pulumi.set(__self__, "container_type", container_type)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if dash_manifest_urls and not isinstance(dash_manifest_urls, list):
            raise TypeError("Expected argument 'dash_manifest_urls' to be a list")
        pulumi.set(__self__, "dash_manifest_urls", dash_manifest_urls)
        if dash_manifests and not isinstance(dash_manifests, list):
            raise TypeError("Expected argument 'dash_manifests' to be a list")
        pulumi.set(__self__, "dash_manifests", dash_manifests)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if hls_manifest_urls and not isinstance(hls_manifest_urls, list):
            raise TypeError("Expected argument 'hls_manifest_urls' to be a list")
        pulumi.set(__self__, "hls_manifest_urls", hls_manifest_urls)
        if hls_manifests and not isinstance(hls_manifests, list):
            raise TypeError("Expected argument 'hls_manifests' to be a list")
        pulumi.set(__self__, "hls_manifests", hls_manifests)
        if low_latency_hls_manifest_urls and not isinstance(low_latency_hls_manifest_urls, list):
            raise TypeError("Expected argument 'low_latency_hls_manifest_urls' to be a list")
        pulumi.set(__self__, "low_latency_hls_manifest_urls", low_latency_hls_manifest_urls)
        if low_latency_hls_manifests and not isinstance(low_latency_hls_manifests, list):
            raise TypeError("Expected argument 'low_latency_hls_manifests' to be a list")
        pulumi.set(__self__, "low_latency_hls_manifests", low_latency_hls_manifests)
        if modified_at and not isinstance(modified_at, str):
            raise TypeError("Expected argument 'modified_at' to be a str")
        pulumi.set(__self__, "modified_at", modified_at)
        if segment and not isinstance(segment, dict):
            raise TypeError("Expected argument 'segment' to be a dict")
        pulumi.set(__self__, "segment", segment)
        if startover_window_seconds and not isinstance(startover_window_seconds, int):
            raise TypeError("Expected argument 'startover_window_seconds' to be a int")
        pulumi.set(__self__, "startover_window_seconds", startover_window_seconds)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        <p>The Amazon Resource Name (ARN) associated with the resource.</p>
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="containerType")
    def container_type(self) -> Optional['OriginEndpointContainerType']:
        """
        The container type associated with the origin endpoint configuration.
        """
        return pulumi.get(self, "container_type")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        <p>The date and time the origin endpoint was created.</p>
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dashManifestUrls")
    def dash_manifest_urls(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "dash_manifest_urls")

    @property
    @pulumi.getter(name="dashManifests")
    def dash_manifests(self) -> Optional[Sequence['outputs.OriginEndpointDashManifestConfiguration']]:
        """
        <p>A DASH manifest configuration.</p>
        """
        return pulumi.get(self, "dash_manifests")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        <p>Enter any descriptive text that helps you to identify the origin endpoint.</p>
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hlsManifestUrls")
    def hls_manifest_urls(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "hls_manifest_urls")

    @property
    @pulumi.getter(name="hlsManifests")
    def hls_manifests(self) -> Optional[Sequence['outputs.OriginEndpointHlsManifestConfiguration']]:
        """
        <p>An HTTP live streaming (HLS) manifest configuration.</p>
        """
        return pulumi.get(self, "hls_manifests")

    @property
    @pulumi.getter(name="lowLatencyHlsManifestUrls")
    def low_latency_hls_manifest_urls(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "low_latency_hls_manifest_urls")

    @property
    @pulumi.getter(name="lowLatencyHlsManifests")
    def low_latency_hls_manifests(self) -> Optional[Sequence['outputs.OriginEndpointLowLatencyHlsManifestConfiguration']]:
        """
        <p>A low-latency HLS manifest configuration.</p>
        """
        return pulumi.get(self, "low_latency_hls_manifests")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> Optional[str]:
        """
        <p>The date and time the origin endpoint was modified.</p>
        """
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter
    def segment(self) -> Optional['outputs.OriginEndpointSegment']:
        """
        The segment associated with the origin endpoint.
        """
        return pulumi.get(self, "segment")

    @property
    @pulumi.getter(name="startoverWindowSeconds")
    def startover_window_seconds(self) -> Optional[int]:
        """
        <p>The size of the window (in seconds) to create a window of the live stream that's available for on-demand viewing. Viewers can start-over or catch-up on content that falls within the window. The maximum startover window is 1,209,600 seconds (14 days).</p>
        """
        return pulumi.get(self, "startover_window_seconds")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags associated with the origin endpoint.
        """
        return pulumi.get(self, "tags")


class AwaitableGetOriginEndpointResult(GetOriginEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOriginEndpointResult(
            arn=self.arn,
            container_type=self.container_type,
            created_at=self.created_at,
            dash_manifest_urls=self.dash_manifest_urls,
            dash_manifests=self.dash_manifests,
            description=self.description,
            hls_manifest_urls=self.hls_manifest_urls,
            hls_manifests=self.hls_manifests,
            low_latency_hls_manifest_urls=self.low_latency_hls_manifest_urls,
            low_latency_hls_manifests=self.low_latency_hls_manifests,
            modified_at=self.modified_at,
            segment=self.segment,
            startover_window_seconds=self.startover_window_seconds,
            tags=self.tags)


def get_origin_endpoint(arn: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOriginEndpointResult:
    """
    <p>Represents an origin endpoint that is associated with a channel, offering a dynamically repackaged version of its content through various streaming media protocols. The content can be efficiently disseminated to end-users via a Content Delivery Network (CDN), like Amazon CloudFront.</p>


    :param str arn: <p>The Amazon Resource Name (ARN) associated with the resource.</p>
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:mediapackagev2:getOriginEndpoint', __args__, opts=opts, typ=GetOriginEndpointResult).value

    return AwaitableGetOriginEndpointResult(
        arn=pulumi.get(__ret__, 'arn'),
        container_type=pulumi.get(__ret__, 'container_type'),
        created_at=pulumi.get(__ret__, 'created_at'),
        dash_manifest_urls=pulumi.get(__ret__, 'dash_manifest_urls'),
        dash_manifests=pulumi.get(__ret__, 'dash_manifests'),
        description=pulumi.get(__ret__, 'description'),
        hls_manifest_urls=pulumi.get(__ret__, 'hls_manifest_urls'),
        hls_manifests=pulumi.get(__ret__, 'hls_manifests'),
        low_latency_hls_manifest_urls=pulumi.get(__ret__, 'low_latency_hls_manifest_urls'),
        low_latency_hls_manifests=pulumi.get(__ret__, 'low_latency_hls_manifests'),
        modified_at=pulumi.get(__ret__, 'modified_at'),
        segment=pulumi.get(__ret__, 'segment'),
        startover_window_seconds=pulumi.get(__ret__, 'startover_window_seconds'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_origin_endpoint)
def get_origin_endpoint_output(arn: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOriginEndpointResult]:
    """
    <p>Represents an origin endpoint that is associated with a channel, offering a dynamically repackaged version of its content through various streaming media protocols. The content can be efficiently disseminated to end-users via a Content Delivery Network (CDN), like Amazon CloudFront.</p>


    :param str arn: <p>The Amazon Resource Name (ARN) associated with the resource.</p>
    """
    ...
