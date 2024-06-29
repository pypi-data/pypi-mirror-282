# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AppAutoBranchCreationConfigStage',
    'AppPlatform',
    'BranchStage',
    'DomainCertificateCertificateType',
    'DomainCertificateSettingsCertificateType',
]


class AppAutoBranchCreationConfigStage(str, Enum):
    """
    Stage for the auto created branch.
    """
    EXPERIMENTAL = "EXPERIMENTAL"
    BETA = "BETA"
    PULL_REQUEST = "PULL_REQUEST"
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"


class AppPlatform(str, Enum):
    """
    The platform for the Amplify app. For a static app, set the platform type to `WEB` . For a dynamic server-side rendered (SSR) app, set the platform type to `WEB_COMPUTE` . For an app requiring Amplify Hosting's original SSR support only, set the platform type to `WEB_DYNAMIC` .
    """
    WEB = "WEB"
    WEB_DYNAMIC = "WEB_DYNAMIC"
    WEB_COMPUTE = "WEB_COMPUTE"


class BranchStage(str, Enum):
    """
    Describes the current stage for the branch.
    """
    EXPERIMENTAL = "EXPERIMENTAL"
    BETA = "BETA"
    PULL_REQUEST = "PULL_REQUEST"
    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"


class DomainCertificateCertificateType(str, Enum):
    """
    The type of SSL/TLS certificate that you want to use.

    Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.

    Specify `CUSTOM` to use your own certificate that you have already added to AWS Certificate Manager in your AWS account . Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide* .
    """
    AMPLIFY_MANAGED = "AMPLIFY_MANAGED"
    CUSTOM = "CUSTOM"


class DomainCertificateSettingsCertificateType(str, Enum):
    """
    The certificate type.

    Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.

    Specify `CUSTOM` to use your own certificate that you have already added to AWS Certificate Manager in your AWS account . Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide* .
    """
    AMPLIFY_MANAGED = "AMPLIFY_MANAGED"
    CUSTOM = "CUSTOM"
