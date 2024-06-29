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

__all__ = ['ProtectionGroupArgs', 'ProtectionGroup']

@pulumi.input_type
class ProtectionGroupArgs:
    def __init__(__self__, *,
                 aggregation: pulumi.Input['ProtectionGroupAggregation'],
                 pattern: pulumi.Input['ProtectionGroupPattern'],
                 protection_group_id: pulumi.Input[str],
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_type: Optional[pulumi.Input['ProtectionGroupResourceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a ProtectionGroup resource.
        :param pulumi.Input['ProtectionGroupAggregation'] aggregation: Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.
               * Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
               * Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
               * Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.
        :param pulumi.Input['ProtectionGroupPattern'] pattern: The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.
        :param pulumi.Input[str] protection_group_id: The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.
        :param pulumi.Input['ProtectionGroupResourceType'] resource_type: The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: One or more tag key-value pairs for the Protection object.
        """
        pulumi.set(__self__, "aggregation", aggregation)
        pulumi.set(__self__, "pattern", pattern)
        pulumi.set(__self__, "protection_group_id", protection_group_id)
        if members is not None:
            pulumi.set(__self__, "members", members)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def aggregation(self) -> pulumi.Input['ProtectionGroupAggregation']:
        """
        Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.
        * Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
        * Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
        * Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.
        """
        return pulumi.get(self, "aggregation")

    @aggregation.setter
    def aggregation(self, value: pulumi.Input['ProtectionGroupAggregation']):
        pulumi.set(self, "aggregation", value)

    @property
    @pulumi.getter
    def pattern(self) -> pulumi.Input['ProtectionGroupPattern']:
        """
        The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.
        """
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: pulumi.Input['ProtectionGroupPattern']):
        pulumi.set(self, "pattern", value)

    @property
    @pulumi.getter(name="protectionGroupId")
    def protection_group_id(self) -> pulumi.Input[str]:
        """
        The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.
        """
        return pulumi.get(self, "protection_group_id")

    @protection_group_id.setter
    def protection_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "protection_group_id", value)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input['ProtectionGroupResourceType']]:
        """
        The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input['ProtectionGroupResourceType']]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        One or more tag key-value pairs for the Protection object.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class ProtectionGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aggregation: Optional[pulumi.Input['ProtectionGroupAggregation']] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pattern: Optional[pulumi.Input['ProtectionGroupPattern']] = None,
                 protection_group_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input['ProtectionGroupResourceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        A grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        protection_group = aws_native.shield.ProtectionGroup("protectionGroup",
            protection_group_id="ProtectionGroupForAllResources",
            aggregation=aws_native.shield.ProtectionGroupAggregation.SUM,
            pattern=aws_native.shield.ProtectionGroupPattern.ALL)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        protection_group = aws_native.shield.ProtectionGroup("protectionGroup",
            protection_group_id="ProtectionGroupForAllResources",
            aggregation=aws_native.shield.ProtectionGroupAggregation.SUM,
            pattern=aws_native.shield.ProtectionGroupPattern.ALL)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        protection_group = aws_native.shield.ProtectionGroup("protectionGroup",
            protection_group_id="ProtectionGroupForAllEIPResources",
            aggregation=aws_native.shield.ProtectionGroupAggregation.SUM,
            pattern=aws_native.shield.ProtectionGroupPattern.BY_RESOURCE_TYPE,
            resource_type=aws_native.shield.ProtectionGroupResourceType.ELASTIC_IP_ALLOCATION)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        protection_group = aws_native.shield.ProtectionGroup("protectionGroup",
            protection_group_id="ProtectionGroupForAllEIPResources",
            aggregation=aws_native.shield.ProtectionGroupAggregation.SUM,
            pattern=aws_native.shield.ProtectionGroupPattern.BY_RESOURCE_TYPE,
            resource_type=aws_native.shield.ProtectionGroupResourceType.ELASTIC_IP_ALLOCATION)

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['ProtectionGroupAggregation'] aggregation: Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.
               * Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
               * Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
               * Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.
        :param pulumi.Input['ProtectionGroupPattern'] pattern: The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.
        :param pulumi.Input[str] protection_group_id: The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.
        :param pulumi.Input['ProtectionGroupResourceType'] resource_type: The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: One or more tag key-value pairs for the Protection object.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProtectionGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        protection_group = aws_native.shield.ProtectionGroup("protectionGroup",
            protection_group_id="ProtectionGroupForAllResources",
            aggregation=aws_native.shield.ProtectionGroupAggregation.SUM,
            pattern=aws_native.shield.ProtectionGroupPattern.ALL)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        protection_group = aws_native.shield.ProtectionGroup("protectionGroup",
            protection_group_id="ProtectionGroupForAllResources",
            aggregation=aws_native.shield.ProtectionGroupAggregation.SUM,
            pattern=aws_native.shield.ProtectionGroupPattern.ALL)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        protection_group = aws_native.shield.ProtectionGroup("protectionGroup",
            protection_group_id="ProtectionGroupForAllEIPResources",
            aggregation=aws_native.shield.ProtectionGroupAggregation.SUM,
            pattern=aws_native.shield.ProtectionGroupPattern.BY_RESOURCE_TYPE,
            resource_type=aws_native.shield.ProtectionGroupResourceType.ELASTIC_IP_ALLOCATION)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        protection_group = aws_native.shield.ProtectionGroup("protectionGroup",
            protection_group_id="ProtectionGroupForAllEIPResources",
            aggregation=aws_native.shield.ProtectionGroupAggregation.SUM,
            pattern=aws_native.shield.ProtectionGroupPattern.BY_RESOURCE_TYPE,
            resource_type=aws_native.shield.ProtectionGroupResourceType.ELASTIC_IP_ALLOCATION)

        ```

        :param str resource_name: The name of the resource.
        :param ProtectionGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProtectionGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aggregation: Optional[pulumi.Input['ProtectionGroupAggregation']] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 pattern: Optional[pulumi.Input['ProtectionGroupPattern']] = None,
                 protection_group_id: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input['ProtectionGroupResourceType']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProtectionGroupArgs.__new__(ProtectionGroupArgs)

            if aggregation is None and not opts.urn:
                raise TypeError("Missing required property 'aggregation'")
            __props__.__dict__["aggregation"] = aggregation
            __props__.__dict__["members"] = members
            if pattern is None and not opts.urn:
                raise TypeError("Missing required property 'pattern'")
            __props__.__dict__["pattern"] = pattern
            if protection_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'protection_group_id'")
            __props__.__dict__["protection_group_id"] = protection_group_id
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["protection_group_arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["protectionGroupId"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ProtectionGroup, __self__).__init__(
            'aws-native:shield:ProtectionGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProtectionGroup':
        """
        Get an existing ProtectionGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProtectionGroupArgs.__new__(ProtectionGroupArgs)

        __props__.__dict__["aggregation"] = None
        __props__.__dict__["members"] = None
        __props__.__dict__["pattern"] = None
        __props__.__dict__["protection_group_arn"] = None
        __props__.__dict__["protection_group_id"] = None
        __props__.__dict__["resource_type"] = None
        __props__.__dict__["tags"] = None
        return ProtectionGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def aggregation(self) -> pulumi.Output['ProtectionGroupAggregation']:
        """
        Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.
        * Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
        * Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
        * Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.
        """
        return pulumi.get(self, "aggregation")

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def pattern(self) -> pulumi.Output['ProtectionGroupPattern']:
        """
        The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.
        """
        return pulumi.get(self, "pattern")

    @property
    @pulumi.getter(name="protectionGroupArn")
    def protection_group_arn(self) -> pulumi.Output[str]:
        """
        The ARN (Amazon Resource Name) of the protection group.
        """
        return pulumi.get(self, "protection_group_arn")

    @property
    @pulumi.getter(name="protectionGroupId")
    def protection_group_id(self) -> pulumi.Output[str]:
        """
        The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.
        """
        return pulumi.get(self, "protection_group_id")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Output[Optional['ProtectionGroupResourceType']]:
        """
        The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        One or more tag key-value pairs for the Protection object.
        """
        return pulumi.get(self, "tags")

