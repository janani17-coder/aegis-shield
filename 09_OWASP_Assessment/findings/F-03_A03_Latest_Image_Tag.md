# F-03 — Juice Shop Image Uses the `latest` Tag

## Finding Details

- **Finding ID:** F-03
- **Title:** Container image tag is not pinned to a specific release
- **Application:** OWASP Juice Shop — local lab
- **Target:** Local Docker configuration
- **OWASP Category:** A03 — Software Supply Chain Failures
- **Severity:** Low — improvement recommended
- **Status:** Configuration concern observed; vulnerability status not verified

## Summary

The local Docker Compose file specifies `bkimminich/juice-shop:latest`. The local image list also shows the Juice Shop image with the `latest` tag. This makes the selected release less explicit and can reduce reproducibility when the tag points to a different image in the future.

## Scope and Preconditions

- Inspection was restricted to the local Aegis Shield lab.
- The Docker Compose file and local image list were read.
- No image was downloaded, upgraded, or modified as part of this check.

## Steps to Reproduce

1. Open `05_Lab_and_Samples/docker-compose.lab.yml`.
2. Inspect the `juice-shop` service's `image` field.
3. Run the Docker image-list command.
4. Observe that the image is listed as `bkimminich/juice-shop:latest`.

## Expected Result

The lab should use a documented, reproducible application version or an explicitly pinned image digest, with updates reviewed before adoption.

## Actual Result

The configuration uses the mutable `latest` tag. The exact application version and dependency vulnerability status were not verified.

## Evidence

- Configuration: `05_Lab_and_Samples/docker-compose.lab.yml`
- Command output: Docker image list showing `bkimminich/juice-shop:latest`

## Impact

A mutable tag can cause different lab runs to use different software versions, complicating reproducibility and vulnerability tracking. This check does not establish that the current image contains a vulnerability.

## Recommendation

Choose a reviewed, explicit release tag or image digest, document the selected version, and update it through a controlled process. Check the image's provenance and vulnerability information before using it.

## STRIDE Threat Mapping

- **Threat ID:** No direct mapping identified.
- **Mapping type:** No direct match.
- **Rationale:** T-08 concerns users gaining HR/payroll permissions beyond their assigned roles. That threat is not directly related to container image version selection. Although T-30 covers service dependencies, the current test did not establish a compromised dependency or dependency failure. No direct threat in the payroll-focused STRIDE model was demonstrated by this observation.
- **Limitation:** The mutable image tag is a reproducibility and supply-chain management concern; it does not prove that the image is vulnerable or compromised.

## Limitations

Only the configured tag and local image-list entry were inspected. The exact application version, image digest provenance, and known vulnerabilities were not verified.

## Final Assessment

**Configuration improvement recommended.** Pinning and documenting the image version would improve reproducibility. No software supply-chain vulnerability was confirmed by this check.
