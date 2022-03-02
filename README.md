# Assignment 05

**_Update March 1, 2022_**
*I am updating this README with instructions for the user to pull data from multiple sources, merge it together and create a GIF that shows vaccination rates vs. death rates for counties across the United States over the period from May 1 - November 30, 2021. I will indicate updates to the original assignment in italicized text.*

To analyze the effectiveness of the COVID-19 vaccines over time, I decided to 
create a GIF that showed how the scatterplot we developed in class changed 
between June 01, 2021 and November 30, 2021. 

I adapted the vaccines.py, deaths.py and combinedata.py files so that 
they could create multiple datasets. *After cloning the repo and while in the* kayne-assignment05 *branch, the user can run the following commands on the command line:*

* **make cdc** _will pull the latest file on vaccinations from the CDC website and gzip it_
* **make vaccines** _will use vaccines.py to create seven .csv files at the selected dates_
* **make deaths** _will use deaths.py to create seven .csv files at the selected dates by pulling data from Johns Hopkins University_
* **make merged** _will use combinedata.py to merge a vaccine data file and a deaths file using the common FIPS field. It will result in seven .csv files._
* **make scatters** _will use the merged datasets to run scatters.py, which creates seven .png files_
* **make gif** _will stitch those image files together into a .gif file, as seen below!_

![GIF for vax_effectiveness](https://github.com/ds5010/vaccines/blob/kayne-assignment05/img/vax_effectiveness.gif)
  

_In my original submission, I relied on an offline process that relied on converting filetypes and uploading a special graphics package into the active directory. In class, we discovered the **imageio** package, so I shifted tactics and used that package. I want to be clear, I coded this section on my own and did not rely on the group effort that's due as part of Assignment 06._
  

### Data Provenance ###
The CDC vaccination data comes from [here](https://data.cdc.gov/api/views/8xkx-amqh).  

The JHU death data comes from [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports).  


