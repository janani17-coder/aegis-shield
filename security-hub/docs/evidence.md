
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
