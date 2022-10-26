import pandas as pd

def merge(date):
    """
    This function return a dataframe that contains merge data. It use dataframes merge option that Prof. Bogden mentioned
    scatterplot team can use it to get the dataframe they want
    But please make sure that the csv to merge are already in in the ..data/JHU and ..data/CDC
    Parameters: 
        date : str, The last date of each month.  form date = "11-30-2021"
    """
    base_CDC = "data/CDC/"
    base_JHU = "data/JHU/"
    df = pd.read_csv(base_CDC + "vaccinations-" + date + ".csv",
                     converters={'FIPS': str})
    deaths = pd.read_csv(
        base_JHU + "deaths-05-01-2021-to-"+date+".csv", converters={'FIPS': str})

    # Add the deaths data to the dataframe
    return df.merge(deaths, on='FIPS')

def write_merge_data_to_csv(date):
    """This function write a csv to directory data/Merge. 
    Parameters: 
        date: str, The last date of each month.  form date = "11-30-2021"
    """
    base_Merge = "data/Merge/"
    df = merge(date)
    # print(df)
    df.to_csv(base_Merge+"vaccinations-and-deaths-"+date+'.csv', index=False)

def create_merge_data():
    """This function write 7 csvs to directory data/Merge. 
    Please make sure that the csv to merge are already in in the ..data/JHU and ..data/CDC
    """
    months=pd.read_csv("months.csv")
    dates=months.date.to_list()

    for date in dates:
        write_merge_data_to_csv(date)

if __name__ == "__main__":
    create_merge_data()
