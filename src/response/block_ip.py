"""
Module to block malicious IP addresses.
"""

def execute(alert):
    print(f"Blocking IP address {alert['source_ip']} on host {alert['host']}")
