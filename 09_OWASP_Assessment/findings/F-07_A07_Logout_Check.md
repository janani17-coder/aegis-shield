# F-07 — Logout and Account Access Check

## Finding Details

- **Finding ID:** F-07
- **Title:** Account area returned to login screen after logout
- **Application:** OWASP Juice Shop — local lab
- **Target:** `http://127.0.0.1:3000`
- **OWASP Category:** A07 — Authentication Failures
- **Severity:** Informational
- **Status:** Limited authentication workflow check completed

## Summary

The normal logout action completed successfully. After logout, opening the account area displayed the login screen rather than account information.

## Scope and Preconditions

- Testing was restricted to the local Juice Shop lab.
- The normal login/logout interface was used.
- No credentials or session tokens were shared.

## Steps to Reproduce

1. Open the local Juice Shop application.
2. Sign in using an authorized lab account.
3. Select the logout option.
4. Open the account area again.
5. Observe whether the application requests authentication.

## Expected Result

After logout, protected account information should not be available through the normal account interface without signing in again.

## Actual Result

Logout succeeded. The account area displayed the login screen afterward.

## Evidence

- Evidence source: Manual browser observation.
- Screenshot: Not captured for this check.

## Impact

No authentication vulnerability was confirmed. The observation supports the expected logout workflow but does not independently establish server-side session invalidation or token expiry behavior.

## Recommendation

Test session invalidation and token expiry separately using authorized lab accounts. Ensure protected server-side resources reject expired or invalid sessions.

## STRIDE Threat Mapping

- **Threat ID:** T-03
- **Rationale:** T-03 concerns unauthorized access to restricted employee records. Authentication and authorization controls help reduce this risk, but this logout observation does not demonstrate that T-03 is exploitable.

## Limitations

The check covered logout and the account-area screen only. Session replay, token expiry, and direct protected-resource access were not tested.

## Final Assessment

**Informational observation.** The logout workflow returned the account area to the login screen. No authentication vulnerability was confirmed.
