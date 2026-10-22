# Aegis Shield — Isolated Security Lab Setup Guide

## 1. Purpose
This guide explains how to build and use a local cybersecurity practice lab safely on Windows.

## 2. Requirements
- Windows computer
- Docker Desktop
- OWASP Juice Shop
- DVWA
- OWASP ZAP
- Burp Suite Community Edition
- Nmap

## 3. Start the Lab
1. Start Docker Desktop and wait until it is running.
2. Open PowerShell in the Aegis Shield repository folder.
3. Review `05_Lab_and_Samples/LAB_RULES.md`.
4. Start both applications:

```powershell
docker compose -f .\05_Lab_and_Samples\docker-compose.lab.yml up -d
```

5. Check container status:

```powershell
docker compose -f .\05_Lab_and_Samples\docker-compose.lab.yml ps
```

Both containers should show a running status.

## 4. Open the Applications
- Juice Shop: http://127.0.0.1:3000
- DVWA: http://127.0.0.1:8081

For a fresh DVWA setup, open its setup page and use the local application's database setup option if needed.

## 5. Security Tools
- Open OWASP ZAP.
- Open Burp Suite Community Edition.
- Verify Nmap in PowerShell with `nmap --version`.

Use these tools only against the local lab applications or other explicitly authorized targets. Do not scan the whole network.

## 6. Verify Isolation
1. Confirm the Docker port mappings use `127.0.0.1`.
2. From another device on the same Wi-Fi, test the laptop's network address on ports 3000 and 8081.
3. Save genuine screenshots of the Docker port mappings and the failed phone connection attempts.
4. Record the test date and results in `evidence/lab_privacy_test.md`.

A failed connection from one device is useful evidence, but it does not prove every possible network path is blocked.

## 7. Stop the Lab
When finished, run:

```powershell
docker compose -f .\05_Lab_and_Samples\docker-compose.lab.yml down
```

## 8. Rebuild Checklist
For a fresh setup:
1. Install and start Docker Desktop.
2. Clone or open the Aegis Shield repository.
3. Review `LAB_RULES.md`.
4. Start the lab with the Docker Compose command above.
5. Verify both containers are running.
6. Open both local application URLs.
7. Open ZAP and Burp Suite.
8. Verify Nmap with `nmap --version`.
9. Confirm loopback-only port mappings before testing.

## 9. Responsible Testing
Use fictional data only. Record findings with the affected location, reproduction steps, impact, and recommended fix. Stop testing if a tool attempts to target systems outside the authorized lab.