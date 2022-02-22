# vaccines

Collaborative project to investigate vaccine effectiveness

## 0. Dependencies

This program requires numpy, matplotlib, pandas, and statsmodels. Additionally, geopandas is required if you wish to use the choropleth plotting function.

## 1. Getting and Merging Data

In general, the Makefile simplifies accessing python scripts and implements some basic dependency logic. The following three commands will download vaccination data from the US CDC, COVID-19 deaths data from JHU, and merge them into a single file by matching them with FIPS codes.

```makefile
make vaccines
make deaths
make merge
```

## 2. Helper Functions

plot.py contains most of the code necessary, with the exception of geoprocessing, which is kept in plotgeo.py in case you would prefer not to install geopandas.

A few helper functions are available that could be of interest:

```python
'''
filter_data() takes a dataframe and a dictionary of filters, then returns a
dataframe containing the slice with only the filtered values
'''
def filter_data(df, filters):
    # see src/plot.py for source code
```

```python
'''
compute_stats() adds several additional calculations to the dataframe
'''
def compute_stats(df):
    # Calculate the number of deaths per 10,000 population
    # Add a GEOID column (which is backwards-compatible to FIPS)
    # Translate state code strings into CDC Regions
    # see src/plot.py for source code
```

```python
'''
regress() performs a linear regression on a dataframe or slice and return the parameters
'''
def regress(subset, xlabel='Series_Complete_18PlusPop_Pct', ylabel='Deaths_Per_1e5'):
    # see src/plot.py for source code
```

```python
'''
regress_multiple() runs a series of linear regressions grouped by "column" and save the resulting parameters
into a new pair of columns. By default, this function will run a linear regression for each state.
'''
def regress_multiple(df, xlabel='Series_Complete_18PlusPop_Pct', ylabel='Deaths_Per_1e5', column="Recip_State"):
    # see src/plot.py for source code
```

## 3. Plotting Functions

Two plotting functions are available: scatter and choropleth.

### ```scatter```
```python
'''
scatter() creates a scatter plot including datapoints scaled by population. It also shows a trendline
and can be passed filters in the form of a dictionary.
'''
def scatter(df, xlabel='Series_Complete_18PlusPop_Pct', ylabel='Deaths_Per_1e5', filters=None, outfile=None):
    # see src/plot.py for source code
```

For example, running ```scatter(df)``` on the full dataset produces the following result:

![example scatter plot](/figs/All_FIPS_Scatter_Plot.png)

scatter() also uses the filter_data(), making it easy to close in on a specific geographic region. ```scatter(df, filters={"CDC_Region":"Region 1"}, outfile="figs/CDC Region 1 Scatter Plot.png")``` produces the following result, showing data from the CDC's northeast region:

![example scatter plot filtered by CDC Region 1](/figs/CDC_Region_1_Scatter_Plot.png")

### ```choropleth```

As it turns out, once you have regression coefficients it becomes expedient to look directly at those correlations rather than examining region-by-region. Once we have run some regressions, choropleth map is an effective way of showing these results:
```python
df = regress_multiple(df) # defaults to state-by-state
choropleth(df)
```
![example choropleth by state](/figs/Regression_by_Recip_State_Choropleth.png)

Visualizing the data this way highlights some... interesting results. To look at Florida, for example, we could run ```scatter(df, filters={"Recip_State": "FL"}``` and see that there seem to be unusually low death rates compared to overall:

![example scatter filtered by state (florida)](/figs/Florida_Scatter_Plot.png)

There could be perfectly good reasons for this. Perhaps Florida just got lucky. Or perhaps a government official there has ulterior motives for implementing policies that underreport death counts because they're considering a bid for the Republican presidential nomination. Perhaps.

Things look more reasonable if we repeat the regression on a regional level:
```python
df = regress_multiple(df, column="CDC_Region")
choropleth(df, column="CDC_Region")
```
![example choropleth by CDC region](/figs/Regression_by_CDC_Region_Choropleth.png)
