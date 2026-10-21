# Policy 5: Logging & Monitoring

**Policy ID:** POL-05  
**Owner:** Security Team  
**Status:** Draft

## 1. Purpose

To record important security events, detect suspicious activity, and support investigations into incidents involving Aura Workforce.

## 2. Scope

This policy applies to authentication systems, applications, APIs, databases, payroll services, administrator activities, and systems that process sensitive information.

## 3. Rules

1. Systems must log successful and failed sign-in events, including timestamps, account identifiers, and source information when available.
2. Systems must record access-denied events and authorization failures involving employee or payroll records.
3. Changes to user permissions, privileged accounts, payroll data, and security settings must be recorded in audit logs.
4. Each security event must include a timestamp and sufficient information to identify the affected account, system, and action.
5. Logs must not contain passwords, authentication tokens, encryption keys, or unnecessary Confidential or Restricted information.
6. Access to security logs must be restricted to authorized personnel, and attempts to alter or delete protected audit records must be detectable.
7. Security alerts must be configured for repeated failed sign-ins, unexpected privilege changes, suspicious payroll activity, and unusual access to sensitive records.
8. Security staff must review alerts according to the approved monitoring schedule and document investigation outcomes.
9. Log retention periods must be documented and follow legal, regulatory, and business requirements.
10. Log collection failures affecting critical security monitoring must generate an alert for investigation.

## 4. Roles

- **Security Team:** Defines monitoring requirements and investigates alerts.
- **IT administrators:** Maintain log collection, access controls, and retention settings.
- **System owners:** Ensure their systems produce the required events.
- **Incident responders:** Preserve relevant logs during investigations.

## 5. Exceptions

Exceptions require written approval from the system owner and Security Team, a documented reason, compensating controls, and an expiry date. Required audit records must not be disabled without an approved alternative.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-03, T-09, T-11, T-12, and T-15** by recording unauthorized access attempts, sensitive data changes, exports, and payroll-related activity.