#Bridget Mohler
#15 February 2022
#This program will combine the JHU and CDC data and remove excess columns (the excess rows are a work in progress on my local repo). 
import pandas as pd

keep = ["FIPS", "Date", "Series_Complete_Yes", "Deaths"]
drop_list = []
drop_date = []
merged_file = pd.concat(map(pd.read_csv, ["JHU_masterfile_with_dates.csv", "COVID-19_Vaccinations_in_the_United_States_County.csv"]))

#print(len(merged_file.columns))

for label in merged_file:
    if label not in keep:
        drop_list.append(label)

four_column_file = merged_file.drop(drop_list, axis=1)
#print(len(four_column_file.columns))
