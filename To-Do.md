**Look at the issues page for most up to date to do items**

1. Align schedules with team members -- see [SCHEDULES.md](./SCHEDULES.md)
2. Finalize project objective. -- DONE
  * Objective: Explore vaccination rate against death rate.
  * Start time: when vaccinations first became available -- May 1
  * End time: when Omicron emerges -- end of November
  * Get data for vaccination rates as of the end of November (fully vaccinated/100K)
  * Get data for deaths that occurred during the period May through Nov, when vaccinations were available.
3. Determine source(s) for Covid data. -- DONE
  * CDC (https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh)
  * Johns Hopkins (https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports)
  * FIPS codes can be used to merge data at the county level
  * Other data ?? -- Maybe later: CDC and JHU should have everything we need for step #2
4. Check datasets in Python for accuracy against source files. 
  * This should be done at various stages and documented.
5. Vaccination data
  * Download and compress the vaccination data -- DONE
  * Someone may want to extract the desired fields from the downloaded data
  * Hint: Use [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
    * `.read_csv()` returns a [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
6. Mortality data
  * Someone should get the mortality data from JHU repository on github
  * It may not be necessary to download all the files -- they can be processed in place.
    * Hint: Use [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
      * the `.read_csv()` method will read data directly from a URL
      * `.read_csv()` returns a [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
    * Clean data set.
    * Remove erroneous data.
    * Remove unneeded columns. 
    * Compute the sums
    * Save only the desired fields to a local file
    * Hint: Look at [pandas.DataFrame.to_csv()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
      * every pandas DataFrame instance has a `.to_csv()` method that can write to a file.
7. Combine and plot the datasets to create full set of data that includes vaccination and mortality data.
   * It probably make senses to combine the data as part of the plotting step
   * Again, you should consider using pandas.
8. Perform EDA 
   * Scatterplot
   * Choropleth
