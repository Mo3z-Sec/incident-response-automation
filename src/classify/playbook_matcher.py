"""
Module to match alerts with predefined YAML playbooks.
"""

def match_playbook(alert):
    """
    Match an alert to a playbook.
    """
    print(f"Classifying alert {alert['id']} ({alert['type']})")

    playbook = {
        "incident_type": alert["type"],
        "actions": ["block_ip", "generate_report"]
    }

    print(f"Playbook matched: {playbook['incident_type']}")
    return playbook
