# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApplicationCredentialCredentialType',
    'ApplicationType',
]


class ApplicationCredentialCredentialType(str, Enum):
    """
    The type of the application credentials.
    """
    ADMIN = "ADMIN"


class ApplicationType(str, Enum):
    """
    The type of the application.
    """
    HANA = "HANA"
