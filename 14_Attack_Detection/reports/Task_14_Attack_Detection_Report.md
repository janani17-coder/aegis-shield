
# Aegis Shield – Task 14: Advanced Attack Detection Report

## 1. Objective

The objective of Task 14 was to analyze authentication, payroll audit and web access logs to identify suspicious activity, implement detection rules, generate alerts and visualize the results in a monitoring dashboard.

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
| Web access requests | 5,803 |
| **Total** | **19,942** |

Input files:
- `data/auth_events.csv`
- `data/payroll_audit_events.csv`
- `data/web_access.log`

## 4. Detection Results

The detection script generated 12 alerts.

| Detection Rule | Severity | Alerts |
|---|---|---:|
| AUTH-01 Account brute force | High | 3 |
| AUTH-02 Password spraying | High | 2 |
| AUTH-03 Rapid country change | High | 1 |
| PAY-01 Night salary access | High | 1 |
| PAY-02 Full payroll export | High | 1 |
| PAY-03 Salary change approval review | Medium | 1 |
| WEB-01 Path traversal indicator | High | 1 |
| WEB-01 Scanning indicator | High | 1 |
| WEB-01 Script injection indicator | High | 1 |
| **Total** | | **12** |

## 5. Detection Logic and Thresholds

### Authentication
- AUTH-01: Five or more failed logins for one account within 10 minutes.
- AUTH-02: Five or more distinct accounts receiving failed logins from one IP within 10 minutes.
- AUTH-03: Successful logins from different countries for one account within 30 minutes.
- AUTH-04: Not active because the supplied authentication data has no administrator role field.

### Payroll
- PAY-01: Ten or more distinct employee salary records viewed by one actor within one hour during 22:00–05:59.
- PAY-02: Any full payroll export event.
- PAY-03: Any salary update generates an approval review because the source data does not contain an approval reference.

### Web
- WEB-01: Identifies request patterns associated with path traversal, script injection, SQL injection-like activity and recognized scanning tools.

These indicators require investigation and do not independently prove successful exploitation.

## 6. Alert Tuning and False-Positive Handling

Detection thresholds were configured to identify repeated and potentially suspicious behavior rather than treating every event as malicious.

The following checks are recommended:
- Verify account ownership and legitimate authentication failures.
- Review VPN, proxy and travel activity before classifying geographic changes.
- Validate payroll access against job responsibilities and approved schedules.
- Confirm full exports against authorized business requests.
- Review web requests alongside application and server logs.

### Scheduled Administrator Backup Exception

A legitimate administrator may perform backups every Friday at 02:00.

Do not disable all off-hours administrator alerts.

A narrow exception should require a verified administrator or service identity, approved schedule, expected source host, change record and matching backup job identifier.

Unexpected sources, failed or missing backup jobs, and unrelated privileged activity must remain reviewable.

## 7. Dashboard

The detection dashboard was generated using Matplotlib.

Evidence:
`evidence/Task_14_Detection_Dashboard.png`

The dashboard displays:
1. Alerts by severity.
2. Alerts by detection rule.
3. Alert activity over event timestamps.

The dashboard contains 12 alerts and uses the timestamps from the analyzed logs.

## 8. Generated Reports

- `reports/detection_alerts.csv`
- `reports/detection_summary.csv`
- `reports/Task_14_Attack_Detection_Report.md`

## 9. Data Limitations

1. Authentication logs do not contain administrator role information, so AUTH-04 remains inactive.
2. Payroll logs do not contain approval references; missing approval cannot be conclusively established.
3. Payroll logs do not contain source IP information.
4. Geographic changes and web request indicators require additional investigation.
5. The `unlock_AS-14` reference file was not available during this analysis.

## 10. Planted-Item Validation

The assessment requires comparison against 13 planted items in `unlock_AS-14`.

The reference file has not yet been located. Therefore:
- Detection coverage against the 13 planted items is not verified.
- A claim of detecting at least 9 out of 13 items cannot currently be made.
- Validation must be completed when the original reference file becomes available.

## 11. Conclusion

A Python-based log detection and monitoring workflow was implemented successfully.

The system processed 19,942 events across three log sources and generated 12 alerts covering authentication, payroll and suspicious web activity.

A dashboard and CSV reports were generated. Detection limitations and false-positive handling requirements were documented.

The planted-item validation remains pending because the original assessment reference file was unavailable.
