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
    'RecordingConfigurationDestinationConfiguration',
    'RecordingConfigurationRenditionConfiguration',
    'RecordingConfigurationS3DestinationConfiguration',
    'RecordingConfigurationThumbnailConfiguration',
    'StorageConfigurationS3StorageConfiguration',
    'VideoProperties',
]

@pulumi.output_type
class RecordingConfigurationDestinationConfiguration(dict):
    """
    Recording Destination Configuration.
    """
    def __init__(__self__, *,
                 s3: Optional['outputs.RecordingConfigurationS3DestinationConfiguration'] = None):
        """
        Recording Destination Configuration.
        :param 'RecordingConfigurationS3DestinationConfiguration' s3: An S3 destination configuration where recorded videos will be stored. See the [S3DestinationConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html) property type for more information.
        """
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)

    @property
    @pulumi.getter
    def s3(self) -> Optional['outputs.RecordingConfigurationS3DestinationConfiguration']:
        """
        An S3 destination configuration where recorded videos will be stored. See the [S3DestinationConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivs-recordingconfiguration-s3destinationconfiguration.html) property type for more information.
        """
        return pulumi.get(self, "s3")


@pulumi.output_type
class RecordingConfigurationRenditionConfiguration(dict):
    """
    Rendition Configuration describes which renditions should be recorded for a stream.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "renditionSelection":
            suggest = "rendition_selection"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordingConfigurationRenditionConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordingConfigurationRenditionConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordingConfigurationRenditionConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 rendition_selection: Optional['RecordingConfigurationRenditionConfigurationRenditionSelection'] = None,
                 renditions: Optional[Sequence['RecordingConfigurationRenditionConfigurationRenditionsItem']] = None):
        """
        Rendition Configuration describes which renditions should be recorded for a stream.
        :param 'RecordingConfigurationRenditionConfigurationRenditionSelection' rendition_selection: Resolution Selection indicates which set of renditions are recorded for a stream.
        :param Sequence['RecordingConfigurationRenditionConfigurationRenditionsItem'] renditions: Renditions indicates which renditions are recorded for a stream.
        """
        if rendition_selection is not None:
            pulumi.set(__self__, "rendition_selection", rendition_selection)
        if renditions is not None:
            pulumi.set(__self__, "renditions", renditions)

    @property
    @pulumi.getter(name="renditionSelection")
    def rendition_selection(self) -> Optional['RecordingConfigurationRenditionConfigurationRenditionSelection']:
        """
        Resolution Selection indicates which set of renditions are recorded for a stream.
        """
        return pulumi.get(self, "rendition_selection")

    @property
    @pulumi.getter
    def renditions(self) -> Optional[Sequence['RecordingConfigurationRenditionConfigurationRenditionsItem']]:
        """
        Renditions indicates which renditions are recorded for a stream.
        """
        return pulumi.get(self, "renditions")


@pulumi.output_type
class RecordingConfigurationS3DestinationConfiguration(dict):
    """
    Recording S3 Destination Configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketName":
            suggest = "bucket_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordingConfigurationS3DestinationConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordingConfigurationS3DestinationConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordingConfigurationS3DestinationConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_name: str):
        """
        Recording S3 Destination Configuration.
        :param str bucket_name: Location (S3 bucket name) where recorded videos will be stored.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        Location (S3 bucket name) where recorded videos will be stored.
        """
        return pulumi.get(self, "bucket_name")


@pulumi.output_type
class RecordingConfigurationThumbnailConfiguration(dict):
    """
    Recording Thumbnail Configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "recordingMode":
            suggest = "recording_mode"
        elif key == "targetIntervalSeconds":
            suggest = "target_interval_seconds"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordingConfigurationThumbnailConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordingConfigurationThumbnailConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordingConfigurationThumbnailConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 recording_mode: Optional['RecordingConfigurationThumbnailConfigurationRecordingMode'] = None,
                 resolution: Optional['RecordingConfigurationThumbnailConfigurationResolution'] = None,
                 storage: Optional[Sequence['RecordingConfigurationThumbnailConfigurationStorageItem']] = None,
                 target_interval_seconds: Optional[int] = None):
        """
        Recording Thumbnail Configuration.
        :param 'RecordingConfigurationThumbnailConfigurationRecordingMode' recording_mode: Thumbnail Recording Mode, which determines whether thumbnails are recorded at an interval or are disabled.
        :param 'RecordingConfigurationThumbnailConfigurationResolution' resolution: Resolution indicates the desired resolution of recorded thumbnails.
        :param Sequence['RecordingConfigurationThumbnailConfigurationStorageItem'] storage: Storage indicates the format in which thumbnails are recorded.
        :param int target_interval_seconds: Target Interval Seconds defines the interval at which thumbnails are recorded. This field is required if RecordingMode is INTERVAL.
        """
        if recording_mode is not None:
            pulumi.set(__self__, "recording_mode", recording_mode)
        if resolution is not None:
            pulumi.set(__self__, "resolution", resolution)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)
        if target_interval_seconds is not None:
            pulumi.set(__self__, "target_interval_seconds", target_interval_seconds)

    @property
    @pulumi.getter(name="recordingMode")
    def recording_mode(self) -> Optional['RecordingConfigurationThumbnailConfigurationRecordingMode']:
        """
        Thumbnail Recording Mode, which determines whether thumbnails are recorded at an interval or are disabled.
        """
        return pulumi.get(self, "recording_mode")

    @property
    @pulumi.getter
    def resolution(self) -> Optional['RecordingConfigurationThumbnailConfigurationResolution']:
        """
        Resolution indicates the desired resolution of recorded thumbnails.
        """
        return pulumi.get(self, "resolution")

    @property
    @pulumi.getter
    def storage(self) -> Optional[Sequence['RecordingConfigurationThumbnailConfigurationStorageItem']]:
        """
        Storage indicates the format in which thumbnails are recorded.
        """
        return pulumi.get(self, "storage")

    @property
    @pulumi.getter(name="targetIntervalSeconds")
    def target_interval_seconds(self) -> Optional[int]:
        """
        Target Interval Seconds defines the interval at which thumbnails are recorded. This field is required if RecordingMode is INTERVAL.
        """
        return pulumi.get(self, "target_interval_seconds")


@pulumi.output_type
class StorageConfigurationS3StorageConfiguration(dict):
    """
    A complex type that describes an S3 location where recorded videos will be stored.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketName":
            suggest = "bucket_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StorageConfigurationS3StorageConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StorageConfigurationS3StorageConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StorageConfigurationS3StorageConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_name: str):
        """
        A complex type that describes an S3 location where recorded videos will be stored.
        :param str bucket_name: Location (S3 bucket name) where recorded videos will be stored. Note that the StorageConfiguration and S3 bucket must be in the same region as the Composition.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        Location (S3 bucket name) where recorded videos will be stored. Note that the StorageConfiguration and S3 bucket must be in the same region as the Composition.
        """
        return pulumi.get(self, "bucket_name")


@pulumi.output_type
class VideoProperties(dict):
    """
    Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps
    """
    def __init__(__self__, *,
                 bitrate: Optional[int] = None,
                 framerate: Optional[float] = None,
                 height: Optional[int] = None,
                 width: Optional[int] = None):
        """
        Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps
        :param int bitrate: Bitrate for generated output, in bps. Default: 2500000.
        :param float framerate: Video frame rate, in fps. Default: 30.
        :param int height: Video-resolution height. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 720.
        :param int width: Video-resolution width. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 1280.
        """
        if bitrate is not None:
            pulumi.set(__self__, "bitrate", bitrate)
        if framerate is not None:
            pulumi.set(__self__, "framerate", framerate)
        if height is not None:
            pulumi.set(__self__, "height", height)
        if width is not None:
            pulumi.set(__self__, "width", width)

    @property
    @pulumi.getter
    def bitrate(self) -> Optional[int]:
        """
        Bitrate for generated output, in bps. Default: 2500000.
        """
        return pulumi.get(self, "bitrate")

    @property
    @pulumi.getter
    def framerate(self) -> Optional[float]:
        """
        Video frame rate, in fps. Default: 30.
        """
        return pulumi.get(self, "framerate")

    @property
    @pulumi.getter
    def height(self) -> Optional[int]:
        """
        Video-resolution height. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 720.
        """
        return pulumi.get(self, "height")

    @property
    @pulumi.getter
    def width(self) -> Optional[int]:
        """
        Video-resolution width. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 1280.
        """
        return pulumi.get(self, "width")


