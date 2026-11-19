import unittest

from secure_employee_record_access import authorize_employee_record_access


class EmployeeRecordAccessTests(unittest.TestCase):

    def setUp(self):
        self.audit_log = []
        self.valid_grant = {
            "status": "APPROVED",
            "requester": "employee_01",
            "target_employee": "employee_02",
            "approver": "manager_01",
        }

    def test_allows_own_record(self):
        event = authorize_employee_record_access(
            "employee_01", {"employee_record_view_own"},
            "employee_01", True, None, self.audit_log
        )
        self.assertEqual(event["result"], "AUTHORIZED")

    def test_allows_approved_delegated_access(self):
        event = authorize_employee_record_access(
            "employee_01", {"employee_record_view_delegated"},
            "employee_02", True, self.valid_grant, self.audit_log
        )
        self.assertEqual(event["access_type"], "APPROVED_DELEGATED_ACCESS")

    def test_rejects_unauthenticated_user(self):
        with self.assertRaises(PermissionError):
            authorize_employee_record_access(
                "employee_01", {"employee_record_view_own"},
                "employee_01", False, None, self.audit_log
            )

    def test_rejects_missing_own_record_role(self):
        with self.assertRaises(PermissionError):
            authorize_employee_record_access(
                "employee_01", set(), "employee_01",
                True, None, self.audit_log
            )

    def test_rejects_missing_delegated_role(self):
        with self.assertRaises(PermissionError):
            authorize_employee_record_access(
                "employee_01", {"employee_record_view_own"},
                "employee_02", True, self.valid_grant, self.audit_log
            )

    def test_rejects_missing_grant(self):
        with self.assertRaises(PermissionError):
            authorize_employee_record_access(
                "employee_01", {"employee_record_view_delegated"},
                "employee_02", True, None, self.audit_log
            )

    def test_rejects_unapproved_grant(self):
        grant = dict(self.valid_grant, status="PENDING")
        with self.assertRaises(PermissionError):
            authorize_employee_record_access(
                "employee_01", {"employee_record_view_delegated"},
                "employee_02", True, grant, self.audit_log
            )

    def test_rejects_wrong_requester(self):
        grant = dict(self.valid_grant, requester="employee_03")
        with self.assertRaises(PermissionError):
            authorize_employee_record_access(
                "employee_01", {"employee_record_view_delegated"},
                "employee_02", True, grant, self.audit_log
            )

    def test_rejects_wrong_target(self):
        grant = dict(self.valid_grant, target_employee="employee_03")
        with self.assertRaises(PermissionError):
            authorize_employee_record_access(
                "employee_01", {"employee_record_view_delegated"},
                "employee_02", True, grant, self.audit_log
            )

    def test_rejects_self_approval(self):
        grant = dict(self.valid_grant, approver="employee_01")
        with self.assertRaises(PermissionError):
            authorize_employee_record_access(
                "employee_01", {"employee_record_view_delegated"},
                "employee_02", True, grant, self.audit_log
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
