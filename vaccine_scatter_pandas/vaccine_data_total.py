#Sophia Cofone
#15 February 2022
#Acknowledgements: pandas, Python, and matplotlib documentation, stackoverflow 
#this file has 3 parts. file_to_df creates a dataframe from a csv file.
# clean_data cleans the data by removing NA values.
# merge_data brings together 2 df by using a common key
# and scatter creates a scatterplot

import pandas as pd
import matplotlib.pyplot as plt

def file_to_df(filename,col,desired_date=None):

    orig_df = pd.read_csv(filename, compression="gzip")

    #filters the CDC data sets by date
    if desired_date != None:
        df_date = orig_df[orig_df['Date']==desired_date][['FIPS', col]].copy()
    else:
        df_date = orig_df[['FIPS', col]].copy()
    
    #removes unknown values
    df_no_unk = df_date[df_date['FIPS'] != 'UNK']  
            
    #makes FIPS to float
    df_float = df_no_unk.astype(float)

    return df_float

def clean_data(df,col):
    #removing N/A values
    df_clean1 = df[df['FIPS'].notna()]

    df_clean2 = df_clean1[df_clean1[col].notna()]
    
    return df_clean2

def merged_data(df1,df2,key):

    df_merge = pd.merge(df1,df2,on = key)

    return df_merge

def scatter(df,x,y):
    xp = df[x]
    yp = df[y]
    plt.scatter(xp, yp)
    plt.show()

#FOR MAY 1st 2021
#calling the first function to create the DF from CDC
cdc = file_to_df('COVID-19_Vaccinations_in_the_United_States_County.csv.gz','Series_Complete_18Plus','05/01/2021')
#cleaning the CDC data 
cdc_clean = clean_data(cdc,'Series_Complete_18Plus')
#same thing for JHU
jhu = file_to_df('JHU_masterfile_with_dates.csv.gz','Deaths','05-01-2021')
#cleaning the JHU data
jhu_clean = clean_data(jhu,'Deaths')
#merging the two DFs using FIPS as the common key
merged_df = merged_data(cdc_clean,jhu_clean,'FIPS')
#generating a scatterplot
scatter(merged_df,'Deaths','Series_Complete_18Plus')

#FOR AUG 1st 2021
cdc = file_to_df('COVID-19_Vaccinations_in_the_United_States_County.csv.gz','Series_Complete_18Plus','08/01/2021')
cdc_clean = clean_data(cdc,'Series_Complete_18Plus')
jhu = file_to_df('JHU_masterfile_with_dates.csv.gz','Deaths','08-01-2021')
jhu_clean = clean_data(jhu,'Deaths')
merged_df = merged_data(cdc_clean,jhu_clean,'FIPS')
scatter(merged_df,'Deaths','Series_Complete_18Plus')

#FOR NOV 30th 2021
cdc = file_to_df('COVID-19_Vaccinations_in_the_United_States_County.csv.gz','Series_Complete_18Plus','11/30/2021')
cdc_clean = clean_data(cdc,'Series_Complete_18Plus')
jhu = file_to_df('JHU_masterfile_with_dates.csv.gz','Deaths','11-30-2021')
jhu_clean = clean_data(jhu,'Deaths')
merged_df = merged_data(cdc_clean,jhu_clean,'FIPS')
scatter(merged_df,'Deaths','Series_Complete_18Plus')