import pandas as pd
import gzip
# df = pd.read_csv('/data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz',
#                  index_col='Date')
# print(df)
# print(type(df.index_col))
# print(df.to_datetime)
start_date = '5/1/2021'
end_date = '11/30/2021'

# convert the data from start date to end date into a csv file 153 mb


def get_data_from_startdate_to_enddate_csv(start_date, end_date):
    df = pd.read_csv('data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz', compression='gzip',
                     header=0)
    print(type(df.iloc[1]))
    df['Date'] = pd.to_datetime(df.Date)
    df.Date
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    # print(start_date)
    # print(end_date)
    df = df.loc[df.Date >= start_date][df.Date <= end_date]
    # df = df.loc[start_date:end_date]
    df.to_csv('my_new_file.csv', index=False)

# convert the data from start date to end date into a gzip file 43mb


def get_data_from_startdate_to_enddate_gzip(start_date, end_date):
    df = pd.read_csv('data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz', compression='gzip',
                     header=0)
    print(type(df.iloc[1]))
    df['Date'] = pd.to_datetime(df.Date)
    df.Date
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    # print(start_date)
    # print(end_date)
    df = df.loc[df.Date >= start_date][df.Date <= end_date]
    # df = df.loc[start_date:end_date]
    df.to_csv('May_1st_to_November_30th.csv.gz',
              index=False, compression='gzip')


get_data_from_startdate_to_enddate_gzip(start_date, end_date)
