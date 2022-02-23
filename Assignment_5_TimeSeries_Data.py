#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 12:24:44 2022

@author: matthewray
"""
#[MR] Imports Johns Hopikins Combined raw data file from May - Nov 2021. 
import pandas as pd
jhu_df = pd.read_csv ('/Users/matthewray/Desktop/JSHU_CovidData_Clean.csv')
list_columns = jhu_df.columns.values.tolist()
print(list_columns)

#[MR] Drops unused columns in JH dataset.
drop_columns = ['Admin2', 'Province_State', 'Country_Region', 'Lat', 'Long_', 'Confirmed', 'Recovered', 'Active', 'Combined_Key', 'Incident_Rate', 'Case_Fatality_Ratio']
jhu_df.drop(columns=drop_columns, inplace=True)
print(jhu_df.columns)   
print(jhu_df)

#[MR] Removes row with no FIPS code (non-US data).
jhu_df_cl = jhu_df[jhu_df['FIPS'].notna()]
print(jhu_df_cl)

#[MR] Removes decimal from FIPS code to match CDC Dataset.
jhu_df_cl['FIPS'] = jhu_df_cl['FIPS'].astype(str).replace('\.0', '', regex=True)
print(jhu_df_cl)

#[MR] Removes time-stamp from last updated data-time column in JH dataset.
jhu_df_cl['Last_Update'] = jhu_df_cl['Last_Update'].str.split().str[0]
print(jhu_df_cl)

#[MR] Creates a unique ide using Date and FIPS code to combine data with CDC. 
jhu_df_cl['Unique_id'] = jhu_df_cl.Last_Update.astype(str) + '_' + jhu_df_cl.FIPS.astype(str)
print(jhu_df_cl)

#[MR] Removes Last_Update column now that unique ID is created. 
drop_columns = ['Last_Update']
jhu_df_cl.drop(columns=drop_columns, inplace=True)
print(jhu_df_cl.columns)   
print(jhu_df_cl)

#[MR] Imports CDC data file with Covid vaccination and and census data.
cdc_df = pd.read_csv ('/Users/matthewray/Desktop/Northeastern/PythonProjects/DS5010/Assignment3/COVID-19_Vaccinations_in_the_United_States_County.csv')
cdc_list_columns = cdc_df.columns.values.tolist()
print(cdc_list_columns)

#[MR] Drops unused CDC data. 
drop_columns = ['MMWR_week', 'Completeness_pct', 'Administered_Dose1_Recip', 'Administered_Dose1_Pop_Pct', 'Administered_Dose1_Recip_5Plus', 'Administered_Dose1_Recip_5PlusPop_Pct', 'Administered_Dose1_Recip_12Plus', 'Administered_Dose1_Recip_12PlusPop_Pct', 'Administered_Dose1_Recip_18Plus', 'Administered_Dose1_Recip_18PlusPop_Pct', 'Administered_Dose1_Recip_65Plus', 'Administered_Dose1_Recip_65PlusPop_Pct', 'Series_Complete_Yes', 'Series_Complete_Pop_Pct', 'Series_Complete_5Plus', 'Series_Complete_5PlusPop_Pct', 'Series_Complete_12Plus', 'Series_Complete_12PlusPop_Pct', 'Series_Complete_65Plus', 'Series_Complete_65PlusPop_Pct', 'Booster_Doses', 'Booster_Doses_Vax_Pct', 'Booster_Doses_18Plus', 'Booster_Doses_18Plus_Vax_Pct', 'Booster_Doses_50Plus', 'Booster_Doses_50Plus_Vax_Pct', 'Booster_Doses_65Plus', 'Booster_Doses_65Plus_Vax_Pct', 'SVI_CTGY', 'Series_Complete_Pop_Pct_SVI', 'Series_Complete_5PlusPop_Pct_SVI', 'Series_Complete_12PlusPop_Pct_SVI', 'Series_Complete_18PlusPop_Pct_SVI', 'Series_Complete_65PlusPop_Pct_SVI', 'Metro_status', 'Series_Complete_Pop_Pct_UR_Equity', 'Series_Complete_5PlusPop_Pct_UR_Equity', 'Series_Complete_12PlusPop_Pct_UR_Equity', 'Series_Complete_18PlusPop_Pct_UR_Equity', 'Series_Complete_65PlusPop_Pct_UR_Equity', 'Census2019', 'Census2019_5PlusPop', 'Census2019_12PlusPop', 'Census2019_65PlusPop']
cdc_df.drop(columns=drop_columns, inplace=True)
print(cdc_df.columns)   
print(cdc_df)

#[MR] Removes row with no FIPS code (non-US data).
cdc_df_cl = cdc_df[cdc_df['FIPS'].notna()]
print(cdc_df_cl)

#[MR] Converts Date into standard datetime format to match JH dataset.
cdc_df_cl['Date']=pd.to_datetime(cdc_df_cl.Date,errors='coerce')

#[MR] Creates a unique ide using Date and FIPS code to combine data with JH data.
cdc_df_cl['Unique_id'] = cdc_df_cl.Date.astype(str) + '_' + cdc_df_cl.FIPS.astype(str)
print(cdc_df_cl)

#[MR] Combines two datasets based on Unique_ID (Date_FIPS).
combined_data = pd.merge(cdc_df_cl, jhu_df_cl)
list_columns = combined_data.columns.values.tolist()
print(list_columns)
print(combined_data)

#[MR] Saves combined data frame as a CSV to desktop repo.
combined_data.to_csv('/Users/matthewray/Desktop/5010_Data/Combined_CovidData_Clean.csv', index=False)
