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

__all__ = ['RepositoryLinkArgs', 'RepositoryLink']

@pulumi.input_type
class RepositoryLinkArgs:
    def __init__(__self__, *,
                 connection_arn: pulumi.Input[str],
                 owner_id: pulumi.Input[str],
                 repository_name: pulumi.Input[str],
                 encryption_key_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a RepositoryLink resource.
        :param pulumi.Input[str] connection_arn: The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.
        :param pulumi.Input[str] owner_id: the ID of the entity that owns the repository.
        :param pulumi.Input[str] repository_name: The repository for which the link is being created.
        :param pulumi.Input[str] encryption_key_arn: The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: Specifies the tags applied to a RepositoryLink.
        """
        pulumi.set(__self__, "connection_arn", connection_arn)
        pulumi.set(__self__, "owner_id", owner_id)
        pulumi.set(__self__, "repository_name", repository_name)
        if encryption_key_arn is not None:
            pulumi.set(__self__, "encryption_key_arn", encryption_key_arn)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.
        """
        return pulumi.get(self, "connection_arn")

    @connection_arn.setter
    def connection_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "connection_arn", value)

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Input[str]:
        """
        the ID of the entity that owns the repository.
        """
        return pulumi.get(self, "owner_id")

    @owner_id.setter
    def owner_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner_id", value)

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Input[str]:
        """
        The repository for which the link is being created.
        """
        return pulumi.get(self, "repository_name")

    @repository_name.setter
    def repository_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository_name", value)

    @property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.
        """
        return pulumi.get(self, "encryption_key_arn")

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_key_arn", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        Specifies the tags applied to a RepositoryLink.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class RepositoryLink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_arn: Optional[pulumi.Input[str]] = None,
                 encryption_key_arn: Optional[pulumi.Input[str]] = None,
                 owner_id: Optional[pulumi.Input[str]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Schema for AWS::CodeStarConnections::RepositoryLink resource which is used to aggregate repository metadata relevant to synchronizing source provider content to AWS Resources.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_arn: The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.
        :param pulumi.Input[str] encryption_key_arn: The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.
        :param pulumi.Input[str] owner_id: the ID of the entity that owns the repository.
        :param pulumi.Input[str] repository_name: The repository for which the link is being created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: Specifies the tags applied to a RepositoryLink.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepositoryLinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Schema for AWS::CodeStarConnections::RepositoryLink resource which is used to aggregate repository metadata relevant to synchronizing source provider content to AWS Resources.

        :param str resource_name: The name of the resource.
        :param RepositoryLinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryLinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_arn: Optional[pulumi.Input[str]] = None,
                 encryption_key_arn: Optional[pulumi.Input[str]] = None,
                 owner_id: Optional[pulumi.Input[str]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepositoryLinkArgs.__new__(RepositoryLinkArgs)

            if connection_arn is None and not opts.urn:
                raise TypeError("Missing required property 'connection_arn'")
            __props__.__dict__["connection_arn"] = connection_arn
            __props__.__dict__["encryption_key_arn"] = encryption_key_arn
            if owner_id is None and not opts.urn:
                raise TypeError("Missing required property 'owner_id'")
            __props__.__dict__["owner_id"] = owner_id
            if repository_name is None and not opts.urn:
                raise TypeError("Missing required property 'repository_name'")
            __props__.__dict__["repository_name"] = repository_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["provider_type"] = None
            __props__.__dict__["repository_link_arn"] = None
            __props__.__dict__["repository_link_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["ownerId", "repositoryName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(RepositoryLink, __self__).__init__(
            'aws-native:codestarconnections:RepositoryLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RepositoryLink':
        """
        Get an existing RepositoryLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RepositoryLinkArgs.__new__(RepositoryLinkArgs)

        __props__.__dict__["connection_arn"] = None
        __props__.__dict__["encryption_key_arn"] = None
        __props__.__dict__["owner_id"] = None
        __props__.__dict__["provider_type"] = None
        __props__.__dict__["repository_link_arn"] = None
        __props__.__dict__["repository_link_id"] = None
        __props__.__dict__["repository_name"] = None
        __props__.__dict__["tags"] = None
        return RepositoryLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionArn")
    def connection_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.
        """
        return pulumi.get(self, "connection_arn")

    @property
    @pulumi.getter(name="encryptionKeyArn")
    def encryption_key_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.
        """
        return pulumi.get(self, "encryption_key_arn")

    @property
    @pulumi.getter(name="ownerId")
    def owner_id(self) -> pulumi.Output[str]:
        """
        the ID of the entity that owns the repository.
        """
        return pulumi.get(self, "owner_id")

    @property
    @pulumi.getter(name="providerType")
    def provider_type(self) -> pulumi.Output['RepositoryLinkProviderType']:
        """
        The name of the external provider where your third-party code repository is configured.
        """
        return pulumi.get(self, "provider_type")

    @property
    @pulumi.getter(name="repositoryLinkArn")
    def repository_link_arn(self) -> pulumi.Output[str]:
        """
        A unique Amazon Resource Name (ARN) to designate the repository link.
        """
        return pulumi.get(self, "repository_link_arn")

    @property
    @pulumi.getter(name="repositoryLinkId")
    def repository_link_id(self) -> pulumi.Output[str]:
        """
        A UUID that uniquely identifies the RepositoryLink.
        """
        return pulumi.get(self, "repository_link_id")

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Output[str]:
        """
        The repository for which the link is being created.
        """
        return pulumi.get(self, "repository_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        Specifies the tags applied to a RepositoryLink.
        """
        return pulumi.get(self, "tags")

