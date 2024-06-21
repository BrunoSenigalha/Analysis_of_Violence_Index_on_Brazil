import pandas as pd


class Statistic:
    def __init__(self, url, sheet_name):
        self.url = url
        self.sheet_name = sheet_name

    def reading_file(self):
        violence_file = pd.read_excel(self.url, index_col=0, sheet_name=self.sheet_name).squeeze()
        return violence_file

