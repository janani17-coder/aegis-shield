# E-21 – Installed Python Environment Check

Date: 22 November 2026

## Result
The globally installed Python environment was inspected using `python -m pip show` and `python -m pip check`.

The installed versions were:
- Flask 3.1.3
- Jinja2 3.1.6
- Werkzeug 3.1.8
- PyYAML 6.0.3
- Requests 2.33.1
- urllib3 2.6.3
- idna 3.11

`python -m pip check` returned: No broken requirements found.

## Scope limitation
These are globally installed packages, not a verified installation of the payroll application's pinned requirements.txt. The clean dependency check does not establish that the payroll sample is remediated or that its E-20 advisories are inapplicable.

## Conclusion
E-21 is environment inventory evidence only. It does not replace the E-20 manifest audit, application testing, dependency compatibility testing or a fresh audit of an isolated payroll environment.
