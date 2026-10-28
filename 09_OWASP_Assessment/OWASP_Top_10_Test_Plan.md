# Task 9 — OWASP Top 10:2025 Assessment Test Plan

## 1. Scope and Rules

- **Application:** OWASP Juice Shop
- **Target URL:** `http://127.0.0.1:3000`
- **Environment:** Local lab only
- **Testing method:** Manual browser testing and review of available application and configuration information
- **Evidence folder:** `09_OWASP_Assessment/evidence/`
- **Findings folder:** `09_OWASP_Assessment/findings/`
- **Related threat model:** `docs/threat_model_template_completed.md`

### Testing Rules

1. Test only the local Juice Shop application.
2. Use only accounts and data authorized for this lab.
3. Record actual observations rather than assuming a vulnerability exists.
4. Capture screenshots or other supporting evidence for completed tests.
5. Classify results as **Found**, **Not found**, or **Not tested**. Use **Partially tested** in progress notes when only part of a category has been assessed.
6. A Not found result applies only to the specific test performed.
7. Do not claim a security control is absent unless sufficient evidence supports that conclusion.
8. Do not include real personal, financial, or confidential information in test inputs.

## 2. OWASP Top 10:2025 Categories

| ID | Category | Plain-English Explanation |
|---|---|---|
| A01:2025 | Broken Access Control | Users can access information or perform actions outside their permissions. |
| A02:2025 | Security Misconfiguration | Incorrect or unsafe settings make an application less secure. |
| A03:2025 | Software Supply Chain Failures | Vulnerable or compromised dependencies and software delivery processes can put an application at risk. |
| A04:2025 | Cryptographic Failures | Sensitive information is not adequately protected through appropriate cryptography. |
| A05:2025 | Injection | Untrusted input is interpreted as part of a query, command, or expression. |
| A06:2025 | Insecure Design | Security requirements and foreseeable misuse are not adequately addressed in the application's design. |
| A07:2025 | Authentication Failures | Login, identity verification, or session handling does not reliably establish or maintain the user's identity. |
| A08:2025 | Software or Data Integrity Failures | Software or data is trusted without adequate integrity verification. |
| A09:2025 | Security Logging and Alerting Failures | Security events are not adequately recorded, monitored, or brought to the attention of responsible personnel. |
| A10:2025 | Mishandling of Exceptional Conditions | Unexpected errors or unusual conditions are handled in ways that may create security weaknesses. |

## 3. Test Plan and Preliminary Results

The following table records the checks already performed. These are preliminary observations, not proof that any category is completely secure or vulnerable.

| ID | Planned Test | Expected Safe Result | Status | Evidence and Notes |
|---|---|---|---|---|
| A01:2025 | Review access to account, basket, or order information using an unauthenticated session and authorized lab accounts. | Users can access only information and actions permitted to them. | Partially tested | `evidence/A01_unauthenticated_login.png` shows the account area displaying the login page in a private window. Broader access-control enforcement was not verified. |
| A02:2025 | Review invalid URL handling, visible error messages, response headers, and exposed application information. | Unnecessary technical details, secrets, and unsafe configuration are not exposed. | Partially tested | `evidence/A02_invalid_url_response.png` records the invalid URL response. Security headers and other configuration settings were not checked. |
| A03:2025 | Review local container configuration and available component or dependency metadata. | Dependencies are traceable, maintained, and assessed for relevant supply-chain risks. | Partially tested | `05_Lab_and_Samples/docker-compose.lab.yml` specifies `bkimminich/juice-shop:latest`. The `latest` tag makes the selected version less explicit. The exact application version and dependency vulnerability status were not verified. |
| A04:2025 | Review browser-visible storage and information exposed during an authorized local session. | Sensitive information is appropriately protected and minimized. | Partially tested | Local Storage was inspected. The visible entries did not appear to contain sensitive information. This visual check does not establish encryption, secure transmission, or the absence of sensitive data elsewhere. No screenshot was captured for this check. |
| A05:2025 | Enter harmless ordinary text and a single quote into the application search field. | Input is handled safely without unauthorized behavior or sensitive error disclosure. | Partially tested | `test123` and `test'123` returned no results without an obvious error. These simple inputs do not establish injection resistance. No screenshot was captured for this check. |
| A06:2025 | Review a normal basket workflow and consider the relevant business rules and authorization requirements. | Security requirements are enforced throughout the workflow. | Partially tested | Adding a product to the basket succeeded normally. Business-rule enforcement and authorization boundaries were not tested. No screenshot was captured for this check. |
| A07:2025 | Test logout and review whether the account area returns to an unauthenticated state. | A logged-out session cannot continue using protected functionality. | Partially tested | Logout succeeded and the account area returned to the login screen. Server-side session invalidation and token expiry were not independently verified. No screenshot was captured for this check. |
| A08:2025 | Review a normal data-handling workflow and available information about integrity controls. | Data is validated and its integrity is verified where required. | Partially tested | A product remained in the basket after refresh. This is a normal workflow observation; it does not establish whether unauthorized modification is prevented. No screenshot was captured for this check. |
| A09:2025 | Make one benign failed login attempt and determine whether security logs or alerts can be reviewed. | Security events are recorded and appropriate monitoring or alerting can be verified. | Partially tested | One failed login displayed a generic failure message. Application logs, security-event recording, and alerting were not verified. No screenshot was captured for this check. |
| A10:2025 | Review handling of a moderately long, harmless search input and observe the response. | Unexpected inputs are handled safely without exposing sensitive information or bypassing controls. | Partially tested | `test123test123test123test123test123` returned a normal no-results message. Broader boundary-condition and exception handling were not tested. No screenshot was captured for this check. |

### Status Definitions

- **Found:** Evidence supports the presence of a security weakness.
- **Not found:** The specific test did not identify the suspected weakness. This does not establish that the category is secure.
- **Not tested:** The test was not performed, the feature was unavailable, or the evidence was insufficient.
- **Partially tested:** Some checks were performed, but the category has not been assessed sufficiently to reach a complete conclusion.

**Current assessment:** The recorded checks provide preliminary observations for all 10 categories. They do not confirm a security vulnerability. Several checks still need stronger evidence or additional testing.

## 4. Test Execution Record

For every test performed, record the following information:

- Test ID and OWASP category
- Date and time of the test
- Application page or feature tested
- Preconditions and steps performed
- Expected safe result
- Actual observed result
- Status and justification
- Evidence filename
- Limitations or reason the test could not be completed

### Evidence Requirements

- Save screenshots in `09_OWASP_Assessment/evidence/`.
- Use descriptive filenames, such as `A01_unauthenticated_login.png`.
- Capture the relevant application state without exposing real credentials or personal data.
- For request/response evidence, record only information obtained from the authorized local lab.
- If evidence was not captured, state that explicitly. Do not create or claim evidence that does not exist.

## 5. Findings

Eight finding reports have been prepared under `09_OWASP_Assessment/findings/`.

| Finding ID | Category | Report |
|---|---|---|
| F-01 | A01:2025 — Broken Access Control | `findings/F-01_A01_Access_Control.md` |
| F-02 | A02:2025 — Security Misconfiguration | `findings/F-02_A02_Error_Handling.md` |
| F-03 | A03:2025 — Software Supply Chain Failures | `findings/F-03_A03_Latest_Image_Tag.md` |
| F-04 | A04:2025 — Cryptographic Failures | `findings/F-04_A04_Browser_Storage.md` |
| F-05 | A05:2025 — Injection | `findings/F-05_A05_Search_Input.md` |
| F-06 | A06:2025 — Insecure Design | `findings/F-06_A06_Basket_Workflow.md` |
| F-07 | A07:2025 — Authentication Failures | `findings/F-07_A07_Logout_Check.md` |
| F-08 | A10:2025 — Mishandling of Exceptional Conditions | `findings/F-08_A10_Exception_Handling.md` |

These reports document preliminary observations and limitations. They must not be interpreted as eight confirmed vulnerabilities. Some reports still need stronger supporting evidence, and their STRIDE mappings must be reviewed for relevance.

### Finding Report Requirements

Each finding should contain:

1. Finding ID and title
2. OWASP Top 10:2025 category
3. Severity and status
4. Scope and affected feature
5. Summary and potential impact
6. Reproducible test steps
7. Expected and actual results
8. Evidence filenames
9. Recommended remediation
10. Related STRIDE threat ID from Task 2
11. Explanation of the threat mapping
12. Limitations and verification notes

If the evidence does not support a vulnerability, describe the observation as informational or as an area requiring further verification. Do not assign a vulnerability severity merely because a category was tested.

## 6. Mapping Findings to the Task 2 Threat Model

Use `docs/threat_model_template_completed.md` as the source of truth for STRIDE threat IDs.

For each finding:

1. Identify the underlying security property involved.
2. Select the threat whose description most closely matches that property.
3. Record the exact threat ID and explain the relationship.
4. State whether the mapping is direct or only a conceptual analogy.
5. If no threat matches clearly, document the gap rather than inventing a relationship.

The threat model describes the intended payroll application, while the tests in this task use OWASP Juice Shop. Therefore, mappings may be conceptual and must not imply that the same payroll threat was demonstrated in Juice Shop.

## 7. Payroll Application Reflection

**Initial assessment:** Broken Access Control (A01:2025) could be among the most dangerous categories for a payroll application because unauthorized access may expose employee salary, personal, and bank information or permit unauthorized payroll actions.

Software or Data Integrity Failures (A08:2025) could also have severe consequences if payroll values, employee payment details, or payment-related records were altered without appropriate validation and integrity controls.

Which category is most dangerous depends on the payroll system's architecture, permissions, data sensitivity, existing safeguards, and potential impact. Unauthorized disclosure can harm employee privacy and facilitate fraud, while unauthorized modification can result in incorrect salary calculations or payments.

For the Aegis Shield payroll threat model, Broken Access Control and Software or Data Integrity Failures should both receive serious attention. The available Juice Shop observations do not establish that either weakness exists in a real payroll system.

## 8. References

- OWASP Top 10:2025: https://top10.owasp.org/2025/
- OWASP Top 10 official repository: https://github.com/OWASP/Top10
- OWASP Web Security Testing Guide: https://github.com/OWASP/wstg
- OWASP Juice Shop: https://github.com/juice-shop/juice-shop

## 9. Assessment Limitations

This assessment is a manual review of a local training application. Results describe only the tests actually performed.

Some categories require source-code review, dependency analysis, server-side logs, application configuration, or additional authorized testing. Those controls cannot be verified solely from a normal browser response.

The use of a `latest` image tag is a reproducibility and version-management concern, not proof that a dependency is vulnerable. A normal response to an invalid URL or harmless search input is likewise not proof that security controls are effective.

Further testing should prioritize collecting missing evidence, verifying access-control boundaries with authorized lab accounts, reviewing available configuration and logging information, and checking that each finding's STRIDE mapping is justified.

**Assessment conclusion:** The test plan covers all 10 OWASP Top 10:2025 categories and documents eight preliminary finding reports. The assessment remains limited in depth; no confirmed vulnerability should be claimed without additional supporting evidence.
