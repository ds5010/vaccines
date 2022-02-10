# Sample one date from the source dataset and write it to an intermediate file
import gzip

# Source data
input_filename = "COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
input_directory = "./data/"

# Date to extract from file
#desired_date = '11/30/2021'
desired_date = '02/01/2022'

# Output
output_directory = "./data/"
output_filename = "vaccinations-" + desired_date[:2] + "-" + \
    desired_date[3:5] + "-" + desired_date[6:10] + ".csv"

data = []
lines_read = 0
with gzip.open(input_directory + input_filename, mode="rt") as file:
  header = file.readline()
  for line in file:
    lines_read += 1
    if line[:10] == desired_date:
      data.append(line)

lines_written = 0
with open(output_directory + output_filename, 'w') as outfile:
  outfile.write(header)
  for line in data:
    lines_written += 1
    outfile.write(line)

print("Lines read:", lines_read)
print("Lines written:", lines_written)
