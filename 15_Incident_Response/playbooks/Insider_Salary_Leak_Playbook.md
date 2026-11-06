# Incident Playbook: Insider Salary Leak (AS-15)
**Severity:** High (Critical if large-scale disclosure is confirmed)
**Trigger:** PAY-01 Night Salary Access or PAY-03 Salary Change Approval Review from Task 14, or a report of unauthorized salary information disclosure.
**Owner:** Security Incident Response Lead
**Backup owner:** HR Security Representative / IT Security Lead

## 1. Detect and confirm (what evidence?)
- Record the alert ID, timestamp and reporting source.
- Identify the account, affected salary records and relevant system.
- Review payroll audit logs and authentication events.
- Check whether access was consistent with the employee's approved responsibilities.
- Review available export, download and salary modification records.
- Verify the activity with authorized HR and Payroll representatives.
- Do not assume an employee is responsible based on an alert alone.

## 2. Contain (the first 30 minutes)
1. **0–5 minutes:** SOC analyst records the alert and preserves available evidence.
2. **5–10 minutes:** Notify the Incident Response Lead and IT Security Lead.
3. **10–15 minutes:** Involve the HR representative and Privacy Officer through confidential channels.
4. **15–20 minutes:** Assess the scope of salary information accessed or potentially disclosed.
5. **20–25 minutes:** With proper authorization, restrict unnecessary access or pause suspicious export activity.
6. **25–30 minutes:** Confirm containment, document decisions and limit incident information to authorized personnel.

## 3. Eradicate
- Remove unauthorized permissions after investigation and approval.
- Correct excessive access privileges.
- Reset credentials if account compromise is suspected.
- Review payroll export and approval controls.
- Address any confirmed process or configuration weakness.
- Do not confront or accuse a suspected employee without HR and Legal guidance.

## 4. Recover
- Restore appropriate payroll access based on verified job responsibilities.
- Confirm salary records have not been improperly modified.
- Validate access permissions with HR and Payroll.
- Monitor relevant access and export activity.
- Confirm that business operations can safely continue.

## 5. Communicate (who is told, when, by whom?)
- Immediately: SOC analyst informs the Incident Response Lead.
- Within 10 minutes: Incident Response Lead informs the IT Security Lead.
- Within 20 minutes: HR representative and Privacy Officer are informed confidentially.
- Within 30 minutes: Legal Counsel and relevant management are informed according to the incident scope.
- Share only necessary information with authorized stakeholders.
- **Employee/customer notification:** Privacy Officer or designated Data Protection Officer, together with Legal Counsel and HR, decides whether notification is required and approves the content and timing.
- Regulatory notifications must follow applicable legal and contractual requirements.
- Do not disclose the identity of a suspected insider unnecessarily.
- SOC analysts must not independently contact affected employees or external parties.

## 6. Learn
- Conduct a post-incident review within 5 days.
- Identify how unauthorized access or disclosure occurred.
- Review payroll access permissions and separation of duties.
- Improve monitoring of salary views, changes and exports.
- Review employee access procedures and awareness training.
- Assign corrective actions, owners and completion dates.

## Evidence to preserve
- Original PAY-01 and PAY-03 alerts.
- Payroll audit records and relevant authentication logs.
- Account identifiers and timestamps.
- Salary record identifiers, without unnecessary copies of sensitive salary values.
- Available export and access records.
- Approved access permissions and relevant authorization records.
- Incident timeline, decisions and evidence collection history.
- Confidential HR, Legal and Privacy communications.

## Decision points
- If unusual salary access is detected, then validate the business reason and approved access.
- If access exceeds job responsibilities, then involve HR, Privacy and the Incident Response Lead.
- If unauthorized disclosure is confirmed, then assess affected records and notification obligations.
- If an account is suspected to be compromised, then follow the approved account restriction and credential reset process.
- If evidence is insufficient, then preserve available records and continue the investigation without making unsupported accusations.
- If activity is authorized, document the validation and close the alert appropriately.

## Tabletop questions (5 hard ones to ask the team)
1. What would you do if an employee accessed salary records outside their job responsibilities?
2. How would you protect employee privacy while investigating the incident?
3. Who can authorize temporary restriction of payroll access?
4. How would you respond if salary information had already been shared outside the organization?
5. How would you investigate fairly without making an unsupported accusation against an employee?

## 7. Proposed operational improvements for validation
- The Incident Response Lead coordinates the investigation and containment decisions.
- HR, Legal Counsel and the Privacy Officer coordinate a fair and confidential investigation.
- Authorized IT Security personnel carry out account restrictions only after the required approval.
- Preserve payroll audit logs, authentication records, access records and relevant communications according to the evidence retention policy.
- The SOC Analyst maintains a timestamped evidence register containing evidence ID, source, collection time, owner and handling history.
- The Privacy Officer and Legal Counsel assess employee or regulatory notification obligations with management.
- The Payroll System Owner verifies salary access and export activity against official authorization records.
