import pandas as pd


def file_to_df(filename,col,desired_date=None):

    orig_df = pd.read_csv(filename, compression="gzip")
    
    #this does not work, gets an error. Trying to make it so it does not import FIPS as an "object" type so we can use FIPS as a key to combine
    #orig_df['FIPS'].astype(float)
    #print(orig_df.dtypes)

    #filters the CDC data set by date
    if desired_date != None:
        new_df = orig_df[orig_df['Date']==desired_date][['FIPS', col]].copy()
    else:
        new_df = orig_df[['FIPS', col]].copy()

    #attempting to clean the data by removing N/A values
    new_df_clean1 = new_df[new_df['FIPS'].notna()]

    new_df_clean2 = new_df_clean1[new_df_clean1[col].notna()]

    return new_df_clean2

