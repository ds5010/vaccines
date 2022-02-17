import pandas as pd
import numpy as np

def merge():
    base = "./data/"
    df = pd.read_csv(base + "vaccinations-11-30-2021.csv", converters={'FIPS' : str})
    deaths = pd.read_csv(base + "deaths-05-01-2021-to-11-30-2021.csv", converters={'FIPS' : str})
    
    ## Add the deaths data to the dataframe
    df['Deaths'] = None
    bad = 0
    for i, row in df.iterrows():
        fips = row.FIPS
        try:
          df.loc[i, 'Deaths'] = deaths.loc[deaths.FIPS == fips].iloc[0,1]
        except:
          bad += 1
          print(bad, "Couldn't find deaths for FIPS:", fips, row.FIPS, row.Recip_County, row.Recip_State)
    
    print("BEFORE:", df.shape)
    df = df.dropna()
    print("AFTER:", df.shape)
    return df

df = merge()

df.to_csv("data/merge.csv")
