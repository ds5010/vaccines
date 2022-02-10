# Subsample (subset of columns and single date) the gzip'ed CDC vaccination data and write a csv
import gzip
import json

# Source data
input_filename = "vaccinations-02-01-2022.csv"
input_directory = "./data/"

# Fields to extract from the source data
#col = "Series_Complete_Pop_Pct"
#col = "Series_Complete_Yes"
col = "Series_Complete_5Plus"
fips = "FIPS"
county = "Recip_County"
state = "Recip_State"
keys = [fips, county, state, col]

# Output
output_directory = "./data/"
output_filename = "columns.csv"

# Subsample the dataset
data = []
with open(input_directory + input_filename) as file:
  header = file.readline().rstrip().split(",")
  for line in file:
    values = line.rstrip().split(",")

    d = {}
    for i, key in enumerate(header):
      if key in keys:
        d[key] = values[i]
    data.append(d)

# Write output to a JSON file
#with open('vaccines.json', 'w') as file:
#  json.dump(data, file)

# Write the output to a CSV
i = 0
with open(output_directory + output_filename, 'w') as file:
  file.write(",".join(keys) + "\n") # header
  for line in data:
    file.write(",".join([line[key] for key in keys]) + "\n")
