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
from ._enums import *
from ._inputs import *

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 resources_vpc_config: pulumi.Input['ClusterResourcesVpcConfigArgs'],
                 role_arn: pulumi.Input[str],
                 access_config: Optional[pulumi.Input['ClusterAccessConfigArgs']] = None,
                 bootstrap_self_managed_addons: Optional[pulumi.Input[bool]] = None,
                 encryption_config: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterEncryptionConfigArgs']]]] = None,
                 kubernetes_network_config: Optional[pulumi.Input['ClusterKubernetesNetworkConfigArgs']] = None,
                 logging: Optional[pulumi.Input['LoggingArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outpost_config: Optional[pulumi.Input['ClusterOutpostConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input['ClusterResourcesVpcConfigArgs'] resources_vpc_config: The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide* . You must specify at least two subnets. You can specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.
        :param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        :param pulumi.Input['ClusterAccessConfigArgs'] access_config: The access configuration for the cluster.
        :param pulumi.Input[bool] bootstrap_self_managed_addons: Set this value to false to avoid creating the default networking addons when the cluster is created.
        :param pulumi.Input[Sequence[pulumi.Input['ClusterEncryptionConfigArgs']]] encryption_config: The encryption configuration for the cluster.
        :param pulumi.Input['ClusterKubernetesNetworkConfigArgs'] kubernetes_network_config: The Kubernetes network configuration for the cluster.
        :param pulumi.Input['LoggingArgs'] logging: The logging configuration for your cluster.
        :param pulumi.Input[str] name: The unique name to give to your cluster.
        :param pulumi.Input['ClusterOutpostConfigArgs'] outpost_config: An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. This object isn't available for clusters on the AWS cloud.
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] version: The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
        """
        pulumi.set(__self__, "resources_vpc_config", resources_vpc_config)
        pulumi.set(__self__, "role_arn", role_arn)
        if access_config is not None:
            pulumi.set(__self__, "access_config", access_config)
        if bootstrap_self_managed_addons is not None:
            pulumi.set(__self__, "bootstrap_self_managed_addons", bootstrap_self_managed_addons)
        if encryption_config is not None:
            pulumi.set(__self__, "encryption_config", encryption_config)
        if kubernetes_network_config is not None:
            pulumi.set(__self__, "kubernetes_network_config", kubernetes_network_config)
        if logging is not None:
            pulumi.set(__self__, "logging", logging)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if outpost_config is not None:
            pulumi.set(__self__, "outpost_config", outpost_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="resourcesVpcConfig")
    def resources_vpc_config(self) -> pulumi.Input['ClusterResourcesVpcConfigArgs']:
        """
        The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide* . You must specify at least two subnets. You can specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.
        """
        return pulumi.get(self, "resources_vpc_config")

    @resources_vpc_config.setter
    def resources_vpc_config(self, value: pulumi.Input['ClusterResourcesVpcConfigArgs']):
        pulumi.set(self, "resources_vpc_config", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> Optional[pulumi.Input['ClusterAccessConfigArgs']]:
        """
        The access configuration for the cluster.
        """
        return pulumi.get(self, "access_config")

    @access_config.setter
    def access_config(self, value: Optional[pulumi.Input['ClusterAccessConfigArgs']]):
        pulumi.set(self, "access_config", value)

    @property
    @pulumi.getter(name="bootstrapSelfManagedAddons")
    def bootstrap_self_managed_addons(self) -> Optional[pulumi.Input[bool]]:
        """
        Set this value to false to avoid creating the default networking addons when the cluster is created.
        """
        return pulumi.get(self, "bootstrap_self_managed_addons")

    @bootstrap_self_managed_addons.setter
    def bootstrap_self_managed_addons(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bootstrap_self_managed_addons", value)

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ClusterEncryptionConfigArgs']]]]:
        """
        The encryption configuration for the cluster.
        """
        return pulumi.get(self, "encryption_config")

    @encryption_config.setter
    def encryption_config(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ClusterEncryptionConfigArgs']]]]):
        pulumi.set(self, "encryption_config", value)

    @property
    @pulumi.getter(name="kubernetesNetworkConfig")
    def kubernetes_network_config(self) -> Optional[pulumi.Input['ClusterKubernetesNetworkConfigArgs']]:
        """
        The Kubernetes network configuration for the cluster.
        """
        return pulumi.get(self, "kubernetes_network_config")

    @kubernetes_network_config.setter
    def kubernetes_network_config(self, value: Optional[pulumi.Input['ClusterKubernetesNetworkConfigArgs']]):
        pulumi.set(self, "kubernetes_network_config", value)

    @property
    @pulumi.getter
    def logging(self) -> Optional[pulumi.Input['LoggingArgs']]:
        """
        The logging configuration for your cluster.
        """
        return pulumi.get(self, "logging")

    @logging.setter
    def logging(self, value: Optional[pulumi.Input['LoggingArgs']]):
        pulumi.set(self, "logging", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique name to give to your cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="outpostConfig")
    def outpost_config(self) -> Optional[pulumi.Input['ClusterOutpostConfigArgs']]:
        """
        An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. This object isn't available for clusters on the AWS cloud.
        """
        return pulumi.get(self, "outpost_config")

    @outpost_config.setter
    def outpost_config(self, value: Optional[pulumi.Input['ClusterOutpostConfigArgs']]):
        pulumi.set(self, "outpost_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_config: Optional[pulumi.Input[pulumi.InputType['ClusterAccessConfigArgs']]] = None,
                 bootstrap_self_managed_addons: Optional[pulumi.Input[bool]] = None,
                 encryption_config: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterEncryptionConfigArgs']]]]] = None,
                 kubernetes_network_config: Optional[pulumi.Input[pulumi.InputType['ClusterKubernetesNetworkConfigArgs']]] = None,
                 logging: Optional[pulumi.Input[pulumi.InputType['LoggingArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outpost_config: Optional[pulumi.Input[pulumi.InputType['ClusterOutpostConfigArgs']]] = None,
                 resources_vpc_config: Optional[pulumi.Input[pulumi.InputType['ClusterResourcesVpcConfigArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object representing an Amazon EKS cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ClusterAccessConfigArgs']] access_config: The access configuration for the cluster.
        :param pulumi.Input[bool] bootstrap_self_managed_addons: Set this value to false to avoid creating the default networking addons when the cluster is created.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterEncryptionConfigArgs']]]] encryption_config: The encryption configuration for the cluster.
        :param pulumi.Input[pulumi.InputType['ClusterKubernetesNetworkConfigArgs']] kubernetes_network_config: The Kubernetes network configuration for the cluster.
        :param pulumi.Input[pulumi.InputType['LoggingArgs']] logging: The logging configuration for your cluster.
        :param pulumi.Input[str] name: The unique name to give to your cluster.
        :param pulumi.Input[pulumi.InputType['ClusterOutpostConfigArgs']] outpost_config: An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. This object isn't available for clusters on the AWS cloud.
        :param pulumi.Input[pulumi.InputType['ClusterResourcesVpcConfigArgs']] resources_vpc_config: The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide* . You must specify at least two subnets. You can specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.
        :param pulumi.Input[str] role_arn: The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] version: The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object representing an Amazon EKS cluster.

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_config: Optional[pulumi.Input[pulumi.InputType['ClusterAccessConfigArgs']]] = None,
                 bootstrap_self_managed_addons: Optional[pulumi.Input[bool]] = None,
                 encryption_config: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ClusterEncryptionConfigArgs']]]]] = None,
                 kubernetes_network_config: Optional[pulumi.Input[pulumi.InputType['ClusterKubernetesNetworkConfigArgs']]] = None,
                 logging: Optional[pulumi.Input[pulumi.InputType['LoggingArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 outpost_config: Optional[pulumi.Input[pulumi.InputType['ClusterOutpostConfigArgs']]] = None,
                 resources_vpc_config: Optional[pulumi.Input[pulumi.InputType['ClusterResourcesVpcConfigArgs']]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            __props__.__dict__["access_config"] = access_config
            __props__.__dict__["bootstrap_self_managed_addons"] = bootstrap_self_managed_addons
            __props__.__dict__["encryption_config"] = encryption_config
            __props__.__dict__["kubernetes_network_config"] = kubernetes_network_config
            __props__.__dict__["logging"] = logging
            __props__.__dict__["name"] = name
            __props__.__dict__["outpost_config"] = outpost_config
            if resources_vpc_config is None and not opts.urn:
                raise TypeError("Missing required property 'resources_vpc_config'")
            __props__.__dict__["resources_vpc_config"] = resources_vpc_config
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version"] = version
            __props__.__dict__["arn"] = None
            __props__.__dict__["aws_id"] = None
            __props__.__dict__["certificate_authority_data"] = None
            __props__.__dict__["cluster_security_group_id"] = None
            __props__.__dict__["encryption_config_key_arn"] = None
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["open_id_connect_issuer_url"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["accessConfig.bootstrapClusterCreatorAdminPermissions", "bootstrapSelfManagedAddons", "encryptionConfig[*]", "kubernetesNetworkConfig", "name", "outpostConfig", "roleArn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Cluster, __self__).__init__(
            'aws-native:eks:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterArgs.__new__(ClusterArgs)

        __props__.__dict__["access_config"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["aws_id"] = None
        __props__.__dict__["bootstrap_self_managed_addons"] = None
        __props__.__dict__["certificate_authority_data"] = None
        __props__.__dict__["cluster_security_group_id"] = None
        __props__.__dict__["encryption_config"] = None
        __props__.__dict__["encryption_config_key_arn"] = None
        __props__.__dict__["endpoint"] = None
        __props__.__dict__["kubernetes_network_config"] = None
        __props__.__dict__["logging"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["open_id_connect_issuer_url"] = None
        __props__.__dict__["outpost_config"] = None
        __props__.__dict__["resources_vpc_config"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["version"] = None
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> pulumi.Output[Optional['outputs.ClusterAccessConfig']]:
        """
        The access configuration for the cluster.
        """
        return pulumi.get(self, "access_config")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the cluster, such as arn:aws:eks:us-west-2:666666666666:cluster/prod.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsId")
    def aws_id(self) -> pulumi.Output[str]:
        """
        The unique ID given to your cluster.
        """
        return pulumi.get(self, "aws_id")

    @property
    @pulumi.getter(name="bootstrapSelfManagedAddons")
    def bootstrap_self_managed_addons(self) -> pulumi.Output[Optional[bool]]:
        """
        Set this value to false to avoid creating the default networking addons when the cluster is created.
        """
        return pulumi.get(self, "bootstrap_self_managed_addons")

    @property
    @pulumi.getter(name="certificateAuthorityData")
    def certificate_authority_data(self) -> pulumi.Output[str]:
        """
        The certificate-authority-data for your cluster.
        """
        return pulumi.get(self, "certificate_authority_data")

    @property
    @pulumi.getter(name="clusterSecurityGroupId")
    def cluster_security_group_id(self) -> pulumi.Output[str]:
        """
        The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.
        """
        return pulumi.get(self, "cluster_security_group_id")

    @property
    @pulumi.getter(name="encryptionConfig")
    def encryption_config(self) -> pulumi.Output[Optional[Sequence['outputs.ClusterEncryptionConfig']]]:
        """
        The encryption configuration for the cluster.
        """
        return pulumi.get(self, "encryption_config")

    @property
    @pulumi.getter(name="encryptionConfigKeyArn")
    def encryption_config_key_arn(self) -> pulumi.Output[str]:
        """
        Amazon Resource Name (ARN) or alias of the customer master key (CMK).
        """
        return pulumi.get(self, "encryption_config_key_arn")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        The endpoint for your Kubernetes API server, such as https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="kubernetesNetworkConfig")
    def kubernetes_network_config(self) -> pulumi.Output[Optional['outputs.ClusterKubernetesNetworkConfig']]:
        """
        The Kubernetes network configuration for the cluster.
        """
        return pulumi.get(self, "kubernetes_network_config")

    @property
    @pulumi.getter
    def logging(self) -> pulumi.Output[Optional['outputs.Logging']]:
        """
        The logging configuration for your cluster.
        """
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The unique name to give to your cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="openIdConnectIssuerUrl")
    def open_id_connect_issuer_url(self) -> pulumi.Output[str]:
        """
        The issuer URL for the cluster's OIDC identity provider, such as https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLED539D4633E53DE1B716D3041E. If you need to remove https:// from this output value, you can include the following code in your template.
        """
        return pulumi.get(self, "open_id_connect_issuer_url")

    @property
    @pulumi.getter(name="outpostConfig")
    def outpost_config(self) -> pulumi.Output[Optional['outputs.ClusterOutpostConfig']]:
        """
        An object representing the configuration of your local Amazon EKS cluster on an AWS Outpost. This object isn't available for clusters on the AWS cloud.
        """
        return pulumi.get(self, "outpost_config")

    @property
    @pulumi.getter(name="resourcesVpcConfig")
    def resources_vpc_config(self) -> pulumi.Output['outputs.ClusterResourcesVpcConfig']:
        """
        The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide* . You must specify at least two subnets. You can specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.
        """
        return pulumi.get(self, "resources_vpc_config")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
        """
        return pulumi.get(self, "version")

