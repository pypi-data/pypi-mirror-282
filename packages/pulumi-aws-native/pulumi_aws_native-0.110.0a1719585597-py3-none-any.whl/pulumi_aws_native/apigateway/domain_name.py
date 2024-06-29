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
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs
from ._inputs import *

__all__ = ['DomainNameArgs', 'DomainName']

@pulumi.input_type
class DomainNameArgs:
    def __init__(__self__, *,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 endpoint_configuration: Optional[pulumi.Input['DomainNameEndpointConfigurationArgs']] = None,
                 mutual_tls_authentication: Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']] = None,
                 ownership_verification_certificate_arn: Optional[pulumi.Input[str]] = None,
                 regional_certificate_arn: Optional[pulumi.Input[str]] = None,
                 security_policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a DomainName resource.
        :param pulumi.Input[str] certificate_arn: The reference to an AWS -managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
        :param pulumi.Input[str] domain_name: The custom domain name as an API host name, for example, `my-api.example.com` .
        :param pulumi.Input['DomainNameEndpointConfigurationArgs'] endpoint_configuration: The endpoint configuration of this DomainName showing the endpoint types of the domain name.
        :param pulumi.Input['DomainNameMutualTlsAuthenticationArgs'] mutual_tls_authentication: The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.
        :param pulumi.Input[str] ownership_verification_certificate_arn: The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the RegionalCertificateArn.
        :param pulumi.Input[str] regional_certificate_arn: The reference to an AWS -managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.
        :param pulumi.Input[str] security_policy: The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2` .
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: The collection of tags. Each tag element is associated with a given resource.
        """
        if certificate_arn is not None:
            pulumi.set(__self__, "certificate_arn", certificate_arn)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if endpoint_configuration is not None:
            pulumi.set(__self__, "endpoint_configuration", endpoint_configuration)
        if mutual_tls_authentication is not None:
            pulumi.set(__self__, "mutual_tls_authentication", mutual_tls_authentication)
        if ownership_verification_certificate_arn is not None:
            pulumi.set(__self__, "ownership_verification_certificate_arn", ownership_verification_certificate_arn)
        if regional_certificate_arn is not None:
            pulumi.set(__self__, "regional_certificate_arn", regional_certificate_arn)
        if security_policy is not None:
            pulumi.set(__self__, "security_policy", security_policy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The reference to an AWS -managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
        """
        return pulumi.get(self, "certificate_arn")

    @certificate_arn.setter
    def certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_arn", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The custom domain name as an API host name, for example, `my-api.example.com` .
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(self) -> Optional[pulumi.Input['DomainNameEndpointConfigurationArgs']]:
        """
        The endpoint configuration of this DomainName showing the endpoint types of the domain name.
        """
        return pulumi.get(self, "endpoint_configuration")

    @endpoint_configuration.setter
    def endpoint_configuration(self, value: Optional[pulumi.Input['DomainNameEndpointConfigurationArgs']]):
        pulumi.set(self, "endpoint_configuration", value)

    @property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(self) -> Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']]:
        """
        The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.
        """
        return pulumi.get(self, "mutual_tls_authentication")

    @mutual_tls_authentication.setter
    def mutual_tls_authentication(self, value: Optional[pulumi.Input['DomainNameMutualTlsAuthenticationArgs']]):
        pulumi.set(self, "mutual_tls_authentication", value)

    @property
    @pulumi.getter(name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the RegionalCertificateArn.
        """
        return pulumi.get(self, "ownership_verification_certificate_arn")

    @ownership_verification_certificate_arn.setter
    def ownership_verification_certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ownership_verification_certificate_arn", value)

    @property
    @pulumi.getter(name="regionalCertificateArn")
    def regional_certificate_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The reference to an AWS -managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.
        """
        return pulumi.get(self, "regional_certificate_arn")

    @regional_certificate_arn.setter
    def regional_certificate_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "regional_certificate_arn", value)

    @property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2` .
        """
        return pulumi.get(self, "security_policy")

    @security_policy.setter
    def security_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_policy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        The collection of tags. Each tag element is associated with a given resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class DomainName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 endpoint_configuration: Optional[pulumi.Input[pulumi.InputType['DomainNameEndpointConfigurationArgs']]] = None,
                 mutual_tls_authentication: Optional[pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']]] = None,
                 ownership_verification_certificate_arn: Optional[pulumi.Input[str]] = None,
                 regional_certificate_arn: Optional[pulumi.Input[str]] = None,
                 security_policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ApiGateway::DomainName.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        config = pulumi.Config()
        cfn_domain_name = config.require("cfnDomainName")
        certificate_arn = config.require("certificateArn")
        type = config.require("type")
        my_domain_name = aws_native.apigateway.DomainName("myDomainName",
            certificate_arn=certificate_arn,
            domain_name=cfn_domain_name,
            endpoint_configuration=aws_native.apigateway.DomainNameEndpointConfigurationArgs(
                types=[type],
            ),
            regional_certificate_arn=certificate_arn)
        pulumi.export("domainName", my_domain_name.id)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        config = pulumi.Config()
        cfn_domain_name = config.require("cfnDomainName")
        certificate_arn = config.require("certificateArn")
        type = config.require("type")
        my_domain_name = aws_native.apigateway.DomainName("myDomainName",
            certificate_arn=certificate_arn,
            domain_name=cfn_domain_name,
            endpoint_configuration=aws_native.apigateway.DomainNameEndpointConfigurationArgs(
                types=[type],
            ),
            regional_certificate_arn=certificate_arn)
        pulumi.export("domainName", my_domain_name.id)

        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_arn: The reference to an AWS -managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
        :param pulumi.Input[str] domain_name: The custom domain name as an API host name, for example, `my-api.example.com` .
        :param pulumi.Input[pulumi.InputType['DomainNameEndpointConfigurationArgs']] endpoint_configuration: The endpoint configuration of this DomainName showing the endpoint types of the domain name.
        :param pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']] mutual_tls_authentication: The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.
        :param pulumi.Input[str] ownership_verification_certificate_arn: The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the RegionalCertificateArn.
        :param pulumi.Input[str] regional_certificate_arn: The reference to an AWS -managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.
        :param pulumi.Input[str] security_policy: The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2` .
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: The collection of tags. Each tag element is associated with a given resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[DomainNameArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ApiGateway::DomainName.

        ## Example Usage
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        config = pulumi.Config()
        cfn_domain_name = config.require("cfnDomainName")
        certificate_arn = config.require("certificateArn")
        type = config.require("type")
        my_domain_name = aws_native.apigateway.DomainName("myDomainName",
            certificate_arn=certificate_arn,
            domain_name=cfn_domain_name,
            endpoint_configuration=aws_native.apigateway.DomainNameEndpointConfigurationArgs(
                types=[type],
            ),
            regional_certificate_arn=certificate_arn)
        pulumi.export("domainName", my_domain_name.id)

        ```
        ### Example

        ```python
        import pulumi
        import pulumi_aws_native as aws_native

        config = pulumi.Config()
        cfn_domain_name = config.require("cfnDomainName")
        certificate_arn = config.require("certificateArn")
        type = config.require("type")
        my_domain_name = aws_native.apigateway.DomainName("myDomainName",
            certificate_arn=certificate_arn,
            domain_name=cfn_domain_name,
            endpoint_configuration=aws_native.apigateway.DomainNameEndpointConfigurationArgs(
                types=[type],
            ),
            regional_certificate_arn=certificate_arn)
        pulumi.export("domainName", my_domain_name.id)

        ```

        :param str resource_name: The name of the resource.
        :param DomainNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_arn: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 endpoint_configuration: Optional[pulumi.Input[pulumi.InputType['DomainNameEndpointConfigurationArgs']]] = None,
                 mutual_tls_authentication: Optional[pulumi.Input[pulumi.InputType['DomainNameMutualTlsAuthenticationArgs']]] = None,
                 ownership_verification_certificate_arn: Optional[pulumi.Input[str]] = None,
                 regional_certificate_arn: Optional[pulumi.Input[str]] = None,
                 security_policy: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainNameArgs.__new__(DomainNameArgs)

            __props__.__dict__["certificate_arn"] = certificate_arn
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["endpoint_configuration"] = endpoint_configuration
            __props__.__dict__["mutual_tls_authentication"] = mutual_tls_authentication
            __props__.__dict__["ownership_verification_certificate_arn"] = ownership_verification_certificate_arn
            __props__.__dict__["regional_certificate_arn"] = regional_certificate_arn
            __props__.__dict__["security_policy"] = security_policy
            __props__.__dict__["tags"] = tags
            __props__.__dict__["distribution_domain_name"] = None
            __props__.__dict__["distribution_hosted_zone_id"] = None
            __props__.__dict__["regional_domain_name"] = None
            __props__.__dict__["regional_hosted_zone_id"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["domainName"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(DomainName, __self__).__init__(
            'aws-native:apigateway:DomainName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DomainName':
        """
        Get an existing DomainName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainNameArgs.__new__(DomainNameArgs)

        __props__.__dict__["certificate_arn"] = None
        __props__.__dict__["distribution_domain_name"] = None
        __props__.__dict__["distribution_hosted_zone_id"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["endpoint_configuration"] = None
        __props__.__dict__["mutual_tls_authentication"] = None
        __props__.__dict__["ownership_verification_certificate_arn"] = None
        __props__.__dict__["regional_certificate_arn"] = None
        __props__.__dict__["regional_domain_name"] = None
        __props__.__dict__["regional_hosted_zone_id"] = None
        __props__.__dict__["security_policy"] = None
        __props__.__dict__["tags"] = None
        return DomainName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateArn")
    def certificate_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The reference to an AWS -managed certificate that will be used by edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
        """
        return pulumi.get(self, "certificate_arn")

    @property
    @pulumi.getter(name="distributionDomainName")
    def distribution_domain_name(self) -> pulumi.Output[str]:
        """
        The Amazon CloudFront distribution domain name that's mapped to the custom domain name. This is only applicable for endpoints whose type is `EDGE` .

        Example: `d111111abcdef8.cloudfront.net`
        """
        return pulumi.get(self, "distribution_domain_name")

    @property
    @pulumi.getter(name="distributionHostedZoneId")
    def distribution_hosted_zone_id(self) -> pulumi.Output[str]:
        """
        The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint. The only valid value is `Z2FDTNDATAQYW2` for all regions.
        """
        return pulumi.get(self, "distribution_hosted_zone_id")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[Optional[str]]:
        """
        The custom domain name as an API host name, for example, `my-api.example.com` .
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="endpointConfiguration")
    def endpoint_configuration(self) -> pulumi.Output[Optional['outputs.DomainNameEndpointConfiguration']]:
        """
        The endpoint configuration of this DomainName showing the endpoint types of the domain name.
        """
        return pulumi.get(self, "endpoint_configuration")

    @property
    @pulumi.getter(name="mutualTlsAuthentication")
    def mutual_tls_authentication(self) -> pulumi.Output[Optional['outputs.DomainNameMutualTlsAuthentication']]:
        """
        The mutual TLS authentication configuration for a custom domain name. If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.
        """
        return pulumi.get(self, "mutual_tls_authentication")

    @property
    @pulumi.getter(name="ownershipVerificationCertificateArn")
    def ownership_verification_certificate_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The ARN of the public certificate issued by ACM to validate ownership of your custom domain. Only required when configuring mutual TLS and using an ACM imported or private CA certificate ARN as the RegionalCertificateArn.
        """
        return pulumi.get(self, "ownership_verification_certificate_arn")

    @property
    @pulumi.getter(name="regionalCertificateArn")
    def regional_certificate_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The reference to an AWS -managed certificate that will be used for validating the regional domain name. AWS Certificate Manager is the only supported source.
        """
        return pulumi.get(self, "regional_certificate_arn")

    @property
    @pulumi.getter(name="regionalDomainName")
    def regional_domain_name(self) -> pulumi.Output[str]:
        """
        The domain name associated with the regional endpoint for this custom domain name. You set up this association by adding a DNS record that points the custom domain name to this regional domain name.
        """
        return pulumi.get(self, "regional_domain_name")

    @property
    @pulumi.getter(name="regionalHostedZoneId")
    def regional_hosted_zone_id(self) -> pulumi.Output[str]:
        """
        The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint.
        """
        return pulumi.get(self, "regional_hosted_zone_id")

    @property
    @pulumi.getter(name="securityPolicy")
    def security_policy(self) -> pulumi.Output[Optional[str]]:
        """
        The Transport Layer Security (TLS) version + cipher suite for this DomainName. The valid values are `TLS_1_0` and `TLS_1_2` .
        """
        return pulumi.get(self, "security_policy")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        The collection of tags. Each tag element is associated with a given resource.
        """
        return pulumi.get(self, "tags")

