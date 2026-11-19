
# Security Findings

## Overview

This section summarises security weaknesses identified during the Aegis Shield learning assessment.

The findings are based on source-code review and controlled laboratory assessment. They do not establish successful exploitation of a live system.

## Finding 1 – SQL Injection Risk

**Category:** Injection

**Observation:** Unsafe SQL query construction using string interpolation was identified during source-code review.

**Potential Impact:** Improper query handling may expose application data.

**Recommended Mitigation:**
- Use parameterised queries.
- Validate input on the server.
- Apply least-privilege database permissions.
- Include security tests in development.

**Validation Status:** Source-code issue identified. Runtime exploitation was not demonstrated.

## Finding 2 – Cross-Site Scripting Risk

**Category:** Injection / Client-side security

**Observation:** Unsafe HTML rendering patterns involving trusted HTML handling were identified.

**Potential Impact:** Improper handling of untrusted content may create a client-side scripting risk.

**Recommended Mitigation:**
- Use framework-provided safe rendering.
- Avoid bypassing sanitisation.
- Apply context-appropriate output encoding.
- Review untrusted HTML handling.

**Validation Status:** Unsafe rendering behaviour was observed. JavaScript execution was not demonstrated.

## Finding 3 – Broken Access Control Risk

**Category:** Access Control

**Observation:** A source-code review identified a potentially incomplete ownership check in basket retrieval logic.

**Potential Impact:** Inadequate ownership enforcement could expose another user's records.

**Recommended Mitigation:**
- Enforce server-side ownership checks.
- Apply deny-by-default access controls.
- Review authorisation at every sensitive endpoint.
- Add access-control tests.

**Validation Status:** Potential weakness identified through source review. Cross-user access was not tested.

## Assessment Limitations

- Findings are based on the available assessment evidence.
- Successful exploitation was not established for these findings.
- The findings do not represent a live production security audit.
- Further authorised testing and remediation validation are required.

> All assessment findings belong to a fictional cybersecurity learning project.
