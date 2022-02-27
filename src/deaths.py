'''
deaths contains two functions:
readit pulls the data from github for the given date, returns dataframe
deathsample computes the difference between death figures for the two dates, returns dataframe
'''
import pandas as pd

def readit(end_date, col = ['FIPS','Deaths']):
  address ="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + end_date +'.csv'
  df = pd.read_csv(address, usecols= col)
  
  # Drop missing FIPS
  df = df[df['FIPS'].notna()]
  
  # Change FIPS from INT64 to formatted string
  df['FIPS'] = df['FIPS'].apply(lambda x: f'{x:05.0f}')
  df.set_index('FIPS',inplace=True)
  
  return df

def death_sample(end_date):
  # must keep leading zeros for url to work
  start_date = '05-30-2021'

  start_df = readit(start_date)
  end_df = readit(end_date)
  change = end_df.sub(start_df,fill_value=0)
  return change


# main function is for testing only 
def main():
    death_sample('11-30-2021')

if __name__=='__main__':
    main()
