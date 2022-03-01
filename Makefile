
single_plot:
	python -B src/plotter.py

time_plot:
	python -B src/time_plotter.py

datadir:
	mkdir -p data
# Download and compress the CDC data
cdc: datadir
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv
# Create a CSV from merged vaccines and deaths CSVs
merge:
	python -B src/merge.py

# Create CSV with sampled CDC data
vaccines:
	python -B src/vaccines.py

# Create CSV with JHU data
deaths: datadir
	mkdir -p data/JHU
	python -B src/JHU_data.py
