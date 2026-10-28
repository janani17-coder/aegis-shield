# F-01 — Unauthenticated Access to Account Area

## Finding Details

- **Finding ID:** F-01
- **Title:** Login required to access account area
- **Application:** OWASP Juice Shop — local lab
- **Target:** `http://127.0.0.1:3000`
- **OWASP Category:** A01 — Broken Access Control
- **Severity:** Informational
- **Status:** Observation recorded; broader authorization testing not performed

## Summary

During a manual check in a private browser window, selecting the account area displayed a login screen. No unauthenticated account information was observed during this check.

## Scope and Preconditions

- Testing was restricted to the local Juice Shop lab.
- The browser was in a private session without an authenticated user.
- No access-control bypass attempts were performed.

## Steps to Reproduce

1. Open `http://127.0.0.1:3000` in a private browser window.
2. Select the account area.
3. Observe the page displayed by the application.

## Expected Result

Protected account information should require appropriate authentication and authorization.

## Actual Result

The application displayed the login screen. Other protected resources and authorization rules were not tested.

## Evidence

- Screenshot: `../evidence/A01_unauthenticated_login.png`

## Impact

No security vulnerability was confirmed by this limited check. Additional testing is required to assess authorization across protected resources.

## Recommendation

Continue testing protected resources with authorized lab accounts. Verify that the server enforces authorization for each sensitive resource and action.

## STRIDE Threat Mapping

- **Threat ID:** T-03
- **Rationale:** T-03 concerns unauthorized access to restricted employee records. This observation is relevant to access-control testing, but it does not demonstrate that T-03 is exploitable.

## Limitations

This check covered only the account-area login screen. It did not test direct resource access, role separation, or server-side authorization across the application.

## Final Assessment

**Informational observation.** The login screen appeared as expected. No Broken Access Control vulnerability was confirmed by this test.
