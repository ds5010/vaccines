# DS5010 Spring 2022
## **Tim Moriarity**
### Vaccine Effectiveness

Packages:
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```


Loading data into Pandas Dataframe:
```
url = "https://raw.githubusercontent.com/ds5010/spring-2022/main/data/merge.csv"
df = pd.read_csv(url, converters={'FIPS' : str})
```

Generating new data columns for easier understanding and visualization:
```
df['Vaccination%'] = df['Series_Complete_18PlusPop_Pct']
df['Population'] = df['Census2019_18PlusPop']
df['Deaths_per_1k'] = (df['Deaths']/df['Population'])*1000
df['Population_adjusted'] = df['Population']/1000
```

Scatterplot:
```
xlabel = 'Vaccination%'
ylabel = 'Deaths_per_1k'

x = df[xlabel]
y = df[ylabel]
area = df['Population'] / 10000

fig, ax = plt.subplots()
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.set_xlim(0,100)
ax.set_ylim(0,6)
fig.set_size_inches(12,12)

scatter = ax.scatter(x, y, s=area, alpha=.6)

handles, labels = scatter.legend_elements(prop='sizes', alpha=0.4, num='auto')
ax.legend(handles, labels, loc="upper right", title="Population Sizes (x10k)", labelspacing=2, borderpad=1)
```
