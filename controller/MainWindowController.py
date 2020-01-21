# coding=utf8

import pandas as ps

from model.interactor import Interactor
from model.model_analysis import *


class MainWindowController:
    window = None
    data = None
    model = ModelAnalysis()
    list_model_analysis = []

    def __init__(self, window):
        self.window = window

    def file_chosen(self, file_path):
        self.model = ModelAnalysis()
        print(file_path)
        self.data = ps.read_csv(file_path, index_col=None, header=None, sep="	")
        self.window.fill_ts(self.data)
        for i_row, row in self.data.iterrows():
            for i_col in range(0, len(self.data.columns)):
                self.data[i_col][i_row] = float(self.data[i_col][i_row].replace(",", "."))
        print(self.data.head())
        self.show_graphic()

    def show_graphic(self):
        self.window.show_graphic(self.data)

    def make_analysis(self):

        if self.data is None:
            self.window.show_error("Please, choose file first")
            return
        for i_row, row in self.data.iterrows():
            interactor = Interactor(row.tolist())
            self.list_model_analysis.insert(0, interactor.get_model_analysis())

        self.window.show_properties(self.list_model_analysis)
        self.window.show_taus(Interactor([]).get_kendal_tau(self.list_model_analysis))
