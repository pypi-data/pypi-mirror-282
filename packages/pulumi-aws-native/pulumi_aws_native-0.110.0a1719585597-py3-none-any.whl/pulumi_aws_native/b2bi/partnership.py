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

__all__ = ['PartnershipArgs', 'Partnership']

@pulumi.input_type
class PartnershipArgs:
    def __init__(__self__, *,
                 email: pulumi.Input[str],
                 profile_id: pulumi.Input[str],
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Partnership resource.
        :param pulumi.Input[str] profile_id: Returns the unique, system-generated identifier for the profile connected to this partnership.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] capabilities: Returns one or more capabilities associated with this partnership.
        :param pulumi.Input[str] name: Returns the name of the partnership.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.
        """
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "profile_id", profile_id)
        if capabilities is not None:
            pulumi.set(__self__, "capabilities", capabilities)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if phone is not None:
            pulumi.set(__self__, "phone", phone)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> pulumi.Input[str]:
        """
        Returns the unique, system-generated identifier for the profile connected to this partnership.
        """
        return pulumi.get(self, "profile_id")

    @profile_id.setter
    def profile_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_id", value)

    @property
    @pulumi.getter
    def capabilities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Returns one or more capabilities associated with this partnership.
        """
        return pulumi.get(self, "capabilities")

    @capabilities.setter
    def capabilities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "capabilities", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Returns the name of the partnership.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def phone(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "phone")

    @phone.setter
    def phone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Partnership(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 profile_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::B2BI::Partnership Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] capabilities: Returns one or more capabilities associated with this partnership.
        :param pulumi.Input[str] name: Returns the name of the partnership.
        :param pulumi.Input[str] profile_id: Returns the unique, system-generated identifier for the profile connected to this partnership.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PartnershipArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::B2BI::Partnership Resource Type

        :param str resource_name: The name of the resource.
        :param PartnershipArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartnershipArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capabilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 phone: Optional[pulumi.Input[str]] = None,
                 profile_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PartnershipArgs.__new__(PartnershipArgs)

            __props__.__dict__["capabilities"] = capabilities
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            __props__.__dict__["name"] = name
            __props__.__dict__["phone"] = phone
            if profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'profile_id'")
            __props__.__dict__["profile_id"] = profile_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_at"] = None
            __props__.__dict__["modified_at"] = None
            __props__.__dict__["partnership_arn"] = None
            __props__.__dict__["partnership_id"] = None
            __props__.__dict__["trading_partner_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["email", "phone", "profileId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Partnership, __self__).__init__(
            'aws-native:b2bi:Partnership',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Partnership':
        """
        Get an existing Partnership resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PartnershipArgs.__new__(PartnershipArgs)

        __props__.__dict__["capabilities"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["email"] = None
        __props__.__dict__["modified_at"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partnership_arn"] = None
        __props__.__dict__["partnership_id"] = None
        __props__.__dict__["phone"] = None
        __props__.__dict__["profile_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["trading_partner_id"] = None
        return Partnership(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def capabilities(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Returns one or more capabilities associated with this partnership.
        """
        return pulumi.get(self, "capabilities")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Returns a timestamp for creation date and time of the partnership.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> pulumi.Output[str]:
        """
        Returns a timestamp that identifies the most recent date and time that the partnership was modified.
        """
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Returns the name of the partnership.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnershipArn")
    def partnership_arn(self) -> pulumi.Output[str]:
        """
        Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.
        """
        return pulumi.get(self, "partnership_arn")

    @property
    @pulumi.getter(name="partnershipId")
    def partnership_id(self) -> pulumi.Output[str]:
        """
        Returns the unique, system-generated identifier for a partnership.
        """
        return pulumi.get(self, "partnership_id")

    @property
    @pulumi.getter
    def phone(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "phone")

    @property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> pulumi.Output[str]:
        """
        Returns the unique, system-generated identifier for the profile connected to this partnership.
        """
        return pulumi.get(self, "profile_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tradingPartnerId")
    def trading_partner_id(self) -> pulumi.Output[str]:
        """
        Returns the unique, system-generated identifier for a trading partner.
        """
        return pulumi.get(self, "trading_partner_id")

