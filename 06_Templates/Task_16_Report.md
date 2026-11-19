git status# Task 16 – Risk Register and Compliance Mapping

**Project:** Aegis Shield – Cybersecurity Assessment  
**Track:** Cybersecurity  
**Task:** 16 – Risk Register and Compliance Mapping  
**Status:** Learning exercise – documented; review and validation pending

## 1. Objective

The objective was to consolidate security findings into a scored risk register, assign proposed treatments and owners, and map security controls to privacy principles and ISO/IEC 27001 themes.

## 2. Risk Register

The completed workbook contains 17 identified risks.

Each risk is assessed using:

**Risk Score = Likelihood × Impact**

Both likelihood and impact are rated from 1 to 5.

| Score | Rating |
|---|---|
| 1–4 | Low |
| 5–9 | Medium |
| 10–14 | High |
| 15–25 | Critical |

The register records the affected asset or process, risk description, evidence, recommended action, treatment, proposed owner, due date and status.

## 3. Top Five Risks

| Risk ID | Risk | Likelihood | Impact | Score | Rating |
|---|---|---:|---:|---:|---|
| R-01 | Full payroll export risk | 4 | 5 | 20 | Critical |
| R-02 | Insider salary disclosure | 4 | 5 | 20 | Critical |
| R-06 | Repeated failed logins / brute-force indicators | 4 | 4 | 16 | Critical |
| R-14 | Unremediated dependency advisories | 4 | 4 | 16 | Critical |
| R-03 | Incomplete ownership checks | 3 | 5 | 15 | Critical |

These are assessment priorities, not proof that a breach or successful attack occurred.

### Prioritisation and tie-break method

Where risks have the same score, prioritisation considers:

1. Sensitivity and potential impact on personal or confidential data.
2. Number of affected users and systems.
3. Exposure and accessibility.
4. Exploitability and existing safeguards.
5. Detection capability and time exposed.

R-03 is prioritised among risks scoring 15 because incomplete ownership checks could expose another user's records if the weakness is confirmed.

## 4. Risk Treatment and Ownership

The workbook assigns a proposed treatment, role-based owner and due date to each risk.

Treatments include mitigation, acceptance, transfer or avoidance, as appropriate.

Owners and due dates are proposed for this learning exercise. They must be reviewed and agreed by the responsible organisation before being treated as approved assignments.

## 5. Compliance Mapping

The Compliance Map sheet contains 14 controls mapped to relevant privacy principles and ISO/IEC 27001 themes.

The controls cover:

- Role-based access control and least privilege.
- Payroll export approval.
- Audit logging and tamper-evident records.
- Restricted independent log storage.
- Secure code review.
- Dependency vulnerability management.
- Secret detection.
- Input validation and output encoding.
- Authentication monitoring.
- Payroll audit metadata.
- Incident response.
- Data minimisation and retention.
- Ransomware detection and recovery readiness.

These mappings are indicative learning references. They do not establish legal compliance or ISO certification.

## 6. Evidence

The following evidence is included:

- `risk_register_completed.xlsx` – completed risk register, scoring guide, compliance map and top-five summary.
- `Task_16_Evidence/Task_16_Risk_Register.png` – risk register screenshot.
- `Task_16_Evidence/Task_16_Compliance_Map.png` – compliance mapping screenshot.

## 7. Reference Resources

- OWASP Cheat Sheet Series: https://github.com/OWASP/CheatSheetSeries
- OpenSSF Scorecard: https://github.com/ossf/scorecard

These resources support secure development and software supply-chain security learning.

## 8. Limitations and Review

This is a cybersecurity learning exercise based on the available project findings and synthetic assessment data.

Risk ratings are estimates and may change when additional evidence becomes available, controls are tested, dependencies are remediated, or the system's exposure changes.

The compliance mapping is not legal advice, a formal legal assessment, proof of compliance with the DPDP Act or GDPR, or evidence of ISO/IEC 27001 certification. Qualified legal and security professionals should review any real-world implementation.

## 9. Conclusion

Task 16 consolidates 17 security risks, applies a consistent likelihood-impact scoring method, identifies five priority risks, and maps 14 controls to relevant privacy and information-security themes.

The workbook and supporting screenshots provide a documented basis for further review, remediation and validation.

**Overall status:** Documentation prepared; organisational review and validation remain pending.
