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
from ._inputs import *

__all__ = ['CapacityReservationFleetArgs', 'CapacityReservationFleet']

@pulumi.input_type
class CapacityReservationFleetArgs:
    def __init__(__self__, *,
                 allocation_strategy: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 instance_match_criteria: Optional[pulumi.Input['CapacityReservationFleetInstanceMatchCriteria']] = None,
                 instance_type_specifications: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationFleetInstanceTypeSpecificationArgs']]]] = None,
                 no_remove_end_date: Optional[pulumi.Input[bool]] = None,
                 remove_end_date: Optional[pulumi.Input[bool]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationFleetTagSpecificationArgs']]]] = None,
                 tenancy: Optional[pulumi.Input['CapacityReservationFleetTenancy']] = None,
                 total_target_capacity: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a CapacityReservationFleet resource.
        :param pulumi.Input[str] allocation_strategy: The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently, only the `prioritized` allocation strategy is supported. For more information, see [Allocation strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy) in the *Amazon EC2 User Guide* .
               
               Valid values: `prioritized`
        :param pulumi.Input[str] end_date: The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to `expired` and all of the Capacity Reservations in the Fleet expire.
               
               The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify `5/31/2019` , `13:30:55` , the Capacity Reservation Fleet is guaranteed to expire between `13:30:55` and `14:30:55` on `5/31/2019` .
        :param pulumi.Input['CapacityReservationFleetInstanceMatchCriteria'] instance_match_criteria: Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.
               
               Currently, Capacity Reservation Fleets support `open` instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.
        :param pulumi.Input[Sequence[pulumi.Input['CapacityReservationFleetInstanceTypeSpecificationArgs']]] instance_type_specifications: Information about the instance types for which to reserve the capacity.
        :param pulumi.Input[bool] no_remove_end_date: Used to add an end date to a Capacity Reservation Fleet that has no end date and time. To add an end date to a Capacity Reservation Fleet, specify `true` for this paramater and specify the end date and time (in UTC time format) for the *EndDate* parameter.
        :param pulumi.Input[bool] remove_end_date: Used to remove an end date from a Capacity Reservation Fleet that is configured to end automatically at a specific date and time. To remove the end date from a Capacity Reservation Fleet, specify `true` for this paramater and omit the *EndDate* parameter.
        :param pulumi.Input[Sequence[pulumi.Input['CapacityReservationFleetTagSpecificationArgs']]] tag_specifications: The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations in the Fleet.
        :param pulumi.Input['CapacityReservationFleetTenancy'] tenancy: Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. The Capacity Reservation Fleet can have one of the following tenancy settings:
               
               - `default` - The Capacity Reservation Fleet is created on hardware that is shared with other AWS accounts .
               - `dedicated` - The Capacity Reservations are created on single-tenant hardware that is dedicated to a single AWS account .
        :param pulumi.Input[int] total_target_capacity: The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see [Total target capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity) in the *Amazon EC2 User Guide* .
        """
        if allocation_strategy is not None:
            pulumi.set(__self__, "allocation_strategy", allocation_strategy)
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)
        if instance_match_criteria is not None:
            pulumi.set(__self__, "instance_match_criteria", instance_match_criteria)
        if instance_type_specifications is not None:
            pulumi.set(__self__, "instance_type_specifications", instance_type_specifications)
        if no_remove_end_date is not None:
            pulumi.set(__self__, "no_remove_end_date", no_remove_end_date)
        if remove_end_date is not None:
            pulumi.set(__self__, "remove_end_date", remove_end_date)
        if tag_specifications is not None:
            pulumi.set(__self__, "tag_specifications", tag_specifications)
        if tenancy is not None:
            pulumi.set(__self__, "tenancy", tenancy)
        if total_target_capacity is not None:
            pulumi.set(__self__, "total_target_capacity", total_target_capacity)

    @property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> Optional[pulumi.Input[str]]:
        """
        The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently, only the `prioritized` allocation strategy is supported. For more information, see [Allocation strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy) in the *Amazon EC2 User Guide* .

        Valid values: `prioritized`
        """
        return pulumi.get(self, "allocation_strategy")

    @allocation_strategy.setter
    def allocation_strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allocation_strategy", value)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to `expired` and all of the Capacity Reservations in the Fleet expire.

        The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify `5/31/2019` , `13:30:55` , the Capacity Reservation Fleet is guaranteed to expire between `13:30:55` and `14:30:55` on `5/31/2019` .
        """
        return pulumi.get(self, "end_date")

    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date", value)

    @property
    @pulumi.getter(name="instanceMatchCriteria")
    def instance_match_criteria(self) -> Optional[pulumi.Input['CapacityReservationFleetInstanceMatchCriteria']]:
        """
        Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.

        Currently, Capacity Reservation Fleets support `open` instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.
        """
        return pulumi.get(self, "instance_match_criteria")

    @instance_match_criteria.setter
    def instance_match_criteria(self, value: Optional[pulumi.Input['CapacityReservationFleetInstanceMatchCriteria']]):
        pulumi.set(self, "instance_match_criteria", value)

    @property
    @pulumi.getter(name="instanceTypeSpecifications")
    def instance_type_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationFleetInstanceTypeSpecificationArgs']]]]:
        """
        Information about the instance types for which to reserve the capacity.
        """
        return pulumi.get(self, "instance_type_specifications")

    @instance_type_specifications.setter
    def instance_type_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationFleetInstanceTypeSpecificationArgs']]]]):
        pulumi.set(self, "instance_type_specifications", value)

    @property
    @pulumi.getter(name="noRemoveEndDate")
    def no_remove_end_date(self) -> Optional[pulumi.Input[bool]]:
        """
        Used to add an end date to a Capacity Reservation Fleet that has no end date and time. To add an end date to a Capacity Reservation Fleet, specify `true` for this paramater and specify the end date and time (in UTC time format) for the *EndDate* parameter.
        """
        return pulumi.get(self, "no_remove_end_date")

    @no_remove_end_date.setter
    def no_remove_end_date(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "no_remove_end_date", value)

    @property
    @pulumi.getter(name="removeEndDate")
    def remove_end_date(self) -> Optional[pulumi.Input[bool]]:
        """
        Used to remove an end date from a Capacity Reservation Fleet that is configured to end automatically at a specific date and time. To remove the end date from a Capacity Reservation Fleet, specify `true` for this paramater and omit the *EndDate* parameter.
        """
        return pulumi.get(self, "remove_end_date")

    @remove_end_date.setter
    def remove_end_date(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_end_date", value)

    @property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationFleetTagSpecificationArgs']]]]:
        """
        The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations in the Fleet.
        """
        return pulumi.get(self, "tag_specifications")

    @tag_specifications.setter
    def tag_specifications(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CapacityReservationFleetTagSpecificationArgs']]]]):
        pulumi.set(self, "tag_specifications", value)

    @property
    @pulumi.getter
    def tenancy(self) -> Optional[pulumi.Input['CapacityReservationFleetTenancy']]:
        """
        Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. The Capacity Reservation Fleet can have one of the following tenancy settings:

        - `default` - The Capacity Reservation Fleet is created on hardware that is shared with other AWS accounts .
        - `dedicated` - The Capacity Reservations are created on single-tenant hardware that is dedicated to a single AWS account .
        """
        return pulumi.get(self, "tenancy")

    @tenancy.setter
    def tenancy(self, value: Optional[pulumi.Input['CapacityReservationFleetTenancy']]):
        pulumi.set(self, "tenancy", value)

    @property
    @pulumi.getter(name="totalTargetCapacity")
    def total_target_capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see [Total target capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity) in the *Amazon EC2 User Guide* .
        """
        return pulumi.get(self, "total_target_capacity")

    @total_target_capacity.setter
    def total_target_capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "total_target_capacity", value)


class CapacityReservationFleet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_strategy: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 instance_match_criteria: Optional[pulumi.Input['CapacityReservationFleetInstanceMatchCriteria']] = None,
                 instance_type_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationFleetInstanceTypeSpecificationArgs']]]]] = None,
                 no_remove_end_date: Optional[pulumi.Input[bool]] = None,
                 remove_end_date: Optional[pulumi.Input[bool]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationFleetTagSpecificationArgs']]]]] = None,
                 tenancy: Optional[pulumi.Input['CapacityReservationFleetTenancy']] = None,
                 total_target_capacity: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::CapacityReservationFleet

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        ec2_capacity_reservation_fleet_canary = aws_native.ec2.CapacityReservationFleet("ec2CapacityReservationFleetCanary",
            allocation_strategy="prioritized",
            instance_type_specifications=[
                aws_native.ec2.CapacityReservationFleetInstanceTypeSpecificationArgs(
                    instance_type="c4.large",
                    instance_platform="Linux/UNIX",
                    availability_zone="us-east-1a",
                    weight=1,
                    priority=1,
                ),
                aws_native.ec2.CapacityReservationFleetInstanceTypeSpecificationArgs(
                    instance_type="c5.large",
                    instance_platform="Linux/UNIX",
                    availability_zone="us-east-1a",
                    weight=1,
                    priority=2,
                ),
            ],
            tenancy=aws_native.ec2.CapacityReservationFleetTenancy.DEFAULT,
            total_target_capacity=2,
            instance_match_criteria=aws_native.ec2.CapacityReservationFleetInstanceMatchCriteria.OPEN)

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] allocation_strategy: The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently, only the `prioritized` allocation strategy is supported. For more information, see [Allocation strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy) in the *Amazon EC2 User Guide* .
               
               Valid values: `prioritized`
        :param pulumi.Input[str] end_date: The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to `expired` and all of the Capacity Reservations in the Fleet expire.
               
               The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify `5/31/2019` , `13:30:55` , the Capacity Reservation Fleet is guaranteed to expire between `13:30:55` and `14:30:55` on `5/31/2019` .
        :param pulumi.Input['CapacityReservationFleetInstanceMatchCriteria'] instance_match_criteria: Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.
               
               Currently, Capacity Reservation Fleets support `open` instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationFleetInstanceTypeSpecificationArgs']]]] instance_type_specifications: Information about the instance types for which to reserve the capacity.
        :param pulumi.Input[bool] no_remove_end_date: Used to add an end date to a Capacity Reservation Fleet that has no end date and time. To add an end date to a Capacity Reservation Fleet, specify `true` for this paramater and specify the end date and time (in UTC time format) for the *EndDate* parameter.
        :param pulumi.Input[bool] remove_end_date: Used to remove an end date from a Capacity Reservation Fleet that is configured to end automatically at a specific date and time. To remove the end date from a Capacity Reservation Fleet, specify `true` for this paramater and omit the *EndDate* parameter.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationFleetTagSpecificationArgs']]]] tag_specifications: The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations in the Fleet.
        :param pulumi.Input['CapacityReservationFleetTenancy'] tenancy: Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. The Capacity Reservation Fleet can have one of the following tenancy settings:
               
               - `default` - The Capacity Reservation Fleet is created on hardware that is shared with other AWS accounts .
               - `dedicated` - The Capacity Reservations are created on single-tenant hardware that is dedicated to a single AWS account .
        :param pulumi.Input[int] total_target_capacity: The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see [Total target capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity) in the *Amazon EC2 User Guide* .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CapacityReservationFleetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::CapacityReservationFleet

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        ec2_capacity_reservation_fleet_canary = aws_native.ec2.CapacityReservationFleet("ec2CapacityReservationFleetCanary",
            allocation_strategy="prioritized",
            instance_type_specifications=[
                aws_native.ec2.CapacityReservationFleetInstanceTypeSpecificationArgs(
                    instance_type="c4.large",
                    instance_platform="Linux/UNIX",
                    availability_zone="us-east-1a",
                    weight=1,
                    priority=1,
                ),
                aws_native.ec2.CapacityReservationFleetInstanceTypeSpecificationArgs(
                    instance_type="c5.large",
                    instance_platform="Linux/UNIX",
                    availability_zone="us-east-1a",
                    weight=1,
                    priority=2,
                ),
            ],
            tenancy=aws_native.ec2.CapacityReservationFleetTenancy.DEFAULT,
            total_target_capacity=2,
            instance_match_criteria=aws_native.ec2.CapacityReservationFleetInstanceMatchCriteria.OPEN)

        ```

        :param str resource_name: The name of the resource.
        :param CapacityReservationFleetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CapacityReservationFleetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allocation_strategy: Optional[pulumi.Input[str]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 instance_match_criteria: Optional[pulumi.Input['CapacityReservationFleetInstanceMatchCriteria']] = None,
                 instance_type_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationFleetInstanceTypeSpecificationArgs']]]]] = None,
                 no_remove_end_date: Optional[pulumi.Input[bool]] = None,
                 remove_end_date: Optional[pulumi.Input[bool]] = None,
                 tag_specifications: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CapacityReservationFleetTagSpecificationArgs']]]]] = None,
                 tenancy: Optional[pulumi.Input['CapacityReservationFleetTenancy']] = None,
                 total_target_capacity: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CapacityReservationFleetArgs.__new__(CapacityReservationFleetArgs)

            __props__.__dict__["allocation_strategy"] = allocation_strategy
            __props__.__dict__["end_date"] = end_date
            __props__.__dict__["instance_match_criteria"] = instance_match_criteria
            __props__.__dict__["instance_type_specifications"] = instance_type_specifications
            __props__.__dict__["no_remove_end_date"] = no_remove_end_date
            __props__.__dict__["remove_end_date"] = remove_end_date
            __props__.__dict__["tag_specifications"] = tag_specifications
            __props__.__dict__["tenancy"] = tenancy
            __props__.__dict__["total_target_capacity"] = total_target_capacity
            __props__.__dict__["capacity_reservation_fleet_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["allocationStrategy", "endDate", "instanceMatchCriteria", "instanceTypeSpecifications[*]", "tagSpecifications[*]", "tenancy"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(CapacityReservationFleet, __self__).__init__(
            'aws-native:ec2:CapacityReservationFleet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CapacityReservationFleet':
        """
        Get an existing CapacityReservationFleet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CapacityReservationFleetArgs.__new__(CapacityReservationFleetArgs)

        __props__.__dict__["allocation_strategy"] = None
        __props__.__dict__["capacity_reservation_fleet_id"] = None
        __props__.__dict__["end_date"] = None
        __props__.__dict__["instance_match_criteria"] = None
        __props__.__dict__["instance_type_specifications"] = None
        __props__.__dict__["no_remove_end_date"] = None
        __props__.__dict__["remove_end_date"] = None
        __props__.__dict__["tag_specifications"] = None
        __props__.__dict__["tenancy"] = None
        __props__.__dict__["total_target_capacity"] = None
        return CapacityReservationFleet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allocationStrategy")
    def allocation_strategy(self) -> pulumi.Output[Optional[str]]:
        """
        The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently, only the `prioritized` allocation strategy is supported. For more information, see [Allocation strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy) in the *Amazon EC2 User Guide* .

        Valid values: `prioritized`
        """
        return pulumi.get(self, "allocation_strategy")

    @property
    @pulumi.getter(name="capacityReservationFleetId")
    def capacity_reservation_fleet_id(self) -> pulumi.Output[str]:
        """
        The ID of the Capacity Reservation Fleet.
        """
        return pulumi.get(self, "capacity_reservation_fleet_id")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[str]]:
        """
        The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to `expired` and all of the Capacity Reservations in the Fleet expire.

        The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify `5/31/2019` , `13:30:55` , the Capacity Reservation Fleet is guaranteed to expire between `13:30:55` and `14:30:55` on `5/31/2019` .
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter(name="instanceMatchCriteria")
    def instance_match_criteria(self) -> pulumi.Output[Optional['CapacityReservationFleetInstanceMatchCriteria']]:
        """
        Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.

        Currently, Capacity Reservation Fleets support `open` instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.
        """
        return pulumi.get(self, "instance_match_criteria")

    @property
    @pulumi.getter(name="instanceTypeSpecifications")
    def instance_type_specifications(self) -> pulumi.Output[Optional[Sequence['outputs.CapacityReservationFleetInstanceTypeSpecification']]]:
        """
        Information about the instance types for which to reserve the capacity.
        """
        return pulumi.get(self, "instance_type_specifications")

    @property
    @pulumi.getter(name="noRemoveEndDate")
    def no_remove_end_date(self) -> pulumi.Output[Optional[bool]]:
        """
        Used to add an end date to a Capacity Reservation Fleet that has no end date and time. To add an end date to a Capacity Reservation Fleet, specify `true` for this paramater and specify the end date and time (in UTC time format) for the *EndDate* parameter.
        """
        return pulumi.get(self, "no_remove_end_date")

    @property
    @pulumi.getter(name="removeEndDate")
    def remove_end_date(self) -> pulumi.Output[Optional[bool]]:
        """
        Used to remove an end date from a Capacity Reservation Fleet that is configured to end automatically at a specific date and time. To remove the end date from a Capacity Reservation Fleet, specify `true` for this paramater and omit the *EndDate* parameter.
        """
        return pulumi.get(self, "remove_end_date")

    @property
    @pulumi.getter(name="tagSpecifications")
    def tag_specifications(self) -> pulumi.Output[Optional[Sequence['outputs.CapacityReservationFleetTagSpecification']]]:
        """
        The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations in the Fleet.
        """
        return pulumi.get(self, "tag_specifications")

    @property
    @pulumi.getter
    def tenancy(self) -> pulumi.Output[Optional['CapacityReservationFleetTenancy']]:
        """
        Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. The Capacity Reservation Fleet can have one of the following tenancy settings:

        - `default` - The Capacity Reservation Fleet is created on hardware that is shared with other AWS accounts .
        - `dedicated` - The Capacity Reservations are created on single-tenant hardware that is dedicated to a single AWS account .
        """
        return pulumi.get(self, "tenancy")

    @property
    @pulumi.getter(name="totalTargetCapacity")
    def total_target_capacity(self) -> pulumi.Output[Optional[int]]:
        """
        The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see [Total target capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity) in the *Amazon EC2 User Guide* .
        """
        return pulumi.get(self, "total_target_capacity")

