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

__all__ = [
    'GetFleetMetricResult',
    'AwaitableGetFleetMetricResult',
    'get_fleet_metric',
    'get_fleet_metric_output',
]

@pulumi.output_type
class GetFleetMetricResult:
    def __init__(__self__, aggregation_field=None, aggregation_type=None, creation_date=None, description=None, index_name=None, last_modified_date=None, metric_arn=None, period=None, query_string=None, query_version=None, tags=None, unit=None, version=None):
        if aggregation_field and not isinstance(aggregation_field, str):
            raise TypeError("Expected argument 'aggregation_field' to be a str")
        pulumi.set(__self__, "aggregation_field", aggregation_field)
        if aggregation_type and not isinstance(aggregation_type, dict):
            raise TypeError("Expected argument 'aggregation_type' to be a dict")
        pulumi.set(__self__, "aggregation_type", aggregation_type)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if index_name and not isinstance(index_name, str):
            raise TypeError("Expected argument 'index_name' to be a str")
        pulumi.set(__self__, "index_name", index_name)
        if last_modified_date and not isinstance(last_modified_date, str):
            raise TypeError("Expected argument 'last_modified_date' to be a str")
        pulumi.set(__self__, "last_modified_date", last_modified_date)
        if metric_arn and not isinstance(metric_arn, str):
            raise TypeError("Expected argument 'metric_arn' to be a str")
        pulumi.set(__self__, "metric_arn", metric_arn)
        if period and not isinstance(period, int):
            raise TypeError("Expected argument 'period' to be a int")
        pulumi.set(__self__, "period", period)
        if query_string and not isinstance(query_string, str):
            raise TypeError("Expected argument 'query_string' to be a str")
        pulumi.set(__self__, "query_string", query_string)
        if query_version and not isinstance(query_version, str):
            raise TypeError("Expected argument 'query_version' to be a str")
        pulumi.set(__self__, "query_version", query_version)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if unit and not isinstance(unit, str):
            raise TypeError("Expected argument 'unit' to be a str")
        pulumi.set(__self__, "unit", unit)
        if version and not isinstance(version, float):
            raise TypeError("Expected argument 'version' to be a float")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="aggregationField")
    def aggregation_field(self) -> Optional[str]:
        """
        The aggregation field to perform aggregation and metric emission
        """
        return pulumi.get(self, "aggregation_field")

    @property
    @pulumi.getter(name="aggregationType")
    def aggregation_type(self) -> Optional['outputs.FleetMetricAggregationType']:
        """
        The type of the aggregation query.
        """
        return pulumi.get(self, "aggregation_type")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        """
        The creation date of a fleet metric
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of a fleet metric
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="indexName")
    def index_name(self) -> Optional[str]:
        """
        The index name of a fleet metric
        """
        return pulumi.get(self, "index_name")

    @property
    @pulumi.getter(name="lastModifiedDate")
    def last_modified_date(self) -> Optional[str]:
        """
        The last modified date of a fleet metric
        """
        return pulumi.get(self, "last_modified_date")

    @property
    @pulumi.getter(name="metricArn")
    def metric_arn(self) -> Optional[str]:
        """
        The Amazon Resource Number (ARN) of a fleet metric metric
        """
        return pulumi.get(self, "metric_arn")

    @property
    @pulumi.getter
    def period(self) -> Optional[int]:
        """
        The period of metric emission in seconds
        """
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[str]:
        """
        The Fleet Indexing query used by a fleet metric
        """
        return pulumi.get(self, "query_string")

    @property
    @pulumi.getter(name="queryVersion")
    def query_version(self) -> Optional[str]:
        """
        The version of a Fleet Indexing query used by a fleet metric
        """
        return pulumi.get(self, "query_version")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def unit(self) -> Optional[str]:
        """
        The unit of data points emitted by a fleet metric
        """
        return pulumi.get(self, "unit")

    @property
    @pulumi.getter
    def version(self) -> Optional[float]:
        """
        The version of a fleet metric
        """
        return pulumi.get(self, "version")


class AwaitableGetFleetMetricResult(GetFleetMetricResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFleetMetricResult(
            aggregation_field=self.aggregation_field,
            aggregation_type=self.aggregation_type,
            creation_date=self.creation_date,
            description=self.description,
            index_name=self.index_name,
            last_modified_date=self.last_modified_date,
            metric_arn=self.metric_arn,
            period=self.period,
            query_string=self.query_string,
            query_version=self.query_version,
            tags=self.tags,
            unit=self.unit,
            version=self.version)


def get_fleet_metric(metric_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFleetMetricResult:
    """
    An aggregated metric of certain devices in your fleet


    :param str metric_name: The name of the fleet metric
    """
    __args__ = dict()
    __args__['metricName'] = metric_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getFleetMetric', __args__, opts=opts, typ=GetFleetMetricResult).value

    return AwaitableGetFleetMetricResult(
        aggregation_field=pulumi.get(__ret__, 'aggregation_field'),
        aggregation_type=pulumi.get(__ret__, 'aggregation_type'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        description=pulumi.get(__ret__, 'description'),
        index_name=pulumi.get(__ret__, 'index_name'),
        last_modified_date=pulumi.get(__ret__, 'last_modified_date'),
        metric_arn=pulumi.get(__ret__, 'metric_arn'),
        period=pulumi.get(__ret__, 'period'),
        query_string=pulumi.get(__ret__, 'query_string'),
        query_version=pulumi.get(__ret__, 'query_version'),
        tags=pulumi.get(__ret__, 'tags'),
        unit=pulumi.get(__ret__, 'unit'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_fleet_metric)
def get_fleet_metric_output(metric_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFleetMetricResult]:
    """
    An aggregated metric of certain devices in your fleet


    :param str metric_name: The name of the fleet metric
    """
    ...
