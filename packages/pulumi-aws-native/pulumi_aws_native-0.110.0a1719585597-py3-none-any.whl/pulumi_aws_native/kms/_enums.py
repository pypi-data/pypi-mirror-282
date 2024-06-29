# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'KeyOrigin',
    'KeySpec',
    'KeyUsage',
]


class KeyOrigin(str, Enum):
    """
    The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is ``AWS_KMS``, which means that KMS creates the key material.
     To [create a KMS key with no key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html) (for imported key material), set this value to ``EXTERNAL``. For more information about importing key material into KMS, see [Importing Key Material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the *Developer Guide*.
     You can ignore ``ENABLED`` when Origin is ``EXTERNAL``. When a KMS key with Origin ``EXTERNAL`` is created, the key state is ``PENDING_IMPORT`` and ``ENABLED`` is ``false``. After you import the key material, ``ENABLED`` updated to ``true``. The KMS key can then be used for Cryptographic Operations. 
       CFN doesn't support creating an ``Origin`` parameter of the ``AWS_CLOUDHSM`` or ``EXTERNAL_KEY_STORE`` values.
    """
    AWS_KMS = "AWS_KMS"
    EXTERNAL = "EXTERNAL"


class KeySpec(str, Enum):
    """
    Specifies the type of KMS key to create. The default value, ``SYMMETRIC_DEFAULT``, creates a KMS key with a 256-bit symmetric key for encryption and decryption. In China Regions, ``SYMMETRIC_DEFAULT`` creates a 128-bit symmetric key that uses SM4 encryption. You can't change the ``KeySpec`` value after the KMS key is created. For help choosing a key spec for your KMS key, see [Choosing a KMS key type](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose.html) in the *Developer Guide*.
     The ``KeySpec`` property determines the type of key material in the KMS key and the algorithms that the KMS key supports. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see [condition keys](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms) in the *Developer Guide*.
      If you change the value of the ``KeySpec`` property on an existing KMS key, the update request fails, regardless of the value of the [UpdateReplacePolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.
        [services that are integrated with](https://docs.aws.amazon.com/kms/features/#AWS_Service_Integration) use symmetric encryption KMS keys to protect your data. These services do not support encryption with asymmetric KMS keys. For help determining whether a KMS key is asymmetric, see [Identifying asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/find-symm-asymm.html) in the *Developer Guide*.
       KMS supports the following key specs for KMS keys:
      +  Symmetric encryption key (default)
      +   ``SYMMETRIC_DEFAULT`` (AES-256-GCM)
      
      +  HMAC keys (symmetric)
      +   ``HMAC_224`` 
      +   ``HMAC_256`` 
      +   ``HMAC_384`` 
      +   ``HMAC_512`` 
      
      +  Asymmetric RSA key pairs
      +   ``RSA_2048`` 
      +   ``RSA_3072`` 
      +   ``RSA_4096`` 
      
      +  Asymmetric NIST-recommended elliptic curve key pairs
      +   ``ECC_NIST_P256`` (secp256r1)
      +   ``ECC_NIST_P384`` (secp384r1)
      +   ``ECC_NIST_P521`` (secp521r1)
      
      +  Other asymmetric elliptic curve key pairs
      +   ``ECC_SECG_P256K1`` (secp256k1), commonly used for cryptocurrencies.
      
      +  SM2 key pairs (China Regions only)
      +   ``SM2``
    """
    SYMMETRIC_DEFAULT = "SYMMETRIC_DEFAULT"
    RSA2048 = "RSA_2048"
    RSA3072 = "RSA_3072"
    RSA4096 = "RSA_4096"
    ECC_NIST_P256 = "ECC_NIST_P256"
    ECC_NIST_P384 = "ECC_NIST_P384"
    ECC_NIST_P521 = "ECC_NIST_P521"
    ECC_SECG_P256K1 = "ECC_SECG_P256K1"
    HMAC224 = "HMAC_224"
    HMAC256 = "HMAC_256"
    HMAC384 = "HMAC_384"
    HMAC512 = "HMAC_512"
    SM2 = "SM2"


class KeyUsage(str, Enum):
    """
    Determines the [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) for which you can use the KMS key. The default value is ``ENCRYPT_DECRYPT``. This property is required for asymmetric KMS keys and HMAC KMS keys. You can't change the ``KeyUsage`` value after the KMS key is created.
      If you change the value of the ``KeyUsage`` property on an existing KMS key, the update request fails, regardless of the value of the [UpdateReplacePolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html). This prevents you from accidentally deleting a KMS key by changing an immutable property value.
      Select only one valid value.
      +  For symmetric encryption KMS keys, omit the property or specify ``ENCRYPT_DECRYPT``.
      +  For asymmetric KMS keys with RSA key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY``.
      +  For asymmetric KMS keys with ECC key material, specify ``SIGN_VERIFY``.
      +  For asymmetric KMS keys with SM2 (China Regions only) key material, specify ``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY``.
      +  For HMAC KMS keys, specify ``GENERATE_VERIFY_MAC``.
    """
    ENCRYPT_DECRYPT = "ENCRYPT_DECRYPT"
    SIGN_VERIFY = "SIGN_VERIFY"
    GENERATE_VERIFY_MAC = "GENERATE_VERIFY_MAC"
    KEY_AGREEMENT = "KEY_AGREEMENT"
