# Aegis Shield – Task 15: Incident Response Playbooks and Tabletop Exercise

## 1. Objective

The objective of Task 15 was to prepare incident response playbooks for three serious security scenarios and evaluate the response process through a tabletop exercise.

## 2. Playbooks Created

Three playbooks were created:

1. Payroll Data Breach
   - Location: `playbooks/Payroll_Data_Breach_Playbook.md`
   - Detection mapping: PAY-02 Full Payroll Export and PAY-03 Salary Change Approval Review.

2. Ransomware Incident
   - Location: `playbooks/Ransomware_Incident_Playbook.md`
   - Detection mapping: Related authentication and web indicators can provide context. Task 14 does not contain a dedicated ransomware detection rule.

3. Insider Salary Leak
   - Location: `playbooks/Insider_Salary_Leak_Playbook.md`
   - Detection mapping: PAY-01 Night Salary Access and PAY-03 Salary Change Approval Review.

## 3. Response Procedures

Each playbook documents:
- Detection and initial confirmation.
- Numbered first-30-minute response steps.
- Containment, eradication and recovery responsibilities.
- Internal and external communication responsibilities.
- Evidence preservation requirements.
- Decision points and five tabletop questions.

The playbooks assign incident coordination to the Incident Response Lead. Authorized IT Security personnel carry out approved technical restrictions. The Privacy Officer and Legal Counsel assess notification obligations with management.

## 4. Tabletop Exercise

An AI-assisted tabletop simulation was documented using a fictional payroll incident involving night-time access and a full payroll export.

Five challenging questions and simulated responses were recorded.

Exercise status: AI-assisted simulation completed. A real spoken tabletop exercise with a human participant is still pending. The simulation must not be treated as proof of a completed spoken exercise.

## 5. Proposed Improvements

Five improvement proposals were documented:
1. Define containment approval authority.
2. Improve payroll audit logging.
3. Create a notification approval matrix.
4. Document payroll export authorization.
5. Introduce a timestamped evidence register.

These proposals have been added as draft operational improvements to the three playbooks where relevant.

Status: Proposed and incorporated as draft text; formal validation and approval remain pending.

## 6. Evidence

- `evidence/Tabletop_Evidence.md`
- `tabletop/Tabletop_Exercise_Scenario.md`
- `tabletop/Tabletop_Exercise_Notes.md`
- `tabletop/Improvements.md`
- `playbooks/Payroll_Data_Breach_Playbook.md`
- `playbooks/Ransomware_Incident_Playbook.md`
- `playbooks/Insider_Salary_Leak_Playbook.md`

## 7. References

- OWASP Cheat Sheet Series: https://github.com/OWASP/CheatSheetSeries
- Mermaid: https://github.com/mermaid-js/mermaid

## 8. Limitations

- The tabletop exercise has only been simulated with AI; a real spoken exercise is pending.
- Proposed improvements have not yet been formally approved.
- Task 14 does not provide a dedicated ransomware detection rule.
- Detection alerts are indicators for investigation and do not independently prove a successful breach or malicious activity.

## 9. Completion Checklist

- [x] Three incident response playbooks created.
- [x] Each playbook linked to relevant detection indicators or documented detection gaps.
- [x] First-30-minute response steps documented.
- [x] Notification roles and evidence requirements documented.
- [x] Five tabletop questions and AI-assisted simulation notes recorded.
- [x] Five proposed operational improvements documented.
- [ ] Real spoken tabletop exercise completed with a human participant.
- [ ] Proposed improvements validated and formally approved.
- [ ] Final review and Phase 3 completion confirmed.

## 10. Overall Status

Task 15 documentation is substantially prepared. The real spoken tabletop exercise, formal validation of improvements and final phase review remain outstanding.
