# Automated IR Playbook System

## Overview
The **Automated IR Playbook System** is a Python-based security automation tool designed to simulate a mini Security Operations Center (SOC).  
It connects to **Wazuh**, a free SIEM, to collect alerts from monitored endpoints and automatically executes **predefined incident response playbooks**.  

An optional **AI module** can summarize incidents and generate human-readable reports, making analysis faster and more understandable.  

**Key feature:** Fully executable from the bash terminal with a single command (`./run_ir.sh`), so anyone can clone the repo and test it.

---

## How It Works (High-Level)
1. **Detection:** Wazuh Agent monitors endpoints and generates alerts (e.g., SSH brute-force, malware).  
2. **Alert Ingestion:** Python IR Engine pulls alerts via Wazuh API.  
3. **Playbook Matching:** YAML-based rules determine which actions to take.  
4. **Automated Response:** Python executes actions such as blocking IPs, killing processes, or isolating hosts.  
5. **AI-Assisted Triage:** Optional module generates human-readable summaries of incidents.  
6. **Reporting:** Detailed audit-ready reports saved in `/reports/`.  

**Architecture Diagram:**  
![Architecture Diagram](docs/architecture/architecture_v1.png)

---

## Core Components
| Component | Role |
|-----------|------|
| Wazuh | SIEM for alert detection |
| Python IR Engine | Automates ingestion, playbook matching, actions |
| Playbooks (YAML) | Define incident rules |
| AI Module | Generates summaries and incident reports |
| Bash Script (`run_ir.sh`) | Launches system with one command |
| Docker Compose | Spins up Wazuh + Elastic containers |

---

## Technologies Used
- Python 3.11  
- Docker & Docker Compose  
- Wazuh SIEM  
- YAML (playbooks)  
- AI (OpenAI GPT or optional local models)  
- Bash (one-command execution)  

---
