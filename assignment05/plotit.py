from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plotit():
    df = pd.read_csv('data/vaccinations-and-confirmed-11-30-2021.csv')
    df['Vaccination_Pop_Per_1e5'] = (df['Series_Complete_18PlusPop_Pct'] * df['Census2019_18PlusPop']) / 1e5
    area = df['Census2019_18PlusPop'] / 1e4
    xlabel = 'Vaccination_Pop_Per_1e5'
    ylabel = 'Confirmed'

    x = df[xlabel]
    y = df[ylabel]
    

    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0,200)
    ax.set_ylim(0,10000)

    scatter = ax.scatter(x, y, color="blue", s=area, alpha=0.25)

    # produce a legend with a cross section of sizes from the scatter
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
    ax.legend(handles, labels, loc="upper right", title="Vaccined vs Confirmed")


    plt.show()

plotit()