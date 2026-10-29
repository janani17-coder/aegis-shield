# F-04 — Browser Storage Inspection

## Finding Details

- **Finding ID:** F-04
- **OWASP Top 10:2025 Category:** A04 — Cryptographic Failures
- **Title:** Browser Local Storage inspection
- **Severity:** Informational
- **Status:** Limited inspection completed; no vulnerability confirmed
- **Application:** OWASP Juice Shop — local lab
- **Target:** `http://127.0.0.1:3000`

## Summary

The browser's Developer Tools were used to inspect the Local Storage view for the local Juice Shop application. The selected Local Storage table displayed no keys or tokens at the time of inspection. This limited observation does not establish whether authentication data or sensitive information is stored elsewhere.

## Scope and Preconditions

- Testing was restricted to the local Juice Shop lab.
- Chrome Developer Tools was used.
- The selected Local Storage view for `http://127.0.0.1:3000` was inspected.
- No credentials or session tokens were shared.

## Steps to Reproduce

1. Open `http://127.0.0.1:3000` in Chrome.
2. Open Developer Tools.
3. Select the Application tab.
4. Open Local Storage in the left sidebar.
5. Select `http://127.0.0.1:3000`.
6. Observe the displayed storage entries.

## Expected Result

Browser storage should be assessed to determine whether sensitive information is stored or exposed inappropriately. The security of any stored data depends on its sensitivity, protections, and use.

## Actual Result

The selected Local Storage table displayed no keys or tokens at the time of inspection. Other browser storage mechanisms and application data flows were not comprehensively assessed.

## Evidence

- **Evidence source:** Manual inspection in browser Developer Tools.
- **Screenshot:** `../evidence/A04_browser_storage.png`
- **Observation:** The selected Local Storage table displayed no keys or tokens at the time of inspection.
- **Evidence limitation:** This observation applies only to the selected Local Storage view at that time. It does not establish that the application stores no authentication data elsewhere or that sensitive data is never exposed.

## Impact

No cryptographic or browser-storage vulnerability was confirmed. The limited observation is insufficient to determine whether sensitive information is stored securely across all browser storage mechanisms or application data flows.

## STRIDE Threat Mapping

- **Threat ID:** No direct mapping identified.
- **Mapping type:** No direct match for the observed test.
- **Rationale:** This test inspected the browser's Local Storage view. The payroll-specific STRIDE threat concerning restricted data sent to AI prompts or logs was not tested, and no direct payroll-specific threat was demonstrated.
- **Limitation:** This observation does not establish whether encryption is appropriate or correctly implemented for any data stored elsewhere.

## Recommendation

If further assessment is required, inspect relevant browser storage mechanisms and data flows within the authorized lab. Determine whether sensitive information is stored, whether access is appropriately restricted, and whether applicable encryption requirements are met. Record only the evidence needed for the assessment, without exposing credentials or tokens.

## Conclusion

The selected Local Storage table displayed no keys or tokens during this inspection. This is a limited observation, not proof that all browser storage and data handling are secure. No vulnerability was confirmed by the current evidence.
