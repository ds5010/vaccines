import pandas as pd

# learn about merging dataframes at https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
def merge_by_FIPS(vaccinations_file, confirmed_file, outfile=None):
    vaccinations = pd.read_csv(vaccinations_file)
    confirmed = pd.read_csv(confirmed_file)
    merged = vaccinations.merge(confirmed, on="FIPS", sort=True)
    if outfile:
        merged.to_csv(outfile, index=False)
    return merged

merge_by_FIPS("data/vaccinations-11-30-2021.csv", "data/confirmed-05-01-2021-to-11-30-2021.csv", \
    outfile="data/vaccinations-and-confirmed-11-30-2021")