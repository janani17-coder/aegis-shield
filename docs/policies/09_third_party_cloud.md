# Policy 9: Third-Party & Cloud Security

**Policy ID:** POL-09  
**Owner:** Security Team  
**Status:** Draft

## 1. Purpose

To ensure that third-party providers and cloud services protect Aura Workforce information and systems appropriately.

## 2. Scope

This policy applies to cloud platforms, software vendors, contractors, external service providers, integrations, and third parties that access or process Aura Workforce data.

## 3. Rules

1. A third party must receive access to Aura Workforce information only after its business purpose, required access, and security risks have been reviewed and approved.
2. Contracts involving Confidential or Restricted data must document applicable security requirements, permitted data use, incident notification, and secure data deletion or return.
3. Third-party access must be limited to the minimum permissions and duration required for the approved service.
4. Multi-factor authentication must be enabled for third-party accounts with administrative access or remote access to sensitive systems.
5. Restricted data must not be uploaded to a third-party service unless the service and intended use have been explicitly approved by the data owner and Security Team.
6. Third-party integrations must use approved authentication methods and protected credentials. Secrets must not be embedded in public source code.
7. Security and privacy risks must be assessed before a new cloud service is used to store or process Confidential or Restricted data.
8. Third-party access and service permissions must be reviewed at least every three months while access remains active.
9. Access must be revoked when a contract ends or the business need expires, and the provider's access removal must be confirmed.
10. Security incidents involving a third party must be reported and handled under the incident response policy and applicable contractual requirements.

## 4. Roles

- **Security Team:** Reviews security risks and approval requirements.
- **Data owners:** Approve permitted uses of their data.
- **Procurement or contract owners:** Ensure relevant security terms are included in agreements.
- **IT administrators:** Configure, review, and revoke third-party access.
- **Third-party providers:** Meet their agreed security obligations.

## 5. Exceptions

Exceptions require written approval from the system or data owner and Security Team, a documented business reason, compensating controls, and an expiry date. Legal and contractual obligations must still be met.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-19, T-28, and T-29** by controlling external data sharing, cloud storage, backup exposure, and third-party credentials.