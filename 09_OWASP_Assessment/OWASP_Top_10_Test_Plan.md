# Task 9 — OWASP Top 10:2025 Assessment Test Plan

## 1. Scope and Rules

- **Application:** OWASP Juice Shop
- **Target URL:** `http://127.0.0.1:3000`
- **Environment:** Local lab only
- **Testing method:** Manual browser testing and review of available request/response information
- **Evidence folder:** `09_OWASP_Assessment/evidence/`
- **Findings folder:** `09_OWASP_Assessment/findings/`

### Testing rules

1. Test only the local Juice Shop application.
2. Use only accounts and data authorized for this lab.
3. Record actual observations rather than assuming a vulnerability exists.
4. Save screenshots and notes for completed tests.
5. Mark each category Found, Not found, or partially tested.
6. A Not found result applies only to the specific test performed.
7. Do not claim that a security control is absent unless sufficient evidence supports that conclusion.

## 2. OWASP Top 10:2025 Categories

| ID | Category | Plain-English explanation |
|---|---|---|
| A01:2025 | Broken Access Control | Users can access information or perform actions outside their permissions. |
| A02:2025 | Partially tested — invalid URL returned a normal page | security headers and other configuration settings not yet checked. | Incorrect or unsafe settings make an application less secure. |
| A03:2025 | Partially tested — local image is tagged latest | exact application version and dependency vulnerability status not verified | Risks arise from compromised, vulnerable, or inadequately managed software dependencies and build or distribution processes. |
| A04:2025 | Partially tested — inspected Local Storage | entries did not appear sensitive, but encryption and other data flows were not verified. | Sensitive information is not adequately protected by cryptography. |
| A05:2025 | Partially tested — ordinary text and a single quote in search returned no results without an obvious error | deeper injection testing not performed | Untrusted input is interpreted as part of a query, command, or expression. |
| A06:2025 | Partially tested — normal add-to-basket workflow succeeded | authorization and business-rule enforcement were not tested | The application's design does not adequately address security requirements and foreseeable misuse. |
| A07:2025 | Partially tested — logout succeeded and the account area returned to the login screen | session invalidation and token expiry were not independently verified | Login, identity verification, or session handling does not reliably establish the user's identity. |
| A08:2025 | Partially tested — basket contents remained consistent after refresh | request integrity and protection against unauthorized data modification were not tested | Software or data is trusted without adequate integrity verification. |
| A09:2025 | Partially tested — one failed login displayed a generic message | security event logging and alerting were not verified | Security events are not adequately logged, monitored, or brought to the attention of responsible personnel. |
| A10:2025 | Partially tested — a moderately long search string returned a normal no-results message | broader exception and boundary-condition handling was not tested | Unexpected errors or unusual conditions are handled in ways that may create security weaknesses. |

## 3. Test Plan

All statuses start as Not tested. Update them only after performing the relevant test and recording the evidence.

| ID | Planned test | Expected safe result | Status | Evidence and notes |
|---|---|---|---|---|
| A01:2025 | Review access to account, basket, or order information using authorized lab accounts and normal application navigation. | Each user can access only information and actions permitted to that user. | Not tested | Pending |
| A02:2025 | Review visible error messages, available response headers, and exposed application information. | Unnecessary technical details, secrets, and unsafe configuration are not exposed. | Not tested | Pending |
| A03:2025 | Review available local project or dependency metadata for component names and versions. | Dependencies are traceable, maintained, and assessed for relevant supply-chain risks. | Not tested | Pending |
| A04:2025 | Review whether sensitive information is unnecessarily exposed in browser-visible responses or storage during an authorized local session. | Sensitive information is appropriately protected and minimized. | Not tested | Pending |
| A05:2025 | Use a harmless test input in an appropriate application field and observe how the application handles it. | Input is treated safely and does not produce unauthorized behavior. | Not tested | Pending |
| A06:2025 | Review one security-sensitive workflow against its intended business rules and authorization requirements. | Security requirements are enforced throughout the workflow. | Not tested | Pending |
| A07:2025 | Test authorized login and logout behavior and check whether protected pages remain accessible after logout. | Authentication is enforced and a logged-out session cannot continue using protected functionality. | Not tested | Pending |
| A08:2025 | Review an ordinary data-handling workflow and available documentation for integrity checks and trust boundaries. | Data is validated and its integrity is verified where required. | Not tested | Pending |
| A09:2025 | Make one benign failed login attempt and determine whether relevant security logs are available for review. | Security events are recorded and appropriate alerting can be verified. | Not tested | Pending |
| A10:2025 | Review normal and invalid application inputs for safe error handling and consistent behavior under unexpected conditions. | Errors are handled safely without exposing sensitive information or bypassing security controls. | Not tested | Pending |

## 4. Test Execution Record

For every test performed, record:

- Test ID and category
- Date and time
- Application page or feature tested
- Steps performed
- Expected safe result
- Actual observed result
- Status: Found, Not found, or Not tested
- Evidence filename
- Limitations or reason the test could not be completed

### Status definitions

- **Found:** Evidence supports the presence of a security weakness.
- **Not found:** The specific test did not identify the weakness.
- **Not tested:** The test was not completed, the feature was unavailable, or the evidence was insufficient.

Do not report a category as fully secure merely because one test did not identify a problem.

## 5. Findings

Prepare eight evidence-backed finding reports using a consistent finding template.

Each report should include:

- Finding ID and title
- OWASP Top 10:2025 category
- Severity and status
- Scope and affected feature
- Summary and potential impact
- Reproducible test steps
- Expected and actual results
- Evidence filenames
- Recommended remediation
- Related STRIDE threat ID from Task 2
- Explanation of the threat mapping
- Limitations and verification notes

Do not invent vulnerabilities or claim that an untested weakness exists. Each finding must be supported by actual evidence.

## 6. Mapping Findings to the Task 2 Threat Model

For every finding, review `docs/threat_model_template_completed.md` and select the STRIDE threat whose description most closely matches the observed issue.

Record the exact threat ID and explain the connection. If no threat matches clearly, document the gap rather than inventing a mapping.

## 7. Payroll Application Reflection

**Initial assessment:** Broken Access Control (A01:2025) could be among the most dangerous categories for a payroll application because unauthorized access may expose employee salary, personal, and bank information or permit unauthorized payroll actions.

Software or Data Integrity Failures (A08:2025) could also have severe consequences if payroll values or payment-related data are altered without appropriate verification.

The final answer should consider the application's design, actual controls, potential impact, and available evidence rather than assuming one category is always the most dangerous.

## 8. References

- OWASP Top 10:2025: https://top10.owasp.org/2025/
- OWASP Top 10 official repository: https://github.com/OWASP/Top10
- OWASP Web Security Testing Guide: https://github.com/OWASP/wstg
- OWASP Juice Shop: https://github.com/juice-shop/juice-shop

## 9. Assessment Limitations

This is a manual assessment of a local training application. Results describe only the tests actually performed. Some categories may require source-code review, dependency analysis, application logs, or other evidence unavailable through the browser.

Record these limitations honestly in the final report.
