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

__all__ = ['SubscriberArgs', 'Subscriber']

@pulumi.input_type
class SubscriberArgs:
    def __init__(__self__, *,
                 access_types: pulumi.Input[Sequence[pulumi.Input['SubscriberAccessTypesItem']]],
                 data_lake_arn: pulumi.Input[str],
                 sources: pulumi.Input[Sequence[pulumi.Input['SubscriberSourceArgs']]],
                 subscriber_identity: pulumi.Input['SubscriberIdentityPropertiesArgs'],
                 subscriber_description: Optional[pulumi.Input[str]] = None,
                 subscriber_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Subscriber resource.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriberAccessTypesItem']]] access_types: You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.
               
               Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as `LAKEFORMATION` .
        :param pulumi.Input[str] data_lake_arn: The ARN for the data lake.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriberSourceArgs']]] sources: The supported AWS services from which logs and events are collected.
        :param pulumi.Input['SubscriberIdentityPropertiesArgs'] subscriber_identity: The AWS identity used to access your data.
        :param pulumi.Input[str] subscriber_description: The description for your subscriber account in Security Lake.
        :param pulumi.Input[str] subscriber_name: The name of your Security Lake subscriber account.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.
        """
        pulumi.set(__self__, "access_types", access_types)
        pulumi.set(__self__, "data_lake_arn", data_lake_arn)
        pulumi.set(__self__, "sources", sources)
        pulumi.set(__self__, "subscriber_identity", subscriber_identity)
        if subscriber_description is not None:
            pulumi.set(__self__, "subscriber_description", subscriber_description)
        if subscriber_name is not None:
            pulumi.set(__self__, "subscriber_name", subscriber_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="accessTypes")
    def access_types(self) -> pulumi.Input[Sequence[pulumi.Input['SubscriberAccessTypesItem']]]:
        """
        You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.

        Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as `LAKEFORMATION` .
        """
        return pulumi.get(self, "access_types")

    @access_types.setter
    def access_types(self, value: pulumi.Input[Sequence[pulumi.Input['SubscriberAccessTypesItem']]]):
        pulumi.set(self, "access_types", value)

    @property
    @pulumi.getter(name="dataLakeArn")
    def data_lake_arn(self) -> pulumi.Input[str]:
        """
        The ARN for the data lake.
        """
        return pulumi.get(self, "data_lake_arn")

    @data_lake_arn.setter
    def data_lake_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_lake_arn", value)

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Input[Sequence[pulumi.Input['SubscriberSourceArgs']]]:
        """
        The supported AWS services from which logs and events are collected.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: pulumi.Input[Sequence[pulumi.Input['SubscriberSourceArgs']]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter(name="subscriberIdentity")
    def subscriber_identity(self) -> pulumi.Input['SubscriberIdentityPropertiesArgs']:
        """
        The AWS identity used to access your data.
        """
        return pulumi.get(self, "subscriber_identity")

    @subscriber_identity.setter
    def subscriber_identity(self, value: pulumi.Input['SubscriberIdentityPropertiesArgs']):
        pulumi.set(self, "subscriber_identity", value)

    @property
    @pulumi.getter(name="subscriberDescription")
    def subscriber_description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for your subscriber account in Security Lake.
        """
        return pulumi.get(self, "subscriber_description")

    @subscriber_description.setter
    def subscriber_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscriber_description", value)

    @property
    @pulumi.getter(name="subscriberName")
    def subscriber_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of your Security Lake subscriber account.
        """
        return pulumi.get(self, "subscriber_name")

    @subscriber_name.setter
    def subscriber_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscriber_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class Subscriber(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_types: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriberAccessTypesItem']]]] = None,
                 data_lake_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriberSourceArgs']]]]] = None,
                 subscriber_description: Optional[pulumi.Input[str]] = None,
                 subscriber_identity: Optional[pulumi.Input[pulumi.InputType['SubscriberIdentityPropertiesArgs']]] = None,
                 subscriber_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SecurityLake::Subscriber

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input['SubscriberAccessTypesItem']]] access_types: You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.
               
               Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as `LAKEFORMATION` .
        :param pulumi.Input[str] data_lake_arn: The ARN for the data lake.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriberSourceArgs']]]] sources: The supported AWS services from which logs and events are collected.
        :param pulumi.Input[str] subscriber_description: The description for your subscriber account in Security Lake.
        :param pulumi.Input[pulumi.InputType['SubscriberIdentityPropertiesArgs']] subscriber_identity: The AWS identity used to access your data.
        :param pulumi.Input[str] subscriber_name: The name of your Security Lake subscriber account.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubscriberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SecurityLake::Subscriber

        :param str resource_name: The name of the resource.
        :param SubscriberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubscriberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_types: Optional[pulumi.Input[Sequence[pulumi.Input['SubscriberAccessTypesItem']]]] = None,
                 data_lake_arn: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubscriberSourceArgs']]]]] = None,
                 subscriber_description: Optional[pulumi.Input[str]] = None,
                 subscriber_identity: Optional[pulumi.Input[pulumi.InputType['SubscriberIdentityPropertiesArgs']]] = None,
                 subscriber_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubscriberArgs.__new__(SubscriberArgs)

            if access_types is None and not opts.urn:
                raise TypeError("Missing required property 'access_types'")
            __props__.__dict__["access_types"] = access_types
            if data_lake_arn is None and not opts.urn:
                raise TypeError("Missing required property 'data_lake_arn'")
            __props__.__dict__["data_lake_arn"] = data_lake_arn
            if sources is None and not opts.urn:
                raise TypeError("Missing required property 'sources'")
            __props__.__dict__["sources"] = sources
            __props__.__dict__["subscriber_description"] = subscriber_description
            if subscriber_identity is None and not opts.urn:
                raise TypeError("Missing required property 'subscriber_identity'")
            __props__.__dict__["subscriber_identity"] = subscriber_identity
            __props__.__dict__["subscriber_name"] = subscriber_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["resource_share_arn"] = None
            __props__.__dict__["resource_share_name"] = None
            __props__.__dict__["s3_bucket_arn"] = None
            __props__.__dict__["subscriber_arn"] = None
            __props__.__dict__["subscriber_role_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["dataLakeArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Subscriber, __self__).__init__(
            'aws-native:securitylake:Subscriber',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Subscriber':
        """
        Get an existing Subscriber resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubscriberArgs.__new__(SubscriberArgs)

        __props__.__dict__["access_types"] = None
        __props__.__dict__["data_lake_arn"] = None
        __props__.__dict__["resource_share_arn"] = None
        __props__.__dict__["resource_share_name"] = None
        __props__.__dict__["s3_bucket_arn"] = None
        __props__.__dict__["sources"] = None
        __props__.__dict__["subscriber_arn"] = None
        __props__.__dict__["subscriber_description"] = None
        __props__.__dict__["subscriber_identity"] = None
        __props__.__dict__["subscriber_name"] = None
        __props__.__dict__["subscriber_role_arn"] = None
        __props__.__dict__["tags"] = None
        return Subscriber(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessTypes")
    def access_types(self) -> pulumi.Output[Sequence['SubscriberAccessTypesItem']]:
        """
        You can choose to notify subscribers of new objects with an Amazon Simple Queue Service (Amazon SQS) queue or through messaging to an HTTPS endpoint provided by the subscriber.

        Subscribers can consume data by directly querying AWS Lake Formation tables in your Amazon S3 bucket through services like Amazon Athena. This subscription type is defined as `LAKEFORMATION` .
        """
        return pulumi.get(self, "access_types")

    @property
    @pulumi.getter(name="dataLakeArn")
    def data_lake_arn(self) -> pulumi.Output[str]:
        """
        The ARN for the data lake.
        """
        return pulumi.get(self, "data_lake_arn")

    @property
    @pulumi.getter(name="resourceShareArn")
    def resource_share_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Amazon Security Lake subscriber.
        """
        return pulumi.get(self, "resource_share_arn")

    @property
    @pulumi.getter(name="resourceShareName")
    def resource_share_name(self) -> pulumi.Output[str]:
        """
        The ARN name of the Amazon Security Lake subscriber.
        """
        return pulumi.get(self, "resource_share_name")

    @property
    @pulumi.getter(name="s3BucketArn")
    def s3_bucket_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the S3 bucket.
        """
        return pulumi.get(self, "s3_bucket_arn")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Sequence['outputs.SubscriberSource']]:
        """
        The supported AWS services from which logs and events are collected.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="subscriberArn")
    def subscriber_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Security Lake subscriber.
        """
        return pulumi.get(self, "subscriber_arn")

    @property
    @pulumi.getter(name="subscriberDescription")
    def subscriber_description(self) -> pulumi.Output[Optional[str]]:
        """
        The description for your subscriber account in Security Lake.
        """
        return pulumi.get(self, "subscriber_description")

    @property
    @pulumi.getter(name="subscriberIdentity")
    def subscriber_identity(self) -> pulumi.Output['outputs.SubscriberIdentityProperties']:
        """
        The AWS identity used to access your data.
        """
        return pulumi.get(self, "subscriber_identity")

    @property
    @pulumi.getter(name="subscriberName")
    def subscriber_name(self) -> pulumi.Output[str]:
        """
        The name of your Security Lake subscriber account.
        """
        return pulumi.get(self, "subscriber_name")

    @property
    @pulumi.getter(name="subscriberRoleArn")
    def subscriber_role_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the role used to create the Security Lake subscriber.
        """
        return pulumi.get(self, "subscriber_role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string.
        """
        return pulumi.get(self, "tags")

