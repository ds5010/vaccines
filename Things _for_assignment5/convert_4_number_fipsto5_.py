# data_US.FIPS.dtype
# data_US.to_csv('final_data.csv',index=False)
# Why I use this method ,https://www.youtube.com/watch?v=W3SMXmxBpwo
# I tried iterarrow, my mac can cook steak ,if I use that method on my 597753 rows data. but in 👇🏻 this way, 10 seconds.
death = pd.read_csv('final_data.csv', converters={'FIPS': str})
death
dict_copy = death.to_dict('records') # Turn the death dataframe into a dictionary
for r in dict_copy:
    if len(r['FIPS']) == 4:
        r['FIPS'] = '0'+r['FIPS']
death2 = pd.DataFrame.from_dict(dict_copy)
death2.to_csv('final_data.csv', converters={'FIPS': str})
