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
    'GetDetectorResult',
    'AwaitableGetDetectorResult',
    'get_detector',
    'get_detector_output',
]

@pulumi.output_type
class GetDetectorResult:
    def __init__(__self__, arn=None, associated_models=None, created_time=None, description=None, detector_version_id=None, detector_version_status=None, event_type=None, last_updated_time=None, rule_execution_mode=None, rules=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if associated_models and not isinstance(associated_models, list):
            raise TypeError("Expected argument 'associated_models' to be a list")
        pulumi.set(__self__, "associated_models", associated_models)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if detector_version_id and not isinstance(detector_version_id, str):
            raise TypeError("Expected argument 'detector_version_id' to be a str")
        pulumi.set(__self__, "detector_version_id", detector_version_id)
        if detector_version_status and not isinstance(detector_version_status, str):
            raise TypeError("Expected argument 'detector_version_status' to be a str")
        pulumi.set(__self__, "detector_version_status", detector_version_status)
        if event_type and not isinstance(event_type, dict):
            raise TypeError("Expected argument 'event_type' to be a dict")
        pulumi.set(__self__, "event_type", event_type)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if rule_execution_mode and not isinstance(rule_execution_mode, str):
            raise TypeError("Expected argument 'rule_execution_mode' to be a str")
        pulumi.set(__self__, "rule_execution_mode", rule_execution_mode)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the detector.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associatedModels")
    def associated_models(self) -> Optional[Sequence['outputs.DetectorModel']]:
        """
        The models to associate with this detector.
        """
        return pulumi.get(self, "associated_models")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        The time when the detector was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the detector.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detectorVersionId")
    def detector_version_id(self) -> Optional[str]:
        """
        The active version ID of the detector
        """
        return pulumi.get(self, "detector_version_id")

    @property
    @pulumi.getter(name="detectorVersionStatus")
    def detector_version_status(self) -> Optional['DetectorVersionStatus']:
        """
        The desired detector version status for the detector
        """
        return pulumi.get(self, "detector_version_status")

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> Optional['outputs.DetectorEventType']:
        """
        The event type to associate this detector with.
        """
        return pulumi.get(self, "event_type")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        The time when the detector was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="ruleExecutionMode")
    def rule_execution_mode(self) -> Optional['DetectorRuleExecutionMode']:
        """
        The rule execution mode for the rules included in the detector version.

        Valid values: `FIRST_MATCHED | ALL_MATCHED` Default value: `FIRST_MATCHED`

        You can define and edit the rule mode at the detector version level, when it is in draft status.

        If you specify `FIRST_MATCHED` , Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.

        If you specifiy `ALL_MATCHED` , Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules.
        """
        return pulumi.get(self, "rule_execution_mode")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.DetectorRule']]:
        """
        The rules to include in the detector version.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Tags associated with this detector.
        """
        return pulumi.get(self, "tags")


class AwaitableGetDetectorResult(GetDetectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDetectorResult(
            arn=self.arn,
            associated_models=self.associated_models,
            created_time=self.created_time,
            description=self.description,
            detector_version_id=self.detector_version_id,
            detector_version_status=self.detector_version_status,
            event_type=self.event_type,
            last_updated_time=self.last_updated_time,
            rule_execution_mode=self.rule_execution_mode,
            rules=self.rules,
            tags=self.tags)


def get_detector(arn: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDetectorResult:
    """
    A resource schema for a Detector in Amazon Fraud Detector.


    :param str arn: The ARN of the detector.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:frauddetector:getDetector', __args__, opts=opts, typ=GetDetectorResult).value

    return AwaitableGetDetectorResult(
        arn=pulumi.get(__ret__, 'arn'),
        associated_models=pulumi.get(__ret__, 'associated_models'),
        created_time=pulumi.get(__ret__, 'created_time'),
        description=pulumi.get(__ret__, 'description'),
        detector_version_id=pulumi.get(__ret__, 'detector_version_id'),
        detector_version_status=pulumi.get(__ret__, 'detector_version_status'),
        event_type=pulumi.get(__ret__, 'event_type'),
        last_updated_time=pulumi.get(__ret__, 'last_updated_time'),
        rule_execution_mode=pulumi.get(__ret__, 'rule_execution_mode'),
        rules=pulumi.get(__ret__, 'rules'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_detector)
def get_detector_output(arn: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDetectorResult]:
    """
    A resource schema for a Detector in Amazon Fraud Detector.


    :param str arn: The ARN of the detector.
    """
    ...
