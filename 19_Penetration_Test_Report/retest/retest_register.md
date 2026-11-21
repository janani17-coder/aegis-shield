# Task 19 – Retest Register

## 1. Purpose

Record remediation demonstrations, available before-and-after evidence,
and outstanding application-level validation.

## 2. Retest Results

| Retest ID | Related Finding / Area | Before State | Remediation Evidence | Test Result | Task 19 Status |
|---|---|---|---|---|---|
| RT-01 | Task 12 F-04 – SQL construction | Unsafe SQL string interpolation identified | secure_login.py uses parameterized SQL and password-hash verification | Code example reviewed; no application runtime test | Demonstration reviewed; application retest pending |
| RT-02 | Task 12 F-06 – Search rendering | User input concatenated into HTML template | secure_search.py uses separate template rendering | Code example reviewed; no application runtime test | Demonstration reviewed; application retest pending |
| RT-03 | Task 12 F-08 – Deserialization | pickle.loads used on request data | secure_import.py uses JSON parsing and basic type validation | Code example reviewed; no application runtime test | Demonstration reviewed; application retest pending |
| RT-04 | Task 12 F-05 / salary authorization | Salary route did not visibly enforce ownership | Task 18 R-02 isolated authorization demonstration | 5 passed, 0 failed | Demonstration verified; original application retest pending |
| RT-05 | Employee record ownership | Complete ownership checks not visible | Task 18 R-03 isolated authorization demonstration | 10 passed, 0 failed | Demonstration verified; original application retest pending |
| RT-06 | Payroll export authorization | Complete export approval workflow not visible | Task 18 R-01 isolated authorization demonstration | 5 passed, 0 failed | Demonstration verified; production integration pending |
| RT-07 | Scoped dependencies | 72 vulnerability records across 37 advisory groups | Task 18 scoped review of eight packages | 0 advisory matches; pip check reported no broken requirements | Scoped result verified; full dependency coverage pending |

## 3. Summary

- Isolated authorization demonstrations: 20 tests passed, 0 failed.
- Three secure-code examples reviewed.
- Scoped dependency review: 8 packages, 0 advisory matches after remediation.
- Original payroll sample application: not deployed or executed.
- Production integration: not verified.
- Full application-level retesting: pending.

## 4. Retest Limitations

1. Passing tests apply only to their isolated demonstration code.
2. They do not prove integration with the original payroll application.
3. The three secure-code examples were reviewed as source code; runtime behavior was not independently retested.
4. The dependency result applies only to the eight packages in scope.
5. No production environment or real payroll records were tested.

## 5. Final Retest Status

The isolated remediation demonstrations passed their documented tests.
Application-level and production retesting remain pending.

## 6. Technical Validation Update – 21 November 2026

- The Task 12 payroll source patterns were inspected directly.
- Three secure-code examples remain separate from the original application.
- The 20 passing authorization tests apply only to isolated demonstrations.
- No original payroll application runtime retest has been completed.
- No production integration or production validation is claimed.
- The 17 Task 19 observations remain candidates; successful exploitation has not been established.
- CVSS v3.1 scoring remains pending technical validation.


## 7. Current-Environment Validation – OWASP Juice Shop – 21 November 2026

### Environment

- Application: OWASP Juice Shop
- Version: 20.3.0 (verified from installed package metadata)
- Docker image: `bkimminich/juice-shop:latest`
- Image revision label: `e39a3bd`
- Image ID: `sha256:42843723a7bf4246aa5d63c324978b17ef296ac78434aeddd34c427bfb5853f4`
- Local URL: `http://127.0.0.1:3000`
- Original Task 11 application version: Not recorded; equivalence with the current image is unverified.

### PT-02 – Harmless HTML Rendering Observation

- Original evidence: `11_Prove_Flaws/evidence/dom-xss-html-rendering.png`
- Original notes record that `<b>janani-test</b>` was rendered as bold text.
- Current retest: The same harmless HTML-like search input was rendered as bold text in the current local Juice Shop 20.3.0 environment.
- Search API availability check: HTTP 200.
- Result: HTML interpretation reproduced in the current environment.
- JavaScript execution: Not tested.
- Security impact: Not established.
- Assessment: Reproduced HTML-rendering observation; do not treat as proof of script execution or confirmed exploitation.

### Limitations

This validation applies only to the current local Juice Shop 20.3.0 image. The original Task 11 version was not recorded, so this result cannot establish equivalence with the original test environment or confirm a remediation regression. PT-01 runtime validation and PT-03 cross-user authorization validation remain outstanding.
