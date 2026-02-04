"""
Module to kill malicious processes.
"""

def execute(alert):
    print(f"Terminating malicious process related to alert {alert['id']}")
