# Task 11 – Prove Security Flaws

## 1. Objective

Investigate one injection issue, one cross-site scripting (XSS) issue, and one broken access-control issue in the local OWASP Juice Shop lab. Review the evidence, identify potential root causes, recommend fixes, and define regression tests.

## 2. Lab Environment

- Application: OWASP Juice Shop
- Environment: Local Docker lab
- Application URL: `http://127.0.0.1:3000`
- Testing scope: Own lab account and local application source code

## 3. Finding 1 – SQL Injection

**Challenge:** Login Admin

**Source file:** `routes/login.ts`

**Observation:** Source-code review identified SQL query construction using string interpolation with the email supplied in the login request.

**Root cause:** Untrusted input is inserted directly into an SQL statement rather than being passed as a parameter.

**Potential impact:** In a payroll application, a similar weakness could expose employee or payroll records, depending on database permissions and other controls.

**Recommended fix:** Use parameterized queries or safe Sequelize ORM methods. Never concatenate untrusted input into SQL statements.

**Regression test:** Verify that special characters in email input are treated as data. Test valid and invalid login attempts using automated tests and a test database.

**Evidence status:** Source-code pattern identified. Runtime SQL injection was not demonstrated.

## 4. Finding 2 – DOM-Based Cross-Site Scripting

**Challenge:** DOM XSS

**Source files:**
- `frontend/src/app/search-result/search-result.component.ts`
- `frontend/src/app/search-result/search-result.component.html`

**Observation:** A harmless HTML-like search value was rendered as formatted HTML in the search results.

**Root cause:** The application uses `bypassSecurityTrustHtml()` on search input and displays the result using `[innerHTML]`.

**Potential impact:** If executable untrusted content can reach this rendering path, it could affect users viewing the page. Actual impact depends on browser protections and application controls.

**Recommended fix:** Treat search input as plain text. Avoid bypassing Angular's HTML sanitization for untrusted data. Use normal text interpolation.

**Regression test:** Submit harmless HTML-like input and verify it is displayed literally rather than interpreted as HTML. Confirm normal search functionality still works.

**Evidence status:** HTML interpretation demonstrated with a screenshot. JavaScript execution was not demonstrated.

## 5. Finding 3 – Broken Access Control

**Challenge:** View Basket

**Source file:** `routes/basket.ts`

**Function:** `retrieveBasket()`

**Baseline request:**
- Method: GET
- Endpoint: `/rest/basket/6`
- Status: 304 Not Modified
- Result: Own test product was visible.

**Source-code observation:** The displayed function retrieves a basket using the requested ID. The shown retrieval logic does not visibly check basket ownership before returning the result.

**Root cause:** A server-side ownership check was not visible in the reviewed function. Other middleware or route-level controls still need to be checked.

**Potential impact:** If no other authorisation control exists, a similar issue could expose another employee's basket or associated information.

**Recommended fix:** Derive the authenticated user identity from the server-side session and verify basket ownership on every read and modification. Reject unauthorised requests.

**Regression test:**
- Allow users to access their own basket.
- Deny access to baskets they do not own.
- Reject unauthenticated requests.
- Confirm normal basket operations continue to work.

**Evidence status:** Baseline request and source-code observation recorded. Cross-user access was not tested. Finding remains potential, not confirmed.

## 6. Evidence Files

Evidence and notes are stored under:

`11_Prove_Flaws/`

- `fix-notes/injection-notes.md`
- `fix-notes/xss-notes.md`
- `fix-notes/access-control-notes.md`
- `evidence/xss/dom-xss-html-rendering.png`

## 7. Payroll Application – Remediation Priority

1. **SQL Injection:** Prioritise investigation and remediation because an unsafe database query may put sensitive payroll records at risk.
2. **Broken Access Control:** Verify ownership enforcement and remediate any missing server-side checks because employee records must only be accessible to authorised users.
3. **DOM XSS:** Remove unsafe HTML handling and ensure untrusted input is rendered as text.

All three issues should be addressed promptly. Final priority should be based on verified exploitability, affected data, exposure, and business impact.

## 8. Limitations

- Testing was restricted to the local OWASP Juice Shop lab.
- No other user's basket or private data was accessed.
- SQL injection was identified through source-code review only.
- XSS HTML interpretation was demonstrated, but JavaScript execution was not.
- Basket ownership enforcement through other middleware or route-level controls remains to be verified.

## 9. Conclusion

Task 11 identified three security patterns for further investigation. Source-code review revealed unsafe SQL query construction, unsafe HTML rendering, and a potentially missing basket ownership check. Evidence and recommended fixes were documented while avoiding unsupported claims of successful exploitation.
