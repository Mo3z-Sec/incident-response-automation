"""
Module to isolate compromised hosts.
"""

def execute(alert):
    print(f"Isolating host {alert['host']} from the network")
