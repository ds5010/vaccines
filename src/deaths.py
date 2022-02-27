import pandas as pd

def time_sample(end_date):
  # Dates for filename
  # must keep leading zeros for url to work
  # start is one month prior end date
  #start = f'{str(int(end_date[:2])-1):02d}' +end_date[2:]
  start_date = '05-30-2021'

  def readit(end_date, col = ['FIPS','Deaths']):
    # URL for JHU data repo
    address ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + end_date +'.csv'
    df = pd.read_csv(address, usecols= col)
    # Drop missing FIPS
    df = df[df['FIPS'].notna()]
    # Change FIPS from INT64 to formatted string
    df['FIPS'] = df['FIPS'].apply(lambda x: f'{x:05.0f}')
    df.set_index('FIPS',inplace=True)
    return df

  start_df = readit(start_date)
  end_df = readit(end_date)
  change = end_df.sub(start_df,fill_value=0)
  print(change)
  return change
  
def main():
    time_sample('11-30-2021')

if __name__=='__main__':
    main()
