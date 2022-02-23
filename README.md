# Want to know what's the vaccine effectiveness of your home county? check iy out!

### Concusion first, The vaccine effectiveness declines since July (I think delta start to spread at that time) but strengthed at the end of August .At the middle of November, It declines again(I think Omicron start to spread at that time ).  
In last few days, I try to built a function to show vaccine effectiveness in particular counties.
I don't have enought time to get all code sorted. But I will explain what I did for this.
- First I need to show the time-evolution of vaccine effectiveness. I think the x axis should be time.
- So for Y axis , I need some indicator to show effectiveness.Here's my solution 
> vaccine effectiveness=daily diagnosis rate/vaccination rate
> daily diagnosis rate=number of daily confimed/vaccination rate
 
So Here's what I need to do 
1. get all death and comfirm data from 05-01-2021 to 11-30-2021.
   - scratch all csv from https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
   - use concat merge those the csv file from 5-01-2021 to 11-30-2021
   - Offset the death data , because the time of  update of the death data is on the second day
   - Modify the date ,We just need to be accurate to the day，remove the hour minute seconds in death data 
   - Filter the data without a FIPS
   - make some four digital fips to 5 digital

2.merge the death data with vaccine rate data ,use date and fips 
- This takes quite a while,But if we make the dataframe into a dictionary and modify the data on the dictionary then we transform the dictionary back to a dataframe, that will be much faster.
- merge confirm and death column into the vaccine dataframe
- make 2 columns 'Deaths_from_May' and 'Confirmed_from_May' .one indicates how many people died since May 1t, and another indicates what's the total numer of confirmed since May 1st
- make column 'population_confirm_today' which indicates the number of confirm number in that particular day.
- make column 'confirm_rate_perday' this shows the confirm rate of today```confirm_rate_perday=population_confirm_today/Census2019_18PlusPop```




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

