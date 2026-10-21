# Task 3: Top 10 Threat-to-Policy Mapping

**Project:** Aura Workforce  
**Task:** AS-03 — Security Requirements and Policy Pack  
**Status:** Draft

## Purpose

This mapping connects the ten highest-priority threats from the STRIDE threat model to specific policy rules. It helps reviewers verify that each major threat has a corresponding security requirement.

| Threat ID | Threat summary | Policy reference | How the policy helps |
|---|---|---|---|
| T-03 | Unauthorized access to another employee's records | POL-01 Rule 2; POL-08 Rule 4 | Requires server-side authorization for every record request. |
| T-09 | Payroll input tampering | POL-08 Rules 5–6; POL-05 Rule 3 | Requires input validation, transaction controls, and audit records. |
| T-11 | Payroll calculation or output tampering | POL-08 Rule 6; POL-05 Rule 3 | Requires integrity checks and records of sensitive changes. |
| T-19 | Restricted data exposed to AI tools or logs | POL-03 Rule 6; POL-05 Rule 5; POL-09 Rule 5 | Restricts unapproved external sharing and prevents sensitive information in logs. |
| T-12 | Payroll report or export disclosure | POL-03 Rules 3–5; POL-04 Rule 8 | Restricts access and requires approved, protected transfer methods. |
| T-15 | Ledger entries altered, duplicated, or omitted | POL-08 Rule 6; POL-05 Rule 3; POL-07 Rule 9 | Requires integrity controls, audit records, and recovery validation. |
| T-24 | Dashboard access-control bypass | POL-01 Rule 2; POL-08 Rules 3–4 | Requires server-side permission checks instead of relying on interface restrictions. |
| T-28 | Sensitive backups or exports exposed | POL-07 Rules 3–5; POL-04 Rule 2; POL-03 Rule 8 | Requires encrypted backups, restricted access, and controlled storage. |
| T-08 | Excessive HR or payroll privileges | POL-01 Rules 3, 5–6; POL-02 Rule 1 | Requires least privilege, separation of duties, periodic reviews, and MFA for administrators. |
| T-29 | Overprivileged service account | POL-01 Rule 8; POL-04 Rules 3–5; POL-09 Rule 6 | Requires a documented owner, limited permissions, and protected credentials. |

## Review Checklist

- [ ] All ten top-priority threats are included.
- [ ] Every threat maps to at least one policy and a specific rule.
- [ ] Policy references match the actual policy files.
- [ ] The Security Team or reviewer has checked the mapping.

## References

- OWASP Cheat Sheet Series: https://github.com/OWASP/CheatSheetSeries
- OWASP Software Assurance Maturity Model (SAMM): https://github.com/OWASP/samm
- OWASP Application Security Verification Standard (ASVS): https://github.com/OWASP/ASVS
