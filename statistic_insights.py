import pandas as pd
import numpy as np


class DataStatistic:
    def __init__(self, url, sheet_name):
        self.url = url
        self.sheet_name = sheet_name
        self.violence_data = self.reading_file()

    def reading_file(self):
        violence_file = pd.read_excel(self.url, index_col=0, sheet_name=self.sheet_name).squeeze()
        return violence_file

    def analyze_data(self):
        statistics = {
            'mean': self.violence_data.mean(),
            'median': self.violence_data.median(),
            'quartile_25': self.violence_data.quantile(0.25),
            'quartile_50': self.violence_data.quantile(0.50),
            'quartile_75': self.violence_data.quantile(0.75),
            'non_null': self.violence_data.count(),
            'std': self.violence_data.std()
        }
        return statistics

    def calculate_score_z(self, number):
        return (self.violence_data[number] - self.violence_data.mean()) / self.violence_data.std()

# class DataStatistic:
#     def __init__(self, violence_data):
#         self.violence_data = violence_data
#
#     def analyze_data(self):
#         statistics = {
#             'mean': self.violence_data.mean(),
#             'median': self.violence_data.median(),
#             'quartile_25': self.violence_data.quantile(0.25),
#             'quartile_50': self.violence_data.quantile(0.50),
#             'quartile_75': self.violence_data.quantile(0.75),
#             'non_null': self.violence_data.count(),
#             'std': self.violence_data.std()
#         }
#         return statistics
#
#     def calculate_score_z(self, number):
#         return (self.violence_data[number] - self.violence_data.mean()) / self.violence_data.std()
#
#
# class Data:
#     def __init__(self, url, sheet_name):
#         self.url = url
#         self.sheet_name = sheet_name
#
#     def reading_file(self):
#         violence_file = pd.read_excel(self.url, index_col=0, sheet_name=self.sheet_name).squeeze()
#         return violence_file
