"""Defensive salary-record authorization demonstration.

Uses sample metadata only. Not connected to a real payroll system.
"""


def authorize_salary_view(
    requester_id,
    requester_roles,
    target_employee_id,
    authenticated,
    audit_log,
):
    """Check authentication, role and employee-record ownership."""

    if not authenticated:
        raise PermissionError("Authentication is required")

    if not requester_id or not target_employee_id:
        raise PermissionError("Valid user and employee identifiers are required")

    if "payroll_view" not in requester_roles:
        raise PermissionError("Payroll viewing permission is required")

    if requester_id != target_employee_id:
        raise PermissionError("Access to another employee's salary record is denied")

    event = {
        "actor": requester_id,
        "action": "VIEW_OWN_SALARY",
        "target_employee": target_employee_id,
        "result": "AUTHORIZED",
    }

    audit_log.append(event)
    return event
