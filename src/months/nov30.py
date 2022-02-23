#Kayne Ryan
#DS5010 Spring 2022
#nov30.py -- creates and saves scatterplot showing vax/deaths data for Nov30 2021

import pandas as pd
import matplotlib.pyplot as plt

def nov30():
    df_nov30 = pd.read_csv('data/vaccinations-and-deaths-11-30-2021', converters={'FIPS' : str})
    df_nov30['Deaths_Per_1e5'] = df_nov30['Deaths'] / df_nov30['Census2019_18PlusPop'] * 1e5

    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df_nov30[xlabel]
    y = df_nov30[ylabel]
    area = df_nov30['Census2019_18PlusPop'] / 1e4

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
    plt.savefig('nov30.jpg')