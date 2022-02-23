import pandas as pd

def time_sample(end_date):
  # Dates for filename
  start = "05-01-2021"

  def readit(end_date):
    # Read CSV while keeping FIPS as a string
    # Base URL for JHU data repo
    address ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + end_date +'.csv'
    df = pd.read_csv(address, converters={'FIPS' : str})
    df.dropna() # This doesn't do anything because missing data are not NaN when FIPS is read as a string
    return df[df['FIPS'] != ""] # This eliminates rows without a FIPS (i.e., foreign countries)

  data = {}

  df_deaths = readit(end_date)
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
            end_date + '.csv'

  with open(filename, 'w') as file:
    file.write("FIPS,Deaths\n") # header
    for key, value in data.items():
      file.write(",".join([key, str(value)]) + "\n")
