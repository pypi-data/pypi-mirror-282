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
    'AgentPermissionsProperties',
    'ProfilingGroupChannel',
]

@pulumi.output_type
class AgentPermissionsProperties(dict):
    """
    The agent permissions attached to this profiling group.
    """
    def __init__(__self__, *,
                 principals: Sequence[str]):
        """
        The agent permissions attached to this profiling group.
        :param Sequence[str] principals: The principals for the agent permissions.
        """
        pulumi.set(__self__, "principals", principals)

    @property
    @pulumi.getter
    def principals(self) -> Sequence[str]:
        """
        The principals for the agent permissions.
        """
        return pulumi.get(self, "principals")


@pulumi.output_type
class ProfilingGroupChannel(dict):
    """
    Notification medium for users to get alerted for events that occur in application profile. We support SNS topic as a notification channel.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "channelUri":
            suggest = "channel_uri"
        elif key == "channelId":
            suggest = "channel_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProfilingGroupChannel. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProfilingGroupChannel.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProfilingGroupChannel.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 channel_uri: str,
                 channel_id: Optional[str] = None):
        """
        Notification medium for users to get alerted for events that occur in application profile. We support SNS topic as a notification channel.
        :param str channel_uri: The channel URI.
        :param str channel_id: The channel ID.
        """
        pulumi.set(__self__, "channel_uri", channel_uri)
        if channel_id is not None:
            pulumi.set(__self__, "channel_id", channel_id)

    @property
    @pulumi.getter(name="channelUri")
    def channel_uri(self) -> str:
        """
        The channel URI.
        """
        return pulumi.get(self, "channel_uri")

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[str]:
        """
        The channel ID.
        """
        return pulumi.get(self, "channel_id")


