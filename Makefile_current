# Download and compress the CDC data
#cdc:
#	mkdir -p data
#	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
#	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv

# Create CSV with sampled CDC data
vaccines:
	python -B src/vaccines_current.py

# Create CSV with JHU data
deaths:
	python -B src/deaths_current.py

merged:
	python -B src/combinedata_current.py
