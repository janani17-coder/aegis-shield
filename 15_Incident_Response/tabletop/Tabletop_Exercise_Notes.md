# Task 15: Tabletop Exercise Notes

## 1. Exercise Details

- **Exercise title:** Aegis Shield – Payroll Security Incident
- **Date:** 6 November 2026
- **Exercise type:** AI-assisted tabletop simulation
- **Facilitator:** Project Owner
- **Participant:** Simulated SOC Analyst (ChatGPT)
- **Scenario:** Suspected unauthorized payroll access and full payroll export
- **Severity:** Critical

## 2. Scenario Summary

At 11:30 PM, the security monitoring system generated a PAY-01 Night Salary Access alert.

Shortly afterwards, a PAY-02 Full Payroll Export alert appeared.

The Payroll System Owner had not confirmed whether the activity was authorized.

The SOC Analyst and Incident Response Lead discussed how to investigate, preserve evidence, contain suspicious access and communicate with relevant stakeholders.

## 3. Participant Responses

### Question 1
**What are your first three actions after receiving the alert?**

**Simulated SOC Analyst response:**

1. Review both alerts, timestamps, account details and affected payroll records.
2. Preserve relevant payroll audit logs and authentication records.
3. Notify the Incident Response Lead and Payroll System Owner immediately.

**Finding:** Initial investigation and escalation should happen promptly.

### Question 2
**How would you confirm whether the payroll export was authorized?**

**Simulated SOC Analyst response:**

- Check the employee's approved access permissions.
- Verify the export against an authorized payroll request.
- Contact the Payroll System Owner for confirmation.
- Compare the export event with relevant audit records.
- Record the verification result.

**Finding:** The playbook should clearly identify the authorization source and responsible approver.

### Question 3
**Who can approve restricting the suspicious account?**

**Simulated SOC Analyst response:**

The Incident Response Lead should coordinate the response. The authorized IT Security Lead or system owner should approve and carry out account restrictions according to organizational procedures.

**Finding:** Account restriction authority must be clearly defined.

### Question 4
**Who decides whether affected employees or regulators must be notified?**

**Simulated SOC Analyst response:**

The Privacy Officer or designated Data Protection Officer should assess notification requirements with Legal Counsel and management. Notifications must follow applicable legal and contractual deadlines.

**Finding:** External notification responsibilities must be established before an incident occurs.

### Question 5
**What would you do if the payroll audit logs were incomplete?**

**Simulated SOC Analyst response:**

- Preserve all available logs.
- Record missing evidence and affected time periods.
- Check other authorized sources, such as authentication and export records.
- Escalate the evidence gap to the Incident Response Lead.
- Avoid making unsupported conclusions.

**Finding:** The organization needs reliable log retention and centralized evidence collection.

## 4. Gaps Identified During Simulation

The following are simulated findings that require validation in a real tabletop discussion.

1. **Unclear approval authority:** The account restriction approval process needs clearly assigned roles.
2. **Incomplete audit evidence:** Missing or incomplete payroll logs could delay incident investigation.
3. **Notification uncertainty:** Employee and regulator notification responsibilities need a documented approval process.
4. **Authorization verification:** The playbook should identify the official source for verifying payroll export requests.
5. **Evidence ownership:** A designated person should maintain the incident timeline and evidence register.

## 5. Recommended Improvements

### Improvement 1: Define containment approval authority
- Related playbook: Payroll Data Breach
- Action: Document who approves and performs account restrictions.
- Owner: IT Security Lead
- Priority: High
- Status: Proposed

### Improvement 2: Improve payroll audit logging
- Related playbook: Payroll Data Breach / Insider Salary Leak
- Action: Define audit log retention, access and evidence collection responsibilities.
- Owner: Payroll System Owner
- Priority: High
- Status: Proposed

### Improvement 3: Create a notification approval matrix
- Related playbook: All three playbooks
- Action: Document the responsibilities of Privacy, Legal, HR and management for notification decisions.
- Owner: Privacy Officer
- Priority: High
- Status: Proposed

### Improvement 4: Document payroll export authorization
- Related playbook: Payroll Data Breach
- Action: Identify the official approval record and verification owner.
- Owner: Payroll System Owner
- Priority: Medium
- Status: Proposed

### Improvement 5: Introduce an evidence register
- Related playbook: All three playbooks
- Action: Maintain a timestamped record of evidence collection, ownership and handling.
- Owner: SOC Analyst
- Priority: Medium
- Status: Proposed

## 6. Exercise Conclusion

The simulation demonstrated the importance of:

- Early incident detection and escalation.
- Clear containment responsibilities.
- Preserving original evidence.
- Coordinating with HR, Privacy and Legal.
- Establishing notification approval procedures.
- Maintaining reliable audit logs.

The three playbooks provide an initial response framework. The proposed improvements should be reviewed and incorporated after validation.

## 7. Exercise Status

**Status: AI-assisted simulation completed. Real spoken tabletop exercise pending.**

This document records simulated responses and proposed improvements. It does not claim that a real friend or team participated.

A real tabletop discussion should validate the findings before the project is marked fully complete.
