#Kayne Ryan
#DS5010 Spring 2022

#test.py -- enhancing scatterplot design

import pandas as pd
import matplotlib.pyplot as plt

def scatter(month):
    df = pd.read_csv('data/vaccinations-and-deaths-'+month+'.csv', converters={'FIPS' : str})
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df[xlabel]
    y = df[ylabel]
    area = df['Census2019_18PlusPop'] / 1e4     #size of bubble = # of 10Ks in county)

    fig, ax = plt.subplots()
    ax.set_xlabel("Percent of Population Considered Fully Vaccinated")
    ax.set_ylabel("Deaths per 100K")
    ax.set_xlim(0,100)
    ax.set_ylim(0,500)
    ax.set_title("Snapshot as of: "+ month)
    fig.set_size_inches(6,6)

    scatter = ax.scatter(x, y, s=area, alpha=0.5)

    # produce a legend with a cross section of sizes from the scatter
    #handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5, num=4)
    #ax.legend(handles, labels, loc="upper right", title="Population Sizes", labelspacing=2, borderpad=1); 
    
    leg = dict(prop='sizes', num=4, fmt = '{x:0f}00,000', func=lambda s: x/100)
    legend1 = ax.legend(*scatter.legend_elements(**leg), loc="upper right", title = "Population Size")

    ##
    #kw = dict(prop="sizes", num=5,color=scatter.cmap(0.7), fmt="$ {x:.2f}", func=lambda s: np.sqrt(s/.3)/3)
    #legend2 = ax.legend(*scatter.legend_elements(**kw),loc="lower right", title="Price")
    ##

    plt.savefig('test_img/'+month+'.png')
    plt.show()

scatter('10-01-2021')