# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ServiceLinkedRoleArgs', 'ServiceLinkedRole']

@pulumi.input_type
class ServiceLinkedRoleArgs:
    def __init__(__self__, *,
                 aws_service_name: Optional[pulumi.Input[str]] = None,
                 custom_suffix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServiceLinkedRole resource.
        :param pulumi.Input[str] aws_service_name: The service principal for the AWS service to which this role is attached.
        :param pulumi.Input[str] custom_suffix: A string that you provide, which is combined with the service-provided prefix to form the complete role name.
        :param pulumi.Input[str] description: The description of the role.
        """
        if aws_service_name is not None:
            pulumi.set(__self__, "aws_service_name", aws_service_name)
        if custom_suffix is not None:
            pulumi.set(__self__, "custom_suffix", custom_suffix)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="awsServiceName")
    def aws_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The service principal for the AWS service to which this role is attached.
        """
        return pulumi.get(self, "aws_service_name")

    @aws_service_name.setter
    def aws_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aws_service_name", value)

    @property
    @pulumi.getter(name="customSuffix")
    def custom_suffix(self) -> Optional[pulumi.Input[str]]:
        """
        A string that you provide, which is combined with the service-provided prefix to form the complete role name.
        """
        return pulumi.get(self, "custom_suffix")

    @custom_suffix.setter
    def custom_suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_suffix", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the role.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


class ServiceLinkedRole(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_service_name: Optional[pulumi.Input[str]] = None,
                 custom_suffix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::IAM::ServiceLinkedRole

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        basic_slr = aws_native.iam.ServiceLinkedRole("basicSLR",
            aws_service_name="autoscaling.amazonaws.com",
            description="Test SLR description",
            custom_suffix="TestSuffix")
        pulumi.export("slrId", basic_slr.id)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        basic_slr = aws_native.iam.ServiceLinkedRole("basicSLR",
            aws_service_name="autoscaling.amazonaws.com",
            description="Test SLR description",
            custom_suffix="TestSuffix")
        pulumi.export("slrId", basic_slr.id)

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] aws_service_name: The service principal for the AWS service to which this role is attached.
        :param pulumi.Input[str] custom_suffix: A string that you provide, which is combined with the service-provided prefix to form the complete role name.
        :param pulumi.Input[str] description: The description of the role.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServiceLinkedRoleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::IAM::ServiceLinkedRole

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        basic_slr = aws_native.iam.ServiceLinkedRole("basicSLR",
            aws_service_name="autoscaling.amazonaws.com",
            description="Test SLR description",
            custom_suffix="TestSuffix")
        pulumi.export("slrId", basic_slr.id)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        basic_slr = aws_native.iam.ServiceLinkedRole("basicSLR",
            aws_service_name="autoscaling.amazonaws.com",
            description="Test SLR description",
            custom_suffix="TestSuffix")
        pulumi.export("slrId", basic_slr.id)

        ```

        :param str resource_name: The name of the resource.
        :param ServiceLinkedRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceLinkedRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_service_name: Optional[pulumi.Input[str]] = None,
                 custom_suffix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceLinkedRoleArgs.__new__(ServiceLinkedRoleArgs)

            __props__.__dict__["aws_service_name"] = aws_service_name
            __props__.__dict__["custom_suffix"] = custom_suffix
            __props__.__dict__["description"] = description
            __props__.__dict__["role_name"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["awsServiceName", "customSuffix"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(ServiceLinkedRole, __self__).__init__(
            'aws-native:iam:ServiceLinkedRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceLinkedRole':
        """
        Get an existing ServiceLinkedRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceLinkedRoleArgs.__new__(ServiceLinkedRoleArgs)

        __props__.__dict__["aws_service_name"] = None
        __props__.__dict__["custom_suffix"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["role_name"] = None
        return ServiceLinkedRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="awsServiceName")
    def aws_service_name(self) -> pulumi.Output[Optional[str]]:
        """
        The service principal for the AWS service to which this role is attached.
        """
        return pulumi.get(self, "aws_service_name")

    @property
    @pulumi.getter(name="customSuffix")
    def custom_suffix(self) -> pulumi.Output[Optional[str]]:
        """
        A string that you provide, which is combined with the service-provided prefix to form the complete role name.
        """
        return pulumi.get(self, "custom_suffix")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[str]:
        """
        The name of the role.
        """
        return pulumi.get(self, "role_name")

