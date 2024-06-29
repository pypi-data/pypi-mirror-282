# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AppAutoBranchCreationConfigArgs',
    'AppBasicAuthConfigArgs',
    'AppCustomRuleArgs',
    'AppEnvironmentVariableArgs',
    'BranchBackendArgs',
    'BranchBasicAuthConfigArgs',
    'BranchEnvironmentVariableArgs',
    'DomainCertificateSettingsArgs',
    'DomainSubDomainSettingArgs',
]

@pulumi.input_type
class AppAutoBranchCreationConfigArgs:
    def __init__(__self__, *,
                 auto_branch_creation_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 basic_auth_config: Optional[pulumi.Input['AppBasicAuthConfigArgs']] = None,
                 build_spec: Optional[pulumi.Input[str]] = None,
                 enable_auto_branch_creation: Optional[pulumi.Input[bool]] = None,
                 enable_auto_build: Optional[pulumi.Input[bool]] = None,
                 enable_performance_mode: Optional[pulumi.Input[bool]] = None,
                 enable_pull_request_preview: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]] = None,
                 framework: Optional[pulumi.Input[str]] = None,
                 pull_request_environment_name: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input['AppAutoBranchCreationConfigStage']] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] auto_branch_creation_patterns: Automated branch creation glob patterns for the Amplify app.
        :param pulumi.Input['AppBasicAuthConfigArgs'] basic_auth_config: Sets password protection for your auto created branch.
        :param pulumi.Input[str] build_spec: The build specification (build spec) for the autocreated branch.
        :param pulumi.Input[bool] enable_auto_branch_creation: Enables automated branch creation for the Amplify app.
        :param pulumi.Input[bool] enable_auto_build: Enables auto building for the auto created branch.
        :param pulumi.Input[bool] enable_performance_mode: Enables performance mode for the branch.
               
               Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
        :param pulumi.Input[bool] enable_pull_request_preview: Sets whether pull request previews are enabled for each branch that Amplify Hosting automatically creates for your app. Amplify creates previews by deploying your app to a unique URL whenever a pull request is opened for the branch. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch.
               
               To provide backend support for your preview, Amplify Hosting automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the `PullRequestEnvironmentName` property.
               
               For more information, see [Web Previews](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) in the *AWS Amplify Hosting User Guide* .
        :param pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]] environment_variables: The environment variables for the autocreated branch.
        :param pulumi.Input[str] framework: The framework for the autocreated branch.
        :param pulumi.Input[str] pull_request_environment_name: If pull request previews are enabled, you can use this property to specify a dedicated backend environment for your previews. For example, you could specify an environment named `prod` , `test` , or `dev` that you initialized with the Amplify CLI.
               
               To enable pull request previews, set the `EnablePullRequestPreview` property to `true` .
               
               If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify deletes this environment when the pull request is closed.
               
               For more information about creating backend environments, see [Feature Branch Deployments and Team Workflows](https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html) in the *AWS Amplify Hosting User Guide* .
        :param pulumi.Input['AppAutoBranchCreationConfigStage'] stage: Stage for the auto created branch.
        """
        if auto_branch_creation_patterns is not None:
            pulumi.set(__self__, "auto_branch_creation_patterns", auto_branch_creation_patterns)
        if basic_auth_config is not None:
            pulumi.set(__self__, "basic_auth_config", basic_auth_config)
        if build_spec is not None:
            pulumi.set(__self__, "build_spec", build_spec)
        if enable_auto_branch_creation is not None:
            pulumi.set(__self__, "enable_auto_branch_creation", enable_auto_branch_creation)
        if enable_auto_build is not None:
            pulumi.set(__self__, "enable_auto_build", enable_auto_build)
        if enable_performance_mode is not None:
            pulumi.set(__self__, "enable_performance_mode", enable_performance_mode)
        if enable_pull_request_preview is not None:
            pulumi.set(__self__, "enable_pull_request_preview", enable_pull_request_preview)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if framework is not None:
            pulumi.set(__self__, "framework", framework)
        if pull_request_environment_name is not None:
            pulumi.set(__self__, "pull_request_environment_name", pull_request_environment_name)
        if stage is not None:
            pulumi.set(__self__, "stage", stage)

    @property
    @pulumi.getter(name="autoBranchCreationPatterns")
    def auto_branch_creation_patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Automated branch creation glob patterns for the Amplify app.
        """
        return pulumi.get(self, "auto_branch_creation_patterns")

    @auto_branch_creation_patterns.setter
    def auto_branch_creation_patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "auto_branch_creation_patterns", value)

    @property
    @pulumi.getter(name="basicAuthConfig")
    def basic_auth_config(self) -> Optional[pulumi.Input['AppBasicAuthConfigArgs']]:
        """
        Sets password protection for your auto created branch.
        """
        return pulumi.get(self, "basic_auth_config")

    @basic_auth_config.setter
    def basic_auth_config(self, value: Optional[pulumi.Input['AppBasicAuthConfigArgs']]):
        pulumi.set(self, "basic_auth_config", value)

    @property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[pulumi.Input[str]]:
        """
        The build specification (build spec) for the autocreated branch.
        """
        return pulumi.get(self, "build_spec")

    @build_spec.setter
    def build_spec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "build_spec", value)

    @property
    @pulumi.getter(name="enableAutoBranchCreation")
    def enable_auto_branch_creation(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables automated branch creation for the Amplify app.
        """
        return pulumi.get(self, "enable_auto_branch_creation")

    @enable_auto_branch_creation.setter
    def enable_auto_branch_creation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_auto_branch_creation", value)

    @property
    @pulumi.getter(name="enableAutoBuild")
    def enable_auto_build(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables auto building for the auto created branch.
        """
        return pulumi.get(self, "enable_auto_build")

    @enable_auto_build.setter
    def enable_auto_build(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_auto_build", value)

    @property
    @pulumi.getter(name="enablePerformanceMode")
    def enable_performance_mode(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables performance mode for the branch.

        Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out.
        """
        return pulumi.get(self, "enable_performance_mode")

    @enable_performance_mode.setter
    def enable_performance_mode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_performance_mode", value)

    @property
    @pulumi.getter(name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> Optional[pulumi.Input[bool]]:
        """
        Sets whether pull request previews are enabled for each branch that Amplify Hosting automatically creates for your app. Amplify creates previews by deploying your app to a unique URL whenever a pull request is opened for the branch. Development and QA teams can use this preview to test the pull request before it's merged into a production or integration branch.

        To provide backend support for your preview, Amplify Hosting automatically provisions a temporary backend environment that it deletes when the pull request is closed. If you want to specify a dedicated backend environment for your previews, use the `PullRequestEnvironmentName` property.

        For more information, see [Web Previews](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) in the *AWS Amplify Hosting User Guide* .
        """
        return pulumi.get(self, "enable_pull_request_preview")

    @enable_pull_request_preview.setter
    def enable_pull_request_preview(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_pull_request_preview", value)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]]:
        """
        The environment variables for the autocreated branch.
        """
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter
    def framework(self) -> Optional[pulumi.Input[str]]:
        """
        The framework for the autocreated branch.
        """
        return pulumi.get(self, "framework")

    @framework.setter
    def framework(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "framework", value)

    @property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> Optional[pulumi.Input[str]]:
        """
        If pull request previews are enabled, you can use this property to specify a dedicated backend environment for your previews. For example, you could specify an environment named `prod` , `test` , or `dev` that you initialized with the Amplify CLI.

        To enable pull request previews, set the `EnablePullRequestPreview` property to `true` .

        If you don't specify an environment, Amplify Hosting provides backend support for each preview by automatically provisioning a temporary backend environment. Amplify deletes this environment when the pull request is closed.

        For more information about creating backend environments, see [Feature Branch Deployments and Team Workflows](https://docs.aws.amazon.com/amplify/latest/userguide/multi-environments.html) in the *AWS Amplify Hosting User Guide* .
        """
        return pulumi.get(self, "pull_request_environment_name")

    @pull_request_environment_name.setter
    def pull_request_environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pull_request_environment_name", value)

    @property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input['AppAutoBranchCreationConfigStage']]:
        """
        Stage for the auto created branch.
        """
        return pulumi.get(self, "stage")

    @stage.setter
    def stage(self, value: Optional[pulumi.Input['AppAutoBranchCreationConfigStage']]):
        pulumi.set(self, "stage", value)


@pulumi.input_type
class AppBasicAuthConfigArgs:
    def __init__(__self__, *,
                 enable_basic_auth: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enable_basic_auth: Enables basic authorization for the Amplify app's branches.
        :param pulumi.Input[str] password: The password for basic authorization.
        :param pulumi.Input[str] username: The user name for basic authorization.
        """
        if enable_basic_auth is not None:
            pulumi.set(__self__, "enable_basic_auth", enable_basic_auth)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables basic authorization for the Amplify app's branches.
        """
        return pulumi.get(self, "enable_basic_auth")

    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_basic_auth", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for basic authorization.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        The user name for basic authorization.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class AppCustomRuleArgs:
    def __init__(__self__, *,
                 source: pulumi.Input[str],
                 target: pulumi.Input[str],
                 condition: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] source: The source pattern for a URL rewrite or redirect rule.
        :param pulumi.Input[str] target: The target pattern for a URL rewrite or redirect rule.
        :param pulumi.Input[str] condition: The condition for a URL rewrite or redirect rule, such as a country code.
        :param pulumi.Input[str] status: The status code for a URL rewrite or redirect rule.
               
               - **200** - Represents a 200 rewrite rule.
               - **301** - Represents a 301 (moved pemanently) redirect rule. This and all future requests should be directed to the target URL.
               - **302** - Represents a 302 temporary redirect rule.
               - **404** - Represents a 404 redirect rule.
               - **404-200** - Represents a 404 rewrite rule.
        """
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "target", target)
        if condition is not None:
            pulumi.set(__self__, "condition", condition)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        The source pattern for a URL rewrite or redirect rule.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[str]:
        """
        The target pattern for a URL rewrite or redirect rule.
        """
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[str]]:
        """
        The condition for a URL rewrite or redirect rule, such as a country code.
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status code for a URL rewrite or redirect rule.

        - **200** - Represents a 200 rewrite rule.
        - **301** - Represents a 301 (moved pemanently) redirect rule. This and all future requests should be directed to the target URL.
        - **302** - Represents a 302 temporary redirect rule.
        - **404** - Represents a 404 redirect rule.
        - **404-200** - Represents a 404 rewrite rule.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class AppEnvironmentVariableArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The environment variable name.
        :param pulumi.Input[str] value: The environment variable value.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The environment variable name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The environment variable value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class BranchBackendArgs:
    def __init__(__self__, *,
                 stack_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] stack_arn: The Amazon Resource Name (ARN) for the AWS CloudFormation stack.
        """
        if stack_arn is not None:
            pulumi.set(__self__, "stack_arn", stack_arn)

    @property
    @pulumi.getter(name="stackArn")
    def stack_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) for the AWS CloudFormation stack.
        """
        return pulumi.get(self, "stack_arn")

    @stack_arn.setter
    def stack_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_arn", value)


@pulumi.input_type
class BranchBasicAuthConfigArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str],
                 enable_basic_auth: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] password: The password for basic authorization.
        :param pulumi.Input[bool] enable_basic_auth: Enables basic authorization for the branch.
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)
        if enable_basic_auth is not None:
            pulumi.set(__self__, "enable_basic_auth", enable_basic_auth)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password for basic authorization.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Enables basic authorization for the branch.
        """
        return pulumi.get(self, "enable_basic_auth")

    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_basic_auth", value)


@pulumi.input_type
class BranchEnvironmentVariableArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The environment variable name.
        :param pulumi.Input[str] value: The environment variable value.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The environment variable name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The environment variable value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class DomainCertificateSettingsArgs:
    def __init__(__self__, *,
                 certificate_type: Optional[pulumi.Input['DomainCertificateSettingsCertificateType']] = None,
                 custom_certificate_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['DomainCertificateSettingsCertificateType'] certificate_type: The certificate type.
               
               Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.
               
               Specify `CUSTOM` to use your own certificate that you have already added to AWS Certificate Manager in your AWS account . Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide* .
        :param pulumi.Input[str] custom_certificate_arn: The Amazon resource name (ARN) for the custom certificate that you have already added to AWS Certificate Manager in your AWS account .
               
               This field is required only when the certificate type is `CUSTOM` .
        """
        if certificate_type is not None:
            pulumi.set(__self__, "certificate_type", certificate_type)
        if custom_certificate_arn is not None:
            pulumi.set(__self__, "custom_certificate_arn", custom_certificate_arn)

    @property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> Optional[pulumi.Input['DomainCertificateSettingsCertificateType']]:
        """
        The certificate type.

        Specify `AMPLIFY_MANAGED` to use the default certificate that Amplify provisions for you.

        Specify `CUSTOM` to use your own certificate that you have already added to AWS Certificate Manager in your AWS account . Make sure you request (or import) the certificate in the US East (N. Virginia) Region (us-east-1). For more information about using ACM, see [Importing certificates into AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *ACM User guide* .
        """
        return pulumi.get(self, "certificate_type")

    @certificate_type.setter
    def certificate_type(self, value: Optional[pulumi.Input['DomainCertificateSettingsCertificateType']]):
        pulumi.set(self, "certificate_type", value)

    @property
    @pulumi.getter(name="customCertificateArn")
    def custom_certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon resource name (ARN) for the custom certificate that you have already added to AWS Certificate Manager in your AWS account .

        This field is required only when the certificate type is `CUSTOM` .
        """
        return pulumi.get(self, "custom_certificate_arn")

    @custom_certificate_arn.setter
    def custom_certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_certificate_arn", value)


@pulumi.input_type
class DomainSubDomainSettingArgs:
    def __init__(__self__, *,
                 branch_name: pulumi.Input[str],
                 prefix: pulumi.Input[str]):
        """
        :param pulumi.Input[str] branch_name: The branch name setting for the subdomain.
               
               *Length Constraints:* Minimum length of 1. Maximum length of 255.
               
               *Pattern:* (?s).+
        :param pulumi.Input[str] prefix: The prefix setting for the subdomain.
        """
        pulumi.set(__self__, "branch_name", branch_name)
        pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> pulumi.Input[str]:
        """
        The branch name setting for the subdomain.

        *Length Constraints:* Minimum length of 1. Maximum length of 255.

        *Pattern:* (?s).+
        """
        return pulumi.get(self, "branch_name")

    @branch_name.setter
    def branch_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "branch_name", value)

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[str]:
        """
        The prefix setting for the subdomain.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "prefix", value)


