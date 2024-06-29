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
from ._enums import *

__all__ = [
    'PackageGroupOriginConfiguration',
    'PackageGroupRestrictionType',
    'PackageGroupRestrictions',
]

@pulumi.output_type
class PackageGroupOriginConfiguration(dict):
    def __init__(__self__, *,
                 restrictions: 'outputs.PackageGroupRestrictions'):
        """
        :param 'PackageGroupRestrictions' restrictions: The origin configuration that is applied to the package group.
        """
        pulumi.set(__self__, "restrictions", restrictions)

    @property
    @pulumi.getter
    def restrictions(self) -> 'outputs.PackageGroupRestrictions':
        """
        The origin configuration that is applied to the package group.
        """
        return pulumi.get(self, "restrictions")


@pulumi.output_type
class PackageGroupRestrictionType(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "restrictionMode":
            suggest = "restriction_mode"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PackageGroupRestrictionType. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PackageGroupRestrictionType.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PackageGroupRestrictionType.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 restriction_mode: 'PackageGroupRestrictionTypeRestrictionMode',
                 repositories: Optional[Sequence[str]] = None):
        """
        :param 'PackageGroupRestrictionTypeRestrictionMode' restriction_mode: The package group origin restriction setting. When the value is `INHERIT` , the value is set to the value of the first parent package group which does not have a value of `INHERIT` .
        :param Sequence[str] repositories: The repositories to add to the allowed repositories list. The allowed repositories list is used when the `RestrictionMode` is set to `ALLOW_SPECIFIC_REPOSITORIES` .
        """
        pulumi.set(__self__, "restriction_mode", restriction_mode)
        if repositories is not None:
            pulumi.set(__self__, "repositories", repositories)

    @property
    @pulumi.getter(name="restrictionMode")
    def restriction_mode(self) -> 'PackageGroupRestrictionTypeRestrictionMode':
        """
        The package group origin restriction setting. When the value is `INHERIT` , the value is set to the value of the first parent package group which does not have a value of `INHERIT` .
        """
        return pulumi.get(self, "restriction_mode")

    @property
    @pulumi.getter
    def repositories(self) -> Optional[Sequence[str]]:
        """
        The repositories to add to the allowed repositories list. The allowed repositories list is used when the `RestrictionMode` is set to `ALLOW_SPECIFIC_REPOSITORIES` .
        """
        return pulumi.get(self, "repositories")


@pulumi.output_type
class PackageGroupRestrictions(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "externalUpstream":
            suggest = "external_upstream"
        elif key == "internalUpstream":
            suggest = "internal_upstream"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PackageGroupRestrictions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PackageGroupRestrictions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PackageGroupRestrictions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 external_upstream: Optional['outputs.PackageGroupRestrictionType'] = None,
                 internal_upstream: Optional['outputs.PackageGroupRestrictionType'] = None,
                 publish: Optional['outputs.PackageGroupRestrictionType'] = None):
        """
        :param 'PackageGroupRestrictionType' external_upstream: The external upstream restriction determines if new package versions can be ingested or retained from external connections.
        :param 'PackageGroupRestrictionType' internal_upstream: The internal upstream restriction determines if new package versions can be ingested or retained from upstream repositories.
        :param 'PackageGroupRestrictionType' publish: The publish restriction determines if new package versions can be published.
        """
        if external_upstream is not None:
            pulumi.set(__self__, "external_upstream", external_upstream)
        if internal_upstream is not None:
            pulumi.set(__self__, "internal_upstream", internal_upstream)
        if publish is not None:
            pulumi.set(__self__, "publish", publish)

    @property
    @pulumi.getter(name="externalUpstream")
    def external_upstream(self) -> Optional['outputs.PackageGroupRestrictionType']:
        """
        The external upstream restriction determines if new package versions can be ingested or retained from external connections.
        """
        return pulumi.get(self, "external_upstream")

    @property
    @pulumi.getter(name="internalUpstream")
    def internal_upstream(self) -> Optional['outputs.PackageGroupRestrictionType']:
        """
        The internal upstream restriction determines if new package versions can be ingested or retained from upstream repositories.
        """
        return pulumi.get(self, "internal_upstream")

    @property
    @pulumi.getter
    def publish(self) -> Optional['outputs.PackageGroupRestrictionType']:
        """
        The publish restriction determines if new package versions can be published.
        """
        return pulumi.get(self, "publish")


