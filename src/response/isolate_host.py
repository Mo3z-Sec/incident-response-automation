"""
Module to isolate compromised hosts.
"""

def execute(alert):
    """
    Simulate isolating a compromised host.
    """
    host = alert["agent"]["name"]

    print(f"[ACTION] Isolating host {host} from the network")
