import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def filter(df, filters={}):
    for filter, value in filters.items():
        df = df[df[filter] == value]
    return df

def compute_stats(df):
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
    # Add more stats here if desired
    return df

def scatter_merged(filters=None):
    df = pd.read_csv('../data/merge.csv')
    df = compute_stats(df)
    if filters:
        df = filter(df, filters)
    area = df['Census2019_18PlusPop'] / df['Census2019_18PlusPop'].max() * 1e2
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
    
    # perform regressin
    model = sm.WLS(df[ylabel], sm.add_constant(df[xlabel]), df["Census2019_18PlusPop"])
    p = model.fit().params

    # generate x-values for your regression line (two is sufficient)
    x = np.arange(5, 95)

    # plot regression line on the same axes, set x-axis limits
    ax.plot(x, p.const + p[xlabel] * x)
    plt.show()

