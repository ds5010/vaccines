#Welcome to Yune's branch
***On February 14, 1946, the world's first general-purpose computer was born at the University of Pennsylvania. Please accompany your computer on this special day.***
## Work Log
- 2/14/2022:
Today I created two methods with pandas one is get_data_from_startdate_to_enddate_csv and the other is get_data_from_startdate_to_enddate_gzip. 
I use read_csv() and to_csv. I transform the colomn date to datetime.

##Here are something might be useful

https://www.geeksforgeeks.org/how-to-create-multiple-csv-files-from-existing-csv-file-using-pandas/?ref=rp

https://pandas.pydata.org/docs/user_guide/timeseries.html?highlight=datetime

### YouTube videos
[Pandas To CSV | pd.DataFrame.to_csv()](https://www.youtube.com/watch?v=UE0BbRdEFYA)

[How do I work with dates and times in pandas?](https://www.youtube.com/watch?v=yCgJGsg0Xa4) This one is extremly helpful

[Parsing and Formatting Dates in Python With Datetime](https://www.youtube.com/watch?v=zY02utxcauo)
## My solution
```python
def get_data_from_startdate_to_enddate_gzip(start_date, end_date):
    df = pd.read_csv('data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz', compression='gzip',
                     header=0)
    print(type(df.iloc[1]))
    df['Date'] = pd.to_datetime(df.Date)
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df = df.loc[df.Date >= start_date][df.Date <= end_date]
    # df = df.loc[start_date:end_date]
    df.to_csv('May_1st_to_November_30th.csv.gz',
              index=False, compression='gzip')
```
## how to play with the code
- first, make sure that there are no file named ```May_1st_to_November_30th.csv.gz``` in your directory
- second, define start date and end date in get_dcd_date_from_start_end.py
- run``` python get_dcd_date_from_start_end.py``` you will get a csv.zip file containing data from 5/1/2021 to 11/30/2021