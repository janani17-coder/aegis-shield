
# Aegis Shield – Task 14: Attack Detection Rules

## 1. Authentication Monitoring

### AUTH-01: Account Brute Force
- Severity: High
- Threshold: 5 or more failed logins for one account within 10 minutes.
- Purpose: Identify repeated authentication failures against one account.
- First check: Check account owner, source IPs, successful logins and MFA.
- False-positive handling: Confirm whether the user had a legitimate password or account issue before escalation.

### AUTH-02: Password Spraying
- Severity: High
- Threshold: 5 or more distinct accounts receiving failed logins from one IP within 10 minutes.
- Purpose: Identify a possible password-spraying pattern.
- First check: Review source IP, affected accounts, timestamps and any subsequent successful logins.
- False-positive handling: Compare the source with approved corporate gateways and identity-provider logs.

### AUTH-03: Rapid Country Change
- Severity: High
- Threshold: Successful logins for one account from different countries within 30 minutes.
- Purpose: Identify suspicious geographic login changes.
- First check: Verify user travel, VPN usage, source IP reputation and authentication details.
- False-positive handling: Check VPN and proxy services before classifying the event as suspicious.

### AUTH-04: Admin Login at Odd Hours
- Severity: High
- Status: Not active.
- Reason: Authentication data does not contain a role or administrator field.
- Required data: Verified administrator roster, source IP and login timestamps.
- First check: Confirm administrator identity, approved maintenance window and change ticket.

## 2. Payroll Monitoring

### PAY-01: Night-Time Salary Access
- Severity: High
- Threshold: 10 or more distinct employee salary records viewed by one actor within one hour during 22:00–05:59.
- Purpose: Identify unusually large salary-data access outside normal hours.
- First check: Confirm actor's job responsibility, access approval, affected records and business reason.
- False-positive handling: Check approved payroll processing and reporting schedules.

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
- Limitation: The supplied payroll data has no approval-reference field. Therefore, missing approval cannot be conclusively established.
- False-positive handling: Match the event with an independently maintained approval record.

## 3. Web Request Monitoring

### WEB-01: Suspicious Web Request Indicators
- Severity: High
- Indicators:
  - SQL injection-like request patterns.
  - Script injection-like request patterns.
  - Path traversal indicators.
  - Recognized scanning-tool indicators.
- Purpose: Identify suspicious requests for investigation.
- First check: Review source IP, timestamp, request path, user-agent, response status and application logs.
- False-positive handling: Validate the request against legitimate testing, monitoring and application behavior.
- Important: An indicator is not proof that an application was successfully exploited.

## 4. Threshold Tuning and Exceptions

- Review alert frequency against the normal event baseline.
- Avoid treating every failed login as an attack.
- Retain high-confidence alerts for repeated failures, rapid country changes and full payroll exports.
- Reassess thresholds when normal activity changes.
- Record all threshold changes and their justification.

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

- Authentication data has no administrator role field.
- Payroll data has no approval-reference field.
- Payroll data has no source IP field.
- Geographic login changes require investigation and do not independently prove account compromise.
- Detection thresholds require validation against the supplied baseline and planted test cases.

## 6. Detection Summary

| Rule | Detection |
|---|---|
| AUTH-01 | Account brute force |
| AUTH-02 | Password spraying |
| AUTH-03 | Rapid country change |
| AUTH-04 | Admin odd-hours login – inactive |
| PAY-01 | Night salary access |
| PAY-02 | Full payroll export |
| PAY-03 | Salary approval review |
| WEB-01 | Suspicious web request indicators |
