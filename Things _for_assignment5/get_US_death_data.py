# This is how I got all the US death data from 05/01/2021-11/30/2021.
# I use some regular expression here,which is really powerful
import glob
import pandas as pd
a = glob.glob('../../dead_data/[0][5-9]*-*-2021.csv')
b = glob.glob('../../dead_data/[1][0-1]*-*-2021.csv')
may_to_novenmber = a+b
print(a+b)
may_to_novenmber = sorted(may_to_novenmber)
final_data = pd.concat(
    map(pd.read_csv, may_to_novenmber,), ignore_index=True)
# 删选掉FIPS ==nan的，这个时候 final_data.FIPS.dtype== float64
final_data = final_data[final_data['FIPS'].isna() == False]
final_data
final_data['FIPS'] = final_data['FIPS'].astype('int')
# final_data.FIPS.dtype
final_data.to_csv('final_data.csv', index=False)
