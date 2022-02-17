import pandas as pd

desired_date = "11/30/2021"

filename = "COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
df = pd.read_csv(filename, compression="gzip", converters={'FIPS' : str})

# Filter by date
df = df[df["Date"] == desired_date]

# Extract columns of interest
columns = ["FIPS", "Recip_County", "Recip_State", "Series_Complete_18PlusPop_Pct", "Census2019_18PlusPop"]
df = df[columns]

# Clean the dataset (removes 184 rows if it's done on the entire dataset)
print(df.shape)
df = df.dropna()
print(df.shape)

# Write filtered dataframe to a file
df.to_csv("vaccines.csv", index=False)
