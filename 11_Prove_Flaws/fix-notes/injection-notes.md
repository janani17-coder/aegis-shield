# SQL Injection – Login Admin

## Application
OWASP Juice Shop – Local Docker Lab

## Vulnerable File
routes/login.ts

## Root Cause
The application directly inserts the email supplied by
the user into an SQL query using string interpolation.

This allows user input to affect the SQL statement structure.

## Developer Fix
Use parameterized SQL queries or safe Sequelize ORM methods.
Never concatenate untrusted input into SQL statements.

## Regression Test
Submit SQL metacharacters as an email.
Verify they are treated only as data.

Also test valid and invalid login attempts.

## Business Impact
In a payroll application, a similar vulnerability could
expose employee or payroll records, depending on database
permissions and other security controls.

## Evidence
Source code: routes/login.ts
Runtime SQL injection proof: Pending