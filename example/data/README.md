
# Data provenance

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
