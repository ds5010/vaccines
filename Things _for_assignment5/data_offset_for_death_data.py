import pandas as pd
import gzip
from pandas.tseries.offsets import DateOffset

death = pd.read_csv('final_data.csv', converters={'FIPS': str})
death_columns = ["FIPS", "Last_Update", "Admin2", "Province_State",
                 "Confirmed", "Deaths", "Incident_Rate", "Case_Fatality_Ratio"]
death = death[death_columns]
death.Last_Update = pd.to_datetime(death.Last_Update)
death['normalised_date'] = death['Last_Update'].dt.normalize() - \
    DateOffset(days=1)
# 可以把这个数据重新存储到一个csv death.to_csv('US_data.csv',index=False)
death.to_csv('US_data.csv', index=False)
