# Task 19 – Candidate Findings Register

| ID | Source | Finding | Evidence | Initial status | CVSS v3.1 |
|---|---|---|---|---|---|
| PT-01 | Task 11 – Juice Shop | SQL query constructed using untrusted input | E-03 | Source pattern identified; runtime validation pending | Pending validation |
| PT-02 | Task 11 – Juice Shop | Unsafe HTML rendering in search results | E-04 | HTML interpretation observed; script execution not demonstrated | Provisional assessment required |
| PT-03 | Task 11 – Juice Shop | Basket ownership check not visible in reviewed function | E-05 | Potential issue; cross-user access not tested | Not scored |
| PT-04 | Task 12 – Payroll sample | Hardcoded Flask session secret | E-06 | Code pattern confirmed; application not deployed | Pending validation |
| PT-05 | Task 12 – Payroll sample | Synthetic AWS-like credentials in source | E-06 | Hardcoded example values; active status not verified | Not scored |
| PT-06 | Task 12 – Payroll sample | MD5 password hashing | E-06 | Code pattern confirmed; runtime and database exposure unknown | Pending validation |
| PT-07 | Task 12 – Payroll sample | SQL query string interpolation | E-06 | Code pattern confirmed; runtime injection not tested | Pending validation |
| PT-08 | Task 12 – Payroll sample | Salary route lacks visible ownership check | E-06, E-11 | Isolated remediation passed; original application not retested | Pending validation |
| PT-09 | Task 12 – Payroll sample | User input concatenated into HTML template | E-06, E-07 | Code pattern confirmed; runtime behavior not tested | Pending validation |
| PT-10 | Task 12 – Payroll sample | User-controlled filename appended to download path | E-06 | Code pattern confirmed; path controls not fully reviewed | Pending validation |
| PT-11 | Task 12 – Payroll sample | Unsafe pickle deserialization | E-06, E-07 | Code pattern confirmed; runtime behavior not tested | Pending validation |
| PT-12 | Task 12 – Payroll sample | Flask debug mode enabled | E-06 | Configuration confirmed in sample; exposure unknown | Pending validation |
| PT-13 | Task 12 – Payroll sample | Listener bound to all network interfaces | E-06 | Configuration confirmed; network exposure unknown | Not scored |

## Scoring Rules

1. Use CVSS v3.1 base metrics and include the complete vector for every finding that can be defensibly scored.
2. Mark a score provisional if important exploitability or impact assumptions remain unverified.
3. Do not assign CVSS scores to synthetic credentials or unconfirmed possibilities without sufficient evidence.
4. Keep scanner indicators separate from confirmed findings.
5. Record unscored candidates transparently and explain what additional validation is needed.

## Current Status

Candidate observations recorded: 17 (including 4 Task 10 scanner observations).
Confirmed exploited vulnerabilities: Not established.
CVSS scoring: Pending technical validation.

| PT-14 | Task 10 – Juice Shop | Wildcard CORS response header | E-01 | Scanner evidence; sensitive-data exposure not established | Not scored |
| PT-15 | Task 10 – Juice Shop | Content Security Policy header missing | E-01 | Scanner observation; exploit not demonstrated | Not scored |
| PT-16 | Task 10 – Juice Shop | Cross-Origin-Embedder-Policy header missing or invalid | E-01 | Scanner observation; impact not demonstrated | Not scored |
| PT-17 | Task 10 – Juice Shop | Cross-Origin-Opener-Policy header missing or invalid | E-01 | Scanner observation; impact not demonstrated | Not scored |


## Technical Validation Review â€“ 21 November 2026

### Review Scope
Reviewed the available Task 11 notes and report, Task 12 payroll sample source code, and three separate remediation examples.

### Updated Evidence Assessment

| ID | Updated assessment | Validation limitation | CVSS v3.1 |
|---|---|---|---|
| PT-01 | SQL interpolation documented in Task 11 notes | Original Juice Shop source unavailable; runtime validation not performed | Not scored |
| PT-02 | Unsafe HTML rendering documented; HTML interpretation screenshot exists | Original source unavailable; JavaScript execution not demonstrated | Not scored |
| PT-03 | Potential basket ownership gap documented | Cross-user access not tested; original source unavailable | Not scored |
| PT-04 | Hardcoded Flask session secret confirmed in sample app.py line 4 | Sample app not deployed or executed | Pending |
| PT-05 | Synthetic AWS-like values confirmed in sample app.py lines 6â€“7 | Active credentials not established | Not scored |
| PT-06 | MD5 password hashing confirmed in sample app.py line 8 | Runtime and password database exposure not tested; separate replacement example reviewed | Pending |
| PT-07 | SQL string interpolation confirmed in sample app.py line 12 | Runtime injection not tested; separate parameterized example reviewed | Pending |
| PT-08 | Salary route lacks visible authentication or ownership check in lines 15â€“17 | Other controls not tested; isolated remediation is not integrated | Pending |
| PT-09 | User input concatenated into render_template_string in line 20 | Runtime behavior not tested; separate template example reviewed | Pending |
| PT-10 | User-controlled filename appended to download path in line 23 | Path validation and filesystem controls not tested | Pending |
| PT-11 | pickle.loads applied to request data in line 26 | Runtime behavior not tested; separate JSON example reviewed | Pending |
| PT-12 | Flask debug=True confirmed in line 28 | Exposure and deployment configuration unknown | Pending |
| PT-13 | host="0.0.0.0" confirmed in line 28 | Network reachability and deployment context unknown | Not scored |
| PT-14 | Wildcard CORS scanner observation | Sensitive-data exposure not established | Not scored |
| PT-15 | Missing CSP scanner observation | Exploit and impact not established | Not scored |
| PT-16 | Missing or invalid COEP scanner observation | Security impact not established | Not scored |
| PT-17 | Missing or invalid COOP scanner observation | Security impact not established | Not scored |

### Review Conclusion
The available evidence confirms several insecure source-code patterns in the supplied training sample. It does not establish that the sample application was deployed, externally reachable, or successfully exploited.

The three remediation examples were reviewed as separate code examples. They have not been integrated into the original sample application.

No CVSS v3.1 scores are assigned during this review because the available evidence does not establish all required vulnerability and impact assumptions. Additional validation and independent review are pending.

