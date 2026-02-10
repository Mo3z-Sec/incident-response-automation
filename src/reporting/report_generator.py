"""
Module to generate reports for incidents.
"""

def generate_report(alert, actions, summary):
    print(f"Generating report for incident {alert['id']}")
    print("Report content:")
    print(summary)
