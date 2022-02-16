import gzip
import csv


def readit(filename, xlabel, ylabel, zlabel):
    with gzip.open(filename, 'rt') as file:
        data = file.read().rstrip().split("\n")[213396:915784]

    keys = [xlabel, zlabel, ylabel]
    list = []
    newlist = []

    for line in data:
      datum = line.split(",")
      list.append(datum)

    for line in list: 
      newlist.append([line[0], line[1], line[5]])

    print(newlist)
    

    newfile = "CDCdata_May_to_Nov.csv"
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

filename = "CDCdata.csv.gz"
xlabel = "Date"
ylabel = "Completeness_pct"
zlabel = "FIPS"
x, y, z = readit(filename, xlabel, ylabel, zlabel)
