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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._enums import *
from ._inputs import *

__all__ = ['UserProfileArgs', 'UserProfile']

@pulumi.input_type
class UserProfileArgs:
    def __init__(__self__, *,
                 domain_id: pulumi.Input[str],
                 single_sign_on_user_identifier: Optional[pulumi.Input[str]] = None,
                 single_sign_on_user_value: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]] = None,
                 user_profile_name: Optional[pulumi.Input[str]] = None,
                 user_settings: Optional[pulumi.Input['UserProfileUserSettingsArgs']] = None):
        """
        The set of arguments for constructing a UserProfile resource.
        :param pulumi.Input[str] domain_id: The ID of the associated Domain.
        :param pulumi.Input[str] single_sign_on_user_identifier: A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
        :param pulumi.Input[str] single_sign_on_user_value: The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]] tags: A list of tags to apply to the user profile.
        :param pulumi.Input[str] user_profile_name: A name for the UserProfile.
        :param pulumi.Input['UserProfileUserSettingsArgs'] user_settings: A collection of settings.
        """
        pulumi.set(__self__, "domain_id", domain_id)
        if single_sign_on_user_identifier is not None:
            pulumi.set(__self__, "single_sign_on_user_identifier", single_sign_on_user_identifier)
        if single_sign_on_user_value is not None:
            pulumi.set(__self__, "single_sign_on_user_value", single_sign_on_user_value)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_profile_name is not None:
            pulumi.set(__self__, "user_profile_name", user_profile_name)
        if user_settings is not None:
            pulumi.set(__self__, "user_settings", user_settings)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Input[str]:
        """
        The ID of the associated Domain.
        """
        return pulumi.get(self, "domain_id")

    @domain_id.setter
    def domain_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_id", value)

    @property
    @pulumi.getter(name="singleSignOnUserIdentifier")
    def single_sign_on_user_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
        """
        return pulumi.get(self, "single_sign_on_user_identifier")

    @single_sign_on_user_identifier.setter
    def single_sign_on_user_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "single_sign_on_user_identifier", value)

    @property
    @pulumi.getter(name="singleSignOnUserValue")
    def single_sign_on_user_value(self) -> Optional[pulumi.Input[str]]:
        """
        The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
        """
        return pulumi.get(self, "single_sign_on_user_value")

    @single_sign_on_user_value.setter
    def single_sign_on_user_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "single_sign_on_user_value", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]]:
        """
        A list of tags to apply to the user profile.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.CreateOnlyTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        A name for the UserProfile.
        """
        return pulumi.get(self, "user_profile_name")

    @user_profile_name.setter
    def user_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_profile_name", value)

    @property
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> Optional[pulumi.Input['UserProfileUserSettingsArgs']]:
        """
        A collection of settings.
        """
        return pulumi.get(self, "user_settings")

    @user_settings.setter
    def user_settings(self, value: Optional[pulumi.Input['UserProfileUserSettingsArgs']]):
        pulumi.set(self, "user_settings", value)


class UserProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 single_sign_on_user_identifier: Optional[pulumi.Input[str]] = None,
                 single_sign_on_user_value: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]]] = None,
                 user_profile_name: Optional[pulumi.Input[str]] = None,
                 user_settings: Optional[pulumi.Input[pulumi.InputType['UserProfileUserSettingsArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::UserProfile

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_id: The ID of the associated Domain.
        :param pulumi.Input[str] single_sign_on_user_identifier: A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
        :param pulumi.Input[str] single_sign_on_user_value: The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]] tags: A list of tags to apply to the user profile.
        :param pulumi.Input[str] user_profile_name: A name for the UserProfile.
        :param pulumi.Input[pulumi.InputType['UserProfileUserSettingsArgs']] user_settings: A collection of settings.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::UserProfile

        :param str resource_name: The name of the resource.
        :param UserProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 single_sign_on_user_identifier: Optional[pulumi.Input[str]] = None,
                 single_sign_on_user_value: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.CreateOnlyTagArgs']]]]] = None,
                 user_profile_name: Optional[pulumi.Input[str]] = None,
                 user_settings: Optional[pulumi.Input[pulumi.InputType['UserProfileUserSettingsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserProfileArgs.__new__(UserProfileArgs)

            if domain_id is None and not opts.urn:
                raise TypeError("Missing required property 'domain_id'")
            __props__.__dict__["domain_id"] = domain_id
            __props__.__dict__["single_sign_on_user_identifier"] = single_sign_on_user_identifier
            __props__.__dict__["single_sign_on_user_value"] = single_sign_on_user_value
            __props__.__dict__["tags"] = tags
            __props__.__dict__["user_profile_name"] = user_profile_name
            __props__.__dict__["user_settings"] = user_settings
            __props__.__dict__["user_profile_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domainId", "singleSignOnUserIdentifier", "singleSignOnUserValue", "tags[*]", "userProfileName", "userSettings.rStudioServerProAppSettings.accessStatus", "userSettings.rStudioServerProAppSettings.userGroup"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(UserProfile, __self__).__init__(
            'aws-native:sagemaker:UserProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserProfile':
        """
        Get an existing UserProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserProfileArgs.__new__(UserProfileArgs)

        __props__.__dict__["domain_id"] = None
        __props__.__dict__["single_sign_on_user_identifier"] = None
        __props__.__dict__["single_sign_on_user_value"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_profile_arn"] = None
        __props__.__dict__["user_profile_name"] = None
        __props__.__dict__["user_settings"] = None
        return UserProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        The ID of the associated Domain.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter(name="singleSignOnUserIdentifier")
    def single_sign_on_user_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.
        """
        return pulumi.get(self, "single_sign_on_user_identifier")

    @property
    @pulumi.getter(name="singleSignOnUserValue")
    def single_sign_on_user_value(self) -> pulumi.Output[Optional[str]]:
        """
        The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.
        """
        return pulumi.get(self, "single_sign_on_user_value")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.CreateOnlyTag']]]:
        """
        A list of tags to apply to the user profile.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userProfileArn")
    def user_profile_arn(self) -> pulumi.Output[str]:
        """
        The user profile Amazon Resource Name (ARN).
        """
        return pulumi.get(self, "user_profile_arn")

    @property
    @pulumi.getter(name="userProfileName")
    def user_profile_name(self) -> pulumi.Output[str]:
        """
        A name for the UserProfile.
        """
        return pulumi.get(self, "user_profile_name")

    @property
    @pulumi.getter(name="userSettings")
    def user_settings(self) -> pulumi.Output[Optional['outputs.UserProfileUserSettings']]:
        """
        A collection of settings.
        """
        return pulumi.get(self, "user_settings")

