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
    'GetCapacityReservationResult',
    'AwaitableGetCapacityReservationResult',
    'get_capacity_reservation',
    'get_capacity_reservation_output',
]

@pulumi.output_type
class GetCapacityReservationResult:
    def __init__(__self__, allocated_dpus=None, arn=None, capacity_assignment_configuration=None, creation_time=None, last_successful_allocation_time=None, status=None, tags=None, target_dpus=None):
        if allocated_dpus and not isinstance(allocated_dpus, int):
            raise TypeError("Expected argument 'allocated_dpus' to be a int")
        pulumi.set(__self__, "allocated_dpus", allocated_dpus)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if capacity_assignment_configuration and not isinstance(capacity_assignment_configuration, dict):
            raise TypeError("Expected argument 'capacity_assignment_configuration' to be a dict")
        pulumi.set(__self__, "capacity_assignment_configuration", capacity_assignment_configuration)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if last_successful_allocation_time and not isinstance(last_successful_allocation_time, str):
            raise TypeError("Expected argument 'last_successful_allocation_time' to be a str")
        pulumi.set(__self__, "last_successful_allocation_time", last_successful_allocation_time)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if target_dpus and not isinstance(target_dpus, int):
            raise TypeError("Expected argument 'target_dpus' to be a int")
        pulumi.set(__self__, "target_dpus", target_dpus)

    @property
    @pulumi.getter(name="allocatedDpus")
    def allocated_dpus(self) -> Optional[int]:
        """
        The number of DPUs Athena has provisioned and allocated for the reservation
        """
        return pulumi.get(self, "allocated_dpus")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the capacity reservation.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="capacityAssignmentConfiguration")
    def capacity_assignment_configuration(self) -> Optional['outputs.CapacityReservationCapacityAssignmentConfiguration']:
        """
        Assigns Athena workgroups (and hence their queries) to capacity reservations. A capacity reservation can have only one capacity assignment configuration, but the capacity assignment configuration can be made up of multiple individual assignments. Each assignment specifies how Athena queries can consume capacity from the capacity reservation that their workgroup is mapped to.
        """
        return pulumi.get(self, "capacity_assignment_configuration")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        The date and time the reservation was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="lastSuccessfulAllocationTime")
    def last_successful_allocation_time(self) -> Optional[str]:
        """
        The timestamp when the last successful allocated was made
        """
        return pulumi.get(self, "last_successful_allocation_time")

    @property
    @pulumi.getter
    def status(self) -> Optional['CapacityReservationStatus']:
        """
        The status of the reservation.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetDpus")
    def target_dpus(self) -> Optional[int]:
        """
        The number of DPUs to request to be allocated to the reservation.
        """
        return pulumi.get(self, "target_dpus")


class AwaitableGetCapacityReservationResult(GetCapacityReservationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCapacityReservationResult(
            allocated_dpus=self.allocated_dpus,
            arn=self.arn,
            capacity_assignment_configuration=self.capacity_assignment_configuration,
            creation_time=self.creation_time,
            last_successful_allocation_time=self.last_successful_allocation_time,
            status=self.status,
            tags=self.tags,
            target_dpus=self.target_dpus)


def get_capacity_reservation(arn: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCapacityReservationResult:
    """
    Resource schema for AWS::Athena::CapacityReservation


    :param str arn: The ARN of the capacity reservation.
    """
    __args__ = dict()
    __args__['arn'] = arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:athena:getCapacityReservation', __args__, opts=opts, typ=GetCapacityReservationResult).value

    return AwaitableGetCapacityReservationResult(
        allocated_dpus=pulumi.get(__ret__, 'allocated_dpus'),
        arn=pulumi.get(__ret__, 'arn'),
        capacity_assignment_configuration=pulumi.get(__ret__, 'capacity_assignment_configuration'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        last_successful_allocation_time=pulumi.get(__ret__, 'last_successful_allocation_time'),
        status=pulumi.get(__ret__, 'status'),
        tags=pulumi.get(__ret__, 'tags'),
        target_dpus=pulumi.get(__ret__, 'target_dpus'))


@_utilities.lift_output_func(get_capacity_reservation)
def get_capacity_reservation_output(arn: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCapacityReservationResult]:
    """
    Resource schema for AWS::Athena::CapacityReservation


    :param str arn: The ARN of the capacity reservation.
    """
    ...
