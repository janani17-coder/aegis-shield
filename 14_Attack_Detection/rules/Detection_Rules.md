@'
# Aegis Shield - Task 14: Advanced Attack Detection Rules

## 1. Authentication Monitoring

### AUTH-01: Account Brute Force
- Severity: High
- Threshold: 5 or more failed logins for one account within 10 minutes.
- Purpose: Identify repeated authentication failures against one account.
- First check: Review account owner, source IPs, timestamps and subsequent successful logins.
- False-positive handling: Confirm legitimate password issues, account recovery or user activity before escalation.

### AUTH-02: Password Spraying
- Severity: High
- Threshold: 5 or more distinct accounts receiving failed logins from one IP within 10 minutes.
- Purpose: Identify possible password-spraying activity.
- First check: Review source IP, affected accounts, timestamps and subsequent successful logins.
- False-positive handling: Compare the source with approved corporate gateways and identity-provider logs.

### AUTH-03: Rapid Country Change
- Severity: High
- Threshold: Successful logins for one account from different countries within 30 minutes.
- Purpose: Identify suspicious geographic login changes.
- First check: Verify user travel, VPN usage, source IP reputation and authentication details.
- False-positive handling: Check VPN and proxy services before classifying the event as suspicious.

### AUTH-04: Admin Login at Odd Hours
- Severity: High
- Status: Active for the assessment.
- Detection method: Successful off-hours logins for the administrator account explicitly mapped in the assessment dataset.
- Purpose: Identify unexpected privileged account activity outside normal hours.
- First check: Verify administrator identity, approved schedule, source host, change record and authentication evidence.
- Limitation: The authentication CSV has no administrator role field. The current implementation uses an assessment-specific account mapping, not general administrator-role discovery.
- Production requirement: Integrate an authoritative administrator roster or identity-provider role source.

## 2. Payroll Monitoring

### PAY-01: Night-Time Salary Access
- Severity: High
- Threshold: 10 or more distinct employee salary records viewed by one actor within one hour during the configured 22:00-05:59 window.
- Purpose: Identify unusually large salary-data access outside normal hours.
- First check: Confirm actor's job responsibility, access approval, affected records and business reason.
- False-positive handling: Check approved payroll processing and reporting schedules.
- Limitation: Confirm the source timezone before applying this rule in production.

### PAY-02: Full Payroll Export
- Severity: High
- Threshold: Any full payroll export event.
- Purpose: Identify bulk extraction of sensitive payroll information.
- First check: Verify requester, authorization, export destination and business purpose.
- False-positive handling: Confirm approved payroll-cycle exports while retaining an audit trail.

### PAY-03: Salary Change Approval Review
- Severity: Medium
- Threshold: Any salary update event.
- Purpose: Identify salary changes requiring approval verification.
- First check: Check the approved salary-change request, manager authorization and audit history.
- Limitation: The supplied payroll CSV does not contain an independent approval reference or second-person approval record. The planted assessment event contains the result value `OK_NO_APPROVAL`, which is a review indicator but does not replace independent workflow verification.
- False-positive handling: Match the event with an independently maintained approval record.

## 3. Web Request Monitoring

### WEB-01: Suspicious Web Request Indicators
- Severity: High
- Indicators:
  - SQL injection-like request patterns.
  - Script injection-like request patterns.
  - Path traversal indicators.
  - Recognized scanning-tool indicators.
- Purpose: Identify suspicious web requests for investigation.
- First check: Review source IP, timestamp, request path, user-agent, response status and application logs.
- False-positive handling: Validate the request against authorized testing, monitoring and normal application behavior.
- Important: An indicator is not proof that an application was successfully exploited.
- Overlap note: A request containing a recognized scanning-tool user-agent may generate both a scanning indicator and another web indicator.

### WEB-02: Web Login Brute Force
- Severity: High
- Threshold: 50 or more failed POST requests to the login endpoint from one IP within 10 minutes.
- Purpose: Identify repeated failed web authentication attempts.
- First check: Review source IP, affected accounts, application logs, timestamps and authentication outcomes.
- False-positive handling: Check legitimate client retries, application errors and approved testing activity.
- Tuning note: The threshold is based on the supplied assessment data and must be validated against normal application traffic before production use.

## 4. Threshold Tuning and Exceptions

- Review alert frequency against a normal activity baseline.
- Avoid treating every failed login as an attack.
- Retain high-priority alerts for repeated failures, rapid country changes and full payroll exports.
- Reassess thresholds when normal activity changes.
- Record threshold changes and their justification.
- Correlate alerts with identity-provider, application and audit records where available.

### Friday 02:00 Administrator Backup Exception

A legitimate administrator may perform scheduled backups every Friday at 02:00.

Do not suppress all administrator logins outside business hours.

Use a narrowly scoped exception requiring:
- A verified administrator or service identity.
- An approved backup schedule and change record.
- An expected source host or IP.
- A matching backup job identifier.
- Successful completion of the expected backup task.

Continue alerting if the source changes, the job is missing or fails, or unrelated privileged activity occurs.

## 5. Data Limitations

- Authentication data has no administrator role field. AUTH-04 currently uses an assessment-specific account mapping.
- Authentication data has no dedicated MFA field. MFA status requires independent verification.
- Payroll data has no independent approval-reference field.
- Payroll data has no source IP field.
- Authentication and payroll timestamps do not contain timezone offsets. Confirm timezone interpretation before production correlation.
- Geographic login changes and suspicious web request indicators require investigation.
- Scanning indicators can overlap with other web indicators when the same request contains a recognized scanning-tool user-agent.
- Detection thresholds require validation against normal activity before production deployment.

## 6. Detection Summary

| Rule | Detection |
|---|---|
| AUTH-01 | Account brute force |
| AUTH-02 | Password spraying |
| AUTH-03 | Rapid country change |
| AUTH-04 | Assessment-mapped administrator off-hours login |
| PAY-01 | Night salary access |
| PAY-02 | Full payroll export |
| PAY-03 | Salary change approval review |
| WEB-01 | SQL injection, script injection, path traversal and scanning indicators |
| WEB-02 | Web login brute force |

## 7. Assessment Results

The current detection run generated 21 alert rows across the nine detection rules.

Alert rows are not equivalent to unique attack scenarios. Multiple alerts can represent different time windows or overlapping indicators for the same scenario.

The planted-scenario validation is documented separately in:
`reports/Task_14_Attack_Detection_Report.md`
'@ | Set-Content -Path "14_Attack_Detection\rules\Detection_Rules.md" -Encoding utf8