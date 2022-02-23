# Want to know what's the vaccine effectiveness of your home county? check iy out!
>*1.* Make sure US_data.csv is in your directory. This file take me long time to create. All things I done for it is in Folder Things_for_assignment5
>*2.* go to file assignment5.py, make county_FIPS the county you want to check.
>*3.* Run python assignment5.py

23005 Cumberland County (Portland,Maine)
![output](https://github.com/ds5010/vaccines/blob/yune_branch/sceenshot/portland.png)
25025 Suffolk County (Boston)
![output](https://github.com/ds5010/vaccines/blob/yune_branch/sceenshot/boston.png)
36061 New York County
![output](https://github.com/ds5010/vaccines/blob/yune_branch/sceenshot/newyork.png)
06037  Los Angeles county
![output](https://github.com/ds5010/vaccines/blob/yune_branch/sceenshot/losangeles.png)
06075 San Francisco County
![output](https://github.com/ds5010/vaccines/blob/yune_branch/sceenshot/sanfrancisco.png)

## Concusion 
In most county, The vaccine effectiveness declines since July (I think delta start to spread at that time) but strengthed at the end of August .At the middle of November, It declines again(I think Omicron start to spread at that time ).  
##What I do
- First I need to show the time-evolution of vaccine effectiveness. I think the x axis should be time.
- So for Y axis , I need some indicator to show effectiveness.Here's my solution 
> vaccine effectiveness=daily diagnosis rate/vaccination rate
> daily diagnosis rate=number of daily confimed/vaccination rate
 
## Steps to do
1. get all death and comfirm data from 05-01-2021 to 11-30-2021.
   - scratch all csv from https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports .
```python
import requests
import re
from bs4 import BeautifulSoup
import wget

# URL on the Github where the csv files are stored
# change USERNAME, REPOSITORY and FOLDER with actual name
github_url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'

result = requests.get(github_url)
with open('/Users/mac/csse_covid_19_daily_reports', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

csvfiles = soup.find_all(title=re.compile("\.*csv$"))
filename = []
for i in csvfiles:
    filename.append(i.extract().get_text())
# get a list like this ['01-01-2021.csv', '01-01-2022.csv', '01-02-2021.csv', '01-02-2022.csv', '01-03-2021.csv', '01-03-2022.csv', '01-04-2021.csv', '01-04-2022.csv', '01-05-2021.csv', '01-05-2022.csv', '01-06-2021.csv', '01-06-2022.csv', '01-07-2021.csv', '01-07-2022.csv', '01-08-2021.csv', '01-08-2022.csv', '01-09-2021.csv', '01-09-2022.csv', '01-10-2021.csv', '01-10-2022.csv', '01-11-2021.csv', '01-11-2022.csv', '01-12-2021.csv', '01-12-2022.csv', '01-13-2021.csv', '01-13-2022.csv', '01-14-2021.csv', '01-14-2022.csv', '01-15-2021.csv', '01-15-2022.csv', '01-16-2021.csv', '01-16-2022.csv', '01-17-2021.csv', '01-17-2022.csv', '01-18-2021.csv', '01-18-2022.csv', '01-19-2021.csv', '01-19-2022.csv', '01-20-2021.csv', '01-

base = "https://raw.githubusercontent.com/"
base += "CSSEGISandData/COVID-19/master/csse_covid_19_data/"
base += "csse_covid_19_daily_reports/"
download_list = []
for i in filename:
    download_list.append(base+i)
print(download_list[0])
# 👆🏻 get list like this ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv', 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2022.csv',
for url in download_list:
    wget.download(url, '/Users/mac/dead_data')
# use wget to down load
```
   - use concat to merge those the csv file from 5-01-2021 to 11-30-2021. I use glob module and regular expression here. 
```python
import glob
import pandas as pd
a = glob.glob('../../dead_data/[0][5-9]*-*-2021.csv')
b = glob.glob('../../dead_data/[1][0-1]*-*-2021.csv')
may_to_novenmber = a+b
print(a+b)
may_to_novenmber = sorted(may_to_novenmber)
final_data = pd.concat(
    map(pd.read_csv, may_to_novenmber,), ignore_index=True)
# 删选掉FIPS ==nan的，这个时候 final_data.FIPS.dtype== float64
final_data = final_data[final_data['FIPS'].isna() == False]
final_data
final_data['FIPS'] = final_data['FIPS'].astype('int')
# final_data.FIPS.dtype
final_data.to_csv('final_data.csv', index=False)

```
   - Modify the date ,We just need to be accurate to the day，remove the hour minute seconds in death data .Offset the death data , because the time of  update of the death data is on the second day. Use to_dict to tranform the dataframe into a dictionary instead of using df.iterrows(), to_dict is much faster if you are play with large volumn data
```python
import pandas as pd
death = pd.read_csv('final_data.csv', converters={'FIPS': str})
# Turn the death dataframe into a dictionary
dict_copy = death.to_dict('records')
for r in dict_copy:
    if len(r['FIPS']) == 4:
        r['FIPS'] = '0'+r['FIPS']
death2 = pd.DataFrame.from_dict(dict_copy)
death2.to_csv('final_data.csv', index=False)

```
   - Filter the data without a FIPS, use .isna()
   - make some four digital fips to 5 digital
```python
import pandas as pd
death = pd.read_csv('final_data.csv', converters={'FIPS': str})
# Turn the death dataframe into a dictionary
dict_copy = death.to_dict('records')
for r in dict_copy:
    if len(r['FIPS']) == 4:
        r['FIPS'] = '0'+r['FIPS']
death2 = pd.DataFrame.from_dict(dict_copy)
death2.to_csv('final_data.csv', index=False)

```

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

