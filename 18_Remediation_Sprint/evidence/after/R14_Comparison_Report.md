# R-14 - Dependency Remediation Comparison

## Before remediation
- Packages: 8
- Advisory groups: 37
- Vulnerability records: 72
- Source: R14_osv_before.json

## After remediation
- Packages scanned: 8
- Advisory groups: 0
- Vulnerability records: 0
- Source: R14_osv_after.json

## Result
Reported advisory groups reduced from 37 to 0.
Reported vulnerability records reduced from 72 to 0.
Reduction in reported records: 100%.

The updated dependency list installed successfully in an isolated Python 3.11.9 virtual environment.
pip check reported: No broken requirements found.

## Scope and limitations
This result applies only to the eight packages in requirements-remediated.txt.
It does not prove that the complete application, runtime environment, or all transitive dependencies are free of vulnerabilities.
Application-level validation remains pending.
