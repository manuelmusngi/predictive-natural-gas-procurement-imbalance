import numpy as np

class SimpleEnsembleForecaster:
    def __init__(self, arimax_model, gbm_model, lstm_model, weights=(0.2, 0.4, 0.4)):
        self.arimax = arimax_model
        self.gbm = gbm_model
        self.lstm = lstm_model
        self.weights = np.array(weights) / sum(weights)

    def predict(self, arimax_pred, gbm_pred, lstm_pred):
        preds = np.vstack([arimax_pred, gbm_pred, lstm_pred])
        return (self.weights[:, None] * preds).sum(axis=0)
