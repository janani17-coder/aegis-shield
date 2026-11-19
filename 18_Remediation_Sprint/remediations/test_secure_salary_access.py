import unittest

from secure_salary_access import authorize_salary_view


class SalaryAccessTests(unittest.TestCase):

    def setUp(self):
        self.audit_log = []

    def test_authorized_own_salary_access(self):
        event = authorize_salary_view(
            "employee_01", {"payroll_view"},
            "employee_01", True, self.audit_log
        )
        self.assertEqual(event["result"], "AUTHORIZED")
        self.assertEqual(len(self.audit_log), 1)

    def test_rejects_unauthenticated_user(self):
        with self.assertRaises(PermissionError):
            authorize_salary_view(
                "employee_01", {"payroll_view"},
                "employee_01", False, self.audit_log
            )

    def test_rejects_missing_role(self):
        with self.assertRaises(PermissionError):
            authorize_salary_view(
                "employee_01", set(),
                "employee_01", True, self.audit_log
            )

    def test_rejects_other_employee_record(self):
        with self.assertRaises(PermissionError):
            authorize_salary_view(
                "employee_01", {"payroll_view"},
                "employee_02", True, self.audit_log
            )

    def test_rejects_missing_employee_id(self):
        with self.assertRaises(PermissionError):
            authorize_salary_view(
                "employee_01", {"payroll_view"},
                "", True, self.audit_log
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
