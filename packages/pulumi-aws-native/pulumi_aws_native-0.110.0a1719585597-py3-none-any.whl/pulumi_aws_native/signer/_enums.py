# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'SigningProfilePlatformId',
    'SigningProfileSignatureValidityPeriodType',
]


class SigningProfilePlatformId(str, Enum):
    AWS_LAMBDA_SHA384ECDSA = "AWSLambda-SHA384-ECDSA"
    NOTATION_OCISHA384ECDSA = "Notation-OCI-SHA384-ECDSA"


class SigningProfileSignatureValidityPeriodType(str, Enum):
    """
    The time unit for signature validity: DAYS | MONTHS | YEARS.
    """
    DAYS = "DAYS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"
