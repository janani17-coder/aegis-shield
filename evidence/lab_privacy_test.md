# Task 4 — Lab Privacy Test

**Date:** 22 October 2026

## Purpose
Verify that the local security lab is not reachable from another device on the same Wi-Fi network.

## Configuration evidence
Docker Compose showed these port mappings:

- Juice Shop: `127.0.0.1:3000->3000/tcp`
- DVWA: `127.0.0.1:8081->80/tcp`

## Test performed
From a phone connected to the same Wi-Fi network, I attempted to open the following laptop addresses:

- `http://172.19.73.205:3000` — did not open
- `http://172.19.73.205:8081` — did not open

## Result
Both applications were blocked from the phone. This is consistent with the services being bound to localhost only.

## Evidence
- `lab_localhost_ports.png` — Docker port mappings
- Capture a screenshot of the phone's failed connection attempts and save it as `lab_phone_blocked.png`.

## Limitation
The phone test confirms that the applications did not open from that device during this test. It does not independently prove that every possible network path is blocked.