import pandas as pd

"""
This function return a dataframe that contains merge data. It use dataframes merge option that Prof. Bogden mentioned
scatterplot team can use it to get the dataframe they want
But please make sure that the csv to merge are already in in the ..data/JHU and ..data/CDC
parameter: 
date : The last date of each month.  form date = "11-30-2021"
"""


def merge_v2(date):
    base_CDC = "data/CDC/"
    base_JHU = "data/JHU/"
    df = pd.read_csv(base_CDC + "vaccinations-" + date + ".csv",
                     converters={'FIPS': str})
    deaths = pd.read_csv(
        base_JHU + "deaths-05-01-2021-to-"+date+".csv", converters={'FIPS': str})

    # Add the deaths data to the dataframe
    return df.merge(deaths, on='FIPS')

# test case 1
# date = "11-30-2021"
# df = merge(date)
# print(df)


"""This function write a csv to directory data/Merge. 
parameter: 
date : The last date of each month.  form date = "11-30-2021"
"""


def write_merge_data_to_csv(date):
    base_Merge = "data/Merge/"
    df = merge_v2(date)
    # print(df)
    df.to_csv(base_Merge+"vaccinations-and-deaths-"+date+'.csv', index=False)


# test case 2
# date = "05-31-2021"
# write_merge_data_to_csv(date)
"""This function write 7 csvs to directory data/Merge. 
Please make sure that the csv to merge are already in in the ..data/JHU and ..data/CDC

"""


def create_merge_data():
    write_merge_data_to_csv("05-31-2021")
    write_merge_data_to_csv("06-30-2021")
    write_merge_data_to_csv("07-31-2021")
    write_merge_data_to_csv("08-31-2021")
    write_merge_data_to_csv("09-30-2021")
    write_merge_data_to_csv("10-31-2021")
    write_merge_data_to_csv("11-30-2021")


create_merge_data()
