# F-08 — Handling of a Moderately Long Search Input

## Finding Details

- **Finding ID:** F-08
- **Title:** Search handled a moderately long input normally
- **Application:** OWASP Juice Shop — local lab
- **Target:** `http://127.0.0.1:3000`
- **OWASP Category:** A10 — Mishandling of Exceptional Conditions
- **Severity:** Informational
- **Status:** Limited input-handling check completed

## Summary

A moderately long, harmless search string was submitted through the normal search interface. The application displayed a standard no-results message and did not visibly fail.

## Scope and Preconditions

- Testing was restricted to the local Juice Shop lab.
- The normal search interface was used.
- No scripts or unusually large inputs were submitted.

## Steps to Reproduce

1. Open `http://127.0.0.1:3000`.
2. Open the search field.
3. Enter `test123test123test123test123test123`.
4. Submit the search.
5. Observe the application response.

## Expected Result

The application should handle ordinary and invalid inputs safely, returning an appropriate response without exposing sensitive details or entering an unstable state.

## Actual Result

The application displayed: “No results found. Try adjusting your search to find what you're looking for.” No visible error or application failure was observed.

## Evidence

- Evidence source: Manual browser observation.
- Screenshot: Not captured for this check.

## Impact

No exceptional-condition handling vulnerability was confirmed by this test.

## Recommendation

Continue testing reasonable input boundaries and invalid application states in the local lab. Confirm that unexpected conditions are handled safely and do not expose sensitive information.

## STRIDE Threat Mapping

- **Threat ID:** T-11
- **Rationale:** T-11 concerns payroll calculations or results being altered. This search input check did not test payroll calculations, so the mapping is not direct. Record this limitation rather than treating the observation as evidence of T-11.

## Limitations

Only one moderately long search input was tested. Input length limits, server-side exception handling, and other exceptional conditions were not assessed.

## Final Assessment

**Informational observation.** The search handled the tested input normally. No A10 vulnerability was confirmed by this check.
