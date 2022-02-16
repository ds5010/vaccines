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
    * Kayne 2/14: I uploaded a couple of programs that can help us check the status of the datasets
5. Vaccination data
  * Download and compress the vaccination data -- DONE
  * Someone may want to extract the desired fields from the downloaded data
  * Hint: Use [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
    * `.read_csv()` returns a [pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
    * Kayne 2/14: ...anybody who already is familiar with Pandas want to take a stab at this?
6. Mortality data
  * Someone should get the mortality data from JHU repository on github
  * It may not be necessary to download all the files -- they can be processed in place.
    * Kayne 2/14: I downloaded select files (May 1, June 1, July 1, Aug 1, Sep 1, Oct 1, Nov 1, Dec 1)... wasn't sure how to code it to run in place
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
     * Kayne 2/14: What are people thinking for the visuals? Will we need multiple scatterplots to show the changes over time? Are we going to include all 3000ish FIPS? I think it would be great to show:
       * 8 scatterplots, one for each month, depicting dots for all 3000ish FIPS
         * Do we need to filter out any that have data from one source but missing from the other?
       * size of dot = index based on population of county
       * X-axis is vaccination rate
       * Y-axis is death rate
   * Choropleth
