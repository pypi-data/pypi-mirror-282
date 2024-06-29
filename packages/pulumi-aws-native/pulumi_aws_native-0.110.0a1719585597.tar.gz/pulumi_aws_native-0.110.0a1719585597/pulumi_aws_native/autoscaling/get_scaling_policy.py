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

__all__ = [
    'GetScalingPolicyResult',
    'AwaitableGetScalingPolicyResult',
    'get_scaling_policy',
    'get_scaling_policy_output',
]

@pulumi.output_type
class GetScalingPolicyResult:
    def __init__(__self__, adjustment_type=None, arn=None, cooldown=None, estimated_instance_warmup=None, metric_aggregation_type=None, min_adjustment_magnitude=None, policy_name=None, policy_type=None, predictive_scaling_configuration=None, scaling_adjustment=None, step_adjustments=None, target_tracking_configuration=None):
        if adjustment_type and not isinstance(adjustment_type, str):
            raise TypeError("Expected argument 'adjustment_type' to be a str")
        pulumi.set(__self__, "adjustment_type", adjustment_type)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if cooldown and not isinstance(cooldown, str):
            raise TypeError("Expected argument 'cooldown' to be a str")
        pulumi.set(__self__, "cooldown", cooldown)
        if estimated_instance_warmup and not isinstance(estimated_instance_warmup, int):
            raise TypeError("Expected argument 'estimated_instance_warmup' to be a int")
        pulumi.set(__self__, "estimated_instance_warmup", estimated_instance_warmup)
        if metric_aggregation_type and not isinstance(metric_aggregation_type, str):
            raise TypeError("Expected argument 'metric_aggregation_type' to be a str")
        pulumi.set(__self__, "metric_aggregation_type", metric_aggregation_type)
        if min_adjustment_magnitude and not isinstance(min_adjustment_magnitude, int):
            raise TypeError("Expected argument 'min_adjustment_magnitude' to be a int")
        pulumi.set(__self__, "min_adjustment_magnitude", min_adjustment_magnitude)
        if policy_name and not isinstance(policy_name, str):
            raise TypeError("Expected argument 'policy_name' to be a str")
        pulumi.set(__self__, "policy_name", policy_name)
        if policy_type and not isinstance(policy_type, str):
            raise TypeError("Expected argument 'policy_type' to be a str")
        pulumi.set(__self__, "policy_type", policy_type)
        if predictive_scaling_configuration and not isinstance(predictive_scaling_configuration, dict):
            raise TypeError("Expected argument 'predictive_scaling_configuration' to be a dict")
        pulumi.set(__self__, "predictive_scaling_configuration", predictive_scaling_configuration)
        if scaling_adjustment and not isinstance(scaling_adjustment, int):
            raise TypeError("Expected argument 'scaling_adjustment' to be a int")
        pulumi.set(__self__, "scaling_adjustment", scaling_adjustment)
        if step_adjustments and not isinstance(step_adjustments, list):
            raise TypeError("Expected argument 'step_adjustments' to be a list")
        pulumi.set(__self__, "step_adjustments", step_adjustments)
        if target_tracking_configuration and not isinstance(target_tracking_configuration, dict):
            raise TypeError("Expected argument 'target_tracking_configuration' to be a dict")
        pulumi.set(__self__, "target_tracking_configuration", target_tracking_configuration)

    @property
    @pulumi.getter(name="adjustmentType")
    def adjustment_type(self) -> Optional[str]:
        """
        Specifies how the scaling adjustment is interpreted. The valid values are ChangeInCapacity, ExactCapacity, and PercentChangeInCapacity.
        """
        return pulumi.get(self, "adjustment_type")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the AutoScaling scaling policy
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def cooldown(self) -> Optional[str]:
        """
        The duration of the policy's cooldown period, in seconds. When a cooldown period is specified here, it overrides the default cooldown period defined for the Auto Scaling group.
        """
        return pulumi.get(self, "cooldown")

    @property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[int]:
        """
        The estimated time, in seconds, until a newly launched instance can contribute to the CloudWatch metrics. If not provided, the default is to use the value from the default cooldown period for the Auto Scaling group. Valid only if the policy type is TargetTrackingScaling or StepScaling.
        """
        return pulumi.get(self, "estimated_instance_warmup")

    @property
    @pulumi.getter(name="metricAggregationType")
    def metric_aggregation_type(self) -> Optional[str]:
        """
        The aggregation type for the CloudWatch metrics. The valid values are Minimum, Maximum, and Average. If the aggregation type is null, the value is treated as Average. Valid only if the policy type is StepScaling.
        """
        return pulumi.get(self, "metric_aggregation_type")

    @property
    @pulumi.getter(name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> Optional[int]:
        """
        The minimum value to scale by when the adjustment type is PercentChangeInCapacity. For example, suppose that you create a step scaling policy to scale out an Auto Scaling group by 25 percent and you specify a MinAdjustmentMagnitude of 2. If the group has 4 instances and the scaling policy is performed, 25 percent of 4 is 1. However, because you specified a MinAdjustmentMagnitude of 2, Amazon EC2 Auto Scaling scales out the group by 2 instances.
        """
        return pulumi.get(self, "min_adjustment_magnitude")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[str]:
        """
        Returns the name of a scaling policy.
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[str]:
        """
        One of the following policy types: TargetTrackingScaling, StepScaling, SimpleScaling (default), PredictiveScaling
        """
        return pulumi.get(self, "policy_type")

    @property
    @pulumi.getter(name="predictiveScalingConfiguration")
    def predictive_scaling_configuration(self) -> Optional['outputs.ScalingPolicyPredictiveScalingConfiguration']:
        """
        A predictive scaling policy. Includes support for predefined metrics only.
        """
        return pulumi.get(self, "predictive_scaling_configuration")

    @property
    @pulumi.getter(name="scalingAdjustment")
    def scaling_adjustment(self) -> Optional[int]:
        """
        The amount by which to scale, based on the specified adjustment type. A positive value adds to the current capacity while a negative number removes from the current capacity. For exact capacity, you must specify a positive value. Required if the policy type is SimpleScaling. (Not used with any other policy type.)
        """
        return pulumi.get(self, "scaling_adjustment")

    @property
    @pulumi.getter(name="stepAdjustments")
    def step_adjustments(self) -> Optional[Sequence['outputs.ScalingPolicyStepAdjustment']]:
        """
        A set of adjustments that enable you to scale based on the size of the alarm breach. Required if the policy type is StepScaling. (Not used with any other policy type.)
        """
        return pulumi.get(self, "step_adjustments")

    @property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> Optional['outputs.ScalingPolicyTargetTrackingConfiguration']:
        """
        A target tracking scaling policy. Includes support for predefined or customized metrics.
        """
        return pulumi.get(self, "target_tracking_configuration")


class AwaitableGetScalingPolicyResult(GetScalingPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScalingPolicyResult(
            adjustment_type=self.adjustment_type,
            arn=self.arn,
            cooldown=self.cooldown,
            estimated_instance_warmup=self.estimated_instance_warmup,
            metric_aggregation_type=self.metric_aggregation_type,
            min_adjustment_magnitude=self.min_adjustment_magnitude,
            policy_name=self.policy_name,
            policy_type=self.policy_type,
            predictive_scaling_configuration=self.predictive_scaling_configuration,
            scaling_adjustment=self.scaling_adjustment,
            step_adjustments=self.step_adjustments,
            target_tracking_configuration=self.target_tracking_configuration)


def get_scaling_policy(arn: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScalingPolicyResult:
    """
    The AWS::AutoScaling::ScalingPolicy resource specifies an Amazon EC2 Auto Scaling scaling policy so that the Auto Scaling group can scale the number of instances available for your application.


    :param str arn: The ARN of the AutoScaling scaling policy
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:autoscaling:getScalingPolicy', __args__, opts=opts, typ=GetScalingPolicyResult).value

    return AwaitableGetScalingPolicyResult(
        adjustment_type=pulumi.get(__ret__, 'adjustment_type'),
        arn=pulumi.get(__ret__, 'arn'),
        cooldown=pulumi.get(__ret__, 'cooldown'),
        estimated_instance_warmup=pulumi.get(__ret__, 'estimated_instance_warmup'),
        metric_aggregation_type=pulumi.get(__ret__, 'metric_aggregation_type'),
        min_adjustment_magnitude=pulumi.get(__ret__, 'min_adjustment_magnitude'),
        policy_name=pulumi.get(__ret__, 'policy_name'),
        policy_type=pulumi.get(__ret__, 'policy_type'),
        predictive_scaling_configuration=pulumi.get(__ret__, 'predictive_scaling_configuration'),
        scaling_adjustment=pulumi.get(__ret__, 'scaling_adjustment'),
        step_adjustments=pulumi.get(__ret__, 'step_adjustments'),
        target_tracking_configuration=pulumi.get(__ret__, 'target_tracking_configuration'))


@_utilities.lift_output_func(get_scaling_policy)
def get_scaling_policy_output(arn: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScalingPolicyResult]:
    """
    The AWS::AutoScaling::ScalingPolicy resource specifies an Amazon EC2 Auto Scaling scaling policy so that the Auto Scaling group can scale the number of instances available for your application.


    :param str arn: The ARN of the AutoScaling scaling policy
    """
    ...
