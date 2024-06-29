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
    'LoggingConfigurationCloudWatchLogsDestinationConfiguration',
    'LoggingConfigurationDestinationConfiguration',
    'LoggingConfigurationFirehoseDestinationConfiguration',
    'LoggingConfigurationS3DestinationConfiguration',
    'RoomMessageReviewHandler',
]

@pulumi.output_type
class LoggingConfigurationCloudWatchLogsDestinationConfiguration(dict):
    """
    CloudWatch destination configuration for IVS Chat logging.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logGroupName":
            suggest = "log_group_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoggingConfigurationCloudWatchLogsDestinationConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoggingConfigurationCloudWatchLogsDestinationConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoggingConfigurationCloudWatchLogsDestinationConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_group_name: str):
        """
        CloudWatch destination configuration for IVS Chat logging.
        :param str log_group_name: Name of the Amazon CloudWatch Logs log group where chat activity will be logged.
        """
        pulumi.set(__self__, "log_group_name", log_group_name)

    @property
    @pulumi.getter(name="logGroupName")
    def log_group_name(self) -> str:
        """
        Name of the Amazon CloudWatch Logs log group where chat activity will be logged.
        """
        return pulumi.get(self, "log_group_name")


@pulumi.output_type
class LoggingConfigurationDestinationConfiguration(dict):
    """
    Destination configuration for IVS Chat logging.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudWatchLogs":
            suggest = "cloud_watch_logs"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoggingConfigurationDestinationConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoggingConfigurationDestinationConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoggingConfigurationDestinationConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_watch_logs: Optional['outputs.LoggingConfigurationCloudWatchLogsDestinationConfiguration'] = None,
                 firehose: Optional['outputs.LoggingConfigurationFirehoseDestinationConfiguration'] = None,
                 s3: Optional['outputs.LoggingConfigurationS3DestinationConfiguration'] = None):
        """
        Destination configuration for IVS Chat logging.
        :param 'LoggingConfigurationCloudWatchLogsDestinationConfiguration' cloud_watch_logs: An Amazon CloudWatch Logs destination configuration where chat activity will be logged.
        :param 'LoggingConfigurationFirehoseDestinationConfiguration' firehose: An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.
        :param 'LoggingConfigurationS3DestinationConfiguration' s3: An Amazon S3 destination configuration where chat activity will be logged.
        """
        if cloud_watch_logs is not None:
            pulumi.set(__self__, "cloud_watch_logs", cloud_watch_logs)
        if firehose is not None:
            pulumi.set(__self__, "firehose", firehose)
        if s3 is not None:
            pulumi.set(__self__, "s3", s3)

    @property
    @pulumi.getter(name="cloudWatchLogs")
    def cloud_watch_logs(self) -> Optional['outputs.LoggingConfigurationCloudWatchLogsDestinationConfiguration']:
        """
        An Amazon CloudWatch Logs destination configuration where chat activity will be logged.
        """
        return pulumi.get(self, "cloud_watch_logs")

    @property
    @pulumi.getter
    def firehose(self) -> Optional['outputs.LoggingConfigurationFirehoseDestinationConfiguration']:
        """
        An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.
        """
        return pulumi.get(self, "firehose")

    @property
    @pulumi.getter
    def s3(self) -> Optional['outputs.LoggingConfigurationS3DestinationConfiguration']:
        """
        An Amazon S3 destination configuration where chat activity will be logged.
        """
        return pulumi.get(self, "s3")


@pulumi.output_type
class LoggingConfigurationFirehoseDestinationConfiguration(dict):
    """
    Kinesis Firehose destination configuration for IVS Chat logging.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "deliveryStreamName":
            suggest = "delivery_stream_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoggingConfigurationFirehoseDestinationConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoggingConfigurationFirehoseDestinationConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoggingConfigurationFirehoseDestinationConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 delivery_stream_name: str):
        """
        Kinesis Firehose destination configuration for IVS Chat logging.
        :param str delivery_stream_name: Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.
        """
        pulumi.set(__self__, "delivery_stream_name", delivery_stream_name)

    @property
    @pulumi.getter(name="deliveryStreamName")
    def delivery_stream_name(self) -> str:
        """
        Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.
        """
        return pulumi.get(self, "delivery_stream_name")


@pulumi.output_type
class LoggingConfigurationS3DestinationConfiguration(dict):
    """
    S3 destination configuration for IVS Chat logging.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bucketName":
            suggest = "bucket_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LoggingConfigurationS3DestinationConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LoggingConfigurationS3DestinationConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LoggingConfigurationS3DestinationConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bucket_name: str):
        """
        S3 destination configuration for IVS Chat logging.
        :param str bucket_name: Name of the Amazon S3 bucket where chat activity will be logged.
        """
        pulumi.set(__self__, "bucket_name", bucket_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        """
        Name of the Amazon S3 bucket where chat activity will be logged.
        """
        return pulumi.get(self, "bucket_name")


@pulumi.output_type
class RoomMessageReviewHandler(dict):
    """
    Configuration information for optional review of messages.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fallbackResult":
            suggest = "fallback_result"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RoomMessageReviewHandler. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RoomMessageReviewHandler.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RoomMessageReviewHandler.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fallback_result: Optional['RoomMessageReviewHandlerFallbackResult'] = None,
                 uri: Optional[str] = None):
        """
        Configuration information for optional review of messages.
        :param 'RoomMessageReviewHandlerFallbackResult' fallback_result: Specifies the fallback behavior if the handler does not return a valid response, encounters an error, or times out.
        :param str uri: Identifier of the message review handler.
        """
        if fallback_result is not None:
            pulumi.set(__self__, "fallback_result", fallback_result)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="fallbackResult")
    def fallback_result(self) -> Optional['RoomMessageReviewHandlerFallbackResult']:
        """
        Specifies the fallback behavior if the handler does not return a valid response, encounters an error, or times out.
        """
        return pulumi.get(self, "fallback_result")

    @property
    @pulumi.getter
    def uri(self) -> Optional[str]:
        """
        Identifier of the message review handler.
        """
        return pulumi.get(self, "uri")


