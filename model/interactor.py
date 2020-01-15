import numpy as np
from sklearn.linear_model import LinearRegression

from model.model_analysis import *


class Interactor:
    timeseries = []

    def __init__(self, data_frame_row_list):
        self.timeseries = data_frame_row_list

    def get_model_analysis(self):
        model_analysis = ModelAnalysis()
        model_analysis.properties[TREND] = self.determine_trend()
        model_analysis.properties[SEASON] = self.determine_season()
        model_analysis.properties[OSCILLATION] = self.determine_oscillation()
        model_analysis.properties[SINGLE_ANOMALY] = self.determine_single_anomaly()
        model_analysis.properties[GROUP_ANOMALY] = self.determine_group_anomaly()
        model_analysis.properties[MEAN_VALUE] = self.determine_mean_value()
        model_analysis.properties[LENGTH] = self.determine_length()
        return model_analysis

    def determine_trend(self):
        X = np.array([i for i in range(len(self.timeseries))]).reshape(-1,1)
        y = np.array(self.timeseries).reshape(-1, 1)
        model = LinearRegression().fit(X, y)
        return str(model.coef_[0][0])

    def determine_season(self):
        return ""

    def determine_oscillation(self):
        return ""

    def determine_single_anomaly(self):
        return ""

    def determine_group_anomaly(self):
        return ""

    def determine_mean_value(self):
        return np.mean(self.timeseries)

    def determine_length(self):
        return len(self.timeseries)
