#Kayne Ryan
#DS5010 Spring 2022
#scatters.py -- uses dataframes to create a series of scatter plots

import pandas as pd
import matplotlib.pyplot as plt

def scatter(month):
    df = pd.read_csv('data/vaccinations-and-deaths-'+month+'.csv', converters={'FIPS' : str})
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df[xlabel]
    y = df[ylabel]
    area = df['Census2019_18PlusPop'] / 1e4     

    fig, ax = plt.subplots()
    ax.set_xlabel("Percent of Population (+18) Considered Fully Vaccinated")
    ax.set_ylabel("Deaths per 100K")
    ax.set_xlim(0,100)
    ax.set_ylim(0,500)
    ax.set_title("Vaccine Effectiveness Snapshot as of: "+ month)
    fig.set_size_inches(8,6)

    scatter = ax.scatter(x, y, s=area, alpha=0.5)

    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4)
    ax.legend(handles, labels, loc="upper right", title="Population Sizes (0000s)", labelspacing=2, borderpad=1)
    
    plt.tight_layout()
    plt.savefig('img/'+month+'.png')
    

scatter('06-01-2021')
scatter('07-01-2021')
scatter('08-01-2021')
scatter('09-01-2021')
scatter('10-01-2021')
scatter('11-01-2021')
scatter('11-30-2021')





