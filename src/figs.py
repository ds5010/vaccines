from plot import *
from plotgeo import *
import pandas as pd

# start with merged data and compute additional stats
df = pd.read_csv('data/merge.csv', converters={"FIPS":str})
df = compute_stats(df)

# create two sample files, one with and one without filtering
scatter(df, outfile="figs/All FIPS Scatter Plot.png")
scatter(df, filters={"CDC_Region":"Region 1"}, outfile="figs/CDC Region 1 Scatter Plot.png")

# run regressions (default to state-level)
df = regress_multiple(df)
choropleth(df, outfile="figs/Regression by Recip_State Choropleth.png")
scatter(df, filters={"Recip_State": "FL"}, outfile="figs/Florida Scatter Plot.png")

# run another regression (this time by CDC Region)
df = regress_multiple(df, column="CDC_Region")
choropleth(df, column="CDC_Region", outfile="figs/Regression by CDC_Region Choropleth.png")
