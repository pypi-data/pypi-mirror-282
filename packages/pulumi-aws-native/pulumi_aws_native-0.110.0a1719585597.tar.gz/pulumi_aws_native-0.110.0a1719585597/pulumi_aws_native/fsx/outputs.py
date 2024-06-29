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
    'DataRepositoryAssociationAutoExportPolicy',
    'DataRepositoryAssociationAutoImportPolicy',
    'DataRepositoryAssociationS3',
]

@pulumi.output_type
class DataRepositoryAssociationAutoExportPolicy(dict):
    """
    Describes a data repository association's automatic export policy. The ``AutoExportPolicy`` defines the types of updated objects on the file system that will be automatically exported to the data repository. As you create, modify, or delete files, Amazon FSx for Lustre automatically exports the defined changes asynchronously once your application finishes modifying the file.
     The ``AutoExportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
    """
    def __init__(__self__, *,
                 events: Sequence['DataRepositoryAssociationEventType']):
        """
        Describes a data repository association's automatic export policy. The ``AutoExportPolicy`` defines the types of updated objects on the file system that will be automatically exported to the data repository. As you create, modify, or delete files, Amazon FSx for Lustre automatically exports the defined changes asynchronously once your application finishes modifying the file.
         The ``AutoExportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
        :param Sequence['DataRepositoryAssociationEventType'] events: The ``AutoExportPolicy`` can have the following event values:
                 +   ``NEW`` - New files and directories are automatically exported to the data repository as they are added to the file system.
                 +   ``CHANGED`` - Changes to files and directories on the file system are automatically exported to the data repository.
                 +   ``DELETED`` - Files and directories are automatically deleted on the data repository when they are deleted on the file system.
                 
                You can define any combination of event types for your ``AutoExportPolicy``.
        """
        pulumi.set(__self__, "events", events)

    @property
    @pulumi.getter
    def events(self) -> Sequence['DataRepositoryAssociationEventType']:
        """
        The ``AutoExportPolicy`` can have the following event values:
          +   ``NEW`` - New files and directories are automatically exported to the data repository as they are added to the file system.
          +   ``CHANGED`` - Changes to files and directories on the file system are automatically exported to the data repository.
          +   ``DELETED`` - Files and directories are automatically deleted on the data repository when they are deleted on the file system.
          
         You can define any combination of event types for your ``AutoExportPolicy``.
        """
        return pulumi.get(self, "events")


@pulumi.output_type
class DataRepositoryAssociationAutoImportPolicy(dict):
    """
    Describes the data repository association's automatic import policy. The AutoImportPolicy defines how Amazon FSx keeps your file metadata and directory listings up to date by importing changes to your Amazon FSx for Lustre file system as you modify objects in a linked S3 bucket.
     The ``AutoImportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
    """
    def __init__(__self__, *,
                 events: Sequence['DataRepositoryAssociationEventType']):
        """
        Describes the data repository association's automatic import policy. The AutoImportPolicy defines how Amazon FSx keeps your file metadata and directory listings up to date by importing changes to your Amazon FSx for Lustre file system as you modify objects in a linked S3 bucket.
         The ``AutoImportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
        :param Sequence['DataRepositoryAssociationEventType'] events: The ``AutoImportPolicy`` can have the following event values:
                 +   ``NEW`` - Amazon FSx automatically imports metadata of files added to the linked S3 bucket that do not currently exist in the FSx file system.
                 +   ``CHANGED`` - Amazon FSx automatically updates file metadata and invalidates existing file content on the file system as files change in the data repository.
                 +   ``DELETED`` - Amazon FSx automatically deletes files on the file system as corresponding files are deleted in the data repository.
                 
                You can define any combination of event types for your ``AutoImportPolicy``.
        """
        pulumi.set(__self__, "events", events)

    @property
    @pulumi.getter
    def events(self) -> Sequence['DataRepositoryAssociationEventType']:
        """
        The ``AutoImportPolicy`` can have the following event values:
          +   ``NEW`` - Amazon FSx automatically imports metadata of files added to the linked S3 bucket that do not currently exist in the FSx file system.
          +   ``CHANGED`` - Amazon FSx automatically updates file metadata and invalidates existing file content on the file system as files change in the data repository.
          +   ``DELETED`` - Amazon FSx automatically deletes files on the file system as corresponding files are deleted in the data repository.
          
         You can define any combination of event types for your ``AutoImportPolicy``.
        """
        return pulumi.get(self, "events")


@pulumi.output_type
class DataRepositoryAssociationS3(dict):
    """
    The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "autoExportPolicy":
            suggest = "auto_export_policy"
        elif key == "autoImportPolicy":
            suggest = "auto_import_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DataRepositoryAssociationS3. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DataRepositoryAssociationS3.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DataRepositoryAssociationS3.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auto_export_policy: Optional['outputs.DataRepositoryAssociationAutoExportPolicy'] = None,
                 auto_import_policy: Optional['outputs.DataRepositoryAssociationAutoImportPolicy'] = None):
        """
        The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.
        :param 'DataRepositoryAssociationAutoExportPolicy' auto_export_policy: Describes a data repository association's automatic export policy. The ``AutoExportPolicy`` defines the types of updated objects on the file system that will be automatically exported to the data repository. As you create, modify, or delete files, Amazon FSx for Lustre automatically exports the defined changes asynchronously once your application finishes modifying the file.
                The ``AutoExportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
        :param 'DataRepositoryAssociationAutoImportPolicy' auto_import_policy: Describes the data repository association's automatic import policy. The AutoImportPolicy defines how Amazon FSx keeps your file metadata and directory listings up to date by importing changes to your Amazon FSx for Lustre file system as you modify objects in a linked S3 bucket.
                The ``AutoImportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
        """
        if auto_export_policy is not None:
            pulumi.set(__self__, "auto_export_policy", auto_export_policy)
        if auto_import_policy is not None:
            pulumi.set(__self__, "auto_import_policy", auto_import_policy)

    @property
    @pulumi.getter(name="autoExportPolicy")
    def auto_export_policy(self) -> Optional['outputs.DataRepositoryAssociationAutoExportPolicy']:
        """
        Describes a data repository association's automatic export policy. The ``AutoExportPolicy`` defines the types of updated objects on the file system that will be automatically exported to the data repository. As you create, modify, or delete files, Amazon FSx for Lustre automatically exports the defined changes asynchronously once your application finishes modifying the file.
         The ``AutoExportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
        """
        return pulumi.get(self, "auto_export_policy")

    @property
    @pulumi.getter(name="autoImportPolicy")
    def auto_import_policy(self) -> Optional['outputs.DataRepositoryAssociationAutoImportPolicy']:
        """
        Describes the data repository association's automatic import policy. The AutoImportPolicy defines how Amazon FSx keeps your file metadata and directory listings up to date by importing changes to your Amazon FSx for Lustre file system as you modify objects in a linked S3 bucket.
         The ``AutoImportPolicy`` is only supported on Amazon FSx for Lustre file systems with a data repository association.
        """
        return pulumi.get(self, "auto_import_policy")


