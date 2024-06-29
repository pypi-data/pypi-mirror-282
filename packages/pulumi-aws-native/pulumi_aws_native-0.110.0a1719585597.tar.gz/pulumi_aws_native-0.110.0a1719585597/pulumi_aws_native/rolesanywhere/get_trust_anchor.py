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
    'GetTrustAnchorResult',
    'AwaitableGetTrustAnchorResult',
    'get_trust_anchor',
    'get_trust_anchor_output',
]

@pulumi.output_type
class GetTrustAnchorResult:
    def __init__(__self__, enabled=None, name=None, notification_settings=None, source=None, tags=None, trust_anchor_arn=None, trust_anchor_id=None):
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notification_settings and not isinstance(notification_settings, list):
            raise TypeError("Expected argument 'notification_settings' to be a list")
        pulumi.set(__self__, "notification_settings", notification_settings)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if trust_anchor_arn and not isinstance(trust_anchor_arn, str):
            raise TypeError("Expected argument 'trust_anchor_arn' to be a str")
        pulumi.set(__self__, "trust_anchor_arn", trust_anchor_arn)
        if trust_anchor_id and not isinstance(trust_anchor_id, str):
            raise TypeError("Expected argument 'trust_anchor_id' to be a str")
        pulumi.set(__self__, "trust_anchor_id", trust_anchor_id)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Indicates whether the trust anchor is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the trust anchor.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationSettings")
    def notification_settings(self) -> Optional[Sequence['outputs.TrustAnchorNotificationSetting']]:
        """
        A list of notification settings to be associated to the trust anchor.
        """
        return pulumi.get(self, "notification_settings")

    @property
    @pulumi.getter
    def source(self) -> Optional['outputs.TrustAnchorSource']:
        """
        The trust anchor type and its related certificate data.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        The tags to attach to the trust anchor.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustAnchorArn")
    def trust_anchor_arn(self) -> Optional[str]:
        """
        The ARN of the trust anchor.
        """
        return pulumi.get(self, "trust_anchor_arn")

    @property
    @pulumi.getter(name="trustAnchorId")
    def trust_anchor_id(self) -> Optional[str]:
        """
        The unique identifier of the trust anchor.
        """
        return pulumi.get(self, "trust_anchor_id")


class AwaitableGetTrustAnchorResult(GetTrustAnchorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrustAnchorResult(
            enabled=self.enabled,
            name=self.name,
            notification_settings=self.notification_settings,
            source=self.source,
            tags=self.tags,
            trust_anchor_arn=self.trust_anchor_arn,
            trust_anchor_id=self.trust_anchor_id)


def get_trust_anchor(trust_anchor_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrustAnchorResult:
    """
    Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.


    :param str trust_anchor_id: The unique identifier of the trust anchor.
    """
    __args__ = dict()
    __args__['trustAnchorId'] = trust_anchor_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:rolesanywhere:getTrustAnchor', __args__, opts=opts, typ=GetTrustAnchorResult).value

    return AwaitableGetTrustAnchorResult(
        enabled=pulumi.get(__ret__, 'enabled'),
        name=pulumi.get(__ret__, 'name'),
        notification_settings=pulumi.get(__ret__, 'notification_settings'),
        source=pulumi.get(__ret__, 'source'),
        tags=pulumi.get(__ret__, 'tags'),
        trust_anchor_arn=pulumi.get(__ret__, 'trust_anchor_arn'),
        trust_anchor_id=pulumi.get(__ret__, 'trust_anchor_id'))


@_utilities.lift_output_func(get_trust_anchor)
def get_trust_anchor_output(trust_anchor_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrustAnchorResult]:
    """
    Definition of AWS::RolesAnywhere::TrustAnchor Resource Type.


    :param str trust_anchor_id: The unique identifier of the trust anchor.
    """
    ...
