# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DomainNameApiAssociationArgs', 'DomainNameApiAssociation']

@pulumi.input_type
class DomainNameApiAssociationArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 domain_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a DomainNameApiAssociation resource.
        :param pulumi.Input[str] api_id: The API ID.
        :param pulumi.Input[str] domain_name: The domain name.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "domain_name", domain_name)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        The API ID.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The domain name.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)


class DomainNameApiAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::AppSync::DomainNameApiAssociation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: The API ID.
        :param pulumi.Input[str] domain_name: The domain name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainNameApiAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::AppSync::DomainNameApiAssociation

        :param str resource_name: The name of the resource.
        :param DomainNameApiAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainNameApiAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainNameApiAssociationArgs.__new__(DomainNameApiAssociationArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["api_association_identifier"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domainName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DomainNameApiAssociation, __self__).__init__(
            'aws-native:appsync:DomainNameApiAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DomainNameApiAssociation':
        """
        Get an existing DomainNameApiAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainNameApiAssociationArgs.__new__(DomainNameApiAssociationArgs)

        __props__.__dict__["api_association_identifier"] = None
        __props__.__dict__["api_id"] = None
        __props__.__dict__["domain_name"] = None
        return DomainNameApiAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiAssociationIdentifier")
    def api_association_identifier(self) -> pulumi.Output[str]:
        return pulumi.get(self, "api_association_identifier")

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[str]:
        """
        The API ID.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The domain name.
        """
        return pulumi.get(self, "domain_name")

