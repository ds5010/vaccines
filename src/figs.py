from plot import *
from plotgeo import *
import pandas as pd

# start with merged data and compute additional stats
df = pd.read_csv('data/merge.csv', converters={"FIPS":str})
df = compute_stats(df)

# create two sample files, one with and one without filtering
scatter(df, outfile="figs/All_FIPS_Scatter_Plot.png")
scatter(df, filters={"CDC_Region":"Region 1"}, outfile="figs/CDC_Region_1_Scatter_Plot.png")

# run regressions (default to state-level)
df = regress_multiple(df)
choropleth(df, outfile="figs/Regression_by_Recip_State_Choropleth.png")
scatter(df, filters={"Recip_State": "FL"}, outfile="figs/Florida_Scatter_Plot.png")

# run another regression (this time by CDC Region)
df = regress_multiple(df, column="CDC_Region")
choropleth(df, column="CDC_Region", outfile="figs/Regression_by_CDC_Region_Choropleth.png")
