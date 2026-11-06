@'
# Aegis Shield - Task 14: Advanced Attack Detection Report

## 1. Objective

The objective of Task 14 was to analyze authentication, payroll audit and web access logs, identify suspicious activity, implement detection rules, generate alerts and visualize the results in a monitoring dashboard.

## 2. Tools and Technologies

- Python 3.11
- Pandas
- Matplotlib
- PowerShell
- Visual Studio Code

## 3. Log Sources

Three log sources were analyzed.

| Log Source | Events Processed |
|---|---:|
| Authentication events | 11,487 |
| Payroll audit events | 2,652 |
| Web access requests parsed | 5,805 |
| **Total** | **19,944** |

Input files:
- `data/auth_events.csv`
- `data/payroll_audit_events.csv`
- `data/web_access.log`

## 4. Final Detection Results

The final detection script generated 21 alerts.

| Detection Rule | Severity | Alerts |
|---|---|---:|
| AUTH-01 Account brute force | High | 3 |
| AUTH-02 Password spraying | High | 2 |
| AUTH-03 Rapid country change | High | 1 |
| AUTH-04 Admin off-hours login | High | 4 |
| PAY-01 Night salary access | High | 1 |
| PAY-02 Full payroll export | High | 1 |
| PAY-03 Salary change approval review | Medium | 1 |
| WEB-01 Path traversal indicator | High | 1 |
| WEB-01 SQL injection indicator | High | 2 |
| WEB-01 Scanning indicator | High | 3 |
| WEB-01 Script injection indicator | High | 1 |
| WEB-02 Web login brute force | High | 1 |
| **Total** | | **21** |

Alert counts are not equivalent to unique attack scenarios. Some scenarios generate multiple alerts, and different indicators can identify the same request.

## 5. Detection Logic and Thresholds

### Authentication

- AUTH-01: Five or more failed logins for one account within 10 minutes.
- AUTH-02: Five or more distinct accounts receiving failed logins from one IP within 10 minutes.
- AUTH-03: Successful logins from different countries for one account within 30 minutes.
- AUTH-04: Successful off-hours login for the administrator account explicitly mapped for this assessment. Production deployment requires an authoritative administrator-role source.

### Payroll

- PAY-01: Ten or more distinct employee salary records viewed by one actor within one hour during 22:00-05:59.
- PAY-02: Any full payroll export event.
- PAY-03: Any salary update generates an approval review because approval workflow evidence is not independently available in the source CSV.

### Web

- WEB-01: Identifies request patterns associated with SQL injection, script injection, path traversal and recognized scanning tools.
- WEB-02: Fifty or more failed POST requests to the login endpoint from one IP within 10 minutes.

These indicators identify suspicious activity and do not independently prove successful exploitation.

## 6. Planted-Item Validation

The supplied assessment reference file `unlock_AS-14_planted_attacks_in_logs.csv` was located and compared with the detection results.

| No. | Planted Scenario | Detection Rule | Validation |
|---:|---|---|---|
| 1 | Account brute force | AUTH-01 | Detected |
| 2 | Password spraying | AUTH-02 | Detected |
| 3 | Impossible travel | AUTH-03 | Detected |
| 4 | Off-hours administrator login | AUTH-04 | Detected |
| 5 | Insider salary snooping | PAY-01 | Detected |
| 6 | Full payroll export | PAY-02 | Detected |
| 7 | Salary change without approval | PAY-03 | Detected |
| 8 | SQL injection event 1 | WEB-01 | Detected |
| 9 | SQL injection event 2 | WEB-01 | Detected |
| 10 | Cross-site scripting indicator | WEB-01 | Detected |
| 11 | Path traversal | WEB-01 | Detected |
| 12 | Web scanning | WEB-01 | Detected |
| 13 | Web login brute force | WEB-02 | Detected |

**Validation result: 13 of 13 planted scenarios have corresponding detection evidence.**

### Important validation observations

- AUTH-01 generated three alert windows for the 420 failed login attempts.
- AUTH-02 generated two alert windows covering 60 distinct targeted accounts.
- AUTH-04 generated four alerts for four successful off-hours administrator logins.
- PAY-01 identified 150 distinct salary records viewed by one actor.
- PAY-03 source data explicitly contains the result `OK_NO_APPROVAL`. Independent approval-workflow records are unavailable.
- WEB-01 generated scanning indicators for the two SQL injection requests because their user-agent contained `sqlmap`. These are overlapping indicators, not additional planted scenarios.
- WEB-02 identified 300 failed POST login requests in 10 minutes.

## 7. Alert Tuning and False-Positive Handling

Detection thresholds were configured to identify repeated and potentially suspicious behavior rather than treating every event as malicious.

Recommended investigation steps:

- Verify account ownership and legitimate authentication failures.
- Review VPN, proxy and travel activity before classifying geographic changes.
- Validate payroll access against job responsibilities and approved schedules.
- Confirm full exports against authorized business requests.
- Review web requests alongside application and server logs.
- Validate thresholds against normal traffic before production deployment.

### Scheduled Administrator Backup Exception

A legitimate administrator may perform backups every Friday at 02:00.

Do not disable all off-hours administrator alerts.

A narrow exception should require a verified administrator or service identity, approved schedule, expected source host, change record and matching backup job identifier.

Unexpected sources, failed or missing backup jobs, and unrelated privileged activity must remain reviewable.

## 8. Dashboard

The detection dashboard was generated using Matplotlib.

Evidence:
`evidence/Task_14_Detection_Dashboard.png`

The dashboard displays:

1. Alerts by severity.
2. Alerts by detection rule.
3. Alert activity over event timestamps.

The dashboard must be regenerated using the final 21-alert output before submission.

## 9. Generated Reports

- `reports/detection_alerts.csv`
- `reports/detection_summary.csv`
- `reports/Task_14_Attack_Detection_Report.md`
- `evidence/Task_14_Detection_Dashboard.png`

## 10. Data Limitations

1. The authentication dataset has no administrator role field. AUTH-04 therefore uses an assessment-specific account mapping, not general role discovery.
2. Authentication data does not provide a dedicated MFA field. MFA status requires independent verification.
3. Payroll data does not contain an approval reference or independent second-person approval record.
4. Payroll data does not contain source IP information.
5. Geographic changes and web request indicators require additional investigation.
6. Authentication and payroll source timestamps do not contain timezone offsets. Their timestamp interpretation should be confirmed before production correlation.
7. Scanning indicators can overlap with SQL injection indicators when the same request contains a recognized scanning-tool user-agent.

## 11. Conclusion

A Python-based log detection and monitoring workflow was implemented successfully.

The system processed 19,944 events across three log sources and generated 21 alerts covering authentication, payroll and suspicious web activity.

All 13 planted assessment scenarios have corresponding detection evidence. The project also includes detection rules, CSV alert reports, a monitoring dashboard and documented investigation recommendations.

The solution demonstrates a defensive security monitoring workflow. Production deployment would require authoritative identity and approval data, timezone normalization, baseline tuning and further false-positive testing.
'@ | Set-Content -Path "14_Attack_Detection\reports\Task_14_Attack_Detection_Report.md" -Encoding utf8