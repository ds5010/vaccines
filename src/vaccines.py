# Sample one date from the source dataset and write it to an intermediate file
import pandas as pd

def time_sample(desired_date, cols = ["Series_Complete_18PlusPop_Pct", "Census2019_18PlusPop"]):
    # Source data
    input_filename = "./data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
    df = pd.read_csv(input_filename, index_col='FIPS', compression="gzip")
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
    df.sort_index()
    return df

def main():
    time_sample('11-30-2021')

if __name__=='__main__':
    main()