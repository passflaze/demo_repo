import matplotlib.pyplot as plt


def plot_lists(x, y, nameX='X', nameY='Y'):
    if len(x) != len(y):
        raise ValueError("Lists need to be of the same length")
    idx = range(int(len(x)))
    plt.plot(idx, x, y)
    plt.title('Plot of ' + nameY + ' vs ' + nameX)
    plt.grid(True)
    plt.legend([nameX, nameY])
    plt.show()
    pass
