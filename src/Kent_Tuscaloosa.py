import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def comparison():
    months = {
        'May':'05-31-2021',
        'June':'06-30-2021',
        'July':'07-31-2021',
        'August':'08-31-2021',
        'September':'09-30-2021',
        'October':'10-31-2021',
        'November':'11-30-2021'
        }
    file_list = []
    for month, csv_date in months.items():
        df = pd.read_csv('data/Merge/vaccinations-and-deaths-' + csv_date +'.csv', converters={'FIPS' : str})
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
    ax1.set_title('18+ Vaccination Rates and Deaths in Kent County, RI and Tuscaloosa County, AL', wrap=True)
    ax1.set_xlabel('Month 2021')
    ax1.set_ylabel('Percent Vaccinated') 
    ax1.bar(x - width/2, Kent_vax, width, color='darkcyan', label = '% Vaxxed Kent')
    ax1.bar(x + width/2, Tuscaloosa_vax, width, color='darkslategray', label = '% Vaxxed Tuscaloosa')
    ax2 = ax1.twinx()
    ax2.plot(x, Kent_death, color='indianred', label = '# of Deaths Kent')
    ax2.plot(x, Tuscaloosa_death, color='firebrick', label = '# of Deaths Tuscaloosa')
    ax2.set_ylabel('Deaths per 1e5 of Pop.')
    handles_1, _ = ax1.get_legend_handles_labels()
    handles_2, _ = ax2.get_legend_handles_labels()
    handles_2.extend(handles_1) # adds the list items from handles_1 to handles_2
    ax2.legend(handles = handles_2, loc='upper right')
    plt.show()
comparison()