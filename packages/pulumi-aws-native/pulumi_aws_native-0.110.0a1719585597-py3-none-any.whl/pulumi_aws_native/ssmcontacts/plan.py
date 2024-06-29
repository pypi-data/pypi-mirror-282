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
from ._inputs import *

__all__ = ['PlanArgs', 'Plan']

@pulumi.input_type
class PlanArgs:
    def __init__(__self__, *,
                 contact_id: Optional[pulumi.Input[str]] = None,
                 rotation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 stages: Optional[pulumi.Input[Sequence[pulumi.Input['PlanStageArgs']]]] = None):
        """
        The set of arguments for constructing a Plan resource.
        :param pulumi.Input[str] contact_id: Contact ID for the AWS SSM Incident Manager Contact to associate the plan.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rotation_ids: Rotation Ids to associate with Oncall Contact for engagement.
        :param pulumi.Input[Sequence[pulumi.Input['PlanStageArgs']]] stages: The stages that an escalation plan or engagement plan engages contacts and contact methods in.
        """
        if contact_id is not None:
            pulumi.set(__self__, "contact_id", contact_id)
        if rotation_ids is not None:
            pulumi.set(__self__, "rotation_ids", rotation_ids)
        if stages is not None:
            pulumi.set(__self__, "stages", stages)

    @property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> Optional[pulumi.Input[str]]:
        """
        Contact ID for the AWS SSM Incident Manager Contact to associate the plan.
        """
        return pulumi.get(self, "contact_id")

    @contact_id.setter
    def contact_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_id", value)

    @property
    @pulumi.getter(name="rotationIds")
    def rotation_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Rotation Ids to associate with Oncall Contact for engagement.
        """
        return pulumi.get(self, "rotation_ids")

    @rotation_ids.setter
    def rotation_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "rotation_ids", value)

    @property
    @pulumi.getter
    def stages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PlanStageArgs']]]]:
        """
        The stages that an escalation plan or engagement plan engages contacts and contact methods in.
        """
        return pulumi.get(self, "stages")

    @stages.setter
    def stages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PlanStageArgs']]]]):
        pulumi.set(self, "stages", value)


class Plan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_id: Optional[pulumi.Input[str]] = None,
                 rotation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 stages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PlanStageArgs']]]]] = None,
                 __props__=None):
        """
        Engagement Plan for a SSM Incident Manager Contact.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] contact_id: Contact ID for the AWS SSM Incident Manager Contact to associate the plan.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] rotation_ids: Rotation Ids to associate with Oncall Contact for engagement.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PlanStageArgs']]]] stages: The stages that an escalation plan or engagement plan engages contacts and contact methods in.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PlanArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Engagement Plan for a SSM Incident Manager Contact.

        :param str resource_name: The name of the resource.
        :param PlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_id: Optional[pulumi.Input[str]] = None,
                 rotation_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 stages: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PlanStageArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PlanArgs.__new__(PlanArgs)

            __props__.__dict__["contact_id"] = contact_id
            __props__.__dict__["rotation_ids"] = rotation_ids
            __props__.__dict__["stages"] = stages
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["contactId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Plan, __self__).__init__(
            'aws-native:ssmcontacts:Plan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Plan':
        """
        Get an existing Plan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PlanArgs.__new__(PlanArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["contact_id"] = None
        __props__.__dict__["rotation_ids"] = None
        __props__.__dict__["stages"] = None
        return Plan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the contact.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> pulumi.Output[Optional[str]]:
        """
        Contact ID for the AWS SSM Incident Manager Contact to associate the plan.
        """
        return pulumi.get(self, "contact_id")

    @property
    @pulumi.getter(name="rotationIds")
    def rotation_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Rotation Ids to associate with Oncall Contact for engagement.
        """
        return pulumi.get(self, "rotation_ids")

    @property
    @pulumi.getter
    def stages(self) -> pulumi.Output[Optional[Sequence['outputs.PlanStage']]]:
        """
        The stages that an escalation plan or engagement plan engages contacts and contact methods in.
        """
        return pulumi.get(self, "stages")

