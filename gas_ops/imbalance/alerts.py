from typing import List, Dict

def map_alert_to_actions(alert: Dict) -> List[str]:
    severity = alert["severity"]
    actions = []

    if severity == "HIGH":
        actions.append("Check latest gas burn forecast vs scheduled quantities.")
        actions.append("Evaluate intra-day re-nominations on affected pipeline.")
        actions.append("Explore locational swaps or imbalance trades if available.")
    elif severity == "MEDIUM":
        actions.append("Tighten monitoring of gas burn vs schedule.")
        actions.append("Prepare potential re-nomination scenarios.")
    else:
        actions.append("No immediate action; continue monitoring.")

    return actions
