# F-07 — Logout and Account Access Check

## Finding Details

- **Finding ID:** F-07
- **OWASP Top 10:2025 Category:** A07 — Authentication Failures
- **Title:** Logout and Account Access Check
- **Severity:** Informational
- **Status:** Preliminary check completed; no vulnerability confirmed
- **Target:** Local OWASP Juice Shop lab

## Objective

Observe whether the application returns to the login screen after logout and identify any limitations in verifying session invalidation.

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

Logout succeeded. The account area displayed the login screen afterward. Server-side session invalidation was not independently verified.

## Evidence

- **Evidence source:** Manual browser observation.
- **Screenshot:** Not captured for this check.
- **Evidence limitation:** The visible logout workflow was observed, but reuse of a previous session and token expiration were not tested.

## Impact

No authentication vulnerability was confirmed. If an application failed to invalidate sessions properly, a previously issued session could potentially remain usable after logout. This possibility was not demonstrated during this check.

## STRIDE Threat Mapping

- **Threat ID:** T-03
- **Mapping type:** Conceptual relationship; not a confirmed threat.
- **Rationale:** T-03 concerns unauthorized access to restricted employee records. Reliable session handling helps protect restricted resources, but this test only observed the visible logout workflow. It did not test whether a previously issued session could still access protected resources.
- **Limitation:** T-03 was not demonstrated by this observation, and no direct payroll-specific threat was confirmed.

## Recommendation

For a more complete assessment, verify session invalidation using an authorized test account and controlled lab testing. Check whether protected resources remain accessible after logout, and document the results without exposing session tokens or credentials.

## Conclusion

The visible logout workflow behaved as expected. Further testing would be required to assess server-side session invalidation. No vulnerability is confirmed by the current evidence.
