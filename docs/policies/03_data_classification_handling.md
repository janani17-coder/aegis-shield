# Policy 3: Data Classification & Handling

**Policy ID:** POL-03  
**Owner:** Data Protection Owner  
**Status:** Draft

## 1. Purpose

To ensure that Aura Workforce information is classified, stored, shared, and disposed of according to its sensitivity.

## 2. Scope

This policy applies to all employee, HR, payroll, financial, operational, and system data handled by Aura Workforce employees, applications, contractors, and approved third parties.

## 3. Rules

1. All in-scope information must be assigned one of four classifications: Public, Internal, Confidential, or Restricted.
2. Data owners must approve the classification of new datasets and review classifications when the data's sensitivity or purpose changes.
3. Confidential and Restricted data must be accessible only to authorized users with a documented business need.
4. Payroll records, authentication secrets, and highly sensitive employee information must not be placed in public repositories or publicly accessible storage.
5. Before exporting or sharing Confidential or Restricted data, users must verify the recipient, business purpose, and approved transfer method.
6. Restricted data must not be entered into public AI tools or unapproved external services.
7. Applications must return only the data fields required for the user's authorized task.
8. Temporary exports and downloaded sensitive files must be stored in approved locations and deleted when no longer required, according to the organization's retention rules.
9. Data owners must review access to Confidential and Restricted datasets at least every three months.
10. Suspected data exposure or unauthorized sharing must be reported promptly through the incident response process.

## 4. Roles

- **Data owners:** Assign classifications and approve access and sharing.
- **Security Team:** Defines handling requirements and investigates suspected exposure.
- **IT administrators:** Configure access restrictions and approved storage.
- **Users:** Handle information according to its classification and report mistakes.

## 5. Exceptions

Exceptions require written approval from the data owner and Security Team, a documented business reason, compensating controls, and an expiry date. Legal or regulatory requirements cannot be waived through this process.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-12, T-19, T-24, and T-28** by controlling exports, external AI sharing, unnecessary data access, and sensitive copies.