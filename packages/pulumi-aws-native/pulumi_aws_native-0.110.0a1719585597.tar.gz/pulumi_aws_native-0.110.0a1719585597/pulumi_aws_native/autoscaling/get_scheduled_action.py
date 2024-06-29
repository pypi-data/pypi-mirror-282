# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetScheduledActionResult',
    'AwaitableGetScheduledActionResult',
    'get_scheduled_action',
    'get_scheduled_action_output',
]

@pulumi.output_type
class GetScheduledActionResult:
    def __init__(__self__, desired_capacity=None, end_time=None, max_size=None, min_size=None, recurrence=None, scheduled_action_name=None, start_time=None, time_zone=None):
        if desired_capacity and not isinstance(desired_capacity, int):
            raise TypeError("Expected argument 'desired_capacity' to be a int")
        pulumi.set(__self__, "desired_capacity", desired_capacity)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if max_size and not isinstance(max_size, int):
            raise TypeError("Expected argument 'max_size' to be a int")
        pulumi.set(__self__, "max_size", max_size)
        if min_size and not isinstance(min_size, int):
            raise TypeError("Expected argument 'min_size' to be a int")
        pulumi.set(__self__, "min_size", min_size)
        if recurrence and not isinstance(recurrence, str):
            raise TypeError("Expected argument 'recurrence' to be a str")
        pulumi.set(__self__, "recurrence", recurrence)
        if scheduled_action_name and not isinstance(scheduled_action_name, str):
            raise TypeError("Expected argument 'scheduled_action_name' to be a str")
        pulumi.set(__self__, "scheduled_action_name", scheduled_action_name)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="desiredCapacity")
    def desired_capacity(self) -> Optional[int]:
        """
        The desired capacity is the initial capacity of the Auto Scaling group after the scheduled action runs and the capacity it attempts to maintain.
        """
        return pulumi.get(self, "desired_capacity")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[str]:
        """
        The latest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[int]:
        """
        The minimum size of the Auto Scaling group.
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[int]:
        """
        The minimum size of the Auto Scaling group.
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter
    def recurrence(self) -> Optional[str]:
        """
        The recurring schedule for the action, in Unix cron syntax format. When StartTime and EndTime are specified with Recurrence , they form the boundaries of when the recurring action starts and stops.
        """
        return pulumi.get(self, "recurrence")

    @property
    @pulumi.getter(name="scheduledActionName")
    def scheduled_action_name(self) -> Optional[str]:
        """
        Auto-generated unique identifier
        """
        return pulumi.get(self, "scheduled_action_name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[str]:
        """
        The earliest scheduled start time to return. If scheduled action names are provided, this parameter is ignored.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        The time zone for the cron expression.
        """
        return pulumi.get(self, "time_zone")


class AwaitableGetScheduledActionResult(GetScheduledActionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduledActionResult(
            desired_capacity=self.desired_capacity,
            end_time=self.end_time,
            max_size=self.max_size,
            min_size=self.min_size,
            recurrence=self.recurrence,
            scheduled_action_name=self.scheduled_action_name,
            start_time=self.start_time,
            time_zone=self.time_zone)


def get_scheduled_action(auto_scaling_group_name: Optional[str] = None,
                         scheduled_action_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduledActionResult:
    """
    The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.


    :param str auto_scaling_group_name: The name of the Auto Scaling group.
    :param str scheduled_action_name: Auto-generated unique identifier
    """
    __args__ = dict()
    __args__['autoScalingGroupName'] = auto_scaling_group_name
    __args__['scheduledActionName'] = scheduled_action_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:autoscaling:getScheduledAction', __args__, opts=opts, typ=GetScheduledActionResult).value

    return AwaitableGetScheduledActionResult(
        desired_capacity=pulumi.get(__ret__, 'desired_capacity'),
        end_time=pulumi.get(__ret__, 'end_time'),
        max_size=pulumi.get(__ret__, 'max_size'),
        min_size=pulumi.get(__ret__, 'min_size'),
        recurrence=pulumi.get(__ret__, 'recurrence'),
        scheduled_action_name=pulumi.get(__ret__, 'scheduled_action_name'),
        start_time=pulumi.get(__ret__, 'start_time'),
        time_zone=pulumi.get(__ret__, 'time_zone'))


@_utilities.lift_output_func(get_scheduled_action)
def get_scheduled_action_output(auto_scaling_group_name: Optional[pulumi.Input[str]] = None,
                                scheduled_action_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduledActionResult]:
    """
    The AWS::AutoScaling::ScheduledAction resource specifies an Amazon EC2 Auto Scaling scheduled action so that the Auto Scaling group can change the number of instances available for your application in response to predictable load changes.


    :param str auto_scaling_group_name: The name of the Auto Scaling group.
    :param str scheduled_action_name: Auto-generated unique identifier
    """
    ...
