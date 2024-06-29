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

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 app_config_resource: Optional[pulumi.Input['ProjectAppConfigResourceObjectArgs']] = None,
                 data_delivery: Optional[pulumi.Input['ProjectDataDeliveryObjectArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input['ProjectAppConfigResourceObjectArgs'] app_config_resource: Use this parameter if the project will use *client-side evaluation powered by AWS AppConfig* . Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the [EvaluateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html) operation. This mitigates the latency and availability risks that come with an API call. For more information, see [Use client-side evaluation - powered by AWS AppConfig .](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-client-side-evaluation.html)
               
               This parameter is a structure that contains information about the AWS AppConfig application that will be used as for client-side evaluation.
               
               To create a project that uses client-side evaluation, you must have the `evidently:ExportProjectAsConfiguration` permission.
        :param pulumi.Input['ProjectDataDeliveryObjectArgs'] data_delivery: A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so. If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.
               
               You can't specify both `CloudWatchLogs` and `S3Destination` in the same operation.
        :param pulumi.Input[str] description: An optional description of the project.
        :param pulumi.Input[str] name: The name for the project. It can include up to 127 characters.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        if app_config_resource is not None:
            pulumi.set(__self__, "app_config_resource", app_config_resource)
        if data_delivery is not None:
            pulumi.set(__self__, "data_delivery", data_delivery)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appConfigResource")
    def app_config_resource(self) -> Optional[pulumi.Input['ProjectAppConfigResourceObjectArgs']]:
        """
        Use this parameter if the project will use *client-side evaluation powered by AWS AppConfig* . Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the [EvaluateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html) operation. This mitigates the latency and availability risks that come with an API call. For more information, see [Use client-side evaluation - powered by AWS AppConfig .](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-client-side-evaluation.html)

        This parameter is a structure that contains information about the AWS AppConfig application that will be used as for client-side evaluation.

        To create a project that uses client-side evaluation, you must have the `evidently:ExportProjectAsConfiguration` permission.
        """
        return pulumi.get(self, "app_config_resource")

    @app_config_resource.setter
    def app_config_resource(self, value: Optional[pulumi.Input['ProjectAppConfigResourceObjectArgs']]):
        pulumi.set(self, "app_config_resource", value)

    @property
    @pulumi.getter(name="dataDelivery")
    def data_delivery(self) -> Optional[pulumi.Input['ProjectDataDeliveryObjectArgs']]:
        """
        A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so. If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.

        You can't specify both `CloudWatchLogs` and `S3Destination` in the same operation.
        """
        return pulumi.get(self, "data_delivery")

    @data_delivery.setter
    def data_delivery(self, value: Optional[pulumi.Input['ProjectDataDeliveryObjectArgs']]):
        pulumi.set(self, "data_delivery", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of the project.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for the project. It can include up to 127 characters.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_config_resource: Optional[pulumi.Input[pulumi.InputType['ProjectAppConfigResourceObjectArgs']]] = None,
                 data_delivery: Optional[pulumi.Input[pulumi.InputType['ProjectDataDeliveryObjectArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Evidently::Project

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ProjectAppConfigResourceObjectArgs']] app_config_resource: Use this parameter if the project will use *client-side evaluation powered by AWS AppConfig* . Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the [EvaluateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html) operation. This mitigates the latency and availability risks that come with an API call. For more information, see [Use client-side evaluation - powered by AWS AppConfig .](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-client-side-evaluation.html)
               
               This parameter is a structure that contains information about the AWS AppConfig application that will be used as for client-side evaluation.
               
               To create a project that uses client-side evaluation, you must have the `evidently:ExportProjectAsConfiguration` permission.
        :param pulumi.Input[pulumi.InputType['ProjectDataDeliveryObjectArgs']] data_delivery: A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so. If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.
               
               You can't specify both `CloudWatchLogs` and `S3Destination` in the same operation.
        :param pulumi.Input[str] description: An optional description of the project.
        :param pulumi.Input[str] name: The name for the project. It can include up to 127 characters.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProjectArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Evidently::Project

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_config_resource: Optional[pulumi.Input[pulumi.InputType['ProjectAppConfigResourceObjectArgs']]] = None,
                 data_delivery: Optional[pulumi.Input[pulumi.InputType['ProjectDataDeliveryObjectArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["app_config_resource"] = app_config_resource
            __props__.__dict__["data_delivery"] = data_delivery
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["name"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Project, __self__).__init__(
            'aws-native:evidently:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProjectArgs.__new__(ProjectArgs)

        __props__.__dict__["app_config_resource"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["data_delivery"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appConfigResource")
    def app_config_resource(self) -> pulumi.Output[Optional['outputs.ProjectAppConfigResourceObject']]:
        """
        Use this parameter if the project will use *client-side evaluation powered by AWS AppConfig* . Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the [EvaluateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html) operation. This mitigates the latency and availability risks that come with an API call. For more information, see [Use client-side evaluation - powered by AWS AppConfig .](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-client-side-evaluation.html)

        This parameter is a structure that contains information about the AWS AppConfig application that will be used as for client-side evaluation.

        To create a project that uses client-side evaluation, you must have the `evidently:ExportProjectAsConfiguration` permission.
        """
        return pulumi.get(self, "app_config_resource")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the project. For example, `arn:aws:evidently:us-west-2:0123455678912:project/myProject`
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataDelivery")
    def data_delivery(self) -> pulumi.Output[Optional['outputs.ProjectDataDeliveryObject']]:
        """
        A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so. If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.

        You can't specify both `CloudWatchLogs` and `S3Destination` in the same operation.
        """
        return pulumi.get(self, "data_delivery")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description of the project.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for the project. It can include up to 127 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

