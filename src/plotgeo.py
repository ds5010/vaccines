import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm


'''
chloropleth() creates a county map of the contiguous 48 states colored by the slope of the
regression calculated using plot/regress_multiple()
'''
def choropleth(df, cmap="viridis", column="Recip_State", outfile=None):
    # create the new plot
    fig, ax = plt.subplots()
    fig.suptitle("Vaccine Effectiveness by\n"+column)

    # load county shapes
    counties = gpd.read_file("data/cb_2018_us_county_500k/cb_2018_us_county_500k.shp")

    # filter out non-contiguous states (somewhat clumsily)
    filtered_counties = counties.copy()
    filtered_counties = filtered_counties[~(filtered_counties["STATEFP"] == "02")] # alaska
    filtered_counties = filtered_counties[~(filtered_counties["STATEFP"] == "15")] # hawaii
    filtered_counties = filtered_counties[~(filtered_counties["STATEFP"] == "72")] # puerto rico

    # merge the datasets
    merge = filtered_counties.merge(df, on="GEOID")
    # calculate the normalization and colormap so that we can use them
    column = column+"_slope"
    norm = Normalize(vmin=merge[column].min(), vmax=merge[column].max())
    n_cmap = cm.ScalarMappable(norm=norm, cmap=cmap)
    
    ax = merge.plot(column, cmap=cmap, ax=ax)

    # add the colorbar
    n_cmap.set_array([])
    ax.get_figure().colorbar(n_cmap, ax=ax, orientation='horizontal')
    
    if outfile:
        fig.savefig(outfile)
    else:
        fig.show()