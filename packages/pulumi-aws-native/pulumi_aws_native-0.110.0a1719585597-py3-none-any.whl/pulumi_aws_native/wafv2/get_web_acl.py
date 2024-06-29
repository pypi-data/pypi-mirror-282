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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetWebAclResult',
    'AwaitableGetWebAclResult',
    'get_web_acl',
    'get_web_acl_output',
]

@pulumi.output_type
class GetWebAclResult:
    def __init__(__self__, arn=None, association_config=None, capacity=None, captcha_config=None, challenge_config=None, custom_response_bodies=None, default_action=None, description=None, id=None, label_namespace=None, rules=None, tags=None, token_domains=None, visibility_config=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if association_config and not isinstance(association_config, dict):
            raise TypeError("Expected argument 'association_config' to be a dict")
        pulumi.set(__self__, "association_config", association_config)
        if capacity and not isinstance(capacity, int):
            raise TypeError("Expected argument 'capacity' to be a int")
        pulumi.set(__self__, "capacity", capacity)
        if captcha_config and not isinstance(captcha_config, dict):
            raise TypeError("Expected argument 'captcha_config' to be a dict")
        pulumi.set(__self__, "captcha_config", captcha_config)
        if challenge_config and not isinstance(challenge_config, dict):
            raise TypeError("Expected argument 'challenge_config' to be a dict")
        pulumi.set(__self__, "challenge_config", challenge_config)
        if custom_response_bodies and not isinstance(custom_response_bodies, dict):
            raise TypeError("Expected argument 'custom_response_bodies' to be a dict")
        pulumi.set(__self__, "custom_response_bodies", custom_response_bodies)
        if default_action and not isinstance(default_action, dict):
            raise TypeError("Expected argument 'default_action' to be a dict")
        pulumi.set(__self__, "default_action", default_action)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label_namespace and not isinstance(label_namespace, str):
            raise TypeError("Expected argument 'label_namespace' to be a str")
        pulumi.set(__self__, "label_namespace", label_namespace)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if token_domains and not isinstance(token_domains, list):
            raise TypeError("Expected argument 'token_domains' to be a list")
        pulumi.set(__self__, "token_domains", token_domains)
        if visibility_config and not isinstance(visibility_config, dict):
            raise TypeError("Expected argument 'visibility_config' to be a dict")
        pulumi.set(__self__, "visibility_config", visibility_config)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the web ACL.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associationConfig")
    def association_config(self) -> Optional['outputs.WebAclAssociationConfig']:
        """
        Specifies custom configurations for the associations between the web ACL and protected resources.

        Use this to customize the maximum size of the request body that your protected resources forward to AWS WAF for inspection. You can customize this setting for CloudFront, API Gateway, Amazon Cognito, App Runner, or Verified Access resources. The default setting is 16 KB (16,384 bytes).

        > You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](https://docs.aws.amazon.com/waf/pricing/) . 

        For Application Load Balancer and AWS AppSync , the limit is fixed at 8 KB (8,192 bytes).
        """
        return pulumi.get(self, "association_config")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        The web ACL capacity units (WCUs) currently being used by this web ACL.

        AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. The WCU limit for web ACLs is 1,500.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter(name="captchaConfig")
    def captcha_config(self) -> Optional['outputs.WebAclCaptchaConfig']:
        """
        Specifies how AWS WAF should handle `CAPTCHA` evaluations for rules that don't have their own `CaptchaConfig` settings. If you don't specify this, AWS WAF uses its default settings for `CaptchaConfig` .
        """
        return pulumi.get(self, "captcha_config")

    @property
    @pulumi.getter(name="challengeConfig")
    def challenge_config(self) -> Optional['outputs.WebAclChallengeConfig']:
        """
        Specifies how AWS WAF should handle challenge evaluations for rules that don't have their own `ChallengeConfig` settings. If you don't specify this, AWS WAF uses its default settings for `ChallengeConfig` .
        """
        return pulumi.get(self, "challenge_config")

    @property
    @pulumi.getter(name="customResponseBodies")
    def custom_response_bodies(self) -> Optional[Mapping[str, 'outputs.WebAclCustomResponseBody']]:
        """
        A map of custom response keys and content bodies. When you create a rule with a block action, you can send a custom response to the web request. You define these for the web ACL, and then use them in the rules and default actions that you define in the web ACL.

        For information about customizing web requests and responses, see [Customizing web requests and responses in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *AWS WAF Developer Guide* .

        For information about the limits on count and size for custom request and response settings, see [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *AWS WAF Developer Guide* .
        """
        return pulumi.get(self, "custom_response_bodies")

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional['outputs.WebAclDefaultAction']:
        """
        The action to perform if none of the `Rules` contained in the `WebACL` match.
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the web ACL that helps with identification.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The ID of the web ACL.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="labelNamespace")
    def label_namespace(self) -> Optional[str]:
        """
        The label namespace prefix for this web ACL. All labels added by rules in this web ACL have this prefix.

        The syntax for the label namespace prefix for a web ACL is the following: `awswaf:<account ID>:webacl:<web ACL name>:`

        When a rule with a label matches a web request, AWS WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon.
        """
        return pulumi.get(self, "label_namespace")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.WebAclRule']]:
        """
        Collection of Rules.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        Key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        > To modify tags on existing resources, use the AWS WAF APIs or command line interface. With AWS CloudFormation , you can only add tags to AWS WAF resources during resource creation.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tokenDomains")
    def token_domains(self) -> Optional[Sequence[str]]:
        """
        Specifies the domains that AWS WAF should accept in a web request token. This enables the use of tokens across multiple protected websites. When AWS WAF provides a token, it uses the domain of the AWS resource that the web ACL is protecting. If you don't specify a list of token domains, AWS WAF accepts tokens only for the domain of the protected resource. With a token domain list, AWS WAF accepts the resource's host domain plus all domains in the token domain list, including their prefixed subdomains.
        """
        return pulumi.get(self, "token_domains")

    @property
    @pulumi.getter(name="visibilityConfig")
    def visibility_config(self) -> Optional['outputs.WebAclVisibilityConfig']:
        """
        Defines and enables Amazon CloudWatch metrics and web request sample collection.
        """
        return pulumi.get(self, "visibility_config")


class AwaitableGetWebAclResult(GetWebAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAclResult(
            arn=self.arn,
            association_config=self.association_config,
            capacity=self.capacity,
            captcha_config=self.captcha_config,
            challenge_config=self.challenge_config,
            custom_response_bodies=self.custom_response_bodies,
            default_action=self.default_action,
            description=self.description,
            id=self.id,
            label_namespace=self.label_namespace,
            rules=self.rules,
            tags=self.tags,
            token_domains=self.token_domains,
            visibility_config=self.visibility_config)


def get_web_acl(id: Optional[str] = None,
                name: Optional[str] = None,
                scope: Optional['WebAclScope'] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAclResult:
    """
    Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.


    :param str id: The ID of the web ACL.
    :param str name: The name of the web ACL. You cannot change the name of a web ACL after you create it.
    :param 'WebAclScope' scope: Specifies whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an AWS AppSync GraphQL API, an Amazon Cognito user pool, an AWS App Runner service, or an AWS Verified Access instance. Valid Values are `CLOUDFRONT` and `REGIONAL` .
           
           > For `CLOUDFRONT` , you must create your WAFv2 resources in the US East (N. Virginia) Region, `us-east-1` . 
           
           For information about how to define the association of the web ACL with your resource, see `WebACLAssociation` .
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:wafv2:getWebAcl', __args__, opts=opts, typ=GetWebAclResult).value

    return AwaitableGetWebAclResult(
        arn=pulumi.get(__ret__, 'arn'),
        association_config=pulumi.get(__ret__, 'association_config'),
        capacity=pulumi.get(__ret__, 'capacity'),
        captcha_config=pulumi.get(__ret__, 'captcha_config'),
        challenge_config=pulumi.get(__ret__, 'challenge_config'),
        custom_response_bodies=pulumi.get(__ret__, 'custom_response_bodies'),
        default_action=pulumi.get(__ret__, 'default_action'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        label_namespace=pulumi.get(__ret__, 'label_namespace'),
        rules=pulumi.get(__ret__, 'rules'),
        tags=pulumi.get(__ret__, 'tags'),
        token_domains=pulumi.get(__ret__, 'token_domains'),
        visibility_config=pulumi.get(__ret__, 'visibility_config'))


@_utilities.lift_output_func(get_web_acl)
def get_web_acl_output(id: Optional[pulumi.Input[str]] = None,
                       name: Optional[pulumi.Input[str]] = None,
                       scope: Optional[pulumi.Input['WebAclScope']] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAclResult]:
    """
    Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.


    :param str id: The ID of the web ACL.
    :param str name: The name of the web ACL. You cannot change the name of a web ACL after you create it.
    :param 'WebAclScope' scope: Specifies whether this is for an Amazon CloudFront distribution or for a regional application. A regional application can be an Application Load Balancer (ALB), an Amazon API Gateway REST API, an AWS AppSync GraphQL API, an Amazon Cognito user pool, an AWS App Runner service, or an AWS Verified Access instance. Valid Values are `CLOUDFRONT` and `REGIONAL` .
           
           > For `CLOUDFRONT` , you must create your WAFv2 resources in the US East (N. Virginia) Region, `us-east-1` . 
           
           For information about how to define the association of the web ACL with your resource, see `WebACLAssociation` .
    """
    ...
