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
from ._enums import *

__all__ = ['ProfileArgs', 'Profile']

@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *,
                 as2_id: pulumi.Input[str],
                 profile_type: pulumi.Input['ProfileType'],
                 certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Profile resource.
        :param pulumi.Input[str] as2_id: AS2 identifier agreed with a trading partner.
        :param pulumi.Input['ProfileType'] profile_type: Enum specifying whether the profile is local or associated with a trading partner.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] certificate_ids: List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "as2_id", as2_id)
        pulumi.set(__self__, "profile_type", profile_type)
        if certificate_ids is not None:
            pulumi.set(__self__, "certificate_ids", certificate_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="as2Id")
    def as2_id(self) -> pulumi.Input[str]:
        """
        AS2 identifier agreed with a trading partner.
        """
        return pulumi.get(self, "as2_id")

    @as2_id.setter
    def as2_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "as2_id", value)

    @property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> pulumi.Input['ProfileType']:
        """
        Enum specifying whether the profile is local or associated with a trading partner.
        """
        return pulumi.get(self, "profile_type")

    @profile_type.setter
    def profile_type(self, value: pulumi.Input['ProfileType']):
        pulumi.set(self, "profile_type", value)

    @property
    @pulumi.getter(name="certificateIds")
    def certificate_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
        """
        return pulumi.get(self, "certificate_ids")

    @certificate_ids.setter
    def certificate_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "certificate_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Profile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 as2_id: Optional[pulumi.Input[str]] = None,
                 certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 profile_type: Optional[pulumi.Input['ProfileType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Transfer::Profile

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] as2_id: AS2 identifier agreed with a trading partner.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] certificate_ids: List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
        :param pulumi.Input['ProfileType'] profile_type: Enum specifying whether the profile is local or associated with a trading partner.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Transfer::Profile

        :param str resource_name: The name of the resource.
        :param ProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 as2_id: Optional[pulumi.Input[str]] = None,
                 certificate_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 profile_type: Optional[pulumi.Input['ProfileType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfileArgs.__new__(ProfileArgs)

            if as2_id is None and not opts.urn:
                raise TypeError("Missing required property 'as2_id'")
            __props__.__dict__["as2_id"] = as2_id
            __props__.__dict__["certificate_ids"] = certificate_ids
            if profile_type is None and not opts.urn:
                raise TypeError("Missing required property 'profile_type'")
            __props__.__dict__["profile_type"] = profile_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["profile_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["profileType"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Profile, __self__).__init__(
            'aws-native:transfer:Profile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Profile':
        """
        Get an existing Profile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProfileArgs.__new__(ProfileArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["as2_id"] = None
        __props__.__dict__["certificate_ids"] = None
        __props__.__dict__["profile_id"] = None
        __props__.__dict__["profile_type"] = None
        __props__.__dict__["tags"] = None
        return Profile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Specifies the unique Amazon Resource Name (ARN) for the profile.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="as2Id")
    def as2_id(self) -> pulumi.Output[str]:
        """
        AS2 identifier agreed with a trading partner.
        """
        return pulumi.get(self, "as2_id")

    @property
    @pulumi.getter(name="certificateIds")
    def certificate_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.
        """
        return pulumi.get(self, "certificate_ids")

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> pulumi.Output[str]:
        """
        A unique identifier for the profile
        """
        return pulumi.get(self, "profile_id")

    @property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> pulumi.Output['ProfileType']:
        """
        Enum specifying whether the profile is local or associated with a trading partner.
        """
        return pulumi.get(self, "profile_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

