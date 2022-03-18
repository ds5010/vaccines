#Kayne Ryan and Matt Ray
#DS5010 Spring 2022

#test.py -- enhancing scatterplot design

import pandas as pd
import matplotlib.pyplot as plt


def scatter(month):
    df = pd.read_csv('data/Merge/vaccinations-and-deaths-'+month+'.csv', converters={'FIPS' : str})
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df[xlabel]
    y = df[ylabel]
    area = df['Census2019_18PlusPop'] / 1e6     #size of bubble = Millions

    fig, ax = plt.subplots()
    ax.set_xlabel("Percent of Population (+18) Considered Fully Vaccinated")
    ax.set_ylabel("Deaths per 100K")
    ax.set_xlim(0,100)
    ax.set_ylim(0,500)
    ax.set_title("Vaccine Effectiveness Snapshot as of: "+ month)
    fig.set_size_inches(8,6)

    #[KR] adding plot scale variable
    plot_scl = 100 #converts population units to pixel units

    #[MR] Added color dictionary by region
    colors = {'AL':'blue','AK':'gold','AZ':'gold','AR':'blue','CA':'gold','CO':'gold','CT':'red','DE':'blue','DC':'blue','FL':'blue','GA':'blue','HI':'gold','ID':'gold','IL':'green','IN':'green','IA':'green','KS':'green','KY':'blue','LA':'blue','ME':'red','MD':'blue','MA':'red','MI':'green','MN':'green','MS':'blue','MO':'green','MT':'gold','NE':'green','NV':'gold','NH':'red','NJ':'red','NM':'gold','NY':'red','NC':'blue','ND':'green','OH':'green','OK':'blue','OR':'gold','PA':'red','RI':'red','SC':'blue','SD':'green','TN':'blue','TX':'blue','UT':'gold','VT':'red','VA':'blue','WA':'gold','WV':'blue','WI':'green','WY':'gold','PR':'blue'}
    #[MR] Added region dictionary to align color legend
    regions = {'South':'blue','West':'gold','Northeast':'red','Midwest':'green'}
    
    #[MR] Added color to reflect region based on state
    scatter = ax.scatter(x, y, s=area*plot_scl, alpha=0.5,c=df['Recip_State'].map(colors), edgecolor='white')

    #[MR] Creates fake line to use index for second legend
    markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in regions.values()]
    leg = plt.legend(markers, regions.keys(), numpoints=1, loc=(1.05,0), title="Region")
    ax.add_artist(leg)

    #[KR] Creates population legend with code-controlled bubble sizes
    for area_scl in [0.5, 2, 4]:
        ax.scatter([], [], s = plot_scl*area_scl, c = "gray", alpha = 0.5, label = str(area_scl) + 'M')
    ax.legend(loc = (1.05, 0.3), title="Population (Millions)", labelspacing = 1.5, borderpad = 1)
    #handles, labels = scatter.legend_elements(prop="sizes", num=4, alpha=0.4)
    #plt.legend(handles, labels, loc=(1.05,0.3), title="Population (Millions)", labelspacing=2, borderpad=1)
    
    plt.tight_layout()
    plt.savefig('test_img/'+month+'.png')

    plt.show()

scatter('11-30-2021')
