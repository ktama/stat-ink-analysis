import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def plot_table(df):
    plt.figure()
    df.plot()
    plt.savefig('figures/plot.png')
    plt.close('all')
