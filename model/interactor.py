import numpy as np


class Interactor:
    timeseries = []

    def __init__(self, data_frame_row_list):
        self.timeseries = data_frame_row_list

    def determine_trend(self):
        return ""

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
