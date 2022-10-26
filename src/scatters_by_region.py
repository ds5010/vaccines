#Matt Ray and Kayne Ryan
#DS5010 Spring 2022
#creates series of scatterplots for selected date ranges, saves images to .png file

import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np

def scatter(month):
    df = pd.read_csv('data/Merge/vaccinations-and-deaths-'+month+'.csv', converters={'FIPS' : str})
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'
    #population in millions



    #[KR] adding plot scale variable
    plot_scl = 100 #converts population units to pixel units

    #[MR] Added color dictionary by region
    colors = {'AL':'blue','AK':'gold','AZ':'gold','AR':'blue','CA':'gold','CO':'gold','CT':'red','DE':'blue','DC':'blue','FL':'blue','GA':'blue','HI':'gold','ID':'gold','IL':'green','IN':'green','IA':'green','KS':'green','KY':'blue','LA':'blue','ME':'red','MD':'blue','MA':'red','MI':'green','MN':'green','MS':'blue','MO':'green','MT':'gold','NE':'green','NV':'gold','NH':'red','NJ':'red','NM':'gold','NY':'red','NC':'blue','ND':'green','OH':'green','OK':'blue','OR':'gold','PA':'red','RI':'red','SC':'blue','SD':'green','TN':'blue','TX':'blue','UT':'gold','VT':'red','VA':'blue','WA':'gold','WV':'blue','WI':'green','WY':'gold','PR':'blue'}
    #[MR] Added region dictionary to align color legend
    
    regions = {'blue':'South','gold':'West','red':'NorthEast','green':'Midwest'}
    df["region_color"]=df["Recip_State"].map(colors)
    df["region"]=df["region_color"].map(regions)
    for k,v in regions.items():
    	fig, ax = plt.subplots()
    	ax.set_xlabel("Percent of Population (+18) Considered Fully Vaccinated")
    	ax.set_ylabel("Deaths per 100K")
    	ax.set_xlim(0,100)
    	ax.set_ylim(0,400) #[KR] changed from 500 limit to 400 limit
    	ax.set_title("Vaccine Effectiveness Snapshot as of: "+ month)
    	fig.set_size_inches(8,6)
    	ax.spines['top'].set_visible(False) #[MR] Removes top spine
    	ax.spines['right'].set_visible(False) #[MR] Removes right spine
    	ax.grid(color='gray', linestyle='-', linewidth=0.25, alpha=0.6) #[MR] Adds gridlines
	    
    	region_df = df[df["region"]==v]
    	print(region_df.shape[0])
    	x = region_df[xlabel]
    	y = region_df[ylabel]
    	area = region_df['Census2019_18PlusPop'] / 1e6
    	    #[MR] Adds best fit line 
    	m, b = np.polyfit(x, y, 1)
    	plt.plot(x, m*x + b, alpha=0.8, c='dimgray')

    	#[MR] Added color to reflect region based on state
    	#[KR] changed s to incorporate plot_scl variable
    	scatter = ax.scatter(x, y, s=area*plot_scl, alpha=0.5,c=region_df['region_color'], edgecolor='white')
    	#[MR] Creates fake line to use index for second legend
    	# markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in regions.values()]
    	# leg = plt.legend(markers, regions.keys(), numpoints=1, loc=(1.05,0), title="Region")
    	# ax.add_artist(leg)
    	#[KR] Creates population legend using code-controlled bubble sizes
    	for area_scl in [0.5, 2, 4]:
    		ax.scatter([], [], s = plot_scl*area_scl, c = "gray", alpha = 0.5, label = str(area_scl) + 'M')
    	ax.legend(loc = (1.05, 0.3), title="Population (Millions)", labelspacing = 1.5, borderpad = 1)
    	plt.tight_layout()
    	plt.savefig('img/'+month+f"_{v}"+'.png')

def create_scatters():
    """This function creates seven scatter plots based on the merged data.
    """

    
    dates = [
        "05-31-2021",
        "06-30-2021",
        "07-31-2021",
        "08-31-2021",
        "09-30-2021",
        "10-31-2021",
        "11-30-2021"
    ]
    for date in dates:
        # print(date)
        scatter(date)

if __name__ == "__main__":
    create_scatters()
