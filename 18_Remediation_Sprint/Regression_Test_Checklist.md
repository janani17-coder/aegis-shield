# Task 18 - Remediation Regression Checklist

## Automated demonstration tests

| ID | Test | Expected result | Actual result |
|---|---|---|---|
| R-01-T1 | Authorized payroll export | Allow and audit | PASS |
| R-01-T2 | Missing export role | Reject | PASS |
| R-01-T3 | Missing approval | Reject | PASS |
| R-01-T4 | Self-approval | Reject | PASS |
| R-01-T5 | Unapproved report | Reject | PASS |
| R-02-T1 | Employee views own salary | Allow and audit | PASS |
| R-02-T2 | Unauthenticated request | Reject | PASS |
| R-02-T3 | Missing payroll role | Reject | PASS |
| R-02-T4 | Other employee salary | Reject | PASS |
| R-02-T5 | Missing employee ID | Reject | PASS |
| R-03-T1 | Own employee record | Allow | PASS |
| R-03-T2 | Approved delegated access | Allow | PASS |
| R-03-T3 | Unauthenticated request | Reject | PASS |
| R-03-T4 | Missing own-record role | Reject | PASS |
| R-03-T5 | Missing delegated role | Reject | PASS |
| R-03-T6 | Missing access grant | Reject | PASS |
| R-03-T7 | Unapproved grant | Reject | PASS |
| R-03-T8 | Incorrect requester | Reject | PASS |
| R-03-T9 | Incorrect target | Reject | PASS |
| R-03-T10 | Self-approval | Reject | PASS |

## Dependency regression
- [x] Updated eight-package dependency list installed in isolated environment
- [x] pip check reported no broken requirements
- [x] OSV scan reported zero advisory matches for the scoped list

## Detection regression
- [x] Existing detection report contains 21 alert records
- [x] Six authentication-related alerts identified
- [ ] Production rate limiting verified
- [ ] MFA enforcement independently verified

## Production validation still required
- [ ] Integrate R-01 authorization with a trusted approval system
- [ ] Integrate R-02 checks with trusted authentication and role services
- [ ] Integrate R-03 checks with trusted identity and access-grant services
- [ ] Verify audit-log protection and retention
- [ ] Run application-level security and regression tests
- [ ] Validate detection thresholds against normal production traffic
- [ ] Obtain system-owner approval

## Overall result
Demonstration regression tests: 20 passed.
Production deployment: Not verified.
