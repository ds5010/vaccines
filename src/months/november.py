#Kayne Ryan
#DS5010 Spring 2022
#november.py -- creates and saves scatterplot showing vax/deaths data for Nov 2021

import pandas as pd
import matplotlib.pyplot as plt

def november():
    df_nov = pd.read_csv('data/vaccinations-and-deaths-11-01-2021.csv', converters={'FIPS' : str})
    df_nov['Deaths_Per_1e5'] = df_nov['Deaths'] / df_nov['Census2019_18PlusPop'] * 1e5

    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df_nov[xlabel]
    y = df_nov[ylabel]
    area = df_nov['Census2019_18PlusPop'] / 1e4

    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0,100)
    ax.set_ylim(0,500)
    fig.set_size_inches(8,8)

    scatter = ax.scatter(x, y, s=area, alpha=0.5)

    # produce a legend with a cross section of sizes from the scatter
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
    ax.legend(handles, labels, loc="upper right", title="Population Sizes (x10k)", labelspacing=2, borderpad=1); # Haven't figured out how to make the numbers from the legend different
    plt.savefig('img/nov.png')