# This tells the makefile that there might be a file
# or folder named "data" later on, and to ignore it
# so that "make data" runs the code below
.PHONY: data

cdcdata:
	mkdir -p data
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv

jhudata:
# TODO: Add code to download and compress JHU data

data:
	make cdcdata
	make jhudata

clean:
	rm -r data/