# Create CSV with sampled CDC data
vaccines:
	python -B src/vaccines.py

# Create CSVs with JHU data
deaths:
	python -B src/deaths.py	
#python3 -B src/deaths.py jun
#python3 -B src/deaths.py jul
#python3 -B src/deaths.py aug
#python3 -B src/deaths.py sep
#python3 -B src/deaths.py oct
#python3 -B src/deaths.py nov
#python3 -B src/deaths.py nov30

merged:
	python -B src/combinedata.py

# Download and compress the CDC data
cdc:
	mkdir -p data
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv
