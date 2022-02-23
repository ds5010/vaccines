# Assignment 05

To analyze the effectiveness of the COVID-19 vaccines over time, I decided to 
create a GIF that showed how the scatterplot we developed in class changed 
between June 01, 2021 and November 30, 2021. 

I adapted the vaccines.py, deaths.py and combinedata.py files so that 
they could create multiple datasets. The user only needs to follow the 'make deaths', 
'make vaccines' and 'make merged' commands to create individual data files for the 
following time periods:

* May 01 - June 01, 2021
* May 01 - July 01, 2021
* May 01 - August 01, 2021
* May 01 - September 01, 2021
* May 01 - October 01, 2021
* May 01 - November 01, 2021
* May 01 - November 30, 2021

Using the combined datasets, I created dataframes for each timeframe using files 
in the src/months folder. The user only needs to call scatters.py from the src directory
to create a set of image files. 

We need to create .ppm image files, and cannot export the scatterplot in that file format. 
So we need to use an external file conversion service, like [Convert.io](https://convertio.co/).

Now you can upload the .ppm files to the Images directory, and call vaxgif.py to play the GIF. 

Here it is, in action:
[Watch the vaccines work](https://drive.google.com/file/d/1WMtjV7JWnMQTIQmz9G2xw1lEBQKWRqbH/view?usp=sharing)

