'''
example code to join dataframes
merge_by_FIPS doesn't need to be it's own file; it's just calling .join on two data frames
'''

from deaths import death_sample
from vaccines import vaccine_sample


def merge_by_FIPS(desired_date):
    # get dataframes with FIPS as indices
    deaths_df = death_sample(desired_date)
    vaccines_df = vaccine_sample(desired_date)
    # how=inner specifies that only the intersection of each dataframe will be used.
    merged = deaths_df.join(vaccines_df, how='inner')
    return merged


# main function is for testing only 
def main():
    print(merge_by_FIPS('11-30-2021'))

if __name__=='__main__':
    main()