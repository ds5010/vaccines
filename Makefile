
single_plot:
	python -B src/plotter.py

time_plot:
	python -B src/time_plotter.py
	
# Download and compress the CDC data
cdc:
	mkdir -p data
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv
