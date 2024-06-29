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

__all__ = [
    'GetListenerRuleResult',
    'AwaitableGetListenerRuleResult',
    'get_listener_rule',
    'get_listener_rule_output',
]

@pulumi.output_type
class GetListenerRuleResult:
    def __init__(__self__, actions=None, conditions=None, is_default=None, priority=None, rule_arn=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if conditions and not isinstance(conditions, list):
            raise TypeError("Expected argument 'conditions' to be a list")
        pulumi.set(__self__, "conditions", conditions)
        if is_default and not isinstance(is_default, bool):
            raise TypeError("Expected argument 'is_default' to be a bool")
        pulumi.set(__self__, "is_default", is_default)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if rule_arn and not isinstance(rule_arn, str):
            raise TypeError("Expected argument 'rule_arn' to be a str")
        pulumi.set(__self__, "rule_arn", rule_arn)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence['outputs.ListenerRuleAction']]:
        """
        The actions.
         The rule must include exactly one of the following types of actions: ``forward``, ``fixed-response``, or ``redirect``, and it must be the last action to be performed. If the rule is for an HTTPS listener, it can also optionally include an authentication action.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence['outputs.ListenerRuleRuleCondition']]:
        """
        The conditions.
         The rule can optionally include up to one of each of the following conditions: ``http-request-method``, ``host-header``, ``path-pattern``, and ``source-ip``. A rule can also optionally include one or more of each of the following conditions: ``http-header`` and ``query-string``.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[bool]:
        """
        Indicates whether this is the default rule.
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def priority(self) -> Optional[int]:
        """
        The rule priority. A listener can't have multiple rules with the same priority.
         If you try to reorder rules by updating their priorities, do not specify a new priority if an existing rule already uses this priority, as this can cause an error. If you need to reuse a priority with a different rule, you must remove it as a priority first, and then specify it in a subsequent update.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="ruleArn")
    def rule_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the rule.
        """
        return pulumi.get(self, "rule_arn")


class AwaitableGetListenerRuleResult(GetListenerRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListenerRuleResult(
            actions=self.actions,
            conditions=self.conditions,
            is_default=self.is_default,
            priority=self.priority,
            rule_arn=self.rule_arn)


def get_listener_rule(rule_arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListenerRuleResult:
    """
    Specifies a listener rule. The listener must be associated with an Application Load Balancer. Each rule consists of a priority, one or more actions, and one or more conditions.
     For more information, see [Quotas for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html) in the *User Guide for Application Load Balancers*.


    :param str rule_arn: The Amazon Resource Name (ARN) of the rule.
    """
    __args__ = dict()
    __args__['ruleArn'] = rule_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:elasticloadbalancingv2:getListenerRule', __args__, opts=opts, typ=GetListenerRuleResult).value

    return AwaitableGetListenerRuleResult(
        actions=pulumi.get(__ret__, 'actions'),
        conditions=pulumi.get(__ret__, 'conditions'),
        is_default=pulumi.get(__ret__, 'is_default'),
        priority=pulumi.get(__ret__, 'priority'),
        rule_arn=pulumi.get(__ret__, 'rule_arn'))


@_utilities.lift_output_func(get_listener_rule)
def get_listener_rule_output(rule_arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListenerRuleResult]:
    """
    Specifies a listener rule. The listener must be associated with an Application Load Balancer. Each rule consists of a priority, one or more actions, and one or more conditions.
     For more information, see [Quotas for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html) in the *User Guide for Application Load Balancers*.


    :param str rule_arn: The Amazon Resource Name (ARN) of the rule.
    """
    ...
