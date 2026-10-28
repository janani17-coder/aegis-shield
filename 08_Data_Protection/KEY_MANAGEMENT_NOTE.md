# Task 8 — Key Management and Encryption at Rest

## 1. Purpose

This note explains how to protect encryption keys used for sensitive employee data, including salary and bank-account-style fields. The accompanying Python script is a local learning demonstration using the Fernet authenticated-encryption API.

## 2. Key storage

**Demo environment:** The script generates a key and stores it in `08_Data_Protection/demo.key`. The key is excluded from Git through `.gitignore`. This is suitable only for a controlled local demonstration, not production storage. File permissions alone do not provide complete protection on every operating system.

**Production environment:** Store keys in a managed Key Management Service (KMS), Hardware Security Module (HSM), or approved secrets-management platform. Keep keys separate from encrypted data and source code. Do not place production keys in Git, application logs, screenshots, or ordinary configuration files.

## 3. Access control

Access to decrypt sensitive data should be granted only to approved services and personnel with a documented business need. Use least privilege, role-based access controls, strong authentication, and audit logging.

Developers, general users, unrelated administrators, and database operators should not automatically have permission to retrieve plaintext data or export encryption keys. Separate key administration from routine data access where practical.

## 4. Key rotation and recovery

Establish a documented rotation schedule based on organizational policy, risk, and the KMS provider's guidance. Rotate keys immediately when compromise is suspected or confirmed.

Use key versioning and a controlled re-encryption or key-wrapping process so authorized services can continue to access existing data during rotation. Retain old key versions only as long as required to decrypt data that still depends on them, and securely retire them when no longer needed. Test recovery procedures and maintain approved backups of key-management configuration.

## 5. Encryption limitations

Encryption at rest protects stored data against certain forms of unauthorized access when strong encryption and effective key controls are in place. It does not automatically protect plaintext while an authorized application is processing it, prevent misuse by an authorized account, or stop data theft from a compromised application that can decrypt the data. It does not replace access control, monitoring, secure backups, or endpoint security.

## 6. Five-line summary

1. Encryption at rest protects stored data by keeping it unreadable without the required key.
2. It can reduce exposure if storage media, backups, or files are stolen.
3. It does not protect plaintext while an application is using or displaying it.
4. It cannot prevent all misuse by authorized users or a compromised service with decryption access.
5. Key storage, access control, rotation, monitoring, and recovery procedures are essential.

## 7. Production recommendation

Use a managed KMS or HSM with audited access, least privilege, key versioning, and controlled rotation. No person or service should receive broad key access merely because they can access the database. Test the process and document approvals before production deployment.

**Scope note:** This document describes recommended controls; it does not claim that production key-management infrastructure has been configured or tested.
