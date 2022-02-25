
# Roadmap
**Updated 2/24 for completion by 2/29*
## Core Tasks
We want to focus on creating a finished product first, which has been discussed and decided as a series of scatterplots combined into an animation. Once core task are accomplished, there a list of possible enhancements afterwards
* ### CDC Data - Connor & Jerry  
  * Takes **desired date** via command line
  * Work to remove all hardcoded dates and links
  * returns a dataframe for merge function
  * Possibly take column names as optional arguments?

* ### JHU Data - Yune & Jerry
  * Takes **end date** and **start date** via command line
  * Work to remove all hardcoded dates and links
  * returns a dataframe for merge function

* ### Merge - Tim & Yune
  * Remove hard coded dates as much as possible
  * Communicate with the CDC and JHU folks to call their functions within merge
  * Try the dataframes merge option that Prof. Bogden mentioned
  * If the dataframes merge doesn't happen, we can revert back to writing intermediate vaccine-only & deaths-only csv files to the data folder and using the existing merge code
  * returns dataframe for scatterplot function

* ### Scatterplot - Matt & Kayne
  * Create a scatterplot with the dataframe from Merge
  * Plot Vaccination rate on x-axis, Deaths per 10k on y-axis, population of county as dot size
  * Create img folder
  * Create multiple plots over time and save to img folder

* ### Time Sequence + Animation - Sophia & Bridget
  * Create gif/video with imageio package, using contents of img folder
  * Save or play the animation? 

* ### README - Matt & Kayne
  * Tell a story about what we're trying to show with this repo
  * Give instructions for reproducability
  * Give attribution/references, use authoritative sources
  * Keep it concise; assume a sophisticed audience

* ### Clean up Repo - Philip
  * Update Makefile too?


## Enhancements
* Regression Line on scatterplot
* Informative legend on scatterplot
* Optional arguments for column names in vaccines.py and deaths.py
* Using color as additional dimension in scatterplot

