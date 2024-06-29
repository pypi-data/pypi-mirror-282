# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WebAclAssociationArgs', 'WebAclAssociation']

@pulumi.input_type
class WebAclAssociationArgs:
    def __init__(__self__, *,
                 resource_arn: pulumi.Input[str],
                 web_acl_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a WebAclAssociation resource.
        :param pulumi.Input[str] resource_arn: The Amazon Resource Name (ARN) of the resource to associate with the web ACL.
               
               The ARN must be in one of the following formats:
               
               - For an Application Load Balancer: `arn: *partition* :elasticloadbalancing: *region* : *account-id* :loadbalancer/app/ *load-balancer-name* / *load-balancer-id*`
               - For an Amazon API Gateway REST API: `arn: *partition* :apigateway: *region* ::/restapis/ *api-id* /stages/ *stage-name*`
               - For an AWS AppSync GraphQL API: `arn: *partition* :appsync: *region* : *account-id* :apis/ *GraphQLApiId*`
               - For an Amazon Cognito user pool: `arn: *partition* :cognito-idp: *region* : *account-id* :userpool/ *user-pool-id*`
               - For an AWS App Runner service: `arn: *partition* :apprunner: *region* : *account-id* :service/ *apprunner-service-name* / *apprunner-service-id*`
               - For an AWS Verified Access instance: `arn: *partition* :ec2: *region* : *account-id* :verified-access-instance/ *instance-id*`
        :param pulumi.Input[str] web_acl_arn: The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.
        """
        pulumi.set(__self__, "resource_arn", resource_arn)
        pulumi.set(__self__, "web_acl_arn", web_acl_arn)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the resource to associate with the web ACL.

        The ARN must be in one of the following formats:

        - For an Application Load Balancer: `arn: *partition* :elasticloadbalancing: *region* : *account-id* :loadbalancer/app/ *load-balancer-name* / *load-balancer-id*`
        - For an Amazon API Gateway REST API: `arn: *partition* :apigateway: *region* ::/restapis/ *api-id* /stages/ *stage-name*`
        - For an AWS AppSync GraphQL API: `arn: *partition* :appsync: *region* : *account-id* :apis/ *GraphQLApiId*`
        - For an Amazon Cognito user pool: `arn: *partition* :cognito-idp: *region* : *account-id* :userpool/ *user-pool-id*`
        - For an AWS App Runner service: `arn: *partition* :apprunner: *region* : *account-id* :service/ *apprunner-service-name* / *apprunner-service-id*`
        - For an AWS Verified Access instance: `arn: *partition* :ec2: *region* : *account-id* :verified-access-instance/ *instance-id*`
        """
        return pulumi.get(self, "resource_arn")

    @resource_arn.setter
    def resource_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_arn", value)

    @property
    @pulumi.getter(name="webAclArn")
    def web_acl_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.
        """
        return pulumi.get(self, "web_acl_arn")

    @web_acl_arn.setter
    def web_acl_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "web_acl_arn", value)


class WebAclAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 web_acl_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Associates WebACL to Application Load Balancer, CloudFront or API Gateway.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_arn: The Amazon Resource Name (ARN) of the resource to associate with the web ACL.
               
               The ARN must be in one of the following formats:
               
               - For an Application Load Balancer: `arn: *partition* :elasticloadbalancing: *region* : *account-id* :loadbalancer/app/ *load-balancer-name* / *load-balancer-id*`
               - For an Amazon API Gateway REST API: `arn: *partition* :apigateway: *region* ::/restapis/ *api-id* /stages/ *stage-name*`
               - For an AWS AppSync GraphQL API: `arn: *partition* :appsync: *region* : *account-id* :apis/ *GraphQLApiId*`
               - For an Amazon Cognito user pool: `arn: *partition* :cognito-idp: *region* : *account-id* :userpool/ *user-pool-id*`
               - For an AWS App Runner service: `arn: *partition* :apprunner: *region* : *account-id* :service/ *apprunner-service-name* / *apprunner-service-id*`
               - For an AWS Verified Access instance: `arn: *partition* :ec2: *region* : *account-id* :verified-access-instance/ *instance-id*`
        :param pulumi.Input[str] web_acl_arn: The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAclAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Associates WebACL to Application Load Balancer, CloudFront or API Gateway.

        :param str resource_name: The name of the resource.
        :param WebAclAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAclAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_arn: Optional[pulumi.Input[str]] = None,
                 web_acl_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebAclAssociationArgs.__new__(WebAclAssociationArgs)

            if resource_arn is None and not opts.urn:
                raise TypeError("Missing required property 'resource_arn'")
            __props__.__dict__["resource_arn"] = resource_arn
            if web_acl_arn is None and not opts.urn:
                raise TypeError("Missing required property 'web_acl_arn'")
            __props__.__dict__["web_acl_arn"] = web_acl_arn
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["resourceArn", "webAclArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(WebAclAssociation, __self__).__init__(
            'aws-native:wafv2:WebAclAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAclAssociation':
        """
        Get an existing WebAclAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAclAssociationArgs.__new__(WebAclAssociationArgs)

        __props__.__dict__["resource_arn"] = None
        __props__.__dict__["web_acl_arn"] = None
        return WebAclAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resourceArn")
    def resource_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the resource to associate with the web ACL.

        The ARN must be in one of the following formats:

        - For an Application Load Balancer: `arn: *partition* :elasticloadbalancing: *region* : *account-id* :loadbalancer/app/ *load-balancer-name* / *load-balancer-id*`
        - For an Amazon API Gateway REST API: `arn: *partition* :apigateway: *region* ::/restapis/ *api-id* /stages/ *stage-name*`
        - For an AWS AppSync GraphQL API: `arn: *partition* :appsync: *region* : *account-id* :apis/ *GraphQLApiId*`
        - For an Amazon Cognito user pool: `arn: *partition* :cognito-idp: *region* : *account-id* :userpool/ *user-pool-id*`
        - For an AWS App Runner service: `arn: *partition* :apprunner: *region* : *account-id* :service/ *apprunner-service-name* / *apprunner-service-id*`
        - For an AWS Verified Access instance: `arn: *partition* :ec2: *region* : *account-id* :verified-access-instance/ *instance-id*`
        """
        return pulumi.get(self, "resource_arn")

    @property
    @pulumi.getter(name="webAclArn")
    def web_acl_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.
        """
        return pulumi.get(self, "web_acl_arn")

