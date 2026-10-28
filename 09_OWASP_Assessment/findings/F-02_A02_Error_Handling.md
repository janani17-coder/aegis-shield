# F-02 — Invalid URL Returned a Normal Page

## Finding Details

- **Finding ID:** F-02
- **Title:** Normal response to an invalid URL
- **Application:** OWASP Juice Shop — local lab
- **Target:** `http://127.0.0.1:3000/this-page-does-not-exist-123`
- **OWASP Category:** A02 — Security Misconfiguration
- **Severity:** Informational
- **Status:** Observation recorded; broader configuration review not performed

## Summary

A manual request to a nonexistent local application URL displayed a normal page. No detailed technical error was observed during this check. This result alone does not establish whether error handling or security configuration is correct.

## Scope and Preconditions

- Testing was restricted to the local Juice Shop lab.
- A browser was used to visit a deliberately nonexistent path.
- No application configuration was changed.

## Steps to Reproduce

1. Open `http://127.0.0.1:3000`.
2. Navigate to `/this-page-does-not-exist-123`.
3. Observe the response displayed by the application.

## Expected Result

Invalid URLs should be handled safely without exposing unnecessary internal implementation details, secrets, or stack traces.

## Actual Result

A normal page was displayed. The HTTP status code, response headers, and server-side error details were not inspected.

## Evidence

- Screenshot: `../evidence/A02_invalid_url_response.png`

## Impact

No security misconfiguration was confirmed by this check. Additional configuration and error-handling tests are needed before drawing a broader conclusion.

## Recommendation

Review security headers, production error handling, exposed application information, and deployment settings as separate checks. Inspect the HTTP status code and response headers during follow-up testing.

## STRIDE Threat Mapping

- **Threat ID:** No direct mapping identified.
- **Mapping type:** No direct match.
- **Rationale:** The payroll-focused STRIDE model does not contain a specific threat directly demonstrated by this invalid-URL observation. T-30 covers dependency failures and diagnostic-log exposure, but neither was tested here. Assigning T-30 would imply a connection that the current evidence does not establish.
- **Limitation:** This observation does not confirm a vulnerability or demonstrate that the application's error handling is insecure.
