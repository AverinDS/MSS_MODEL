# coding=utf8

import pandas as ps


class MainWindowController:
    window = None
    data = None

    def __init__(self, window):
        self.window = window

    def file_chosen(self, file_path):
        print(file_path)
        self.data = ps.read_csv(file_path, index_col=None, header=None, sep="	")
        self.window.fill_ts(self.data)
        for i_row, row in self.data.iterrows():
            for i_col in range(0, len(self.data.columns)):
                self.data[i_col][i_row] = float(self.data[i_col][i_row].replace(",","."))
        print(self.data.head())
        self.show_graphic()

    def show_graphic(self):
        self.window.show_graphic(self.data)



