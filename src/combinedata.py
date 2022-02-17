import pandas as pd

# learn about merging dataframes at https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
def merge_by_FIPS(vaccinations_file, deaths_file, outfile=None):
    vaccinations = pd.read_csv(vaccinations_file)
    deaths = pd.read_csv(deaths_file)
    merged = vaccinations.merge(deaths, on="FIPS", sort=True)
    if outfile:
        merged.to_csv(outfile, index=False)
    return merged

merge_by_FIPS("data/vaccinations-11-30-2021.csv", "data/deaths-05-01-2021-to-11-30-2021.csv", \
    outfile="data/vaccinations-and-deaths-11-30-2021")
