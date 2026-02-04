"""
Main IR Engine
Coordinates ingestion, playbook matching, automated responses, AI summaries, and reporting.
"""

import time
from ingest.wazuh_client import get_alerts
from classify.playbook_matcher import match_playbook
from response import block_ip, kill_process, isolate_host
from ai.ai_triage import summarize_incident
from reporting.report_generator import generate_report

def main():
    """
    Entry point for the IR Engine.
    Shows professional terminal output with loading messages.
    """

    print("="*60)
    print("Automated IR Playbook System — Starting...")
    print("="*60)
    time.sleep(1)

    # Step 1: Fetch alerts
    print("\n[1/5] Fetching alerts from Wazuh...")
    alerts = get_alerts()
    time.sleep(1)
    print(f"Found {len(alerts)} alerts.\n")

    # Step 2: Match alerts with playbooks
    print("[2/5] Matching alerts to playbooks...")
    matched = [match_playbook(alert) for alert in alerts]
    time.sleep(1)
    print(f"Matched {len(matched)} playbooks.\n")

    # Step 3: Execute responses
    print("[3/5] Executing automated responses...")
    for alert, playbook in zip(alerts, matched):
        if "block_ip" in playbook["actions"]:
            block_ip.execute(alert)
        if "kill_process" in playbook["actions"]:
            kill_process.execute(alert)
        if "isolate_host" in playbook["actions"]:
            isolate_host.execute(alert)
    time.sleep(1)
    print("Responses executed.\n")

    # Step 4: AI triage
    print("[4/5] Summarizing incidents with AI...")
    summaries = []
    for alert, playbook in zip(alerts, matched):
        summary = summarize_incident(alert, playbook["actions"])
        summaries.append(summary)
    time.sleep(1)
    print("AI summaries completed.\n")

    # Step 5: Generate reports
    print("[5/5] Generating reports...")
    for alert, summary in zip(alerts, summaries):
        generate_report(alert, actions={}, summary=summary)
    time.sleep(1)
    print("Reports generated.\n")

    print("="*60)
    print("Automated IR Playbook System — Completed Successfully!")
    print("="*60)


if __name__ == "__main__":
    main()
