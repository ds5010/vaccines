import pandas as pd
import deaths
import vaccines


def merge_by_FIPS(desired_date):
    deaths_df = deaths.time_sample(desired_date)
    vaccines_df = vaccines.time_sample(desired_date)
    merged = deaths_df.join(vaccines_df, how='inner')
    print(merged)
    return merged
    
def main():
    merge_by_FIPS('11-30-2021')

if __name__=='__main__':
    main()