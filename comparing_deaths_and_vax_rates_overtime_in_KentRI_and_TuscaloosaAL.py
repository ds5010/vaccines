import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv('vaccinations_and_deaths_file.csv.gz', low_memory=False, converters={'FIPS' : str})
df1 = df[df['FIPS'].str.contains('44003')]
df2 = df[df['FIPS'].str.contains('1125')]

may_death_data_Kent = df1.loc[df['Month'] == "May", 'Deaths'].sum()
june_death_data_Kent = df1.loc[df['Month'] == "June", 'Deaths'].sum()
july_death_data_Kent = df1.loc[df['Month'] == "July", 'Deaths'].sum()
august_death_data_Kent = df1.loc[df['Month'] == "August", 'Deaths'].sum()
september_death_data_Kent = df1.loc[df['Month'] == "September", 'Deaths'].sum()
october_death_data_Kent = df1.loc[df['Month'] == "October", 'Deaths'].sum()
november_death_data_Kent = df1.loc[df['Month'] == "November", 'Deaths'].sum()

may_pop_data_Kent = df1.loc[df['Month'] == "May", 'Census2019_18PlusPop'].sum()
june_pop_data_Kent = df1.loc[df['Month'] == "June", 'Census2019_18PlusPop'].sum()
july_pop_data_Kent = df1.loc[df['Month'] == "July", 'Census2019_18PlusPop'].sum()
august_pop_data_Kent = df1.loc[df['Month'] == "August", 'Census2019_18PlusPop'].sum()
september_pop_data_Kent = df1.loc[df['Month'] == "September", 'Census2019_18PlusPop'].sum()
october_pop_data_Kent = df1.loc[df['Month'] == "October", 'Census2019_18PlusPop'].sum()
november_pop_data_Kent = df1.loc[df['Month'] == "November", 'Census2019_18PlusPop'].sum()

may_vax_data_Kent = df1.loc[df['Month'] == "May", 'Series_Complete_18Plus'].sum()
june_vax_data_Kent = df1.loc[df['Month'] == "June", 'Series_Complete_18Plus'].sum()
july_vax_data_Kent = df1.loc[df['Month'] == "July", 'Series_Complete_18Plus'].sum()
august_vax_data_Kent = df1.loc[df['Month'] == "August", 'Series_Complete_18Plus'].sum()
september_vax_data_Kent = df1.loc[df['Month'] == "September", 'Series_Complete_18Plus'].sum()
october_vax_data_Kent = df1.loc[df['Month'] == "October", 'Series_Complete_18Plus'].sum()
november_vax_data_Kent = df1.loc[df['Month'] == "November", 'Series_Complete_18Plus'].sum()

may_vax_plot_Kent = may_vax_data_Kent / may_pop_data_Kent
june_vax_plot_Kent = june_vax_data_Kent / june_pop_data_Kent
july_vax_plot_Kent = july_vax_data_Kent / july_pop_data_Kent
august_vax_plot_Kent = august_vax_data_Kent / august_pop_data_Kent
september_vax_plot_Kent = september_vax_data_Kent / september_pop_data_Kent
october_vax_plot_Kent = october_vax_data_Kent / october_pop_data_Kent
november_vax_plot_Kent = november_vax_data_Kent / november_pop_data_Kent

death_plot_Kent = [may_death_data_Kent, june_death_data_Kent, july_death_data_Kent, august_death_data_Kent, september_death_data_Kent, october_death_data_Kent, november_death_data_Kent]
vax_plot_Kent = [may_vax_plot_Kent, june_vax_plot_Kent, july_vax_plot_Kent, august_vax_plot_Kent, september_vax_plot_Kent, october_vax_plot_Kent, november_vax_plot_Kent]

may_death_data_Tuscaloosa = df2.loc[df['Month'] == "May", 'Deaths'].sum()
june_death_data_Tuscaloosa = df2.loc[df['Month'] == "June", 'Deaths'].sum()
july_death_data_Tuscaloosa = df2.loc[df['Month'] == "July", 'Deaths'].sum()
august_death_data_Tuscaloosa = df2.loc[df['Month'] == "August", 'Deaths'].sum()
september_death_data_Tuscaloosa = df2.loc[df['Month'] == "September", 'Deaths'].sum()
october_death_data_Tuscaloosa = df2.loc[df['Month'] == "October", 'Deaths'].sum()
november_death_data_Tuscaloosa = df2.loc[df['Month'] == "November", 'Deaths'].sum()

may_pop_data_Tuscaloosa = df2.loc[df['Month'] == "May", 'Census2019_18PlusPop'].sum()
june_pop_data_Tuscaloosa = df2.loc[df['Month'] == "June", 'Census2019_18PlusPop'].sum()
july_pop_data_Tuscaloosa = df2.loc[df['Month'] == "July", 'Census2019_18PlusPop'].sum()
august_pop_data_Tuscaloosa = df2.loc[df['Month'] == "August", 'Census2019_18PlusPop'].sum()
september_pop_data_Tuscaloosa = df2.loc[df['Month'] == "September", 'Census2019_18PlusPop'].sum()
october_pop_data_Tuscaloosa = df2.loc[df['Month'] == "October", 'Census2019_18PlusPop'].sum()
november_pop_data_Tuscaloosa = df2.loc[df['Month'] == "November", 'Census2019_18PlusPop'].sum()

may_vax_data_Tuscaloosa = df2.loc[df['Month'] == "May", 'Series_Complete_18Plus'].sum()
june_vax_data_Tuscaloosa = df2.loc[df['Month'] == "June", 'Series_Complete_18Plus'].sum()
july_vax_data_Tuscaloosa = df2.loc[df['Month'] == "July", 'Series_Complete_18Plus'].sum()
august_vax_data_Tuscaloosa = df2.loc[df['Month'] == "August", 'Series_Complete_18Plus'].sum()
september_vax_data_Tuscaloosa = df2.loc[df['Month'] == "September", 'Series_Complete_18Plus'].sum()
october_vax_data_Tuscaloosa = df2.loc[df['Month'] == "October", 'Series_Complete_18Plus'].sum()
november_vax_data_Tuscaloosa = df2.loc[df['Month'] == "November", 'Series_Complete_18Plus'].sum()

may_vax_plot_Tuscaloosa = may_vax_data_Tuscaloosa / may_pop_data_Tuscaloosa
june_vax_plot_Tuscaloosa = june_vax_data_Tuscaloosa / june_pop_data_Tuscaloosa
july_vax_plot_Tuscaloosa = july_vax_data_Tuscaloosa / july_pop_data_Tuscaloosa
august_vax_plot_Tuscaloosa = august_vax_data_Tuscaloosa / august_pop_data_Tuscaloosa
september_vax_plot_Tuscaloosa = september_vax_data_Tuscaloosa / september_pop_data_Tuscaloosa
october_vax_plot_Tuscaloosa = october_vax_data_Tuscaloosa / october_pop_data_Tuscaloosa
november_vax_plot_Tuscaloosa = november_vax_data_Tuscaloosa / november_pop_data_Tuscaloosa

death_plot_Tuscaloosa = [may_death_data_Tuscaloosa, june_death_data_Tuscaloosa, july_death_data_Tuscaloosa, august_death_data_Tuscaloosa, september_death_data_Tuscaloosa, october_death_data_Tuscaloosa, november_death_data_Tuscaloosa]
vax_plot_Tuscaloosa = [may_vax_plot_Tuscaloosa, june_vax_plot_Tuscaloosa, july_vax_plot_Tuscaloosa, august_vax_plot_Tuscaloosa, september_vax_plot_Tuscaloosa, october_vax_plot_Tuscaloosa, november_vax_plot_Tuscaloosa]

y1Kent = vax_plot_Kent
y1Tuscaloosa = vax_plot_Tuscaloosa

y2Kent = death_plot_Kent
y2Tuscaloosa = death_plot_Tuscaloosa

x = [0, 1, 2, 3, 4, 5, 6]
labels = ['May', 'June', 'July', 'August', 'September', 'October', 'November']

fig, ax1 = plt.subplots()

color1 = 'tab:blue'
color2 = 'tab:orange'
x = np.arange(len(labels))
width = 0.35  
plt.xticks(x, labels)
ax1.set_xlabel('Month 2021')
ax1.set_ylabel('Percent Vaccinated') 
Kent_vax = ax1.bar(x - width/2, y1Kent, width, color=color1, label = '% Vaxxed Kent')
Tuscaloosa_vax = ax1.bar(x + width/2, y1Tuscaloosa, width, color=color2, label = '% Vaxxed Tuscaloosa')
ax1.tick_params(axis='y')

ax1.legend(loc='upper left')

ax2 = ax1.twinx()  

color1 = 'tab:red'
color2 = 'tab:gray'
ax2.set_ylabel('Number of Deaths')
Kent_death = ax2.plot(x, y2Kent, color=color2, label = '# of Deaths Kent')
Tuscaloosa_death = ax2.plot(x, y2Tuscaloosa, color=color1, label = '# of Deaths Tuscaloosa')
ax2.tick_params(axis='y')

ax2.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
                      ncol=2, mode="expand", borderaxespad=0.)

fig.tight_layout()  
plt.show()
