import pandas as pd

# learn about merging dataframes at https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html
def merge_by_FIPS(vaccinations_file, deaths_file, outfile=None):
    vaccinations = pd.read_csv(vaccinations_file)
    deaths = pd.read_csv(deaths_file)
    merged = vaccinations.merge(deaths, on="FIPS", sort=True)
    if outfile:
        merged.to_csv(outfile, index=False)
    return merged

merge_by_FIPS("data/vaccinations-06-01-2021.csv", "data/deaths-05-01-2021-to-06-01-2021.csv", \
    outfile="data/vaccinations-and-deaths-06-01-2021")
merge_by_FIPS("data/vaccinations-07-01-2021.csv", "data/deaths-05-01-2021-to-07-01-2021.csv", \
    outfile="data/vaccinations-and-deaths-07-01-2021")
merge_by_FIPS("data/vaccinations-08-01-2021.csv", "data/deaths-05-01-2021-to-08-01-2021.csv", \
    outfile="data/vaccinations-and-deaths-08-01-2021")
merge_by_FIPS("data/vaccinations-09-01-2021.csv", "data/deaths-05-01-2021-to-09-01-2021.csv", \
    outfile="data/vaccinations-and-deaths-09-01-2021")
merge_by_FIPS("data/vaccinations-10-01-2021.csv", "data/deaths-05-01-2021-to-10-01-2021.csv", \
    outfile="data/vaccinations-and-deaths-10-01-2021")
merge_by_FIPS("data/vaccinations-11-01-2021.csv", "data/deaths-05-01-2021-to-11-01-2021.csv", \
    outfile="data/vaccinations-and-deaths-11-01-2021")
merge_by_FIPS("data/vaccinations-11-30-2021.csv", "data/deaths-05-01-2021-to-11-30-2021.csv", \
    outfile="data/vaccinations-and-deaths-11-30-2021")
