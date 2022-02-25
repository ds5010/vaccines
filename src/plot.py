from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


'''
filter_data() takes a dataframe and a dictionary of filters, then returns a
dataframe containing the slice with only the filtered values
'''
def filter_data(df, filters):
    for filter, value in filters.items():
        print("Filtering by "+str(filter)+" ("+value+")")
        df = df[df[filter] == value]
    return df


'''
compute_stats() adds several additional calculations to the dataframe
'''
def compute_stats(df):
    # Calculate the number of deaths per 10,000 population
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
    # Add a GEOID column (which is backwards-compatible to FIPS)
    df["GEOID"] = df["FIPS"]
    # Translate state code strings into CDC Regions
    regions = defaultdict(None) | {
        "CT": "Region 1",
        "ME": "Region 1",
        "MA": "Region 1",
        "NH": "Region 1",
        "RI": "Region 1",
        "VT": "Region 1",
        "NY": "Region 2",
        "NJ": "Region 2",
        "PR": "Region 2",
        "PA": "Region 3",
        "DE": "Region 3",
        "DC": "Region 3",
        "MD": "Region 3",
        "VA": "Region 3",
        "WV": "Region 3",
        "AL": "Region 4",
        "FL": "Region 4",
        "GA": "Region 4",
        "KY": "Region 4",
        "MS": "Region 4",
        "NC": "Region 4",
        "SC": "Region 4",
        "TN": "Region 4",
        "IL": "Region 5",
        "IN": "Region 5",
        "MI": "Region 5",
        "MN": "Region 5",
        "OH": "Region 5",
        "WI": "Region 5",
        "AR": "Region 6",
        "LA": "Region 6",
        "NM": "Region 6",
        "OK": "Region 6",
        "TX": "Region 6",
        "IA": "Region 7",
        "KS": "Region 7",
        "MO": "Region 7",
        "NE": "Region 7",
        "CO": "Region 8",
        "MT": "Region 8",
        "ND": "Region 8",
        "SD": "Region 8",
        "UT": "Region 8",
        "WY": "Region 8",
        "AZ": "Region 9",
        "CA": "Region 9",
        "HI": "Region 9",
        "NV": "Region 9",
        "AK": "Region 10",
        "ID": "Region 10",
        "OR": "Region 10",
        "WA": "Region 10"
    }
    df["CDC_Region"] = df["Recip_State"].copy()
    df["CDC_Region"] = df["CDC_Region"].apply(lambda x: regions[x])
    #TODO add additional statistics here
    return df


'''
regress() performs a linear regression on a dataframe or slice and return the parameters
'''
def regress(subset, xlabel='Series_Complete_18PlusPop_Pct', ylabel='Deaths_Per_1e5'):
    model = sm.WLS(subset[ylabel], sm.add_constant(subset[xlabel]), subset["Census2019_18PlusPop"])
    return model.fit().params


'''
regress_multiple() runs a series of linear regressions grouped by "column" and save the resulting parameters
into a new pair of columns. By default, this function will run a linear regression for each state.
'''
def regress_multiple(df, xlabel='Series_Complete_18PlusPop_Pct', ylabel='Deaths_Per_1e5', column="Recip_State"):
    print("Regressing by "+column)
    df[column+"_const"] = pd.NA
    df[column+"_slope"] = pd.NA
    for value in df[column].unique():
        # print("Working on "+value)
        subset = df[df[column] == value]
        # print("Regressing over {} datapoints.".format(subset.shape[0]))
        # perform regression
        p = regress(subset, xlabel=xlabel, ylabel=ylabel)
        try:
            # print(p)
            df.loc[df[column] == value, column+"_const"] = float(p.const)
            df.loc[df[column] == value, column+"_slope"] = float(p[xlabel])
        except AttributeError:
            continue
    return df
        

'''
scatter() creates a scatter plot including datapoints scaled by population. It also shows a trendline
and can be passed filters in the form of a dictionary.
'''
def scatter(df, xlabel='Series_Complete_18PlusPop_Pct', ylabel='Deaths_Per_1e5', filters=None, outfile=None):
    titlestr = ylabel+" vs "+xlabel
    if filters:
        df = filter_data(df, filters)
        titlestr = titlestr + ",\n filtered by "
        for filter, value in filters.items():
            titlestr = titlestr+" "+filter+" ("+value+") "

    x = df[xlabel]
    y = df[ylabel]

    fig, ax = plt.subplots()

    fig.suptitle(titlestr)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xlim(0,100)
    ax.set_ylim(0,500)

    scatter = ax.scatter(x, y, s=df['Census2019_18PlusPop']/1e4, alpha=0.25)

    # produce a legend with a cross section of sizes from the scatter
    handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6, num=4, func=lambda x: np.log10(10000*x))
    labels = ["$10^"+label[1:] for label in labels]
    ax.legend(handles, labels, loc="upper right", title="2019 Census Population", labelspacing=1.0)
    
    # perform regression
    p = regress(df, xlabel=xlabel, ylabel=ylabel)

    # plot regression line on the same axes, set x-axis limits
    ax.plot(x, p.const + p[xlabel] * x)

    if outfile:
        fig.savefig(outfile)
    else:
        fig.show()
