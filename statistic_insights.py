import pandas as pd


class DataStatistic:
    def __init__(self, url, sheet_name):
        self.url = url
        self.sheet_name = sheet_name
        self.violence_data = self.reading_file()
        self.statistics = self.analyze_data()

    def reading_file(self):
        violence_data = pd.read_excel(self.url, index_col=0, sheet_name=self.sheet_name).squeeze()
        return violence_data

    def analyze_data(self):
        statistics = {
            'mean': self.violence_data.mean(),
            'median': self.violence_data.median(),
            'Q1': self.violence_data.quantile(0.25),
            'Q2': self.violence_data.quantile(0.50),
            'Q3': self.violence_data.quantile(0.75),
            'std': self.violence_data.std()
        }
        return statistics

    def calculate_score_z(self, number):
        return (self.violence_data[number] - self.violence_data.mean()) / self.violence_data.std()

    def finding_highest_index(self):
        index = self.violence_data.idxmax()
        value = self.violence_data.max()
        return [index, value]

    def outlier(self):
        diq = self.statistics['Q3'] - self.statistics['Q1']
        lower_bound = self.statistics['Q1'] - 1.5 * diq
        upper_bound = self.statistics['Q3'] + 1.5 * diq
        outliers = [bound for bound in self.violence_data if bound < lower_bound or bound > upper_bound]

        return f"Não há outliers" if not outliers else f"Outliers:{outliers}"

    def __str__(self):
        return (f"Média: {self.statistics['mean']:.2f} \n"
                f"Mediana: {self.statistics['median']:.2f} \n"
                f"Primeiro Quartil: {self.statistics['Q1']:.2f} \n"
                f"Segundo Quartil: {self.statistics['Q2']:.2f} \n"
                f"Terceiro Quartil: {self.statistics['Q3']:.2f} \n"
                f"Desvio Padrão: {self.statistics['std']:.2f}")
