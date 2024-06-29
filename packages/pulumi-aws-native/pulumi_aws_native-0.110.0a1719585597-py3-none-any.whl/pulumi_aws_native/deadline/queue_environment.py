# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['QueueEnvironmentArgs', 'QueueEnvironment']

@pulumi.input_type
class QueueEnvironmentArgs:
    def __init__(__self__, *,
                 farm_id: pulumi.Input[str],
                 priority: pulumi.Input[int],
                 queue_id: pulumi.Input[str],
                 template: pulumi.Input[str],
                 template_type: pulumi.Input['QueueEnvironmentEnvironmentTemplateType']):
        """
        The set of arguments for constructing a QueueEnvironment resource.
        :param pulumi.Input[str] farm_id: The identifier assigned to the farm that contains the queue.
        :param pulumi.Input[int] priority: The queue environment's priority.
        :param pulumi.Input[str] queue_id: The unique identifier of the queue that contains the environment.
        :param pulumi.Input[str] template: A JSON or YAML template that describes the processing environment for the queue.
        :param pulumi.Input['QueueEnvironmentEnvironmentTemplateType'] template_type: Specifies whether the template for the queue environment is JSON or YAML.
        """
        pulumi.set(__self__, "farm_id", farm_id)
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "queue_id", queue_id)
        pulumi.set(__self__, "template", template)
        pulumi.set(__self__, "template_type", template_type)

    @property
    @pulumi.getter(name="farmId")
    def farm_id(self) -> pulumi.Input[str]:
        """
        The identifier assigned to the farm that contains the queue.
        """
        return pulumi.get(self, "farm_id")

    @farm_id.setter
    def farm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "farm_id", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[int]:
        """
        The queue environment's priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> pulumi.Input[str]:
        """
        The unique identifier of the queue that contains the environment.
        """
        return pulumi.get(self, "queue_id")

    @queue_id.setter
    def queue_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "queue_id", value)

    @property
    @pulumi.getter
    def template(self) -> pulumi.Input[str]:
        """
        A JSON or YAML template that describes the processing environment for the queue.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: pulumi.Input[str]):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter(name="templateType")
    def template_type(self) -> pulumi.Input['QueueEnvironmentEnvironmentTemplateType']:
        """
        Specifies whether the template for the queue environment is JSON or YAML.
        """
        return pulumi.get(self, "template_type")

    @template_type.setter
    def template_type(self, value: pulumi.Input['QueueEnvironmentEnvironmentTemplateType']):
        pulumi.set(self, "template_type", value)


class QueueEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 farm_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 queue_id: Optional[pulumi.Input[str]] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 template_type: Optional[pulumi.Input['QueueEnvironmentEnvironmentTemplateType']] = None,
                 __props__=None):
        """
        Definition of AWS::Deadline::QueueEnvironment Resource Type

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] farm_id: The identifier assigned to the farm that contains the queue.
        :param pulumi.Input[int] priority: The queue environment's priority.
        :param pulumi.Input[str] queue_id: The unique identifier of the queue that contains the environment.
        :param pulumi.Input[str] template: A JSON or YAML template that describes the processing environment for the queue.
        :param pulumi.Input['QueueEnvironmentEnvironmentTemplateType'] template_type: Specifies whether the template for the queue environment is JSON or YAML.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QueueEnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of AWS::Deadline::QueueEnvironment Resource Type

        :param str resource_name: The name of the resource.
        :param QueueEnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueueEnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 farm_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 queue_id: Optional[pulumi.Input[str]] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 template_type: Optional[pulumi.Input['QueueEnvironmentEnvironmentTemplateType']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QueueEnvironmentArgs.__new__(QueueEnvironmentArgs)

            if farm_id is None and not opts.urn:
                raise TypeError("Missing required property 'farm_id'")
            __props__.__dict__["farm_id"] = farm_id
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            if queue_id is None and not opts.urn:
                raise TypeError("Missing required property 'queue_id'")
            __props__.__dict__["queue_id"] = queue_id
            if template is None and not opts.urn:
                raise TypeError("Missing required property 'template'")
            __props__.__dict__["template"] = template
            if template_type is None and not opts.urn:
                raise TypeError("Missing required property 'template_type'")
            __props__.__dict__["template_type"] = template_type
            __props__.__dict__["name"] = None
            __props__.__dict__["queue_environment_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["farmId", "queueId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(QueueEnvironment, __self__).__init__(
            'aws-native:deadline:QueueEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'QueueEnvironment':
        """
        Get an existing QueueEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = QueueEnvironmentArgs.__new__(QueueEnvironmentArgs)

        __props__.__dict__["farm_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["queue_environment_id"] = None
        __props__.__dict__["queue_id"] = None
        __props__.__dict__["template"] = None
        __props__.__dict__["template_type"] = None
        return QueueEnvironment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="farmId")
    def farm_id(self) -> pulumi.Output[str]:
        """
        The identifier assigned to the farm that contains the queue.
        """
        return pulumi.get(self, "farm_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the queue environment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        The queue environment's priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="queueEnvironmentId")
    def queue_environment_id(self) -> pulumi.Output[str]:
        """
        The queue environment ID.
        """
        return pulumi.get(self, "queue_environment_id")

    @property
    @pulumi.getter(name="queueId")
    def queue_id(self) -> pulumi.Output[str]:
        """
        The unique identifier of the queue that contains the environment.
        """
        return pulumi.get(self, "queue_id")

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output[str]:
        """
        A JSON or YAML template that describes the processing environment for the queue.
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter(name="templateType")
    def template_type(self) -> pulumi.Output['QueueEnvironmentEnvironmentTemplateType']:
        """
        Specifies whether the template for the queue environment is JSON or YAML.
        """
        return pulumi.get(self, "template_type")

