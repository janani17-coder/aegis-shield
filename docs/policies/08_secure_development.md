# Policy 8: Secure Development

**Policy ID:** POL-08  
**Owner:** Engineering Lead  
**Status:** Draft

## 1. Purpose

To ensure that Aura Workforce applications are designed, developed, tested, and maintained with security built into each stage.

## 2. Scope

This policy applies to developers, testers, reviewers, build systems, application code, APIs, database queries, and software dependencies used by Aura Workforce.

## 3. Rules

1. Every application change must be stored in version control and linked to a documented change or work item.
2. Code changes must receive review by at least one other authorized team member before being merged into the protected main branch.
3. Applications must enforce authentication and authorization on the server. Hiding a user interface element alone is not an authorization control.
4. APIs that return employee or payroll data must verify that the requesting user is authorized to access each requested record.
5. Applications must validate input on the server and use parameterized database queries for database operations.
6. Payroll calculations and ledger updates must include appropriate integrity checks, validation, and controls against duplicate processing.
7. Secrets, passwords, private keys, and production tokens must not be committed to source code or stored in client-side code.
8. Automated security checks must run in the build or review process for changes to critical applications, with findings tracked until resolved or formally accepted.
9. Developers must test access-control failures and relevant security cases before releasing significant changes.
10. Production releases must have an identified approver, a documented deployment record, and a rollback or recovery plan appropriate to the change.

## 4. Roles

- **Developers:** Follow secure coding rules and fix identified vulnerabilities.
- **Code reviewers:** Check security-sensitive changes before approval.
- **Engineering Lead:** Ensures review and release controls are followed.
- **Security Team:** Provides security requirements and reviews significant risks.
- **Testers:** Verify expected security behavior.

## 5. Exceptions

Exceptions require written approval from the Engineering Lead and Security Team, a documented reason, risk assessment, compensating controls, and an expiry date. Critical unresolved risks must be escalated before release.

## 6. Review Date

**Next review:** 21 October 2027

## Threat Mapping

Supports STRIDE threats **T-03, T-09, T-11, T-15, and T-24** through server-side authorization, input validation, transaction integrity, and secure code review.