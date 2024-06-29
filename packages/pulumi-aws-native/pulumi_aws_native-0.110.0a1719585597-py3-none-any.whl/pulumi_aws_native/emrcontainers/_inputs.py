# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'VirtualClusterContainerInfoArgs',
    'VirtualClusterContainerProviderArgs',
    'VirtualClusterEksInfoArgs',
]

@pulumi.input_type
class VirtualClusterContainerInfoArgs:
    def __init__(__self__, *,
                 eks_info: pulumi.Input['VirtualClusterEksInfoArgs']):
        """
        :param pulumi.Input['VirtualClusterEksInfoArgs'] eks_info: The information about the Amazon EKS cluster.
        """
        pulumi.set(__self__, "eks_info", eks_info)

    @property
    @pulumi.getter(name="eksInfo")
    def eks_info(self) -> pulumi.Input['VirtualClusterEksInfoArgs']:
        """
        The information about the Amazon EKS cluster.
        """
        return pulumi.get(self, "eks_info")

    @eks_info.setter
    def eks_info(self, value: pulumi.Input['VirtualClusterEksInfoArgs']):
        pulumi.set(self, "eks_info", value)


@pulumi.input_type
class VirtualClusterContainerProviderArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 info: pulumi.Input['VirtualClusterContainerInfoArgs'],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] id: The ID of the container cluster
        :param pulumi.Input['VirtualClusterContainerInfoArgs'] info: The information about the container cluster.
        :param pulumi.Input[str] type: The type of the container provider
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "info", info)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The ID of the container cluster
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def info(self) -> pulumi.Input['VirtualClusterContainerInfoArgs']:
        """
        The information about the container cluster.
        """
        return pulumi.get(self, "info")

    @info.setter
    def info(self, value: pulumi.Input['VirtualClusterContainerInfoArgs']):
        pulumi.set(self, "info", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the container provider
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class VirtualClusterEksInfoArgs:
    def __init__(__self__, *,
                 namespace: pulumi.Input[str]):
        """
        :param pulumi.Input[str] namespace: The namespaces of the EKS cluster.
               
               *Minimum* : 1
               
               *Maximum* : 63
               
               *Pattern* : `[a-z0-9]([-a-z0-9]*[a-z0-9])?`
        """
        pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        The namespaces of the EKS cluster.

        *Minimum* : 1

        *Maximum* : 63

        *Pattern* : `[a-z0-9]([-a-z0-9]*[a-z0-9])?`
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)


