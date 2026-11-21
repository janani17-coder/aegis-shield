# Task 19 – Evidence Register

## Purpose
This register maps the evidence reviewed for the penetration test report.
Evidence is retained in its original project location. No evidence is represented
as proof of exploitation unless the documented test supports that conclusion.

## Evidence Register

| Evidence ID | Source | Evidence / Observation | Limitation |
|---|---|---|---|
| E-01 | Task 10 | OWASP ZAP baseline report and seven alert categories | Scanner alerts require manual validation |
| E-02 | Task 10 | Nmap scan of local lab ports 3000 and 8081 | Open ports alone do not establish vulnerabilities |
| E-03 | Task 11 | SQL query construction documented in Task 11 notes and report | Original Juice Shop source unavailable in the repository; runtime SQL injection not demonstrated |
| E-04 | Task 11 | 11_Prove_Flaws/evidence/dom-xss-html-rendering.png | HTML interpretation observed; JavaScript execution not demonstrated |
| E-05 | Task 11 | Basket retrieval source review | Cross-user access not tested; other controls not fully reviewed |
| E-06 | Task 12 | Task_12_Secure_Code_Review_Report.md and scan evidence | Sample application not deployed or executed |
| E-07 | Task 12 | secure_login.py, secure_search.py, secure_import.py | Rewritten examples; application integration and runtime retest pending |
| E-08 | Task 14 | Task_14_Attack_Detection_Report.md | 13 planted scenarios detected; alerts are not proof of successful attacks |
| E-09 | Task 14 | Task_14_Detection_Dashboard.png | Visualization of detection results |
| E-10 | Task 18 | R01_Payroll_Export_Remediation_Evidence.md | Isolated demonstration; production integration not verified |
| E-11 | Task 18 | R02_Salary_Access_Remediation_Evidence.md | Isolated demonstration; original application not retested |
| E-12 | Task 18 | R03_Employee_Record_Access_Remediation_Evidence.md | Isolated demonstration; original application not retested |
| E-13 | Task 18 | R14_Dependency_Remediation_Evidence.md and OSV comparison | Limited to eight scoped packages |


| E-15 | Task 19 local lab | Juice Shop homepage and product-search API returned wildcard CORS; OPTIONS preflight returned HTTP 204 with allowed methods. CSP, COEP and COOP were absent from the tested responses. | Limited to the tested local endpoints; sensitive-data exposure, credentialed cross-origin access and exploitability not demonstrated |

## Original Evidence Locations

- `10_Automated_Scanning_and_Triage/`
- `11_Prove_Flaws/`
- `12_Secure_Code_Review/`
- `14_Attack_Detection/`
- `18_Remediation_Sprint/`

## Evidence Handling

- Original evidence files remain in their source folders.
- The Task 19 report references evidence by source path and evidence ID.
- No real customer, employee, or production data was accessed.
- Findings must distinguish source-code observations, demonstrated behavior,
  scanner indicators, and confirmed vulnerabilities.
- CVSS scores must only be assigned where sufficient technical evidence exists.

## Review Status

Evidence inventory: Initial review completed.
Independent human review: Reported completed; written review evidence/sign-off unavailable.
Production validation: Not performed.

## Technical Validation Review – 21 November 2026

- Task 11 evidence was reviewed against the available report, notes and screenshot.
- Task 12 payroll sample source code was inspected directly.
- Three separate remediation examples were reviewed but were not integrated into the original application.
- Scanner observations remain distinct from confirmed vulnerabilities.
- No CVSS v3.1 scores are assigned at this stage.
- Independent human review was reported completed; written review evidence/sign-off was unavailable for inspection. Application-level retesting remains pending.


## Additional Source Evidence

| Evidence ID | Source | Evidence / Observation | Limitation |
|---|---|---|---|
| E-14 | Task 12 | `sample/payroll_portal/app.py` source review (lines 2, 4, 6–8, 12, 17, 20, 23, 26, 28) and `requirements.txt` | Static review only; application not executed; runtime exploitability and deployment exposure not established |

## Additional Retest Evidence

| Evidence ID | Source | Evidence / Observation | Limitation |
|---|---|---|---|
| E-16 | Task 19 authorized local retest - 21 November 2026 | `E-16_Juice_Shop_Header_Retest.md`; homepage and product-search API both returned `Access-Control-Allow-Origin: *`; CSP, COEP and COOP were not observed on either tested response | Limited to two endpoints and one test session; security impact, credentialed access and broader header coverage remain unverified |

| E-17 | Task 19 authorized local retest - 21 November 2026 | `E-17_Additional_Header_Review.md`; three additional public routes returned HTTP 200 and showed wildcard CORS; CSP, COEP and COOP were not observed | Limited to three public routes using HEAD requests; no exploit or security impact demonstrated |

| E-18 | 21 November 2026 independent human review record | independent_human_review_record.md; reviewer Mothilal Nehru; review reported completed | Written feedback and signed approval pending |
