# Sample one date from the source dataset and write it to an intermediate file
from lib2to3.pgen2.pgen import DFAState
import pandas as pd

# Source data
def CDCdata(desired_date):
    input_filename = "./data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
    df = pd.read_csv(input_filename, compression="gzip", converters={'FIPS' : str})
    print("START:", df.shape)
    

    # Filter by date
    df = df[df["Date"] == desired_date]

    # Extract columns of interest
    columns = ["FIPS", "Recip_County", "Recip_State", "Series_Complete_18PlusPop_Pct", "Census2019_18PlusPop"]
    df = df[columns]

    # Clean the dataset (removes 62 rows for 11/30/2021)
    print("BEFORE:", df.shape)
    df = df.dropna()
    print("AFTER:", df.shape)

    # Output
    output_filename = "./data/CDC/vaccinations-" + desired_date[:2] + '-' + \
                    desired_date[3:5] + "-" + desired_date[6:11] + ".csv"

    # Write filtered dataframe to a file
    df.to_csv(output_filename, index=False)
    return df

def CDCdata_all():
    CDCdata('05/31/2021')
    CDCdata('06/30/2021')
    CDCdata('07/31/2021')
    CDCdata('08/31/2021')
    CDCdata('09/30/2021')
    CDCdata('10/31/2021')
    CDCdata('11/30/2021')
# CDCdata_all()

aaa=CDCdata('05/31/2021')
print(aaa)