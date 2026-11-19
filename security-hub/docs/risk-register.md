
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
