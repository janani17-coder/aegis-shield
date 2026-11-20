
# Evidence Index

## Overview

This page lists the main evidence produced during the Aegis Shield cybersecurity assessment.

All evidence is from a fictional training environment. No real customer or production data is included.

## Task 12 – Secure Code Review

- Bandit findings: 8 before, 0 after.
- Semgrep findings: 12 before, 0 after.
- Gitleaks reported no leaks in the reviewed scan.
- OSV Scanner identified dependency advisories that remain pending remediation.

[View Task 12 Evidence](https://github.com/janani17-coder/aegis-shield/tree/main/12_Secure_Code_Review/evidence)

## Task 13 – Audit Logging

- Original hash-chain verification passed.
- Tampered-record verification detected a hash mismatch.

## Task 14 – Attack Detection

- Authentication, payroll and web request datasets were analysed.
- 21 alert rows were reported.
- Detection results have documented limitations.

[View Detection Evidence](https://github.com/janani17-coder/aegis-shield/tree/main/14_Attack_Detection)

## Task 15 – Incident Response

- Three incident response playbooks were prepared.
- An AI-assisted tabletop simulation was documented.
- Human-led validation remains pending.

[View Incident Response Evidence](https://github.com/janani17-coder/aegis-shield/tree/main/15_Incident_Response)

## Task 16 – Risk Register

- 17 risks documented.
- 14 controls mapped.
- Top five risks prioritised.

[View Risk Register and Evidence](https://github.com/janani17-coder/aegis-shield/tree/main/06_Templates)

## Evidence Limitations

Screenshots and scripts support the reported learning results. They do not establish production security, legal compliance or independent certification.


## Public Release Safety Checklist

- [x] Fictional training data is clearly identified.
- [x] No real customer records are intentionally included.
- [x] No passwords, API keys or private keys are included in the documentation.
- [x] Vulnerable lab configurations are excluded.
- [x] Generated website files are excluded from Git commits.

## Three Things Never to Publish

1. **Passwords, API keys and private keys:** They could allow unauthorised access.
2. **Real personal or customer information:** It could expose private information.
3. **Detailed exploit instructions and vulnerable system configurations:** They could help someone attack systems.

The public Security Hub is a learning portfolio, not a production security environment.


## Official References

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [OpenSSF Scorecard](https://scorecard.dev/)

These references provide guidance on documentation publishing and open-source security practices.

## Task 18 - Remediation Sprint

The remediation sprint contains isolated defensive demonstrations and supporting regression evidence.

- R-01: Payroll export authorization - 5/5 tests passed.
- R-02: Salary-record access - 5/5 tests passed.
- R-03: Employee-record ownership and delegated access - 10/10 tests passed.
- R-06: Six authentication-related detection alerts identified in the assessment dataset.
- R-14: Eight-package dependency review; scoped OSV results reduced from 72 vulnerability records to zero, with `pip check` reporting no broken requirements.
- Regression checklist: 20 demonstration tests passed.

### Remediation evidence

- [R-01 Payroll Export Evidence](https://github.com/janani17-coder/aegis-shield/blob/main/18_Remediation_Sprint/evidence/after/R01_Payroll_Export_Remediation_Evidence.md)
- [R-02 Salary Access Evidence](https://github.com/janani17-coder/aegis-shield/blob/main/18_Remediation_Sprint/evidence/after/R02_Salary_Access_Remediation_Evidence.md)
- [R-03 Employee Record Access Evidence](https://github.com/janani17-coder/aegis-shield/blob/main/18_Remediation_Sprint/evidence/after/R03_Employee_Record_Access_Remediation_Evidence.md)
- [R-06 Authentication Detection Evidence](https://github.com/janani17-coder/aegis-shield/blob/main/18_Remediation_Sprint/evidence/after/R06_Authentication_Detection_Evidence.md)
- [R-14 Dependency Remediation Evidence](https://github.com/janani17-coder/aegis-shield/blob/main/18_Remediation_Sprint/evidence/after/R14_Dependency_Remediation_Evidence.md)
- [Regression Test Checklist](https://github.com/janani17-coder/aegis-shield/blob/main/18_Remediation_Sprint/Regression_Test_Checklist.md)

### Task 18 limitations

These results apply only to isolated demonstrations and the scoped dependency scan. Production integration, MFA and rate-limiting verification, application-level regression, audit-log validation and system-owner approval remain pending. The associated risks are not marked closed.


## Individual Tabletop Walkthrough - Payroll Data Breach

- Exercise type: Individual document-based self-review.
- Playbook reviewed: AS-15 Payroll Data Breach.
- Five incident-response decision scenarios reviewed.
- Response lifecycle, evidence requirements and improvement actions documented.
- Status: Individual walkthrough completed; formal team tabletop exercise pending.

[View Individual Walkthrough Report](https://github.com/janani17-coder/aegis-shield/blob/main/15_Incident_Response/evidence/tabletop/Payroll_Data_Breach_Individual_Walkthrough.md)

This walkthrough was completed individually. It does not constitute an independently facilitated team exercise or demonstrate production incident-response effectiveness.
