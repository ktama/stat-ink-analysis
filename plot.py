import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_table(df, file_name):
    plt.figure()
    df.plot()
    plt.savefig('figures/' + file_name + '.png')
    plt.close('all')
