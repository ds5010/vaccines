# Do everything (except test)
all: data cdc vaccines deaths merge scatters animation

# Make the data directory
.PHONY: data # lets us use "make data" even though data/ is also a directory
data:
	mkdir -p data

# Download and compress the CDC data
cdc: data/
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv

# Create CSV with sampled CDC data
vaccines: data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz
	mkdir -p data/CDC
	python -B src/vaccines.py

# Create CSV with JHU data
deaths: data/
	mkdir -p data/JHU
	python -B src/deaths.py

# Create the merged datasets
merge: data/JHU/ data/CDC/
	mkdir -p data/Merge
	python -B src/merge.py

# Create series of scatter plots, save .png files to 'img' directory
scatters:
	mkdir -p img
	python -B src/scatters.py

# Create single scatterplot and show in window
test:
	python -B src/test.py

# Combine generated png's to make an animation
animation: scatters img/*.png
	python -B src/animation.py

# Remove image and data directories
clean:
	rm -r data img
