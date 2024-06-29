# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AlarmModelSimpleRuleComparisonOperator',
    'DetectorModelEvaluationMethod',
]


class AlarmModelSimpleRuleComparisonOperator(str, Enum):
    """
    The comparison operator.
    """
    GREATER = "GREATER"
    GREATER_OR_EQUAL = "GREATER_OR_EQUAL"
    LESS = "LESS"
    LESS_OR_EQUAL = "LESS_OR_EQUAL"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"


class DetectorModelEvaluationMethod(str, Enum):
    """
    Information about the order in which events are evaluated and how actions are executed.
    """
    BATCH = "BATCH"
    SERIAL = "SERIAL"
