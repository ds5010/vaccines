
# Roadmap
*Updated 2/24 for completion by 2/29*  
[Link to in-class Google doc](https://docs.google.com/document/d/1p1ru7QAT71t3leCCaC_e88HN7AwzkLz-vohalUIci04/edit)
## Core Tasks
We want to focus on creating a finished product first, which has been discussed and decided as a series of scatterplots combined into an animation. Once core task are accomplished, we can jump into the list of possible enhancements at the end. But it doesn't hurt to keep those enhancements in mind while implementing the core tasks.

### Possible Roadmap, working back from the desired result:
1. Animation function reads images in a folder and creates animation
2. Scatterplot function loops through dates and calls merge function to plot combined data and save to img folder
3. Merge Function calls CDC and JHU functions then combines their dataframes by FIPS
4. CDC and JHU functions handle downloading and trimming the data so they're ready to merge 

* #### CDC Data - Connor & Jerry  
  * Takes **desired date** arguments
  * Work to remove all hardcoded dates and links
  * returns a dataframe for merge function  

* #### JHU Data - Yune & Jerry
  * Takes **end date** and **start date** arguments
  * Work to remove all hardcoded dates and links
  * returns a dataframe for merge function

* #### Merge - Tim & Yune
  * Takes **end date** and **start date** arguments
  * Remove hard coded dates as much as possible
  * Communicate with the CDC and JHU folks to call their functions within merge
  * Try the dataframes merge option that Prof. Bogden mentioned
  * If the dataframes merge doesn't happen, we can revert back to writing intermediate vaccine-only & deaths-only csv files to the data folder and using the existing merge code
  * returns dataframe for scatterplot function

* #### Scatterplot - Matt & Kayne
  * Create a scatterplot with the dataframe from Merge
  * Plot Vaccination rate on x-axis, Deaths per 10k on y-axis, population of county as dot size
  * Create img folder
  * Create multiple plots over time and save to img folder

* #### Time Sequence + Animation - Sophia & Bridget
  * Create gif/video using contents of img folder
  * Use [imagio](https://github.com/imageio/imageio) -- github
  * Save or play the animation? 

* #### README - Matt & Kayne
  * Tell a story about what we're trying to show with this repo
  * Give instructions for reproducability
  * Give attribution/references, use authoritative sources
  * Keep it concise; assume a sophisticed audience

* #### Clean up Repo - Philip
  * Update Makefile too?


## Enhancements
* Regression Line on scatterplot
* Informative legend on scatterplot
* Optional arguments for column names in vaccines.py and deaths.py
* Using color as additional dimension in scatterplot

