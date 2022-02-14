# Download and compress the CDC data
# Data downloaded 14 Feb is ~250M before compression, and almost 100M after gzip
cdcdata:
	mkdir -p data
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv

# This is a placeholder for JHU data download
jhudata:
# TODO: Add code to download and compress JHU data

clean:
	rm -r data/
