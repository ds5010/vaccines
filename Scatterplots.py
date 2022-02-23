# Scatterplot 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Scatterplot(DATA):
    df = pd.read_csv(DATA, converters={'FIPS' : str})
    df['Vaccination%'] = df['Series_Complete_18PlusPop_Pct']
    df['Population'] = df['Census2019_18PlusPop']
    df['Deaths_per_1k'] = (df['Deaths']/df['Population'])*1000
    df['Population_adjusted'] = df['Population']/1000

    xlabel = 'Vaccination%'
    ylabel = 'Deaths_per_1k'

    x = df[xlabel]
    y = df[ylabel]
    area = df['Population'] / 10000

    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0,100)
    ax.set_ylim(0,6)
    fig.set_size_inches(12,12)

    scatter = ax.scatter(x, y, s=area, alpha=.6)

    handles, labels = scatter.legend_elements(prop='sizes', alpha=0.4, num='auto')
    ax.legend(handles, labels, loc="upper right", title="Population Sizes (x10k)", labelspacing=2, borderpad=1)
    return scatter