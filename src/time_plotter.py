import vaccines
import deaths
import combinedata
import plotter

def time_loop():
    for i in range(6,12):
        end_date = f'{i:02d}' + '-30-2021'
        vaccines.time_sample(end_date)
        deaths.time_sample(end_date)
        combinedata.merge_by_FIPS('data/vaccinations-' + end_date + '.csv',\
            'data/deaths-05-01-2021-to-' + end_date + '.csv',\
            outfile='data/vaccinations-and-deaths-' + end_date + '.csv')
        plotter.sctplt(end_date)

     
def main():
    time_loop()

if __name__ == '__main__':
    main()