# Exploring Covid-19 Vaccine Effectiveness

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-03-01%20at%208.40.31%20AM%20(1).jpg)

## Overview 
This analysis aims to explore the relationship between Covid-19 vaccinations and deaths attributed to Covid-19 in the U.S. between 5/31/21 - 11/30/21 to analyze the effectiveness of the Covid-19 vaccination over time.

## Data

Data related to the Covid-19 vaccination was sourced from the Center For Disease Control and Prevention (CDC) and data related to Covid-19 deaths was sourced from Johns Hopkins University (JHU).

To begin to assess the effectiveness of the vaccination over time, the % of the vaccinated population over 18 years of age (CDC) is compared to Covid related deaths per 100k (JHU). The data was broken down by U.S. region (West, Midwest, South, Northeast) based on the [Census Bureau regional divisions](https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf), and a snapshot was of data was taken at the of each month to create a more accurate representation. Because the JHU cumulates deaths, the time series was adjusted to compute the difference in death figures between dates. 

**CDC Data**
```
https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh
```

**Johns Hopkins University Data**
```
https://github.com/CSSEGISandData/COVID-19/tree/f57525e860010f6c5c0c103fd97e2e7282b480c8
```

## Running The Code 

A [makefile](https://github.com/ds5010/vaccines/blob/026e1fcd37258919abd97fb9b69afcb1156bfb90/Makefile) has been created to streamline code compilation.  
To execute, clone the vaccines repotitory to local drive & run the makefile outlined below. 

Create a data directory.
```
datadir:
	mkdir -p data
```
Download and compress the CDC data.
```
cdc: data/
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz
```
Create a CSV file CDC vaccinations data.
```
vaccines: data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz
	mkdir -p data/CDC
	python -B src/vaccines.py
```
Create CSV file for JHU deaths data.

```
deaths: data/
	mkdir -p data/JHU
	python -B src/JHU_data.py
```
Merge the CDC vaccination dataset with the JHU deaths dataset and clean dataset to remove non U.S. data.
```
merge_v1:
	python -B src/merge.py

merge_v2: data/JHU/ data/CDC/
	mkdir -p data/Merge
	python -B src/merge_v2.py

make clean:
	rm -r data
```
Create series of scatter plots, save .png files to 'img' directory
```
scatters:
	python -B src/scatters.py
```
Create single scatterplot and an animated time series of vaccinated % of population vs deaths per 100,000.
```
test:
	python -B src/test.py

animation: img/*.png
	python -B src/animation_option2.py
```

## Output

![](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/animation.gif)

## Analysis

As a more significant percentage of the population becomes vaccinated, deaths increase over time. However, this does not consider the increase in Covid-19 cases over the same time period. Regionally, the South has a much lower vaccination rate among its population but a much higher increase in deaths, indicating that the opposite may be true. As a more significant percentage of a population becomes vaccinated, deaths trend downward.  Overall, there is much more to uncover within the data and areas for additional exploration.

## Future Considerations

**Dataset**  
  * Compare different regions with similar population sizes 
  * Compare individual areas with higher vaccination rates against similar areas with lower vaccination rates
  * Subset data to explore effectiveness across different age ranges 
  * Segment date ranges and countes to align with peaks and valleys in Covid spread

**Code**  
  * Add regression line to better visualize trends in data
  * Explore the use of different chart types (map, bar chart, line graph)

### Contributors

![alt text](https://github.com/ds5010/vaccines/raw/MatthewjRay_Assigment05/Screen%20Shot%202022-03-01%20at%204.29.38%20PM.png)

[Philip Bogden](https://github.com/pbogden) | [Sophia Cofone](https://github.com/sophiacofone) | [Qiwei "Jerry" Hu](https://github.com/JerryV77) |
[Connor Lynch](https://github.com/CCLynch) | [Philip Mathieu](https://github.com/PhilipMathieu) | [Bridget Mohler](https://github.com/b-mohler) |
[Matthew Ray](https://github.com/MatthewjRay) | [Kayne Ryan](https://github.com/kayneryan) | [Zeng Yune](https://github.com/zyune) |
