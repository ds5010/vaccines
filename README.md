# ds5010/vaccines

The DS5010 Vaccines project is a collaborative effort to explore the efficacy of vaccination as a response to the COVID-19 pandemic. 

## About the Data

### CDC Data
Download and compress the CDC vaccination data

```
make cdcdata
```

See Makefile for details.

### JHU data

TBD

### Merged Data

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

## License
This project is licensed under the MIT license, a copy of which can be found in the license file, but just to reiterate: 

```
```

## References
