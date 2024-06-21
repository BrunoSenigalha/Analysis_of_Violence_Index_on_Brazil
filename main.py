import statistic_insights as st

url = 'homicidios.xlsx'
sheet_name = 'Planilha2'

data_xlsx = st.DataStatistic(url, sheet_name)
statistics = data_xlsx.analyze_data()
score_z = data_xlsx.calculate_score_z(2019)


print(f"A média é {statistics['mean']}")
print(f"O Escore Z é {score_z}")
