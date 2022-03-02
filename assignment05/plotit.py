import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plotit(months):
    df = pd.read_csv('./assignment05/data/vaccinations-and-deaths-'+ months +'-2021.csv')
    #df['Vaccination_Pop_Per_1e5'] = (df['Series_Complete_18PlusPop_Pct'] * df['Census2019_18PlusPop']) / 1e5
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
    area = df['Census2019_18PlusPop'] / 1e4
    #xlabel = 'Vaccination_Pop_Per_1e5'
    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df[xlabel]
    y = df[ylabel]
    

    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0,100)
    ax.set_ylim(0,500)
    ax.set_title("Vaccination Effectiveness in " + months)
    scatter = ax.scatter(x, y, color='tab:blue', s=area, alpha=0.25)

    # produce a legend with a cross section of sizes from the scatter
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
    ax.legend(handles, labels, loc="upper right", title="Population(*10k)")


    plt.show()
    plt.savefig('./assignment05/img/'+ months +'.png')

plotit("May")
plotit("June")
plotit("July")
plotit("Aug")
plotit("Sep")
plotit("Oct")
plotit("Nov")