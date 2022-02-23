# Vaccine Effectiveness Over Time
## Overview 
The Covid-19 pandemic will go down in history as one of the worst global events on record. Currently, there have been ~426 Million cases and 6 Million deaths world wide since the start in Jan. 2020 - Feb. 2022 (WHO: https://covid19.who.int/).
Due to the global nature of the disease and the span in which it has been affecting the world's population (~2 years), there is massive amounts of data available to analyze. 
The goal of this analysis is to explore the relationship between Covid-19 vaccination rates and deaths in U.S.

![alt text](https://www.emeraldgrouppublishing.com/sites/default/files/image/covid-cells.jpg)

## Gathering Data 
In this analysis, data sources were compiled from the Center For Disease Control and Prevention (CDC) and Johns Hopkins University (JHU). The following data and datasets were used. 

CDC Dataset
```
https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh
```

Johns Hopkins Dataset
```
https://github.com/CSSEGISandData/COVID-19/tree/f57525e860010f6c5c0c103fd97e2e7282b480c8
```
The data files were downloaded from their respective websites and stored on a local drive until combined. Vaccination data was sources from the CDC dataset and death data was sourced from the Johns Hoplins dataset. 
U.S. data was identified by FIPS codes and it was determined that August - September would be used for analysis, due to full roll out of the vaccination and before the Omicron varient of Covid-19 ramped up in the U.S. 

    FIPS: Federal Information Processing Standard Publication is a five-digit Federal Information Processing Standards code which uniquely identified counties and county equivalents in the United States, certain U.S. possessions, and certain freely associated states.

## Combining Data

The Johns Hopkins data was dowloaded to the local drive and the individuals days worth of data were combined using pd.concat() to create the full JHU dataset between May - Nov of 2021. 
This can be done my downloading the files to your local drive and modifying Assignment_5_JHU_CovidData_May-Nov_2021.py to combine the individual days into one dataset. 
https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Assignment_5_JHU_CovidData_May-Nov_2021.py
- Luckily, the final data file is provided below. 

The CDC and full Johns Hopkins datasets were combined and cleaned in Python by running the Assignment_5_TimeSeries_Data.py file. 
https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Assignment_5_TimeSeries_Data.py

- Step 1: Import the Johns Hopkins Data, create a data frame and print the column names. 
```
jhu_df = pd.read_csv ('/Users/matthewray/Desktop/JSHU_CovidData_Clean.csv')
list_columns = jhu_df.columns.values.tolist()
print(list_columns)
```
- Step 2: Drops unused columns in JH dataset. Only a few remain: FIPS, Last_Updated, Deaths. 
```
drop_columns = ['Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Confirmed', 'Recovered', 'Active', 'Combined_Key', 'Incident_Rate', 'Case_Fatality_Ratio']
jhu_df.drop(columns=drop_columns, inplace=True)
print(jhu_df.columns)   
print(jhu_df)
```
- Step 3: Remove the rows with no FIPS code as we only want to analyze U.S. data. 
```
jhu_df_cl = jhu_df[jhu_df['FIPS'].notna()]
print(jhu_df_cl)
```
- Step 4: Create a unique identifying column by concatonating the last_updated column with the FIPS code (common data across both sets)
```
jhu_df_cl['Unique_id'] = jhu_df_cl.Last_Update.astype(str) + '_' + jhu_df_cl.FIPS.astype(str)
print(jhu_df_cl)
```
- Step 5: Repeat steps 1 - 4 using the CDC data. 
```
cdc_df = pd.read_csv ('/Users/matthewray/Desktop/Northeastern/PythonProjects/DS5010/Assignment3/COVID-19_Vaccinations_in_the_United_States_County.csv')
cdc_list_columns = cdc_df.columns.values.tolist()
print(cdc_list_columns)

drop_columns = ['MMWR_week', 'Completeness_pct', 'Administered_Dose1_Recip', 'Administered_Dose1_Pop_Pct', 'Administered_Dose1_Recip_5Plus', 'Administered_Dose1_Recip_5PlusPop_Pct', 'Administered_Dose1_Recip_12Plus', 'Administered_Dose1_Recip_12PlusPop_Pct', 'Administered_Dose1_Recip_18Plus', 'Administered_Dose1_Recip_18PlusPop_Pct', 'Administered_Dose1_Recip_65Plus', 'Administered_Dose1_Recip_65PlusPop_Pct', 'Series_Complete_Yes', 'Series_Complete_Pop_Pct', 'Series_Complete_5Plus', 'Series_Complete_5PlusPop_Pct', 'Series_Complete_12Plus', 'Series_Complete_12PlusPop_Pct', 'Series_Complete_65Plus', 'Series_Complete_65PlusPop_Pct', 'Booster_Doses', 'Booster_Doses_Vax_Pct', 'Booster_Doses_18Plus', 'Booster_Doses_18Plus_Vax_Pct', 'Booster_Doses_50Plus', 'Booster_Doses_50Plus_Vax_Pct', 'Booster_Doses_65Plus', 'Booster_Doses_65Plus_Vax_Pct', 'SVI_CTGY', 'Series_Complete_Pop_Pct_SVI', 'Series_Complete_5PlusPop_Pct_SVI', 'Series_Complete_12PlusPop_Pct_SVI', 'Series_Complete_18PlusPop_Pct_SVI', 'Series_Complete_65PlusPop_Pct_SVI', 'Metro_status', 'Series_Complete_Pop_Pct_UR_Equity', 'Series_Complete_5PlusPop_Pct_UR_Equity', 'Series_Complete_12PlusPop_Pct_UR_Equity', 'Series_Complete_18PlusPop_Pct_UR_Equity', 'Series_Complete_65PlusPop_Pct_UR_Equity', 'Census2019', 'Census2019_5PlusPop', 'Census2019_12PlusPop', 'Census2019_65PlusPop']
cdc_df.drop(columns=drop_columns, inplace=True)
print(cdc_df.columns)   
print(cdc_df)

cdc_df_cl = cdc_df[cdc_df['FIPS'].notna()]
print(cdc_df_cl)

cdc_df_cl['Date']=pd.to_datetime(cdc_df_cl.Date,errors='coerce')

cdc_df_cl['Unique_id'] = cdc_df_cl.Date.astype(str) + '_' + cdc_df_cl.FIPS.astype(str)
print(cdc_df_cl)
```
- Step 6: Merge the two datasets using the unique identifier to create a complete dataset with vaccine and death data. Export to .csv
```
combined_data = pd.merge(cdc_df_cl, jhu_df_cl)
list_columns = combined_data.columns.values.tolist()
print(list_columns)
print(combined_data)

combined_data.to_csv()
```
#### Final Dataset (As Promised): https://github.com/MatthewjRay/5010_Data/raw/main/Combined_CovidData_Clean.csv

## Analyzing Data

Objective: Determine the relationship between vaccination rates 18+ and covid deaths rates over time. 

TL;DR: To skip the tutorial, run: Assignment_5_Covid_Time_Series.py
https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Assignment_5_Covid_Time_Series.py


Now that there is a clean, consolidated dataset, it is time to have some fun. Let's dig in and take a look. 

The first thing that needs to be done is to get the file loaded into python as a dataframe. Good thing the link is public and the pandas package exists. 
```
url = 'https://github.com/MatthewjRay/5010_Data/raw/main/Combined_CovidData_Clean.csv'
df = pd.read_csv(url, converters={'FIPS' : str})
df = pd.read_csv(url)
```
Now we can start plotting!!
... but first we need to make some additional updates to our data. 

Plotting everyday would result in 213 points to be plotted, resulting in a mess of a graph (ask me how I know). 
Because of this, we can add a month data column and group our data by month using the groupby function. 
We also want to add a percentage of deaths against the total population to compare with the percentage of fully vaccinated individuals. 
```
pd.to_datetime(df['Date'],)
df['Month'] = pd.DatetimeIndex(df['Date']).month_name().str[:3]
df['Death_Pct'] = df['Deaths'] / df['Census2019_18PlusPop'] * 100
df.head()

#[MR] Group plot data by month
grouped_death = df.groupby('Month')['Death_Pct'].mean()
grouped_vacc = df.groupby('Month')['Series_Complete_18PlusPop_Pct'].mean()
```

Finally, we get to plot. 
- The first plots are simple (although not that simple) variables against time. 

Plot deaths against total population by month.
```
fig, ax = plt.subplots(figsize=(15,7)) 

df.groupby('Month')['Death_Pct'].mean().plot(ax=ax)
ax.set(xlabel="Month", ylabel="% of Total Pop Deaths")
plt.title("% of Total Pop. Deaths Over Time (May - Nov 2021)")
```

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-02-22%20at%2011.33.06%20PM.png)


Plot % of total vaccinated individuals 18+ against total population by month.  
```
fig, ax = plt.subplots(figsize=(15,7)) 

df.groupby('Month')['Series_Complete_18PlusPop_Pct'].mean().plot(ax=ax)
ax.set(xlabel="Month", ylabel="% of Total Pop 18+ Vaccinated")
plt.title("% of 18+ Vaccinated Over Time (May - Nov 2021)")
```

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-02-22%20at%2011.33.21%20PM.png)


We have some pretty graphs, but they do not tell us much. Lets see if we can overlay the two to compare % of vaccinated against deaths to the total population by month. 
```
fig, ax1 = plt.subplots(figsize=(15,7))  

ax1.set_xlabel('Date') 
ax1.tick_params(axis ='x', which='major', labelcolor = 'black')
ax1.set_ylabel('% of population 18+ Vaccinated', color = 'black') 
plot_1 = df.groupby('Month')['Series_Complete_18PlusPop_Pct'].mean().plot(ax=ax1, color = "black")
ax1.tick_params(axis ='y', labelcolor = 'black') 

ax2 = ax1.twinx()
  
ax2.set_ylabel('% of Population Deaths', color = 'green') 
plot_2 = df.groupby('Month')['Death_Pct'].mean().plot(ax=ax2, color = "green")
ax2.tick_params(axis ='y', labelcolor = 'green') 

plt.title("% of 18+ Vaccinated Vs. % of Pop. Deaths Over Time (May - Nov 2021)")


plt.show()
```

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-02-22%20at%2011.33.35%20PM.png)


Now we are getting somewhere. We can see that the data is coorelated, but we have some more exploration to do and some future considerations. 

## Future Consideration

While the data certainly tells a story, the dates need to be ordered to really visualize the impact of vaccintion rates against death rates. 
I would have also liked to explore cases vs. vaccinations and a longer time period of data to see how the omicron variant impacted the analysis. 






  
