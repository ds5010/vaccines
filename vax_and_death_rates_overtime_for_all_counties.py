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
ax1.set_ylabel('Percent Vaccinated', color=color)
ax1.bar(x, y2, color=color)
ax1.tick_params(axis='y', labelcolor=color, )

ax2 = ax1.twinx()

color = 'tab:red'
ax2.set_ylabel('Number of Deaths', color=color)
ax2.plot(x, y1, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()
