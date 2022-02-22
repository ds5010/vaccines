import pandas as pd

deaths_may = pd.read_csv('deaths-05-01-2021-to-05-31-2021.csv')
deaths_may['Month'] = 'May'

deaths_june = pd.read_csv('deaths-06-01-2021-to-06-30-2021.csv')
deaths_june['Month'] = 'June'

deaths_july = pd.read_csv('deaths-07-01-2021-to-07-31-2021.csv')
deaths_july['Month'] = 'July'

deaths_august =  pd.read_csv('deaths-08-01-2021-to-08-31-2021.csv')
deaths_august['Month'] = 'August'

deaths_september  = pd.read_csv('deaths-09-01-2021-to-09-30-2021.csv')
deaths_september['Month'] = 'September'

deaths_october = pd.read_csv('deaths-10-01-2021-to-10-31-2021.csv')
deaths_october['Month'] = 'October'

deaths_november = pd.read_csv('deaths-11-01-2021-to-11-30-2021.csv')
deaths_november['Month'] = 'November'

#df = pd.concat(map(pd.read_csv, ['deaths-05-01-2021-to-05-31-2021.csv', 'deaths-06-01-2021-to-06-30-2021.csv', 'deaths-07-01-2021-to-07-31-2021.csv', 'deaths-08-01-2021-to-08-31-2021.csv', 'deaths-09-01-2021-to-09-30-2021.csv', 'deaths-10-01-2021-to-10-31-2021.csv', 'deaths-11-01-2021-to-11-30-2021.csv']), ignore_index = True)

deaths_data = [deaths_may, deaths_june, deaths_july, deaths_august, deaths_september, deaths_october, deaths_november]

df = pd.concat(deaths_data)
df.to_csv('merged_deaths.csv', index = False)
