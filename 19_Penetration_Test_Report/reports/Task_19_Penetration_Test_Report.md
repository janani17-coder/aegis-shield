# Task 19 ? Penetration Test Report

**Project:** Aegis Shield  
**Assessment environment:** Local cybersecurity lab and supplied sample source code  
**Assessment period:** October?November 2026  
**Report status:** Documentation prepared ? independent human review reported completed; written review evidence unavailable; additional validation outstanding
**Assessment type:** Lab-based security assessment

---

## 1. Executive Summary

This assessment reviewed a local OWASP Juice Shop and DVWA lab, selected source code from a sample payroll application, security scanner results, and isolated remediation demonstrations.

The assessment identified 17 candidate observations across the reviewed material. These include source-code security concerns, observed HTML rendering behaviour, and configuration alerts from OWASP ZAP. They must not all be interpreted as confirmed exploitable vulnerabilities.

The most important areas requiring attention are unsafe handling of user input, SQL query construction, password storage, unsafe deserialization, and missing or unverified authorization controls.

Several remediation examples were prepared. Three secure-code examples were reviewed, and three isolated authorization demonstrations recorded 20 passing tests with no failures. A scoped dependency review also reported zero advisory matches across eight reviewed packages after remediation.

However, the supplied payroll application was not deployed or tested at runtime. The remediation examples and authorization demonstrations were not integrated into that original application. Production security improvements therefore remain unverified.

**Overall conclusion:** The assessment provides useful evidence of security weaknesses and remediation progress, but it does not establish that the original payroll application or any production environment is secure. Additional authorized testing, integration, and retesting are required. Independent human review was reported as completed, but no written review report or sign-off is available in this project.

## 2. Scope and Rules of Engagement

### 2.1 In scope

- Local OWASP Juice Shop lab.
- Local DVWA lab.
- Source-code review of the supplied sample payroll application.
- OWASP ZAP baseline scan results.
- Nmap results for the local lab.
- Bandit, Semgrep, Gitleaks and OSV-Scanner results.
- Review of secure-code remediation examples.
- Review of isolated authorization demonstrations and their test results.
- Review of defensive detection results from Task 14.

### 2.2 Out of scope

- Production systems and real company infrastructure.
- Real employee, customer, payroll or financial data.
- Systems belonging to other people or organizations.
- Deployment of the supplied payroll sample application.
- Production integration of the remediation examples.
- Full runtime validation of every candidate finding.

### 2.3 Rules of engagement

All testing discussed in this report was limited to the authorized local lab and supplied project materials. No external target was intentionally assessed. No real employee or customer data was accessed.

Source-code observations, scanner alerts, isolated demonstrations and observed application behaviour are identified separately. A scanner alert or source-code pattern is not automatically treated as proof of successful exploitation.

## 3. Assessment Method and Tools

The assessment used the following methods:

| Method | Tools or evidence | Purpose |
|---|---|---|
| Web application scanning | OWASP ZAP | Identify potential web configuration and application issues |
| Network discovery | Nmap 7.992 | Record exposed services in the local lab |
| Source-code review | Manual review | Identify unsafe coding patterns and missing visible controls |
| Static analysis | Bandit and Semgrep | Identify code security concerns |
| Secret scanning | Gitleaks | Search reviewed code for exposed secrets |
| Dependency review | OSV-Scanner | Check scoped dependencies against known advisories |
| Remediation review | Python examples and isolated tests | Review proposed security controls |
| Detection validation | Task 14 detection scripts and dashboard | Review detection of planted test scenarios |

### 3.1 Assessment approach

1. Identify the authorized lab targets and supplied source files.
2. Review scanner results and record potential observations.
3. Inspect relevant source code and existing evidence.
4. Separate observed behaviour from theoretical impact.
5. Review remediation examples and isolated test results.
6. Record limitations and outstanding validation requirements.
7. Prepare recommendations and retest status.

## 4. Risk Rating Method

CVSS v3.1 is intended to describe the technical severity of a vulnerability using a base score and vector. Business impact is considered separately because the same technical weakness can have different consequences in different environments.

The report uses these principles:

- A CVSS score and complete vector are assigned only when the available evidence supports the required metrics.
- Source-code patterns without demonstrated runtime impact remain candidates requiring validation.
- Scanner severity labels are not treated as CVSS scores.
- Missing security headers are not automatically assigned vulnerability scores.
- Synthetic example credentials are not treated as active credentials.
- Business impact is described separately from technical severity.
- Unverified findings remain unscored rather than receiving invented values.

**Current scoring status:** No CVSS v3.1 scores or vectors are asserted in this draft. The available evidence does not justify defensible scoring for the candidate observations as currently documented.

The assignment requirement for at least 12 scored findings remains outstanding. Additional authorized validation is needed before such scores can be responsibly assigned.

## 5. Findings Overview

The findings register contains 17 candidate observations. The following table summarizes their current evidence status.

| ID | Finding | Current evidence status | CVSS status |
|---|---|---|---|
| PT-01 | SQL query constructed using untrusted input ? Juice Shop | Source pattern identified; runtime validation pending | Not scored |
| PT-02 | Unsafe HTML rendering in search results ? Juice Shop | HTML interpretation observed; script execution not demonstrated | Not scored |
| PT-03 | Basket ownership check not visible ? Juice Shop | Potential issue; cross-user access not tested | Not scored |
| PT-04 | Hardcoded Flask session secret ? payroll sample | Code pattern confirmed; application not deployed | Not scored |
| PT-05 | Synthetic AWS-like credentials ? payroll sample | Example values; active status not verified | Not scored |
| PT-06 | MD5 password hashing ? payroll sample | Code pattern confirmed; runtime and database exposure unknown | Not scored |
| PT-07 | SQL query string interpolation ? payroll sample | Code pattern confirmed; runtime injection not tested | Not scored |
| PT-08 | Salary route lacks visible ownership check ? payroll sample | Isolated remediation passed; original application not retested | Not scored |
| PT-09 | User input concatenated into HTML template ? payroll sample | Code pattern confirmed; runtime behaviour not tested | Not scored |
| PT-10 | User-controlled filename appended to download path ? payroll sample | Code pattern confirmed; path controls not fully reviewed | Not scored |
| PT-11 | Unsafe pickle deserialization ? payroll sample | Code pattern confirmed; runtime behaviour not tested | Not scored |
| PT-12 | Flask debug mode enabled ? payroll sample | Configuration confirmed in sample; exposure unknown | Not scored |
| PT-13 | Listener bound to all network interfaces ? payroll sample | Configuration confirmed; network exposure unknown | Not scored |
| PT-14 | Wildcard CORS response header ? Juice Shop | Scanner evidence; sensitive-data exposure not established | Not scored |
| PT-15 | Content Security Policy header missing ? Juice Shop | Scanner observation; exploit not demonstrated | Not scored |
| PT-16 | COEP header missing or invalid ? Juice Shop | Scanner observation; impact not demonstrated | Not scored |
| PT-17 | COOP header missing or invalid ? Juice Shop | Scanner observation; impact not demonstrated | Not scored |

### 5.1 Detailed finding evidence and recommended actions

**PT-01 ? SQL query construction**

- Asset: Juice Shop login functionality; original source file was unavailable for direct review.
- Evidence: E-03.
- Observation: User-supplied login input is incorporated into SQL query construction.
- Validation limitation: Task 11 notes identify SQL string interpolation in routes/login.ts, but runtime SQL injection was not demonstrated. The original application source and version equivalence with the current Juice Shop 20.3.0 image are unavailable.
- Business impact: If the pattern is exploitable in the deployed application, database confidentiality and integrity could be affected.
- Recommendation: Use parameterized queries or safe ORM query methods.
- Retest: Runtime application validation remains pending.

**PT-02 ? Unsafe HTML rendering**

- Asset: Juice Shop search results.
- Evidence: E-04.
- Observation: A benign HTML-like search value was interpreted as HTML in the page.
- Validation limitation: JavaScript execution was not demonstrated.
- Business impact: Unsafe handling of untrusted content can create a client-side injection risk.
- Recommendation: Render untrusted values as text and avoid bypassing the framework's HTML sanitization.
- Retest: HTML interpretation was observed; security behaviour after a verified application-level fix remains pending.

**PT-03 ? Basket ownership check**

- Asset: Juice Shop basket retrieval function.
- Evidence: E-05.
- Observation: The reviewed function did not visibly establish basket ownership.
- Validation limitation: Task 11 notes record an own-basket baseline and a source-review concern in retrieveBasket(). Cross-user access was not tested; other middleware or route-level authorization controls were not ruled out. Original-version equivalence with the current Juice Shop 20.3.0 image is unverified.
- Business impact: If no other authorization control exists, another user's basket information could be exposed.
- Recommendation: Enforce server-side identity and ownership checks for every basket request.
- Retest: Pending.

**PT-04 ? Hardcoded Flask session secret**

- Asset: Supplied payroll sample, `app.py`.
- Evidence: E-06.
- Observation: A fixed session secret is assigned in source code.
- Business impact: A real exposed secret could undermine session integrity.
- Recommendation: Load a strong secret from protected configuration or a secrets manager.
- Retest: Secure example reviewed; original application integration not tested.

**PT-05 ? Synthetic AWS-like credentials**

- Asset: Supplied payroll sample, `app.py`.
- Evidence: E-06.
- Observation: Example AWS-like credential strings appear in source code.
- Validation limitation: Values are synthetic examples; active status was not verified.
- Business impact: No real credential exposure is established.
- Recommendation: Never commit real credentials; use managed secret storage and rotate credentials if they are genuine and exposed.
- Retest: Not applicable to the synthetic values.

**PT-06 ? MD5 password hashing**

- Asset: Supplied payroll sample, `app.py`.
- Evidence: E-06.
- Observation: Passwords are hashed using MD5.
- Business impact: Weak password hashing can increase the risk of password recovery if password hashes are exposed.
- Recommendation: Use a password hashing function designed for passwords, such as Argon2id, scrypt or an appropriately configured PBKDF2 implementation.
- Retest: Secure login example reviewed; original application and stored password migration were not tested.

**PT-07 ? SQL query interpolation**

- Asset: Supplied payroll sample, login function.
- Evidence: E-06.
- Observation: User input is inserted into an SQL query string.
- Validation limitation: Runtime injection was not tested.
- Business impact: If exploitable, database records and authentication logic could be affected.
- Recommendation: Use parameterized SQL queries.
- Retest: A separate secure login example was reviewed; original application runtime validation remains pending.

**PT-08 ? Salary route authorization**

- Asset: Supplied payroll sample, salary route.
- Evidence: E-06 and E-11.
- Observation: The reviewed route does not visibly show authentication or employee ownership enforcement.
- Validation limitation: Other middleware and application-level controls were not fully verified.
- Business impact: Inadequate authorization could expose salary information.
- Recommendation: Enforce authentication, role authorization and employee ownership on the server.
- Retest: Isolated R02 demonstration recorded 5 passing tests and 0 failures. The original application was not retested.

**PT-09 ? Unsafe template construction**

- Asset: Supplied payroll sample, search route.
- Evidence: E-06 and E-07.
- Observation: User input is concatenated into an HTML template string.
- Business impact: Unsafe rendering may introduce client-side injection risks.
- Recommendation: Use normal template rendering with automatic escaping and avoid building HTML from untrusted input.
- Retest: A separate secure search example was reviewed; runtime application validation remains pending.

**PT-10 ? Download path construction**

- Asset: Supplied payroll sample, download route.
- Evidence: E-06.
- Observation: A user-controlled filename is appended to a filesystem path.
- Validation limitation: Surrounding path validation and runtime behaviour were not fully reviewed.
- Business impact: Inadequate path controls could expose files outside the intended directory.
- Recommendation: Restrict downloads to an allowlist of known files and validate resolved paths against an approved directory.
- Retest: Pending.

**PT-11 ? Unsafe deserialization**

- Asset: Supplied payroll sample, import route.
- Evidence: E-06 and E-07.
- Observation: The route uses `pickle.loads` on request data.
- Business impact: Deserializing untrusted objects can create serious application security risks.
- Recommendation: Use a data-only format such as JSON, validate its structure and reject unexpected values.
- Retest: A separate JSON-based example was reviewed; original application runtime validation remains pending.

**PT-12 ? Flask debug mode**

- Asset: Supplied payroll sample.
- Evidence: E-06.
- Observation: The sample starts Flask with debug mode enabled.
- Validation limitation: Actual network exposure and deployment configuration are unknown.
- Business impact: Debug functionality in an exposed environment can disclose sensitive diagnostic information.
- Recommendation: Disable debug mode in deployed environments and use controlled logging.
- Retest: Pending.

**PT-13 ? Listener bound to all interfaces**

- Asset: Supplied payroll sample.
- Evidence: E-06.
- Observation: The sample binds to `0.0.0.0`.
- Validation limitation: Actual network reachability depends on deployment and network controls.
- Business impact: The service may be reachable through more network interfaces than intended.
- Recommendation: Bind only to required interfaces and enforce appropriate network restrictions.
- Retest: Pending.

**PT-14 ? Wildcard CORS response header**

- Asset: Juice Shop local lab.
- Evidence: E-01, E-16, E-17.
- Observation: ZAP reported wildcard CORS; the 21 November 2026 retest reconfirmed Access-Control-Allow-Origin: * on the homepage and product-search API.
- Validation limitation: Sensitive authenticated data exposure was not demonstrated; listed examples included public resources.
- Business impact: Depends on the data and endpoints exposed by the policy.
- Recommendation: Restrict cross-origin access to trusted origins where required.
- Retest: Pending.

**PT-15 ? Missing Content Security Policy**

- Asset: Juice Shop local lab.
- Evidence: E-01, E-16, E-17.
- Observation: ZAP reported missing CSP; the 21 November 2026 retest found no CSP header on the homepage and product-search API.
- Validation limitation: No exploit was demonstrated.
- Business impact: A suitable CSP can provide an additional browser-side security layer.
- Recommendation: Define and test a policy appropriate to the application's resources.
- Retest: Pending.

**PT-16 ? COEP header missing or invalid**

- Asset: Juice Shop local lab.
- Evidence: E-01, E-16, E-17.
- Observation: ZAP reported missing or invalid COEP; the 21 November 2026 retest found no COEP header on the homepage and product-search API.
- Validation limitation: No security impact was demonstrated.
- Business impact: Depends on the application's cross-origin isolation requirements.
- Recommendation: Review whether cross-origin isolation is required and configure the header accordingly.
- Retest: Pending.

**PT-17 ? COOP header missing or invalid**

- Asset: Juice Shop local lab.
- Evidence: E-01, E-16, E-17.
- Observation: ZAP reported missing or invalid COOP; the 21 November 2026 retest found no COOP header on the homepage and product-search API.
- Validation limitation: No security impact was demonstrated.
- Business impact: Depends on the application's window and cross-origin isolation requirements.
- Recommendation: Review application requirements and configure an appropriate policy.
- Retest: Pending.

## 6. Positive Security Observations

The assessment also recorded the following positive results:

1. The ZAP baseline covered 116 URLs and reported zero FAIL-NEW and zero FAIL-INPROG results. This does not mean the application is vulnerability-free.
2. Bandit findings reduced from 8 to 0 in the reviewed fixed-code scope.
3. Semgrep findings reduced from 12 to 0 in the reviewed fixed-code scope.
4. Gitleaks reported no findings in the reviewed fixed-code scope. This result does not establish that every possible secret was detected.
5. Three secure-code examples were prepared for login, search rendering and data import.
6. Three isolated authorization demonstrations recorded 20 passing tests and 0 failures.
7. The scoped dependency review reported 72 baseline vulnerability records across 37 advisory groups and zero advisory matches after remediation across eight reviewed packages.
8. Task 14 detection logic identified all 13 planted validation scenarios. This demonstrates detection of those test scenarios, not actual attacks.

## 7. Retest Results

| Area | Before | After / current result | Remaining limitation |
|---|---|---|---|
| SQL query construction | Unsafe interpolation identified | Parameterized query shown in separate secure example | Original app not retested |
| Search rendering | User input concatenated into HTML | Separate safe template example reviewed | Original app not retested |
| Deserialization | `pickle.loads` used | Separate JSON-based example reviewed | Original app not retested |
| Salary authorization | Ownership enforcement not visible in reviewed route | R02: 5 tests passed, 0 failed | Not integrated into original app |
| Employee record authorization | Authorization concerns identified | R03: 10 tests passed, 0 failed | Not integrated into production |
| Payroll export authorization | Approval controls required | R01: 5 tests passed, 0 failed | Not integrated into production |
| Scoped dependencies | 72 records across 37 advisory groups | 0 advisory matches across 8 scoped packages | Full dependency coverage pending |
| Juice Shop PT-01 to PT-03 | Original Task 11 source and baseline observations | PT-02 harmless HTML interpretation reproduced in current v20.3.0; PT-01 and PT-03 not runtime-validated | Original-version equivalence unverified; SQL injection and cross-user access not demonstrated |

**Retest conclusion:** The isolated demonstrations and code examples show remediation progress. They do not prove that the original sample application or a production application has been fixed.

## 8. Recommendations and Next Actions

1. Integrate the reviewed secure-code changes into the actual application through an approved development process.
2. Validate authentication, authorization and ownership checks at the application level.
3. Replace weak password hashing and plan a secure migration for existing password records.
4. Remove hardcoded secrets and verify whether any real credentials were ever exposed.
5. Replace unsafe deserialization and review file download path controls.
6. Review browser security headers against actual application requirements.
7. Complete full dependency inventory and scanning.
8. Conduct authorized application-level retesting after integration.
9. Document the reported independent human review and obtain written reviewer sign-off.
10. Use Task 20 to communicate secure input handling, password protection, least privilege, approval controls, secret handling and incident reporting.

## 9. Nontechnical Reader Review

**Purpose:** Confirm that the executive summary is understandable to a reader without a cybersecurity background.

| Review question | Status |
|---|---|
| Is the purpose of the assessment clear? | Pending review |
| Are the main risks explained without unnecessary jargon? | Pending review |
| Is it clear what has and has not been fixed? | Pending review |
| Are the remaining actions understandable? | Pending review |
| Reviewer name and review date | Pending |

No independent nontechnical review is claimed as completed.

## 10. Appendix

### 10.1 Evidence references

| Evidence ID | Description |
|---|---|
| E-01 | Task 10 OWASP ZAP baseline report |
| E-02 | Task 10 Nmap local lab scan |
| E-03 | Task 11 SQL source review |
| E-04 | Task 11 HTML rendering screenshot |
| E-05 | Task 11 basket retrieval source review |
| E-06 | Task 12 static analysis and source review evidence |
| E-07 | Task 12 secure-code examples |
| E-08 | Task 14 detection report |
| E-09 | Task 14 detection dashboard |
| E-10 | Task 18 payroll export authorization demonstration |
| E-11 | Task 18 salary authorization demonstration |
| E-12 | Task 18 employee record authorization demonstration |
| E-13 | Task 18 scoped dependency remediation evidence |
| E-16 | 21 November 2026 Juice Shop homepage and product-search API security-header retest |
| E-17 | 21 November 2026 additional Juice Shop public-route security-header review using HEAD requests |

The detailed evidence register is maintained separately at `19_Penetration_Test_Report/evidence/evidence_register.md`.

### 10.2 Tools and command records

The assessment used OWASP ZAP, Nmap, Bandit, Semgrep, Gitleaks, OSV-Scanner, Python-based isolated tests and manual source review.

Detailed command and execution evidence should be retained with the corresponding task reports. This report does not claim that every tool was run against the same target or that every source-code issue was tested at runtime.

### 10.3 Assessment timeline

- 29 October 2026: Task 10 local lab scanning evidence.
- Task 11: Local Juice Shop source and behaviour review.
- Task 12: Payroll sample static analysis and source-code review.
- Task 14: Defensive detection validation.
- Task 18: Remediation examples, isolated authorization tests and scoped dependency review.
- November 2026: Task 19 evidence consolidation and report preparation.

### 10.4 References

- FIRST ? Common Vulnerability Scoring System (CVSS) v3.1: https://www.first.org/cvss/v3.1/
- OWASP Web Security Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- OWASP ZAP documentation: https://www.zaproxy.org/docs/

---

**Final assessment status:** Documentation prepared; assessment completion is pending authorized application-level retesting, production integration validation, and defensible CVSS v3.1 scoring for at least 12 findings as required by the assignment. The current 17 observations remain candidates; the required 12 scored findings have not been established. Independent human review was reported as completed; written review evidence is unavailable.

### 10.5 Additional source evidence

| Evidence ID | Description |
|---|---|
| E-14 | Direct static review of Task 12 payroll sample `app.py` and `requirements.txt`; source-line mapping for PT-04 through PT-13 is recorded in the findings register. |

E-14 confirms the presence of the documented source-code patterns only. It does not establish runtime exploitability, active credentials, network exposure or production impact.








## E-20 – Dependency audit (22 November 2026)

A pip-audit scan of the payroll sample requirements.txt reported 68 vulnerability records across 7 packages: Flask, Jinja2, Werkzeug, PyYAML, Requests, idna and urllib3. The output is preserved in evidence E-20. The reported count may include duplicate advisory records and must not be interpreted as 68 unique vulnerabilities. Dependency upgrades, compatibility testing and a follow-up audit remain pending. The audit covers the supplied payroll dependency manifest only, not every possible project or runtime dependency.
