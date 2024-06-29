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
    'GetPredefinedAttributeResult',
    'AwaitableGetPredefinedAttributeResult',
    'get_predefined_attribute',
    'get_predefined_attribute_output',
]

@pulumi.output_type
class GetPredefinedAttributeResult:
    def __init__(__self__, last_modified_region=None, last_modified_time=None, values=None):
        if last_modified_region and not isinstance(last_modified_region, str):
            raise TypeError("Expected argument 'last_modified_region' to be a str")
        pulumi.set(__self__, "last_modified_region", last_modified_region)
        if last_modified_time and not isinstance(last_modified_time, float):
            raise TypeError("Expected argument 'last_modified_time' to be a float")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if values and not isinstance(values, dict):
            raise TypeError("Expected argument 'values' to be a dict")
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter(name="lastModifiedRegion")
    def last_modified_region(self) -> Optional[str]:
        """
        Last modified region.
        """
        return pulumi.get(self, "last_modified_region")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[float]:
        """
        Last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def values(self) -> Optional['outputs.ValuesProperties']:
        """
        The values of a predefined attribute.
        """
        return pulumi.get(self, "values")


class AwaitableGetPredefinedAttributeResult(GetPredefinedAttributeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPredefinedAttributeResult(
            last_modified_region=self.last_modified_region,
            last_modified_time=self.last_modified_time,
            values=self.values)


def get_predefined_attribute(instance_arn: Optional[str] = None,
                             name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPredefinedAttributeResult:
    """
    Resource Type definition for AWS::Connect::PredefinedAttribute


    :param str instance_arn: The identifier of the Amazon Connect instance.
    :param str name: The name of the predefined attribute.
    """
    __args__ = dict()
    __args__['instanceArn'] = instance_arn
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:connect:getPredefinedAttribute', __args__, opts=opts, typ=GetPredefinedAttributeResult).value

    return AwaitableGetPredefinedAttributeResult(
        last_modified_region=pulumi.get(__ret__, 'last_modified_region'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        values=pulumi.get(__ret__, 'values'))


@_utilities.lift_output_func(get_predefined_attribute)
def get_predefined_attribute_output(instance_arn: Optional[pulumi.Input[str]] = None,
                                    name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPredefinedAttributeResult]:
    """
    Resource Type definition for AWS::Connect::PredefinedAttribute


    :param str instance_arn: The identifier of the Amazon Connect instance.
    :param str name: The name of the predefined attribute.
    """
    ...
