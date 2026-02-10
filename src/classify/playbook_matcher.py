import yaml
import os

# Path to your playbooks folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PLAYBOOKS_PATH = os.path.join(BASE_DIR, "playbooks")

def load_playbooks():
    """
    Load all YAML playbooks from the playbooks directory.
    Skips empty or invalid YAML files.
    """
    playbooks = []
    for file in os.listdir(PLAYBOOKS_PATH):
        if not file.endswith(".yaml"):
            continue
        path = os.path.join(PLAYBOOKS_PATH, file)
        try:
            with open(path, "r") as f:
                playbook = yaml.safe_load(f)
                if playbook is None:
                    print(f"[WARN] Playbook is empty: {file}")
                    continue
                playbooks.append(playbook)
        except yaml.YAMLError:
            print(f"[WARN] Failed to load playbook: {file}")
    return playbooks

# Preload playbooks once at module import
ALL_PLAYBOOKS = load_playbooks()

def match_playbook(alert):
    """
    Match a single alert to the appropriate playbook.
    Returns a dict with 'name' and 'actions'.
    """
    rule_desc = alert.get("rule", {}).get("description", "").lower()

    for pb in ALL_PLAYBOOKS:
        keywords = pb.get("keywords", [])
        if any(kw.lower() in rule_desc for kw in keywords):
            return pb

    # Default if no playbook matches
    return {"name": "default", "actions": []}
