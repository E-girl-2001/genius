import matplotlib.pyplot as plt


def plot_drinks(names, dolars_per_standard):
    """plot a graph of the data"""
    plt.bar(names, dolars_per_standard)
    plt.xticks()
    plt.ylabel("Dolars Per Standard")
    plt.title("Dolars Per Standard of Different Drinks")
    plt.show()