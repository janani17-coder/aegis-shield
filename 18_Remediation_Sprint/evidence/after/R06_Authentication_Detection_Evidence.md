# R-06 - Authentication Detection Evidence

## Source
14_Attack_Detection/reports/detection_alerts.csv

## Verified results

Total alert records: 21

Authentication-related alerts:
- AUTH-01 Account brute force: 3
- AUTH-02 Password spraying: 2
- WEB-02 Web login brute force: 1

Total authentication-related alerts: 6

## Result
The existing detection report contains alerts for repeated failed logins, password spraying, and web login brute-force indicators.

## Limitations
- These are detection results from the assessment dataset.
- They do not prove that preventive rate limiting is deployed.
- The dataset does not contain a dedicated MFA status field.
- MFA implementation and enforcement require separate verification.
- Detection thresholds must be validated against normal production traffic.

## Status
Detection evidence verified.
Preventive controls: Not verified.
