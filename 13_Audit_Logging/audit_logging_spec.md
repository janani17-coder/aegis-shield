# Task 13 – Payroll Audit Logging Specification

## 1. Purpose
Record payroll actions in a reliable, traceable and tamper-evident audit log. Logs must support investigations, accountability and compliance reviews.

## 2. Audit Event Schema

| Field | Description |
|---|---|
| event_id | Unique event identifier |
| timestamp | UTC date and time |
| actor | User or service account performing the action |
| action | Action performed |
| target_employee | Employee record affected |
| result | Success or failure |
| source_ip | Source IP address, where available |
| application | Application or service name |
| before | Previous value for a change |
| after | New value for a change |
| reason | Business reason for the action |
| approval_reference | Related approval or ticket |
| previous_hash | Hash of the previous event |
| event_hash | SHA-256 hash of the current event |

## 3. Events to Record
- VIEW_SALARY and VIEW_PAYSLIP: record who viewed which employee record and when.
- UPDATE_SALARY: record the authorized change, previous and new salary, reason and approval reference.
- UPDATE_BANK_DETAILS: record that details changed; retain only appropriately masked identifiers.
- APPROVE_PAYROLL_RUN: record approver, time and result.
- EXPORT_FULL_PAYROLL: record the user, export purpose, time and result.
- Record denied and failed sensitive actions as well as successful actions.

## 4. Never-Log List
Never record:
- Passwords or password hashes.
- Session cookies, access tokens, API keys or private keys.
- Full bank account or card numbers.
- Authentication secrets or recovery codes.
- Unnecessary personal information.

Salary values are sensitive payroll data. Store before/after values only in the restricted audit system with role-based access and encryption. Salary views should record the access event, not duplicate the salary amount.

## 5. Tamper-Evidence
Each event is serialized in a consistent format and hashed with SHA-256. Every event stores the previous event's hash. A verification process checks both the event hash and the previous-hash link.

The Python demonstration creates a chain and modifies a historical event in a separate test copy. Verification detects the modification.

A hash chain alone cannot prevent deletion or complete rewriting by an administrator. Therefore:
- Forward logs to a separate, centrally managed logging system.
- Use append-only or immutable storage with retention lock where supported.
- Restrict log administration to a separate role from payroll administration.
- Export signed or independently protected hash checkpoints regularly.
- Alert on missing events, disabled logging and failed verification.
- Review access to audit logs.

## 6. Retention and Access
Proposed retention: 8 years, subject to applicable legal, regulatory and organizational requirements. Review the period with the compliance or legal team before production adoption.

Encrypt logs at rest and in transit. Permit access only to authorized audit, security and compliance personnel. Record and review access to the audit logs themselves. Apply secure deletion after the approved retention period.

## 7. Conclusion
The audit design records who did what, when, where and the before/after values for authorized changes. SHA-256 hash chaining provides tamper evidence, while independent immutable storage and external checkpoints reduce the risk of administrator alteration or deletion.