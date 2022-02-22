import pandas as pd

vax_file = pd.read_csv("vaccinations-cleaned-with-months.csv", low_memory=False)

death_file = pd.read_csv("merged_deaths.csv", low_memory=False)

df = pd.merge(vax_file, death_file)

df.to_csv("vaccinations_and_deaths_file.csv")
