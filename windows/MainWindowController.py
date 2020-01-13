# coding=utf8

from enumeration.fgos import FGOS
import pandas as ps


class MainWindowController:
    window = None
    current_fgos_mode = FGOS.ALWAYS_TRUE
    level = 1
    studentName = ""
    data = None

    def __init__(self, window):
        self.window = window

    def file_chosen(self, file_path):
        print(file_path)
        self.data = ps.read_csv(file_path, index_col=None, header=None, sep="	")
        self.window.fill_ts(self.data)
        # for i, row in self.data.iterrows():
        #     for j in range(len(row)):
        #         self.data[i][j] = float(row[j].replace(",", "."))
        # print(self.data.head())



