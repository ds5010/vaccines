# This code is ugly, adn it uses some scratch method.
# Why I do this is because I failed to find a way to download
# a particular file in git repo
import requests
import re
from bs4 import BeautifulSoup
import wget

# URL on the Github where the csv files are stored
# change USERNAME, REPOSITORY and FOLDER with actual name
github_url = 'https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports'

result = requests.get(github_url)
with open('/Users/mac/csse_covid_19_daily_reports', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

csvfiles = soup.find_all(title=re.compile("\.*csv$"))
filename = []
for i in csvfiles:
    filename.append(i.extract().get_text())
# get a list like this ['01-01-2021.csv', '01-01-2022.csv', '01-02-2021.csv', '01-02-2022.csv', '01-03-2021.csv', '01-03-2022.csv', '01-04-2021.csv', '01-04-2022.csv', '01-05-2021.csv', '01-05-2022.csv', '01-06-2021.csv', '01-06-2022.csv', '01-07-2021.csv', '01-07-2022.csv', '01-08-2021.csv', '01-08-2022.csv', '01-09-2021.csv', '01-09-2022.csv', '01-10-2021.csv', '01-10-2022.csv', '01-11-2021.csv', '01-11-2022.csv', '01-12-2021.csv', '01-12-2022.csv', '01-13-2021.csv', '01-13-2022.csv', '01-14-2021.csv', '01-14-2022.csv', '01-15-2021.csv', '01-15-2022.csv', '01-16-2021.csv', '01-16-2022.csv', '01-17-2021.csv', '01-17-2022.csv', '01-18-2021.csv', '01-18-2022.csv', '01-19-2021.csv', '01-19-2022.csv', '01-20-2021.csv', '01-

base = "https://raw.githubusercontent.com/"
base += "CSSEGISandData/COVID-19/master/csse_covid_19_data/"
base += "csse_covid_19_daily_reports/"
download_list = []
for i in filename:
    download_list.append(base+i)
print(download_list[0])
# 👆🏻 get list like this ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2021.csv', 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/01-01-2022.csv',
for url in download_list:
    wget.download(url, '/Users/mac/dead_data')
# use wget to down load