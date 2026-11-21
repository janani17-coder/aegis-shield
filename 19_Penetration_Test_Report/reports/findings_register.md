# Task 19 – Candidate Findings Register

| ID | Source | Finding | Evidence | Initial status | CVSS v3.1 |
|---|---|---|---|---|---|
| PT-01 | Task 11 – Juice Shop | SQL query constructed using untrusted input | E-03 | Source pattern identified; runtime validation pending | Not scored |
| PT-02 | Task 11 – Juice Shop | Unsafe HTML rendering in search results | E-04 | HTML interpretation observed; script execution not demonstrated | Not scored |
| PT-03 | Task 11 – Juice Shop | Basket ownership check not visible in reviewed function | E-05 | Potential issue; cross-user access not tested | Not scored |
| PT-04 | Task 12 – Payroll sample | Hardcoded Flask session secret | E-06 | Code pattern confirmed; application not deployed | Not scored |
| PT-05 | Task 12 – Payroll sample | Synthetic AWS-like credentials in source | E-06 | Hardcoded example values; active status not verified | Not scored |
| PT-06 | Task 12 – Payroll sample | MD5 password hashing | E-06 | Code pattern confirmed; runtime and database exposure unknown | Not scored |
| PT-07 | Task 12 – Payroll sample | SQL query string interpolation | E-06 | Code pattern confirmed; runtime injection not tested | Not scored |
| PT-08 | Task 12 – Payroll sample | Salary route lacks visible ownership check | E-06, E-11 | Isolated remediation passed; original application not retested | Not scored |
| PT-09 | Task 12 – Payroll sample | User input concatenated into HTML template | E-06, E-07 | Code pattern confirmed; runtime behavior not tested | Not scored |
| PT-10 | Task 12 – Payroll sample | User-controlled filename appended to download path | E-06 | Code pattern confirmed; path controls not fully reviewed | Not scored |
| PT-11 | Task 12 – Payroll sample | Unsafe pickle deserialization | E-06, E-07 | Code pattern confirmed; runtime behavior not tested | Not scored |
| PT-12 | Task 12 – Payroll sample | Flask debug mode enabled | E-06 | Configuration confirmed in sample; exposure unknown | Not scored |
| PT-13 | Task 12 – Payroll sample | Listener bound to all network interfaces | E-06 | Configuration confirmed; network exposure unknown | Not scored |
| PT-14 | Task 10 – Juice Shop | Wildcard CORS response header | E-01, E-16, E-17 | Wildcard CORS observed on five public endpoints; sensitive-data exposure not established | Not scored |
| PT-15 | Task 10 – Juice Shop | Content Security Policy header missing | E-01, E-16, E-17 | CSP not observed on five tested public endpoints; exploit not demonstrated | Not scored |
| PT-16 | Task 10 – Juice Shop | Cross-Origin-Embedder-Policy header missing or invalid | E-01, E-16, E-17 | COEP not observed on five tested public endpoints; impact not demonstrated | Not scored |
| PT-17 | Task 10 – Juice Shop | Cross-Origin-Opener-Policy header missing or invalid | E-01, E-16, E-17 | COOP not observed on five tested public endpoints; impact not demonstrated | Not scored |

| PT-18 | Payroll dependency manifest | Outdated dependencies with known vulnerability advisories | E-20 | 68 reported advisory records across 7 packages; duplicate records may exist; remediation and compatibility testing pending | Not scored |

## Scoring Rules

1. Use CVSS v3.1 base metrics and include the complete vector for every finding that can be defensibly scored.
2. Mark a score provisional if important exploitability or impact assumptions remain unverified.
3. Do not assign CVSS scores to synthetic credentials or unconfirmed possibilities without sufficient evidence.
4. Keep scanner indicators separate from confirmed findings.
5. Record unscored candidates transparently and explain what additional validation is needed.

## Current Status

Candidate observations recorded: 18 (including 4 Task 10 scanner observations).
Confirmed exploited vulnerabilities: Not established.
CVSS scoring: No scores assigned; technical validation required before scoring.



## Technical Validation Review â€“ 21 November 2026

### Review Scope
Reviewed the available Task 11 notes and report, Task 12 payroll sample source code, and three separate remediation examples.

### Updated Evidence Assessment

| ID | Updated assessment | Validation limitation | CVSS v3.1 |
|---|---|---|---|
| PT-01 | SQL interpolation documented in Task 11 notes | Original Juice Shop source unavailable; runtime validation not performed | Not scored |
| PT-02 | Unsafe HTML rendering documented; HTML interpretation screenshot exists | Original source unavailable; JavaScript execution not demonstrated | Not scored |
| PT-03 | Potential basket ownership gap documented | Cross-user access not tested; original source unavailable | Not scored |
| PT-04 | Hardcoded Flask session secret confirmed in sample app.py line 4 | Sample app not deployed; secret reuse or production exposure not established | Not scored |
| PT-05 | Synthetic AWS-like example values confirmed in sample app.py lines 6–7 | Active credentials not established; not treated as a confirmed credential leak | Not scored |
| PT-06 | MD5 password hashing confirmed in sample app.py line 8; separate example uses check_password_hash | Hash generation, password migration, integration and runtime retest not verified | Not scored |
| PT-07 | SQL string interpolation confirmed in sample app.py line 12; separate example uses parameterized SQL | Replacement not integrated; runtime injection and application retest not performed | Not scored |
| PT-08 | Salary route lacks visible authentication or ownership check in lines 15–17 | No secure salary-route replacement found; other controls and runtime access not tested | Not scored |
| PT-09 | User input concatenated into render_template_string in line 20; separate example uses render_template and a Jinja variable with default auto-escaping | Template source reviewed; integration and runtime retest not performed | Not scored |
| PT-10 | User-controlled filename appended to download path in line 23 | No secure download replacement found; filesystem controls and runtime access not tested | Not scored |
| PT-11 | pickle.loads applied to request data in line 26; separate example uses JSON parsing and validates top-level data type | Replacement not integrated; runtime retest not performed | Not scored |
| PT-12 | Flask debug=True confirmed in line 28 | No secure startup configuration found; deployment exposure unknown | Not scored |
| PT-13 | host="0.0.0.0" confirmed in line 28 | Network reachability and deployment context unknown; no secure replacement found | Not scored |
| PT-14 | Wildcard CORS; reconfirmed on two endpoints in E-16 | Sensitive-data exposure not established | Not scored |
| PT-15 | CSP absent on two endpoints in E-16 | Exploit not demonstrated | Not scored |
| PT-16 | COEP absent on two endpoints in E-16 | Security impact not established | Not scored |
| PT-17 | COOP absent on two endpoints in E-16 | Security impact not established | Not scored |

### Review Conclusion
The available evidence confirms several insecure source-code patterns in the supplied training sample. It does not establish that the sample application was deployed, externally reachable, or successfully exploited.

The three remediation examples were reviewed as separate code examples. They have not been integrated into the original sample application.

No CVSS v3.1 scores are assigned during this review because the available evidence does not establish all required vulnerability and impact assumptions. Additional validation and independent review are pending.


## E-14 Source-Line Mapping

| Finding ID | Source location | Evidence reference |
|---|---|---|
| PT-04 | app.py, line 4 | E-14 |
| PT-05 | app.py, lines 6â€“7 | E-14 |
| PT-06 | app.py, line 8 | E-14 |
| PT-07 | app.py, line 12 | E-14 |
| PT-08 | app.py, lines 15â€“17 | E-14 |
| PT-09 | app.py, line 20 | E-14 |
| PT-10 | app.py, line 23 | E-14 |
| PT-11 | app.py, line 26 | E-14 |
| PT-12 | app.py, line 28 (debug configuration) | E-14 |
| PT-13 | app.py, line 28 (network binding) | E-14 |

Note: These references establish source-code observations only. They do not establish runtime exploitability or deployment exposure.





