# Task 6 — RBAC Conflicts, Fixes, and Policy Alignment

## Design assumptions
- `Own` means access only to the signed-in user's own record.
- `Yes` means access is still restricted to the role's approved scope and must be logged for sensitive operations.
- `No` means the role is not granted the permission by default.
- The template has no separate Finance role. Therefore, ledger posting/editing and broad financial-report access remain `No` for all four roles until a dedicated Finance role and controls are approved.
- `ADMIN` is a technical administration role, not a universal business superuser. Administrative actions must be logged and role changes require independent approval.

## Three dangerous combinations and fixes

1. **One person can run and approve payroll.**
   - Risk: an error or fraudulent payroll change could be processed without independent review.
   - Fix: HR may run payroll; a separate authorized approver (shown as MANAGER in this four-role template) approves it. Enforce that the same user cannot perform both steps, and require approval evidence.

2. **One person can change roles and then use the elevated access.**
   - Risk: an administrator could grant themselves or an accomplice unnecessary privileges.
   - Fix: require a documented request and independent approval for every role change; prevent self-approval; log before/after role values and review role changes periodically.

3. **One person can access/export all payroll data without a business need.**
   - Risk: bulk exposure of salary and personal data.
   - Fix: only HR receives full payroll view/export permissions for approved duties; require a recorded purpose, audit logging, and approval for bulk exports. ADMIN, MANAGER, and EMPLOYEE do not receive full payroll export permission.

## Day 5 audit follow-up
- **Privilege mismatches / privilege creep:** validate each flagged account against its approved job role and owner, not department alone. Remove unnecessary admin privileges, assign the minimum business role, record approval, and verify the change in the audit log.
- **Admin without MFA:** require MFA for every privileged account before retaining administrative access.
- **Shared accounts:** replace shared identities with named individual accounts; retain a documented owner and audit trail for any technical service account, and do not use shared human logins.
- **Leavers still active:** disable access on the exit date and verify the disablement event.
- **Dormant accounts:** review accounts inactive for 90 days; disable or remove access when no current business need is confirmed.

## Day 3 access policy alignment and required updates
The matrix follows individual accounts, least privilege, administrative MFA, logging, and separation of duties. Update the Day 3 policy to make these rules explicit:
1. Disable leaver accounts on the confirmed exit date (stricter than a one-business-day allowance).
2. Review accounts inactive for 90 days and disable them when no approved need exists.
3. Limit privileged administrator roles to approved IT/security owners; department name alone is not sufficient proof of authorization.
4. Prohibit shared human accounts; service accounts must be individually identified, owned, justified, and monitored.
5. Require independent approval for role changes and payroll approval, and prohibit self-approval.

## Three-sentence response to the HR manager
“I can’t grant broad Admin rights just in case, because access must match an approved business need. I can help identify the specific HR tasks you need and request the minimum permissions required for them. Any additional access must be approved, time-limited where possible, logged, and reviewed.”

## Ten suggested automated checks
1. Every permission cell contains only `Yes`, `No`, or `Own`.
2. Every `Yes` permission has a non-empty justification.
3. EMPLOYEE has `Own` for viewing their own profile.
4. EMPLOYEE has `Own` for viewing their own payslip.
5. EMPLOYEE cannot view any payslip.
6. MANAGER can approve leave for their own team only.
7. HR can run payroll.
8. MANAGER is the separate payroll approver in this proposed four-role design.
9. ADMIN role changes require independent approval and are logged.
10. No role can both run and approve the same payroll run as the same user.

**Important limitation:** the matrix alone cannot enforce same-user separation, team scoping, MFA, logging, approval workflows, or same-day deprovisioning. Those controls must be implemented and tested in the application/process.
