import pandas as pd
import gzip
# df = pd.read_csv('/data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz',
#                  index_col='Date')
# print(df)
# print(type(df.index_col))
# print(df.to_datetime)

zip_data = gzip.open(
    'COVID-19_Vaccinations_in_the_United_States_County.csv.gz', 'rt')
