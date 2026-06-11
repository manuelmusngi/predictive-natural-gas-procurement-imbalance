from statsmodels.tsa.statespace.sarimax import SARIMAX
import pandas as pd
from typing import List

class ARIMAXForecaster:
    def __init__(self, order=(1, 0, 1), seasonal_order=(0, 0, 0, 0)):
        self.order = order
        self.seasonal_order = seasonal_order
        self.model_ = None

    def fit(self, y: pd.Series, exog: pd.DataFrame):
        self.model_ = SARIMAX(
            y,
            exog=exog,
            order=self.order,
            seasonal_order=self.seasonal_order,
            enforce_stationarity=False,
            enforce_invertibility=False,
        ).fit(disp=False)
        return self

    def forecast(self, exog_future: pd.DataFrame, steps: int):
        return self.model_.forecast(steps=steps, exog=exog_future)
