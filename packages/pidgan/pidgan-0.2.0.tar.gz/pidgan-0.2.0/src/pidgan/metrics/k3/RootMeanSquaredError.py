import keras as k

from pidgan.metrics.k3.BaseMetric import BaseMetric


class RootMeanSquaredError(BaseMetric):
    def __init__(self, name="rmse", dtype=None):
        super().__init__(name=name, dtype=dtype)
        self._rmse = k.metrics.RootMeanSquaredError(name=name, dtype=dtype)

    def update_state(self, y_true, y_pred, sample_weight=None):
        state = self._rmse(y_true, y_pred, sample_weight=sample_weight)
        self._metric_values.assign(state)
