import numpy as np
import pandas as pd
from lightgbm import LGBMRegressor

class GBMForecaster:
    def __init__(self, **kwargs):
        self.model = LGBMRegressor(
            n_estimators=500,
            learning_rate=0.05,
            max_depth=-1,
            subsample=0.8,
            colsample_bytree=0.8,
            **kwargs,
        )

    def fit(self, X: pd.DataFrame, y: pd.Series):
        self.model.fit(X, y)
        return self

    def predict(self, X_future: pd.DataFrame) -> np.ndarray:
        return self.model.predict(X_future)
