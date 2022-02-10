# Compute a column sum from the sampled data

# Source data
input_filename = "vaccinations-02-01-2022.csv"
input_directory = "./data/"

key = "Series_Complete_5Plus"

# Subsample the dataset
sum = 0
with open(input_directory + input_filename) as file:
  header = file.readline().rstrip().split(",")
  for line in file:
    values = line.rstrip().split(",")

    if key in header:
      index = header.index(key)
      sum += int(values[index])

print("{} total: {:,d}".format(key, sum))
