# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetGeofenceCollectionResult',
    'AwaitableGetGeofenceCollectionResult',
    'get_geofence_collection',
    'get_geofence_collection_output',
]

@pulumi.output_type
class GetGeofenceCollectionResult:
    def __init__(__self__, arn=None, collection_arn=None, create_time=None, description=None, pricing_plan=None, pricing_plan_data_source=None, tags=None, update_time=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if collection_arn and not isinstance(collection_arn, str):
            raise TypeError("Expected argument 'collection_arn' to be a str")
        pulumi.set(__self__, "collection_arn", collection_arn)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if pricing_plan and not isinstance(pricing_plan, str):
            raise TypeError("Expected argument 'pricing_plan' to be a str")
        pulumi.set(__self__, "pricing_plan", pricing_plan)
        if pricing_plan_data_source and not isinstance(pricing_plan_data_source, str):
            raise TypeError("Expected argument 'pricing_plan_data_source' to be a str")
        pulumi.set(__self__, "pricing_plan_data_source", pricing_plan_data_source)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all AWS .

        - Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection`
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="collectionArn")
    def collection_arn(self) -> Optional[str]:
        """
        Synonym for `Arn` . The Amazon Resource Name (ARN) for the geofence collection resource. Used when you need to specify a resource across all AWS .

        - Format example: `arn:aws:geo:region:account-id:geofence-collection/ExampleGeofenceCollection`
        """
        return pulumi.get(self, "collection_arn")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[str]:
        """
        The timestamp for when the geofence collection resource was created in [ISO 8601](https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        An optional description for the geofence collection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> Optional['GeofenceCollectionPricingPlan']:
        return pulumi.get(self, "pricing_plan")

    @property
    @pulumi.getter(name="pricingPlanDataSource")
    def pricing_plan_data_source(self) -> Optional[str]:
        """
        This shape is deprecated since 2022-02-01: Deprecated. No longer allowed.
        """
        return pulumi.get(self, "pricing_plan_data_source")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[str]:
        """
        The timestamp for when the geofence collection resource was last updated in [ISO 8601](https://docs.aws.amazon.com/https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sssZ` .
        """
        return pulumi.get(self, "update_time")


class AwaitableGetGeofenceCollectionResult(GetGeofenceCollectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGeofenceCollectionResult(
            arn=self.arn,
            collection_arn=self.collection_arn,
            create_time=self.create_time,
            description=self.description,
            pricing_plan=self.pricing_plan,
            pricing_plan_data_source=self.pricing_plan_data_source,
            tags=self.tags,
            update_time=self.update_time)


def get_geofence_collection(collection_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGeofenceCollectionResult:
    """
    Definition of AWS::Location::GeofenceCollection Resource Type


    :param str collection_name: A custom name for the geofence collection.
           
           Requirements:
           
           - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).
           - Must be a unique geofence collection name.
           - No spaces allowed. For example, `ExampleGeofenceCollection` .
    """
    __args__ = dict()
    __args__['collectionName'] = collection_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:location:getGeofenceCollection', __args__, opts=opts, typ=GetGeofenceCollectionResult).value

    return AwaitableGetGeofenceCollectionResult(
        arn=pulumi.get(__ret__, 'arn'),
        collection_arn=pulumi.get(__ret__, 'collection_arn'),
        create_time=pulumi.get(__ret__, 'create_time'),
        description=pulumi.get(__ret__, 'description'),
        pricing_plan=pulumi.get(__ret__, 'pricing_plan'),
        pricing_plan_data_source=pulumi.get(__ret__, 'pricing_plan_data_source'),
        tags=pulumi.get(__ret__, 'tags'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_geofence_collection)
def get_geofence_collection_output(collection_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGeofenceCollectionResult]:
    """
    Definition of AWS::Location::GeofenceCollection Resource Type


    :param str collection_name: A custom name for the geofence collection.
           
           Requirements:
           
           - Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).
           - Must be a unique geofence collection name.
           - No spaces allowed. For example, `ExampleGeofenceCollection` .
    """
    ...
