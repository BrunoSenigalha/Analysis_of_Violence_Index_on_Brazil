import matplotlib.pyplot as plt


def generating_graphic(file_data):
    plt.figure(figsize=(15, 10))
    plt.style.use('_classic_test_patch')
    plt.plot(file_data, marker='o')
    plt.annotate('Ano do Desarmamento', color='red', xy=(2003, 30.0), xytext=(2002, 29.7))
    plt.title("Taxa de Homicídio no Brasil")
    plt.ylabel("Taxa de Homicídio")
    plt.xlabel("Anos")
    plt.xlim([1980, 2021])
    plt.xticks(file_data.index, rotation=45)
    plt.grid()
    plt.show()
