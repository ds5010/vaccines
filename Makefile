
single_plot:
	python -B src/plotter.py

time_plot:
	python -B src/time_plotter.py

datadir:
	mkdir -p data

# Download and compress the CDC data
cdc: data/
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz

# Create CSV with sampled CDC data
vaccines: data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz
	mkdir -p data/CDC
	python -B src/vaccines.py

# Create CSV with JHU data
deaths: data/
	mkdir -p data/JHU
	python -B src/JHU_data.py

# Create a CSV from merged vaccines and deaths CSVs
merge_v1:
	python -B src/merge.py

merge_v2: data/JHU/ data/CDC/
	mkdir -p data/Merge
	python -B src/merge_v2.py

make clean:
	rm -r data

# Create series of scatter plots, save .png files to 'img' directory
scatters:
	python -B src/scatters.py

# Create single scatterplot and show in window
test:
	python -B src/test.py
