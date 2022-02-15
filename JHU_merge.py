#Bridget Mohler
#15 February 2022
#Acknowledgements to Prof. Bogden, stackoverflow, the pandas documentation, and the Python documentation, all of which were referenced over the course of the creation of this code.
#This program merges the daily JHU files into one CSV and adds a Date column with the corresponding datum. 

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
            if url<"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-16-2021.csv":
                for i in range(4006):
                    dates.append(date)
            if "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/09-15-2021.csv"<url<"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/10-06-2021":
                for i in range(4007):
                    dates.append(date)
            if url>"https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/10-05-2021.csv":
                for i in range(4008):
                    dates.append(date)
            urls.append(url)

file=pd.concat(map(pd.read_csv, urls))
file["Date"]=dates
file.to_csv("JHU_masterfile_with)dates.csv")
