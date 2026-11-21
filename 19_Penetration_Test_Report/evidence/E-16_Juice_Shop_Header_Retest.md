# E-16 – Juice Shop Security Header Retest

**Test date:** 21 November 2026  
**Test time:** 21:57:37 IST (UTC+05:30)  
**Environment:** Authorized local Aegis Shield lab  
**Application:** OWASP Juice Shop  
**Base URL:** http://127.0.0.1:3000

## Test scope

Two HTTP GET requests were made to inspect response headers:

1. Homepage: `http://127.0.0.1:3000/`
2. Product-search API: `http://127.0.0.1:3000/rest/products/search?q=test`

## Observed results

| Header | Homepage | Product-search API |
|---|---|---|
| Access-Control-Allow-Origin | `*` | `*` |
| Content-Security-Policy | Not observed | Not observed |
| Cross-Origin-Embedder-Policy | Not observed | Not observed |
| Cross-Origin-Opener-Policy | Not observed | Not observed |
| X-Content-Type-Options | `nosniff` | `nosniff` |
| X-Frame-Options | `SAMEORIGIN` | `SAMEORIGIN` |

Both requests returned HTTP responses successfully.

## Validation limitations

- Results apply only to the two tested endpoints and the recorded test time.
- Header absence on these responses does not establish that every application route has the same configuration.
- Wildcard CORS alone does not prove sensitive-data exposure or unauthorized access.
- No exploit, credentialed cross-origin access, or security impact was demonstrated.
- CSP, COEP and COOP requirements must be assessed against the application's intended behavior and deployment architecture.

## Related candidate findings

- PT-14 – Wildcard CORS
- PT-15 – Missing Content Security Policy
- PT-16 – Missing Cross-Origin-Embedder-Policy
- PT-17 – Missing Cross-Origin-Opener-Policy

**Evidence status:** Fresh response-header observations recorded; broader validation and impact assessment pending.
