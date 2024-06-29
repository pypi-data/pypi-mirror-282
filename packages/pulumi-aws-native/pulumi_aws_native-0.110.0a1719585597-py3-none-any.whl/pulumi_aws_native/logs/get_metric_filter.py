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
    'GetMetricFilterResult',
    'AwaitableGetMetricFilterResult',
    'get_metric_filter',
    'get_metric_filter_output',
]

@pulumi.output_type
class GetMetricFilterResult:
    def __init__(__self__, filter_pattern=None, metric_transformations=None):
        if filter_pattern and not isinstance(filter_pattern, str):
            raise TypeError("Expected argument 'filter_pattern' to be a str")
        pulumi.set(__self__, "filter_pattern", filter_pattern)
        if metric_transformations and not isinstance(metric_transformations, list):
            raise TypeError("Expected argument 'metric_transformations' to be a list")
        pulumi.set(__self__, "metric_transformations", metric_transformations)

    @property
    @pulumi.getter(name="filterPattern")
    def filter_pattern(self) -> Optional[str]:
        """
        A filter pattern for extracting metric data out of ingested log events. For more information, see [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html).
        """
        return pulumi.get(self, "filter_pattern")

    @property
    @pulumi.getter(name="metricTransformations")
    def metric_transformations(self) -> Optional[Sequence['outputs.MetricFilterMetricTransformation']]:
        """
        The metric transformations.
        """
        return pulumi.get(self, "metric_transformations")


class AwaitableGetMetricFilterResult(GetMetricFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetricFilterResult(
            filter_pattern=self.filter_pattern,
            metric_transformations=self.metric_transformations)


def get_metric_filter(filter_name: Optional[str] = None,
                      log_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetricFilterResult:
    """
    The ``AWS::Logs::MetricFilter`` resource specifies a metric filter that describes how CWL extracts information from logs and transforms it into Amazon CloudWatch metrics. If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.
     The maximum number of metric filters that can be associated with a log group is 100.


    :param str filter_name: The name of the metric filter.
    :param str log_group_name: The name of an existing log group that you want to associate with this metric filter.
    """
    __args__ = dict()
    __args__['filterName'] = filter_name
    __args__['logGroupName'] = log_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:logs:getMetricFilter', __args__, opts=opts, typ=GetMetricFilterResult).value

    return AwaitableGetMetricFilterResult(
        filter_pattern=pulumi.get(__ret__, 'filter_pattern'),
        metric_transformations=pulumi.get(__ret__, 'metric_transformations'))


@_utilities.lift_output_func(get_metric_filter)
def get_metric_filter_output(filter_name: Optional[pulumi.Input[str]] = None,
                             log_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetricFilterResult]:
    """
    The ``AWS::Logs::MetricFilter`` resource specifies a metric filter that describes how CWL extracts information from logs and transforms it into Amazon CloudWatch metrics. If you have multiple metric filters that are associated with a log group, all the filters are applied to the log streams in that group.
     The maximum number of metric filters that can be associated with a log group is 100.


    :param str filter_name: The name of the metric filter.
    :param str log_group_name: The name of an existing log group that you want to associate with this metric filter.
    """
    ...
