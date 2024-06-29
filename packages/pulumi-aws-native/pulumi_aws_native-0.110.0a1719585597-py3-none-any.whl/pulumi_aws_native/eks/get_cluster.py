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
from .. import outputs as _root_outputs
from ._enums import *

__all__ = [
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    def __init__(__self__, access_config=None, arn=None, certificate_authority_data=None, cluster_security_group_id=None, encryption_config_key_arn=None, endpoint=None, id=None, logging=None, open_id_connect_issuer_url=None, resources_vpc_config=None, tags=None, version=None):
        if access_config and not isinstance(access_config, dict):
            raise TypeError("Expected argument 'access_config' to be a dict")
        pulumi.set(__self__, "access_config", access_config)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if certificate_authority_data and not isinstance(certificate_authority_data, str):
            raise TypeError("Expected argument 'certificate_authority_data' to be a str")
        pulumi.set(__self__, "certificate_authority_data", certificate_authority_data)
        if cluster_security_group_id and not isinstance(cluster_security_group_id, str):
            raise TypeError("Expected argument 'cluster_security_group_id' to be a str")
        pulumi.set(__self__, "cluster_security_group_id", cluster_security_group_id)
        if encryption_config_key_arn and not isinstance(encryption_config_key_arn, str):
            raise TypeError("Expected argument 'encryption_config_key_arn' to be a str")
        pulumi.set(__self__, "encryption_config_key_arn", encryption_config_key_arn)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if logging and not isinstance(logging, dict):
            raise TypeError("Expected argument 'logging' to be a dict")
        pulumi.set(__self__, "logging", logging)
        if open_id_connect_issuer_url and not isinstance(open_id_connect_issuer_url, str):
            raise TypeError("Expected argument 'open_id_connect_issuer_url' to be a str")
        pulumi.set(__self__, "open_id_connect_issuer_url", open_id_connect_issuer_url)
        if resources_vpc_config and not isinstance(resources_vpc_config, dict):
            raise TypeError("Expected argument 'resources_vpc_config' to be a dict")
        pulumi.set(__self__, "resources_vpc_config", resources_vpc_config)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="accessConfig")
    def access_config(self) -> Optional['outputs.ClusterAccessConfig']:
        """
        The access configuration for the cluster.
        """
        return pulumi.get(self, "access_config")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The ARN of the cluster, such as arn:aws:eks:us-west-2:666666666666:cluster/prod.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="certificateAuthorityData")
    def certificate_authority_data(self) -> Optional[str]:
        """
        The certificate-authority-data for your cluster.
        """
        return pulumi.get(self, "certificate_authority_data")

    @property
    @pulumi.getter(name="clusterSecurityGroupId")
    def cluster_security_group_id(self) -> Optional[str]:
        """
        The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.
        """
        return pulumi.get(self, "cluster_security_group_id")

    @property
    @pulumi.getter(name="encryptionConfigKeyArn")
    def encryption_config_key_arn(self) -> Optional[str]:
        """
        Amazon Resource Name (ARN) or alias of the customer master key (CMK).
        """
        return pulumi.get(self, "encryption_config_key_arn")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[str]:
        """
        The endpoint for your Kubernetes API server, such as https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The unique ID given to your cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def logging(self) -> Optional['outputs.Logging']:
        """
        The logging configuration for your cluster.
        """
        return pulumi.get(self, "logging")

    @property
    @pulumi.getter(name="openIdConnectIssuerUrl")
    def open_id_connect_issuer_url(self) -> Optional[str]:
        """
        The issuer URL for the cluster's OIDC identity provider, such as https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLED539D4633E53DE1B716D3041E. If you need to remove https:// from this output value, you can include the following code in your template.
        """
        return pulumi.get(self, "open_id_connect_issuer_url")

    @property
    @pulumi.getter(name="resourcesVpcConfig")
    def resources_vpc_config(self) -> Optional['outputs.ClusterResourcesVpcConfig']:
        """
        The VPC configuration that's used by the cluster control plane. Amazon EKS VPC resources have specific requirements to work properly with Kubernetes. For more information, see [Cluster VPC Considerations](https://docs.aws.amazon.com/eks/latest/userguide/network_reqs.html) and [Cluster Security Group Considerations](https://docs.aws.amazon.com/eks/latest/userguide/sec-group-reqs.html) in the *Amazon EKS User Guide* . You must specify at least two subnets. You can specify up to five security groups, but we recommend that you use a dedicated security group for your cluster control plane.
        """
        return pulumi.get(self, "resources_vpc_config")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
        """
        return pulumi.get(self, "version")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            access_config=self.access_config,
            arn=self.arn,
            certificate_authority_data=self.certificate_authority_data,
            cluster_security_group_id=self.cluster_security_group_id,
            encryption_config_key_arn=self.encryption_config_key_arn,
            endpoint=self.endpoint,
            id=self.id,
            logging=self.logging,
            open_id_connect_issuer_url=self.open_id_connect_issuer_url,
            resources_vpc_config=self.resources_vpc_config,
            tags=self.tags,
            version=self.version)


def get_cluster(name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    An object representing an Amazon EKS cluster.


    :param str name: The unique name to give to your cluster.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:eks:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        access_config=pulumi.get(__ret__, 'access_config'),
        arn=pulumi.get(__ret__, 'arn'),
        certificate_authority_data=pulumi.get(__ret__, 'certificate_authority_data'),
        cluster_security_group_id=pulumi.get(__ret__, 'cluster_security_group_id'),
        encryption_config_key_arn=pulumi.get(__ret__, 'encryption_config_key_arn'),
        endpoint=pulumi.get(__ret__, 'endpoint'),
        id=pulumi.get(__ret__, 'id'),
        logging=pulumi.get(__ret__, 'logging'),
        open_id_connect_issuer_url=pulumi.get(__ret__, 'open_id_connect_issuer_url'),
        resources_vpc_config=pulumi.get(__ret__, 'resources_vpc_config'),
        tags=pulumi.get(__ret__, 'tags'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    An object representing an Amazon EKS cluster.


    :param str name: The unique name to give to your cluster.
    """
    ...
