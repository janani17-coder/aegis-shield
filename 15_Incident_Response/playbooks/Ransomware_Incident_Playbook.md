# Incident Playbook: Ransomware Incident (AS-15)
**Severity:** Critical
**Trigger:** Suspected ransomware report from an employee or IT team, endpoint security alert, unusual file-access activity, or related suspicious AUTH-01 / WEB-01 alerts from Task 14. These Task 14 alerts are contextual indicators, not ransomware-specific detections.
**Owner:** Security Incident Response Lead
**Backup owner:** IT Security Lead

## 1. Detect and confirm (what evidence?)
- Record the first report, alert ID, timestamp and affected device.
- Contact the affected user and IT support through approved channels.
- Review available endpoint security alerts, authentication logs and network monitoring records.
- Check whether multiple devices or shared systems are affected.
- Treat unusual file activity as a warning signal until verified.
- Task 14 currently has no dedicated ransomware or endpoint encryption detection rule. Record this as a detection gap.

## 2. Contain (the first 30 minutes)
1. **0–5 minutes:** Record the report, affected device names, timestamps and available alerts.
2. **5–10 minutes:** Notify the Incident Response Lead and IT Security Lead.
3. **10–15 minutes:** Assess whether other devices or business systems may be affected.
4. **15–20 minutes:** Authorized IT personnel isolate confirmed affected devices using the organization's approved incident procedure.
5. **20–25 minutes:** Notify system owners and relevant business teams. Protect unaffected systems and backup infrastructure.
6. **25–30 minutes:** Record containment actions, affected services and decisions. Preserve evidence before any cleanup.

## 3. Eradicate
- Have qualified incident responders identify the cause and scope.
- Remove unauthorized access and address the confirmed security weakness.
- Reset credentials where compromise is suspected, following approved procedures.
- Rebuild affected systems from trusted installation sources when authorized.
- Do not delete evidence or attempt unapproved cleanup.
- Validate systems before reconnecting them to the business network.

## 4. Recover
- Verify backup integrity and safety before restoration.
- Restore priority systems using approved clean backups.
- Confirm business applications and data are functioning correctly.
- Obtain system-owner and Incident Response Lead approval before returning systems to service.
- Increase monitoring for unusual authentication and file activity.
- Keep affected systems under observation after recovery.

## 5. Communicate (who is told, when, by whom?)
- Immediately: Reporter informs IT support or SOC.
- Within 10 minutes: SOC informs the Incident Response Lead and IT Security Lead.
- Within 20 minutes: Incident Response Lead informs affected system owners and relevant management.
- Within 30 minutes: Business continuity, Legal and Privacy teams are informed if business operations or personal data may be affected.
- Employees receive verified instructions through approved internal communication channels.
- **Customer notification:** Privacy Officer or designated Data Protection Officer, together with Legal Counsel and management, decides whether customer notification is required and approves its timing and content.
- Regulatory reporting follows applicable legal and contractual deadlines.
- SOC analysts must not independently make external notification decisions.

## 6. Learn
- Conduct a post-incident review within 5 days.
- Document the initial access path, affected systems and business impact.
- Review backup readiness and recovery performance.
- Identify gaps in endpoint monitoring and incident escalation.
- Propose endpoint alerts for unusual mass file changes and encryption-related activity.
- Assign corrective-action owners and deadlines.

## Evidence to preserve
- Original endpoint security alerts and incident reports.
- Authentication and relevant network logs.
- Affected device names, timestamps and system identifiers.
- Available file-access and backup activity records.
- Incident timeline and containment approvals.
- Relevant system and security monitoring records.
- Evidence collection history and approved responder notes.

## Decision points
- If ransomware is suspected, then activate the incident response process immediately.
- If multiple systems may be affected, then escalate severity and involve the IT Security Lead.
- If an endpoint is confirmed affected, then authorized IT personnel follow the approved isolation procedure.
- If backup safety cannot be verified, then do not approve restoration from that backup.
- If personal or customer information may be affected, then involve Privacy and Legal teams.
- If ransomware is not confirmed, document the investigation and continue monitoring as appropriate.

## Tabletop questions (5 hard ones to ask the team)
1. What would you do if several employees reported that their files were unavailable at the same time?
2. Who has authority to isolate affected business systems?
3. How would you decide which business services should be restored first?
4. What would you do if the available backups could not be verified as safe?
5. How would you communicate with employees and customers while the investigation is ongoing?

## 7. Proposed operational improvements for validation
- The Incident Response Lead coordinates incident decisions and communication.
- Authorized IT Security personnel approve and carry out endpoint isolation under the organization's incident response procedure.
- Preserve endpoint, authentication, network and backup-related logs according to the evidence retention policy.
- The SOC Analyst maintains a timestamped evidence register containing evidence ID, source, collection time, owner and handling history.
- The Privacy Officer and Legal Counsel assess external notification obligations with management.
- The organization should evaluate dedicated endpoint detection coverage for ransomware-related activity because Task 14 does not contain a ransomware-specific detection rule.
