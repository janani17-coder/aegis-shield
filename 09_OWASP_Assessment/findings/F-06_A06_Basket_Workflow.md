# F-06 — Normal Shopping Basket Workflow

## Finding Details

- **Finding ID:** F-06
- **Title:** Product added to basket successfully
- **Application:** OWASP Juice Shop — local lab
- **Target:** `http://127.0.0.1:3000`
- **OWASP Category:** A06 — Insecure Design
- **Severity:** Informational
- **Status:** Normal workflow observed; security design not fully assessed

## Summary

A product was added to the local Juice Shop basket through the normal user interface. The product appeared in the basket as expected.

## Scope and Preconditions

- Testing was restricted to the local Juice Shop lab.
- The normal product-selection and add-to-basket workflow was used.
- No order was placed and no payment was made.

## Steps to Reproduce

1. Open `http://127.0.0.1:3000`.
2. Select a product from the product list.
3. Choose **Add to Basket**.
4. Open the basket and inspect the displayed product.

## Expected Result

The application should handle the normal basket workflow correctly and enforce applicable authorization and business rules for sensitive actions.

## Actual Result

The product was added and appeared in the basket. Authorization boundaries and security-sensitive business rules were not tested.

## Evidence

- Evidence source: Manual browser observation.
- Screenshot: Not captured for this check.

## Impact

No insecure design vulnerability was confirmed. A successful normal workflow does not establish whether the application prevents unauthorized or invalid business actions.

## Recommendation

Review authorization requirements and business rules for basket changes, checkout, order submission, and other sensitive workflows. Test them with authorized lab accounts.

## STRIDE Threat Mapping

- **Threat ID:** T-11
- **Rationale:** T-11 concerns payroll calculations or results being altered. The basket test did not involve payroll calculations, so this is not a direct match. Use the mapping only as a broad integrity-related reference, not as evidence of T-11.

## Limitations

Only the normal add-to-basket workflow was checked. No authorization bypass, invalid business-state transition, or checkout behavior was tested.

## Final Assessment

**Informational observation.** The normal basket workflow worked as expected. No insecure design vulnerability was confirmed.
