import pandas as pd
from pathlib import Path

#reading the csv file
cur_dir = Path(__file__).parent
csv_path = cur_dir.parent/"data"/"bestsellingbooks.csv"

df = pd.read_csv(csv_path)

#----------------------------------DATA CLEANING-----------------------------------------------
#removing white spaces
df["Name"] = df["Name"].str.strip()
df["Author"] = df["Author"].str.strip()
df["Genre"] = df["Genre"].str.strip()

#removing rows with any empty column entry
df = df.dropna()

#removing free kindle books i.e. price = 0
df = df[df["Price"] != 0]

#user rating limits
df = df[(df["User Rating"] >= 0.0) & (df["User Rating"] <= 5.0)]

df_duplicates = df[df.duplicated(subset=["Name"],keep=False)]
df_unique = df.drop_duplicates(subset=["Name"])
 
#---------------------------------------------ANALYSIS----------------------------------------------------
#BASELINE METRICS & MARKET SURVEY
print("="*100)
print("-"*100)
print(" AMAZON BESTSELLERS REAL-TIME DATA ANALYSIS REPORT(2009-2019) ".center(100,"-"))
print("-"*100)
print("="*100)
 
print("_"*80)
print("1. BASELINE METRICS & MARKET SURVEY")
print("_"*80)
 
print(f" #Total Unique Bestselling Books: {df_unique.shape[0]}")
print(f" #Total Unique Authors: {len(df_unique["Author"].unique().tolist())}\n")
print(f" #Average Bestseller Price: ${df_unique["Price"].mean():.2f}")
print(f" #Highest Price of a Bestseller: ${df_unique["Price"].max():.2f}")
print(f" #Lowest Price of a Bestseller: ${df_unique["Price"].min():.2f}\n")
print(f" #Global Average Consumer Rating: {df_unique["User Rating"].mean():.2f}")
print(f" #Average Review Per Book: {df_unique["Reviews"].mean():.2f}\n")

#GENRE COMPARISON
print("_"*80)
print("2. GENRE COMPARISON (FICTION v/s NON-FICTION)")
print("_"*80)

group = df_unique.groupby("Genre")
count = group["Name"].count()
print(f"Bestseller Market Share Split : Fiction: {(count["Fiction"]/df_unique["Genre"].count())*100:.2f}% | Non-Fiction: {(count["Non Fiction"]/df_unique["Genre"].count())*100:.2f}%\n")
 
rating = group["User Rating"].mean()
print(" #Average Ratings:")
print(f"└── FICTION : {rating["Fiction"]:.2f}")
print(f"└── NON-FICTION : {rating["Non Fiction"]:.2f}\n")
review = group["Reviews"].mean()
print(" #Average Consumer Reviews:")
print(f"└── FICTION : {review["Fiction"]:.2f}")
print(f"└── NON-FICTION : {review["Non Fiction"]:.2f}\n")
group =df_unique.groupby("Genre")
price = group["Price"].mean()
print(" #Average Pricing:")
print(f"└── FICTION : {price["Fiction"]:.2f}")
print(f"└── NON-FICTION : {price["Non Fiction"]:.2f}\n")

#Bestseller leaderboard
print("_"*80)
print("3. THE BESTSELLER LEADERBOARD")
print("_"*80)

print("TOP 5 PROLIFIC AUTHORS".center(30, "-"))
top = df_unique["Author"].value_counts().head(5).reset_index()
top.index = top.index +1
top.columns = ["Author", "Book Count"]
print(top)
print("-"*30)
print("\n")

print("TOP 3 MOST YEARS RETAINING BESTSELLER".center(65,"-"))
year = df_duplicates["Name"].value_counts().head(3).reset_index()
year.index = year.index +1
year.columns = ["Book", "No.Of Years"]
year["Book"] = year["Book"].map(lambda x: f"{str(x): <75}")
print(year.to_string(justify="left"))
print("-"*65)
print("\n")

#Market evolution
print("_"*80)
print("4. YEAR-WISE MARKET EVOLUTION")
print("_"*80)

table_data = []

for year, group in df_duplicates.groupby("Year"):
    max_rat = group.loc[group["User Rating"].idxmax()]
    max_rev = group.loc[group["Reviews"].idxmax()]
    
    row_dict = {
        "Year": year,
        "Max Rated Book": max_rat["Name"],
        "Rating": max_rat["User Rating"],
        "Max Reviewed Book": max_rev["Name"],
        "Reviews":  max_rev["Reviews"],
        "Price($)": max_rev["Price"]
    }
    table_data.append(row_dict)

df_temp = pd.DataFrame(table_data)
df_temp["Max Rated Book"] = df_temp["Max Rated Book"].map(lambda x: f"{str(x) :<100}")
df_temp["Rating"] = df_temp["Rating"].map(lambda x: f"{str(x) :<10}")
df_temp["Max Reviewed Book"] = df_temp["Max Reviewed Book"].map(lambda x: f"{str(x) :<100}")
print(df_temp.to_string(justify = "left", index= False))
print("\n")

#correlation
print("_"*80)
print("5. MATHEMATICAL DATA CORRELATIONS")
print("_"*80)
corr_matrix = df_unique[["Price", "Reviews", "User Rating"]].corr()
print(corr_matrix.round(2))