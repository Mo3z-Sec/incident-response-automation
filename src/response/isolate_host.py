"""
Module to isolate compromised hosts.
"""

def execute(alert):
    """
    Simulate isolating a compromised host.
    """
    host = alert.get("agent", {}).get("name", "unknown host")

    print(f"[ACTION] Isolating host {host} from the network")
