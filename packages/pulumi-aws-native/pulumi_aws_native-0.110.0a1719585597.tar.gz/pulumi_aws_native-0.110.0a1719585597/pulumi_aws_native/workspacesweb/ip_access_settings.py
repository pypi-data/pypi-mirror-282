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

__all__ = ['IpAccessSettingsArgs', 'IpAccessSettings']

@pulumi.input_type
class IpAccessSettingsArgs:
    def __init__(__self__, *,
                 ip_rules: pulumi.Input[Sequence[pulumi.Input['IpAccessSettingsIpRuleArgs']]],
                 additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 customer_managed_key: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a IpAccessSettings resource.
        :param pulumi.Input[Sequence[pulumi.Input['IpAccessSettingsIpRuleArgs']]] ip_rules: The IP rules of the IP access settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_encryption_context: Additional encryption context of the IP access settings.
        :param pulumi.Input[str] customer_managed_key: The custom managed key of the IP access settings.
               
               *Pattern* : `^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$`
        :param pulumi.Input[str] description: The description of the IP access settings.
        :param pulumi.Input[str] display_name: The display name of the IP access settings.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags to add to the IP access settings resource. A tag is a key-value pair.
        """
        pulumi.set(__self__, "ip_rules", ip_rules)
        if additional_encryption_context is not None:
            pulumi.set(__self__, "additional_encryption_context", additional_encryption_context)
        if customer_managed_key is not None:
            pulumi.set(__self__, "customer_managed_key", customer_managed_key)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> pulumi.Input[Sequence[pulumi.Input['IpAccessSettingsIpRuleArgs']]]:
        """
        The IP rules of the IP access settings.
        """
        return pulumi.get(self, "ip_rules")

    @ip_rules.setter
    def ip_rules(self, value: pulumi.Input[Sequence[pulumi.Input['IpAccessSettingsIpRuleArgs']]]):
        pulumi.set(self, "ip_rules", value)

    @property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Additional encryption context of the IP access settings.
        """
        return pulumi.get(self, "additional_encryption_context")

    @additional_encryption_context.setter
    def additional_encryption_context(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_encryption_context", value)

    @property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> Optional[pulumi.Input[str]]:
        """
        The custom managed key of the IP access settings.

        *Pattern* : `^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$`
        """
        return pulumi.get(self, "customer_managed_key")

    @customer_managed_key.setter
    def customer_managed_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_managed_key", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the IP access settings.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the IP access settings.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags to add to the IP access settings resource. A tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class IpAccessSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 customer_managed_key: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpAccessSettingsIpRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Definition of AWS::WorkSpacesWeb::IpAccessSettings Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_encryption_context: Additional encryption context of the IP access settings.
        :param pulumi.Input[str] customer_managed_key: The custom managed key of the IP access settings.
               
               *Pattern* : `^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$`
        :param pulumi.Input[str] description: The description of the IP access settings.
        :param pulumi.Input[str] display_name: The display name of the IP access settings.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpAccessSettingsIpRuleArgs']]]] ip_rules: The IP rules of the IP access settings.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: The tags to add to the IP access settings resource. A tag is a key-value pair.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IpAccessSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::WorkSpacesWeb::IpAccessSettings Resource Type

        :param str resource_name: The name of the resource.
        :param IpAccessSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpAccessSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_encryption_context: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 customer_managed_key: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IpAccessSettingsIpRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IpAccessSettingsArgs.__new__(IpAccessSettingsArgs)

            __props__.__dict__["additional_encryption_context"] = additional_encryption_context
            __props__.__dict__["customer_managed_key"] = customer_managed_key
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if ip_rules is None and not opts.urn:
                raise TypeError("Missing required property 'ip_rules'")
            __props__.__dict__["ip_rules"] = ip_rules
            __props__.__dict__["tags"] = tags
            __props__.__dict__["associated_portal_arns"] = None
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["ip_access_settings_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["additionalEncryptionContext.*", "customerManagedKey"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(IpAccessSettings, __self__).__init__(
            'aws-native:workspacesweb:IpAccessSettings',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IpAccessSettings':
        """
        Get an existing IpAccessSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IpAccessSettingsArgs.__new__(IpAccessSettingsArgs)

        __props__.__dict__["additional_encryption_context"] = None
        __props__.__dict__["associated_portal_arns"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["customer_managed_key"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["ip_access_settings_arn"] = None
        __props__.__dict__["ip_rules"] = None
        __props__.__dict__["tags"] = None
        return IpAccessSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalEncryptionContext")
    def additional_encryption_context(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Additional encryption context of the IP access settings.
        """
        return pulumi.get(self, "additional_encryption_context")

    @property
    @pulumi.getter(name="associatedPortalArns")
    def associated_portal_arns(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of web portal ARNs that this IP access settings resource is associated with.
        """
        return pulumi.get(self, "associated_portal_arns")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The creation date timestamp of the IP access settings.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="customerManagedKey")
    def customer_managed_key(self) -> pulumi.Output[Optional[str]]:
        """
        The custom managed key of the IP access settings.

        *Pattern* : `^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$`
        """
        return pulumi.get(self, "customer_managed_key")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the IP access settings.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the IP access settings.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the IP access settings resource.
        """
        return pulumi.get(self, "ip_access_settings_arn")

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> pulumi.Output[Sequence['outputs.IpAccessSettingsIpRule']]:
        """
        The IP rules of the IP access settings.
        """
        return pulumi.get(self, "ip_rules")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags to add to the IP access settings resource. A tag is a key-value pair.
        """
        return pulumi.get(self, "tags")

