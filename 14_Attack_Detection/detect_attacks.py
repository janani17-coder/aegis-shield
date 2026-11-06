
import re
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
REPORTS = BASE / "reports"

REPORTS.mkdir(exist_ok=True)

alerts = []


def add_alert(rule, timestamp, severity, entity, details, first_check):
    alerts.append({
        "timestamp": timestamp,
        "rule": rule,
        "severity": severity,
        "entity": entity,
        "details": details,
        "first_check": first_check
    })


# ---------------- AUTHENTICATION ----------------

auth = pd.read_csv(DATA / "auth_events.csv")
auth["timestamp"] = pd.to_datetime(auth["timestamp"], errors="coerce")
auth = auth.dropna(subset=["timestamp"])

# Rule 1: Many failed logins against one account.
failed = auth[auth["event"].str.contains("FAIL", case=False, na=False)]

for user, group in failed.groupby("username"):
    group = group.sort_values("timestamp")
    window = group.set_index("timestamp").resample("10min").size()

    for time, count in window[window >= 5].items():
        add_alert(
            "AUTH-01 Account brute force",
            time,
            "High",
            user,
            f"{count} failed logins in 10 minutes",
            "Check account owner, source IPs, successful logins and MFA."
        )

# Rule 2: One IP failing against many accounts.
for ip, group in failed.groupby("source_ip"):
    group = group.sort_values("timestamp")
    window = group.set_index("timestamp").resample("10min")["username"].nunique()

    for time, count in window[window >= 5].items():
        add_alert(
            "AUTH-02 Password spraying",
            time,
            "High",
            ip,
            f"{count} distinct accounts targeted in 10 minutes",
            "Check targeted accounts, source reputation and any later successes."
        )

# Rule 3: Same account logging in from two countries within 30 minutes.
success = auth[auth["event"].str.contains("SUCCESS", case=False, na=False)]

for user, group in success.groupby("username"):
    group = group.sort_values("timestamp")
    rows = group.to_dict("records")

    for i in range(1, len(rows)):
        previous = rows[i - 1]
        current = rows[i]
        minutes = (
            current["timestamp"] - previous["timestamp"]
        ).total_seconds() / 60

        if (
            0 <= minutes <= 30
            and previous["country"] != current["country"]
        ):
            add_alert(
                "AUTH-03 Rapid country change",
                current["timestamp"],
                "High",
                user,
                f"{previous['country']} to {current['country']} in {minutes:.1f} minutes",
                "Check VPN use, travel confirmation, device and session details."
            )

# Rule 4: Admin login at unusual hours.
# Do not infer administrator status from username.
# Activate only if an explicit role field is available.
if "role" in auth.columns:
    admin = auth[auth["role"].astype(str).str.upper().eq("ADMIN")]
    odd = admin[
        admin["timestamp"].dt.hour.isin([0, 1, 2, 3, 4, 5, 22, 23])
        & admin["event"].str.contains("SUCCESS", case=False, na=False)
    ]

    for _, row in odd.iterrows():
        add_alert(
            "AUTH-04 Admin off-hours login",
            row["timestamp"],
            "Medium",
            row["username"],
            f"Successful administrator login at {row['timestamp'].strftime('%H:%M')}",
            "Check approved schedule, backup jobs, source IP and MFA."
        )


# ---------------- PAYROLL ----------------

payroll = pd.read_csv(DATA / "payroll_audit_events.csv")
payroll["timestamp"] = pd.to_datetime(payroll["timestamp"], errors="coerce")
payroll = payroll.dropna(subset=["timestamp"])

# Rule 5: High-volume salary viewing at night.
night = payroll[
    payroll["action"].eq("VIEW_SALARY")
    & payroll["timestamp"].dt.hour.isin([0, 1, 2, 3, 4, 5, 22, 23])
]

for actor, group in night.groupby("actor"):
    group = group.sort_values("timestamp")
    counts = group.set_index("timestamp").resample("1h")["target_employee"].nunique()

    for time, count in counts[counts >= 10].items():
        add_alert(
            "PAY-01 Night salary access",
            time,
            "High",
            actor,
            f"{count} distinct salary records viewed in one hour",
            "Check job role, approved task, access reason and export activity."
        )

# Rule 6: Full payroll export.
exports = payroll[payroll["action"].eq("EXPORT_FULL_PAYROLL")]

for _, row in exports.iterrows():
    add_alert(
        "PAY-02 Full payroll export",
        row["timestamp"],
        "High",
        row["actor"],
        f"Full payroll export result: {row['result']}",
        "Verify approval, business purpose, recipient and data-transfer record."
    )

# Rule 7: Salary change without approval evidence.
salary_changes = payroll[payroll["action"].eq("UPDATE_SALARY")]

for _, row in salary_changes.iterrows():
    # The supplied CSV has no approval_reference column.
    add_alert(
        "PAY-03 Salary change approval review",
        row["timestamp"],
        "Medium",
        row["actor"],
        f"Salary change for {row['target_employee']}; approval not verifiable from source CSV",
        "Check the authoritative approval workflow and change ticket."
    )


# ---------------- WEB ACCESS ----------------

web_pattern = re.compile(
    r"(?P<ip>\S+) \S+ \S+ "
    r"\[(?P<time>[^\]]+)\] "
    r'"(?P<method>[A-Z]+) (?P<path>\S+) HTTP/[^"]+" '
    r'(?P<status>\d{3}) (?P<size>\S+) '
    r'"(?P<referer>[^"]*)" "(?P<agent>[^"]*)"'
)

suspicious_patterns = {
    "SQL injection indicator": r"(?i)(union\s+select|or\s+1=1|sleep\s*\(|information_schema)",
    "Script injection indicator": r"(?i)(<script|javascript:|onerror\s*=|onload\s*=)",
    "Path traversal indicator": r"(?i)(\.\./|%2e%2e|/etc/passwd|%2fetc%2f)",
    "Scanning indicator": r"(?i)(sqlmap|nikto|nmap|dirbuster|gobuster)"
}

web_rows = []

with (DATA / "web_access.log").open("r", encoding="utf-8", errors="replace") as file:
    for line in file:
        match = web_pattern.search(line)

        if not match:
            continue

        row = match.groupdict()
        row["timestamp"] = pd.to_datetime(
            row["time"], format="%d/%b/%Y:%H:%M:%S %z", errors="coerce"
        )
        web_rows.append(row)

web = pd.DataFrame(web_rows)

if not web.empty:
    for _, row in web.iterrows():
        for label, pattern in suspicious_patterns.items():
            if re.search(pattern, row["path"] + " " + row["agent"]):
                add_alert(
                    "WEB-01 " + label,
                    row["timestamp"],
                    "High",
                    row["ip"],
                    f"{row['method']} {row['path']} returned HTTP {row['status']}",
                    "Check request context, response, related requests and application logs."
                )

# ---------------- OUTPUT ----------------

columns = [
    "timestamp", "rule", "severity",
    "entity", "details", "first_check"
]

result = pd.DataFrame(alerts, columns=columns)

if not result.empty:
    result["timestamp"] = pd.to_datetime(
    result["timestamp"], errors="coerce", utc=True
)

result = result.dropna(subset=["timestamp"])
result = result.sort_values("timestamp")

result.to_csv(REPORTS / "detection_alerts.csv", index=False)

summary = (
    result.groupby(["rule", "severity"])
    .size()
    .reset_index(name="alert_count")
    if not result.empty
    else pd.DataFrame(columns=["rule", "severity", "alert_count"])
)

summary.to_csv(REPORTS / "detection_summary.csv", index=False)

print("Authentication events:", len(auth))
print("Payroll events:", len(payroll))
print("Web requests parsed:", len(web))
print("Total alerts:", len(result))
print("\nAlerts by rule:")
print(summary.to_string(index=False))
print("\nReports saved in:", REPORTS)
