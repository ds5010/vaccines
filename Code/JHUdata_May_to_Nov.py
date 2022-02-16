import gzip
import csv
from statistics import mode
import pandas as pd

def readit(filename, xlabel, ylabel, zlabel):
    with gzip.open(filename, 'rt') as file:
        data = file.read().rstrip().split("\n")[1:]

    keys = [xlabel, zlabel, ylabel]
    list = []
    newlist = []

    for line in data:
      datum = line.split(",")
      list.append(datum)

    for line in list: 
      newlist.append([line[4], line[0], line[8]])

    print(newlist)
    

    newfile = "JHUdata_May_to_Nov.csv"
    with open(newfile, "w") as csvfile:
      writter = csv.writer(csvfile)
      writter.writerow(keys)
      writter.writerows(newlist)

    x = []
    y = []
    z = []

    for item in newlist:
      z.append(item[1])
      x.append(item[0])
      y.append(item[2])

    return x, y, z

filename = "/Users/qiweihu/Desktop/NEU/DS5010/Github/vaccines/Data/JHUdata.csv.gz"
xlabel = "Date"
ylabel = "Deaths"
zlabel = "FIPS"
x, y, z = readit(filename, xlabel, ylabel, zlabel)
