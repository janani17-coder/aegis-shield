# E-17 – Additional Juice Shop Security Header Review

**Test date:** 21 November 2026
**Environment:** Authorized local Aegis Shield lab
**Application:** OWASP Juice Shop
**Base URL:** http://127.0.0.1:3000

## Scope and results

Three additional public routes were checked using HTTP HEAD requests:

| Route | HTTP status | CORS | CSP | COEP | COOP | X-Content-Type-Options | X-Frame-Options |
|---|---:|---|---|---|---|---|---|
| `/` | 200 | `*` | Not observed | Not observed | Not observed | `nosniff` | `SAMEORIGIN` |
| `/robots.txt` | 200 | `*` | Not observed | Not observed | Not observed | `nosniff` | `SAMEORIGIN` |
| `/assets/public/images/JuiceShop_Logo.png` | 200 | `*` | Not observed | Not observed | Not observed | `nosniff` | `SAMEORIGIN` |

## Limitations

- This review used HTTP HEAD requests and covered only the three listed public routes.
- Results apply to the local Juice Shop instance and test time.
- The observations do not establish behavior on all routes or deployment configurations.
- Wildcard CORS does not by itself prove sensitive-data exposure or unauthorized access.
- No exploit or security impact was demonstrated.

**Evidence status:** Additional public-route header observations recorded. Broader validation and impact assessment remain pending.
