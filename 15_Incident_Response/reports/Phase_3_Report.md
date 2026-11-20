# Aegis Shield - Phase 3 Review and Report

**Name:** JANANI M
**Track:** Cybersecurity
**Phase:** Phase 3 “ Finding, Detecting and Responding
**GitHub Repository:** [Aegis Shield](https://github.com/janani17-coder/aegis-shield)
**Git Tag:** Pending final validation

## 1. Phase Overview

Phase 3 covered Tasks 11“15. The objective was to identify security weaknesses, review and improve insecure code, design tamper-evident audit logging, detect suspicious activity in logs, and prepare incident response procedures.

The project used a local training environment, synthetic data, Python-based analysis and documented security procedures.

## 2. Five-Task Completion and Evidence Table

| Task | Status | Evidence |
|---|---|---|
| 11 - Prove Flaws | Completed with limitations | `11_Prove_Flaws/Task_11_Prove_Flaws_Report.md` and DOM XSS screenshot |
| 12 - Secure Code Review | Partially complete | `12_Secure_Code_Review/reports/Task_12_Secure_Code_Review_Report.md` and before/after scan results |
| 13 - Audit Logging | Completed | `13_Audit_Logging/evidence/tamper_demo_output.txt` |
| 14 - Attack Detection | Completed with limitations | `14_Attack_Detection/reports/detection_alerts.csv` and dashboard |
| 15 - Incident Response | Partially complete | Three playbooks, tabletop notes and improvement proposals |

### Task 11 - Prove Security Flaws

Reviewed SQL injection, DOM-based XSS and broken access-control patterns in the local OWASP Juice Shop training environment. Documented root causes, potential impacts, fixes and regression tests.

Limitations: SQL injection was identified through source review, JavaScript execution was not demonstrated, and cross-user basket access was not tested.

Evidence: `11_Prove_Flaws/evidence/dom-xss-html-rendering.png`.

### Task 12 - Secure Code Review

Reviewed the sample payroll application using Bandit, Semgrep, Gitleaks, OSV-Scanner and manual source-code review.

- Bandit: 8 findings before remediation, 0 after.
- Semgrep: 12 findings before remediation, 0 after.
- Gitleaks: no leaks detected in the final fixed-code scan.
- OSV-Scanner: the initial dependency review identified advisories. A scoped remediation review was subsequently completed under Task 18.

Three selected weak functions were rewritten as secure code examples.

**Task 18 dependency remediation evidence:**
- 8 scoped packages reviewed.
- 72 baseline vulnerability records across 37 advisory groups.
- 0 advisory matches in the after-scan for the scoped packages.
- `pip check` reported no broken requirements.

**Limitation:** The dependency results apply only to the eight reviewed packages. Full application security validation and production verification remain pending.
### Task 13 - Audit Logging

Designed a payroll audit logging specification covering event fields, sensitive data handling, retention, access controls and tamper evidence.

Implemented a SHA-256 hash-chain demonstration. The original chain passed verification, while a modified test copy failed verification due to a hash mismatch.

Evidence: `13_Audit_Logging/evidence/tamper_demo_output.txt`.

### Task 14 - Attack Detection

Implemented Python-based detection rules for authentication, payroll and web access logs.

- Authentication events: 11,487.
- Payroll audit events: 2,652.
- Web requests: 5,805.
- Total processed: 19,944.
- Alerts generated: 21.
- Planted scenarios with corresponding detection evidence: 13 of 13, as recorded in the Task 14 report.

Detection limitations include missing authoritative administrator-role data, MFA status, payroll approval references and timezone offsets. Alerts require investigation and do not independently prove successful exploitation.

### Task 15 — Incident Response

Prepared three incident response playbooks covering payroll data breach, ransomware and insider salary leak scenarios. Each includes detection references, response steps, notification roles, evidence preservation and decision points.

An AI-assisted tabletop simulation was documented, with five improvement proposals.

An individual document-based walkthrough of the Payroll Data Breach Playbook was also completed and documented. Five incident-response decision scenarios and the response lifecycle were reviewed.

**Outstanding:** A formal team tabletop exercise with a human participant, independent validation of proposed improvements and formal approval remain pending.

**Evidence:** 15_Incident_Response/evidence/tabletop/Payroll_Data_Breach_Individual_Walkthrough.md`.

This individual walkthrough does not constitute an independently facilitated team exercise or demonstrate production incident-response effectiveness.
## 3. Mini Challenge - Detection to Response in Five Lines

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

The remaining activities are:

1. Complete a formal human-led tabletop exercise with an independent participant.
2. Validate and obtain approval for at least three improvement actions.
3. Integrate the R-01, R-02 and R-03 remediation demonstrations with trusted application services.
4. Verify audit-log protection and retention controls.
5. Independently verify production rate limiting and MFA enforcement.
6. Run application-level security and regression tests.
7. Validate detection thresholds against normal production traffic.
8. Obtain system-owner approval.

The Task 18 isolated remediation demonstrations and scoped dependency checks are complete. Production deployment and effectiveness have not been verified.

After the outstanding requirements are completed and independently verified, the Phase 3 report will be finalized and the `phase-3` Git tag will be created and pushed.

## 7. Overall Phase Status

**IN PROGRESS - Technical demonstrations, remediation evidence and documentation prepared; production validation, independent human review and final approvals remain pending.**

### Completed
- Phase 3 technical documentation and evidence for Tasks 11-15.
- Task 18 isolated remediation demonstrations: 20 automated tests passed.
- Scoped dependency remediation: 8 packages reviewed, with zero OSV advisory matches.
- Individual Payroll Data Breach tabletop walkthrough.
- Security Hub documentation published on GitHub Pages.

### Pending
- Formal team tabletop exercise.
- Independent validation and approval of improvement actions.
- Production integration and security validation.
- Audit-log protection and retention verification.
- MFA and rate-limiting verification.
- System-owner approval.

**Git tag:** Pending final validation.

The project remains in progress until the outstanding requirements are completed and verified. No production deployment or production security effectiveness is claimed.
