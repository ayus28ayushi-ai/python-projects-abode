
#removing rows with any empty entry
df = df.dropna(subset=["Name","Author","User Rating","Reviews","Price","Year","Genre"])
#removing white spaces
df["Name"] = df["Name"].str.strip()
df["Author"] = df["Author"].str.strip()
df["Genre"] = df["Genre"].str.strip()

#removing free kindle books i.e. price = 0
df = df[df["Price"] != 0]

#user rating limits
df = df[(df["User Rating"] >= 0.0) & (df["User Rating"] <= 5.0)]

df_duplicates = df[df.duplicated(subset=["Name"],keep=False)]
df_unique = df.drop_duplicates(subset=["Name"])