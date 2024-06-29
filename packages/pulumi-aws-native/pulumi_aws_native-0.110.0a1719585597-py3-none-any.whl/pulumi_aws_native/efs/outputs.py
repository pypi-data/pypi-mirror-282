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
    'AccessPointCreationInfo',
    'AccessPointPosixUser',
    'AccessPointRootDirectory',
    'FileSystemBackupPolicy',
    'FileSystemLifecyclePolicy',
    'FileSystemProtection',
    'FileSystemReplicationConfiguration',
    'FileSystemReplicationDestination',
]

@pulumi.output_type
class AccessPointCreationInfo(dict):
    """
    Required if the ``RootDirectory`` > ``Path`` specified does not exist. Specifies the POSIX IDs and permissions to apply to the access point's ``RootDirectory`` > ``Path``. If the access point root directory does not exist, EFS creates it with these settings when a client connects to the access point. When specifying ``CreationInfo``, you must include values for all properties. 
     Amazon EFS creates a root directory only if you have provided the CreationInfo: OwnUid, OwnGID, and permissions for the directory. If you do not provide this information, Amazon EFS does not create the root directory. If the root directory does not exist, attempts to mount using the access point will fail.
      If you do not provide ``CreationInfo`` and the specified ``RootDirectory`` does not exist, attempts to mount the file system using the access point will fail.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ownerGid":
            suggest = "owner_gid"
        elif key == "ownerUid":
            suggest = "owner_uid"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPointCreationInfo. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPointCreationInfo.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPointCreationInfo.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 owner_gid: str,
                 owner_uid: str,
                 permissions: str):
        """
        Required if the ``RootDirectory`` > ``Path`` specified does not exist. Specifies the POSIX IDs and permissions to apply to the access point's ``RootDirectory`` > ``Path``. If the access point root directory does not exist, EFS creates it with these settings when a client connects to the access point. When specifying ``CreationInfo``, you must include values for all properties. 
         Amazon EFS creates a root directory only if you have provided the CreationInfo: OwnUid, OwnGID, and permissions for the directory. If you do not provide this information, Amazon EFS does not create the root directory. If the root directory does not exist, attempts to mount using the access point will fail.
          If you do not provide ``CreationInfo`` and the specified ``RootDirectory`` does not exist, attempts to mount the file system using the access point will fail.
        :param str owner_gid: Specifies the POSIX group ID to apply to the ``RootDirectory``. Accepts values from 0 to 2^32 (4294967295).
        :param str owner_uid: Specifies the POSIX user ID to apply to the ``RootDirectory``. Accepts values from 0 to 2^32 (4294967295).
        :param str permissions: Specifies the POSIX permissions to apply to the ``RootDirectory``, in the format of an octal number representing the file's mode bits.
        """
        pulumi.set(__self__, "owner_gid", owner_gid)
        pulumi.set(__self__, "owner_uid", owner_uid)
        pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter(name="ownerGid")
    def owner_gid(self) -> str:
        """
        Specifies the POSIX group ID to apply to the ``RootDirectory``. Accepts values from 0 to 2^32 (4294967295).
        """
        return pulumi.get(self, "owner_gid")

    @property
    @pulumi.getter(name="ownerUid")
    def owner_uid(self) -> str:
        """
        Specifies the POSIX user ID to apply to the ``RootDirectory``. Accepts values from 0 to 2^32 (4294967295).
        """
        return pulumi.get(self, "owner_uid")

    @property
    @pulumi.getter
    def permissions(self) -> str:
        """
        Specifies the POSIX permissions to apply to the ``RootDirectory``, in the format of an octal number representing the file's mode bits.
        """
        return pulumi.get(self, "permissions")


@pulumi.output_type
class AccessPointPosixUser(dict):
    """
    The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "secondaryGids":
            suggest = "secondary_gids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPointPosixUser. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPointPosixUser.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPointPosixUser.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 gid: str,
                 uid: str,
                 secondary_gids: Optional[Sequence[str]] = None):
        """
        The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point.
        :param str gid: The POSIX group ID used for all file system operations using this access point.
        :param str uid: The POSIX user ID used for all file system operations using this access point.
        :param Sequence[str] secondary_gids: Secondary POSIX group IDs used for all file system operations using this access point.
        """
        pulumi.set(__self__, "gid", gid)
        pulumi.set(__self__, "uid", uid)
        if secondary_gids is not None:
            pulumi.set(__self__, "secondary_gids", secondary_gids)

    @property
    @pulumi.getter
    def gid(self) -> str:
        """
        The POSIX group ID used for all file system operations using this access point.
        """
        return pulumi.get(self, "gid")

    @property
    @pulumi.getter
    def uid(self) -> str:
        """
        The POSIX user ID used for all file system operations using this access point.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[Sequence[str]]:
        """
        Secondary POSIX group IDs used for all file system operations using this access point.
        """
        return pulumi.get(self, "secondary_gids")


@pulumi.output_type
class AccessPointRootDirectory(dict):
    """
    Specifies the directory on the Amazon EFS file system that the access point provides access to. The access point exposes the specified file system path as the root directory of your file system to applications using the access point. NFS clients using the access point can only access data in the access point's ``RootDirectory`` and its subdirectories.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "creationInfo":
            suggest = "creation_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPointRootDirectory. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPointRootDirectory.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPointRootDirectory.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 creation_info: Optional['outputs.AccessPointCreationInfo'] = None,
                 path: Optional[str] = None):
        """
        Specifies the directory on the Amazon EFS file system that the access point provides access to. The access point exposes the specified file system path as the root directory of your file system to applications using the access point. NFS clients using the access point can only access data in the access point's ``RootDirectory`` and its subdirectories.
        :param 'AccessPointCreationInfo' creation_info: (Optional) Specifies the POSIX IDs and permissions to apply to the access point's ``RootDirectory``. If the ``RootDirectory`` > ``Path`` specified does not exist, EFS creates the root directory using the ``CreationInfo`` settings when a client connects to an access point. When specifying the ``CreationInfo``, you must provide values for all properties. 
                 If you do not provide ``CreationInfo`` and the specified ``RootDirectory`` > ``Path`` does not exist, attempts to mount the file system using the access point will fail.
        :param str path: Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the ``CreationInfo``.
        """
        if creation_info is not None:
            pulumi.set(__self__, "creation_info", creation_info)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="creationInfo")
    def creation_info(self) -> Optional['outputs.AccessPointCreationInfo']:
        """
        (Optional) Specifies the POSIX IDs and permissions to apply to the access point's ``RootDirectory``. If the ``RootDirectory`` > ``Path`` specified does not exist, EFS creates the root directory using the ``CreationInfo`` settings when a client connects to an access point. When specifying the ``CreationInfo``, you must provide values for all properties. 
          If you do not provide ``CreationInfo`` and the specified ``RootDirectory`` > ``Path`` does not exist, attempts to mount the file system using the access point will fail.
        """
        return pulumi.get(self, "creation_info")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        Specifies the path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide the ``CreationInfo``.
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class FileSystemBackupPolicy(dict):
    """
    The backup policy turns automatic backups for the file system on or off.
    """
    def __init__(__self__, *,
                 status: 'FileSystemBackupPolicyStatus'):
        """
        The backup policy turns automatic backups for the file system on or off.
        :param 'FileSystemBackupPolicyStatus' status: Set the backup policy status for the file system.
                 +   *ENABLED* - Turns automatic backups on for the file system. 
                 +   *DISABLED* - Turns automatic backups off for the file system.
        """
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def status(self) -> 'FileSystemBackupPolicyStatus':
        """
        Set the backup policy status for the file system.
          +   *ENABLED* - Turns automatic backups on for the file system. 
          +   *DISABLED* - Turns automatic backups off for the file system.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class FileSystemLifecyclePolicy(dict):
    """
    Describes a policy used by Lifecycle management that specifies when to transition files into and out of the EFS storage classes. For more information, see [Managing file system storage](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html).
      + Each ``LifecyclePolicy`` object can have only a single transition. This means that in a request body, ``LifecyclePolicies`` must be structured as an array of ``LifecyclePolicy`` objects, one object for each transition, ``TransitionToIA``, ``TransitionToArchive``, ``TransitionToPrimaryStorageClass``.
     + See the AWS::EFS::FileSystem examples for the correct ``LifecyclePolicy`` structure. Do not use the syntax shown on this page.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "transitionToArchive":
            suggest = "transition_to_archive"
        elif key == "transitionToIa":
            suggest = "transition_to_ia"
        elif key == "transitionToPrimaryStorageClass":
            suggest = "transition_to_primary_storage_class"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FileSystemLifecyclePolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FileSystemLifecyclePolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FileSystemLifecyclePolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 transition_to_archive: Optional[str] = None,
                 transition_to_ia: Optional[str] = None,
                 transition_to_primary_storage_class: Optional[str] = None):
        """
        Describes a policy used by Lifecycle management that specifies when to transition files into and out of the EFS storage classes. For more information, see [Managing file system storage](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html).
          + Each ``LifecyclePolicy`` object can have only a single transition. This means that in a request body, ``LifecyclePolicies`` must be structured as an array of ``LifecyclePolicy`` objects, one object for each transition, ``TransitionToIA``, ``TransitionToArchive``, ``TransitionToPrimaryStorageClass``.
         + See the AWS::EFS::FileSystem examples for the correct ``LifecyclePolicy`` structure. Do not use the syntax shown on this page.
        :param str transition_to_archive: The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.
        :param str transition_to_ia: The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Infrequent Access (IA) storage. Metadata operations such as listing the contents of a directory don't count as file access events.
        :param str transition_to_primary_storage_class: Whether to move files back to primary (Standard) storage after they are accessed in IA or Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.
        """
        if transition_to_archive is not None:
            pulumi.set(__self__, "transition_to_archive", transition_to_archive)
        if transition_to_ia is not None:
            pulumi.set(__self__, "transition_to_ia", transition_to_ia)
        if transition_to_primary_storage_class is not None:
            pulumi.set(__self__, "transition_to_primary_storage_class", transition_to_primary_storage_class)

    @property
    @pulumi.getter(name="transitionToArchive")
    def transition_to_archive(self) -> Optional[str]:
        """
        The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.
        """
        return pulumi.get(self, "transition_to_archive")

    @property
    @pulumi.getter(name="transitionToIa")
    def transition_to_ia(self) -> Optional[str]:
        """
        The number of days after files were last accessed in primary storage (the Standard storage class) at which to move them to Infrequent Access (IA) storage. Metadata operations such as listing the contents of a directory don't count as file access events.
        """
        return pulumi.get(self, "transition_to_ia")

    @property
    @pulumi.getter(name="transitionToPrimaryStorageClass")
    def transition_to_primary_storage_class(self) -> Optional[str]:
        """
        Whether to move files back to primary (Standard) storage after they are accessed in IA or Archive storage. Metadata operations such as listing the contents of a directory don't count as file access events.
        """
        return pulumi.get(self, "transition_to_primary_storage_class")


@pulumi.output_type
class FileSystemProtection(dict):
    """
    Describes the protection on the file system.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "replicationOverwriteProtection":
            suggest = "replication_overwrite_protection"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FileSystemProtection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FileSystemProtection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FileSystemProtection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 replication_overwrite_protection: Optional['FileSystemProtectionReplicationOverwriteProtection'] = None):
        """
        Describes the protection on the file system.
        :param 'FileSystemProtectionReplicationOverwriteProtection' replication_overwrite_protection: The status of the file system's replication overwrite protection.
                 +   ``ENABLED`` – The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is ``ENABLED`` by default. 
                 +   ``DISABLED`` – The file system can be used as the destination file system in a replication configuration. The file system is read-only and can only be modified by EFS replication.
                 +   ``REPLICATING`` – The file system is being used as the destination file system in a replication configuration. The file system is read-only and is only modified only by EFS replication.
                 
                If the replication configuration is deleted, the file system's replication overwrite protection is re-enabled, the file system becomes writeable.
        """
        if replication_overwrite_protection is not None:
            pulumi.set(__self__, "replication_overwrite_protection", replication_overwrite_protection)

    @property
    @pulumi.getter(name="replicationOverwriteProtection")
    def replication_overwrite_protection(self) -> Optional['FileSystemProtectionReplicationOverwriteProtection']:
        """
        The status of the file system's replication overwrite protection.
          +   ``ENABLED`` – The file system cannot be used as the destination file system in a replication configuration. The file system is writeable. Replication overwrite protection is ``ENABLED`` by default. 
          +   ``DISABLED`` – The file system can be used as the destination file system in a replication configuration. The file system is read-only and can only be modified by EFS replication.
          +   ``REPLICATING`` – The file system is being used as the destination file system in a replication configuration. The file system is read-only and is only modified only by EFS replication.
          
         If the replication configuration is deleted, the file system's replication overwrite protection is re-enabled, the file system becomes writeable.
        """
        return pulumi.get(self, "replication_overwrite_protection")


@pulumi.output_type
class FileSystemReplicationConfiguration(dict):
    """
    Describes the replication configuration for a specific file system.
    """
    def __init__(__self__, *,
                 destinations: Optional[Sequence['outputs.FileSystemReplicationDestination']] = None):
        """
        Describes the replication configuration for a specific file system.
        :param Sequence['FileSystemReplicationDestination'] destinations: An array of destination objects. Only one destination object is supported.
        """
        if destinations is not None:
            pulumi.set(__self__, "destinations", destinations)

    @property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence['outputs.FileSystemReplicationDestination']]:
        """
        An array of destination objects. Only one destination object is supported.
        """
        return pulumi.get(self, "destinations")


@pulumi.output_type
class FileSystemReplicationDestination(dict):
    """
    Describes the destination file system in the replication configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "availabilityZoneName":
            suggest = "availability_zone_name"
        elif key == "fileSystemId":
            suggest = "file_system_id"
        elif key == "kmsKeyId":
            suggest = "kms_key_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FileSystemReplicationDestination. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FileSystemReplicationDestination.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FileSystemReplicationDestination.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 availability_zone_name: Optional[str] = None,
                 file_system_id: Optional[str] = None,
                 kms_key_id: Optional[str] = None,
                 region: Optional[str] = None):
        """
        Describes the destination file system in the replication configuration.
        :param str availability_zone_name: The AWS For One Zone file systems, the replication configuration must specify the Availability Zone in which the destination file system is located. 
                Use the format ``us-east-1a`` to specify the Availability Zone. For more information about One Zone file systems, see [EFS file system types](https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html) in the *Amazon EFS User Guide*.
                 One Zone file system type is not available in all Availability Zones in AWS-Regions where Amazon EFS is available.
        :param str file_system_id: The ID of the destination Amazon EFS file system.
        :param str kms_key_id: The ID of an kms-key-long used to protect the encrypted file system.
        :param str region: The AWS-Region in which the destination file system is located.
                 For One Zone file systems, the replication configuration must specify the AWS-Region in which the destination file system is located.
        """
        if availability_zone_name is not None:
            pulumi.set(__self__, "availability_zone_name", availability_zone_name)
        if file_system_id is not None:
            pulumi.set(__self__, "file_system_id", file_system_id)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> Optional[str]:
        """
        The AWS For One Zone file systems, the replication configuration must specify the Availability Zone in which the destination file system is located. 
         Use the format ``us-east-1a`` to specify the Availability Zone. For more information about One Zone file systems, see [EFS file system types](https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html) in the *Amazon EFS User Guide*.
          One Zone file system type is not available in all Availability Zones in AWS-Regions where Amazon EFS is available.
        """
        return pulumi.get(self, "availability_zone_name")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[str]:
        """
        The ID of the destination Amazon EFS file system.
        """
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The ID of an kms-key-long used to protect the encrypted file system.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The AWS-Region in which the destination file system is located.
          For One Zone file systems, the replication configuration must specify the AWS-Region in which the destination file system is located.
        """
        return pulumi.get(self, "region")


