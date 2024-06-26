import pandas as pd


class DataStatistic:
    def __init__(self, file_data):
        self.file_data = file_data
        self.statistics_data = self.analyze_data()
        self.highest_score_value = self.finding_highest_score()
        self.outlier_result = self.outlier()

    def analyze_data(self):
        statistics = {
            'mean': self.file_data.mean(),
            'median': self.file_data.median(),
            'Q1': self.file_data.quantile(0.25),
            'Q2': self.file_data.quantile(0.50),
            'Q3': self.file_data.quantile(0.75),
            'std': self.file_data.std()
        }
        return statistics

    def finding_highest_score(self):
        index = self.file_data.idxmax()
        value = self.file_data.max()
        return [index, value]

    def outlier(self):
        diq = self.statistics_data['Q3'] - self.statistics_data['Q1']
        lower_bound = self.statistics_data['Q1'] - 1.5 * diq
        upper_bound = self.statistics_data['Q3'] + 1.5 * diq
        outliers = [bound for bound in self.file_data if bound < lower_bound or bound > upper_bound]

        return f"Não há outliers" if not outliers else f"Outliers:{outliers}"

    def __str__(self):
        return (f"Média: {self.statistics_data['mean']:.2f} \n"
                f"Mediana: {self.statistics_data['median']:.2f} \n"
                f"Primeiro Quartil: {self.statistics_data['Q1']:.2f} \n"
                f"Segundo Quartil: {self.statistics_data['Q2']:.2f} \n"
                f"Terceiro Quartil: {self.statistics_data['Q3']:.2f} \n"
                f"Desvio Padrão: {self.statistics_data['std']:.2f} \n"
                f"O ano com maior índice de violência foi {self.highest_score_value[0]}, com o valor de "
                f"{self.highest_score_value[1]} \n"
                f"{self.outlier_result}")


def calculate_score_z(file_data, number):
    return (file_data[number] - file_data.mean()) / file_data.std()
