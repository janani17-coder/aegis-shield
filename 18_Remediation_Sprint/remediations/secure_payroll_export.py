"""Defensive payroll-export authorization demonstration.

Uses sample metadata only. Not connected to a real payroll system.
"""

from datetime import datetime, timezone

ALLOWED_REPORTS = {
    "monthly_payroll_summary",
    "department_payroll_summary",
}


def authorize_export(requester, roles, report, approval, audit_log):
    """Authorize an export using role, approval and separation-of-duties checks."""

    if "payroll_export" not in roles:
        raise PermissionError("User is not authorized to export payroll reports")

    if report not in ALLOWED_REPORTS:
        raise ValueError("Report is not on the approved allowlist")

    if not isinstance(approval, dict):
        raise PermissionError("A valid approval record is required")

    if approval.get("status") != "APPROVED":
        raise PermissionError("Export approval is missing or not approved")

    if approval.get("requester") != requester:
        raise PermissionError("Approval requester does not match the user")

    approver = approval.get("approver", "").strip()

    if not approver or approver == requester:
        raise PermissionError("A separate approver is required")

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "actor": requester,
        "action": "PAYROLL_EXPORT",
        "report": report,
        "approval_reference": approval.get("reference"),
        "approver": approver,
        "result": "AUTHORIZED",
    }

    audit_log.append(event)
    return event
