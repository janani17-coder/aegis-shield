# F-04 — Preliminary Browser Storage Inspection

## Finding Details

- **Finding ID:** F-04
- **Title:** Browser Local Storage reviewed for visible sensitive information
- **Application:** OWASP Juice Shop — local lab
- **Target:** `http://127.0.0.1:3000`
- **OWASP Category:** A04 — Cryptographic Failures
- **Severity:** Informational
- **Status:** Limited inspection completed; encryption not verified

## Summary

The browser's Local Storage was inspected using Developer Tools. Entries were present, but they did not appear to contain sensitive information during this visual check.

## Scope and Preconditions

- Testing was restricted to the local Juice Shop lab.
- Browser Developer Tools were used to inspect Local Storage.
- Secret values and authentication tokens were not copied or shared.

## Steps to Reproduce

1. Open `http://127.0.0.1:3000`.
2. Open Developer Tools using F12.
3. Select **Application → Local Storage**.
4. Select the local Juice Shop origin.
5. Inspect the listed keys and values without sharing secrets.

## Expected Result

Sensitive information should not be unnecessarily exposed to browser storage. Sensitive data should be protected in transit and at rest as appropriate to its purpose and threat model.

## Actual Result

Storage entries were present, but none appeared sensitive during the visual inspection. Encryption, network traffic, and other storage locations were not assessed.

## Evidence

- Evidence source: Manual inspection in browser Developer Tools.
- Screenshot: Not captured for this check.

## Impact

No cryptographic vulnerability was confirmed. The limited inspection cannot establish whether sensitive data is handled securely in other parts of the application.

## Recommendation

Review the application's data flows and storage requirements. Verify transport encryption, server-side storage protection, and whether authentication material is handled appropriately.

## STRIDE Threat Mapping

- **Threat ID:** No direct mapping identified.
- **Mapping type:** No direct match.
- **Rationale:** T-19 concerns restricted data being sent to an AI service or exposed in logs. This Local Storage inspection did not test that data flow. The observation also did not demonstrate a cryptographic weakness, so assigning a specific payroll threat would not be justified.
- **Limitation:** This report records only a limited visual inspection; it does not establish that the application's cryptographic controls are secure or insecure.

## Limitations

Only visible browser Local Storage entries were inspected. IndexedDB, session storage, cookies, network traffic, server-side storage, and encryption controls were not tested.

## Final Assessment

**Informational observation.** No sensitive information was apparent in the inspected Local Storage entries. No Cryptographic Failures vulnerability was confirmed.
