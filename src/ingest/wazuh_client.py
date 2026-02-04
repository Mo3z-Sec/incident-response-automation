"""
Module to pull alerts from Wazuh SIEM.
"""

def get_alerts():
    """
    Fetch alerts from Wazuh API.
    Currently returns mock alerts for testing.
    """
    print("Connecting to Wazuh API...")
    
    # Mock alert for testing
    alerts = [
        {
            "id": "ALERT-001",
            "type": "ssh_bruteforce",
            "source_ip": "192.168.1.50",
            "host": "kali-test",
            "severity": "high"
        }
    ]

    print("Alerts successfully retrieved.")
    return alerts
