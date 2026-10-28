# Security Finding Template

## 1. Finding Details

- **Finding ID:** F-XX
- **Title:** [Short, clear finding title]
- **Assessment:** Aegis Shield — Task 9
- **Application:** OWASP Juice Shop
- **Target:** `http://127.0.0.1:3000`
- **Date tested:** [YYYY-MM-DD]
- **OWASP Top 10:2025 category:** [A01–A10]
- **Severity:** [Informational / Low / Medium / High / Critical / Not rated]
- **Status:** [Found / Not found / Not tested]

## 2. Summary

[Describe what was tested and what the evidence actually showed. Do not claim a vulnerability without supporting evidence.]

## 3. Scope and Preconditions

- **Feature or page tested:** [Name the page or feature]
- **Account or role:** [Authorized test account/role, or not applicable]
- **Preconditions:** [What must be true before the test]
- **Scope confirmation:** Local lab only

## 4. Steps to Reproduce

1. [First action]
2. [Second action]
3. [Continue with the exact steps performed]

Use only steps that were actually performed. A test that was planned but not executed must be marked Not tested.

## 5. Expected Result

[Describe the safe behavior expected from the application.]

## 6. Actual Result

[Record the observed behavior, including relevant response details. If the test was not completed, explain why.]

## 7. Evidence

- **Evidence filename(s):** [List files saved under `09_OWASP_Assessment/evidence/`]
- **Evidence description:** [Explain what each screenshot or captured request demonstrates]
- **Evidence limitations:** [State anything the evidence does not prove]

## 8. Impact

[Explain the plausible security or business impact if the observed weakness is confirmed. Avoid overstating impact.]

## 9. Recommended Remediation

[Suggest a practical security improvement. For a Not found or Not tested result, state any follow-up verification needed instead of presenting a hypothetical weakness as confirmed.]

## 10. STRIDE Threat Mapping

- **Threat ID:** [Exact ID from `docs/threat_model_template_completed.md`, or Pending]
- **Threat description:** [Use the matching description from the Task 2 threat model]
- **Mapping rationale:** [Explain how the observed behavior relates to the threat]
- **Mapping status:** [Confirmed mapping / Needs review / No direct match]

## 11. Limitations and Verification

[Record test coverage limits, unavailable features, missing logs, or additional validation needed.]

## 12. Final Assessment

- **Final status:** [Found / Not found / Not tested]
- **Evidence reviewed:** [Yes / No]
- **Threat mapping reviewed:** [Yes / No / Pending]
- **Reviewer notes:** [Additional observations]
