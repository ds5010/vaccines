# Plot the merged data
plot:
	python -B app.py

# Create a CSV from merged vaccines and deaths CSVs
merge:
	python -B src/merge.py

# Create CSV with sampled CDC data
vaccines:
	python -B src/vaccines.py

# Create CSV with JHU data
deaths:
	python -B src/deaths.py

# Download and compress the CDC data
cdc:
	mkdir -p data
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv
