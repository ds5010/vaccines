#Bridget Mohler
#This program reads in the JHU files from their various URLs, concatenates those files, and then outputs a single file containing all the data. 
#Acknowledgements to Prof. Bogden, stackexchange, the pandas documentation, and the Python documentation, all of which were referenced over the course of the creation of this code. 
#Since the dates are included in the urls but not the csv files, I need to go through and add a Date column with the corresponding dates for the datum, but I'm pretty sure I have a sense of how to do that once I'm not so tired. 
import pandas as pd

months=["05", "06", "07", "08", "09", "10", "11"]
days=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
urls=[]
dates=[]
not_valid=["06-31-2021", "09-31-2021", "11-31-2021" ]

for month in months:
    for day in days:
        url="https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/" + str(month) + "-" + str(day) + "-" + "2021.csv"
        date=str(month) + "-" + str(day) + "-" + "2021"
        if date in not_valid:
            print("Not valid")
            continue
        else:
            dates.append(date)
            urls.append(url)

pd.concat(map(pd.read_csv, urls)).to_csv("JHU_masterfile.csv")
