import numpy as np
import pandas as pd
from typing import List, Dict

class ImbalanceRulesEngine:
    def __init__(
        self,
        high_risk_threshold: float = 0.7,
        medium_risk_threshold: float = 0.4,
    ):
        self.high_risk_threshold = high_risk_threshold
        self.medium_risk_threshold = medium_risk_threshold

    def evaluate(
        self,
        df: pd.DataFrame,
        risk_proba: np.ndarray,
    ) -> List[Dict]:
        alerts = []
        # assume risk_proba[:, 2] is "high" class probability
        high_p = risk_proba[:, 2]

        for i, row in df.iterrows():
            p = high_p[i]
            if p >= self.high_risk_threshold:
                alerts.append({
                    "timestamp": row["timestamp"],
                    "pipeline_id": row["pipeline_id"],
                    "node_id": row["node_id"],
                    "severity": "HIGH",
                    "action": "REVIEW_NOMINATIONS_AND_CONSIDER_TRADES",
                    "details": f"High imbalance risk (p={p:.2f}) near limit.",
                })
            elif p >= self.medium_risk_threshold:
                alerts.append({
                    "timestamp": row["timestamp"],
                    "pipeline_id": row["pipeline_id"],
                    "node_id": row["node_id"],
                    "severity": "MEDIUM",
                    "action": "MONITOR_AND_PREPARE_RENOMINATIONS",
                    "details": f"Medium imbalance risk (p={p:.2f}).",
                })
        return alerts
