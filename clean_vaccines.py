import pandas as pd
input_filename = "COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
df = pd.read_csv(input_filename, compression="gzip", converters={'FIPS' : str})
print("START:", df.shape)

columns = ["FIPS", "Recip_County", "Recip_State", "Series_Complete_18Plus", "Census2019_18PlusPop", "Date"]
df = df[columns]


print("BEFORE:", df.shape)
df = df.dropna()
print("AFTER:", df.shape)

output_filename = "vaccinations-cleaned.csv"

df.to_csv(output_filename, index=False)
