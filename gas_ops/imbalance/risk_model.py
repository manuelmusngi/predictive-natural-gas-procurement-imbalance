import pandas as pd
import numpy as np
from lightgbm import LGBMClassifier

IMB_FEATURES = [
    "scheduled_receipts_mmbtu",
    "scheduled_deliveries_mmbtu",
    "actual_flows_mmbtu",
    "linepack_mmbtu",
    "temp_f", "hdd", "cdd",
    "rt_power_mw", "da_power_mw",
    "constraint_flag",
]

class ImbalanceRiskModel:
    def __init__(self, **kwargs):
        self.model = LGBMClassifier(
            n_estimators=400,
            learning_rate=0.05,
            max_depth=-1,
            subsample=0.8,
            colsample_bytree=0.8,
            **kwargs,
        )

    def fit(self, df: pd.DataFrame, target_col: str = "risk_class"):
        X = df[IMB_FEATURES]
        y = df[target_col]
        self.model.fit(X, y)
        return self

    def predict_proba(self, df: pd.DataFrame) -> np.ndarray:
        X = df[IMB_FEATURES]
        return self.model.predict_proba(X)

    def predict(self, df: pd.DataFrame) -> np.ndarray:
        X = df[IMB_FEATURES]
        return self.model.predict(X)
