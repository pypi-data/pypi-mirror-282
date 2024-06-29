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
    'ServerEngineAttribute',
]

@pulumi.output_type
class ServerEngineAttribute(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 value: Optional[str] = None):
        """
        :param str name: The name of the engine attribute.
               
               *Attribute name for Chef Automate servers:*
               
               - `CHEF_AUTOMATE_ADMIN_PASSWORD`
               
               *Attribute names for Puppet Enterprise servers:*
               
               - `PUPPET_ADMIN_PASSWORD`
               - `PUPPET_R10K_REMOTE`
               - `PUPPET_R10K_PRIVATE_KEY`
        :param str value: The value of the engine attribute.
               
               *Attribute value for Chef Automate servers:*
               
               - `CHEF_AUTOMATE_PIVOTAL_KEY` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. You can generate this key by running the following [OpenSSL](https://docs.aws.amazon.com/https://www.openssl.org/) command on Linux-based computers.
               
               `openssl genrsa -out *pivotal_key_file_name* .pem 2048`
               
               On Windows-based computers, you can use the PuTTYgen utility to generate a base64-encoded RSA private key. For more information, see [PuTTYgen - Key Generator for PuTTY on Windows](https://docs.aws.amazon.com/https://www.ssh.com/ssh/putty/windows/puttygen) on SSH.com.
               
               *Attribute values for Puppet Enterprise servers:*
               
               - `PUPPET_ADMIN_PASSWORD` : An administrator password that you can use to sign in to the Puppet Enterprise console webpage after the server is online. The password must use between 8 and 32 ASCII characters.
               - `PUPPET_R10K_REMOTE` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170.
               - `PUPPET_R10K_PRIVATE_KEY` : If you are using a private Git repository, add `PUPPET_R10K_PRIVATE_KEY` to specify a PEM-encoded private SSH key.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the engine attribute.

        *Attribute name for Chef Automate servers:*

        - `CHEF_AUTOMATE_ADMIN_PASSWORD`

        *Attribute names for Puppet Enterprise servers:*

        - `PUPPET_ADMIN_PASSWORD`
        - `PUPPET_R10K_REMOTE`
        - `PUPPET_R10K_PRIVATE_KEY`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value of the engine attribute.

        *Attribute value for Chef Automate servers:*

        - `CHEF_AUTOMATE_PIVOTAL_KEY` : A base64-encoded RSA public key. The corresponding private key is required to access the Chef API. You can generate this key by running the following [OpenSSL](https://docs.aws.amazon.com/https://www.openssl.org/) command on Linux-based computers.

        `openssl genrsa -out *pivotal_key_file_name* .pem 2048`

        On Windows-based computers, you can use the PuTTYgen utility to generate a base64-encoded RSA private key. For more information, see [PuTTYgen - Key Generator for PuTTY on Windows](https://docs.aws.amazon.com/https://www.ssh.com/ssh/putty/windows/puttygen) on SSH.com.

        *Attribute values for Puppet Enterprise servers:*

        - `PUPPET_ADMIN_PASSWORD` : An administrator password that you can use to sign in to the Puppet Enterprise console webpage after the server is online. The password must use between 8 and 32 ASCII characters.
        - `PUPPET_R10K_REMOTE` : The r10k remote is the URL of your control repository (for example, ssh://git@your.git-repo.com:user/control-repo.git). Specifying an r10k remote opens TCP port 8170.
        - `PUPPET_R10K_PRIVATE_KEY` : If you are using a private Git repository, add `PUPPET_R10K_PRIVATE_KEY` to specify a PEM-encoded private SSH key.
        """
        return pulumi.get(self, "value")


