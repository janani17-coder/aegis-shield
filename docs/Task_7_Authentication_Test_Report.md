# Task 7 — Authentication Testing Report

## 1. Scope

- **Application:** OWASP Juice Shop
- **Environment:** Local Docker lab
- **URL:** `http://127.0.0.1:3000`
- **Test account:** Fictional lab account only
- **Scope restriction:** Testing was limited to the local lab. No real user accounts or credentials were used.

## 2. Test Results

### T-01 — Registration form

- **Test:** Inspect the registration form and complete registration.
- **Observed result:** Registration completed successfully. The form included password, repeat-password, security-question, and security-answer fields.
- **Evidence:** Registration page screenshot to be captured.
- **Status:** Observed.

### T-02 — Password length validation

- **Test:** Inspect the password requirements and submit a password shorter than the stated minimum.
- **Observed result:** The form displayed: “Password must be 5–40 characters long.” Registration was rejected when the password was shorter than five characters.
- **Policy comparison:** Aegis Shield `POL-02` requires at least 15 characters for password-only authentication.
- **Assessment:** Potential policy mismatch. Server-side enforcement has not been independently verified.
- **Evidence:** Screenshot of the validation message to be captured.
- **Status:** Observed; further validation required.

### T-03 — Password confirmation

- **Test:** Enter different values in the password and repeat-password fields.
- **Observed result:** The form displayed “Passwords do not match.”
- **Assessment:** Mismatch validation worked in this test.
- **Status:** Observed; no vulnerability demonstrated.

### T-04 — Failed login behavior

- **Test:** Make three manual failed login attempts using the fictional lab account.
- **Observed result:** The application displayed a login error. No temporary account block was observed during these three attempts.
- **Assessment:** This limited test does not establish whether account lockout or rate limiting is absent.
- **Evidence:** Screenshot of the error message to be captured, with account details hidden.
- **Status:** Observed; lockout effectiveness not verified.

### T-05 — Logout and refresh

- **Test:** Log out, refresh the page, and inspect the application state.
- **Observed result:** The application showed the Login option after refresh.
- **Assessment:** The logged-out interface persisted. Server-side session invalidation was not directly tested.
- **Status:** Observed; server-side invalidation unverified.

### T-06 — Browser storage after logout

- **Test:** Inspect Local Storage without copying or sharing values.
- **Observed result:** An authentication-related key was present while logged in and disappeared after logout.
- **Assessment:** Client-side cleanup was observed. Server-side token invalidation remains unverified.
- **Status:** Observed.

### T-07 — Password reset

- **Test:** Inspect the password-reset flow using the fictional lab account.
- **Observed result:** The reset page requested an email address and security question/answer. The account's security question was displayed.
- **Assessment:** The recovery flow was observed. Its resistance to guessing or bypass was not tested.
- **Status:** Observed; security effectiveness unverified.

### T-08 — Token expiry

- **Test:** Look for an authentication-related request in the Network tab.
- **Observed result:** New requests appeared, but no request clearly related to login or authentication was identified.
- **Assessment:** Token expiry was not verified.
- **Status:** Not verified.

## 3. Potential Finding

### F-01 — Password minimum-length policy mismatch

**Severity:** Pending risk assessment

**Where:** Juice Shop registration page, password field.

**What:** The form displayed a minimum password length of five characters, while Aegis Shield `POL-02` specifies a minimum of 15 characters for password-only authentication.

**Steps to reproduce:**
1. Open the local Juice Shop registration page.
2. Inspect the password requirement.
3. Enter a password shorter than five characters.
4. Observe the validation message and registration result.

**Evidence:** Record the exact message: “Password must be 5–40 characters long.” Capture a screenshot of the message without exposing account details.

**Impact:** If the application's effective policy permits passwords shorter than the organization's required minimum, it may not meet the organization's password policy and may increase password-guessing risk.

**Fix:** Align application password requirements with the approved policy. Enforce the requirement server-side, block commonly used or exposed passwords, and apply appropriate login rate limiting.

**Retest result:** The form rejected a password shorter than five characters. Independent server-side enforcement and the policy mismatch's practical impact have not been fully validated.

## 4. Recommended Controls for Aura Workforce

1. Require MFA for administrator accounts and remote access.
2. Enforce the approved minimum password length and block common or exposed passwords.
3. Apply and monitor rate limiting for repeated failed sign-ins.
4. Define session expiry and securely invalidate sessions on logout.
5. Protect password recovery with appropriate identity verification and abuse prevention.
6. Log and review suspicious authentication activity.

## 5. Limitations

- Testing was performed only against the local lab.
- Only three manual failed login attempts were performed.
- Server-side session invalidation was not directly tested.
- Token expiry was not verified.
- Password-reset bypass resistance was not tested.
- Findings must not be treated as confirmed vulnerabilities unless supported by additional evidence.

## 6. Completion Status

- [x] Local lab application accessed.
- [x] Registration behavior observed.
- [x] Password-length validation observed.
- [x] Password confirmation behavior observed.
- [x] Three failed login attempts documented.
- [x] Logout and browser-storage behavior documented.
- [x] Password-reset flow inspected.
- [ ] Screenshots captured for Task 7 test results.
- [ ] Additional security tests performed and evidence collected.
- [ ] Five evidence-backed findings completed.
- [ ] Findings reviewed against applicable policies.
