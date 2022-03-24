import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def comparison():
    months = ['May', 'June', 'July', 'August', 'September', 'October', 'November']
    csv_dates = ['05-31-2021', '06-30-2021', '07-31-2021', '08-31-2021', '09-30-2021', '10-31-2021', '11-30-2021']
    index = -1
    file_list = []
    for month in months:
        index+=1
        df = pd.read_csv('data/Merge/vaccinations-and-deaths-' + csv_dates[index] +'.csv', converters={'FIPS' : str})
        df['Deaths_Per_1e5'] = df['Deaths'] / df['Census2019_18PlusPop'] * 1e5
        df['Month'] = month
        file_list.append(df)
    merged_df = pd.concat(file_list)
    cleaned_df = merged_df[merged_df['FIPS'].str.contains('44003|01125')]

    Kent_vax = cleaned_df.loc[cleaned_df['FIPS']=='44003']
    Kent_vax = Kent_vax["Series_Complete_18PlusPop_Pct"]
    Tuscaloosa_vax = cleaned_df.loc[cleaned_df['FIPS']=='01125']
    Tuscaloosa_vax = Tuscaloosa_vax["Series_Complete_18PlusPop_Pct"]
    Kent_death = cleaned_df.loc[cleaned_df['FIPS']=='44003']
    Kent_death = Kent_death['Deaths_Per_1e5']
    Tuscaloosa_death = cleaned_df.loc[cleaned_df['FIPS']=='01125']
    Tuscaloosa_death = Tuscaloosa_death['Deaths_Per_1e5']

    fig,ax1 = plt.subplots() 
    x = [0, 1, 2, 3, 4, 5, 6]
    labels = ['May', 'June', 'July', 'August', 'September', 'October', 'November']
    x = np.arange(len(labels))
    width = 0.35 
    plt.xticks(x, labels)
    ax1.set_title('18+ Vaccination Rates and Deaths in Kent County, RI and Tuscaloosa County, AL')
    ax1.set_xlabel('Month 2021')
    ax1.set_ylabel('Percent Vaccinated') 
    ax1.bar(x - width/2, Kent_vax, width, color='darkcyan', label = '% Vaxxed Kent')
    ax1.bar(x + width/2, Tuscaloosa_vax, width, color='darkslategray', label = '% Vaxxed Tuscaloosa')
    ax1.legend(loc='upper left')
    ax2 = ax1.twinx()
    ax2.plot(x, Kent_death, color='indianred', label = '# of Deaths Kent')
    ax2.plot(x, Tuscaloosa_death, color='firebrick', label = '# of Deaths Tuscaloosa')
    ax2.set_ylabel('Deaths per 1e5 of Pop.')
    ax2.legend(loc='upper right')
    plt.show()
comparison()