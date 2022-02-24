#Sophia Cofone
#22 February 2022
#Acknowledgements: pandas, Python, and matplotlib documentation, stackoverflow 
#this file has 3 parts. file_to_df creates a dataframe from a csv file. Note that the JHU version also sums the deaths column over a period of time. Function also cleans the data.
# merge_data brings together 2 df by using a common key (FIPS)
# and my_scatter creates a scatterplot

import pandas as pd
import matplotlib.pyplot as plt

def file_to_df_cdc(filename,col,desired_date,pop):

    orig_df = pd.read_csv(filename, compression="gzip")
    
    #filters the data sets by date and adds optional column 
    new_df = orig_df[orig_df['Date']==desired_date][['FIPS', col, pop]].copy()
    
    #print("Before removing unknowns:")
    #print(new_df.shape)
    df_no_unk = new_df[new_df['FIPS'] != 'UNK']  
    #print("After removing unknowns:")
    #print(df_no_unk.shape)

    #makes FIPS to float
    df_float = df_no_unk.astype(float)
    
    #removing N/A values
    #print("Before removing unknowns:")
    #print(df_float.shape)
    df_clean = df_float.dropna()
    #print("After removing unknowns:")
    #print(df_clean.shape)

    return df_float

def file_to_df_jhu(filename,col,desired_date,enddate):
    
    orig_df = pd.read_csv(filename, compression="gzip")
        
    #date_list = pd.date_range(start ='05-01-2021', end ='06-01-2021').strftime('%m-%d-%Y').tolist()  
    date_list = [desired_date,enddate]      
    #filters the data sets by date and adds column 
    new_df = orig_df[orig_df['Date'].isin(date_list)][['FIPS','Date',col]].copy()
    
    #print("Before removing unknowns:")
    #print(new_df.shape)
    df_no_unk = new_df[new_df['FIPS'] != 'UNK']  
    #print("After removing unknowns:")
    #print(df_no_unk.shape)
    
    #removing N/A values
    #print("Before removing unknowns:")
    #print(df_float.shape)
    df_clean = df_no_unk.dropna()
    #print("After removing unknowns:")
    #print(df_clean.shape)
    
    #making one day negative, this is giving error not sure why, other option here also doesn't work
    #df_clean = df_clean['Date'].where(df_clean['Date']==desired_date, -df_clean[col])
    
    df_clean.loc[df_clean['Date']==desired_date, col] *= -1

    df_clean = df_clean.groupby('FIPS')[col].sum().reset_index()
    
    return df_clean

def merged_data(df1,df2,key):

    df_merge = pd.merge(df1,df2,on = key)

    return df_merge

def my_scatter(df,x,y,pop):
    xlabel = x
    ylabel = y

    x = df[x]
    y = df[y]/df[pop]

    fig, ax = plt.subplots()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.scatter(x, y)
    plt.show()

    
#creating the data frames from the raw data files, cleaning the data
cdc = file_to_df_cdc('COVID-19_Vaccinations_in_the_United_States_County.csv.gz','Series_Complete_18PlusPop_Pct','08/01/2021','Census2019_18PlusPop')
jhu = file_to_df_jhu('JHU_masterfile_with_dates.csv.gz','Deaths','05-01-2021','08-01-2021')
#merging the two DFs using FIPS as the common key
merged_df = merged_data(cdc,jhu,'FIPS')
#generating a scatterplot
my_scatter(merged_df,'Series_Complete_18PlusPop_Pct','Deaths','Census2019_18PlusPop')

#creating the data frames from the raw data files, cleaning the data
cdc = file_to_df_cdc('COVID-19_Vaccinations_in_the_United_States_County.csv.gz','Series_Complete_18PlusPop_Pct','11/30/2021','Census2019_18PlusPop')
jhu = file_to_df_jhu('JHU_masterfile_with_dates.csv.gz','Deaths','05-01-2021','11-30-2021')
#merging the two DFs using FIPS as the common key
merged_df = merged_data(cdc,jhu,'FIPS')
#generating a scatterplot
my_scatter(merged_df,'Series_Complete_18PlusPop_Pct','Deaths','Census2019_18PlusPop')