
# Detection and Monitoring

## Overview

Aegis Shield includes a Python-based detection and monitoring learning exercise using synthetic authentication, payroll audit and web request datasets.

## Assessment Results

| Data Source | Events Analysed |
|---|---:|
| Authentication logs | 11,487 |
| Payroll audit events | 2,652 |
| Web requests | 5,805 |
| **Total** | **19,944** |

## Detection Categories

The assessment included detection logic for:

- Repeated authentication failures.
- Password spraying indicators.
- Unusual authentication patterns.
- Administrative activity outside expected hours.
- Sensitive payroll access and export activity.
- Suspicious web request patterns.
- Potential injection and scanning indicators.

## Alert Summary

The recorded assessment produced 21 alert rows across the configured detection rules.

Alerts require human investigation. They are indicators for review, not proof that an attack or data breach occurred.

## Monitoring Evidence

The project includes:

- Python detection scripts.
- Detection rule documentation.
- Alert output files.
- Detection summary.
- Dashboard screenshot.

[View Aegis Shield Repository](https://github.com/janani17-coder/aegis-shield)

## Monitoring Limitations

- The assessment uses synthetic datasets.
- This project does not provide continuous production monitoring.
- Detection results depend on the available input data.
- Some indicators require additional context and investigation.
- No dedicated ransomware detection capability has been demonstrated.

> This is a defensive cybersecurity learning exercise. No live customer or production data is published here.
