# Task 10: Automated Scanning and Triage Report

**Project:** Aegis Shield  
**Phase:** Phase 2  
**Assessment Date:** 29 October 2026  
**Tools:** OWASP ZAP, Nmap  
**Git Tag:** `phase-2`

---

## 1. Objective

The objective of this task was to perform automated security scanning against the local lab environment, review the scanner alerts, and compare automated findings with the manual testing completed in Task 9.

## 2. Scope

Testing was restricted to the locally hosted lab environment.

| Target | Purpose |
|---|---|
| OWASP Juice Shop | Web application testing |
| DVWA | Vulnerable web application lab |
| `http://juice-shop:3000` | ZAP scan target |
| `127.0.0.1` ports 3000 and 8081 | Nmap scan target |

No external systems were scanned.

## 3. Tools Used

- OWASP ZAP – automated web application scanning.
- Nmap 7.992 – port and service detection.
- Docker Desktop – local lab environment.
- VS Code – report preparation.

## 4. Evidence Files

- ZAP HTML report: `05_Lab_and_Samples/zap-reports/task10-zap-report.html`
- Nmap results: `05_Lab_and_Samples/zap-reports/task10-nmap-results.txt`
- Docker configuration: `05_Lab_and_Samples/docker-compose.lab.yml`

## 5. ZAP Scan Summary

The ZAP baseline scan completed successfully.

| Metric | Result |
|---|---:|
| URLs scanned | 116 |
| PASS | 61 |
| WARN-NEW | 7 |
| FAIL-NEW | 0 |
| FAIL-INPROG | 0 |
| INFO | 0 |

The scan reported seven alert categories. These are scanner alerts and must not automatically be treated as confirmed vulnerabilities.

## 6. ZAP Alert Triage

| Alert | ID | Count | ZAP Risk | Verdict |
|---|---:|---:|---|---|
| CSP Header Not Set | 10038 | 5 | Medium | Needs further verification |
| Storable and Cacheable Content | 10049 | 6 | Informational | Informational; review cache context |
| Deprecated Feature Policy Header Set | 10063 | 5 | Low | Needs further verification |
| Cross-Domain Misconfiguration | 10098 | 5 | Medium | Needs further verification |
| Modern Web Application | 10109 | 5 | Informational | Informational |
| Dangerous JS Functions | 10110 | 2 | Low | Needs further verification |
| Cross-Origin-Embedder-Policy Header Missing or Invalid | 90004 | 10 | Low | Needs further verification |

### 6.1 CSP Header Not Set [10038]

- **ZAP Risk:** Medium
- **Count:** 5
- **Verdict:** Needs further verification.
- **Evidence:** ZAP reported that the Content Security Policy response header was not set.
- **Assessment:** A missing CSP header can reduce browser-side protection against certain content-injection attacks. Its absence alone does not prove an exploitable vulnerability.
- **Recommended Fix:** Review the application's content requirements and configure an appropriate Content Security Policy.

### 6.2 Storable and Cacheable Content [10049]

- **ZAP Risk:** Informational
- **Count:** 6
- **Verdict:** Informational; review cache context.
- **Evidence:** ZAP identified responses that may be stored or cached.
- **Assessment:** Caching may be appropriate for public content but should be reviewed for sensitive or user-specific responses.
- **Recommended Fix:** Inspect affected URLs and cache headers. Apply suitable cache-control directives where sensitive information is involved.

### 6.3 Deprecated Feature Policy Header Set [10063]

- **ZAP Risk:** Low
- **Count:** 5
- **Verdict:** Needs further verification.
- **Evidence:** ZAP identified a deprecated Feature Policy header.
- **Assessment:** The alert indicates an outdated browser-policy header. It does not independently confirm a security vulnerability.
- **Recommended Fix:** Review the header configuration and use the modern Permissions-Policy header where appropriate.

### 6.4 Cross-Domain Misconfiguration [10098]

- **ZAP Risk:** Medium
- **Count:** 5
- **Verdict:** Needs further verification.
- **Evidence:** ZAP reported a possible cross-domain configuration issue.
- **Assessment:** An overly permissive cross-origin policy may allow unintended access. The affected URLs and CORS response headers must be inspected before confirming impact.
- **Recommended Fix:** Restrict trusted origins and review allowed methods, headers, and credential settings.

### 6.5 Modern Web Application [10109]

- **ZAP Risk:** Informational
- **Count:** 5
- **Verdict:** Informational.
- **Evidence:** ZAP identified characteristics of a modern web application.
- **Assessment:** This is a technology-identification alert, not evidence of a security vulnerability.
- **Recommended Fix:** No direct security fix is established by this alert. Continue normal dependency and application security reviews.

### 6.6 Dangerous JS Functions [10110]

- **ZAP Risk:** Low
- **Count:** 2
- **Verdict:** Needs further verification.
- **Evidence:** ZAP detected potentially risky JavaScript functions.
- **Assessment:** The presence of these functions alone does not prove that they are exploitable. The affected code and its input handling require manual review.
- **Recommended Fix:** Review the affected JavaScript code and use safer alternatives where appropriate. Validate and safely handle untrusted input.

### 6.7 Cross-Origin-Embedder-Policy Header Missing or Invalid [90004]

- **ZAP Risk:** Low
- **Count:** 10
- **Verdict:** Needs further verification.
- **Evidence:** ZAP reported that the Cross-Origin-Embedder-Policy header was missing or invalid.
- **Assessment:** This may reduce browser isolation protections, but it does not independently confirm an exploitable vulnerability.
- **Recommended Fix:** Review whether cross-origin isolation is required and configure an appropriate COEP policy with compatible application resources.

## 7. Nmap Scan Results

Nmap was used to check ports 3000 and 8081 on the local machine.

| Port | State | Service Detection |
|---|---|---|
| 3000/tcp | Open | `ppp?` – inconclusive |
| 8081/tcp | Open | HTTP – Apache httpd 2.4.25 (Debian) |

**Assessment:** Open ports indicate that services are listening. An open port alone is not proof of a vulnerability. The results are limited to the specified local ports.

## 8. Comparison with Task 9 Manual Testing

Task 9 included manual checks involving:

- Access to account-related areas.
- Login error handling.
- Logout behaviour.
- Browser Local Storage.
- Search input handling.
- Basket workflow.
- Error handling.
- Container image tag review.

The automated ZAP scan identified additional security-header and JavaScript-related observations.

The manual checks and automated scan provide different types of evidence. Neither should be treated as proof of issues outside the specific tests performed.

## 9. Prioritisation and Remediation

The following order is recommended for further investigation. This is a proposed investigation order, not a list of confirmed vulnerabilities.

1. **Cross-Domain Misconfiguration – Medium:** Inspect CORS headers and verify whether unintended origins can access protected resources.
2. **CSP Header Not Set – Medium:** Review the application’s content security requirements and implement an appropriate policy.
3. **Dangerous JS Functions – Low:** Inspect the affected code and determine whether untrusted input can reach the functions.
4. **COEP Header Missing or Invalid – Low:** Review whether cross-origin isolation is required.
5. **Deprecated Feature Policy Header – Low:** Review and modernise the browser-policy configuration.
6. **Storable and Cacheable Content – Informational:** Review caching on sensitive or user-specific responses.
7. **Modern Web Application – Informational:** No direct remediation is indicated by this alert alone.

## 10. Critical Alert That Cannot Be Reproduced

**Question:** A scan reports a critical vulnerability, but manual testing cannot reproduce it. What should you do?

**Answer:**

I would not immediately mark the alert as a false positive. I would:

1. Review the alert description, affected URL, and supporting evidence.
2. Check the scanner configuration and test conditions.
3. Attempt safe manual verification within the authorised lab.
4. Check whether the issue depends on authentication, application state, or specific inputs.
5. Record the reproduction attempts and limitations.
6. Keep the finding unconfirmed if there is insufficient evidence.
7. Escalate it to the team lead for review.

A critical alert should not be ignored just because it cannot immediately be reproduced.

## 11. Limitations

- The ZAP baseline scan is not a complete penetration test.
- Scanner alerts require manual validation.
- Nmap testing covered only the specified local ports.
- No alert is classified as a confirmed vulnerability without sufficient supporting evidence.
- The assessment reflects the lab configuration and application state at the time of testing.

## 12. Conclusion

Task 10 successfully completed automated scanning of the local Aegis Shield lab using OWASP ZAP and Nmap.

ZAP scanned 116 URLs and reported seven alert categories. Nmap identified two open local ports. The reported alerts were reviewed and assigned their displayed ZAP risk levels. Findings requiring additional evidence remain marked as needing further verification.

The results provide a basis for further manual validation and remediation planning in Phase 2.

## 13. References

- OWASP ZAP: https://www.zaproxy.org/
- Nmap: https://nmap.org/
- DefectDojo: https://defectdojo.com/
- OWASP Top 10: https://owasp.org/www-project-top-ten/

---

**Status:** Task 10 scanning and initial alert triage completed. Further verification remains pending for selected alerts.