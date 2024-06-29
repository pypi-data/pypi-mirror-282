# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['ThreatIntelSetArgs', 'ThreatIntelSet']

@pulumi.input_type
class ThreatIntelSetArgs:
    def __init__(__self__, *,
                 format: pulumi.Input[str],
                 location: pulumi.Input[str],
                 activate: Optional[pulumi.Input[bool]] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a ThreatIntelSet resource.
        :param pulumi.Input[str] format: The format of the file that contains the ThreatIntelSet.
        :param pulumi.Input[str] location: The URI of the file that contains the ThreatIntelSet.
        :param pulumi.Input[bool] activate: A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        :param pulumi.Input[str] detector_id: The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.
        :param pulumi.Input[str] name: A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags to be added to a new threat list resource. Each tag consists of a key and an optional value, both of which you define.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        pulumi.set(__self__, "format", format)
        pulumi.set(__self__, "location", location)
        if activate is not None:
            pulumi.set(__self__, "activate", activate)
        if detector_id is not None:
            pulumi.set(__self__, "detector_id", detector_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def format(self) -> pulumi.Input[str]:
        """
        The format of the file that contains the ThreatIntelSet.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: pulumi.Input[str]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The URI of the file that contains the ThreatIntelSet.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def activate(self) -> Optional[pulumi.Input[bool]]:
        """
        A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        """
        return pulumi.get(self, "activate")

    @activate.setter
    def activate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "activate", value)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.
        """
        return pulumi.get(self, "detector_id")

    @detector_id.setter
    def detector_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detector_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags to be added to a new threat list resource. Each tag consists of a key and an optional value, both of which you define.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class ThreatIntelSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activate: Optional[pulumi.Input[bool]] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::GuardDuty::ThreatIntelSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] activate: A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        :param pulumi.Input[str] detector_id: The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.
        :param pulumi.Input[str] format: The format of the file that contains the ThreatIntelSet.
        :param pulumi.Input[str] location: The URI of the file that contains the ThreatIntelSet.
        :param pulumi.Input[str] name: A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: The tags to be added to a new threat list resource. Each tag consists of a key and an optional value, both of which you define.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ThreatIntelSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::GuardDuty::ThreatIntelSet

        :param str resource_name: The name of the resource.
        :param ThreatIntelSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ThreatIntelSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 activate: Optional[pulumi.Input[bool]] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ThreatIntelSetArgs.__new__(ThreatIntelSetArgs)

            __props__.__dict__["activate"] = activate
            __props__.__dict__["detector_id"] = detector_id
            if format is None and not opts.urn:
                raise TypeError("Missing required property 'format'")
            __props__.__dict__["format"] = format
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["aws_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["detectorId", "format"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ThreatIntelSet, __self__).__init__(
            'aws-native:guardduty:ThreatIntelSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ThreatIntelSet':
        """
        Get an existing ThreatIntelSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ThreatIntelSetArgs.__new__(ThreatIntelSetArgs)

        __props__.__dict__["activate"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["detector_id"] = None
        __props__.__dict__["format"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return ThreatIntelSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def activate(self) -> pulumi.Output[Optional[bool]]:
        """
        A Boolean value that indicates whether GuardDuty is to start using the uploaded ThreatIntelSet.
        """
        return pulumi.get(self, "activate")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        """
        The unique ID of the `threatIntelSet` .
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[Optional[str]]:
        """
        The unique ID of the detector of the GuardDuty account that you want to create a threatIntelSet for.
        """
        return pulumi.get(self, "detector_id")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[str]:
        """
        The format of the file that contains the ThreatIntelSet.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The URI of the file that contains the ThreatIntelSet.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        A user-friendly ThreatIntelSet name displayed in all findings that are generated by activity that involves IP addresses included in this ThreatIntelSet.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags to be added to a new threat list resource. Each tag consists of a key and an optional value, both of which you define.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) .
        """
        return pulumi.get(self, "tags")

