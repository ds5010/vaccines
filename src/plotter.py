import pandas as pd
import matplotlib.pyplot as plt

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
    
def main():
    sctplt('11-30-2021')

if __name__ == '__main__':
    main()