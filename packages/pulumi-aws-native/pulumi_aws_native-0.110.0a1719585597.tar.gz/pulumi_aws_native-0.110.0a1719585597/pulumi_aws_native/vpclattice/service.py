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

__all__ = ['ServiceArgs', 'Service']

@pulumi.input_type
class ServiceArgs:
    def __init__(__self__, *,
                 auth_type: Optional[pulumi.Input['ServiceAuthType']] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 dns_entry: Optional[pulumi.Input['ServiceDnsEntryArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Service resource.
        :param pulumi.Input['ServiceAuthType'] auth_type: The type of IAM policy.
               
               - `NONE` : The resource does not use an IAM policy. This is the default.
               - `AWS_IAM` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
        :param pulumi.Input[str] certificate_arn: The Amazon Resource Name (ARN) of the certificate.
        :param pulumi.Input[str] custom_domain_name: The custom domain name of the service.
        :param pulumi.Input['ServiceDnsEntryArgs'] dns_entry: The DNS information of the service.
        :param pulumi.Input[str] name: The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
               
               If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The tags for the service.
        """
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if certificate_arn is not None:
            pulumi.set(__self__, "certificate_arn", certificate_arn)
        if custom_domain_name is not None:
            pulumi.set(__self__, "custom_domain_name", custom_domain_name)
        if dns_entry is not None:
            pulumi.set(__self__, "dns_entry", dns_entry)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input['ServiceAuthType']]:
        """
        The type of IAM policy.

        - `NONE` : The resource does not use an IAM policy. This is the default.
        - `AWS_IAM` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
        """
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input['ServiceAuthType']]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the certificate.
        """
        return pulumi.get(self, "certificate_arn")

    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_arn", value)

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The custom domain name of the service.
        """
        return pulumi.get(self, "custom_domain_name")

    @custom_domain_name.setter
    def custom_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_domain_name", value)

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> Optional[pulumi.Input['ServiceDnsEntryArgs']]:
        """
        The DNS information of the service.
        """
        return pulumi.get(self, "dns_entry")

    @dns_entry.setter
    def dns_entry(self, value: Optional[pulumi.Input['ServiceDnsEntryArgs']]):
        pulumi.set(self, "dns_entry", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.

        If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The tags for the service.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Service(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input['ServiceAuthType']] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 dns_entry: Optional[pulumi.Input[pulumi.InputType['ServiceDnsEntryArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['ServiceAuthType'] auth_type: The type of IAM policy.
               
               - `NONE` : The resource does not use an IAM policy. This is the default.
               - `AWS_IAM` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
        :param pulumi.Input[str] certificate_arn: The Amazon Resource Name (ARN) of the certificate.
        :param pulumi.Input[str] custom_domain_name: The custom domain name of the service.
        :param pulumi.Input[pulumi.InputType['ServiceDnsEntryArgs']] dns_entry: The DNS information of the service.
        :param pulumi.Input[str] name: The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.
               
               If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: The tags for the service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServiceArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A service is any software application that can run on instances containers, or serverless functions within an account or virtual private cloud (VPC).

        :param str resource_name: The name of the resource.
        :param ServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_type: Optional[pulumi.Input['ServiceAuthType']] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 custom_domain_name: Optional[pulumi.Input[str]] = None,
                 dns_entry: Optional[pulumi.Input[pulumi.InputType['ServiceDnsEntryArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceArgs.__new__(ServiceArgs)

            __props__.__dict__["auth_type"] = auth_type
            __props__.__dict__["certificate_arn"] = certificate_arn
            __props__.__dict__["custom_domain_name"] = custom_domain_name
            __props__.__dict__["dns_entry"] = dns_entry
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["last_updated_at"] = None
            __props__.__dict__["status"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["customDomainName", "name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Service, __self__).__init__(
            'aws-native:vpclattice:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceArgs.__new__(ServiceArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["auth_type"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["certificate_arn"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["custom_domain_name"] = None
        __props__.__dict__["dns_entry"] = None
        __props__.__dict__["last_updated_at"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the service.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> pulumi.Output[Optional['ServiceAuthType']]:
        """
        The type of IAM policy.

        - `NONE` : The resource does not use an IAM policy. This is the default.
        - `AWS_IAM` : The resource uses an IAM policy. When this type is used, auth is enabled and an auth policy is required.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        """
        The ID of the service.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the certificate.
        """
        return pulumi.get(self, "certificate_arn")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The date and time that the service was created, specified in ISO-8601 format.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="customDomainName")
    def custom_domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        The custom domain name of the service.
        """
        return pulumi.get(self, "custom_domain_name")

    @property
    @pulumi.getter(name="dnsEntry")
    def dns_entry(self) -> pulumi.Output[Optional['outputs.ServiceDnsEntry']]:
        """
        The DNS information of the service.
        """
        return pulumi.get(self, "dns_entry")

    @property
    @pulumi.getter(name="lastUpdatedAt")
    def last_updated_at(self) -> pulumi.Output[str]:
        """
        The date and time that the service was last updated, specified in ISO-8601 format.
        """
        return pulumi.get(self, "last_updated_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the service. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.

        If you don't specify a name, CloudFormation generates one. However, if you specify a name, and later want to replace the resource, you must specify a new name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['ServiceStatus']:
        """
        The status of the service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The tags for the service.
        """
        return pulumi.get(self, "tags")

