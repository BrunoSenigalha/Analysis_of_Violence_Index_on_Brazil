import statistics as st
import line_graphic as lg
import boxplot_graphic as bg
import read_file as rf

# url = input("Informe a url da planilha")
# sheet_name = input("Informe o nome da planilha")
url = "homicidios.xlsx"
sheet_name = "Planilha2"
data_file = rf.reading_file(url, sheet_name)
print(data_file.transpose())

print("0 para ver dados estatísticos")
print("1 para gerar um gráfico de linhas")
print("2 para gerar um boxplot")
print("3 Score Z")
option = input()

if option == '0':
    data_statistics = st.DataStatistic(data_file.squeeze())
    print(data_statistics)

elif option == '1':
    lg.generating_graphic(data_file.transpose())

elif option == '2':
    bg.graphic_generator_boxplot(data_file.transpose())

elif option == '3':
    input_score_z = int(input("Informe o valor de Score Z: "))
    score_z = st.calculate_score_z(data_file.squeeze(), input_score_z)
    print(f"Sua distância em relação à média (escore z) de {score_z:.2f}")

else:
    print("Opção não encontrada.")
