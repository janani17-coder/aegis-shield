# Policy 2: Passwords & Multi-Factor Authentication (MFA)

**Policy ID:** POL-02  
**Owner:** Security Team  
**Status:** Draft

## 1. Purpose

To protect Aura Workforce accounts from unauthorized access by requiring strong authentication.

## 2. Scope

This policy applies to employees, administrators, contractors, service accounts, and anyone accessing Aura Workforce systems.

## 3. Rules

1. Administrator accounts and remote access accounts must use multi-factor authentication (MFA).
2. Passwords must be at least 15 characters long when used as the single authentication factor.
3. Systems must block commonly used, known-compromised, or easily guessed passwords.
4. Users must not share passwords or reuse their work passwords for personal accounts.
5. Users must store passwords in an organization-approved password manager when one is available.
6. Systems must limit repeated failed sign-in attempts and generate an alert when the configured threshold is reached.
7. Passwords must be changed promptly when compromise is suspected or confirmed. Routine password changes are not required unless risk or applicable standards require them.
8. Recovery codes and authentication reset requests must be protected and verified before access is restored.
9. Default passwords must be changed before a system or account is put into service.
10. Security or IT staff must review authentication alerts and investigate suspicious sign-in activity according to the incident response process.

## 4. Roles

- **Security Team:** Defines authentication requirements and monitors suspicious activity.
- **IT administrators:** Configure MFA, password controls, and sign-in protections.
- **Users:** Keep authentication information private and report suspected compromise.
- **Managers:** Ensure team members follow this policy.

## 5. Exceptions

Exceptions require written approval from the system owner and Security Team, a documented reason, compensating controls, and an expiry date. Exceptions must be reviewed before renewal.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-03, T-08, and T-29** by strengthening account protection and reducing the risk of unauthorized access.