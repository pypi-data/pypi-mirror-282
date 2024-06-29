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
    'ExecutionPlanCapacityUnitsConfiguration',
]

@pulumi.output_type
class ExecutionPlanCapacityUnitsConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "rescoreCapacityUnits":
            suggest = "rescore_capacity_units"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ExecutionPlanCapacityUnitsConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ExecutionPlanCapacityUnitsConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ExecutionPlanCapacityUnitsConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 rescore_capacity_units: int):
        """
        :param int rescore_capacity_units: The amount of extra capacity for your rescore execution plan.
               
               A single extra capacity unit for a rescore execution plan provides 0.01 rescore requests per second. You can add up to 1000 extra capacity units.
        """
        pulumi.set(__self__, "rescore_capacity_units", rescore_capacity_units)

    @property
    @pulumi.getter(name="rescoreCapacityUnits")
    def rescore_capacity_units(self) -> int:
        """
        The amount of extra capacity for your rescore execution plan.

        A single extra capacity unit for a rescore execution plan provides 0.01 rescore requests per second. You can add up to 1000 extra capacity units.
        """
        return pulumi.get(self, "rescore_capacity_units")


