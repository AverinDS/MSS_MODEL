from datetime import datetime

import numpy as np
import pandas as ps
from dateutil.relativedelta import relativedelta
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose

from model.model_analysis import *


class Interactor:
    timeseries = []
    k = None
    timeseries_without_trend = []
    decomposition = None
    x = []

    def __init__(self, data_frame_row_list):
        self.timeseries = data_frame_row_list
        self.x = (
            [ps.to_datetime(datetime.today() + relativedelta(months=i)) for i in range(1, len(self.timeseries) + 1)])

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
        X = np.array([i for i in range(len(self.timeseries))]).reshape(-1, 1)
        y = np.array(self.timeseries).reshape(-1, 1)
        model = LinearRegression().fit(X, y)
        self.delete_trend(k=model.coef_[0][0])
        return str(model.coef_[0][0])

    def determine_season(self):
        self.make_decomposition()
        season = self.decomposition.seasonal
        return str((season.max() - season.min())[0] * 0.03 > len(self.timeseries))

    def determine_oscillation(self):
        self.make_decomposition()
        resid = self.decomposition.resid
        return str((resid.max() - resid.min())[0] * 0.03 > len(self.timeseries))

    def determine_single_anomaly(self):
        return ""

    def determine_group_anomaly(self):
        return ""

    def determine_mean_value(self):
        return str(np.mean(self.timeseries))

    def determine_length(self):
        return str(len(self.timeseries))

    def delete_trend(self, k):
        self.timeseries_without_trend = []
        for i in range(0, len(self.timeseries)):
            self.timeseries_without_trend.append(self.timeseries[i] - k * i)

        # print(self.timeseries_without_trend)
        # plt.plot(self.timeseries)
        # plt.plot(self.timeseries_without_trend)
        # plt.show()

    def make_decomposition(self):
        if self.decomposition is not None:
            print("Decomposition already made")
            return
        data = DataFrame(self.timeseries_without_trend, index=self.x)
        data.head()
        self.decomposition = seasonal_decompose(data, freq=1, model='additive')
        # resplot = self.decomposition.plot()
        # resplot.show()
