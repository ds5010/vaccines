'''
vaccine_sample reads the g-zipped cdc data
desired_date 'mm-dd-yyyy', only keep rows containing this date
cols an optional parameter list of names of columns we keep
'''
import pandas as pd

def vaccine_sample(desired_date, cols = ["Series_Complete_18PlusPop_Pct", "Census2019_18PlusPop"]):
    # Source data
    input_filename = "./data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
    df = pd.read_csv(input_filename, index_col='FIPS', compression='gzip')
    print("Total vaccine rows, cols:", df.shape)

    # Filter by date
    filter = desired_date.replace('-','/')
    df = df[df["Date"] == filter]

    # Extract columns of interest
    df = df[cols]

    # Clean the dataset
    print("Total " + filter + " rows, cols:", df.shape)
    df = df.dropna()
    print("Valid " + filter + " rows, cols:", df.shape)
    return df

# main function is for testing only 
def main():
    print(vaccine_sample('11-30-2021'))

if __name__=='__main__':
    main()