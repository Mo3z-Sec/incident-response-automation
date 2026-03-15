import logging
from ingest.wazuh_client import get_alerts
from classify.playbook_matcher import match_playbook
from response import block_ip, kill_process, isolate_host
from ai.ai_triage import summarize_incident
from reporting.report_generator import generate_report

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger(__name__)

R     = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
CYAN  = "\033[38;5;81m"
GREEN = "\033[38;5;114m"
RED   = "\033[38;5;203m"
AMBER = "\033[38;5;179m"
GRAY  = "\033[38;5;245m"

def sev_color(s):
    return {
        "critical": RED, "high": RED,
        "medium": AMBER, "low": GREEN
    }.get(s.lower(), GRAY)


def main():
    print(f"\n{BOLD}  ir-engine{R}  {GRAY}v0.1.0{R}")
    print(f"{GRAY}  {'─' * 36}{R}\n")

    # load alerts
    print(f"  {CYAN}→{R}  fetch alerts")
    alerts = get_alerts()
    print(f"  {GREEN}✓{R}  {len(alerts)} alert(s) loaded\n")

    # match each alert to a playbook
    print(f"  {CYAN}→{R}  match playbooks")
    matched = [match_playbook(a) for a in alerts]
    print(f"  {GREEN}✓{R}  {len(matched)} matched\n")

    print(f"  {CYAN}→{R}  respond + triage")
    summaries = []

    for alert, playbook in zip(alerts, matched):
        aid      = alert.get("id", "?")
        host     = alert.get("agent", {}).get("name", "unknown")
        severity = alert.get("severity", "unknown")
        sc       = sev_color(severity)

        print(f"\n  {BOLD}{aid}{R}  {host}  {sc}{severity}{R}")

        try:
            actions = playbook["actions"]

            if "block_ip"     in actions: block_ip.execute(alert)
            if "kill_process" in actions: kill_process.execute(alert)
            if "isolate_host" in actions: isolate_host.execute(alert)

            summary = summarize_incident(alert, actions)
            summaries.append(summary)
            print(f"  {GRAY}·{R}  summary ready")

        except Exception as e:
            log.error("failed on %s — %s", aid, e)
            summaries.append("error")
            print(f"  {RED}✗{R}  {e}")

    # write reports
    print(f"\n  {CYAN}→{R}  generate reports")
    for alert, playbook, summary in zip(alerts, matched, summaries):
        generate_report(alert, actions=playbook["actions"], summary=summary)
        print(f"  {GREEN}✓{R}  {GRAY}{alert.get('id')}{R}")

    print(f"\n{GRAY}  {'─' * 36}")
    print(f"  done  —  {len(alerts)} alerts  {len(summaries)} reports{R}\n")


if __name__ == "__main__":
    main()