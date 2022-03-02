# Is the Covid-19 Vaccine Effective?

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Covid_banner.jpg)

## Overview 
This analysis aims to explore the relationship between Covid-19 vaccinations and deaths attributed to Covid-19 in the U.S. between 5/31/21 - 11/30/21 to analyze the effectiveness of the Covid-19 vaccination over time.

## Data

Data related to the Covid-19 vaccination was sourced from the Center For Disease Control and Prevention (CDC) and data related to Covid-19 deaths was sourced from Johns Hopkins University (JHU).

To begin to assess the effectiveness of the vaccination over time, the % of the vaccinated population over 18 years of age (CDC) is compared to Covid related deaths per 100k (JHU). The data was then broken down by U.S. region (West, Midwest, South, Northeast) based on the [Census Bureau regional divisions](https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf), and a snapshot was of data was taken at the of each month to create a more accurate representation. Because the JHU cumulates deaths, the time series was adjusted to compute the difference in death figures between dates. 

**CDC Data**
```
https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh
```

**Johns Hopkins University Data**
```
https://github.com/CSSEGISandData/COVID-19/tree/f57525e860010f6c5c0c103fd97e2e7282b480c8
```

## Running The Code 

Run the [Assignment_5_Covid_Time_Series.py](https://github.com/ds5010/vaccines/blob/MatthewjRay_Assigment05/Assignment_5_Covid_Time_Series.py) file in the [MatthewjRay_Assigment05](https://github.com/ds5010/vaccines/tree/MatthewjRay_Assigment05) branch of the repository. The data links a public repository, so there shouldn't be any issues when running the code.  
    * Some of the code mirrors code from the class project (as does the README template) because I developed it for the class assignment. 

## Output & Analysis

### Cumulative Scatter Plot

The final output from class, gives us a good overall look at the Covid-19 data between 5/1/21 - 11/30/21. As a larger percent of the population is vaccinated the lower the number of deaths. This is a good sign that the vaccine could be effective. However, the U.S. is such a large set of data, I wanted to see how it could be segmented further. 

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-03-01%20at%207.09.30%20PM.png)

###  Cumulative Scatter Plot by Region

Having the FIPS codes allowed the data to be coded by state and region, presenting a different look into the data set. Broken down by region, the South has a lower vaccination rate in many of its counties and much higher number of deaths than other regions. 

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-03-01%20at%207.09.46%20PM.png)

### Time Series

As data from the beginning (May), middle (Aug), and end (Nov) of the time period is compared, we can see that overall, the vaccine is effective. As a greater percentage of the population becomes vaccinated the number of deaths declines. 

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-03-01%20at%207.10.10%20PM.png)
![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-03-01%20at%207.11.32%20PM.png)
![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-03-01%20at%207.11.52%20PM.png)

## Future Considerations

**Dataset**  
  * Compare different regions with similar population sizes 
  * Compare individual areas with higher vaccination rates against similar areas with lower vaccination rates
  * Subset data to explore effectiveness across different age ranges 
  * Segment date ranges and countes to align with peaks and valleys in Covid cases

**Code**  
  * Add regression line to better visualize trends in data
  * Explore the use of different chart types (map, bar chart, line graph)





  
