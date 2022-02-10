import pandas as pd

col = "Series_Complete_5Plus"
desired_date = "02/01/2022"

filename = "data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz"
df = pd.read_csv(filename, compression="gzip")

# Filter by date
df = df[df["Date"] == "02/01/2022"] # .dropna()

# Print the total of one column
print("{} total: {:,.0f}".format(col, df[col].sum()))
