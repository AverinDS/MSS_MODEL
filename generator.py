import math, random
import math
import random
import time

import matplotlib.pyplot as plt
from matplotlib import colors
from pandas import DataFrame, Series

colors_list = list(colors._colors_full_map.values())
COUNT_TS = 10
LENGTH_FROM = 10
LENGTH_TO = 120

data = DataFrame(columns=[i for i in range(-3, LENGTH_TO)], index=[i for i in range(COUNT_TS)])


for ts_i in range(COUNT_TS):
    TREND_K = 5 #random.randint(1, 5)
    TREND_B = random.randint(-10, 10)
    SEASON_PERIOD = 1
    SEASON_AMPLITUDE = 55
    ANOMALY_COUNT = 0

    actual_length = random.randint(LENGTH_FROM, LENGTH_TO)
    x = []
    y = []
    y_arr = []

    for i in range(actual_length):
        y_val = TREND_K * i + TREND_B + SEASON_AMPLITUDE * math.sin(i / SEASON_PERIOD) + random.randint(0, 1)

        x.append(i)
        y.append(y_val)

    data.loc[ts_i] = Series(y)
    plt.plot(x, y)


plt.show()
data.to_csv(str(time.time())+".csv", encoding='utf-8', index=False, sep=';', header=None)
print(data.head(COUNT_TS))
