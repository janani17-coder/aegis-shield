# Policy 1: Access Control & Least Privilege

**Policy ID:** POL-01  
**Owner:** Security Team  
**Status:** Draft

## 1. Purpose

To ensure that employees and systems can access only the information and functions required for their work.

## 2. Scope

This policy applies to all Aura Workforce users, administrators, applications, service accounts, and systems that access employee, HR, or payroll data.

## 3. Rules

1. All users must sign in with an individually assigned account. Shared user accounts are prohibited unless formally approved for a documented technical need.
2. Access to employee and payroll records must be checked on the server for every request. Users must not access another employee's records without authorization.
3. Access permissions must follow least privilege. Users may receive only the permissions needed for their assigned duties.
4. Administrator accounts must use multi-factor authentication (MFA).
5. HR and payroll permissions must be separated according to job responsibilities. Users must not approve their own sensitive payroll changes.
6. Managers or designated data owners must review privileged and payroll access at least every three months.
7. Access must be removed or updated within one business day after an employee leaves or changes roles, once the change is confirmed by HR.
8. Service accounts must have a documented owner and purpose. They must not use shared human-user credentials or unnecessary administrator privileges.
9. Access grants, permission changes, and removals must be recorded in an audit log.

## 4. Roles

- **Security Team:** Defines access-control requirements and reviews violations.
- **Managers and data owners:** Approve access according to job responsibilities.
- **IT administrators:** Implement approved permissions and remove outdated access.
- **Users:** Protect their accounts and report unexpected access.

## 5. Exceptions

Exceptions require written approval from the system owner and Security Team, a documented reason, compensating controls, and an expiry date. Exceptions must be reviewed before renewal.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-03, T-08, T-24, and T-29** through server-side authorization, least privilege, access reviews, and service-account controls.