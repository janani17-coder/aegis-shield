# Task 19 – Finding Validation Matrix

**Purpose:** Track the evidence and validation required for candidate findings PT-01 to PT-17.
**Status:** Partially updated – source review and limited local header retesting documented; application-level validation, scoring and sign-off remain incomplete.
**Rule:** Do not assign CVSS v3.1 scores without sufficient verified evidence.

| ID | Finding | Current evidence | Validation still required | Current scoring status |
|---|---|---|---|---|
| PT-01 | SQL query construction – Juice Shop | Task 11 report and notes; original login.ts unavailable locally; runtime proof pending | Obtain and review the authorized source; assess runtime behavior and impact if safely available | Not eligible yet |
| PT-02 | Unsafe HTML rendering – Juice Shop | Task 11 notes and screenshot; harmless HTML formatting interpreted | Review available source and browser behavior; JavaScript execution and security impact remain unverified | Not eligible yet |
| PT-03 | Basket ownership – Juice Shop | Task 11 notes; own-basket access confirmed; source review suggests ownership check may be absent | Cross-user authorization was not tested; review complete route and middleware controls before drawing a conclusion | Not eligible yet |
| PT-04 | Hardcoded session secret – payroll sample | app.py confirms a literal Flask secret; separate environment-variable remediation example reviewed but not integrated or runtime-tested | Establish whether the sample was deployed and whether the secret was exposed; verify remediation integration and retest if applicable | Not eligible yet |
| PT-05 | Synthetic AWS-like credentials | Source contains AWS-like strings marked EXAMPLE; no genuine credential exposure established | No credential use or authentication attempt; retain as a synthetic example unless independent evidence proves genuine exposure | Excluded from CVSS scoring |
| PT-06 | MD5 password hashing | app.py confirms MD5 password hashing without a visible salt; runtime and hash exposure unknown | Establish whether real password hashes exist or are exposed; verify migration to a suitable password-hashing method and retest | Not eligible yet |
| PT-07 | SQL query interpolation – payroll sample | app.py line 12 confirms f-string SQL construction in the login query; line 17 uses parameterized SQL | Review query handling and application context; runtime injection and impact remain unverified | Not eligible yet |
| PT-08 | Salary route authorization – payroll sample | Original salary route has no visible authentication, role or ownership checks; isolated R02 remediation passed 5/5 tests but was not integrated | Validate authorization in the original application; production integration and real-record testing remain pending | Not eligible yet |
| PT-09 | Unsafe template construction – payroll sample | app.py line 20 concatenates the request parameter into a string passed to render_template_string | Review template handling and application context; runtime behavior and security impact remain unverified | Not eligible yet |
| PT-10 | Download path construction – payroll sample | app.py download route concatenates the file request parameter with the reports directory; no path validation is visible in that route | Review surrounding application controls and authorized file-access rules; traversal and impact remain unverified | Not eligible yet |
| PT-11 | Unsafe pickle deserialization – payroll sample | Original app.py uses pickle.loads(request.data); separate secure_import.py example uses JSON parsing but is not integrated or runtime-tested | Review application context and verify safe import handling; deployment, runtime behavior and impact remain unverified | Not eligible yet |
| PT-12 | Flask debug mode – payroll sample | app.py line 28 confirms app.run(debug=True); deployment and external exposure are unknown | Verify deployment configuration and whether debug mode was exposed; runtime impact remains unverified | Not eligible yet |
| PT-13 | Listener bound to all interfaces – payroll sample | app.py line 28 specifies host=0.0.0.0; actual deployment and network reachability are unknown | Verify authorized deployment configuration and network exposure; external accessibility and impact remain unverified | Not eligible yet |
| PT-14 | Wildcard CORS – local Juice Shop | E-15 records wildcard CORS and HTTP 204 preflight; E-16 GET retest and E-17 HEAD review observed wildcard CORS on five public routes | Assess endpoint sensitivity and browser access controls; credentialed access, sensitive-data exposure and exploitability remain unverified | Not eligible yet |
| PT-15 | Missing Content Security Policy – local Juice Shop | E-15 records CSP absence; E-16 GET retest and E-17 HEAD review did not observe CSP on five public routes | Confirm header coverage across relevant endpoints and assess security impact; exploitability remains unverified | Not eligible yet |
| PT-16 | Missing Cross-Origin-Embedder-Policy – local Juice Shop | E-15 records COEP absence; E-16 GET retest and E-17 HEAD review did not observe COEP on five public routes | Confirm header coverage and assess whether cross-origin isolation is required; security impact remains unverified | Not eligible yet |
| PT-17 | Missing Cross-Origin-Opener-Policy – local Juice Shop | E-15 records COOP absence; E-16 GET retest and E-17 HEAD review did not observe COOP on five public routes | Confirm header coverage and assess application requirements; security impact remains unverified | Not eligible yet |

## Validation rules

1. Use only the authorized local lab and supplied project files.
2. Record the exact test, date, result and evidence location.
3. Distinguish confirmed source patterns from runtime-verified vulnerabilities.
4. Record failed, inconclusive and successful tests honestly.
5. Assign CVSS v3.1 scores only when the vulnerability and scoring assumptions are supported.
6. Do not count synthetic credentials or unverified scanner observations as confirmed vulnerabilities.

## Completion tracking

- [x] Review all 17 candidate findings at the evidence and documentation level.
- [ ] Complete appropriate authorized validation.
- [ ] Identify findings with sufficient evidence for CVSS scoring.
- [ ] Obtain at least 12 defensible CVSS v3.1 scores if supported by the evidence.
- [ ] Update the findings register and main report.
- [ ] Complete retesting and independent review.





















## Review completion update

- [x] Independent human review reported completed – Mothilal Nehru, 21 November 2026 (E-18). Written sign-off pending.
- [x] Nontechnical reader review reported completed – 21 November 2026 (E-19). Written feedback pending.

## PT-18 – Dependency audit

- Evidence: E-20 (pip-audit output).
- Result: 68 reported vulnerability records across 7 packages in the payroll dependency manifest.
- Limitation: Duplicate advisory records may exist; the count is not a unique-vulnerability count.
- Pending: Review advisories, upgrade affected dependencies, test compatibility and rerun the audit.
- CVSS: Not assigned; applicability and impact require assessment.
