###### "Macro" Commands ######
# Make new plots (leaving data intact)
.PHONY: img
# The two variables below are passed to the comparison.py module.
# To change which counties are compared, add "fips_1=[number]" or
# "fips_2=[number]" as arguments to your "make img"
fips_1 = 44003
fips_2 = 01125
img: clean-img scatters comparison animation

# Make everything (including refreshing data)
all: clean data cdc vaccines deaths merge scatters animation comparison

###### Specific Commands ######
# Make the data directory
.PHONY: data # lets us use "make data" even though data/ is also a directory
data:
	mkdir -p data

# Download and compress the most recent CDC data
cdc: data/
	curl -o data/COVID-19_Vaccinations_in_the_United_States_County.csv https://data.cdc.gov/api/views/8xkx-amqh/rows.csv?accessType=DOWNLOAD
	gzip data/COVID-19_Vaccinations_in_the_United_States_County.csv

# Create (or refresh) CSV with sampled CDC data
vaccines: data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz
	mkdir -p data/CDC
	python -B src/vaccines.py

# Create (or refresh) CSV with JHU data
deaths: data/
	mkdir -p data/JHU
	python -B src/deaths.py

# Create the merged datasets
merge: data/JHU/ data/CDC/
	mkdir -p data/Merge
	python -B src/merge.py

# Create series of scatter plots, save .png files to 'img' directory
scatters: data/Merge/
	mkdir -p img
	python -B src/scatters.py

# Compare two counties based on FIPS
# The two variables below can be changed here or overridden by environment variables using make -e
comparison: data/Merge/
	python -B src/comparison.py $(fips_1) $(fips_2)

# Combine generated png's to make an animation
animation: scatters
	python -B src/animation.py

# Remove data and image directories
# This could be useful if you want to regenerate the merged dataset
# and images with more recent data.
clean:
	rm -rf data img

clean-img:
	rm -rf img

# Run unit tests on JHU and Merge data.
test_JHU: 
	python -B tests/test_JHU.py 
test_Merge:
	python -B tests/test_Merge.py

# run a python development server to work on the docs
serve:
	python -m http.server -d docs
