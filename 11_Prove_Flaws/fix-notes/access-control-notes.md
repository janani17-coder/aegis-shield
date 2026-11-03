# Broken Access Control – Basket Investigation

## Application
OWASP Juice Shop – Local Docker Lab

## Test Account
Newly registered lab-only test account.

## Baseline HTTP Observation
- Endpoint: `/rest/basket/6`
- Method: GET
- Status: 304 Not Modified
- Result: My own test product was visible in the basket response.

## Initial Observation
The basket identifier appears in the request URL. This is a client-visible identifier. Its presence alone does not prove broken access control.

## Root Cause
Pending verification. The server-side authorisation check must be reviewed to determine whether it verifies that the requested basket belongs to the authenticated user.

## Developer Fix
Derive the user's identity from the authenticated server-side session. Verify basket ownership on every basket read and modification. Do not rely on a client-supplied basket identifier as proof of permission.

## Regression Test
- Confirm an authenticated user can access their own basket.
- Confirm a user cannot access or modify another user's basket.
- Confirm unauthenticated requests are rejected.
- Confirm normal basket operations continue to work.

## Evidence
- Baseline request: GET `/rest/basket/6`
- Status: 304 Not Modified
- Own test product visible.
- Cross-user authorisation test: Not performed.

## Current Conclusion
Baseline basket functionality is confirmed. Broken access control has not yet been proven.

## Source Code Review

**File:** `routes/basket.ts`

**Function:** `retrieveBasket()`

**Relevant observations:**
- The requested basket ID is obtained from `req.params.id`.
- `BasketModel.findOne()` retrieves the basket using that ID.
- The displayed retrieval logic does not visibly verify that the requested basket belongs to the authenticated user before retrieving it.
- The `challengeUtils.solveIf()` condition is challenge-detection logic, not an access-control enforcement mechanism.

**Security Assessment:**
A potential Broken Access Control issue was identified through source-code review. Cross-user access was not attempted, so runtime exploitation is not claimed.

**Recommended Fix:**
Before returning basket data, verify that the authenticated user's server-side basket ID matches the requested basket ID. Reject unauthorised requests with HTTP 403 or an appropriate not-found response. Apply equivalent ownership checks to basket modifications.

**Evidence:**
- Source file: `routes/basket.ts`
- Function: `retrieveBasket()`
- Baseline request: GET `/rest/basket/6`
- Own basket product successfully displayed.

