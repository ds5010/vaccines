death=pd.read_csv('final_data.csv',converters={'FIPS' : str})
death_columns=[ "Last_Update","Admin2","Province_State","Confirmed","Deaths","Incident_Rate","Case_Fatality_Ratio"]
death=death[death_columns]