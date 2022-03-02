import pandas as pd

def readit(filename):
  # Read CSV while keeping FIPS as a string
  # Base URL for JHU data repo
  base ="https://raw.githubusercontent.com/"
  base += "CSSEGISandData/COVID-19/master/csse_covid_19_data/"
  base += "csse_covid_19_daily_reports/"
  df = pd.read_csv(base + filename, converters={'FIPS' : str})
  df.dropna() # This doesn't do anything because missing data are not NaN when FIPS is read as a string
  return df[df['FIPS'] != ""] # This eliminates rows without a FIPS (i.e., foreign countries)

#encapsulated file creation and timeframe in a function
def deaths(start, end):
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

#start date
start = '05-01-2021.csv'

deaths(start, "06-01-2021.csv")
deaths(start, "07-01-2021.csv")
deaths(start, "08-01-2021.csv")
deaths(start, "09-01-2021.csv")
deaths(start, "10-01-2021.csv")
deaths(start, "11-01-2021.csv")
deaths(start, "11-30-2021.csv")