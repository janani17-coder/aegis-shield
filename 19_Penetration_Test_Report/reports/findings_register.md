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

