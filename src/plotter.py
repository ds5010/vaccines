import pandas as pd
import matplotlib.pyplot as plt

def sctplt():
    df = pd.read_csv('data/vaccinations-and-deaths-11-30-2021', converters={'FIPS' : str})
    df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5

    xlabel = 'Series_Complete_18PlusPop_Pct'
    ylabel = 'Deaths_Per_1e5'

    x = df[xlabel]
    y = df[ylabel]
    area = df['Census2019_18PlusPop'] / 1e4

    plt.scatter(x,y,area, alpha = .3)
    plt.title('Vaccination Rate vs Deaths by County\ncirca 11/30/2021')
    plt.xlabel('County Vaccination rate')
    plt.ylabel('County Covid Deaths per 10k')
    plt.xlim(0,100)
    plt.ylim(0,400)
    plt.show()
    
def main():
    sctplt()

if __name__ == '__main__':
    main()