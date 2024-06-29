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
    'MultiplexOutputDestinationMultiplexMediaConnectOutputDestinationSettingsPropertiesArgs',
    'MultiplexOutputDestinationArgs',
    'MultiplexSettingsArgs',
    'MultiplexprogramMultiplexProgramPacketIdentifiersMapArgs',
    'MultiplexprogramMultiplexProgramPipelineDetailArgs',
    'MultiplexprogramMultiplexProgramServiceDescriptorArgs',
    'MultiplexprogramMultiplexProgramSettingsArgs',
    'MultiplexprogramMultiplexVideoSettingsArgs',
]

@pulumi.input_type
class MultiplexOutputDestinationMultiplexMediaConnectOutputDestinationSettingsPropertiesArgs:
    def __init__(__self__, *,
                 entitlement_arn: Optional[pulumi.Input[str]] = None):
        """
        Multiplex MediaConnect output destination settings.
        :param pulumi.Input[str] entitlement_arn: The MediaConnect entitlement ARN available as a Flow source.
        """
        if entitlement_arn is not None:
            pulumi.set(__self__, "entitlement_arn", entitlement_arn)

    @property
    @pulumi.getter(name="entitlementArn")
    def entitlement_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The MediaConnect entitlement ARN available as a Flow source.
        """
        return pulumi.get(self, "entitlement_arn")

    @entitlement_arn.setter
    def entitlement_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "entitlement_arn", value)


@pulumi.input_type
class MultiplexOutputDestinationArgs:
    def __init__(__self__, *,
                 multiplex_media_connect_output_destination_settings: Optional[pulumi.Input['MultiplexOutputDestinationMultiplexMediaConnectOutputDestinationSettingsPropertiesArgs']] = None):
        """
        Multiplex MediaConnect output destination settings.
        :param pulumi.Input['MultiplexOutputDestinationMultiplexMediaConnectOutputDestinationSettingsPropertiesArgs'] multiplex_media_connect_output_destination_settings: Multiplex MediaConnect output destination settings.
        """
        if multiplex_media_connect_output_destination_settings is not None:
            pulumi.set(__self__, "multiplex_media_connect_output_destination_settings", multiplex_media_connect_output_destination_settings)

    @property
    @pulumi.getter(name="multiplexMediaConnectOutputDestinationSettings")
    def multiplex_media_connect_output_destination_settings(self) -> Optional[pulumi.Input['MultiplexOutputDestinationMultiplexMediaConnectOutputDestinationSettingsPropertiesArgs']]:
        """
        Multiplex MediaConnect output destination settings.
        """
        return pulumi.get(self, "multiplex_media_connect_output_destination_settings")

    @multiplex_media_connect_output_destination_settings.setter
    def multiplex_media_connect_output_destination_settings(self, value: Optional[pulumi.Input['MultiplexOutputDestinationMultiplexMediaConnectOutputDestinationSettingsPropertiesArgs']]):
        pulumi.set(self, "multiplex_media_connect_output_destination_settings", value)


@pulumi.input_type
class MultiplexSettingsArgs:
    def __init__(__self__, *,
                 transport_stream_bitrate: pulumi.Input[int],
                 transport_stream_id: pulumi.Input[int],
                 maximum_video_buffer_delay_milliseconds: Optional[pulumi.Input[int]] = None,
                 transport_stream_reserved_bitrate: Optional[pulumi.Input[int]] = None):
        """
        A key-value pair to associate with a resource.
        :param pulumi.Input[int] transport_stream_bitrate: Transport stream bit rate.
        :param pulumi.Input[int] transport_stream_id: Transport stream ID.
        :param pulumi.Input[int] maximum_video_buffer_delay_milliseconds: Maximum video buffer delay in milliseconds.
        :param pulumi.Input[int] transport_stream_reserved_bitrate: Transport stream reserved bit rate.
        """
        pulumi.set(__self__, "transport_stream_bitrate", transport_stream_bitrate)
        pulumi.set(__self__, "transport_stream_id", transport_stream_id)
        if maximum_video_buffer_delay_milliseconds is not None:
            pulumi.set(__self__, "maximum_video_buffer_delay_milliseconds", maximum_video_buffer_delay_milliseconds)
        if transport_stream_reserved_bitrate is not None:
            pulumi.set(__self__, "transport_stream_reserved_bitrate", transport_stream_reserved_bitrate)

    @property
    @pulumi.getter(name="transportStreamBitrate")
    def transport_stream_bitrate(self) -> pulumi.Input[int]:
        """
        Transport stream bit rate.
        """
        return pulumi.get(self, "transport_stream_bitrate")

    @transport_stream_bitrate.setter
    def transport_stream_bitrate(self, value: pulumi.Input[int]):
        pulumi.set(self, "transport_stream_bitrate", value)

    @property
    @pulumi.getter(name="transportStreamId")
    def transport_stream_id(self) -> pulumi.Input[int]:
        """
        Transport stream ID.
        """
        return pulumi.get(self, "transport_stream_id")

    @transport_stream_id.setter
    def transport_stream_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "transport_stream_id", value)

    @property
    @pulumi.getter(name="maximumVideoBufferDelayMilliseconds")
    def maximum_video_buffer_delay_milliseconds(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum video buffer delay in milliseconds.
        """
        return pulumi.get(self, "maximum_video_buffer_delay_milliseconds")

    @maximum_video_buffer_delay_milliseconds.setter
    def maximum_video_buffer_delay_milliseconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_video_buffer_delay_milliseconds", value)

    @property
    @pulumi.getter(name="transportStreamReservedBitrate")
    def transport_stream_reserved_bitrate(self) -> Optional[pulumi.Input[int]]:
        """
        Transport stream reserved bit rate.
        """
        return pulumi.get(self, "transport_stream_reserved_bitrate")

    @transport_stream_reserved_bitrate.setter
    def transport_stream_reserved_bitrate(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "transport_stream_reserved_bitrate", value)


@pulumi.input_type
class MultiplexprogramMultiplexProgramPacketIdentifiersMapArgs:
    def __init__(__self__, *,
                 audio_pids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 dvb_sub_pids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 dvb_teletext_pid: Optional[pulumi.Input[int]] = None,
                 etv_platform_pid: Optional[pulumi.Input[int]] = None,
                 etv_signal_pid: Optional[pulumi.Input[int]] = None,
                 klv_data_pids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 pcr_pid: Optional[pulumi.Input[int]] = None,
                 pmt_pid: Optional[pulumi.Input[int]] = None,
                 private_metadata_pid: Optional[pulumi.Input[int]] = None,
                 scte27_pids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 scte35_pid: Optional[pulumi.Input[int]] = None,
                 timed_metadata_pid: Optional[pulumi.Input[int]] = None,
                 video_pid: Optional[pulumi.Input[int]] = None):
        """
        Packet identifiers map for a given Multiplex program.
        """
        if audio_pids is not None:
            pulumi.set(__self__, "audio_pids", audio_pids)
        if dvb_sub_pids is not None:
            pulumi.set(__self__, "dvb_sub_pids", dvb_sub_pids)
        if dvb_teletext_pid is not None:
            pulumi.set(__self__, "dvb_teletext_pid", dvb_teletext_pid)
        if etv_platform_pid is not None:
            pulumi.set(__self__, "etv_platform_pid", etv_platform_pid)
        if etv_signal_pid is not None:
            pulumi.set(__self__, "etv_signal_pid", etv_signal_pid)
        if klv_data_pids is not None:
            pulumi.set(__self__, "klv_data_pids", klv_data_pids)
        if pcr_pid is not None:
            pulumi.set(__self__, "pcr_pid", pcr_pid)
        if pmt_pid is not None:
            pulumi.set(__self__, "pmt_pid", pmt_pid)
        if private_metadata_pid is not None:
            pulumi.set(__self__, "private_metadata_pid", private_metadata_pid)
        if scte27_pids is not None:
            pulumi.set(__self__, "scte27_pids", scte27_pids)
        if scte35_pid is not None:
            pulumi.set(__self__, "scte35_pid", scte35_pid)
        if timed_metadata_pid is not None:
            pulumi.set(__self__, "timed_metadata_pid", timed_metadata_pid)
        if video_pid is not None:
            pulumi.set(__self__, "video_pid", video_pid)

    @property
    @pulumi.getter(name="audioPids")
    def audio_pids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "audio_pids")

    @audio_pids.setter
    def audio_pids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "audio_pids", value)

    @property
    @pulumi.getter(name="dvbSubPids")
    def dvb_sub_pids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "dvb_sub_pids")

    @dvb_sub_pids.setter
    def dvb_sub_pids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "dvb_sub_pids", value)

    @property
    @pulumi.getter(name="dvbTeletextPid")
    def dvb_teletext_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "dvb_teletext_pid")

    @dvb_teletext_pid.setter
    def dvb_teletext_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dvb_teletext_pid", value)

    @property
    @pulumi.getter(name="etvPlatformPid")
    def etv_platform_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "etv_platform_pid")

    @etv_platform_pid.setter
    def etv_platform_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "etv_platform_pid", value)

    @property
    @pulumi.getter(name="etvSignalPid")
    def etv_signal_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "etv_signal_pid")

    @etv_signal_pid.setter
    def etv_signal_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "etv_signal_pid", value)

    @property
    @pulumi.getter(name="klvDataPids")
    def klv_data_pids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "klv_data_pids")

    @klv_data_pids.setter
    def klv_data_pids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "klv_data_pids", value)

    @property
    @pulumi.getter(name="pcrPid")
    def pcr_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "pcr_pid")

    @pcr_pid.setter
    def pcr_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pcr_pid", value)

    @property
    @pulumi.getter(name="pmtPid")
    def pmt_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "pmt_pid")

    @pmt_pid.setter
    def pmt_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pmt_pid", value)

    @property
    @pulumi.getter(name="privateMetadataPid")
    def private_metadata_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "private_metadata_pid")

    @private_metadata_pid.setter
    def private_metadata_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "private_metadata_pid", value)

    @property
    @pulumi.getter(name="scte27Pids")
    def scte27_pids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "scte27_pids")

    @scte27_pids.setter
    def scte27_pids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "scte27_pids", value)

    @property
    @pulumi.getter(name="scte35Pid")
    def scte35_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "scte35_pid")

    @scte35_pid.setter
    def scte35_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scte35_pid", value)

    @property
    @pulumi.getter(name="timedMetadataPid")
    def timed_metadata_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "timed_metadata_pid")

    @timed_metadata_pid.setter
    def timed_metadata_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timed_metadata_pid", value)

    @property
    @pulumi.getter(name="videoPid")
    def video_pid(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "video_pid")

    @video_pid.setter
    def video_pid(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "video_pid", value)


@pulumi.input_type
class MultiplexprogramMultiplexProgramPipelineDetailArgs:
    def __init__(__self__, *,
                 active_channel_pipeline: Optional[pulumi.Input[str]] = None,
                 pipeline_id: Optional[pulumi.Input[str]] = None):
        """
        The current source for one of the pipelines in the multiplex.
        :param pulumi.Input[str] active_channel_pipeline: Identifies the channel pipeline that is currently active for the pipeline (identified by PipelineId) in the multiplex.
        :param pulumi.Input[str] pipeline_id: Identifies a specific pipeline in the multiplex.
        """
        if active_channel_pipeline is not None:
            pulumi.set(__self__, "active_channel_pipeline", active_channel_pipeline)
        if pipeline_id is not None:
            pulumi.set(__self__, "pipeline_id", pipeline_id)

    @property
    @pulumi.getter(name="activeChannelPipeline")
    def active_channel_pipeline(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies the channel pipeline that is currently active for the pipeline (identified by PipelineId) in the multiplex.
        """
        return pulumi.get(self, "active_channel_pipeline")

    @active_channel_pipeline.setter
    def active_channel_pipeline(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "active_channel_pipeline", value)

    @property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifies a specific pipeline in the multiplex.
        """
        return pulumi.get(self, "pipeline_id")

    @pipeline_id.setter
    def pipeline_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_id", value)


@pulumi.input_type
class MultiplexprogramMultiplexProgramServiceDescriptorArgs:
    def __init__(__self__, *,
                 provider_name: pulumi.Input[str],
                 service_name: pulumi.Input[str]):
        """
        Transport stream service descriptor configuration for the Multiplex program.
        :param pulumi.Input[str] provider_name: Name of the provider.
        :param pulumi.Input[str] service_name: Name of the service.
        """
        pulumi.set(__self__, "provider_name", provider_name)
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> pulumi.Input[str]:
        """
        Name of the provider.
        """
        return pulumi.get(self, "provider_name")

    @provider_name.setter
    def provider_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        Name of the service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)


@pulumi.input_type
class MultiplexprogramMultiplexProgramSettingsArgs:
    def __init__(__self__, *,
                 program_number: pulumi.Input[int],
                 preferred_channel_pipeline: Optional[pulumi.Input['MultiplexprogramPreferredChannelPipeline']] = None,
                 service_descriptor: Optional[pulumi.Input['MultiplexprogramMultiplexProgramServiceDescriptorArgs']] = None,
                 video_settings: Optional[pulumi.Input['MultiplexprogramMultiplexVideoSettingsArgs']] = None):
        """
        Multiplex Program settings configuration.
        :param pulumi.Input[int] program_number: Unique program number.
        :param pulumi.Input['MultiplexprogramPreferredChannelPipeline'] preferred_channel_pipeline: Indicates which pipeline is preferred by the multiplex for program ingest.
        :param pulumi.Input['MultiplexprogramMultiplexProgramServiceDescriptorArgs'] service_descriptor: Transport stream service descriptor configuration for the Multiplex program.
        :param pulumi.Input['MultiplexprogramMultiplexVideoSettingsArgs'] video_settings: Program video settings configuration.
        """
        pulumi.set(__self__, "program_number", program_number)
        if preferred_channel_pipeline is not None:
            pulumi.set(__self__, "preferred_channel_pipeline", preferred_channel_pipeline)
        if service_descriptor is not None:
            pulumi.set(__self__, "service_descriptor", service_descriptor)
        if video_settings is not None:
            pulumi.set(__self__, "video_settings", video_settings)

    @property
    @pulumi.getter(name="programNumber")
    def program_number(self) -> pulumi.Input[int]:
        """
        Unique program number.
        """
        return pulumi.get(self, "program_number")

    @program_number.setter
    def program_number(self, value: pulumi.Input[int]):
        pulumi.set(self, "program_number", value)

    @property
    @pulumi.getter(name="preferredChannelPipeline")
    def preferred_channel_pipeline(self) -> Optional[pulumi.Input['MultiplexprogramPreferredChannelPipeline']]:
        """
        Indicates which pipeline is preferred by the multiplex for program ingest.
        """
        return pulumi.get(self, "preferred_channel_pipeline")

    @preferred_channel_pipeline.setter
    def preferred_channel_pipeline(self, value: Optional[pulumi.Input['MultiplexprogramPreferredChannelPipeline']]):
        pulumi.set(self, "preferred_channel_pipeline", value)

    @property
    @pulumi.getter(name="serviceDescriptor")
    def service_descriptor(self) -> Optional[pulumi.Input['MultiplexprogramMultiplexProgramServiceDescriptorArgs']]:
        """
        Transport stream service descriptor configuration for the Multiplex program.
        """
        return pulumi.get(self, "service_descriptor")

    @service_descriptor.setter
    def service_descriptor(self, value: Optional[pulumi.Input['MultiplexprogramMultiplexProgramServiceDescriptorArgs']]):
        pulumi.set(self, "service_descriptor", value)

    @property
    @pulumi.getter(name="videoSettings")
    def video_settings(self) -> Optional[pulumi.Input['MultiplexprogramMultiplexVideoSettingsArgs']]:
        """
        Program video settings configuration.
        """
        return pulumi.get(self, "video_settings")

    @video_settings.setter
    def video_settings(self, value: Optional[pulumi.Input['MultiplexprogramMultiplexVideoSettingsArgs']]):
        pulumi.set(self, "video_settings", value)


@pulumi.input_type
class MultiplexprogramMultiplexVideoSettingsArgs:
    def __init__(__self__):
        """
        The video configuration for each program in a multiplex.
        """
        pass


