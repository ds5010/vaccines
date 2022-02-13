import gzip
from tabulate import tabulate

def readit(filename='covidvaxbycounty20220203.csv.gz'):
    """
    Read and parse CSV -- read entire file all at once.
    """
    if filename.endswith('.gz'):
        with gzip.open(filename, 'rt') as f:
            list = f.read().rstrip().split("\n")
    else:
        with open(filename, 'rt') as file:
            list = file.read().rstrip().split("\n") 

    keys = list.pop(0).split(",")
    data = []
    for line in list:
        values = line.split(",")
        datum = {keys[i]: value for i, value in enumerate(values)}
        data.append(datum)
    print("it worked")
    return data
  
  def facts(listofdicts):
    """
    Read in a file name and report back # of columns, # of rows
    """
    factlist = []
    headers = list(listofdicts[0])
    factlist.append(len(headers)) # number of columns at index 0
    factlist.append(len(listofdicts)) # number of rows at index 1
    factlist.append(headers) # list of column names at index 2
    factlist.append(listofdicts[0]) # dictionary representing first row of data at index 3

    return factlist
  
  def print_table (filename):
    """
    takes in a file, reads and processes it (for data files that follow .csv format)
    reports information about number of columns and rows (for any data file per row 14)
    and reports vaccination status (specific to vax status data file)
    --> no default filename, meant to input data sample file created by sampler.py
    """
    listofdicts = readit(filename)                                               #changed from cr.readit
    list = facts(listofdicts)                                                     #changed from s.facts
    print("Your data has {0} columns and {1} rows.".format(list[0], list[1]))
    if list[0] < 100:
        print("\nAvailable fields:")
        table = []
        cols = 3
        i = 0
        while i <= len(list[2]):
            row = []
            for j in range (cols):
                if i+j <= len(list[2]):
                    try:
                      row.append(list[2][i+j])
                    except:
                      continue
                else:
                    break
            table.append(row)
            if i+cols < len(list[2]):
                i = i + cols
            else:
                break

        print(tabulate(table, tablefmt="plain"))

    else:
        print("Too many (> 100) fields available to print in table")
