import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_month(month):
    f, ax = plt.subplots()
    if month == 'May':
        df = pd.read_csv(
            '../data/Merge/vaccinations-and-deaths-05-31-2021.csv')
    elif month == 'June':
        df = pd.read_csv(
            '../data/Merge/vaccinations-and-deaths-06-30-2021.csv')
    elif month == 'July':
        df = pd.read_csv(
            '../data/Merge/vaccinations-and-deaths-07-31-2021.csv')
    elif month == 'August':
        df = pd.read_csv(
            '../data/Merge/vaccinations-and-deaths-08-31-2021.csv')
    elif month == 'September':
        df = pd.read_csv(
            '../data/Merge/vaccinations-and-deaths-09-30-2021.csv')
    elif month == 'October':
        df = pd.read_csv(
            '../data/Merge/vaccinations-and-deaths-10-31-2021.csv')
    elif month == 'November':
        df = pd.read_csv(
            '../data/Merge/vaccinations-and-deaths-11-30-2021.csv')
    ax.set_title(month)
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 500)
    area = df['Census2019_18PlusPop'] / 1e4
    scatter = ax.scatter(x=df['Series_Complete_18PlusPop_Pct'], y=df['Deaths_Per_1e5'],
                         alpha=0.25, s=area)
    ax.set_xlabel('Series_Complete_18PlusPop_Pct')
    ax.set_ylabel('Deaths_Per_1e5')
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5, num=4)
    ax.legend(handles, labels, loc="upper right",
              title="Population Sizes (x10k)")
    plt.savefig('../img/'+month+'.')
    plt.ion()
    plt.pause(5)
    plt.close()


Months = ['May', 'June', 'July', 'August', 'September', 'October', 'November']


Months = ['May', 'June', 'July', 'August', 'September', 'October', 'November']

for i in Months:
    plot_month(i)
