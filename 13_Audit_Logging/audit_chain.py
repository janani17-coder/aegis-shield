
import csv
import json
import hashlib
import copy
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR.parent / "03_Data" / "payroll_audit_events.csv"
REPORT_DIR = BASE_DIR / "reports"

CHAIN_FILE = REPORT_DIR / "audit_chain.json"
TAMPERED_FILE = REPORT_DIR / "audit_chain_tampered.json"
DEMO_FILE = REPORT_DIR / "tamper_demo_output.txt"


def calculate_hash(event):
    """Calculate SHA-256 using a consistent JSON representation."""
    data = {
        key: value
        for key, value in event.items()
        if key != "event_hash"
    }

    canonical_data = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":")
    )

    return hashlib.sha256(canonical_data.encode("utf-8")).hexdigest()


def add_entry(chain, event):
    """Add an event linked to the previous event."""
    entry = copy.deepcopy(event)

    entry["event_id"] = f"EVT-{len(chain) + 1:05d}"
    entry["previous_hash"] = (
        chain[-1]["event_hash"] if chain else "GENESIS"
    )
    entry["event_hash"] = calculate_hash(entry)

    chain.append(entry)


def verify_chain(chain):
    """Check event hashes and links to previous events."""
    previous_hash = "GENESIS"

    for index, event in enumerate(chain):
        if event["previous_hash"] != previous_hash:
            return False, f"Broken link at event {index + 1}"

        expected_hash = calculate_hash(event)

        if event["event_hash"] != expected_hash:
            return False, f"Hash mismatch at event {index + 1}"

        previous_hash = event["event_hash"]

    return True, "All events passed verification"


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    chain = []

    # Import the original events without changing the CSV.
    with CSV_FILE.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            event = {
                "timestamp": row["timestamp"],
                "actor": row["actor"],
                "action": row["action"],
                "target_employee": row["target_employee"],
                "result": row["result"],
                "source_ip": None,
                "application": "Payroll Portal",
                "before": None,
                "after": None,
                "reason": None,
                "approval_reference": None,
                "synthetic": False
            }

            add_entry(chain, event)

    # Add one clearly labelled synthetic payroll change.
    demo_event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "actor": "payroll_admin_demo",
        "action": "UPDATE_SALARY",
        "target_employee": "EMP-DEMO-001",
        "result": "OK",
        "source_ip": "192.0.2.10",
        "application": "Payroll Audit Demo",
        "before": {"salary": 50000},
        "after": {"salary": 55000},
        "reason": "Synthetic audit-chain demonstration",
        "approval_reference": "DEMO-APPROVAL-001",
        "synthetic": True
    }

    add_entry(chain, demo_event)

    # Save the original hash chain.
    CHAIN_FILE.write_text(
        json.dumps(chain, indent=2),
        encoding="utf-8"
    )

    valid, message = verify_chain(chain)

    # Make a separate copy and alter an old event.
    tampered_chain = copy.deepcopy(chain)
    tampered_chain[0]["action"] = "MODIFIED_ACTION"

    TAMPERED_FILE.write_text(
        json.dumps(tampered_chain, indent=2),
        encoding="utf-8"
    )

    tampered_valid, tampered_message = verify_chain(tampered_chain)

    output = [
        f"Total chained events: {len(chain)}",
        f"Original chain verification: {valid}",
        f"Original result: {message}",
        f"Tampered chain verification: {tampered_valid}",
        f"Tamper detection result: {tampered_message}",
        "Original CSV modified: No",
        "Synthetic event added: Yes"
    ]

    DEMO_FILE.write_text("\n".join(output), encoding="utf-8")

    print("\n".join(output))


if __name__ == "__main__":
    main()
