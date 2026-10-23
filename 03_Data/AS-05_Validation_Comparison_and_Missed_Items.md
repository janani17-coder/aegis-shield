# AS-05 Validation Comparison and Missed-Items Note

**Initial audit commit:** `bbaeeb9` — `Add initial AS-05 IAM access audit`  
**Validation source:** `unlock_AS-05_access_review_planted.csv`  
**Purpose:** Compare the committed initial audit with the planted validation findings. The original initial report and CSV remain unchanged.

## Validation comparison

| Validation finding | Planted accounts | Initial audit coverage | Result |
|---|---|---|---|
| `LEAVER_STILL_ACTIVE` | U-0116, U-0152, U-0565, U-0583, U-0598, U-0630 | All six listed as leaver accounts still active | No planted account missed |
| `DORMANT_ACTIVE` | U-0332, U-0420, U-0428, U-0484, U-0615 | All five listed as active accounts unused over 90 days | No planted account missed |
| `ADMIN_NO_MFA` | U-0099 | Listed as an administrator without MFA | No planted account missed |
| `PRIVILEGE_CREEP` | U-0267, U-0554, U-0597 | All three were identified as admin-role/department mismatches, and also appeared in the initial admin-without-MFA category | Accounts were identified, but the specific privilege-creep finding was not clearly classified |
| `SHARED_ACCOUNT` | U-9001, U-9002 | Both listed as shared accounts | No planted account missed |

## Missed-items and classification analysis

The initial audit identified all 17 planted account IDs in the validation file. Therefore, **no planted account ID was completely missed** in the initial report.

However, there was a meaningful classification weakness:

1. **Privilege creep was not a distinct finding type.** The three accounts U-0267, U-0554, and U-0597 were captured under the broad “Admin role outside IT/security department” category. The validation source describes them more specifically as non-admin jobs holding the `ADMIN` role without MFA. This is a least-privilege / role-to-job mismatch, not just a department mismatch.
2. **Admin-without-MFA needs contextual review.** The validation source distinguishes U-0099 as a genuine admin with MFA switched off, while U-0267, U-0554, and U-0597 are privilege-creep cases. The initial report flagged multiple `ADMIN` accounts with MFA off, but its category labels did not sufficiently distinguish genuine authorized admins from users who should not have had the admin role in the first place. U-9002 also appeared in the initial admin-without-MFA list because of its account fields, but the validation source labels it as a generic shared account with no owner; confirm its role and account type before treating it as an authorized administrator.
3. **Risk-based next step:** For U-0267, U-0554, and U-0597, verify job responsibilities and approval evidence, remove unauthorized `ADMIN` access, grant least privilege, and require MFA for any legitimately retained administrator access. For U-0099, enable and verify MFA. For U-9001 and U-9002, replace shared human logins with individually attributable accounts or an approved, controlled non-human identity, with a documented owner and purpose.

## Why the classification weakness occurred

The initial audit applied broad checks to the role, department, and MFA columns. A department mismatch is a useful signal, but it is not by itself proof that the role is unauthorized; conversely, a user can have an inappropriate `ADMIN` role even when a department-based check is inconclusive. A stronger audit cross-checks role against job function/owner approval and then evaluates MFA separately.

## Policy comparison follow-up

- Add a specific 90-day inactivity review requirement to POL-01.
- Align leaver timing with the README rule requiring disablement on the exit date.
- State explicitly that the `ADMIN` role is restricted to approved IT/security owners and must be checked against job function and approval evidence.
- Resolve the difference between the README's absolute “no shared accounts” rule and POL-01's documented technical-exception wording.
- Keep the existing MFA, least-privilege, quarterly access review, service-account ownership, and access-change logging controls.

## Reviewer reflection

A leaver account should be disabled on the confirmed exit date under the assessment rule. If a manager needs the former employee's files, transfer or delegate access through an approved and logged process; do not keep the former employee's login active or share its credentials.

**Recordkeeping:** This note is a follow-up after validation. It should be added as a separate file and committed separately so the original initial audit commit remains a clear record of the pre-validation assessment.
