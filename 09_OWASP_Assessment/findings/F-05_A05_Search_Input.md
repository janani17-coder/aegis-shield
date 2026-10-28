# F-05 — Basic Search Input Handling Check

## Finding Details

- **Finding ID:** F-05
- **Title:** Search handled basic test inputs without an obvious error
- **Application:** OWASP Juice Shop — local lab
- **Target:** `http://127.0.0.1:3000`
- **OWASP Category:** A05 — Injection
- **Severity:** Informational
- **Status:** Limited manual check completed; injection resistance not verified

## Summary

The search feature was tested with ordinary text (`test123`) and text containing a single quote (`test'123`). Both searches returned no results, and no obvious error was observed.

## Scope and Preconditions

- Testing was restricted to the local Juice Shop lab.
- The application's normal search interface was used.
- Only basic search inputs were tested.

## Steps to Reproduce

1. Open `http://127.0.0.1:3000`.
2. Open the search field.
3. Search for `test123`.
4. Search for `test'123`.
5. Observe the returned results and any visible error messages.

## Expected Result

The search feature should handle user input safely and should not expose database errors or allow unintended commands to execute.

## Actual Result

Both searches returned no results. No obvious error was observed. The application's internal query handling was not inspected.

## Evidence

- Evidence source: Manual browser observation.
- Screenshot: Not captured for this check.

## Impact

No injection vulnerability was confirmed. These simple inputs are insufficient to establish that the search feature is resistant to injection attacks.

## Recommendation

Perform authorized, controlled injection testing within the local lab. Review server-side input handling and parameterized query usage where applicable.

## STRIDE Threat Mapping

- **Threat ID:** T-09
- **Rationale:** T-09 concerns payroll inputs being changed before calculation. Injection could be relevant to unauthorized input manipulation, but this search test did not demonstrate a connection to payroll processing or confirm T-09.

## Limitations

Only two simple search inputs were tested. No deeper injection testing, request inspection, or database behavior analysis was performed.

## Final Assessment

**Informational observation.** The search feature returned normal no-results responses for the tested inputs. Injection resistance remains unverified.
