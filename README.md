# DS5010 Spring 2022
## **Tim Moriarity**
### Vaccination rate at various points in time compared with death rate

The start uses makefile to create 3 different data sets at 3 different points during the vaccine rollout.

* The Original Baseline
* Midsummer 2021
* Current Date

Data was then put into Pandas Dataframes
Data columns for easier understanding and visualization:
```
df['Vaccination%'] = df['Series_Complete_18PlusPop_Pct']
df['Population'] = df['Census2019_18PlusPop']
df['Deaths_per_1k'] = (df['Deaths']/df['Population'])*10000
df['Population_adjusted'] = df['Population']/10000
```

![Baseline Scatterplot](https://github.com/ds5010/vaccines/blob/theBranchOfTim/baseline_scatter.png)
