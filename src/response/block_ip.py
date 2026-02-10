"""
Module to block malicious IP addresses.
"""

def execute(alert):
    """
    Simulate blocking a malicious source IP.
    """
    src_ip = alert["data"].get("srcip", "unknown")
    host = alert["agent"]["name"]

    print(f"[ACTION] Blocking source IP {src_ip} detected on host {host}")
