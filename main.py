import statistic_insights as st

url = 'homicidios.xlsx'
sheet_name = 'Planilha2'

data_xlsx = st.DataStatistic(url, sheet_name)
statistics = data_xlsx.analyze_data()
score_z = data_xlsx.calculate_score_z(2017)
highest_index_value = data_xlsx.finding_highest_index()

print(data_xlsx)
print(f"O Escore Z é {score_z:.2f}")
print(f"O ano com maior índice de violência foi {highest_index_value[0]}, com o valor de {highest_index_value[1]} \n"
      f"Sua distância em relação à média (escore z) de {score_z:.2f}")

