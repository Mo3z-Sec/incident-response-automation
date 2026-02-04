"""
Module for AI-assisted incident triage and summary.
"""

def summarize_incident(alert, actions):
    summary = (
        f"Incident {alert['id']} detected on {alert['host']}. "
        f"Type: {alert['type']}. "
        f"Severity: {alert['severity']}. "
        f"Actions executed: {actions}."
    )

    print("AI-generated incident summary created.")
    return summary
