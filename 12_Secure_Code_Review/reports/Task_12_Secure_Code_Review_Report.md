# Task 12 – Secure Code Review and Secrets Scanning

## 1. Scope and Method
Reviewed the supplied payroll portal sample source code without deploying or running the application.
Performed static analysis using Bandit and Semgrep, secrets scanning using Gitleaks, dependency advisory scanning using OSV-Scanner, and manual source review.

The sample is a local training copy. The AWS-like credentials and Flask secret are synthetic values supplied for this exercise, not verified active credentials.

## 2. Before-and-After Scan Results

| Tool | Before | After | Notes |
|---|---:|---:|---|
| Bandit | 8 findings | 0 findings | Python security findings |
| Semgrep OSS | 12 findings | 0 findings | Some baseline rules reported overlapping issues |
| Gitleaks | No leaks detected | No leaks detected | Did not detect the synthetic sample secrets |
| OSV-Scanner | 72 vulnerability records across 37 advisory groups in the scoped baseline | 0 advisory matches across 8 scoped packages | Task 18 remediation; full application dependency coverage remains unverified |

Semgrep scanned 4 Git-tracked files in the final scan using 290 rules.
Bandit scanned the fixed Python files recursively.
Gitleaks scanned the fixed_code directory and reported no leaks.

Raw finding counts from different tools are not directly comparable. Multiple rules can identify the same underlying weakness.

## 3. Source Review Findings

| ID | File / Location | Finding | OWASP Top 10:2025 | Severity | Recommended Fix |
|---|---|---|---|---|---|
| F-01 | app.py, line 4 | Hardcoded Flask session secret | A02 Security Misconfiguration | High | Load a strong secret from a protected environment or secret manager |
| F-02 | app.py, lines 6–7 | Hardcoded AWS-like credentials | A02 Security Misconfiguration | Critical | Remove secrets from source and use a secret manager; verify and rotate only if credentials are real |
| F-03 | app.py, line 8 | MD5 used for password hashing | A04 Cryptographic Failures | High | Use a password-hashing function such as Werkzeug's secure password hash utilities or Argon2 |
| F-04 | app.py, login function | SQL query built using string interpolation | A05 Injection | Critical | Use parameterized SQL queries |
| F-05 | app.py, salary function | No authentication or employee ownership check visible in the function | A01 Broken Access Control | High | Enforce authentication and verify the requested employee record belongs to the authorized user |
| F-06 | app.py, search function | User input concatenated into a template string | A05 Injection | High | Use a separate template and normal variable rendering with automatic escaping |
| F-07 | app.py, download function | User-controlled filename appended to a filesystem path | A01 Broken Access Control | High | Restrict downloads to an allowlisted set of files and enforce safe path handling |
| F-08 | app.py, import function | Unsafe deserialization using pickle.loads | A08 Software or Data Integrity Failures | Critical | Use a safe data format such as JSON and validate its schema |
| F-09 | app.py, app.run | Flask debug mode enabled | A02 Security Misconfiguration | High | Disable debug mode outside local development |
| F-10 | app.py, app.run | Listener bound to all network interfaces | A02 Security Misconfiguration | Medium | Bind only to the required interface and apply network restrictions |

F-05 is a source-level concern: route-level or middleware protections were not fully verified.
F-07 requires review of filename validation and the surrounding application controls before confirming exploitability.
F-10 is context-dependent and is not automatically a vulnerability.

## 4. Dependency Review

The initial OSV-Scanner baseline identified dependency advisories. A separate scoped remediation review was completed in Task 18.

Eight packages were reviewed using Python 3.11.9:

- Flask 3.1.3
- Jinja2 3.1.6
- PyYAML 6.0.3
- requests 2.34.2
- Werkzeug 3.1.9
- certifi 2026.10.23
- urllib3 2.8.0
- idna 3.20

Scoped scan comparison:
- Before: 8 packages, 37 advisory groups, and 72 vulnerability records.
- After: 8 packages, 0 advisory groups, and 0 vulnerability records.
- `pip check`: no broken requirements.

These results apply only to the eight scoped packages reviewed in Task 18. They do not establish that every application dependency is free of vulnerabilities. Full application testing and production validation remain pending.

Advisory identifiers can overlap or refer to aliases for the same issue. An advisory does not automatically prove that a vulnerable code path is reachable.
## 5. Fixed Code

Three weak functions were rewritten as separate review examples:

1. secure_login.py – parameterized SQL, secure password-hash verification, and environment-based Flask secret.
2. secure_search.py – uses render_template with a separate HTML template and automatic escaping.
3. secure_import.py – replaces unsafe pickle deserialization with JSON parsing and basic input validation.

The sample application was not deployed or executed. Database migration and environment configuration would be required before any production use.

## 6. Scanner Comparison

- Bandit identified Python-specific weaknesses such as MD5 usage, hardcoded values, unsafe deserialization, SQL construction, and debug configuration.
- Semgrep identified unsafe template construction and overlapping SQL injection and deserialization patterns.
- Gitleaks did not detect the synthetic hardcoded sample values. This demonstrates that a clean secrets scan does not guarantee that source code contains no secrets.
- OSV-Scanner initially identified dependency advisories. Task 18 later recorded zero advisory matches across the eight scoped remediated packages; full application dependency coverage remains unverified.
- Manual review identified concerns requiring application context, including salary-record authorization and download path handling.

No single scanner covers every weakness. Manual review and multiple complementary tools are necessary.

## 7. Reference Comparison Limitation

The requested unlock_AS-12 reference file was not available in the supplied repository or to the reviewer. Therefore, the exact 11 planted issues could not be independently compared or confirmed. The findings above are based on the supplied source code and scanner evidence; they are not represented as a verified match to all 11 planted issues.

## 8. Evidence Files

Before:
- evidence/before/bandit_before.json
- evidence/before/semgrep_before.json
- evidence/before/gitleaks_before.json
- evidence/before/gitleaks_git_history_before.json
- evidence/before/osv_before.json

After:
- evidence/after/bandit_after.json
- evidence/after/semgrep_after.json
- evidence/after/gitleaks_after.json

## 9. Conclusion

The three selected weak functions were rewritten. Final Bandit and Semgrep scans reported zero findings, and Gitleaks reported no leaks in the fixed-code directory.

The scoped dependency remediation completed in Task 18 recorded zero OSV advisory matches across eight reviewed packages, with no broken requirements reported by pip check. This result does not establish that every application dependency is free of vulnerabilities. Full application testing and production validation remain pending. The results demonstrate improved static-analysis findings, not proof that the complete payroll application is secure.
