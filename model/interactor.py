import random
from datetime import datetime

import matplotlib.colors as colors
import numpy as np
import pandas as ps
from dateutil.relativedelta import relativedelta
from pandas import DataFrame
from scipy import stats
from scipy.spatial import distance
from sklearn.cluster import DBSCAN
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose

from model.model_analysis import *

colors_list = list(colors._colors_full_map.values())


class Interactor:
    timeseries = []
    k = None
    timeseries_without_trend = []
    decomposition = None
    x = []
    db = None
    isClustering = False

    def __init__(self, data_frame_row_list):
        self.timeseries = data_frame_row_list
        self.x = (
            [ps.to_datetime(datetime.today() + relativedelta(months=i)) for i in range(1, len(self.timeseries) + 1)])

    def get_model_analysis(self):
        model_analysis = ModelAnalysis()
        model_analysis.TREND = self.determine_trend()
        model_analysis.SEASON = self.determine_season()
        model_analysis.OSCILLATION = self.determine_oscillation()
        count_single_a, count_group_a = self.determine_anomaly()
        model_analysis.SINGLE_ANOMALY = count_single_a
        model_analysis.GROUP_ANOMALY = count_group_a
        model_analysis.MEAN_VALUE = self.determine_mean_value()
        model_analysis.LENGTH = self.determine_length()
        model_analysis.index = random.randint(0, 10000)
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

    def determine_anomaly(self):
        x = np.array([i for i in range(0, len(self.timeseries_without_trend))])  # .reshape(-1,1)
        y = np.array(self.timeseries_without_trend)  # .reshape(-1, 1)
        data = []

        for i in range(len(x)):
            data.append(np.array([x[i], y[i]]))

        data = np.array(data)

        euclidians = []
        for index in range(1, len(data)):
            euclidians.append(
                distance.euclidean(
                    (data[index][0], data[index][1])
                    , (data[index - 1][0], data[index - 1][1])
                )
            )
        euclidians = np.mean(euclidians)

        self.db = DBSCAN(eps=euclidians, min_samples=1)
        self.db.fit(data)

        n_clusters_ = len(set(self.db.labels_))  # - (1 if -1 in clust.labels_ else 0)
        clusters_dict = {i: np.where(self.db.labels_ == i)[0] for i in range(-1, n_clusters_)}
        # import matplotlib.pyplot as plt
        # for key in clusters_dict.keys():
        #     for i in clusters_dict[key]:
        #         if key == -1:
        #             plt.scatter(i, y[i], c='black',
        #                         label='cluster' + str(key))
        #         else:
        #             plt.scatter(i, y[i], c=colors_list[key],
        #                         label='cluster' + str(key))
        #
        # plt.show()
        count_single = 0
        count_group = 0
        max_key_group = -1

        for key in clusters_dict.keys():
            if max_key_group == -1 or len(clusters_dict[key]) > len(clusters_dict[max_key_group]):
                max_key_group = key

        for key in clusters_dict.keys():
            if len(clusters_dict[key]) == 1:
                count_single += 1
            elif key != max_key_group and len(clusters_dict[key]) > 0:
                count_group += 1

        return str(count_single), str(count_group)

    def determine_mean_value(self):
        return str(np.mean(self.timeseries))

    def determine_length(self):
        return str(len(self.timeseries))

    def delete_trend(self, k):
        self.timeseries_without_trend = []
        for i in range(0, len(self.timeseries)):
            self.timeseries_without_trend.append(self.timeseries[i] - k * i)

        # import matplotlib.pyplot as plt
        # plt.plot(self.timeseries)
        # plt.plot(self.timeseries_without_trend)
        # plt.show()
        # print(self.timeseries_without_trend)


    def make_decomposition(self):
        if self.decomposition is not None:
            print("Decomposition already made")
            return
        data = DataFrame(self.timeseries_without_trend, index=self.x)
        data.head()
        self.decomposition = seasonal_decompose(data, freq=1, model='additive')
        # resplot = self.decomposition.plot()
        # resplot.show()

    def get_kendal_tau(self, list_models):
        taus = []

        for key in propertiesDicIndex:
            property_correllations = []
            for model in list_models:
                if model.get_property(propertiesDicIndex[key]) == "True":
                    property_correllations.append(1)
                elif model.get_property(propertiesDicIndex[key]) == "False":
                    property_correllations.append(0)
                else:
                    property_correllations.append(float(model.get_property(propertiesDicIndex[key])))

            taus.append(str(stats.kendalltau([i for i in range(len(list_models))], property_correllations).correlation))
        return taus
