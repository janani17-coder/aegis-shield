# AS-05 Remediation and Policy Gaps

## Purpose

This note records follow-up actions identified during validation of the initial IAM access review. The original audit findings and validation comparison remain unchanged to preserve the assessment history.

## 1. Finding classification improvements

- **Privilege creep:** Track U-0267, U-0554, and U-0597 under a distinct `PRIVILEGE_CREEP` finding. Verify whether each account's ADMIN role is justified by its job function and approved access request.
- **Administrator MFA:** Assess MFA independently from role authorization. Confirm the MFA status of U-0099 and investigate any additional accounts flagged by the original audit using the source evidence.
- **Shared accounts:** Investigate U-9001 and U-9002 under the `SHARED_ACCOUNT` finding. Record the account owner, business purpose, and remediation required.
- **Role authorization:** Do not treat department mismatch alone as conclusive proof of unauthorized access. Verify role assignment against job responsibilities and documented approval.

## 2. Policy gaps to address

| Gap | Recommended action |
|---|---|
| Dormant accounts | Add a requirement to review accounts with 90 days of inactivity and disable or retain them based on documented approval. |
| Leaver access | Require account disablement on the employee's exit date, with completion logged and verified. |
| Administrator eligibility | Restrict ADMIN access to approved IT/security owners with a documented business need. |
| Shared accounts | Prohibit shared user accounts. Document and tightly control any approved technical service-account exception without allowing shared human identities. |
| MFA verification | Require MFA for administrator accounts and periodically verify enforcement. |

## 3. Remediation verification

For each finding, record the account ID, evidence reviewed, responsible owner, action taken, date completed, and verification result. Confirm that access changes are reflected in the identity system and audit logs.

## 4. Evidence and audit integrity

The initial audit is preserved in `AS-05_Initial_Access_Audit_Findings.csv` and `AS-05_Initial_Access_Audit_Report.md`. The validation comparison is preserved in `AS-05_Validation_Comparison_and_Missed_Items.md`. This document records proposed remediation; it does not claim that changes have already been implemented or verified.

## 5. Remaining limitation

The identified account IDs were compared with the supplied validation findings. Correct classification and remediation still require review of the source account attributes, role approvals, MFA status, and relevant audit evidence.
