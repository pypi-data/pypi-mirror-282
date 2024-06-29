# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'SubscriberAccessTypesItem',
    'SubscriberNotificationHttpsNotificationConfigurationHttpMethod',
]


class SubscriberAccessTypesItem(str, Enum):
    LAKEFORMATION = "LAKEFORMATION"
    S3 = "S3"


class SubscriberNotificationHttpsNotificationConfigurationHttpMethod(str, Enum):
    """
    The HTTPS method used for the notification subscription.
    """
    POST = "POST"
    PUT = "PUT"
