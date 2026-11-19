
# Risk Register

## Overview

The Aegis Shield risk register consolidates 17 identified security risks using a likelihood and impact scoring method.

**Scoring formula:** Likelihood × Impact

## Risk Rating Scale

| Score | Rating |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–14 | High |
| 15–25 | Critical |

## Top Five Risks

| Risk ID | Risk Description | Likelihood | Impact | Score | Rating |
|---|---|---:|---:|---:|---|
| R-01 | Full payroll export risk | 4 | 5 | 20 | Critical |
| R-02 | Insider salary disclosure | 4 | 5 | 20 | Critical |
| R-06 | Repeated failed login activity | 4 | 4 | 16 | Critical |
| R-14 | Unremediated dependency advisories | 4 | 4 | 16 | Critical |
| R-03 | Incomplete ownership checks | 3 | 5 | 15 | Critical |

## Risk Treatment Priorities

### R-01 – Full Payroll Export Risk
Recommended action: Review export authorisation, restrict access and strengthen approval controls.

### R-02 – Insider Salary Disclosure
Recommended action: Apply least privilege, monitor sensitive data access and strengthen audit reviews.

### R-06 – Repeated Failed Login Activity
Recommended action: Monitor authentication events and review account protection controls.

### R-14 – Dependency Advisories
Recommended action: Review affected dependencies, prioritise remediation and perform a fresh vulnerability scan.

### R-03 – Incomplete Ownership Checks
Recommended action: Enforce server-side ownership validation and review access-control logic.

## Risk Ownership

The complete workbook assigns proposed owners, treatments, due dates and status to all 17 risks.

See the project repository:

[Completed Risk Register](https://github.com/janani17-coder/aegis-shield/blob/main/06_Templates/risk_register_completed.xlsx)

## Limitations

- Scores are assessment estimates.
- Proposed owners and due dates require review and approval.
- Risk ratings may change when new evidence becomes available.
- This register is a learning exercise, not a formal organisational risk assessment.

## Task 18 - Remediation Sprint Update

**Overall status: Demonstration and scoped remediation evidence verified; production remediation remains pending.**

| Risk ID | Remediation evidence | Verification | Current status |
|---|---|---|---|
| R-01 | Payroll export authorization demonstration | 5/5 tests passed | Production integration pending |
| R-02 | Salary-record access demonstration | 5/5 tests passed | Production integration pending |
| R-03 | Employee-record ownership and delegated-access demonstration | 10/10 tests passed | Production integration pending |
| R-06 | Authentication detection review | 6 authentication-related alerts identified | Rate limiting and MFA not verified |
| R-14 | Eight-package dependency remediation | OSV results reduced from 72 vulnerability records to 0 in the scoped scan; pip check clean | Application-level validation pending |

### Evidence locations

- R-01: `18_Remediation_Sprint/evidence/after/R01_Payroll_Export_Remediation_Evidence.md`
- R-02: `18_Remediation_Sprint/evidence/after/R02_Salary_Access_Remediation_Evidence.md`
- R-03: `18_Remediation_Sprint/evidence/after/R03_Employee_Record_Access_Remediation_Evidence.md`
- R-06: `18_Remediation_Sprint/evidence/after/R06_Authentication_Detection_Evidence.md`
- R-14: `18_Remediation_Sprint/evidence/after/R14_Dependency_Remediation_Evidence.md`
- Regression checklist: `18_Remediation_Sprint/Regression_Test_Checklist.md`

### Remaining validation

1. Integrate authorization demonstrations with trusted production identity, role and approval services.
2. Verify MFA enforcement and rate limiting through approved configuration and testing.
3. Run application-level regression and security tests after dependency updates.
4. Validate audit logging, retention and access protection.
5. Obtain system-owner review and approval.

**Risk closure rule:** These five risks remain open until the relevant production controls are implemented, independently validated and formally accepted by the responsible risk owners. Passing isolated demonstration tests alone does not close a production risk.

