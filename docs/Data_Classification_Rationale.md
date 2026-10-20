# Aegis Shield — Data Classification Deliverables

## Scope and assumptions

The supplied worksheet contains 169 data columns across 11 tables. Classifications are proposed for a realistic internal business system, not a legal determination. The examples in the supplied worksheet are fictional; decisions should be reviewed by the data owner/security lead before production use.

- **Public:** explicitly approved for unrestricted public release.
- **Internal:** routine business information that should remain inside the organisation.
- **Confidential:** non-public employee, client, vendor, transaction, or business information.
- **Restricted:** highly sensitive personal, compensation, employment assessment, or security-related information requiring strict need-to-know access.

Personal-data status is recorded separately from sensitivity. A field can be personal data without being Restricted, and a field can be Confidential without being personal data.

## Classification summary

| Sensitivity level | Number of columns |
|---|---:|
| Public | 0 |
| Internal | 60 |
| Confidential | 74 |
| Restricted | 35 |
| **Total** | **169** |

The lack of Public fields is intentional: the worksheet describes operational records and does not identify any field as approved for public release. A field should not be Public merely because its sample value looks harmless.

## 20 difficult classification decisions

### `employees.date_of_birth` — Restricted

Date of birth is a strong personal identifier and can enable identity fraud or re-identification when combined with other fields.

### `employees.gender` — Restricted

Gender is personal information and can create discrimination risk; the worksheet itself says it is for fairness testing only and must not be a model input.

### `employees.career_gap_months` — Restricted

This is personal employment-history information and is explicitly linked to a planted pay-bias scenario; restrict access and prevent inappropriate model use.

### `employees.commute_distance_km` — Restricted

Home-to-office distance can reveal patterns about a person's home location and routine, especially when linked to an employee ID.

### `employees.exit_reason` — Restricted

Exit reasons can reveal sensitive employment circumstances and are marked as post-outcome information with leakage risk in the AI dataset.

### `users.password_policy_note` — Internal

The field is a handling reminder and explicitly says no passwords or hashes are stored. Actual credentials or hashes must never be placed here and would require Restricted handling.

### `salary_revisions.previous_annual_fixed` — Restricted

Individual historical salary is highly sensitive compensation data and could cause privacy or employment harm if disclosed.

### `salary_revisions.new_annual_fixed` — Restricted

Individual new salary is highly sensitive compensation data; restrict to authorised HR/payroll personnel and approvers.

### `salary_revisions.pct_change` — Restricted

A pay-change percentage reveals compensation decisions and can expose individual salary progression when linked to an employee.

### `performance_reviews.performance_rating` — Restricted

Performance ratings can materially affect employment decisions and should be limited to HR and authorised managers.

### `performance_reviews.rating_label` — Restricted

The text label communicates an individual's performance assessment and has the same confidentiality risks as the numeric rating.

### `leave_requests.reason` — Restricted

Free-text leave reasons may reveal health, family, or other private circumstances. Minimise collection and tightly restrict access.

### `leave_requests.leave_type_code` — Restricted

Leave type can indirectly reveal health or family circumstances (for example, medical or maternity leave), so access should be limited.

### `payroll_items.net_pay` — Restricted

Take-home pay is highly sensitive individual financial information, derived from salary and deductions.

### `payroll_items.tds` — Restricted

Tax deductions reveal individual compensation and tax-related information; limit access to authorised payroll staff.

### `payroll_items.other_deductions` — Restricted

Loan recovery or other deductions can reveal personal financial circumstances and should be strongly protected.

### `journal_entries.total_debit` — Confidential

Journal totals are internal financial records. They are not normally personal data alone, but disclosure could expose financial position and activity.

### `clients.contact_email` — Confidential

A role-based accounts mailbox is not necessarily personal data, but it is non-public client contact information and should be protected from misuse.

### `invoices.po_number` — Confidential

Purchase order references can be used to correlate commercial transactions and client procurement records; restrict external sharing.

### `expenses.description` — Confidential

Expense descriptions can reveal operational details or business arrangements. Review free text for personal or confidential information before sharing.

## References

- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- OWASP Application Security Verification Standard (ASVS): https://owasp.org/www-project-application-security-verification-standard/
- OWASP Threat Dragon: https://owasp.org/www-project-threat-dragon/

## Review notes

1. Confirm classifications with the organisation's data owner and applicable policies before production use.
2. Use least privilege and role-based access; review access periodically.
3. Encrypt Confidential and Restricted information in transit and at rest where appropriate.
4. Avoid copying Restricted information into screenshots, public repositories, issue trackers, or unapproved AI tools.
5. The `password_policy_note` field is Internal because it explicitly states that the worksheet stores no passwords or hashes. Actual credentials, password hashes, API keys, and tokens must not be stored in the worksheet and require Restricted handling.
6. The personal-data flag reflects whether the field identifies, describes, or can be linked to a person in the table context. For production data, privacy/legal review may refine these decisions.
