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

__all__ = ['ViewArgs', 'View']

@pulumi.input_type
class ViewArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input[str]]],
                 instance_arn: pulumi.Input[str],
                 template: Any,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a View resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] actions: The actions of the view in an array.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param Any template: The template of the view as JSON.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Connect::View` for more information about the expected schema for this property.
        :param pulumi.Input[str] description: The description of the view.
        :param pulumi.Input[str] name: The name of the view.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: One or more tags.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "instance_arn", instance_arn)
        pulumi.set(__self__, "template", template)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The actions of the view in an array.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the instance.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter
    def template(self) -> Any:
        """
        The template of the view as JSON.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Connect::View` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Any):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the view.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the view.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class View(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 template: Optional[Any] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::View

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] actions: The actions of the view in an array.
        :param pulumi.Input[str] description: The description of the view.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param pulumi.Input[str] name: The name of the view.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: One or more tags.
        :param Any template: The template of the view as JSON.
               
               Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Connect::View` for more information about the expected schema for this property.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ViewArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::View

        :param str resource_name: The name of the resource.
        :param ViewArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ViewArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 template: Optional[Any] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ViewArgs.__new__(ViewArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["description"] = description
            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__.__dict__["instance_arn"] = instance_arn
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            if template is None and not opts.urn:
                raise TypeError("Missing required property 'template'")
            __props__.__dict__["template"] = template
            __props__.__dict__["view_arn"] = None
            __props__.__dict__["view_content_sha256"] = None
            __props__.__dict__["view_id"] = None
        super(View, __self__).__init__(
            'aws-native:connect:View',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'View':
        """
        Get an existing View resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ViewArgs.__new__(ViewArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["instance_arn"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["template"] = None
        __props__.__dict__["view_arn"] = None
        __props__.__dict__["view_content_sha256"] = None
        __props__.__dict__["view_id"] = None
        return View(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[str]]:
        """
        The actions of the view in an array.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the view.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the view.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output[Any]:
        """
        The template of the view as JSON.

        Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Connect::View` for more information about the expected schema for this property.
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter(name="viewArn")
    def view_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the view.
        """
        return pulumi.get(self, "view_arn")

    @property
    @pulumi.getter(name="viewContentSha256")
    def view_content_sha256(self) -> pulumi.Output[str]:
        """
        The view content hash.
        """
        return pulumi.get(self, "view_content_sha256")

    @property
    @pulumi.getter(name="viewId")
    def view_id(self) -> pulumi.Output[str]:
        """
        The view id of the view.
        """
        return pulumi.get(self, "view_id")

