import pandas as pd
import matplotlib.pyplot as plt

import vaccines
import deaths
import combinedata

def sctplt(end_date):
    df = pd.read_csv('data/vaccinations-and-deaths-'+end_date+'.csv', converters={'FIPS' : str})
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df[xlabel]
    y = df[ylabel]
    area = df['Census2019_18PlusPop'] / 1e4

    plt.scatter(x,y,area, c='darkmagenta', alpha = .3)
    title_date = end_date.replace('-', '/')
    plt.title('Vaccination Rate vs Deaths by County\n'+ title_date)
    plt.xlabel('County Vaccination rate')
    plt.ylabel('County Covid Deaths per 10k')
    plt.xlim(0,100)
    plt.ylim(0,400)
    plt.savefig('img/'+ end_date + '.jpg')

def time_loop():
    for i in range(5,12):
        end_date = f'{i:02d}' + '-30-2021'
        vaccines.time_sample(end_date)
        deaths.time_sample(end_date)
        combinedata.merge_by_FIPS('data/vaccinations-' + end_date + '.csv',\
            'data/deaths-05-01-2021-to-' + end_date + '.csv',\
            outfile='data/vaccinations-and-deaths-' + end_date + '.csv')
        sctplt(end_date)

     
def main():
    time_loop()

if __name__ == '__main__':
    main()