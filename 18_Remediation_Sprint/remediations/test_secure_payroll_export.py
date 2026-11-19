import unittest

from secure_payroll_export import authorize_export


class PayrollExportTests(unittest.TestCase):

    def setUp(self):
        self.approval = {
            "status": "APPROVED",
            "requester": "employee_01",
            "approver": "manager_01",
            "reference": "DEMO-APPROVAL-001",
        }
        self.audit_log = []

    def test_authorized_export(self):
        event = authorize_export(
            "employee_01",
            {"payroll_export"},
            "monthly_payroll_summary",
            self.approval,
            self.audit_log,
        )
        self.assertEqual(event["result"], "AUTHORIZED")
        self.assertEqual(len(self.audit_log), 1)

    def test_rejects_missing_role(self):
        with self.assertRaises(PermissionError):
            authorize_export(
                "employee_01", set(), "monthly_payroll_summary",
                self.approval, self.audit_log
            )

    def test_rejects_missing_approval(self):
        with self.assertRaises(PermissionError):
            authorize_export(
                "employee_01", {"payroll_export"},
                "monthly_payroll_summary", None, self.audit_log
            )

    def test_rejects_self_approval(self):
        approval = dict(self.approval, approver="employee_01")
        with self.assertRaises(PermissionError):
            authorize_export(
                "employee_01", {"payroll_export"},
                "monthly_payroll_summary", approval, self.audit_log
            )

    def test_rejects_unapproved_report(self):
        with self.assertRaises(ValueError):
            authorize_export(
                "employee_01", {"payroll_export"},
                "full_employee_data", self.approval, self.audit_log
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
