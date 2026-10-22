# Policy 1: Access Control & Least Privilege

**Policy ID:** POL-01  
**Owner:** Security Team  
**Status:** Draft

## 1. Purpose

This policy ensures that employees and other approved users can access only the information and systems they need to do their work. Limiting access helps protect sensitive information and prevents unauthorized changes.

## 2. Scope

This policy applies to all employees, contractors, administrators, and service accounts that access the organization's systems or information. It covers access to applications, databases, files, and other company resources.

## 3. Rules

1. Every user must have their own account. Sharing accounts is not allowed unless a documented technical need is formally approved.

2. The system must check each request to access employee or payroll records. Users may access another employee's records only when they have permission to do so.

3. Users must receive only the access permissions they need to perform their assigned work. They must not receive extra permissions without a valid, approved reason.

4. Administrator accounts must use multi-factor authentication (MFA), which means confirming identity using an additional verification step beyond a password.

5. HR and payroll access must be assigned according to each person's job responsibilities. Users must not approve their own sensitive payroll changes.

6. Managers or assigned data owners must review administrator access and payroll permissions at least once every three months.

7. When HR confirms that an employee has left the organization or changed roles, their access must be removed or updated within one business day.

8. Every service account (an account used by an application or system rather than a person) must have a documented owner and purpose. It must not use a human user's shared login details or have unnecessary administrator permissions.

9. All access approvals, permission changes, and access removals must be recorded in a log so they can be reviewed later.

## 4. Roles

- **Employees and contractors:** Use only the accounts and information they are approved to access. Never share account credentials.
- **Managers:** Approve access based on job responsibilities and review access when required.
- **HR:** Confirm employee departures and role changes promptly so access can be updated.
- **IT and Security teams:** Create, change, and remove access permissions; protect administrator accounts; and maintain access logs.
- **Data owners:** Confirm who needs access to sensitive information and review permissions at least every three months.
- **System owners:** Ensure application and service accounts have a documented purpose, an assigned owner, and only the permissions they need.

## 5. Exceptions

Any request to make an exception to this policy must be documented and approved by the designated manager and IT/Security team before the exception is applied. The request must explain why the exception is needed, what risks it creates, and how those risks will be reduced. Exceptions must have an expiry or review date. Users must contact their manager or IT/Security team if they cannot follow a rule; they must not bypass the rule on their own.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-03, T-08, T-24, and T-29** through server-side authorization, least privilege, access reviews, and service-account controls.