# Policy 7: Backup & Recovery

**Policy ID:** POL-07  
**Owner:** IT Operations  
**Status:** Draft

## 1. Purpose

To ensure that Aura Workforce information and services can be recovered after data loss, system failure, accidental deletion, or a security incident.

## 2. Scope

This policy applies to databases, payroll records, application configurations, audit logs, and other business-critical systems and information.

## 3. Rules

1. System owners must document which systems and datasets require backups and assign an owner to each backup process.
2. Backup schedules must be based on documented business recovery requirements and approved by the relevant system owner.
3. Confidential and Restricted data in backups must be encrypted using approved encryption methods.
4. Backup access must be restricted to authorized accounts, and backup credentials must be protected separately from the backed-up data.
5. At least one backup copy of critical systems must be protected against unauthorized modification or deletion.
6. Backup jobs must record their status and generate an alert when a critical backup fails.
7. Restoration tests must be performed at least quarterly for critical systems, with results and corrective actions documented.
8. Recovery procedures must identify restoration priorities, responsible personnel, and the required integrity checks.
9. Restored payroll and employee records must be checked for completeness and consistency before the recovered service is returned to normal use.
10. Backup retention and secure disposal must follow documented legal, regulatory, and business requirements.

## 4. Roles

- **IT Operations:** Runs backups and performs restoration tests.
- **System owners:** Define recovery needs and approve restoration priorities.
- **Security Team:** Reviews backup protection and supports recovery from security incidents.
- **Data owners:** Validate recovered data when required.

## 5. Exceptions

Exceptions require written approval from the system owner and Security Team, a documented business reason, compensating controls, and an expiry date. Any applicable legal or regulatory requirement must still be met.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-12, T-15, and T-28** by protecting backups, preserving recovery options, and verifying the integrity of restored records.