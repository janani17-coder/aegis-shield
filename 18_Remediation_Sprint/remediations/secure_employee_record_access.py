"""Defensive employee-record ownership authorization demonstration.

Uses sample metadata only. Not connected to a real payroll system.
"""


def authorize_employee_record_access(
    requester_id,
    requester_roles,
    target_employee_id,
    authenticated,
    access_grant,
    audit_log,
):
    """Authorize own-record or explicitly approved delegated access."""

    if not authenticated:
        raise PermissionError("Authentication is required")

    if not requester_id or not target_employee_id:
        raise PermissionError("Valid user and employee identifiers are required")

    if requester_id == target_employee_id:
        if "employee_record_view_own" not in requester_roles:
            raise PermissionError("Own-record viewing permission is required")
        access_type = "OWN_RECORD"

    else:
        if "employee_record_view_delegated" not in requester_roles:
            raise PermissionError("Delegated access role is required")

        if not isinstance(access_grant, dict):
            raise PermissionError("Approved access grant is required")

        if access_grant.get("status") != "APPROVED":
            raise PermissionError("Access grant is not approved")

        if access_grant.get("requester") != requester_id:
            raise PermissionError("Access grant requester does not match")

        if access_grant.get("target_employee") != target_employee_id:
            raise PermissionError("Access grant target does not match")

        if access_grant.get("approver") == requester_id:
            raise PermissionError("Requester cannot approve their own access")

        if not access_grant.get("approver"):
            raise PermissionError("Independent approver is required")

        access_type = "APPROVED_DELEGATED_ACCESS"

    event = {
        "actor": requester_id,
        "action": "VIEW_EMPLOYEE_RECORD",
        "target_employee": target_employee_id,
        "access_type": access_type,
        "result": "AUTHORIZED",
    }

    audit_log.append(event)
    return event
