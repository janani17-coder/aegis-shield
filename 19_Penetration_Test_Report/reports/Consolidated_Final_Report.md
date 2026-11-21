# AEGIS SHIELD – CONSOLIDATED CYBERSECURITY PROJECT REPORT

**Prepared by:** JANANI M.  
**Track:** Cybersecurity  
**Repository:** https://github.com/janani17-coder/aegis-shield  
**Security Hub:** https://janani17-coder.github.io/aegis-shield/  
**Report date:** 22 November 2026  
**Project:** Aura Workforce – Security Assessment and Improvement

---

## 1. Executive Summary

Aegis Shield documents a cybersecurity assessment and improvement project for the fictional Aura Workforce environment. The work covers data classification, threat modelling, security policies, a local testing environment, secure code review, audit-log integrity, security monitoring, incident response, remediation demonstrations, penetration-test reporting and staff security awareness.

The project combines documentation, static analysis, controlled local testing and defensive validation. It uses synthetic data and intentionally vulnerable local applications for lab activities. It does not represent a production security certification or proof that every finding is exploitable.

The overall recommendation is **NOT READY for production go-live**. Several useful controls and demonstrations have been completed, but important validation, dependency review, formal approvals and operational readiness activities remain outstanding.

## 2. Scope and Methodology

The project uses the fictional Aura Workforce environment and a local development/testing setup. The assessment work includes:

- Reviewing data fields and assigning classification levels.
- Identifying threats and documenting security policies.
- Using local lab applications for controlled security testing.
- Reviewing sample application code and dependency information.
- Demonstrating defensive audit and detection capabilities.
- Preparing incident response playbooks.
- Demonstrating selected remediation controls.
- Recording candidate findings, risks, limitations and recommendations.

The evidence should be interpreted within its stated scope. Synthetic records, local lab results and isolated demonstrations are not evidence of production deployment or production effectiveness.

## 3. Data Classification and Threat Modelling

The data classification exercise covered 169 fields:

| Classification | Field count |
|---|---:|
| Public | 0 |
| Internal | 60 |
| Confidential | 74 |
| Restricted | 35 |
| **Total** | **169** |

The classification work provides a basis for handling information according to sensitivity. Confidential and Restricted information require stronger access controls and careful handling.

The STRIDE threat-modelling exercise considered the Aura Workforce environment. It provided a structured way to consider spoofing, tampering, repudiation, information disclosure, denial of service and elevation of privilege.

The threat model is a planning and risk-identification document. It should be reviewed whenever the application architecture, data flows or business requirements change.

## 4. Security Policies and Governance

The project prepared a policy pack containing ten security policies and supporting mapping and review documents.

The policies establish expectations for areas such as access control, information handling, secure development, monitoring and incident response. They provide a starting point for consistent security practices.

Policies alone do not demonstrate implementation. Management ownership, employee communication, operational procedures, periodic reviews and evidence of compliance are still needed before these documents can be treated as approved organisational controls.

## 5. Local Security Lab and Testing

A local testing environment was prepared using Docker-based lab applications, including OWASP Juice Shop and DVWA. Supporting tools included OWASP ZAP and Nmap.

The lab was intended for controlled learning and assessment. Results from these intentionally vulnerable applications must not be interpreted as findings against a live production service.

The project retained task-specific reports and evidence to distinguish local testing, source-code review and other assessment activities. Findings should always be linked to the exact target, method and evidence that support them.

## 6. Secure Code Review and Dependency Review

The secure code review included Semgrep, Bandit, Gitleaks and OSV checks.

Recorded results included:

| Check | Before | After |
|---|---:|---:|
| Semgrep findings | 12 | 0 |
| Bandit findings | 8 | 0 |
| Gitleaks | No leaks reported | No leaks reported |

The results document the changes observed in the reviewed scope. They do not prove that all possible code weaknesses have been eliminated.

Dependency review requires particular care. The Task 19 dependency evidence recorded 68 advisory records, representing 36 unique package-advisory combinations across seven packages. Applicability, upgrade compatibility and follow-up validation remain pending.

A separate global Python environment check reported no broken requirements. That result does not establish that the payroll application's dependency manifest is free of vulnerabilities.

## 7. Audit Logging and Integrity

The payroll audit exercise processed 2,652 synthetic audit records. The recorded fields included timestamp, actor, action, target employee and result.

The exercise included a hash-chain integrity demonstration:

- The original event sequence passed the integrity check.
- A modified event sequence failed validation.
- The recorded result identified a hash mismatch at event 1.

This demonstrates the value of tamper-evident audit records in a controlled example. A production implementation would also require secure key management where applicable, protected storage, access restrictions, time synchronisation, monitoring and operational retention procedures.

## 8. Security Monitoring and Detection

The detection exercise processed three categories of local or synthetic input:

| Input | Records |
|---|---:|
| Authentication events | 11,487 |
| Payroll events | 2,652 |
| Parsed web requests | 5,805 |
| **Total** | **19,944** |

The final detection output contained 21 alert rows across authentication, payroll and web activity rules. The planted validation scenarios were detected in 13 out of 13 cases.

These results demonstrate that the implemented rules detected the prepared test scenarios. They do not establish detection coverage for every real-world attack, nor do they measure production false-positive and false-negative rates.

## 9. Incident Response

Three incident response playbooks were prepared:

1. Payroll data breach.
2. Ransomware.
3. Insider salary leak.

The playbooks provide a structured starting point for triage, escalation, containment, investigation, recovery and lessons learned.

An AI-assisted tabletop exercise was used for planning. A formal human-led exercise and written approvals remain outstanding. The organisation must also confirm actual incident contacts, escalation routes, decision owners and communication procedures before operational use.

## 10. Remediation Demonstrations

The remediation sprint included isolated demonstrations relating to:

- Payroll export authorisation.
- Salary access control.
- Employee-record ownership.

The associated regression tests recorded 20 passing tests. These results support the behaviour of the isolated examples under their tested conditions.

The demonstrations do not establish that the controls have been integrated into a production application. Integration, code review, deployment controls, security testing and regression testing in the target environment remain necessary.

## 11. Penetration-Test Reporting and Findings

Task 19 documented 18 candidate observations in the findings register and supporting report.

These are candidate findings, not a declaration that all 18 have been independently confirmed as exploitable. The report status remains **IN PROGRESS – NOT YET APPROVED**.

The report does not assign unsupported CVSS scores. Evidence review, application-level validation, dependency applicability assessment, severity decisions and formal approval remain outstanding.

An independent human review and a nontechnical reader review were reported as completed on 21 November 2026. Written sign-off and feedback records still need to be retained.

The report and executive brief are available in the repository under `19_Penetration_Test_Report/reports/`.

## 12. Awareness and Security Hub

A central Security Hub was prepared to provide access to the project's key deliverables, including classification material, the threat model, policies, findings, risk register, playbooks, detection evidence, assessment reports and awareness material.

A staff awareness guide covers phishing, passwords, multi-factor authentication, protection of sensitive information and reporting suspicious activity.

A static knowledge-check quiz was added on the `task20-awareness-improvement` branch. It is a self-review resource and is not an interactive or scored training system.

Before the awareness guide is used operationally, management must publish the correct reporting contact, escalation route and approved support channels. The Security Hub build completed locally; public deployment and access should be confirmed before the link is treated as live.

## 13. Risk Assessment and Go-Live Decision

The project's go-live recommendation is **NOT READY**.

The most important unresolved concern is whether the remaining candidate findings and dependency advisories have been fully assessed, prioritised, remediated where necessary and independently validated.

The following activities are required before reconsidering go-live:

1. Complete authorised application-level validation and retesting.
2. Review all candidate findings and confirm their status using supporting evidence.
3. Assess dependency advisory applicability and approve compatible updates.
4. Integrate remediation changes into the intended application and test them there.
5. Confirm production identity, MFA, access controls, logging, monitoring and backup arrangements.
6. Complete a human-led incident response exercise.
7. Confirm incident contacts and escalation procedures.
8. Obtain written technical, business and management approvals.
9. Publish and verify the Security Hub and awareness guide.

The CEO-level message is straightforward: the project has produced useful security documentation and controlled demonstrations, but unresolved validation and operational readiness work means production launch should be delayed.

## 14. Lessons Learned

The project demonstrated that cybersecurity work requires more than running tools. Findings must be supported by evidence, and the scope and limitations of each test must be clearly stated.

It also showed the importance of connecting secure coding, access control, logging, detection and incident response. A control is only useful when it is implemented, tested and owned by the appropriate people.

Finally, honest reporting is essential. A clean test result in one scope must not be presented as proof that an entire system is secure.

## 15. Future Improvements

Recommended next steps include:

- Complete Task 17 evidence and confirm its deliverables.
- Close outstanding dependency and penetration-test review activities.
- Record written reviewer and management approvals.
- Conduct a human-led incident response tabletop exercise.
- Integrate and validate remediation in the intended application.
- Improve detection testing with additional representative scenarios.
- Add operational ownership and review dates to policies and playbooks.
- Verify public Security Hub deployment and complete the demonstration recording.

## 16. Conclusion

Aegis Shield brings together security assessment documentation, local testing, defensive demonstrations, remediation examples and awareness resources for the fictional Aura Workforce environment.

The work provides a foundation for continued security improvement. However, the outstanding validation, dependency review, human exercise, operational controls and approvals are material limitations.

The final recommendation remains **NOT READY for production go-live** until the required activities are completed and supported by evidence.

---

**Prepared by:** JANANI M.  
**Project repository:** https://github.com/janani17-coder/aegis-shield  
**Security Hub:** https://janani17-coder.github.io/aegis-shield/
