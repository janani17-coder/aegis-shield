# Policy 4: Encryption

**Policy ID:** POL-04  
**Owner:** Security Team  
**Status:** Draft

## 1. Purpose

To protect Aura Workforce information from unauthorized reading or modification while it is stored or transferred.

## 2. Scope

This policy applies to employee records, payroll data, backups, exports, databases, applications, network connections, and systems that store or process sensitive information.

## 3. Rules

1. All connections that transmit Confidential or Restricted data over a network must use approved encrypted protocols, such as HTTPS with current TLS.
2. Confidential and Restricted data stored in databases, backups, and approved file storage must be encrypted using organization-approved encryption methods.
3. Encryption keys must be stored separately from the data they protect and must not be committed to source-code repositories.
4. Access to encryption keys must be limited to authorized personnel and services that require them.
5. Production secrets, private keys, and passwords must not be hard-coded in application source code.
6. Encryption keys must be rotated or replaced according to the organization's key-management schedule and promptly when compromise is suspected.
7. Systems must not use obsolete or explicitly prohibited encryption protocols and algorithms.
8. Sensitive exports must be encrypted during transfer and stored only in approved locations.
9. Security staff must periodically review encryption settings and investigate detected encryption or key-management failures.

## 4. Roles

- **Security Team:** Defines approved encryption and key-management requirements.
- **IT administrators:** Configure encryption and protect keys.
- **Developers:** Use approved encryption libraries and keep secrets out of source code.
- **Data owners:** Confirm that sensitive information is protected appropriately.

## 5. Exceptions

Exceptions require written approval from the system owner and Security Team, a documented reason, compensating controls, and an expiry date. Any applicable legal or regulatory requirement must still be met.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-12, T-19, T-28, and T-29** by protecting sensitive exports, external data transfers, backups, and service credentials.