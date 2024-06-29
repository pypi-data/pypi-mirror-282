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
from ._inputs import *

__all__ = ['VerifiedAccessTrustProviderArgs', 'VerifiedAccessTrustProvider']

@pulumi.input_type
class VerifiedAccessTrustProviderArgs:
    def __init__(__self__, *,
                 policy_reference_name: pulumi.Input[str],
                 trust_provider_type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 device_options: Optional[pulumi.Input['VerifiedAccessTrustProviderDeviceOptionsArgs']] = None,
                 device_trust_provider_type: Optional[pulumi.Input[str]] = None,
                 oidc_options: Optional[pulumi.Input['VerifiedAccessTrustProviderOidcOptionsArgs']] = None,
                 sse_specification: Optional[pulumi.Input['SseSpecificationPropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 user_trust_provider_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VerifiedAccessTrustProvider resource.
        :param pulumi.Input[str] policy_reference_name: The identifier to be used when working with policy rules.
        :param pulumi.Input[str] trust_provider_type: Type of trust provider. Possible values: user|device
        :param pulumi.Input[str] description: A description for the Amazon Web Services Verified Access trust provider.
        :param pulumi.Input['VerifiedAccessTrustProviderDeviceOptionsArgs'] device_options: The options for device-identity trust provider.
        :param pulumi.Input[str] device_trust_provider_type: The type of device-based trust provider. Possible values: jamf|crowdstrike
        :param pulumi.Input['VerifiedAccessTrustProviderOidcOptionsArgs'] oidc_options: The options for an OpenID Connect-compatible user-identity trust provider.
        :param pulumi.Input['SseSpecificationPropertiesArgs'] sse_specification: The configuration options for customer provided KMS encryption.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] user_trust_provider_type: The type of device-based trust provider. Possible values: oidc|iam-identity-center
        """
        pulumi.set(__self__, "policy_reference_name", policy_reference_name)
        pulumi.set(__self__, "trust_provider_type", trust_provider_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_options is not None:
            pulumi.set(__self__, "device_options", device_options)
        if device_trust_provider_type is not None:
            pulumi.set(__self__, "device_trust_provider_type", device_trust_provider_type)
        if oidc_options is not None:
            pulumi.set(__self__, "oidc_options", oidc_options)
        if sse_specification is not None:
            pulumi.set(__self__, "sse_specification", sse_specification)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_trust_provider_type is not None:
            pulumi.set(__self__, "user_trust_provider_type", user_trust_provider_type)

    @property
    @pulumi.getter(name="policyReferenceName")
    def policy_reference_name(self) -> pulumi.Input[str]:
        """
        The identifier to be used when working with policy rules.
        """
        return pulumi.get(self, "policy_reference_name")

    @policy_reference_name.setter
    def policy_reference_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "policy_reference_name", value)

    @property
    @pulumi.getter(name="trustProviderType")
    def trust_provider_type(self) -> pulumi.Input[str]:
        """
        Type of trust provider. Possible values: user|device
        """
        return pulumi.get(self, "trust_provider_type")

    @trust_provider_type.setter
    def trust_provider_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "trust_provider_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Amazon Web Services Verified Access trust provider.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceOptions")
    def device_options(self) -> Optional[pulumi.Input['VerifiedAccessTrustProviderDeviceOptionsArgs']]:
        """
        The options for device-identity trust provider.
        """
        return pulumi.get(self, "device_options")

    @device_options.setter
    def device_options(self, value: Optional[pulumi.Input['VerifiedAccessTrustProviderDeviceOptionsArgs']]):
        pulumi.set(self, "device_options", value)

    @property
    @pulumi.getter(name="deviceTrustProviderType")
    def device_trust_provider_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of device-based trust provider. Possible values: jamf|crowdstrike
        """
        return pulumi.get(self, "device_trust_provider_type")

    @device_trust_provider_type.setter
    def device_trust_provider_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_trust_provider_type", value)

    @property
    @pulumi.getter(name="oidcOptions")
    def oidc_options(self) -> Optional[pulumi.Input['VerifiedAccessTrustProviderOidcOptionsArgs']]:
        """
        The options for an OpenID Connect-compatible user-identity trust provider.
        """
        return pulumi.get(self, "oidc_options")

    @oidc_options.setter
    def oidc_options(self, value: Optional[pulumi.Input['VerifiedAccessTrustProviderOidcOptionsArgs']]):
        pulumi.set(self, "oidc_options", value)

    @property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> Optional[pulumi.Input['SseSpecificationPropertiesArgs']]:
        """
        The configuration options for customer provided KMS encryption.
        """
        return pulumi.get(self, "sse_specification")

    @sse_specification.setter
    def sse_specification(self, value: Optional[pulumi.Input['SseSpecificationPropertiesArgs']]):
        pulumi.set(self, "sse_specification", value)

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

    @property
    @pulumi.getter(name="userTrustProviderType")
    def user_trust_provider_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of device-based trust provider. Possible values: oidc|iam-identity-center
        """
        return pulumi.get(self, "user_trust_provider_type")

    @user_trust_provider_type.setter
    def user_trust_provider_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_trust_provider_type", value)


class VerifiedAccessTrustProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_options: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessTrustProviderDeviceOptionsArgs']]] = None,
                 device_trust_provider_type: Optional[pulumi.Input[str]] = None,
                 oidc_options: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessTrustProviderOidcOptionsArgs']]] = None,
                 policy_reference_name: Optional[pulumi.Input[str]] = None,
                 sse_specification: Optional[pulumi.Input[pulumi.InputType['SseSpecificationPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 trust_provider_type: Optional[pulumi.Input[str]] = None,
                 user_trust_provider_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description for the Amazon Web Services Verified Access trust provider.
        :param pulumi.Input[pulumi.InputType['VerifiedAccessTrustProviderDeviceOptionsArgs']] device_options: The options for device-identity trust provider.
        :param pulumi.Input[str] device_trust_provider_type: The type of device-based trust provider. Possible values: jamf|crowdstrike
        :param pulumi.Input[pulumi.InputType['VerifiedAccessTrustProviderOidcOptionsArgs']] oidc_options: The options for an OpenID Connect-compatible user-identity trust provider.
        :param pulumi.Input[str] policy_reference_name: The identifier to be used when working with policy rules.
        :param pulumi.Input[pulumi.InputType['SseSpecificationPropertiesArgs']] sse_specification: The configuration options for customer provided KMS encryption.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] trust_provider_type: Type of trust provider. Possible values: user|device
        :param pulumi.Input[str] user_trust_provider_type: The type of device-based trust provider. Possible values: oidc|iam-identity-center
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VerifiedAccessTrustProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::EC2::VerifiedAccessTrustProvider type describes a verified access trust provider

        :param str resource_name: The name of the resource.
        :param VerifiedAccessTrustProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VerifiedAccessTrustProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_options: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessTrustProviderDeviceOptionsArgs']]] = None,
                 device_trust_provider_type: Optional[pulumi.Input[str]] = None,
                 oidc_options: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessTrustProviderOidcOptionsArgs']]] = None,
                 policy_reference_name: Optional[pulumi.Input[str]] = None,
                 sse_specification: Optional[pulumi.Input[pulumi.InputType['SseSpecificationPropertiesArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 trust_provider_type: Optional[pulumi.Input[str]] = None,
                 user_trust_provider_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VerifiedAccessTrustProviderArgs.__new__(VerifiedAccessTrustProviderArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["device_options"] = device_options
            __props__.__dict__["device_trust_provider_type"] = device_trust_provider_type
            __props__.__dict__["oidc_options"] = oidc_options
            if policy_reference_name is None and not opts.urn:
                raise TypeError("Missing required property 'policy_reference_name'")
            __props__.__dict__["policy_reference_name"] = policy_reference_name
            __props__.__dict__["sse_specification"] = sse_specification
            __props__.__dict__["tags"] = tags
            if trust_provider_type is None and not opts.urn:
                raise TypeError("Missing required property 'trust_provider_type'")
            __props__.__dict__["trust_provider_type"] = trust_provider_type
            __props__.__dict__["user_trust_provider_type"] = user_trust_provider_type
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["verified_access_trust_provider_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["deviceOptions", "deviceTrustProviderType", "policyReferenceName", "trustProviderType", "userTrustProviderType"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(VerifiedAccessTrustProvider, __self__).__init__(
            'aws-native:ec2:VerifiedAccessTrustProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VerifiedAccessTrustProvider':
        """
        Get an existing VerifiedAccessTrustProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VerifiedAccessTrustProviderArgs.__new__(VerifiedAccessTrustProviderArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["device_options"] = None
        __props__.__dict__["device_trust_provider_type"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["oidc_options"] = None
        __props__.__dict__["policy_reference_name"] = None
        __props__.__dict__["sse_specification"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["trust_provider_type"] = None
        __props__.__dict__["user_trust_provider_type"] = None
        __props__.__dict__["verified_access_trust_provider_id"] = None
        return VerifiedAccessTrustProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the Amazon Web Services Verified Access trust provider.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceOptions")
    def device_options(self) -> pulumi.Output[Optional['outputs.VerifiedAccessTrustProviderDeviceOptions']]:
        """
        The options for device-identity trust provider.
        """
        return pulumi.get(self, "device_options")

    @property
    @pulumi.getter(name="deviceTrustProviderType")
    def device_trust_provider_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of device-based trust provider. Possible values: jamf|crowdstrike
        """
        return pulumi.get(self, "device_trust_provider_type")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        The last updated time.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="oidcOptions")
    def oidc_options(self) -> pulumi.Output[Optional['outputs.VerifiedAccessTrustProviderOidcOptions']]:
        """
        The options for an OpenID Connect-compatible user-identity trust provider.
        """
        return pulumi.get(self, "oidc_options")

    @property
    @pulumi.getter(name="policyReferenceName")
    def policy_reference_name(self) -> pulumi.Output[str]:
        """
        The identifier to be used when working with policy rules.
        """
        return pulumi.get(self, "policy_reference_name")

    @property
    @pulumi.getter(name="sseSpecification")
    def sse_specification(self) -> pulumi.Output[Optional['outputs.SseSpecificationProperties']]:
        """
        The configuration options for customer provided KMS encryption.
        """
        return pulumi.get(self, "sse_specification")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trustProviderType")
    def trust_provider_type(self) -> pulumi.Output[str]:
        """
        Type of trust provider. Possible values: user|device
        """
        return pulumi.get(self, "trust_provider_type")

    @property
    @pulumi.getter(name="userTrustProviderType")
    def user_trust_provider_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of device-based trust provider. Possible values: oidc|iam-identity-center
        """
        return pulumi.get(self, "user_trust_provider_type")

    @property
    @pulumi.getter(name="verifiedAccessTrustProviderId")
    def verified_access_trust_provider_id(self) -> pulumi.Output[str]:
        """
        The ID of the Amazon Web Services Verified Access trust provider.
        """
        return pulumi.get(self, "verified_access_trust_provider_id")

