import matplotlib.pyplot as plt


def graphic_generator_boxplot(file_data):
    plt.figure(figsize=(7, 8))
    plt.boxplot(file_data, tick_labels=['Homocídios'])
    plt.title("Taxa de Homicídios no Brasil")
    plt.ylabel("Taxa de Homicídios por ano")
    plt.grid(axis="y")
    plt.show()
