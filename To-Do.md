1. Align schedules with team members.
2. Finalize project objective.
   * Explore vaccination rate against death rate, but what time frame? 
   * Start time: when vaccinations first became available -- May 1
   * End time when Omicron started to dominate -- end of November
   * Vaccination rates as of end of November (fully vaccinated/100K)
   * Deaths: new deaths during the period May through Nov.
3. Determine source(s) for Covid data.
   * CDC (https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh)
   * Johns Hopkins (https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports)
   * Other ?? -- Maybe later: DCD and JHU should have everything we need for step #2
4. Identify overlapping identifiers between data sets. -- FIPS
5. Import datasets into Python.
   * Someone should get the vaccination data
   * Someone else should get the deaths data
   * Clean data set.
     * Remove erroneous data.
     * Remove unneeded columns. 
   * Compute the sums
6. Combine datasets to create full set of data that includes vaccination and mortality data.
   * It may make sense to combine the data as part of the plotting step
8. Check dataset in Python for accuracy against source files. 
   * This should be done at various stages
9. Perform EDA 
   * Scatterplot
   * Choropleth
