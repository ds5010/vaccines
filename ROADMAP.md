
# Roadmap

* CDC data
  * Goal: Download and compress a file with the vaccine data
  * Rationale: The source CDC CSV is ~250M and constantly updated. We'll keep a stable version for reproducibility.
  * Status: DONE
    * Data downloaded 14 Feb is ~250M before compression, and almost 100M after gzip
  * Command: `make cdc` (see Makefile for details)
* Vaccine data
  * Goal: Create a CSV from the gzipped CDC data containing values needed for the baseline analysis.
  * Rationale: Our baseline for county-level vaccinations is "Series_Complete_18PlusPop_Pct" as of 11/30/2021
    * Fields: FIPS, Recip_County, Recip_State, Series_Complete_18PlusPop_Pct, Census2019_18PlusPop
  * Status: DONE
    * Output file: "./data/vaccines-11-30-2021.csv"
  * Command: `make vaccines` (see Makefile for details)
* Deaths data
  * Goal: Sample the JHU data and create a CSV with only those values used in the baseline analysis.
  * Rationale: Our baseline is the total number of deaths by county between May 1 and Nov 30, 2021
    * Fields: FIPS, deaths
  * Status: DONE
  * Command: `make deaths` (see Makefile for details)
* Merge data
  * Goal: A function that reads and merges the vaccine and deaths data, returning a single dataframe
  * Rationale: merged data used for EDA, including the baseline scatterplot
  * Status: Unknown
* Scatterplot
  * Goal: scatterplot of deaths/100K vs vaccination status for each county
  * Rationale: this will be a baseline data visualization
  * Status: Unknown
