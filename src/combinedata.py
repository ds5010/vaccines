import pandas as pd

counties = pd.read_csv('JHU_05-01-2021.csv')
may = pd.read_csv(data/'JHU_05-01-2021.csv')
jun = pd.read_csv(data/'JHU_06-01-2021.csv')
jul = pd.read_csv(data/'JHU_07-01-2021.csv')
aug = pd.read_csv(data/'JHU_08-01-2021.csv')
sep = pd.read_csv(data/'JHU_09-01-2021.csv')
oct = pd.read_csv(data/'JHU_10-01-2021.csv')
nov = pd.read_csv(data/'JHU_11-01-2021.csv')
dec = pd.read_csv(data/'JHU_12-01-2021.csv')

countylist = []
countylist.append(counties.pop('FIPS'))

# unsuccessful attempts to remove blanks and just leave rows with FIPS code
# for i in range (len(countylist)):    
#   try:
#     int(countylist[i])
#   except:
#     countylist.pop[i]
####
# for i in range (len(countylist)):
#  a = countylist[i]
#  if a > 0:
#    continue
#  else:
#    countylist.pop[i]
#
#



fips = {'FIPS': countylist}


print(may)
