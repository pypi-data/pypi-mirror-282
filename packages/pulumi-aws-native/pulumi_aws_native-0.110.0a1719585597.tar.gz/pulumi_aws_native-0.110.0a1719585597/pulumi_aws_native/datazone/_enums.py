# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DataSourceEnableSetting',
    'DataSourceFilterExpressionType',
    'DataSourceStatus',
    'DomainAuthType',
    'DomainStatus',
    'DomainUserAssignment',
    'EnvironmentStatus',
    'GroupProfileStatus',
    'ProjectMembershipUserDesignation',
    'UserProfileStatus',
    'UserProfileType',
    'UserProfileUserType',
]


class DataSourceEnableSetting(str, Enum):
    """
    Specifies whether the data source is enabled.
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class DataSourceFilterExpressionType(str, Enum):
    """
    The search filter expression type.
    """
    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"


class DataSourceStatus(str, Enum):
    """
    The status of the data source.
    """
    CREATING = "CREATING"
    FAILED_CREATION = "FAILED_CREATION"
    READY = "READY"
    UPDATING = "UPDATING"
    FAILED_UPDATE = "FAILED_UPDATE"
    RUNNING = "RUNNING"
    DELETING = "DELETING"
    FAILED_DELETION = "FAILED_DELETION"


class DomainAuthType(str, Enum):
    """
    The type of single sign-on in Amazon DataZone.
    """
    IAM_IDC = "IAM_IDC"
    DISABLED = "DISABLED"


class DomainStatus(str, Enum):
    """
    The status of the Amazon DataZone domain.
    """
    CREATING = "CREATING"
    AVAILABLE = "AVAILABLE"
    CREATION_FAILED = "CREATION_FAILED"
    DELETING = "DELETING"
    DELETED = "DELETED"
    DELETION_FAILED = "DELETION_FAILED"


class DomainUserAssignment(str, Enum):
    """
    The single sign-on user assignment in Amazon DataZone.
    """
    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"


class EnvironmentStatus(str, Enum):
    """
    The status of the Amazon DataZone environment.
    """
    ACTIVE = "ACTIVE"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    DELETE_FAILED = "DELETE_FAILED"
    VALIDATION_FAILED = "VALIDATION_FAILED"
    SUSPENDED = "SUSPENDED"
    DISABLED = "DISABLED"
    EXPIRED = "EXPIRED"
    DELETED = "DELETED"
    INACCESSIBLE = "INACCESSIBLE"


class GroupProfileStatus(str, Enum):
    """
    The status of the group profile.
    """
    ASSIGNED = "ASSIGNED"
    NOT_ASSIGNED = "NOT_ASSIGNED"


class ProjectMembershipUserDesignation(str, Enum):
    PROJECT_OWNER = "PROJECT_OWNER"
    PROJECT_CONTRIBUTOR = "PROJECT_CONTRIBUTOR"


class UserProfileStatus(str, Enum):
    """
    The status of the user profile.
    """
    ASSIGNED = "ASSIGNED"
    NOT_ASSIGNED = "NOT_ASSIGNED"
    ACTIVATED = "ACTIVATED"
    DEACTIVATED = "DEACTIVATED"


class UserProfileType(str, Enum):
    """
    The type of the user profile.
    """
    IAM = "IAM"
    SSO = "SSO"


class UserProfileUserType(str, Enum):
    """
    The type of the user.
    """
    IAM_USER = "IAM_USER"
    IAM_ROLE = "IAM_ROLE"
    SSO_USER = "SSO_USER"
