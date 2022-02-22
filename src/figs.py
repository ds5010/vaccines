from plot import scatter
from plotgeo import choropleth
import pandas as pd


df = pd.read_csv('../data/merge.csv', converters={"FIPS":str})
scatter(df, outfile="../figs/All FIPS Scatter Plot.png")
scatter(df, filters={"CDC_Region":"Region 1"}, outfile="../figs/CDC Region 1 Scatter Plot.png")
scatter(df, filters={"CDC_Region":"Region 5"}, outfile="../figs/CDC Region 5 Scatter Plot.png")
df = compute_stats(df)
df = regress_multiple(df)
choropleth(df, outfile="../figs/Choropleth.png")

