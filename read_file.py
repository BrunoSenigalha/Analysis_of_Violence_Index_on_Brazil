import pandas as pd


def reading_file(url, sheet_name):
    file_data = pd.read_excel(url, index_col=0, sheet_name=sheet_name)
    return file_data
