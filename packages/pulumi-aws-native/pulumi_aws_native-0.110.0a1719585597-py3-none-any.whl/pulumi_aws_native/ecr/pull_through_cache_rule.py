# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PullThroughCacheRuleArgs', 'PullThroughCacheRule']

@pulumi.input_type
class PullThroughCacheRuleArgs:
    def __init__(__self__, *,
                 credential_arn: Optional[pulumi.Input[str]] = None,
                 ecr_repository_prefix: Optional[pulumi.Input[str]] = None,
                 upstream_registry: Optional[pulumi.Input[str]] = None,
                 upstream_registry_url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PullThroughCacheRule resource.
        :param pulumi.Input[str] credential_arn: The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.
        :param pulumi.Input[str] ecr_repository_prefix: The ECRRepositoryPrefix is a custom alias for upstream registry url.
        :param pulumi.Input[str] upstream_registry: The name of the upstream registry.
        :param pulumi.Input[str] upstream_registry_url: The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached
        """
        if credential_arn is not None:
            pulumi.set(__self__, "credential_arn", credential_arn)
        if ecr_repository_prefix is not None:
            pulumi.set(__self__, "ecr_repository_prefix", ecr_repository_prefix)
        if upstream_registry is not None:
            pulumi.set(__self__, "upstream_registry", upstream_registry)
        if upstream_registry_url is not None:
            pulumi.set(__self__, "upstream_registry_url", upstream_registry_url)

    @property
    @pulumi.getter(name="credentialArn")
    def credential_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.
        """
        return pulumi.get(self, "credential_arn")

    @credential_arn.setter
    def credential_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "credential_arn", value)

    @property
    @pulumi.getter(name="ecrRepositoryPrefix")
    def ecr_repository_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The ECRRepositoryPrefix is a custom alias for upstream registry url.
        """
        return pulumi.get(self, "ecr_repository_prefix")

    @ecr_repository_prefix.setter
    def ecr_repository_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ecr_repository_prefix", value)

    @property
    @pulumi.getter(name="upstreamRegistry")
    def upstream_registry(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the upstream registry.
        """
        return pulumi.get(self, "upstream_registry")

    @upstream_registry.setter
    def upstream_registry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upstream_registry", value)

    @property
    @pulumi.getter(name="upstreamRegistryUrl")
    def upstream_registry_url(self) -> Optional[pulumi.Input[str]]:
        """
        The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached
        """
        return pulumi.get(self, "upstream_registry_url")

    @upstream_registry_url.setter
    def upstream_registry_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upstream_registry_url", value)


class PullThroughCacheRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credential_arn: Optional[pulumi.Input[str]] = None,
                 ecr_repository_prefix: Optional[pulumi.Input[str]] = None,
                 upstream_registry: Optional[pulumi.Input[str]] = None,
                 upstream_registry_url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::ECR::PullThroughCacheRule resource configures the upstream registry configuration details for an Amazon Elastic Container Registry (Amazon Private ECR) pull-through cache.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_ecr_pull_through_cache_rule = aws_native.ecr.PullThroughCacheRule("myECRPullThroughCacheRule",
            ecr_repository_prefix="my-ecr",
            upstream_registry_url="public.ecr.aws")

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_ecr_pull_through_cache_rule = aws_native.ecr.PullThroughCacheRule("myECRPullThroughCacheRule",
            ecr_repository_prefix="my-ecr",
            upstream_registry_url="public.ecr.aws")

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] credential_arn: The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.
        :param pulumi.Input[str] ecr_repository_prefix: The ECRRepositoryPrefix is a custom alias for upstream registry url.
        :param pulumi.Input[str] upstream_registry: The name of the upstream registry.
        :param pulumi.Input[str] upstream_registry_url: The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[PullThroughCacheRuleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::ECR::PullThroughCacheRule resource configures the upstream registry configuration details for an Amazon Elastic Container Registry (Amazon Private ECR) pull-through cache.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_ecr_pull_through_cache_rule = aws_native.ecr.PullThroughCacheRule("myECRPullThroughCacheRule",
            ecr_repository_prefix="my-ecr",
            upstream_registry_url="public.ecr.aws")

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        my_ecr_pull_through_cache_rule = aws_native.ecr.PullThroughCacheRule("myECRPullThroughCacheRule",
            ecr_repository_prefix="my-ecr",
            upstream_registry_url="public.ecr.aws")

        ```

        :param str resource_name: The name of the resource.
        :param PullThroughCacheRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PullThroughCacheRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credential_arn: Optional[pulumi.Input[str]] = None,
                 ecr_repository_prefix: Optional[pulumi.Input[str]] = None,
                 upstream_registry: Optional[pulumi.Input[str]] = None,
                 upstream_registry_url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PullThroughCacheRuleArgs.__new__(PullThroughCacheRuleArgs)

            __props__.__dict__["credential_arn"] = credential_arn
            __props__.__dict__["ecr_repository_prefix"] = ecr_repository_prefix
            __props__.__dict__["upstream_registry"] = upstream_registry
            __props__.__dict__["upstream_registry_url"] = upstream_registry_url
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["credentialArn", "ecrRepositoryPrefix", "upstreamRegistry", "upstreamRegistryUrl"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(PullThroughCacheRule, __self__).__init__(
            'aws-native:ecr:PullThroughCacheRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PullThroughCacheRule':
        """
        Get an existing PullThroughCacheRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PullThroughCacheRuleArgs.__new__(PullThroughCacheRuleArgs)

        __props__.__dict__["credential_arn"] = None
        __props__.__dict__["ecr_repository_prefix"] = None
        __props__.__dict__["upstream_registry"] = None
        __props__.__dict__["upstream_registry_url"] = None
        return PullThroughCacheRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="credentialArn")
    def credential_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that identifies the credentials to authenticate to the upstream registry.
        """
        return pulumi.get(self, "credential_arn")

    @property
    @pulumi.getter(name="ecrRepositoryPrefix")
    def ecr_repository_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The ECRRepositoryPrefix is a custom alias for upstream registry url.
        """
        return pulumi.get(self, "ecr_repository_prefix")

    @property
    @pulumi.getter(name="upstreamRegistry")
    def upstream_registry(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the upstream registry.
        """
        return pulumi.get(self, "upstream_registry")

    @property
    @pulumi.getter(name="upstreamRegistryUrl")
    def upstream_registry_url(self) -> pulumi.Output[Optional[str]]:
        """
        The upstreamRegistryUrl is the endpoint of upstream registry url of the public repository to be cached
        """
        return pulumi.get(self, "upstream_registry_url")

