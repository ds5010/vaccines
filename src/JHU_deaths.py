from tracemalloc import start
import pandas as pd

# Dates for filename
# start = "05-01-2021.csv"
# end = "06-30-2021.csv"

def readit(filename):
  # Read CSV while keeping FIPS as a string
  # Base URL for JHU data repo
  base = "https://raw.githubusercontent.com/"
  base += "CSSEGISandData/COVID-19/master/csse_covid_19_data/"
  base += "csse_covid_19_daily_reports/"
  df = pd.read_csv(base + filename, converters={'FIPS' : str})
  df.dropna() # This doesn't do anything because missing data are not NaN when FIPS is read as a string
  return df[df['FIPS'] != ""] # This eliminates rows without a FIPS (i.e., foreign countries)

def JHU_deaths(start, end):
    data = {}

    df_deaths = readit(end)
    for i, row in df_deaths.iterrows():
        fips = row['FIPS']
        if len(fips) == 4:
            fips = "0" + fips
        data[fips] = row["Deaths"]
    df_deaths = readit(start)
    for i, row in df_deaths.iterrows():
        fips = row['FIPS']
        if len(fips) == 4:
            fips = "0" + fips
        data[fips] -= row["Deaths"]

    # Write dictionary to a CSV file
    filename = "data/deaths-" + \
            start[:2] + '-' + start[3:5] + "-" + start[6:10] + "-to-" + \
            end[:2] + '-' + end[3:5] + "-" + end[6:]

    with open(filename, 'w') as file:
        file.write("FIPS,Deaths\n") # header
        for key, value in data.items():
            file.write(",".join([key, str(value)]) + "\n")
    df = pd.read_csv(filename)
    return df

def JHU_deaths():
    JHU_deaths("05-01-2021.csv", "05-31-2021.csv")
    JHU_deaths("05-01-2021.csv", "06-30-2021.csv")
    JHU_deaths("05-01-2021.csv", "07-31-2021.csv")
    JHU_deaths("05-01-2021.csv", "08-31-2021.csv")
    JHU_deaths("05-01-2021.csv", "09-30-2021.csv")
    JHU_deaths("05-01-2021.csv", "10-31-2021.csv")
    JHU_deaths("05-01-2021.csv", "11-30-2021.csv")
JHU_deaths()