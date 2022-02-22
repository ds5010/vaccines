import pandas as pd

df = pd.read_csv("vaccinations-cleaned.csv")

df.loc[df['Date'].str[:2] == '05', 'Month'] = 'May'  
df.loc[df['Date'].str[:2] == '06', 'Month'] = 'June'  
df.loc[df['Date'].str[:2] == '07', 'Month'] = 'July'
df.loc[df['Date'].str[:2] == '08', 'Month'] = 'August'    
df.loc[df['Date'].str[:2] == '09', 'Month'] = 'September'  
df.loc[df['Date'].str[:2] == '10', 'Month'] = 'October'  
df.loc[df['Date'].str[:2] == '11', 'Month'] = 'November' 

df.loc[df['Date'].str[:2] == '01', 'Month'] = 'NA'
df.loc[df['Date'].str[:2] == '02', 'Month'] = 'NA'
df.loc[df['Date'].str[:2] == '03', 'Month'] = 'NA'
df.loc[df['Date'].str[:2] == '04', 'Month'] = 'NA'
df.loc[df['Date'].str[:2] == '12', 'Month'] = 'NA'

df = df[df['Month'] != 'NA']

df.to_csv('vaccinations-cleaned-with-months.csv', index=False)
