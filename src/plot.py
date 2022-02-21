import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def scatter_merged():
    df = pd.read_csv('../data/merge.csv')
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
    area = df['Census2019_18PlusPop'] / 1e4
    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df[xlabel]
    y = df[ylabel]

    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0,100)
    ax.set_ylim(0,500)

    scatter = ax.scatter(x, y, s=area, alpha=0.25)

    # produce a legend with a cross section of sizes from the scatter
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
    ax.legend(handles, labels, loc="upper right", title="Population Sizes (x10k)");

    plt.show()

