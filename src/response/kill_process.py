"""
Module to kill malicious processes.
"""

def execute(alert):
    """
    Simulate terminating a malicious process.
    """
    alert_id = alert.get("id", "unknown id")
    print(f"[ACTION] Terminating malicious process related to alert {alert_id}")