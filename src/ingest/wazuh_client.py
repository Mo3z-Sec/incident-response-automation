import json
import os

# Absolute path to ensure script works from anywhere
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ALERTS_PATH = os.path.join(BASE_DIR, "data", "alerts")

def get_alerts():
    """
    Loads all alerts from the ALERTS_PATH folder.
    Skips any files that are not valid JSON.
    Returns a list of alert dictionaries.
    """
    alerts = []
    print("Loading alerts from data/alerts ...")

    for file in os.listdir(ALERTS_PATH):
        if not file.endswith(".json"):
            continue

        file_path = os.path.join(ALERTS_PATH, file)
        try:
            with open(file_path, "r") as f:
                content = f.read().strip()
                if not content:
                    print(f"[WARN] Skipping empty file: {file}")
                    continue
                alert = json.loads(content)
                alerts.append(alert)
        except json.JSONDecodeError:
            print(f"[WARN] Skipping invalid JSON file: {file}")

    print(f"Loaded {len(alerts)} alert(s).")
    return alerts
if __name__ == "__main__":
    alerts = get_alerts()
    print(alerts)
