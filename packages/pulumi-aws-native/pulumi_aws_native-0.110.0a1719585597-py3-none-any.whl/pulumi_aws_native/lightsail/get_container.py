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

__all__ = [
    'GetContainerResult',
    'AwaitableGetContainerResult',
    'get_container',
    'get_container_output',
]

@pulumi.output_type
class GetContainerResult:
    def __init__(__self__, container_arn=None, container_service_deployment=None, is_disabled=None, power=None, principal_arn=None, private_registry_access=None, public_domain_names=None, scale=None, tags=None, url=None):
        if container_arn and not isinstance(container_arn, str):
            raise TypeError("Expected argument 'container_arn' to be a str")
        pulumi.set(__self__, "container_arn", container_arn)
        if container_service_deployment and not isinstance(container_service_deployment, dict):
            raise TypeError("Expected argument 'container_service_deployment' to be a dict")
        pulumi.set(__self__, "container_service_deployment", container_service_deployment)
        if is_disabled and not isinstance(is_disabled, bool):
            raise TypeError("Expected argument 'is_disabled' to be a bool")
        pulumi.set(__self__, "is_disabled", is_disabled)
        if power and not isinstance(power, str):
            raise TypeError("Expected argument 'power' to be a str")
        pulumi.set(__self__, "power", power)
        if principal_arn and not isinstance(principal_arn, str):
            raise TypeError("Expected argument 'principal_arn' to be a str")
        pulumi.set(__self__, "principal_arn", principal_arn)
        if private_registry_access and not isinstance(private_registry_access, dict):
            raise TypeError("Expected argument 'private_registry_access' to be a dict")
        pulumi.set(__self__, "private_registry_access", private_registry_access)
        if public_domain_names and not isinstance(public_domain_names, list):
            raise TypeError("Expected argument 'public_domain_names' to be a list")
        pulumi.set(__self__, "public_domain_names", public_domain_names)
        if scale and not isinstance(scale, int):
            raise TypeError("Expected argument 'scale' to be a int")
        pulumi.set(__self__, "scale", scale)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="containerArn")
    def container_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the container.
        """
        return pulumi.get(self, "container_arn")

    @property
    @pulumi.getter(name="containerServiceDeployment")
    def container_service_deployment(self) -> Optional['outputs.ContainerServiceDeployment']:
        """
        Describes a container deployment configuration of an Amazon Lightsail container service.
        """
        return pulumi.get(self, "container_service_deployment")

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[bool]:
        """
        A Boolean value to indicate whether the container service is disabled.
        """
        return pulumi.get(self, "is_disabled")

    @property
    @pulumi.getter
    def power(self) -> Optional[str]:
        """
        The power specification for the container service.
        """
        return pulumi.get(self, "power")

    @property
    @pulumi.getter(name="principalArn")
    def principal_arn(self) -> Optional[str]:
        """
        The principal ARN of the container service.
        """
        return pulumi.get(self, "principal_arn")

    @property
    @pulumi.getter(name="privateRegistryAccess")
    def private_registry_access(self) -> Optional['outputs.ContainerPrivateRegistryAccess']:
        """
        A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.
        """
        return pulumi.get(self, "private_registry_access")

    @property
    @pulumi.getter(name="publicDomainNames")
    def public_domain_names(self) -> Optional[Sequence['outputs.ContainerPublicDomainName']]:
        """
        The public domain names to use with the container service, such as example.com and www.example.com.
        """
        return pulumi.get(self, "public_domain_names")

    @property
    @pulumi.getter
    def scale(self) -> Optional[int]:
        """
        The scale specification for the container service.
        """
        return pulumi.get(self, "scale")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The publicly accessible URL of the container service.
        """
        return pulumi.get(self, "url")


class AwaitableGetContainerResult(GetContainerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerResult(
            container_arn=self.container_arn,
            container_service_deployment=self.container_service_deployment,
            is_disabled=self.is_disabled,
            power=self.power,
            principal_arn=self.principal_arn,
            private_registry_access=self.private_registry_access,
            public_domain_names=self.public_domain_names,
            scale=self.scale,
            tags=self.tags,
            url=self.url)


def get_container(service_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerResult:
    """
    Resource Type definition for AWS::Lightsail::Container


    :param str service_name: The name for the container service.
    """
    __args__ = dict()
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:lightsail:getContainer', __args__, opts=opts, typ=GetContainerResult).value

    return AwaitableGetContainerResult(
        container_arn=pulumi.get(__ret__, 'container_arn'),
        container_service_deployment=pulumi.get(__ret__, 'container_service_deployment'),
        is_disabled=pulumi.get(__ret__, 'is_disabled'),
        power=pulumi.get(__ret__, 'power'),
        principal_arn=pulumi.get(__ret__, 'principal_arn'),
        private_registry_access=pulumi.get(__ret__, 'private_registry_access'),
        public_domain_names=pulumi.get(__ret__, 'public_domain_names'),
        scale=pulumi.get(__ret__, 'scale'),
        tags=pulumi.get(__ret__, 'tags'),
        url=pulumi.get(__ret__, 'url'))


@_utilities.lift_output_func(get_container)
def get_container_output(service_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerResult]:
    """
    Resource Type definition for AWS::Lightsail::Container


    :param str service_name: The name for the container service.
    """
    ...
