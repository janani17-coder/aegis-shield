# Individual Tabletop Walkthrough - Payroll Data Breach



**Project:** Aegis Shield Cybersecurity Assessment

**Playbook:** AS-15 - Payroll Data Breach

**Exercise Type:** Individual tabletop self-review

**Date:** 20 November 2026

**Participant:** Individual project reviewer

**Status:** Completed - Individual walkthrough only



## 1\. Objective



Review the Payroll Data Breach incident-response playbook and evaluate the decisions required during a simulated payroll security incident.



This walkthrough is a document-based self-review. It is not a live incident, production test or independently facilitated team exercise.



## 2\. Scenario



A PAY-02 Full Payroll Export alert is generated outside normal business hours. The alert indicates unusual payroll export activity. Authorization and the extent of any data exposure have not yet been confirmed.



No real employee or payroll information is involved.



## 3\. Decision Scenarios and Responses



### Scenario 1 - Full payroll export outside business hours



**Question:** What should happen when the alert appears?



**Response:** Record the alert ID, timestamp, account and affected system. Notify the Incident Response Lead and Payroll System Owner. Investigate the activity before deciding whether a breach occurred.



**Expected evidence:** Original alert, authentication logs and payroll audit records.



### Scenario 2 - Determining whether the export was authorized



**Question:** How can the team verify authorization?



**Response:** Compare the export activity with official payroll approval records, assigned permissions and the approved business purpose. Do not rely only on the alert or the account owner's explanation.



**Expected evidence:** Approval record, access permissions and export activity record.



### Scenario 3 - Restricting suspicious account access



**Question:** Who can authorize access restrictions?



**Response:** The Incident Response Lead coordinates the response. The authorized Payroll System Owner approves the appropriate restriction, and authorized IT Security personnel carry it out according to the organization's process.



**Expected evidence:** Approval record, decision timestamp and action history.



### Scenario 4 - Employee or regulatory notification



**Question:** Who decides whether notification is required?



**Response:** The Privacy Officer or designated Data Protection Officer works with Legal Counsel and management to assess applicable notification obligations. SOC analysts must not independently notify employees or regulators.



**Expected evidence:** Impact assessment, decision record and approved communication.



### Scenario 5 - Incomplete payroll audit logs



**Question:** What should happen if audit logs are incomplete?



**Response:** Record the evidence gap, preserve available logs, identify alternative authorized evidence sources and escalate the limitation to the Incident Response Lead. Do not claim that the incident scope is fully known.



**Expected evidence:** Available log records, evidence register and documented investigation limitations.



## 4\. Response Lifecycle Review



| Phase | Review outcome |

|---|---|

| Detect and confirm | Alert validation and authorization checks reviewed |

| Contain | Approval-based access restriction process reviewed |

| Eradicate | Credential and permission review requirements identified |

| Recover | Payroll verification and monitoring requirements reviewed |

| Communicate | Internal escalation and notification responsibilities reviewed |

| Learn | Post-incident review and corrective actions identified |



## 5\. Observations



1\. Alert generation alone does not confirm a data breach.

2\. Payroll export authorization must be verified using official records.

3\. Access restrictions require authorized approval.

4\. Privacy and Legal teams must assess notification requirements.

5\. Incomplete logs can prevent accurate incident-scope determination.

6\. Evidence must be preserved with collection and handling history.



## 6\. Improvement Actions



| Improvement | Suggested responsible role | Status |

|---|---|---|

| Verify payroll export approval controls | Payroll System Owner | Pending |

| Review audit-log integrity and retention | IT Security Lead | Pending |

| Verify incident escalation contacts | Incident Response Lead | Pending |

| Review notification procedures | Privacy Officer / Legal | Pending |

| Conduct an independently facilitated team exercise | Incident Response Lead | Pending |



## 7\. Limitations



\- Individual document-based walkthrough only.

\- No additional participant or independent facilitator.

\- No production system or real payroll data accessed.

\- No live incident-response actions performed.

\- No production control effectiveness demonstrated.

\- No formal team exercise approval obtained.



## 8\. Conclusion



The individual walkthrough reviewed five decision scenarios and the six stages of the Payroll Data Breach incident-response process.



The review identified useful evidence requirements, approval responsibilities and improvement actions.



**This record does not replace the pending human tabletop exercise.** Independent participation, production validation and formal approval remain outstanding.



**Final status:** Individual walkthrough completed; formal team tabletop exercise pending.

