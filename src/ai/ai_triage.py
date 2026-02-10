"""
Module for AI-assisted incident triage and summary.
"""

def summarize_incident(alert, actions):
    """
    Summarizes a security incident for reporting.
    """
    host = alert.get("agent", {}).get("name", "unknown host")
    incident_id = alert.get("id", "unknown id")
    incident_type = alert.get("type", "unknown type")
    severity = alert.get("severity", "unknown severity")

    summary = (
        f"Incident {incident_id} detected on {host}. "
        f"Type: {incident_type}. "
        f"Severity: {severity}. "
        f"Actions executed: {actions}."
    )

    print("AI-generated incident summary created.")
    return summary
