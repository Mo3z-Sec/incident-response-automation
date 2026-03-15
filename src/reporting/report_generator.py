"""
Module to generate and save reports for incidents.
"""

import os
import json

REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "reports")

def generate_report(alert, actions, summary):
    os.makedirs(REPORTS_DIR, exist_ok=True)

    report = {
        "id": alert.get("id"),
        "type": alert.get("type"),
        "severity": alert.get("severity"),
        "host": alert.get("agent", {}).get("name"),
        "actions_taken": actions,
        "summary": summary
    }

    filename = f"report_{alert.get('id', 'unknown')}.json"
    path = os.path.join(REPORTS_DIR, filename)

    with open(path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"Report saved: reports/{filename}")