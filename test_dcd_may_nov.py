import gzip
import pandas as pd 

df = pd.read_csv('May_1st_to_November_30th.csv.gz',compression='gzip')
print(df)
