# coding=utf8
#
TREND = 'trend'
SEASON = 'season'
OSCILLATION = 'oscillation'
SINGLE_ANOMALY = 'single_anomaly'
GROUP_ANOMALY = 'group_anomaly'
MEAN_VALUE = 'mean_value'
LENGTH = 'length'

fields = [TREND, SEASON, OSCILLATION, SINGLE_ANOMALY, GROUP_ANOMALY, MEAN_VALUE, LENGTH]

propertiesDicIndex = {
    TREND: 0,
    SEASON: 1,
    OSCILLATION: 2,
    SINGLE_ANOMALY: 3,
    GROUP_ANOMALY: 4,
    MEAN_VALUE: 5,
    LENGTH: 6,
}


class ModelAnalysis:
    TREND = "Not determined"
    SEASON = "Not determined"
    OSCILLATION = "Not determined"
    SINGLE_ANOMALY = "Not determined"
    GROUP_ANOMALY = "Not determined"
    MEAN_VALUE = "Not determined"
    LENGTH = "Not determined"
    INDEX = -1

    def get_property(self, index):
        if index == 0: return self.TREND
        if index == 1: return self.SEASON
        if index == 2: return self.OSCILLATION
        if index == 3: return self.SINGLE_ANOMALY
        if index == 4: return self.GROUP_ANOMALY
        if index == 5: return self.MEAN_VALUE
        if index == 6: return self.LENGTH
