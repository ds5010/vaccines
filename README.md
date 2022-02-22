# ds5010/vaccines

The DS5010 Vaccines project is a collaborative effort to explore the efficacy of vaccination as a response to the COVID-19 pandemic. 

## About the Data
This project focuses on data for all the U.S counties for which relevant data was available, drawing from two different data sources, the CDC and Johns Hopkins University. 

### CDC Data
The CDC data in its entirety can be found at https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh. As of the creation of this README it is updated daily and contains 53 columns, including (but not limited to) data on the number and percentage of different age demographics who are partially vaccinated, fully vaccinated, and boosted, as well as geographic identifiers and census information. For the purposes of this project, those 53 columns were reduced to just 6 (using clean_vaccines.py): 

- FIPS (the unique string of digits used to identify each county)
- Recip_County (the name of each county)
- Recip_State (the name of the state each county is in)
- Series_Complete_18Plus (the number of people 18 and older in each county who are fully vaccinated, defined as having recived both doses of a two dose vaccine or one does of a single dose vaccine, regardless of booster status)
- Census2019_18PlusPop (the number of people in each county who were 18 or older according to the 2019 census)
- Date (the month/day/year the data corresponds to)

The FIPS data was included because it was a unique identifier that was also present in Johns Hopkins data tracking COVID deaths, making it easy to relate the vaccination data for a county to the death data for that same county. The name of each county and the corresponding state were included to make the data less abstract (as FIPS carries the same information as county and state names but isn't as easily understood) and to make it easier to look at specific geographic regions if one wanted to. The original dataset included a column for Series_Complete_18PlusPopPct that would have given the percent of people 18+ in each county who were fully vaccinated, but this would have made it trickier to calculate a statewide or nationwide percent if we were interested in that instead of a more specific county by county percent (which could still be calculated using these two columns of data, were that your druthers). The date was included so that changes could be tracked over time as the pandemic and the nation's response to it proceed. 

### JHU data
The Johns Hopkins University data in its entirety can be found at https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports. As of the creation of this README it is updated daily and contains 14 columns, including (but not limited to), FIPS numbers, geographic information, and data on the number of people who had active COVID cases, had recovered from COVID, or had died from COVID. For the purposes of this project these 14 columns were reduced to just 2 (using deaths.py):

- FIPS (the unique string of digits used to identify each county)
- Deaths (the number of COVID deaths in a county)

The FIPS data was included to make this data easily compatible with the CDC data (which also includes FIPS), and the deaths data was included to allow for examination of how vaccination rates relate to death rates. 

## Examples
For the purposes of these examples we're going to be working just with the subset of the population that is 18 and older since, at least in the window of time we're looking at, this is the group that was elligible for the vaccine for the entire duration. We can write a program (area_graph.py) to graph the number of deaths in relation to the percent of the population who was fully vaccinated (in this case defined as either having received both shots of a two shot vaccine or one shot of a single shot vaccine, not including booster shots), where the size of the dots being plotted is representative of the population of the county represented by that dot: 

```
import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/ds5010/spring-2022/main/data/merge.csv"
df = pd.read_csv(url, converters={'FIPS' : str})
df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

xlabel = 'Series_Complete_18PlusPop_Pct'
ylabel = 'Deaths_Per_1e5'

x = df[xlabel]
y = df[ylabel]
area = df['Census2019_18PlusPop'] / 1e4

fig, ax = plt.subplots()
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xlim(0,100)
ax.set_ylim(0,500)
fig.set_size_inches(8,8)

scatter = ax.scatter(x, y, s=area, alpha=0.5)
```

Which procudes the following scatterplot: 

![](https://github.com/ds5010/vaccines/blob/bridget_dev_final/area_graph.png)

If we wanted to look at data for how death rates change in relation to vaccination rates over a period of time (in this case from 1 May 2021 - 30 November 2021), we could run a program (graph_over_time.py) to do so: 

```
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('vaccinations_and_deaths_file.csv.gz', low_memory=False)

may_death_data = df.loc[df['Month'] == "May", 'Deaths'].sum()
june_death_data = df.loc[df['Month'] == "June", 'Deaths'].sum()
july_death_data = df.loc[df['Month'] == "July", 'Deaths'].sum()
august_death_data = df.loc[df['Month'] == "August", 'Deaths'].sum()
september_death_data = df.loc[df['Month'] == "September", 'Deaths'].sum()
october_death_data = df.loc[df['Month'] == "October", 'Deaths'].sum()
november_death_data = df.loc[df['Month'] == "November", 'Deaths'].sum()

may_pop_data = df.loc[df['Month'] == "May", 'Census2019_18PlusPop'].sum()
june_pop_data = df.loc[df['Month'] == "June", 'Census2019_18PlusPop'].sum()
july_pop_data = df.loc[df['Month'] == "July", 'Census2019_18PlusPop'].sum()
august_pop_data = df.loc[df['Month'] == "August", 'Census2019_18PlusPop'].sum()
september_pop_data = df.loc[df['Month'] == "September", 'Census2019_18PlusPop'].sum()
october_pop_data = df.loc[df['Month'] == "October", 'Census2019_18PlusPop'].sum()
november_pop_data = df.loc[df['Month'] == "November", 'Census2019_18PlusPop'].sum()

may_vax_data = df.loc[df['Month'] == "May", 'Series_Complete_18Plus'].sum()
june_vax_data = df.loc[df['Month'] == "June", 'Series_Complete_18Plus'].sum()
july_vax_data = df.loc[df['Month'] == "July", 'Series_Complete_18Plus'].sum()
august_vax_data = df.loc[df['Month'] == "August", 'Series_Complete_18Plus'].sum()
september_vax_data = df.loc[df['Month'] == "September", 'Series_Complete_18Plus'].sum()
october_vax_data = df.loc[df['Month'] == "October", 'Series_Complete_18Plus'].sum()
november_vax_data = df.loc[df['Month'] == "November", 'Series_Complete_18Plus'].sum()

may_death_plot = may_death_data
june_death_plot = june_death_data
july_death_plot = july_death_data
august_death_plot = august_death_data
september_death_plot = september_death_data
october_death_plot = october_death_data
november_death_plot = november_death_data

may_vax_plot = may_vax_data / may_pop_data
june_vax_plot = june_vax_data / june_pop_data
july_vax_plot = july_vax_data / july_pop_data
august_vax_plot = august_vax_data / august_pop_data
september_vax_plot = september_vax_data / september_pop_data
october_vax_plot = october_vax_data / october_pop_data
november_vax_plot = november_vax_data / november_pop_data

death_plot = [may_death_plot, june_death_plot, july_death_plot, august_death_plot, september_death_plot, october_death_plot, november_death_plot]
vax_plot = [may_vax_plot, june_vax_plot,july_vax_plot, august_vax_plot, september_vax_plot, october_vax_plot, november_vax_plot]

#df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
#df['Vaccinated_Per_1e5'] = df['Series_Complete_18PlusPop_Pct']/ 100 * 1e5

#y1 = df['Deaths_Per_1e5']
#y2 = df['Vaccinated_Per_1e5']

y1 = death_plot
y2 = vax_plot

x = [0, 1, 2, 3, 4, 5, 6]
labels = ['May', 'June', 'July', 'August', 'September', 'October', 'November']

fig, ax1 = plt.subplots()

color = 'tab:blue'
plt.xticks(x, labels)
ax1.set_xlabel('Month 2021')
ax1.set_ylabel('Percent Vaccinated', color=color)  # we already handled the x-label with ax1
ax1.bar(x, y2, color=color)
ax1.tick_params(axis='y', labelcolor=color, )

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('Number of Deaths', color=color)
ax2.plot(x, y1, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
```

Which would generate the following graph:

![](https://github.com/ds5010/vaccines/blob/bridget_dev_final/graph_over_time.png)

Of course, looking only at a graph of the total deaths and vaccination rates across all counties (with available data) doesn't provide as clear a picture of vaccine effectiveness as we get if we also look at a comparison between two counties with similar population demographics but very different rates of vaccination. We can take two such counties, for example Kent County, RI and Tuscaloosa County, AL (graph_over_time_Kent_and_Tuscaloosa.py) and compare the number of deaths in relation to their differing vaccination percentages over the same May to November period we considered when looking at all the counties together: 

```
import matplotlib.pyplot as plt
import pandas as pd


df=pd.read_csv('vaccinations_and_deaths_file.csv.gz', low_memory=False)

may_death_data = df.loc[df['Month'] == "May", 'Deaths'].sum()
june_death_data = df.loc[df['Month'] == "June", 'Deaths'].sum()
july_death_data = df.loc[df['Month'] == "July", 'Deaths'].sum()
august_death_data = df.loc[df['Month'] == "August", 'Deaths'].sum()
september_death_data = df.loc[df['Month'] == "September", 'Deaths'].sum()
october_death_data = df.loc[df['Month'] == "October", 'Deaths'].sum()
november_death_data = df.loc[df['Month'] == "November", 'Deaths'].sum()

may_pop_data = df.loc[df['Month'] == "May", 'Census2019_18PlusPop'].sum()
june_pop_data = df.loc[df['Month'] == "June", 'Census2019_18PlusPop'].sum()
july_pop_data = df.loc[df['Month'] == "July", 'Census2019_18PlusPop'].sum()
august_pop_data = df.loc[df['Month'] == "August", 'Census2019_18PlusPop'].sum()
september_pop_data = df.loc[df['Month'] == "September", 'Census2019_18PlusPop'].sum()
october_pop_data = df.loc[df['Month'] == "October", 'Census2019_18PlusPop'].sum()
november_pop_data = df.loc[df['Month'] == "November", 'Census2019_18PlusPop'].sum()

may_vax_data = df.loc[df['Month'] == "May", 'Series_Complete_18Plus'].sum()
june_vax_data = df.loc[df['Month'] == "June", 'Series_Complete_18Plus'].sum()
july_vax_data = df.loc[df['Month'] == "July", 'Series_Complete_18Plus'].sum()
august_vax_data = df.loc[df['Month'] == "August", 'Series_Complete_18Plus'].sum()
september_vax_data = df.loc[df['Month'] == "September", 'Series_Complete_18Plus'].sum()
october_vax_data = df.loc[df['Month'] == "October", 'Series_Complete_18Plus'].sum()
november_vax_data = df.loc[df['Month'] == "November", 'Series_Complete_18Plus'].sum()

may_death_plot = may_death_data
june_death_plot = june_death_data
july_death_plot = july_death_data
august_death_plot = august_death_data
september_death_plot = september_death_data
october_death_plot = october_death_data
november_death_plot = november_death_data

may_vax_plot = may_vax_data / may_pop_data
june_vax_plot = june_vax_data / june_pop_data
july_vax_plot = july_vax_data / july_pop_data
august_vax_plot = august_vax_data / august_pop_data
september_vax_plot = september_vax_data / september_pop_data
october_vax_plot = october_vax_data / october_pop_data
november_vax_plot = november_vax_data / november_pop_data

death_plot = [may_death_plot, june_death_plot, july_death_plot, august_death_plot, september_death_plot, october_death_plot, november_death_plot]
vax_plot = [may_vax_plot, june_vax_plot,july_vax_plot, august_vax_plot, september_vax_plot, october_vax_plot, november_vax_plot]

#df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
#df['Vaccinated_Per_1e5'] = df['Series_Complete_18PlusPop_Pct']/ 100 * 1e5

#y1 = df['Deaths_Per_1e5']
#y2 = df['Vaccinated_Per_1e5']

y1 = death_plot
y2 = vax_plot

x = [0, 1, 2, 3, 4, 5, 6]
labels = ['May', 'June', 'July', 'August', 'September', 'October', 'November']

fig, ax1 = plt.subplots()

color = 'tab:blue'
plt.xticks(x, labels)
ax1.set_xlabel('Month 2021')
ax1.set_ylabel('Percent Vaccinated', color=color)  # we already handled the x-label with ax1
ax1.bar(x, y2, color=color)
ax1.tick_params(axis='y', labelcolor=color, )

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('Number of Deaths', color=color)
ax2.plot(x, y1, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
```
This generates the following graph, which illustrates a very stark difference between the number of deaths in a county with high vaccination rates (Kent, RI) and the number of deaths in a county with low vaccination rates (Tuscaloosa, AL):

![](https://github.com/ds5010/vaccines/blob/bridget_dev_final/graph_over_time_Kent_and_Tuscaloosa.png)

## Project Walkthrough
To replicate the results presented in this README take the following steps: 
1. Download repo. 
2. Run clean_vaccines.py by entering ```python3 clean_vaccines.py``` in the command line terminal. This will take the COVID-19_Vaccinations_in_the_United_States_County.csv.gz file (which includes the CDC data from 1 May 2021 - 30 November 2021) from the data folder and pull out only 
the six columns we want to preserve as outlined above. This will output a vaccines-cleaned.csv file. 
3. Run months_vaccines.py by entering ```python3 months_vaccines.py``` in the command line terminal. This will take the vaccines-cleaned.csv file you just created and add a "Months" column with a string of the relevant month name for each row of data (making it easier to look at data month by month over time). This will create a vaccinations-cleaned-with-months.csv file. 
4. Run deaths.py to get data for May 2021 by entering ```python3 deaths.py "05-01-2021" "05-31-2021``` in the command line terminal. This will create a file in the data folder called deaths-05-01-2021-05-31-2021.csv containing all the FIPS and death data for the month of May 2021 from the JHU data. Repeat this process, changing the start variable and end variable to be the first and last day of each subsequent month by changing the date strings entered in the command line terminal until you have files for May 2021 - November 2021. 
5. Run merged_deaths.py by entering ```python3 merged_deaths.py``` to merge all the death files you just created and add a column with the relevant month for each row of data. This will output a file called merged_deaths.csv. 
6. Run deaths_and_vaccines.py by entering ```python3 deaths_and_vaccines.py``` in the command line terminal. This will merge the vaccinations-cleaned-with-months.csv file of the CDC data we'll be working with with the merged_deaths.csv file of the JHU data we'll be working with. It will output a file named vaccinations_and_deaths_file.csv. 
7. If you want to create the first graph shown in this README (the scatterplot where the different sized dots relate to the population size of the county they represent), enter ```python3 area_graph.py``` in the command line terminal. 
8. If you want to create the second graph, showing the bar chart/line graph for vaccinations and deaths on a national scale, enter ```python3 graph_over_time.py``` in the command line terminal. 
9. If you want to create the third graph, showing the bar chart/line graph comparing vaccinations and deaths specifically in Kent County, RI and Tuscaloosa County, AL enter ```python3 comparing_deaths_and_vax_rates_overtime_in_KentRI_and_TuscaloosaAL.py``` in the command line terminal. 

## License
This project is licensed under the MIT license, a copy of which can be found in the license file, but just to reiterate: 

```
MIT License

Copyright (c) 2022 ds5010

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
