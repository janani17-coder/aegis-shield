
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
REPORTS = BASE / "reports"
EVIDENCE = BASE / "evidence"

EVIDENCE.mkdir(exist_ok=True)

alerts_file = REPORTS / "detection_alerts.csv"
df = pd.read_csv(alerts_file)

df["timestamp"] = pd.to_datetime(
    df["timestamp"], errors="coerce", utc=True
)
df = df.dropna(subset=["timestamp"])

# Create a dashboard with three charts
fig, axes = plt.subplots(3, 1, figsize=(14, 15))

# 1. Alerts by severity
severity_counts = (
    df["severity"].value_counts().reindex(
        ["Critical", "High", "Medium", "Low"], fill_value=0
    )
)
severity_counts.plot(
    kind="bar", ax=axes[0], title="Alerts by Severity"
)
axes[0].set_ylabel("Number of Alerts")
axes[0].set_xlabel("Severity")

# 2. Alerts by detection rule
rule_counts = df["rule"].value_counts().sort_values()
rule_counts.plot(
    kind="barh", ax=axes[1], title="Alerts by Detection Rule"
)
axes[1].set_xlabel("Number of Alerts")
axes[1].set_ylabel("Detection Rule")

# 3. Alerts over time
hourly = (
    df.set_index("timestamp")
      .resample("1h")
      .size()
)
hourly.plot(
    kind="line", marker="o", ax=axes[2],
    title="Alert Activity Over Event Time"
)
axes[2].set_xlabel("Event Timestamp (UTC)")
axes[2].set_ylabel("Number of Alerts")
axes[2].grid(True)

# Dashboard title and metadata
start = df["timestamp"].min()
end = df["timestamp"].max()

fig.suptitle(
    "AEGIS SHIELD - TASK 14 ATTACK DETECTION DASHBOARD",
    fontsize=15,
    fontweight="bold"
)

fig.text(
    0.5, 0.015,
    f"Generated: {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M UTC} | "
    f"Alerts: {len(df)} | "
    f"Event range: {start:%Y-%m-%d %H:%M} to {end:%Y-%m-%d %H:%M} UTC",
    ha="center",
    fontsize=9
)

plt.tight_layout(rect=[0, 0.04, 1, 0.96])

output = EVIDENCE / "Task_14_Detection_Dashboard.png"
plt.savefig(output, dpi=200, bbox_inches="tight")
plt.show()

print(f"Dashboard saved: {output}")
print(f"Total alerts displayed: {len(df)}")
