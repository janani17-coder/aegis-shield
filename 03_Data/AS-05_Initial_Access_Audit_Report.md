# AS-05: Initial IAM & Access Review

**Review date:** 30 September 2026  
**Source:** `Aegis_Access_Review_Extract.xlsx` → `users_review` and `README` sheets  
**Status:** Initial audit only; validation vault not reviewed.

## Scope and method

Reviewed 747 account rows against the five rules in the README. Findings below are evidence-led and use account IDs, the relevant row fields, a risk rating, and a recommended action. The 90-day cutoff is **2 July 2026** (90 days before the review date). Dormant-account findings only count active accounts with a recorded last login before that cutoff. Admin department findings are provisional because the extract has department names but no explicit security-owner/approval field.

## Summary

| Problem type | Findings |
|---|---:|
| Leavers still active | 6 |
| Active accounts unused for over 90 days | 5 |
| Admin accounts without MFA | 5 |
| Shared accounts | 2 |
| Admin roles outside IT/security departments (provisional) | 6 |
| **Total finding records (categories can overlap)** | **24** |
| **Unique accounts with one or more findings** | **18** |

## Account-level findings

See `AS-05_Initial_Access_Audit_Findings.csv` for the complete structured list with `user_id`, finding type, broken rule, evidence, risk rating, and recommended action.

### Leaver account still active

- **U-0116 — Critical risk.** Evidence: employment_status=Resigned; exit_date=2026-06-03; is_active=Y. Account remains active after recorded exit date. Recommended action: Disable immediately; verify HR exit date and preserve access-removal logs. Investigate why deprovisioning missed the exit date.
- **U-0152 — Critical risk.** Evidence: employment_status=Resigned; exit_date=2026-07-29; is_active=Y. Account remains active after recorded exit date. Recommended action: Disable immediately; verify HR exit date and preserve access-removal logs. Investigate why deprovisioning missed the exit date.
- **U-0565 — Critical risk.** Evidence: employment_status=Resigned; exit_date=2026-04-08; is_active=Y. Account remains active after recorded exit date. Recommended action: Disable immediately; verify HR exit date and preserve access-removal logs. Investigate why deprovisioning missed the exit date.
- **U-0583 — Critical risk.** Evidence: employment_status=Resigned; exit_date=2026-07-31; is_active=Y. Account remains active after recorded exit date. Recommended action: Disable immediately; verify HR exit date and preserve access-removal logs. Investigate why deprovisioning missed the exit date.
- **U-0598 — Critical risk.** Evidence: employment_status=Resigned; exit_date=2026-04-06; is_active=Y. Account remains active after recorded exit date. Recommended action: Disable immediately; verify HR exit date and preserve access-removal logs. Investigate why deprovisioning missed the exit date.
- **U-0630 — Critical risk.** Evidence: employment_status=Resigned; exit_date=2026-06-19; is_active=Y. Account remains active after recorded exit date. Recommended action: Disable immediately; verify HR exit date and preserve access-removal logs. Investigate why deprovisioning missed the exit date.

### Active account unused for over 90 days

- **U-0332 — Medium risk.** Evidence: is_active=Y; last_login_at=2026-03-11; review_date=2026-09-30; last login is before 90-day cutoff 2026-07-02. Recommended action: Confirm account owner and business need; review assigned permissions with manager/data owner. Disable or reduce access if no longer required, following approved process.
- **U-0420 — Medium risk.** Evidence: is_active=Y; last_login_at=2026-03-03; review_date=2026-09-30; last login is before 90-day cutoff 2026-07-02. Recommended action: Confirm account owner and business need; review assigned permissions with manager/data owner. Disable or reduce access if no longer required, following approved process.
- **U-0428 — Medium risk.** Evidence: is_active=Y; last_login_at=2026-03-13; review_date=2026-09-30; last login is before 90-day cutoff 2026-07-02. Recommended action: Confirm account owner and business need; review assigned permissions with manager/data owner. Disable or reduce access if no longer required, following approved process.
- **U-0484 — Medium risk.** Evidence: is_active=Y; last_login_at=2026-03-05; review_date=2026-09-30; last login is before 90-day cutoff 2026-07-02. Recommended action: Confirm account owner and business need; review assigned permissions with manager/data owner. Disable or reduce access if no longer required, following approved process.
- **U-0615 — Medium risk.** Evidence: is_active=Y; last_login_at=2026-03-02; review_date=2026-09-30; last login is before 90-day cutoff 2026-07-02. Recommended action: Confirm account owner and business need; review assigned permissions with manager/data owner. Disable or reduce access if no longer required, following approved process.

### Administrator without MFA

- **U-0099 — High risk.** Evidence: role=ADMIN; mfa_enabled=N; is_active=Y. Recommended action: Require MFA before further privileged use; verify enforcement and review recent admin activity.
- **U-0267 — High risk.** Evidence: role=ADMIN; mfa_enabled=N; is_active=Y. Recommended action: Require MFA before further privileged use; verify enforcement and review recent admin activity.
- **U-0554 — High risk.** Evidence: role=ADMIN; mfa_enabled=N; is_active=Y. Recommended action: Require MFA before further privileged use; verify enforcement and review recent admin activity.
- **U-0597 — High risk.** Evidence: role=ADMIN; mfa_enabled=N; is_active=Y. Recommended action: Require MFA before further privileged use; verify enforcement and review recent admin activity.
- **U-9002 — High risk.** Evidence: role=ADMIN; mfa_enabled=N; is_active=Y. Recommended action: Require MFA before further privileged use; verify enforcement and review recent admin activity.

### Shared account

- **U-9001 — High risk.** Evidence: full_name=(shared account); username=payroll.shared@znova-demo.example; role=HR; is_active=Y. Account is explicitly labelled as a shared account. Recommended action: Replace with named individual accounts or a properly controlled non-human service identity if technically necessary; document owner/purpose, approvals, and audit logging. Remove shared credentials.
- **U-9002 — High risk.** Evidence: full_name=(shared account); username=admin.backup@znova-demo.example; role=ADMIN; is_active=Y. Account is explicitly labelled as a shared account. Recommended action: Replace with named individual accounts or a properly controlled non-human service identity if technically necessary; document owner/purpose, approvals, and audit logging. Remove shared credentials.

### Admin role outside IT/security department

- **U-0099 — High risk.** Evidence: role=ADMIN; department_name=Finance & Accounts; employment_status=Active. Department does not appear to be IT/security. Confirm ownership before concluding unauthorized. Recommended action: Verify documented IT/security ownership and approval. If not an authorized owner, remove ADMIN role and grant least-privilege access; log approval/change.
- **U-0107 — High risk.** Evidence: role=ADMIN; department_name=Human Resources; employment_status=Active. Department does not appear to be IT/security. Confirm ownership before concluding unauthorized. Recommended action: Verify documented IT/security ownership and approval. If not an authorized owner, remove ADMIN role and grant least-privilege access; log approval/change.
- **U-0267 — High risk.** Evidence: role=ADMIN; department_name=Customer Support; employment_status=Active. Department does not appear to be IT/security. Confirm ownership before concluding unauthorized. Recommended action: Verify documented IT/security ownership and approval. If not an authorized owner, remove ADMIN role and grant least-privilege access; log approval/change.
- **U-0554 — High risk.** Evidence: role=ADMIN; department_name=Customer Support; employment_status=Active. Department does not appear to be IT/security. Confirm ownership before concluding unauthorized. Recommended action: Verify documented IT/security ownership and approval. If not an authorized owner, remove ADMIN role and grant least-privilege access; log approval/change.
- **U-0597 — High risk.** Evidence: role=ADMIN; department_name=Customer Support; employment_status=Active. Department does not appear to be IT/security. Confirm ownership before concluding unauthorized. Recommended action: Verify documented IT/security ownership and approval. If not an authorized owner, remove ADMIN role and grant least-privilege access; log approval/change.
- **U-9002 — High risk.** Evidence: role=ADMIN; department_name=Executive; employment_status=nan. Department does not appear to be IT/security. Confirm ownership before concluding unauthorized. Recommended action: Verify documented IT/security ownership and approval. If not an authorized owner, remove ADMIN role and grant least-privilege access; log approval/change.

## Comparison with Day 3 policy (`docs/policies/01_access_control_least_privilege.md`)

- **Covered:** Admin MFA; individual accounts / no shared logins (although POL-01 allows a formally approved technical exception); least privilege and job-based access; admin/payroll permission reviews at least every three months; logging of access approvals and changes.
- **Gap — dormant accounts:** POL-01 does not specify the README’s 90-day inactivity review trigger.
- **Difference — leaver timing:** README says disable on the exit date, while POL-01 says remove/update access within one business day after HR confirms the departure. The policy should explicitly require disablement on the exit date and define how HR confirmation is made available in time.
- **Gap — admin eligibility:** POL-01 describes least privilege but does not explicitly limit the ADMIN role to IT/security owners. The source extract also lacks an explicit owner/approval field, so department-based mismatches need confirmation.
- **Shared-account conflict:** README says no shared accounts; POL-01 permits an exception if a technical need is formally approved. Align the wording, or clarify that approved technical identities are not shared human logins.

## Review questions / limitations

- **Should a leaver account be disabled the same day?** Yes, according to the assessment README. The control should be triggered by the confirmed exit date, with HR/IT coordination and an auditable record.
- **What if a manager needs the leaver’s files?** Preserve and transfer business files through an approved, logged process or delegated access; do not keep the former employee’s login active or share its credentials.
- **Evidence limitations:** The dataset shows current account state and some employment/login fields, but it does not include a full access-approval history or a definitive admin-owner list. Verify these with HR/IT before treating provisional role mismatches as confirmed violations.
- **Validation:** `unlock_AS-05` has not been opened. Compare against it only after saving/committing this initial report, then document missed planted findings and why.

## Suggested commit

```powershell
git add AS-05_Initial_Access_Audit_Report.md AS-05_Initial_Access_Audit_Findings.csv
git commit -m "Add initial AS-05 IAM access audit"
git push origin main
```

Save these two files in the repository root or move them into a dedicated `03_Data` folder before committing. This report is initial and should not be edited using the validation answers until the first commit is recorded.