import pandas as pd

def merge():
    base = "./data/"
    df = pd.read_csv(base + "vaccinations-11-30-2021.csv", converters={'FIPS' : str})
    deaths = pd.read_csv(base + "deaths-05-01-2021-to-11-30-2021.csv", converters={'FIPS' : str})
    
    merged = df.merge(deaths, on="FIPS", sort=True)

    print("BEFORE:", df.shape)
    df = df.dropna()
    print("AFTER:", df.shape)
    return df

df = merge()

df.to_csv("data/merge.csv")
