# Incident Playbook: Payroll Data Breach (AS-15)
**Severity:** Critical
**Trigger:** PAY-02 Full Payroll Export or PAY-03 Salary Change Approval Review from Task 14.
**Owner:** Security Incident Response Lead
**Backup owner:** SOC Analyst / IT Security Lead

## 1. Detect and confirm (what evidence?)
- Review the PAY-02 or PAY-03 alert and its timestamp.
- Identify the account, affected payroll records, event type and affected system.
- Check whether the activity was authorized using approved payroll records and access permissions.
- Determine whether payroll information was viewed, changed, exported or disclosed.
- Do not assume that an alert alone proves a confirmed data breach.

## 2. Contain (the first 30 minutes)
1. **0–5 minutes:** SOC analyst records the alert ID, timestamp and initial evidence.
2. **5–10 minutes:** Notify the Incident Response Lead and Payroll System Owner.
3. **10–15 minutes:** Incident Response Lead assesses the scope and severity.
4. **15–20 minutes:** With approval from the authorized system owner, restrict suspicious account access and pause affected export activity where appropriate.
5. **20–25 minutes:** Notify the Privacy Officer, Legal Team and HR representative.
6. **25–30 minutes:** Confirm containment actions, affected systems and outstanding risks. Maintain a timeline of decisions.

## 3. Eradicate
- Remove unauthorized access after investigation and approval.
- Reset affected credentials where compromise is suspected.
- Correct inappropriate permissions and access-control weaknesses.
- Review relevant application and server security configurations.
- Preserve original evidence before making changes.

## 4. Recover
- Restore normal payroll operations only after the Incident Response Lead and Payroll System Owner approve.
- Verify payroll records and salary changes against authorized records.
- Confirm access permissions and security monitoring are functioning.
- Monitor affected accounts and payroll activity for suspicious behavior.

## 5. Communicate (who is told, when, by whom?)
- Immediately: SOC Analyst informs the Incident Response Lead.
- Within the first 15 minutes: Incident Response Lead informs the IT Security Lead and Payroll System Owner.
- Within 30 minutes: Privacy Officer, Legal Team and HR are informed.
- Management receives a verified impact summary through the Incident Response Lead.
- **Customer/employee notification:** The authorized Privacy Officer or designated Data Protection Officer, with Legal Counsel and management, decides whether notification is required and approves its content and timing.
- Regulatory notifications must follow applicable legal and contractual deadlines.
- SOC analysts must not independently notify customers, employees or regulators.

## 6. Learn
- Conduct a post-incident review within 5 days.
- Identify the cause, affected records, response delays and control weaknesses.
- Review payroll export permissions and approval procedures.
- Improve detection rules and access monitoring.
- Assign owners and deadlines for corrective actions.

## Evidence to preserve
- Original PAY-02 and PAY-03 alert records.
- Relevant payroll audit logs and authentication logs.
- Account IDs, timestamps and affected record identifiers.
- Export activity records and available access-control records.
- Incident timeline, decisions and approval records.
- Evidence collection and access history.
- Secure copies of relevant communications.

## Decision points
- If a full payroll export is detected, then investigate authorization and scope immediately.
- If unauthorized access is confirmed, then restrict the affected account through the approved process.
- If salary changes lack verified approval, then involve Payroll, HR and Legal.
- If personal data exposure is confirmed or suspected, then the Privacy Officer and Legal Counsel assess notification obligations.
- If the alert is legitimate, document the validation and close it through the approved process.

## Tabletop questions (5 hard ones to ask the team)
1. What would you do if a full payroll export alert appeared outside business hours?
2. How would you determine whether the export was authorized?
3. Who has authority to restrict payroll access?
4. Who decides whether affected employees or regulators must be notified?
5. What would you do if the payroll audit logs were incomplete?

## 7. Additional operational improvements
- The Incident Response Lead coordinates containment decisions.
- Authorized IT Security personnel execute approved account restrictions.
- The Payroll System Owner verifies export requests against official approval records.
- Payroll audit logs must be retained and protected according to the organization's retention policy.
- The Privacy Officer and Legal Counsel assess external notification obligations.
- The SOC Analyst maintains a timestamped evidence register containing evidence ID, source, collection time, owner and handling history.
