# Aegis Shield â€“ Phase 3 Review and Report

**Name:** JANANI M
**Track:** Cybersecurity
**Phase:** Phase 3 â€“ Finding, Detecting and Responding
**GitHub Repository:** [Aegis Shield](https://github.com/janani17-coder/aegis-shield)
**Git Tag:** Pending final validation

## 1. Phase Overview

Phase 3 covered Tasks 11â€“15. The objective was to identify security weaknesses, review and improve insecure code, design tamper-evident audit logging, detect suspicious activity in logs, and prepare incident response procedures.

The project used a local training environment, synthetic data, Python-based analysis and documented security procedures.

## 2. Five-Task Completion and Evidence Table

| Task | Status | Evidence |
|---|---|---|
| 11 â€“ Prove Flaws | Completed with limitations | `11_Prove_Flaws/Task_11_Prove_Flaws_Report.md` and DOM XSS screenshot |
| 12 â€“ Secure Code Review | Partially complete | `12_Secure_Code_Review/reports/Task_12_Secure_Code_Review_Report.md` and before/after scan results |
| 13 â€“ Audit Logging | Completed | `13_Audit_Logging/evidence/tamper_demo_output.txt` |
| 14 â€“ Attack Detection | Completed with limitations | `14_Attack_Detection/reports/detection_alerts.csv` and dashboard |
| 15 â€“ Incident Response | Partially complete | Three playbooks, tabletop notes and improvement proposals |

### Task 11 â€“ Prove Security Flaws

Reviewed SQL injection, DOM-based XSS and broken access-control patterns in the local OWASP Juice Shop training environment. Documented root causes, potential impacts, fixes and regression tests.

Limitations: SQL injection was identified through source review, JavaScript execution was not demonstrated, and cross-user basket access was not tested.

Evidence: `11_Prove_Flaws/evidence/dom-xss-html-rendering.png`.

### Task 12 â€“ Secure Code Review

Reviewed the sample payroll application using Bandit, Semgrep, Gitleaks, OSV-Scanner and manual source-code review.

- Bandit: 8 findings before, 0 after.
- Semgrep: 12 findings before, 0 after.
- Gitleaks: no leaks detected in the final fixed-code scan.
- OSV-Scanner: dependency advisories identified; dependencies still require upgrades and a fresh scan.

Three selected weak functions were rewritten as secure code examples.

### Task 13 â€“ Audit Logging

Designed a payroll audit logging specification covering event fields, sensitive data handling, retention, access controls and tamper evidence.

Implemented a SHA-256 hash-chain demonstration. The original chain passed verification, while a modified test copy failed verification due to a hash mismatch.

Evidence: `13_Audit_Logging/evidence/tamper_demo_output.txt`.

### Task 14 â€“ Attack Detection

Implemented Python-based detection rules for authentication, payroll and web access logs.

- Authentication events: 11,487.
- Payroll audit events: 2,652.
- Web requests: 5,805.
- Total processed: 19,944.
- Alerts generated: 21.
- Planted scenarios with corresponding detection evidence: 13 of 13, as recorded in the Task 14 report.

Detection limitations include missing authoritative administrator-role data, MFA status, payroll approval references and timezone offsets. Alerts require investigation and do not independently prove successful exploitation.

### Task 15 â€“ Incident Response

Prepared three playbooks covering payroll data breach, ransomware and insider salary leak scenarios. Each includes detection references, response steps, notification roles, evidence preservation and decision points.

An AI-assisted tabletop simulation was documented, with five improvement proposals.

**Outstanding:** A real spoken tabletop exercise with a human participant, validation of the proposed improvements and formal approval.

## 3. Mini Challenge â€“ Detection to Response in Five Lines

1. Task 14 identifies a full payroll export and generates a PAY-02 high-severity alert.
2. The SOC Analyst reviews the alert and preserves the relevant payroll audit evidence.
3. The Payroll Data Breach Playbook guides the Incident Response Lead's investigation.
4. Authorized IT Security personnel apply approved containment measures while the Payroll System Owner verifies export authorization.
5. Prevention includes documented export approvals, least-privilege access, protected audit logs and periodic access reviews.

**Evidence:** `14_Attack_Detection/reports/detection_alerts.csv` and `15_Incident_Response/playbooks/Payroll_Data_Breach_Playbook.md`.

A PAY-02 alert identifies an export event; it does not by itself establish that the export was unauthorized.

## 4. What I Learned

I learned how to identify security weaknesses and document their root causes and recommended fixes. I gained experience comparing static-analysis results before and after code improvements. I understood how audit-log integrity can be checked using hash chaining. I also learned how detection alerts connect to incident response playbooks and why evidence preservation and authorization checks are important.

## 5. Problems Encountered and Solutions

- Some expected templates were not present at the expected repository paths, so I located and organized the available template files.
- Scanner results required manual review because overlapping rules can report related findings.
- Some log sources lacked important fields, so I documented the limitations rather than making unsupported conclusions.
- Git reported trailing whitespace in Markdown files; I cleaned the files and rechecked the staged changes.
- The real spoken tabletop exercise and formal improvement validation remain outstanding.

## 6. Plan for the Next Phase

My next steps are to complete the human-led tabletop exercise, validate and approve at least three improvements, address outstanding dependency advisories, regenerate the final Task 14 dashboard, and review all Phase 3 evidence.

After completing and verifying the remaining requirements, I will create and push the `phase-3` Git tag and export this report with supporting evidence as one PDF.

## 7. Overall Phase Status

**IN PROGRESS â€“ Documentation and technical evidence prepared; some remediation, human validation and final submission activities remain pending.**

The repository contains the Phase 3 task documentation and evidence. The Git tag and final PDF submission will be completed only after the outstanding requirements are verified.
