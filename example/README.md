# CDC Vaccination data

* CDC article: https://www.cdc.gov/mmwr/volumes/71/wr/mm7104e2.htm
* Learning goals
  * work with compressed data
  * breaking things down into small steps
  * documenting data provenance
  * make the directory easy use -- for collaboration and for when you forget what you did
  * create the intermediate file with reproducible/necessary data for analysis and save it to disk
    * these can be saved to github if other files are too big
    * or you can use [Github's LFS](https://git-lfs.github.com/)
  * compare with pandas (notice the FIPS-related error when running that code)
* Reproducibility (can we reproduce the published results for age-adjusted death & vaccination rates)

## References

* [About vaccine data](https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html)
* [COVID-19 incidence and death rates](https://www.cdc.gov/mmwr/volumes/71/wr/mm7104e2.htm) -- CDC article
  * They compute "age-standardized" values for 25 jurisdictions
  * [Age adjustment](https://en.wikipedia.org/wiki/Age_adjustment) definition -- wikipedia
  * [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) -- wikipedia

## Data provenance

* CDC website: https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh
  * This is the "Export >> CSV" dropdown option on
  * Download URL: https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
* CSV file was downloaded 2 Feb 2022
  * 240MB uncompressed
  * I gzipped the file to 81M
  ```
  $ gzip filename
  ```
  * According to the website:
    * data & metadata were last updated 1 Feb 2022
    * 1.36M rows and 51 columns
* 14M for just a few columns gzip'ed
* 132K for 1 day (uncompressed)
* Note from code examples how little we need to change to work with compressed data

## Sanity check

Homework assignment asked the following

* Find a metric that you can use to verify that you're correctly accessing the data.
* For example, try reproducing any of the published results.
* The goal here is not to reproduce all of the results
  * but simply to provide a sanity check on our ability to extract and analyze the data.
* Published result
  * https://covid.cdc.gov/covid-data-tracker/#vaccinations_vacc-total-admin-rate-total
  * On 9 Feb, this page reports: 213.1M fully vaccinated
* Check the data source...
  * Column header: Series_Complete_Yes
    * Data Dictionary: Total number of people who are fully vaccinated
    * (have second dose of a two-dose vaccine or one dose of a single-dose vaccine)
    * based on the jurisdiction and county where recipient lives
  * Column header: Series_Complete_5Plus
    * Data dictionary: Total number of people 5+ who are fully vaccinated
    * (have second dose of a two-dose vaccine or one dose of a single-dose vaccine)
    * based on the jurisdiction where recipient lives
  * Reference: https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-County/8xkx-amqh
* The sanity check (result of running "make test")
  * 11/30/2021: Series_Complete_Yes for 194,692,655
  * 02/01/2022: Series_Complete_Yes total: 210,108,362
  * 02/01/2022: Series_Complete_5Plus total: 210,097,241
