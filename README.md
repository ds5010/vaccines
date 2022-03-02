# vaccines

Collaborative project to investigate vaccine effectiveness

## Assignment05
The purpose of this project is to use the data collected from CDC website and JHU website to do the EDA of the effectiveness of the vaccines according to the period which starts from May.01,2021 to Nov.30,2021.
The following steps show how I use the datas to anaylze the vaccination effectiveness:

### Vaccine Data from CDC website
In the CDC website, we can find the data about the population who are 18+ years old and have received the full series of vaccines. Then I have created a [vaccines.py](https://github.com/ds5010/vaccines/blob/jerry_assignment05/assignment05/vaccines.py) file to output these data into 7 different csv files according to the time period, such as vaccinations-05-01-2021.csv. You can also find these csv file in the directory of data.

```
make vaccines.py
```

###  Death Data from JHU website
In the JHU website, we can find the data about the situations of death cases in different counties and states inside the United States. I use [death.py](https://github.com/ds5010/vaccines/blob/jerry_assignment05/assignment05/deaths.py) to output these data also into 7 different csv files by the time period, such as dealths-05-01-2021-to-06-01-2021.csv. Each csv file have the same start date, which is May.01,2021, and have different ending dates, such as June.01,2021 and so on. You can find these csv file in the directory of data.

```
make death.py
```

### Merge vaccine data and death data
In this section, I wrote a file which is called [merge-vaccination-and-deaths.py](https://github.com/ds5010/vaccines/blob/jerry_assignment05/assignment05/merge-vaccination-and-deaths.py). In this file, you can merge two different datasets into one csv file by the "FIPS" code during the time processing. Take [vaccinations-and-deaths-May-2021.csv] as an example, you can find the data which happened during the time in May, which includes the number of vaccination rate for each counties and states, the total of population in each counties in the specific state by Census, and the number of death cases in May.

```
make merge-vaccination-and-deaths.py
```

### Plot the scatter plots
In this part, I wrote a file which is called [ploitit.py](https://github.com/ds5010/vaccines/blob/jerry_assignment05/assignment05/plotit.py). In this file, I use two variables to do the scatterplots for each month to show the data visualization, which are the death rate vs the vaccination rate. The death rate is calculated by (death cases in the specified county)/(the total population in the specified county). And the vaccination rate is the number of Series_Complete_18PlusPop_Pct. Then I set the vaccination rate as the xlabel and the death rate as the ylabel. After I get the graphs for each month, I store them under the directory of img.

```
make poltit.py
```
### Here are some examples of data visualization.
This is the graph in May.

![May](https://user-images.githubusercontent.com/97610834/156292669-f98047ba-01f5-4ebb-a92a-653ceaf85ce9.png)

This is the graph in August.

![Aug](https://user-images.githubusercontent.com/97610834/156292726-f14552cb-bb72-4e8c-bee1-4adac16f4c5f.png)

This is the graph in Novomber.

![Nov](https://user-images.githubusercontent.com/97610834/156292746-43a126db-54d1-4c4b-a341-c77770ecd059.png)

### My analysis according to the graph visualizations
According to these 7 graphs, I found that during May to Novomeber, the vaccination rate keep increasing. But during the period from August to October, there was a sudden spike in the death rate. After I have searched on the Internet, I found that the Omicron virus happened from September. It indicates that why the reason the scatter graphs show there was a sudden increase happened. In the conclusion, I suppose that the vaccination rate is keep increasing and the death rate is keep decreasing, which means the vaccines are effective to us.
